from django import forms

class ExpandForm(forms.Form):
    expression = forms.CharField(
        label="Fórmula",
        max_length=200,
        widget=forms.TextInput(attrs={
            "placeholder": "(x+1)*(x-1)",
            "size": "40",
        }),
    )

    def clean_expression(self):
        expr = self.cleaned_data["expression"].strip()
        if not expr:
            raise forms.ValidationError("La expresión no puede estar vacía.")
        # Quizá quieras añadir validación extra, p.ej. sólo caracteres permitidos
        # if re.search(r"[^0-9A-Za-z\+\-\*\^\(\)xyzt ]", expr):
        #     raise forms.ValidationError("Caracteres no permitidos.")
        return expr
