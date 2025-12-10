from flask import Flask, request, jsonify
import sys
import os

# Asegurar que podemos importar desde la carpeta core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.recommendation_engine import MovieRecommender

app = Flask(__name__)

# Inicializar el recomendador
recommender = MovieRecommender()

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Bienvenido a la API de Recomendación de Películas",
        "usage": "Envía una petición POST a /recommend con {'title': 'Nombre de la película'}",
        "endpoints": {
            "/recommend": "POST - Obtener recomendaciones",
            "/movies": "GET - Ver lista de películas disponibles"
        }
    })

@app.route('/movies', methods=['GET'])
def get_movies():
    """Devuelve la lista de películas disponibles en el dataset."""
    movies_list = recommender.movies['title'].tolist()
    return jsonify({"count": len(movies_list), "movies": movies_list})

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Endpoint para obtener recomendaciones.
    Espera un JSON: {"title": "The Dark Knight"}
    """
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Por favor proporciona un título de película en el cuerpo JSON: {'title': '...'}"}), 400
    
    title = data['title']
    limit = data.get('limit', 5)
    
    result = recommender.recommend(title, n_recommendations=int(limit))
    
    if "error" in result:
        return jsonify(result), 404
        
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
