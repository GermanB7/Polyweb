from expander.logic.algebra.term import Term
from expander.logic.algebra.polynomial import Polynomial

def term_to_str(term:Term)->str:
    coeff = term.coeff
    
    # Manejar fracciones en el coeficiente
    if coeff.denominator == 1:
        # Es un entero
        coeff_int = coeff.numerator
        if term.exponents and abs(coeff_int)==1:
            coeff_str = "-" if coeff_int<0 else ""
        else:
            coeff_str = str(coeff_int)
    else:
        # Es una fracción
        if term.exponents and coeff.numerator == 1:
            coeff_str = f"\\frac{{1}}{{{coeff.denominator}}}"
        elif term.exponents and coeff.numerator == -1:
            coeff_str = f"-\\frac{{1}}{{{coeff.denominator}}}"
        else:
            coeff_str = f"\\frac{{{coeff.numerator}}}{{{coeff.denominator}}}"
    
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
