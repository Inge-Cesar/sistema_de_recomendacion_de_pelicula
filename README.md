# Sistema de Recomendación de Películas

Este archivo es la **única guía** que necesitas. Aquí te explico cómo instalar, correr y verificar el proyecto.

## 1. Instalación y Ejecución

Para usar el sistema en tu computadora:

1.  **Instalar requisitos** (si no lo has hecho):
    ```bash
    pip install -r requirements.txt
    ```

2.  **Iniciar el servidor**:
    ```bash
    python backend/app.py
    ```
    *IMPORTANTE: La terminal se quedará "esperando". Eso significa que el servidor está encendido. No la cierres.*

---

## 2. Verificar que funciona (Pruebas)

Tienes dos formas de probarlo.

### Opción A: Prueba Automática (Recomendada)
Abre **otra** terminal y ejecuta:

```bash
python test_project.py
```

**Si ves un `OK` al final, todo está perfecto.** Esto prueba el modelo y la API automáticamente.

### Opción B: Prueba Manual
Con el servidor encendido, abre tu navegador en:
[http://127.0.0.1:5000/movies](http://127.0.0.1:5000/movies)

Si ves una lista de películas, **¡FUNCIONA!**

---

## 3. Pruebas en la Nube (Render/Postman)

Una vez que Render te dé tu link (ejemplo: `https://mi-app.onrender.com`), funciona igual que en local.

**Para preguntar por recomendaciones en Postman:**

1.  **Método**: `POST`
2.  **URL**: `https://TU-LINK-DE-RENDER.onrender.com/recommend`
3.  **Body** (JSON):
    ```json
    {
      "title": "The Dark Knight",
      "limit": 3
    }
    ```

---

## 4. Estructura de Archivos

- `core/`: Cerebro del sistema (Matemáticas).
- `backend/`: Servidor Web (API Flask).
- `requirements.txt`: Librerías necesarias.
- `Procfile`: Para subir a la nube.
- `test_project.py`: Script de prueba automático.
