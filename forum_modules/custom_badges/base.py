from django.utils.translation import ugettext as _

from forum.badges.base import BadgesMeta
from forum.models.tag import Tag
from forum_modules.default_badges.badges import AnswerScoreBadge

import settings


class TagBadgesMeta(BadgesMeta):

    def __new__(cls, name, bases, dic):
        badge = BadgesMeta.__new__(cls, name, bases, dic)
        if badge.tag_name:
            Tag.objects.get_or_create(name=badge.tag_name)
        return badge

    @property
    def tag_name(cls):
        """Get the tag name associated to this badge."""
        if hasattr(cls, '_name') and cls._name:
            words = cls._name.lower().split()
            words.append('badge')
            return "-".join(words)


class AbstractTagBadge(AnswerScoreBadge):

    __metaclass__ = TagBadgesMeta

    abstract = True
    expected_score = settings.PEER_ASSESSMENT_VOTES_UP

    @property
    def description(self):
        return _('Answer received %s badge.') % self.name

    @property
    def name(self):
        """Get translated name."""
        return _(self._name)

    def get_tag_name(self):
        return self.__class__.tag_name
