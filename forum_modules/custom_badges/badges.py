from django.utils.translation import ugettext as _

from base import AbstractTagBadge


class BasicTagBadge(AbstractTagBadge):

    abstract = True
    
    def award_to(self, action):
        author = super(BasicTagBadge, self).award_to(action)
        question = action.node.parent
        if question and self.get_tag_name() in question.tagname_list():
            return author


class JavaScriptBasicBadge(BasicTagBadge):
    _name = "JavaScript Basic"


