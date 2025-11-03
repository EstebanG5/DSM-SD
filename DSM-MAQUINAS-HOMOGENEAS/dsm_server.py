
# Servidor Flask 

from flask import Flask, request, jsonify

app = Flask(__name__)

# La variable compartida 
shared_variable = 0

@app.route('/value', methods=['GET'])
def get_value():
    """Endpoint para LEER la variable compartida."""
    # Retorna el valor actual de la variable.
    return jsonify({
        "node": "nodo1",
        "operation": "READ",
        "value": shared_variable
    })

@app.route('/value', methods=['POST'])
def set_value():
    """Endpoint para ESCRIBIR/MODIFICAR la variable compartida."""
    global shared_variable
    
    try:
        data = request.get_json()
        new_value = data.get('new_value')
        
        if new_value is not None and isinstance(new_value, int):
            old_value = shared_variable
            shared_variable = new_value
            
            return jsonify({
                "status": "success",
                "operation": "WRITE",
                "message": f"Value updated from {old_value} to {shared_variable}",
                "new_value": shared_variable
            }), 200
        else:
            return jsonify({"status": "error", "message": "Invalid integer value in request body."}), 400
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # La aplicación debe escuchar en '0.0.0.0' para ser accesible desde 'nodo2' 
    # a través de la red Docker.
    app.run(host='0.0.0.0', port=5000)