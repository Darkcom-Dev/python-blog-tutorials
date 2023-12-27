import sys

sys.path.append('..')

from blog_tutrorials.juramento_prueba import juramento

def test_juramento():
    # Captura la salida de la función juramento()
    from io import StringIO
    import sys
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    juramento()
    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    # Comprueba si la salida es la esperada
    expected_output = "Juramento Turiano\n"
    assert output == expected_output, f"La salida esperada era '{expected_output}', pero se obtuvo '{output}'"

test_juramento()