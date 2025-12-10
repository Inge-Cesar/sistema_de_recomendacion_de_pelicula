# Sistema de Recomendación de Películas

Este proyecto implementa un **Sistema de Recomendación de Películas** basado en contenido, utilizando técnicas de Machine Learning (TF-IDF y Similitud del Coseno) para sugerir películas similares en base a sus géneros y títulos.

🔗 **URL de la API en Producción:**  
`https://sistema-de-recomendacion-de-pelicula.onrender.com`

📂 **Repositorio en GitHub:**  
`https://github.com/Inge-Cesar/sistema_de_recomendacion_de_pelicula.git`

---

## 1. Instalación y Ejecución Local

Si deseas correr el sistema en tu propia computadora:

1.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Iniciar el servidor**:
    ```bash
    python backend/app.py
    ```
    *El servidor iniciará en http://127.0.0.1:5000*

---

## 2. Cómo Usar la API (Pruebas)

Puedes probar la API tanto localmente como en la versión desplegada en Render.

### Endpoint: `/recommend`
**Método**: `POST`  
**Descripción**: Recibe el título de una película y devuelve recomendaciones similares.

#### Ejemplo de Solicitud (JSON):
```json
{
  "title": "The Dark Knight",
  "limit": 3
}
```

#### Ejemplo de Respuesta:
```json
{
    "movie": "The Dark Knight",
    "recommendations": [
        {
            "genres": "Action|Adventure|Sci-Fi",
            "similarity_score": 0.354,
            "title": "Mad Max: Fury Road",
            "year": 2015
        },
        ...
    ]
}
```

### Probar con cURL:
```bash
curl -X POST https://sistema-de-recomendacion-de-pelicula.onrender.com/recommend \
     -H "Content-Type: application/json" \
     -d '{"title": "The Dark Knight", "limit": 3}'
```

### Probar con Postman:
1.  Crear una nueva petición `POST`.
2.  URL: `https://sistema-de-recomendacion-de-pelicula.onrender.com/recommend`
3.  Body -> Raw -> JSON.
4.  Pegar el JSON de ejemplo y enviar.

---

## 3. ¿Cómo funciona el Modelo?

El "cerebro" del sistema se encuentra en `core/recommendation_engine.py`.

1.  **Datos**: Utiliza un dataset predefinido de películas con sus características (título, año, géneros).
2.  **Preprocesamiento**: Combina el título y los géneros en una sola cadena de texto ("features").
3.  **Vectorización (TF-IDF)**: Convierte el texto en vectores numéricos, dando menos peso a palabras comunes y más peso a palabras distintivas.
4.  **Similitud del Coseno**: Calcula el ángulo entre los vectores de las películas. Películas con un ángulo menor (valor cercano a 1) son consideradas más similares.

---

## 4. Estructura del Proyecto

- `core/`: Contiene la lógica de Machine Learning (`MovieRecommender`).
- `backend/`: Servidor Web hecho con **Flask**.
- `requirements.txt`: Lista de librerías necesarias.
- `Procfile`: Archivo de configuración para el despliegue en Render.
- `test_project.py`: Script para probar todo el flujo automáticamente.
