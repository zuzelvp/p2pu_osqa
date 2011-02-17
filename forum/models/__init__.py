import forum.utils.djangofix
from question import Question ,QuestionRevision, QuestionSubscription
from answer import Answer, AnswerRevision
from tag import Tag, MarkedTag
from user import User, ValidationHash, AuthKeyUserAssociation, SubscriptionSettings
from node import Node, NodeRevision, NodeState, NodeMetaClass
from comment import Comment, VoteComment, AwardComment
from action import Action, ActionRepute
from meta import Vote, Flag, Badge, Award, CustomBadge
from utils import KeyValue
from page import Page

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r"^forum\.models\.\w+\.\w+"])
except:
    pass

from base import *

__all__ = [
        'Node', 'NodeRevision', 'NodeState',  
        'Question', 'QuestionSubscription', 'QuestionRevision',
        'Answer', 'AnswerRevision',
        'Tag', 'Comment', 'VoteComment', 'AwardComment', 'MarkedTag', 'Badge', 'Award', 'CustomBadge',
        'ValidationHash', 'AuthKeyUserAssociation', 'SubscriptionSettings', 'KeyValue', 'User',
        'Action', 'ActionRepute', 'Vote', 'Flag', 'Page'
        ]


from forum.modules import get_modules_script_classes

for k, v in get_modules_script_classes('models', models.Model).items():
    if not k in __all__:
        __all__.append(k)
        exec "%s = v" % k

NodeMetaClass.setup_relations()
BaseMetaClass.setup_denormalizes()
