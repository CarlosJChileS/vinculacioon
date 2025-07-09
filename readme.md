# ExposIA

ExposIA es un sistema modular para mejorar las habilidades de exposición oral.

## Estructura general

- `presentations/`: carga y manejo de presentaciones.
- `practices/`: grabación y navegación de slides.
- `ia_module/`: análisis de audio con FastAPI dividido en capas (controllers,
  dtos, mappers, models, repositories, services).
- `grading/`: generación de calificaciones.

El módulo IA está implementado en Python 3.10+ y expone una API REST documentada
con Swagger.
