from string import ascii_lowercase as letras

def itemize(xs: list) -> list[str]:
    """
    ['primero', 'segundo', 'tercero', ... -> ['(a) primero', '(b) segundo', '(c) tercero', ...
    """
    return [f'{a} {b}' for a,b in zip((f'({x})' for x in letras), xs)]

def obtener_claves_con_prefijo(diccionario, prefijo):
    return [k for k in diccionario.keys() if k.startswith(prefijo)]