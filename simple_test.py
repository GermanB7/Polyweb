#!/usr/bin/env python3
"""
Script de prueba simple para verificar cada componente
"""

import sys
import os

# Agregar el directorio del proyecto al path
project_root = os.path.dirname(__file__)
sys.path.insert(0, project_root)

print("=== Probando la clase Fraction ===")
try:
    from expander.logic.algebra.fraction import Fraction
    
    # Pruebas básicas
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print("✅ Fraction funciona correctamente")
except Exception as e:
    print(f"❌ Error con Fraction: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Probando el parser ===")
try:
    from expander.logic.core.parser import parse
    
    # Probar expresiones simples
    ast = parse("1/2")
    print(f"AST de '1/2': {ast}")
    
    ast = parse("1/2 * x")
    print(f"AST de '1/2 * x': {ast}")
    print("✅ Parser funciona correctamente")
except Exception as e:
    print(f"❌ Error con Parser: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Probando transformer ===")
try:
    from expander.logic.core.transformer import to_polynomial
    
    ast = parse("1/2")
    poly = to_polynomial(ast)
    print(f"Polinomio de '1/2': {poly}")
    print("✅ Transformer funciona correctamente")
except Exception as e:
    print(f"❌ Error con Transformer: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Probando exportador LaTeX ===")
try:
    from expander.logic.export.latex import polynomial_to_latex
    
    ast = parse("1/2")
    poly = to_polynomial(ast)
    latex = polynomial_to_latex(poly)
    print(f"LaTeX de '1/2': {latex}")
    print("✅ Exportador LaTeX funciona correctamente")
except Exception as e:
    print(f"❌ Error con LaTeX: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Prueba completa ===")
try:
    expr = "(1/2 * x + 1) * (x - 1)"
    print(f"Expresión: {expr}")
    
    ast = parse(expr)
    print(f"AST: {ast}")
    
    poly = to_polynomial(ast)
    print(f"Polinomio: {poly}")
    
    latex = polynomial_to_latex(poly)
    print(f"LaTeX: {latex}")
    
    print("✅ ¡Todo funciona correctamente!")
except Exception as e:
    print(f"❌ Error en prueba completa: {e}")
    import traceback
    traceback.print_exc()
