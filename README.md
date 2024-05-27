
# 📈 FastAPI Stock API

Una API simple creada con FastAPI que obtiene datos de acciones en tiempo real desde Yahoo Finance y los guarda en MongoDB. La API proporciona endpoints para obtener las 10 acciones con mayores ganancias y pérdidas.

## 📋 Índice

- [Instalación](#instalación)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso de la API](#uso-de-la-api)
- [Endpoints](#endpoints)
- [Verificación de Datos en MongoDB](#verificación-de-datos-en-mongodb)
- [Créditos](#créditos)

## 🚀 Instalación

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/tuusuario/tu-repo.git
    cd tu-repo
    ```

2. **Crea un entorno virtual e instala las dependencias**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## ⚙️ Configuración de la Base de Datos

Asegúrate de tener MongoDB instalado y en ejecución. Por defecto, MongoDB se ejecuta en el puerto `27017`.

## 🗂️ Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

```
my_fastapi_project/
├── main.py
├── database.py
├── models/
│   └── stock.py
├── routers/
│   └── stock.py
├── services/
│   └── stock_service.py
├── requirements.txt
```

### Descripción de Archivos

- **main.py**: Punto de entrada de la aplicación.
- **database.py**: Configuración de la base de datos MongoDB.
- **models/stock.py**: Definición del modelo de datos `Stock`.
- **routers/stock.py**: Definición de los endpoints de la API.
- **services/stock_service.py**: Lógica para obtener datos de Yahoo Finance y guardarlos en MongoDB.
- **requirements.txt**: Lista de dependencias del proyecto.

## 📖 Uso de la API

1. **Inicia la aplicación**:
    ```bash
    uvicorn main:app --reload
    ```

2. **Accede a la documentación interactiva** de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI) o [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (ReDoc).

## 🔗 Endpoints

### Obtener las 10 acciones con mayores ganancias

- **URL**: `/api/stocks/gainers`
- **Método HTTP**: `GET`
- **Descripción**: Devuelve las 10 acciones con mayores ganancias.
- **Ejemplo de Respuesta**:
    ```json
    [
      {
        "code": "AAPL",
        "name": "Apple Inc.",
        "price": 150.0,
        "movement": 5.0
      },
      ...
    ]
    ```

### Obtener las 10 acciones con mayores pérdidas

- **URL**: `/api/stocks/losers`
- **Método HTTP**: `GET`
- **Descripción**: Devuelve las 10 acciones con mayores pérdidas.
- **Ejemplo de Respuesta**:
    ```json
    [
      {
        "code": "TSLA",
        "name": "Tesla Inc.",
        "price": 600.0,
        "movement": -10.0
      },
      ...
    ]
    ```

## 🗃️ Verificación de Datos en MongoDB

Puedes verificar que los datos se han guardado correctamente en MongoDB usando varias herramientas:

### 1. Usar la Consola de MongoDB (`mongo`)

1. **Abrir la consola de MongoDB**:
    ```bash
    mongo
    ```

2. **Seleccionar la base de datos**:
    ```javascript
    use stocks_db
    ```

3. **Mostrar las colecciones**:
    ```javascript
    show collections
    ```

4. **Consultar los datos**:
    ```javascript
    db.stocks.find().pretty()
    ```

### 2. Usar MongoDB Compass

1. **Descargar e instalar MongoDB Compass** desde [aquí](https://www.mongodb.com/try/download/compass).
2. **Abrir MongoDB Compass** y conectarse a tu base de datos usando la URI de conexión:
    ```plaintext
    mongodb://localhost:27017
    ```
3. **Seleccionar la base de datos `stocks_db`** y la colección `stocks`.
4. **Ver los documentos** almacenados en la colección.

### 3. Usar un Script de Python

1. **Crear un archivo `check_data.py`**:
    ```python
    from pymongo import MongoClient

    MONGO_DETAILS = "mongodb://localhost:27017"
    client = MongoClient(MONGO_DETAILS)
    database = client.stocks_db
    stock_collection = database.get_collection("stocks")

    # Obtener todos los documentos en la colección
    stocks = stock_collection.find()

    for stock in stocks:
        print(stock)
    ```

2. **Ejecutar el script**:
    ```bash
    python check_data.py
    ```

## 👥 Créditos

Desarrollado por [Fernando Cassera](https://github.com/ferc33).

---

🛠️ **Tecnologías Usadas**:
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Yahoo Finance API](https://pypi.org/project/yfinance/)
