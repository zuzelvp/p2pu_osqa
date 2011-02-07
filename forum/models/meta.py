from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator

from base import *


class Vote(models.Model):
    user = models.ForeignKey(User, related_name="votes")
    node = models.ForeignKey(Node, related_name="votes")
    value = models.SmallIntegerField()
    action = models.OneToOneField(Action, related_name="vote")
    voted_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = 'forum'
        unique_together = ('user', 'node')


class Flag(models.Model):
    user = models.ForeignKey(User, related_name="flags")
    node = models.ForeignKey(Node, related_name="flags")
    reason = models.CharField(max_length=300)
    action = models.OneToOneField(Action, related_name="flag")
    flagged_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = 'forum'
        unique_together = ('user', 'node')

class BadgesQuerySet(models.query.QuerySet):
    def get(self, *args, **kwargs):
        try:
            pk = [v for (k,v) in kwargs.items() if k in ('pk', 'pk__exact', 'id', 'id__exact')][0]
        except:
            return super(BadgesQuerySet, self).get(*args, **kwargs)

        from forum.badges.base import BadgesMeta
        badge = BadgesMeta.by_id.get(int(pk), None)
        if not badge:
            return super(BadgesQuerySet, self).get(*args, **kwargs)
        return badge.ondb


class BadgeManager(models.Manager):
    use_for_related_fields = True

    def get_query_set(self):
        return BadgesQuerySet(self.model)

class Badge(models.Model):
    GOLD = 1
    SILVER = 2
    BRONZE = 3

    type        = models.SmallIntegerField()
    cls         = models.CharField(max_length=50, null=True)
    awarded_count = models.PositiveIntegerField(default=0)
    
    awarded_to    = models.ManyToManyField(User, through='Award', related_name='badges')

    objects = BadgeManager()

    @property
    def name(self):
        CustomBadge.load_custom_badges()
        cls = self.__dict__.get('_class', None)
        return cls and cls.name or _("Unknown")

    @property
    def description(self):
        CustomBadge.load_custom_badges()
        cls = self.__dict__.get('_class', None)
        return cls and cls.description or _("No description available")

    @models.permalink
    def get_absolute_url(self):
        return ('badge', [], {'id': self.id, 'slug': slugify(self.name)})

    def save(self, *args, **kwargs):
        if isinstance(self.awarded_count, models.expressions.ExpressionNode):
            super(Badge, self).save(*args, **kwargs)
            self.awarded_count = self.__class__.objects.filter(id=self.id).values_list('awarded_count', flat=True)[0]
        else:
            super(Badge, self).save(*args, **kwargs)


    class Meta:
        app_label = 'forum'


class Award(models.Model):
    user = models.ForeignKey(User)
    badge = models.ForeignKey('Badge', related_name="awards")
    node = models.ForeignKey(Node, null=True)

    awarded_at = models.DateTimeField(default=datetime.datetime.now)

    trigger = models.ForeignKey(Action, related_name="awards", null=True)
    action = models.OneToOneField(Action, related_name="award")


    class Meta:
        unique_together = ('user', 'badge', 'node')
        app_label = 'forum'


class CustomBadge(models.Model):

    name_help = _('Badge names can only include letters and spaces. Please, do not include the word badge at the end of the name.')
    name_validator = RegexValidator(r'^[a-zA-z][a-zA-Z ]*$', name_help)
    name = models.CharField(max_length=100, unique=True, validators=[name_validator], help_text=name_help)
    description = models.TextField(help_text=_('Short description of the badge.'))
    tag = models.ForeignKey('Tag', editable=False)
    ondb = models.ForeignKey('Badge', editable=False)

    min_required_votes = models.PositiveIntegerField(help_text=_('Minimun number of votes required to be awarded.'),
        default=0)

    response_prerequisites = models.ManyToManyField('CustomBadge', symmetrical=False, related_name='next_level_badges',
        help_text=_("Badges required before a user is allowed to submit a response."), null=True, blank=True)

    owners = models.ManyToManyField(User, related_name='badges_managed', null=True, blank=True,
        help_text=_("Badge owners have the same voting priviledges as any user with the badge."))

    voting_restricted = models.BooleanField(help_text="If checked, only users with the badge (or the badge owners) will be allowed to vote.", default=False)

    class Meta:
        app_label = 'forum'

    def __unicode__(self):
        return self.ondb.name

    @property
    def tag_name(self):
        words = self.name.strip().lower().split() + ['badge']
        return "-".join(words)

    @property
    def class_name(self):
        words = self.name.strip().split() + ['CustomBadge']
        return "".join(words)

    def save(self, *args, **kwargs):
        if self.id:
            self._edit_custom_badge()
        else:
            self._create_custom_badge()
        super(CustomBadge, self).save(*args, **kwargs)

    def _create_custom_badge(self):
        from forum.models import Tag, Badge
        try:
            self.tag = Tag.objects.get(name=self.tag_name)
        except Tag.DoesNotExist:
            self.tag = Tag.objects.create(name=self.tag_name)
        self.tag_id = self.tag.id
        self.ondb = Badge.objects.create(cls=self.class_name, type=Badge.BRONZE)
        self.ondb_id = self.ondb.id
        self._register_custom_badge()

    def _edit_custom_badge(self):
        self.tag.name = self.tag_name
        self.tag.save()
        self.ondb.cls = self.class_name
        self.ondb.save()
        old = CustomBadge.objects.get(pk=self.pk)
        for node in old.tag.nodes.all():
            new_tags = node.tagnames.replace(old.tag_name, self.tag_name)
            node.tagnames = new_tags
            node.save()
            node.active_revision.tagnames = new_tags
            node.active_revision.save()
        for user in old.ondb.awarded_to.all():
            for msg in user.message_set.all():
                msg.message = msg.message.replace(old.name, self.name)
                msg.save()
        from forum.badges.base import BadgesMeta
        if old.class_name in BadgesMeta.by_class:
            del BadgesMeta.by_class[old.class_name]
        self._register_custom_badge()

    def _register_custom_badge(self):
        from forum.badges.base import BadgesMeta
        BadgesMeta.by_id[self.ondb.id] = self
        self.ondb.__dict__['_class'] = self
        BadgesMeta.by_class[self.class_name] = self
        from forum.actions import VoteUpAction, VoteDownAction
        self._hook(VoteUpAction)
        self._hook(VoteDownAction)

    def _hook(self, action_cls):
        from forum.models import Action
        if not Action.hooks.get(action_cls, None):
            Action.hooks[action_cls] = []
        hooks = Action.hooks[action_cls]
        if not CustomBadge.procces_voting_action in hooks: 
            hooks.append(CustomBadge.procces_voting_action)

    @classmethod
    def load_custom_badges(cls):
        for badge in CustomBadge.objects.all():
            badge._register_custom_badge()

    @classmethod
    def procces_voting_action(cls, action, new):
        if action.node.node_type == 'answer':
            answer = action.node
            question = answer.parent
            user = action.node.author
            for name in question.tagname_list():
                try:
                    badge = CustomBadge.objects.get(tag__name=name)
                except CustomBadge.DoesNotExist:
                    continue
                if badge.min_required_votes < 1 or answer.score < badge.min_required_votes:
                    continue
                from forum.badges.base import award_badge
                award_badge(badge.ondb, user, action, False)

    @classmethod
    def is_response_restricted(cls, user, question):
        for name in question.tagname_list():
            try:
                badge = CustomBadge.objects.get(tag__name=name)
            except CustomBadge.DoesNotExist:
                continue
            for prerequisite in badge.response_prerequisites.all():
                if not user.is_authenticated or not user.badges.filter(cls=prerequisite.ondb.cls):
                    return True
        return False

    @classmethod
    def is_voting_restricted(cls, user, answer):
        for name in answer.parent.tagname_list():
            try:
                badge = CustomBadge.objects.get(tag__name=name)
            except CustomBadge.DoesNotExist:
                continue
            if badge.voting_restricted:
                if not user.is_authenticated():
                    return True
                if badge.owners.filter(username=user.username):
                    continue
                if not user.badges.filter(cls=badge.ondb.cls):
                    return True
        return False


