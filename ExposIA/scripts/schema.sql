-- SQL schema for ExposIA project
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    email TEXT UNIQUE,
    password TEXT
);

CREATE TABLE tema (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT
);

CREATE TABLE presentacion (
    id SERIAL PRIMARY KEY,
    tema_id INTEGER REFERENCES tema(id),
    usuario_id INTEGER REFERENCES usuario(id),
    archivo_pdf TEXT
);

CREATE TABLE slide (
    id SERIAL PRIMARY KEY,
    presentacion_id INTEGER REFERENCES presentacion(id),
    numero_slide INTEGER,
    img_slide TEXT,
    texto_slide TEXT
);

CREATE TABLE fragmento_audio (
    id SERIAL PRIMARY KEY,
    grabacion_id INTEGER REFERENCES grabacion(id),
    slide_id INTEGER REFERENCES slide(id),
    inicio_segundo INTEGER,
    fin_segundo INTEGER,
    archivo_fragmento TEXT
);

CREATE TABLE navegacion_slide (
    id SERIAL PRIMARY KEY,
    presentacion_id INTEGER REFERENCES presentacion(id),
    slide_id INTEGER REFERENCES slide(id),
    timestamp TIMESTAMP,
    tipo_navegacion TEXT
);

CREATE TABLE nota_slide (
    id SERIAL PRIMARY KEY,
    presentacion_id INTEGER REFERENCES presentacion(id),
    slide_id INTEGER REFERENCES slide(id),
    contenido TEXT,
    timestamp TIMESTAMP
);

CREATE TABLE grabacion (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuario(id),
    presentacion_id INTEGER REFERENCES presentacion(id),
    archivo_audio TEXT,
    fecha_grabacion TIMESTAMP,
    nombre_archivo TEXT,
    ruta_archivo TEXT,
    estado TEXT,
    duracion INTEGER,
    formato TEXT
);

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    grabacion_id INTEGER REFERENCES grabacion(id),
    metrica_id INTEGER REFERENCES metrica(id),
    valor FLOAT,
    comentario TEXT,
    es_manual BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE tipo_metrica (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT
);

CREATE TABLE metrica (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    tipo_metrica_id INTEGER REFERENCES tipo_metrica(id)
);

CREATE TABLE parametro (
    id SERIAL PRIMARY KEY,
    metrica_id INTEGER REFERENCES metrica(id),
    valor FLOAT,
    umbral FLOAT
);

CREATE TABLE hablar_en_publico (
    id SERIAL PRIMARY KEY,
    grabacion_id INTEGER REFERENCES grabacion(id),
    distancia_total FLOAT,
    fecha_inicio TIMESTAMP,
    fecha_fin TIMESTAMP,
    finalizada BOOLEAN
);

CREATE TABLE calificacion (
    id SERIAL PRIMARY KEY,
    grabacion_id INTEGER REFERENCES grabacion(id),
    usuario_id INTEGER REFERENCES usuario(id),
    puntaje_global FLOAT,
    observacion_global TEXT,
    fecha TIMESTAMP,
    parametro_id INTEGER
);

CREATE TABLE parametros_externos (
    id SERIAL PRIMARY KEY,
    calidad_ideal TEXT,
    valor_actual TEXT,
    razones_breves TEXT,
    otros_parametros TEXT
);

CREATE TABLE criterio_evaluacion (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    peso FLOAT
);

CREATE TABLE detalle_calificacion (
    id SERIAL PRIMARY KEY,
    calificacion_id INTEGER REFERENCES calificacion(id),
    criterio_id INTEGER REFERENCES criterio_evaluacion(id),
    valor FLOAT,
    comentario TEXT,
    parametro_metrica_id INTEGER
);

CREATE TABLE feedback_calificacion (
    id SERIAL PRIMARY KEY,
    calificacion_id INTEGER REFERENCES calificacion(id),
    observacion TEXT,
    fecha TIMESTAMP,
    autor TEXT
);

CREATE TABLE deteccion_facial (
    id SERIAL PRIMARY KEY,
    resultado_id INTEGER,
    emocion TEXT,
    confianza FLOAT
);
