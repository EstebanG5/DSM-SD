
# Cliente que accede y modifica la variable compartida

import requests
import json
import time

# La URL de acceso es el nombre del servicio ('nodo1') y su puerto (5000)
SERVER_URL = "http://nodo1:5000/value"
NODE_NAME = "nodo2"

def get_current_value():
    """Lee el valor actual."""
    print(f"\n[{NODE_NAME}] Intentando LEER el valor actual...")
    try:
        response = requests.get(SERVER_URL, timeout=5)
        response.raise_for_status() # Lanza excepción para errores HTTP
        data = response.json()
        print(f"[{NODE_NAME}] Lectura exitosa. Valor actual en DSM: {data['value']}")
        return data['value']
    except requests.exceptions.RequestException as e:
        print(f"[{NODE_NAME}] Error al leer: {e}")
        return None

def set_new_value(new_val):
    """Escribe un nuevo valor."""
    print(f"\n[{NODE_NAME}] Intentando ESCRIBIR el valor {new_val}...")
    try:
        headers = {'Content-Type': 'application/json'}
        payload = {"new_value": new_val}
        
        response = requests.post(SERVER_URL, headers=headers, data=json.dumps(payload), timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"[{NODE_NAME}] Escritura exitosa. Nuevo valor confirmado: {data['new_value']}")
    except requests.exceptions.RequestException as e:
        print(f"[{NODE_NAME}] Error al escribir: {e}")

if __name__ == "__main__":
    # La simulación del ciclo de vida del nodo 2
    
    # 1. Leer el valor inicial
    valor_actual = get_current_value()
    
    # 2. Modificar el valor 
    if valor_actual is not None:
        nuevo_valor= valor_actual +  10 
        set_new_value(nuevo_valor)
        
    time.sleep(1)
    
    # 3. Verificar el nuevo valor después de la modificación
    get_current_value()