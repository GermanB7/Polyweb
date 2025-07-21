from expander.logic.ast.nodes import Node, Const, Var, Add, Mul, Pow
from expander.logic.algebra.term import Term
from expander.logic.algebra.polynomial import Polynomial

def to_polynomial(node:Node) -> Polynomial:
    if isinstance(node, Const):
        return Polynomial([Term(node.value,{})])
    if isinstance(node, Var):
        return Polynomial([Term(1,{node.name:1})])
    if isinstance(node, Add):
        return to_polynomial(node.left) + to_polynomial(node.right)
    if isinstance(node, Mul):
        return to_polynomial(node.left) * to_polynomial(node.right)
    if isinstance(node, Pow):
        base = to_polynomial(node.base)
        result = Polynomial([Term(1,{})])
        for _ in range(node.exp):
            result = result * base
        return result
    raise ValueError(f"Nodo desconocido {node}")
