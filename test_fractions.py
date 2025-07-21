#!/usr/bin/env python3
"""
Script de prueba para verificar que el parser de fracciones funcione correctamente
"""

import sys
import os

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from expander.logic.core.parser import parse
from expander.logic.core.transformer import to_polynomial
from expander.logic.export.latex import polynomial_to_latex

def test_expression(expr):
    print(f"\n--- Probando: {expr} ---")
    try:
        # Parser
        ast = parse(expr)
        print(f"AST: {ast}")
        
        # Transformer
        poly = to_polynomial(ast)
        print(f"Polinomio: {poly}")
        
        # LaTeX
        latex = polynomial_to_latex(poly)
        print(f"LaTeX: {latex}")
        
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    print("=== Pruebas del Parser con Fracciones ===")
    
    # Casos de prueba
    test_cases = [
        # Fracciones básicas
        "1/2",
        "3/4",
        "1/2 * x",
        "(1/2) * x",
        "1/2 * x + 1/3 * y",
        
        # Productos con fracciones
        "(1/2 * x + 1) * (x - 1)",
        "(1/3 * x + 2) * (2 * x - 1/2)",
        "(1/2 * x + 1/3) * (x - 1/4)",
        
        # Casos mixtos
        "2 * x + 1/2",
        "(x + 1/2)^2",
        
        # Casos complejos
        "(1/2 * x + 1/3 * y) * (2 * x - 1/4 * y)",
    ]
    
    successful = 0
    total = len(test_cases)
    
    for expr in test_cases:
        if test_expression(expr):
            successful += 1
    
    print(f"\n=== Resumen ===")
    print(f"Pruebas exitosas: {successful}/{total}")
    
    if successful == total:
        print("¡Todas las pruebas pasaron! ✅")
    else:
        print(f"Faltan {total - successful} pruebas por corregir ❌")
