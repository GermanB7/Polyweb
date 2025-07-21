from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from expander.forms import ExpandForm
from expander.logic.core.parser import parse
from expander.logic.core.transformer import to_polynomial
from expander.logic.export.latex import polynomial_to_latex


def expand_form(request):
    """
    Vista principal: muestra el formulario y, al hacer POST,
    renderiza de forma clásica toda la página con el resultado.
    """
    result: str | None = None
    form = ExpandForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        expr = form.cleaned_data["expression"]
        try:
            ast = parse(expr)
            poly = to_polynomial(ast)
            result = polynomial_to_latex(poly)
        except Exception as e:
            form.add_error(None, f"Error al procesar la expresión: {e}")

    return render(request, "expander/form.html", {
        "form": form,
        "result": result,
    })


def expand_ajax(request):
    """
    Vista para HTMX: recibe GET con el parámetro 'expression',
    procesa y devuelve solo el fragmento HTML con errores o resultado.
    """
    form = ExpandForm(request.GET or None)
    result: str | None = None

    if form.is_valid():
        expr = form.cleaned_data["expression"]
        try:
            ast = parse(expr)
            poly = to_polynomial(ast)
            result = polynomial_to_latex(poly)
        except Exception as e:
            form.add_error(None, f"Error al procesar la expresión: {e}")

    # Renderizamos solo el fragmento parcial
    fragment = render_to_string(
        "expander/_result_fragment.html",
        {"form": form, "result": result},
        request=request
    )
    return HttpResponse(fragment)
