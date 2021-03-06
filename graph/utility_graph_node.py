from uuid import uuid4
from graph.exceptions import NodeConnectionError


class UtilityGraphNode:
    """The base class for all utility graph nodes"""
    def __init__(self):
        self.max_inputs = 1
        self.connected_inputs = []
        self.id = str(uuid4())
        self._output = None

    @property
    def output(self):
        """Get the output value of this node"""
        return self._output

    def connect_input(self, node):
        """Connect another UtilityGraphNode as an input to this node"""
        if len(self.connected_inputs) + 1 <= self.max_inputs:
            self.connected_inputs.append(node)
        else:
            raise NodeConnectionError()

    def reset(self):
        self._output = None
        for i in self.connected_inputs:
            i.reset()
