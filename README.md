# Expansor de Polinomios (Django + HTMX + MathJax)

Un proyecto web en Django que parsea y expande productos de polinomios, mostrando simultáneamente su expresión en LaTeX crudo y renderizada con MathJax, con **live-preview** instantáneo vía HTMX y posibilidad de historial de cálculos.

---

## Características destacadas

* **Parser** de expresiones con operadores `+`, `-`, `*`, `^` y paréntesis.
* **Modelo algebraico** que representa `Term` y `Polynomial` con operaciones de suma y multiplicación.
* **Transformer** que convierte un AST en un polinomio expandido.
* **Exportador LaTeX** para generar la cadena en sintaxis TeX.
* **Live-preview**: actualiza la expansión sin recargar la página (HTMX).
* **Raw + Render**: muestra la cadena LaTeX y su visualización con MathJax.
* **Historial opcional** de expresiones y resultados.
* **Estilos** modernos con Bootstrap y CSS personalizado.

---

## Requisitos

* **Python 3.11+**
* **Django 5.2+**
* **pip** (o pipenv/virtualenv)
* Acceso a Internet para cargar Bootstrap, HTMX y MathJax desde CDN

---

## Configuración inicial

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/TU_USUARIO/polyweb.git
   cd polyweb
   ```

2. **Crear y activar entorno virtual**

   * Linux/macOS:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   * Windows (PowerShell):

     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Aplicar migraciones de Django**

   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor**

   ```bash
   python manage.py runserver 8001
   ```

   Luego abre en tu navegador: `http://127.0.0.1:8001/`

---

## Estructura del proyecto

```
polyweb/
├── manage.py                 # Entrada de Django
├── polyweb/                  # Configuración global de Django
│   ├── settings.py           # Ajustes, INSTALLED_APPS, STATIC_URL...
│   └── urls.py               # Rutas principales
├── expander/                 # App de expansión de polinomios
│   ├── forms.py              # Formulario con validación
│   ├── views.py              # Vistas: expand_form y expand_ajax
│   ├── urls.py               # Rutas de la app
│   ├── templates/expander/   # Plantillas HTML
│   │   ├── form.html         # Interfaz principal con HTMX + MathJax
│   │   └── _result_fragment.html  # Fragmento parcial de resultado
│   ├── static/expander/      # Assets estáticos
│   │   ├── css/style.css     # Estilos personalizados
│   │   └── js/mathjax-config.js  # Config de MathJax
│   └── logic/                # Lógica de parseo y álgebra
│       ├── ast/              # Definición de nodos AST
│       ├── algebra/          # Modelos Term y Polynomial
│       ├── core/             # Parser y transformer
│       └── export/           # Exportador LaTeX
└── requirements-dev.txt      # Django, pytest, flake8, mypy, etc.
```

---

## Flujo de operación (visión de alto nivel)

Cada vez que el usuario escribe o pulsa **Expandir**, ocurre:

1. **HTMX** dispara una petición GET a `/ajax/expand/?expression=…` sin recargar.
2. **Vista AJAX** valida con `ExpandForm`, parsea y transforma la expresión.
3. **Parser → AST** tokeniza y construye el árbol de nodos.
4. **Transformer** convierte AST en `Polynomial`, expandiendo y normalizando términos.
5. **Exportador LaTeX** genera la cadena TeX legible.
6. **Fragmento parcial** (`_result_fragment.html`) se renderiza con raw y delimitadores LaTeX.
7. **HTMX** inyecta la respuesta en `#result-container`.
8. **MathJax** typesetPromise() formatea la ecuación en la página.

---

## Fases de desarrollo (Backend)

A continuación, **sin fragmentos de código**, el propósito de cada fase y cómo encajan:

### Fase 1: Entorno Django y App Base

* **Objetivo:** Crear el esqueleto de Django.
* **Función del código:** Configura el proyecto global (`settings.py`, `urls.py`), crea la app `expander` y establece la ruta inicial.
* **Concepto clave:** Separar el framework de la lógica de expansión.

### Fase 2: Formularios y Validación

* **Objetivo:** Capturar y validar la entrada.
* **Función del código:** Define un `Form` con un solo campo para la expresión, centraliza reglas de validación y prepara mensajes de error.
* **Concepto clave:** Desacoplar validación de la lógica de negocio.

### Fase 3: Parser y AST

* **Objetivo:** Convertir texto en estructura de datos.
* **Función del código:** Tokeniza la fórmula, respeta precedencias mediante un parser recursivo y construye un Árbol de Sintaxis Abstracta.
* **Concepto clave:** Transformar el string en un árbol de nodos manipulables.

### Fase 4: Modelo Algebraico

* **Objetivo:** Representar matemáticamente términos y polinomios.
* **Función del código:** Implementa `Term` y `Polynomial` con operaciones de suma y multiplicación, agrupando términos.
* **Concepto clave:** Separar la representación de datos de la lógica de parseo.

### Fase 5: Transformer AST → Polynomial

* **Objetivo:** Traducir el AST a la estructura algebraica.
* **Función del código:** Recorre el AST y aplica operaciones algebraicas para expandir la expresión.
* **Concepto clave:** Usar un visitor recursivo para ejecutar la expansión.

### Fase 6: Exportador LaTeX

* **Objetivo:** Crear la cadena en sintaxis LaTeX.
* **Función del código:** Recorre términos del polinomio, formatea coeficientes y exponentes, ajusta signos.
* **Concepto clave:** Mantener separada la lógica de negocio de la presentación.

### Fase 7: Integración en Vistas Django

* **Objetivo:** Orquestar el flujo en HTTP.
* **Función del código:** Las vistas reciben el formulario, validan y llaman a parser, transformer y exportador. La vista AJAX devuelve solo el fragmento de resultado.
* **Concepto clave:** Mantener la vista como punto de integración sin mezclar responsabilidades.

### Fase 8: Live-preview con HTMX (Opcional)

* **Objetivo:** Mejorar la UX con peticiones parciales.
* **Función del código:** HTMX dispara al escribir o clicar, actualiza solo el contenedor de resultados y muestra spinner.
* **Concepto clave:** Desacoplar la interacción parcial de la vista completa.

### Fase 9: Testing y Calidad

* **Objetivo:** Garantizar estabilidad y evolución.
* **Función del código:** Tests unitarios e integración para todas las piezas; CI con linters y type checks.
* **Concepto clave:** Adoptar pruebas y QA desde el inicio.



## Extensiones y mejoras posibles

* **Historial** completo almacenado en DB o sesión.
* **Multiplicación implícita** (`2x`, `(x+1)(x-1)`).
* **Exponentes** negativos o fraccionarios.
* **API REST** para consumo externo.
* **Autenticación** y limitación por usuario.
* **Despliegue** con Docker y CI/CD.

---

