import sys
import os
import unittest
import json

# Añadir directorio actual al path
sys.path.append(os.getcwd())

from core.recommendation_engine import MovieRecommender
from backend.app import app

class TestMovieRecommender(unittest.TestCase):
    def setUp(self):
        self.recommender = MovieRecommender()
        self.app = app.test_client()
        self.app.testing = True

    def test_core_initialization(self):
        """Prueba que el modelo se inicializa correctamente"""
        print("\nProbando inicialización del core...")
        self.assertIsNotNone(self.recommender.movies)
        self.assertIsNotNone(self.recommender.cosine_sim)
        self.assertEqual(len(self.recommender.movies), 21)
        print("OK - Dataset cargado con 21 películas.")

    def test_core_recommendation(self):
        """Prueba que el motor devuelve recomendaciones"""
        print("\nProbando motor de recomendaciones...")
        result = self.recommender.recommend("The Dark Knight", 3)
        self.assertEqual(result['movie'], "The Dark Knight")
        self.assertEqual(len(result['recommendations']), 3)
        # Verificar que 'The Godfather' está en las recomendaciones (tienen 'Crime' y 'Drama' en común)
        titles = [m['title'] for m in result['recommendations']]
        print(f"Recomendaciones para 'The Dark Knight': {titles}")
        # Basado en el notebook original, The Godfather suele salir alto
        self.assertTrue(any("The Godfather" in t for t in titles))
        print("OK - Recomendaciones válidas.")

    def test_api_index(self):
        """Prueba el endpoint raíz"""
        print("\nProbando API endpoint / ...")
        response = self.app.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", data)
        print("OK - API responde.")

    def test_api_recommend(self):
        """Prueba el endpoint de recomendación"""
        print("\nProbando API endpoint /recommend ...")
        payload = {"title": "Toy Story", "limit": 2}
        response = self.app.post('/recommend', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['movie'], "Toy Story")
        self.assertEqual(len(data['recommendations']), 2)
        print(f"Respuesta API para 'Toy Story': {data['recommendations']}")
        print("OK - API devuelve recomendaciones correctamente.")

if __name__ == '__main__':
    unittest.main()
