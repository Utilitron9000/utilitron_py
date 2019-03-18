from graph.score_node import ScoreNode


class DecisionFactorNode(ScoreNode):
    """Node representing a decision factor
    that is determined from game statistics.
    Decision factors help to add semantics
    to the utility graph"""
    def __init__(self, name: str):
        super().__init__(name)
