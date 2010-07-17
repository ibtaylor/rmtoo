#
# Requirement Management Toolset
#
#  Requirement Tag Class for Topic
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqTopic(ReqTagGeneric):
    tag = "Topic"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Name) is mandatory
        self.check_mandatory_tag(rid, req, 9)

        t = req[self.tag]
        del req[self.tag]
        return self.tag, t