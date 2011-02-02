from forum.settings import BADGES_SET
from forum.settings.base import Setting
from django.utils.translation import ugettext_lazy as _


PEER_ASSESSMENT_VOTES_UP = Setting('PEER_ASSESSMENT_VOTES_UP', 3, BADGES_SET, dict(
label = _("Peer assessment up votes"),
help_text = _("""
Number of peer up votes required to award a tag badge.
""")))
