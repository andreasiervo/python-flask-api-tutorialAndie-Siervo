#Para crear nuestro primer servidor debemos añadir las siguientes dos líneas en cualquier archivo de Python
from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False }
]


#siempre siemre agregar el retunr con el get
@app.route('/todos', methods=['GET'])
def HelloWorld():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append (request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    deleted = todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)

#Siempre tienen que estar estas dos lineas
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)