def sanitizar(name):
    """
    Limpia y normaliza el input del usuario eliminando artículos, preposiciones y palabras clave 
    que no forman parte del nombre del sujeto de búsqueda (ej. el nombre de una empresa).
    
    Argumentos:
        name (str): Cadena de texto a sanitizar.
        
    Retorna:
        str: El nombre del sujeto extraído y limpio.
    """
    # Lista de prefijos que queremos omitir para aislar el nombre real (ej. "precio de apple" -> "apple")
    prefixes = [
        'la ', 'el ', 'de ', 'acción ', 'accion ', 
        'precio de ', 'precio ', 'stock de ', 'stock ',
        'valor de ', 'valor '
    ]
    
    # Convertir a minúsculas y quitar espacios en los extremos
    name = name.lower().strip()
    
    changed = True
    # Bucle para eliminar prefijos de forma iterativa 
    # Esto permite manejar casos como "la accion de apple" eliminando primero "la accion de " y luego el espacio sobrante.
    while changed:
        changed = False
        for p in prefixes:
            if name.startswith(p):
                name = name[len(p):].strip()
                changed = True
                
    return name
