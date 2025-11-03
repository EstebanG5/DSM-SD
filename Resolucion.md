# Resolucion de las actividades

## 2.Nivel Sistema Operativo – DSM en Máquinas Homogéneas
```bash
CD .\DSM-MAQUINAS-HOMOGENEAS\
docker-compose up -d
```
**Salida**
```bash
nodo1  |  * Running on all addresses (0.0.0.0)
nodo1  |  * Running on http://127.0.0.1:5000
nodo1  |  * Running on http://172.20.0.3:5000
nodo1  | Press CTRL+C to quit
nodo1  | 172.20.0.2 - - [03/Nov/2025 04:19:07] "GET /value HTTP/1.1" 200 -
nodo1  | 172.20.0.2 - - [03/Nov/2025 04:19:07] "POST /value HTTP/1.1" 200 -
nodo1  | 172.20.0.2 - - [03/Nov/2025 04:19:08] "GET /value HTTP/1.1" 200 -

nodo2  | [nodo2] Intentando LEER el valor actual...
nodo2  | [nodo2] Lectura exitosa. Valor actual en DSM: 0
nodo2  |
nodo2  | [nodo2] Intentando ESCRIBIR el valor 10...
nodo2  | [nodo2] Escritura exitosa. Nuevo valor confirmado: 10
nodo2  |
nodo2  | [nodo2] Intentando LEER el valor actual...
nodo2  | [nodo2] Lectura exitosa. Valor actual en DSM: 10
nodo2 exited with code 0
```
Podemos volver a ejecutar el cliente desde otra terminal mientras el servidor siga activo
```bash
docker-compose up --build -d nodo2
```
**Salida**
```bash
nodo2 has been recreated
nodo1  | 172.20.0.2 - - [03/Nov/2025 04:22:16] "GET /value HTTP/1.1" 200 -
nodo1  | 172.20.0.2 - - [03/Nov/2025 04:22:16] "POST /value HTTP/1.1" 200 -


nodo2  |
nodo2  | [nodo2] Intentando LEER el valor actual...
nodo2  | [nodo2] Lectura exitosa. Valor actual en DSM: 10
nodo2  |
nodo2  | [nodo2] Intentando ESCRIBIR el valor 20...
nodo2  | [nodo2] Escritura exitosa. Nuevo valor confirmado: 20
nodo2  |
nodo1  | 172.20.0.2 - - [03/Nov/2025 04:22:17] "GET /value HTTP/1.1" 200 -
nodo2 exited with code 0
nodo2 exited with code 0
```
## Resumen
Una vez corriendo el servidor FLASK con la variable compartida, el cliente hace una peticion del valor actual de la variable, a ese valor le suma 10 y escribe asigna este nuevo valor a la variable compartida.
## 3.Nivel Sistema Distribuido – Máquinas Heterogéneas

1. **Iniciar Redis en docker**
```bash
docker run -d --name redis-shared -p 6379:6379 redis
```

2. **Instalar Redis en Linux**
```bash
sudo apt install redis-tools
```

3. **En Linux conectar al Servidor y escribir**
```bash
redis-cli -h 192.168.1.103
SET contador 100
```

**Salida**
```bash
OK
```

4. **Instalar Redis en Windows**
```bash
pip install redis
```

4. **Leer desde Windows y modificar el valor**
```bash
cd DSM-MAQUINAS-HETEROGENEAS
python windows_client.py
```
### Resultado
```bash
--- NODO WINDOWS: Conexión HETEROGÉNEA exitosa. ---

[NODO WINDOWS] Iniciando lectura y modificación...
[NODO WINDOWS] Valor leído (escrito por Linux): 100
[NODO WINDOWS] Valor modificado a: 150
[NODO WINDOWS] Verificación final: 150
```
## Resumen
Una vez corriendo Redis, 
1. la maquina con Linux se conecta al servidor con la direccion ip de servidor
2. escribe el valor de la variable contador (100)
3. La maquina con Windows se conecta al servidor con la direccion ip del servidor
4. Lee el valor del contador, le suma 50 y modifica el valor del contador.