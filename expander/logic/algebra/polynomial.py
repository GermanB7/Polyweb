from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from .term import Term
from .fraction import Fraction

@dataclass
class Polynomial:
    terms: list[Term]

    def __post_init__(self):
        grouped: dict[tuple[tuple[str,int],...], Fraction] = defaultdict(lambda: Fraction(0, 1))
        for t in self.terms:
            key = tuple(sorted((v,e) for v,e in t.exponents.items() if e!=0))
            grouped[key] = grouped[key] + t.coeff
        self.terms = [
            Term(coeff, dict(key))
            for key, coeff in grouped.items() if not coeff.is_zero()
        ]
        self.terms.sort(key=lambda t: (-sum(t.exponents.values()), tuple(sorted(t.exponents.items()))))

    def __add__(self, other: Polynomial) -> Polynomial:
        return Polynomial(self.terms + other.terms)

    def __mul__(self, other: Polynomial) -> Polynomial:
        prods: list[Term] = []
        for a in self.terms:
            for b in other.terms:
                new_coeff = a.coeff * b.coeff
                exps = {**a.exponents}
                for v,e in b.exponents.items():
                    exps[v] = exps.get(v,0) + e
                prods.append(Term(new_coeff, exps))
        return Polynomial(prods)

    def __repr__(self) -> str:
        if not self.terms:
            return "0"
        return " + ".join(repr(t) for t in self.terms).replace("+ -", "- ")
