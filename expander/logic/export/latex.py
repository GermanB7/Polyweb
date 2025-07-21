from expander.logic.algebra.term import Term
from expander.logic.algebra.polynomial import Polynomial

def term_to_str(term:Term)->str:
    coeff = term.coeff
    # si exponents != {} y |coeff|==1 → omitimos '1'
    if term.exponents and abs(coeff)==1:
        coeff_str = "-" if coeff<0 else ""
    else:
        coeff_str = str(coeff)
    parts = [coeff_str]
    for v,e in sorted(term.exponents.items()):
        if e==0: continue
        if e==1:
            parts.append(v)
        else:
            parts.append(f"{v}^{{{e}}}")
    return "".join(parts)

def polynomial_to_latex(poly:Polynomial)->str:
    if not poly.terms: return "0"
    segs = [term_to_str(t) for t in poly.terms]
    return " + ".join(segs).replace("+ -","- ")
