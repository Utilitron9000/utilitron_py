from .score_node import ScoreNode

class DecisionFactorNode(ScoreNode):
    """Node representing a possible action available to the agent"""
    def __init__(self, name: str):
        ScoreNode.__init__(self, name)
