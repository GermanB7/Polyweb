from django.shortcuts import render
from expander.forms import ExpandForm
from expander.logic.core.parser import parse
from expander.logic.core.transformer import to_polynomial
from expander.logic.export.latex import polynomial_to_latex

def expand_form(request):
    result: str | None = None
    form = ExpandForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        expr = form.cleaned_data["expression"]
        try:
            ast = parse(expr)
            poly = to_polynomial(ast)
            result = polynomial_to_latex(poly)
        except Exception as e:
            # Asigna un error non-field al formulario
            form.add_error(None, f"Error al procesar la expresión: {e}")

    return render(request, "expander/form.html", {
        "form": form,
        "result": result,
    })
