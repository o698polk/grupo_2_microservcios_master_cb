from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

ARCHIVO = "platos.json"


# ==============================
# FUNCIONES AUXILIARES
# ==============================

def leer_datos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_datos(datos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def generar_id(datos):
    if not datos:
        return 1
    return max(plato["id"] for plato in datos) + 1


def verificar_pais_api(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
    respuesta = requests.get(url)
    return respuesta.status_code == 200


# ==============================
# MENU PRINCIPAL
# ==============================

@app.route("/", methods=["GET"])
def menu():
    return jsonify({
        "mensaje": "API DE PLATOS TIPICOS , GRUPO 2",
        "endpoints": {
            "Ver todos": "GET /platos",
            "Ver uno": "GET /platos/<id>",
            "Crear": "POST /platos",
            "Editar": "PUT /platos/<id>",
            "Eliminar": "DELETE /platos/<id>"
        }
    })




# ==============================
# VER TODOS
# ==============================

@app.route("/platos", methods=["GET"])
def obtener_platos():
    datos = leer_datos()
    return jsonify(datos), 200


# ==============================
# VER UNO
# ==============================

@app.route("/platos/<int:id>", methods=["GET"])
def obtener_plato(id):
    datos = leer_datos()
    plato = next((p for p in datos if p["id"] == id), None)

    if not plato:
        return jsonify({"error": "Plato no encontrado"}), 404

    return jsonify(plato), 200


# ==============================
# CREAR
# ==============================

@app.route("/platos", methods=["POST"])
def crear_plato():
    datos = leer_datos()
    data = request.get_json(force=True)

    nombre_pais = data.get("pais")
    nombre_plato = data.get("plato")

    if not nombre_pais or not nombre_plato:
        return jsonify({"error": "Se requiere país y plato"}), 400

    if not verificar_pais_api(nombre_pais):
        return jsonify({"error": "El país no existe"}), 404

    nuevo_plato = {
        "id": generar_id(datos),
        "pais": nombre_pais,
        "plato": nombre_plato
    }

    datos.append(nuevo_plato)
    guardar_datos(datos)

    return jsonify({
        "mensaje": "Plato creado exitosamente",
        "plato": nuevo_plato
    }), 201


# ==============================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)