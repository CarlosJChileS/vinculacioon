# Módulo de IA

Este módulo implementa la API de análisis de audio de ExposIA utilizando FastAPI. 
Está organizado por capas para facilitar su mantenimiento:

- `controllers/`: rutas HTTP.
- `dtos/`: modelos Pydantic para entrada y salida.
- `mappers/`: transformaciones entre modelos y dtos.
- `models/`: entidades de dominio (en memoria).
- `repositories/`: preparado para persistencia futura en base de datos.
- `services/`: lógica de negocio y orquestación de análisis.
- `ia_core/`: funciones básicas de análisis (Whisper, SpaCy, Librosa, etc.).
- `ia_extras/face_detection/`: análisis opcional de emociones faciales.

## Requisitos

- Python 3.10+
- Supabase (PostgreSQL) para guardar resultados
- Variables `SUPABASE_URL` y `SUPABASE_KEY`
- Dependencias de Python indicadas en `../requirements.txt`

Instala todo con:

```bash
pip install -r ../requirements.txt
```

Este módulo emplea la versión local de *Whisper*, por lo que no necesitas una
clave de API. El modelo se descarga automáticamente al ejecutarse por primera
vez. Solo es necesario definir `SUPABASE_URL` y `SUPABASE_KEY` si deseas
almacenar los resultados en PostgreSQL.

## Ejecución

Inicia el módulo con Uvicorn:

```bash
python -m uvicorn ExposIA.ia.main:app --reload
```

Para analizar una grabación ya almacenada debes ubicar el archivo en
`data/recordings/<grabacion_id>.wav` y llamar a:

```bash
curl -X POST http://localhost:8000/analisis/grabaciones/<grabacion_id>
```

Accede a la documentación Swagger en `http://localhost:8000/docs`.

El submódulo `face_detection` es opcional y puede eliminarse sin afectar al resto
del sistema.

Si se configuran las variables de Supabase, los resultados se guardarán en la base
de datos. En caso contrario, se utilizan estructuras en memoria.
Contiene al menos cinco entidades Pydantic (`AudioAnalysisInput`, `AnalysisResult`,
`Result`, `AnalysisResultModel`, `FaceResult`).

Para ejecutar las pruebas unitarias:

```bash
pytest ExposIA/ia/tests
```
