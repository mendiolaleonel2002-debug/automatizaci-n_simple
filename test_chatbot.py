from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima

def test_chatbot():
    """
    Script de prueba para verificar que las funciones del agente 
    sigan funcionando correctamente después del refactor.
    """
    print("--- Iniciando Pruebas de Funciones ---")
    
    print("\n[Prueba] Precio de acción para Microsoft...")
    msft_price = obtener_precio_accion(None, "Microsoft")
    print(f"Resultado Microsoft: {msft_price}")


if __name__ == "__main__":
    test_chatbot()