def sanitizar():

    # Prefijos 
    prefixies = ["la", "el", "las", "los", "de", "la", "las", "los", "precio de", "clima en", "clima de"]
    
    # Entrada en Min
    name = name.lower()

    changed = True
    while changed:
        changed = False
        for p in prefixies:
            if name.startswith(p):
                name = name[len(p):].strip()
                changed = True

    return name 
