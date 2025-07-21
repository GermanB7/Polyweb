from expander.logic.ast.nodes import Node, Const, Frac, Var, Add, Mul, Pow
from expander.logic.algebra.term import Term
from expander.logic.algebra.polynomial import Polynomial
from expander.logic.algebra.fraction import Fraction

def to_polynomial(node:Node) -> Polynomial:
    if isinstance(node, Const):
        return Polynomial([Term(Fraction.from_int(node.value),{})])
    if isinstance(node, Frac):
        return Polynomial([Term(Fraction(node.numerator, node.denominator),{})])
    if isinstance(node, Var):
        return Polynomial([Term(Fraction.from_int(1),{node.name:1})])
    if isinstance(node, Add):
        return to_polynomial(node.left) + to_polynomial(node.right)
    if isinstance(node, Mul):
        return to_polynomial(node.left) * to_polynomial(node.right)
    if isinstance(node, Pow):
        base = to_polynomial(node.base)
        result = Polynomial([Term(Fraction.from_int(1),{})])
        for _ in range(node.exp):
            result = result * base
        return result
    raise ValueError(f"Nodo desconocido {node}")
