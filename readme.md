# ExposIA
## M\u00f3dulos

1. **Presentations** (`ExposIA/presentations`)
   - Carga de archivos PDF de presentaciones.
   - Extracci\u00f3n de diapositivas (t\u00edtulos y n\u00fameros de p\u00e1gina).
2. **Practices** (`ExposIA/practices`)
   - Reproductor de slides y registro de navegaci\u00f3n.
   - Grabaci\u00f3n de audio sincronizada.
3. **IA** (`ExposIA/ia_module`)
   - An\u00e1lisis de grabaciones con FastAPI.
   - Se organiza en capas (`controllers`, `dtos`, `mappers`, `models`, `repositories`, `services`).
   - Subcarpeta opcional `ia_extras/face_detection` para detecci\u00f3n facial.
4. **Grading** (`ExposIA/grading`)
   - C\u00e1lculo de notas a partir de las m\u00e9tricas obtenidas por IA.

## Requisitos

- Python 3.10+
- PostgreSQL
- Dependencias Python listadas en `ExposIA/requirements.txt`

Instala todo con:

```bash
pip install -r ExposIA/requirements.txt
```

Algunas bibliotecas como Whisper pueden requerir modelos o claves externas. Configura variables de entorno como:

- `DATABASE_URL` para la conexi\u00f3n a PostgreSQL.
- `OPENAI_API_KEY` si utilizas Whisper en la nube.

## Ejecuci\u00f3n

El punto de entrada general se encuentra en `ExposIA/main.py`:

```bash
python -m uvicorn ExposIA.main:app --reload
```

Esto cargar\u00e1 las rutas de los cuatro m\u00f3dulos. Si s\u00f3lo quieres probar el m\u00f3dulo de IA puedes ejecutar:

```bash
python -m uvicorn ExposIA.ia_module.main:app --reload
```

Accede a la documentaci\u00f3n Swagger en `http://localhost:8000/docs`.
