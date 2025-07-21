from django import forms

class ExpandForm(forms.Form):
    expression = forms.CharField(
        label="Fórmula",
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "(1/2*x+1)*(x-1/3)",
            "id": "id_expression",
        }),
    )

    def clean_expression(self):
        expr = self.cleaned_data["expression"].strip()
        if not expr:
            raise forms.ValidationError("La expresión no puede estar vacía.")
        # Validar que solo contenga caracteres permitidos (incluyendo "/")
        # if re.search(r"[^0-9A-Za-z\+\-\*\^\(\)xyzt /]", expr):
        #     raise forms.ValidationError("Caracteres no permitidos.")
        return expr
