#!/usr/bin/env python3
"""
Debug script para probar expresiones específicas
"""

import sys
import os

# Agregar el directorio del proyecto al path
project_root = os.path.dirname(__file__)
sys.path.insert(0, project_root)

def debug_expression(expr):
    print(f"\n=== Debugging: '{expr}' ===")
    
    try:
        from expander.logic.core.parser import parse
        print("1. Parser importado ✅")
        
        print(f"2. Parseando '{expr}'...")
        ast = parse(expr)
        print(f"   AST: {ast} ✅")
        
        from expander.logic.core.transformer import to_polynomial
        print("3. Transformer importado ✅")
        
        print("4. Convirtiendo a polinomio...")
        poly = to_polynomial(ast)
        print(f"   Polinomio: {poly} ✅")
        
        from expander.logic.export.latex import polynomial_to_latex
        print("5. Exportador LaTeX importado ✅")
        
        print("6. Convirtiendo a LaTeX...")
        latex = polynomial_to_latex(poly)
        print(f"   LaTeX: {latex} ✅")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR en paso: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Probar la expresión problemática
    expressions = [
        "1/2",                  # Fracción simple
        "1 + 1/2",             # Suma con fracción  
        "1/2 * x",             # Multiplicación simple
        "(1 + 1/2)",           # Paréntesis simples
        "(1 + 1/2) * x"        # Expresión completa
    ]
    
    for expr in expressions:
        if not debug_expression(expr):
            print(f"⛔ Deteniendo en expresión problemática: '{expr}'")
            break
    
    print("\n=== Debug completado ===")
