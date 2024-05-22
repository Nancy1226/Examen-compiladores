import re
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        user_input = request.form['input'].strip()
        parts = user_input.split(maxsplit=1)
        if len(parts) == 2:
            tipo, valor = parts
            if re.match(r'^\d+(\.\d+)?$', valor):  # Verificar si valor es un número decimal
                valor_decimal = float(valor)
                iva = valor_decimal * 1.16
                num = iva - valor_decimal
                total = valor_decimal + iva
                result = (tipo, valor_decimal, num, iva, total)
            else:
                error = "El valor del producto debe ser un número decimal."
        else:
            error = "Entrada inválida. Asegúrate de ingresar en el formato 'producto valor'."

    return render_template('home.html', result=result, error=error)