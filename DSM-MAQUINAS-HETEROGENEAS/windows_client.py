import redis

REDIS_HOST = '192.168.1.103' #IP donde corre redis
KEY = 'contador'

try:
    # Conexión al servidor Redis
    r = redis.Redis(host=REDIS_HOST, port=6379, db=0)
    r.ping()
    print("--- NODO WINDOWS: Conexión HETEROGÉNEA exitosa. ---")
except Exception as e:
    print(f"Error al conectar a Redis en {REDIS_HOST}: {e}")
    exit(1)


print("\n[NODO WINDOWS] Iniciando lectura y modificación...")

# 1. Leer el valor establecido por el Nodo Linux
valor_leido = r.get(KEY)

if valor_leido:
    valor_leido_int = int(valor_leido.decode('utf-8'))
    print(f"[NODO WINDOWS] Valor leído (escrito por Linux): {valor_leido_int}")

    # 2. Modificar el valor (incrementarlo)
    nuevo_valor = valor_leido_int + 50
    r.set(KEY, nuevo_valor)
    print(f"[NODO WINDOWS] Valor modificado a: {nuevo_valor}")

    # 3. Verificación de la Modificación
    valor_final = r.get(KEY)
    print(f"[NODO WINDOWS] Verificación final: {valor_final.decode('utf-8')}")
else:
    print(f"[NODO WINDOWS] Error: La clave '{KEY}' no fue encontrada. ¿Escribió el Nodo Linux?")