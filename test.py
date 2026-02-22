import io
import json
import os


    # =========================
    # Tests del menú principal
    # =========================
    def test_menu(self):
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn("Ver todos", data["endpoints"])
        self.assertIn("Ver uno", data["endpoints"])
        self.assertIn("Crear", data["endpoints"])
        self.assertIn("Editar", data["endpoints"])
        self.assertIn("Eliminar", data["endpoints"])
        