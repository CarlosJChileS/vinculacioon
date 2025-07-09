# ExposIA

ExposIA es un proyecto para entrenar habilidades de exposici\u00f3n oral. El sistema se divide en m\u00f3dulos independientes que pueden ejecutarse de forma conjunta o por separado.
Todos los m\u00f3dulos pueden almacenar su informaci\u00f3n en una base de datos de Supabase (PostgreSQL administrado).
## M\u00f3dulos

1. **Presentaciones** (`ExposIA/presentaciones`)
   - Carga de archivos PDF de presentaciones.
   - Extracci\u00f3n de diapositivas (t\u00edtulos y n\u00fameros de p\u00e1gina).
2. **Prácticas** (`ExposIA/practicas`)
   - Reproductor de slides y registro de navegaci\u00f3n.
   - Grabaci\u00f3n de audio sincronizada.
3. **IA** (`ExposIA/ia`)
   - An\u00e1lisis de grabaciones con FastAPI.
   - Se organiza en capas (`controllers`, `dtos`, `mappers`, `models`, `repositories`, `services`).
   - Subcarpeta opcional `ia_extras/face_detection` para detecci\u00f3n facial.
4. **Calificación** (`ExposIA/calificacion`)
   - C\u00e1lculo de notas a partir de las m\u00e9tricas obtenidas por IA.

## Requisitos

- Python 3.10+
- Una instancia de PostgreSQL gestionada por Supabase
- Variables de entorno `SUPABASE_URL` y `SUPABASE_KEY`
- Dependencias Python listadas en `ExposIA/requirements.txt`

Instala todas las dependencias (incluyendo la librería `supabase`) con:

```bash
pip install -r ExposIA/requirements.txt
```

Algunas bibliotecas como Whisper pueden requerir modelos o claves externas. Configura variables de entorno como:

- `OPENAI_API_KEY` si utilizas Whisper u otros servicios en la nube.
- `SUPABASE_URL` y `SUPABASE_KEY` para conectar con la base de datos.

## Ejecuci\u00f3n

El punto de entrada general se encuentra en `ExposIA/main.py`:

```bash
python -m uvicorn ExposIA.main:app --reload
```

Esto cargar\u00e1 las rutas de los cuatro m\u00f3dulos. Si s\u00f3lo quieres probar el m\u00f3dulo de IA puedes ejecutar:

```bash
python -m uvicorn ExposIA.ia.main:app --reload

```

Accede a la documentaci\u00f3n Swagger en `http://localhost:8000/docs`.

Para ejecutar las pruebas del módulo de IA:

```bash
pytest ExposIA/ia/tests
```

## Frontend

El directorio `frontend/` contiene una pequeña aplicación React.

```bash
cd frontend
npm install
npm run dev
```
