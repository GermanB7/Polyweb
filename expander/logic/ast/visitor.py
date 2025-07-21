from .nodes import Node

class NodeVisitor:
    def visit(self, node: Node):
        method = f"visit_{type(node).__name__}"
        visitor = getattr(self, method, None)
        if not visitor:
            raise NotImplementedError(f"No visit_{type(node).__name__} in {self}")
        return visitor(node)
