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

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080, debug=True)