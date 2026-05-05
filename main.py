import re

def chatbot():
    print("*** Chatbot v1.0.0 Iniciando ***")
    print("Hola soy el chatbot v1.0.0, Puedo ayudarte a obtener información sobre precios de acciones y clima de ciudades")
    print("¿Qué quieres saber hoy?")

    # Ciclo infinito para mantener el chatbot corriendo
    while True:
        try:
            user_input = input("-->").strip()
            if not user_input:
                continue

            # Validar una peticion de salida
            if user_input.lower() in ["salir", "adiós", "chao", "bye", "exit"]:
                print("Chatbot: ¡Hasta luego!")
                break
            # Reglas para detectar intencion de preguntas por acciones

            stock_match = re.search(r"(?:precio|stock|accion|acción)\s+(?:de\s, de la|de las)\s+(\w+)", user_input, re.IGNORECASE)

            # Reglas para detectar intencion de preguntas por clima
            weather_match = re.search(r"(?:clima|tiempo)\s+(?:en|de)\s+(\w+)", user_input, re.IGNORECASE)

            #Caso 1: El usuario pregunta por acciones
            if stock_match:
                # Debemos esperar si el usario indica alguna accion
                price = obtener_precio_accion(None, user_input)
                if price:
                    print(f">> {price}")
                else:
                    print("Chatbot: No pude obtener el precio, ¿podrías intentar con otra acción?")

            # Caso 2: El usuario pregunta por clima
            if weather_match:
                temp = obtener_temperatura(None, user_input)
                if temp:
                    print(f">> {temp}")
                else:
                    print("Chatbot: No pude obtener la temperatura, ¿podrías intentar con otra ciudad?")

            # Caso 3: El usuario no ejecuta alguna peticion 
            else:
                print("Chatbot: No entendí tu petición. ¿Podrías replantearla?")

        except KeyboardInterrupt:
            # Comando de salida Ctrl + C | Cmd + C
            print("\nChatbot: Hasta luego, fue un placer ayudarte")






            
