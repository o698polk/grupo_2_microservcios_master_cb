import unittest
import os
import json
from unittest.mock import patch
from app import app, ARCHIVO

import io
import json
import os

##debe estar dentro de una clase a funcion
    # =========================
    # Tests del menú principal
    # =========================
    #def test_menu(self):
     #   resp = self.app.get("/")
      #  self.assertEqual(resp.status_code, 200)
       # data = resp.get_json()
        #self.assertIn("Ver todos", data["endpoints"])
        #self.assertIn("Ver uno", data["endpoints"])
        #self.assertIn("Crear", data["endpoints"])
        #self.assertIn("Editar", data["endpoints"])
        #self.assertIn("Eliminar", data["endpoints"])
        
class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

        # Crear archivo limpio antes de cada test
        with open(ARCHIVO, "w") as f:
            json.dump([], f)

    def tearDown(self):
        # Eliminar archivo después de pruebas
        if os.path.exists(ARCHIVO):
            os.remove(ARCHIVO)

    # ==============================
    # TEST MENU PRINCIPAL
    # ==============================
    def test_menu(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("mensaje", data)
        self.assertIn("endpoints", data)

    # ==============================
    # TEST CREAR PLATO CORRECTO
    # ==============================
    @patch("app.verificar_pais_api")
    def test_crear_plato_exitoso(self, mock_verificar):
        mock_verificar.return_value = True

        response = self.client.post(
            "/platos",
            json={
                "pais": "Ecuador",
                "plato": "Ceviche"
            }
        )

        self.assertEqual(response.status_code, 201)

        data = response.get_json()
        self.assertEqual(data["plato"]["pais"], "Ecuador")
        self.assertEqual(data["plato"]["plato"], "Ceviche")

    # ==============================
    # TEST CREAR SIN DATOS
    # ==============================
    def test_crear_plato_sin_datos(self):
        response = self.client.post("/platos", json={})
        self.assertEqual(response.status_code, 400)

    # ==============================
    # TEST PAIS INVALIDO
    # ==============================
    @patch("app.verificar_pais_api")
    def test_crear_plato_pais_invalido(self, mock_verificar):
        mock_verificar.return_value = False

        response = self.client.post(
            "/platos",
            json={
                "pais": "PaisInventado",
                "plato": "ComidaX"
            }
        )

        self.assertEqual(response.status_code, 404)

    # ==============================
    # TEST OBTENER TODOS
    # ==============================
    @patch("app.verificar_pais_api")
    def test_obtener_platos(self, mock_verificar):
        mock_verificar.return_value = True

        self.client.post(
            "/platos",
            json={
                "pais": "Perú",
                "plato": "Lomo Saltado"
            }
        )

        response = self.client.get("/platos")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(len(data) > 0)

    # ==============================
    # TEST OBTENER UNO EXISTENTE
    # ==============================
    @patch("app.verificar_pais_api")
    def test_obtener_un_plato_existente(self, mock_verificar):
        mock_verificar.return_value = True

        self.client.post(
            "/platos",
            json={
                "pais": "Colombia",
                "plato": "Bandeja Paisa"
            }
        )

        response = self.client.get("/platos/1")
        self.assertEqual(response.status_code, 200)

    # ==============================
    # TEST OBTENER UNO NO EXISTE
    # ==============================
    def test_obtener_plato_no_existente(self):
        response = self.client.get("/platos/999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()