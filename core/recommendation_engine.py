import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self):
        self.movies = None
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.indices = None
        self._initialize_model()

    def _initialize_model(self):
        """Inicializa los datos y entrena el modelo."""
        # Configurar semilla
        np.random.seed(42)

        # Crear dataset de películas
        self.movies = self._create_dataset()
        
        # Preprocesamiento
        self.movies['features'] = self.movies['title'] + ' ' + self.movies['genres'].str.replace('|', ' ')

        # Vectorización TF-IDF
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.movies['features'])

        # Calcular Similitud del Coseno
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

        # Crear mapeo de índices
        self.indices = pd.Series(self.movies.index, index=self.movies['title']).drop_duplicates()
        print("Modelo entrenado y listo.")

    def _create_dataset(self):
        """Crea el dataset de películas hardcodeado como en el notebook original."""
        movies_data = [
            # Acción
            {'title': 'The Dark Knight', 'year': 2008, 'genres': 'Action|Crime|Drama'},
            {'title': 'Inception', 'year': 2010, 'genres': 'Action|Sci-Fi|Thriller'},
            {'title': 'Mad Max: Fury Road', 'year': 2015, 'genres': 'Action|Adventure|Sci-Fi'},

            # Drama
            {'title': 'The Shawshank Redemption', 'year': 1994, 'genres': 'Drama'},
            {'title': 'Forrest Gump', 'year': 1994, 'genres': 'Drama|Romance'},
            {'title': 'The Godfather', 'year': 1972, 'genres': 'Crime|Drama'},

            # Comedia
            {'title': 'The Hangover', 'year': 2009, 'genres': 'Comedy'},
            {'title': 'Superbad', 'year': 2007, 'genres': 'Comedy'},
            {'title': 'Step Brothers', 'year': 2008, 'genres': 'Comedy'},

            # Ciencia Ficción
            {'title': 'Interstellar', 'year': 2014, 'genres': 'Adventure|Drama|Sci-Fi'},
            {'title': 'The Matrix', 'year': 1999, 'genres': 'Action|Sci-Fi'},
            {'title': 'Blade Runner 2049', 'year': 2017, 'genres': 'Drama|Mystery|Sci-Fi'},

            # Animación
            {'title': 'Toy Story', 'year': 1995, 'genres': 'Animation|Adventure|Comedy'},
            {'title': 'Spirited Away', 'year': 2001, 'genres': 'Animation|Adventure|Family'},
            {'title': 'The Incredibles', 'year': 2004, 'genres': 'Animation|Action|Adventure'},

            # Terror
            {'title': 'Get Out', 'year': 2017, 'genres': 'Horror|Mystery|Thriller'},
            {'title': 'Hereditary', 'year': 2018, 'genres': 'Drama|Horror|Mystery'},
            {'title': 'A Quiet Place', 'year': 2018, 'genres': 'Drama|Horror|Sci-Fi'},

            # Romance
            {'title': 'La La Land', 'year': 2016, 'genres': 'Comedy|Drama|Music'},
            {'title': 'The Notebook', 'year': 2004, 'genres': 'Drama|Romance'},
            {'title': 'Pride & Prejudice', 'year': 2005, 'genres': 'Drama|Romance'},
        ]
        
        df = pd.DataFrame(movies_data)
        df['movieId'] = range(1, len(df) + 1)
        return df

    def recommend(self, title, n_recommendations=5):
        """
        Recomienda películas similares basadas en una película dada.
        Retorna una lista de diccionarios.
        """
        try:
            # Obtener índice de la película
            if title not in self.indices:
                return {"error": f"Película '{title}' no encontrada en el dataset", "recommendations": []}

            idx = self.indices[title]

            # Obtener puntuaciones de similitud
            sim_scores = list(enumerate(self.cosine_sim[idx]))

            # Ordenar películas por similitud
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Obtener índices de las películas más similares (excluyendo la misma)
            sim_scores = sim_scores[1:n_recommendations+1]
            movie_indices = [i[0] for i in sim_scores]

            # Construir resultado
            recommendations = []
            for i, score in zip(movie_indices, sim_scores):
                movie = self.movies.iloc[i]
                recommendations.append({
                    "title": movie['title'],
                    "year": int(movie['year']),
                    "genres": movie['genres'],
                    "similarity_score": round(score[1], 3)
                })

            return {"movie": title, "recommendations": recommendations}

        except Exception as e:
            return {"error": str(e), "recommendations": []}

if __name__ == "__main__":
    # Prueba simple si se ejecuta directamente
    recommender = MovieRecommender()
    print(recommender.recommend("The Dark Knight", 3))
