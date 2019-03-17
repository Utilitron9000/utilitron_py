class NodeNotFoundError(Exception):
    """Exception thrown when trying
    to perform an operation on a
    non-existent node"""
    pass


class NodeConnectionError(Exception):
    """Exception thrown when an invalid connection is attempted"""
    pass


class NodeTypeError(Exception):
    """Exception thrown when trying to perform
    an operation on a node type that does not
    support it"""
    pass
