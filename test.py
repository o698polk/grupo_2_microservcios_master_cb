## TEST DE VALIDACION AUTOMATIZADO

import requests
import json

BASE_URL = "http://localhost:8080"


def imprimir_respuesta(response):
    print("Status Code:", response.status_code)
    try:
        print("Response:", json.dumps(response.json(), indent=4))
    except:
        print("Response:", response.text)
    print("-" * 50)


# =========================
# MENU PRINCIPAL
# =========================
def test_menu():
    print("Probando MENU")
    response = requests.get(f"{BASE_URL}/")
    imprimir_respuesta(response)


# =========================
# CREAR PLATO
# =========================
def test_crear_plato():
    print("Probando CREAR PLATO")

    data = {
        "pais": "Ecuador",
        "plato": "Ceviche"
    }

    response = requests.post(
        f"{BASE_URL}/platos",
        json=data
    )

    imprimir_respuesta(response)


# =========================
# VER TODOS
# =========================
def test_ver_todos():
    print("Probando VER TODOS")
    response = requests.get(f"{BASE_URL}/platos")
    imprimir_respuesta(response)


# =========================
# VER UNO
# =========================
def test_ver_uno(id):
    print(f"Probando VER UNO (id={id})")
    response = requests.get(f"{BASE_URL}/platos/{id}")
    imprimir_respuesta(response)


# =========================
# EDITAR
# =========================
def test_editar(id):
    print(f"Probando EDITAR (id={id})")

    data = {
        "plato": "Encebollado"
    }

    response = requests.put(
        f"{BASE_URL}/platos/{id}",
        json=data
    )

    imprimir_respuesta(response)


# =========================
# ELIMINAR
# =========================
def test_eliminar(id):
    print(f"Probando ELIMINAR (id={id})")
    response = requests.delete(f"{BASE_URL}/platos/{id}")
    imprimir_respuesta(response)


# =========================
# EJECUCIÓN SECUENCIAL
# =========================

if __name__ == "__main__":

    print("\n INICIANDO PRUEBAS AUTOMÁTICAS\n")

    test_menu()
    test_crear_plato()
    test_ver_todos()
    test_ver_uno(1)
    test_editar(1)
    test_ver_uno(1)
    test_eliminar(1)
    test_ver_todos()

    print("\n PRUEBAS FINALIZADAS\n")
