from ExposIA.common.database import engine, init_db, SessionLocal
from ExposIA.presentaciones.models.presentation import PresentationOrm
from ExposIA.presentaciones.models.slide import SlideOrm
from ExposIA.ia.models.analysis_result import AnalysisResult
from ExposIA.calificacion.models.grade import GradeOrm
from ExposIA.practicas.models.slide_nav import SlideNavigationOrm

init_db()

with SessionLocal() as session:
    # Insert presentation and slides
    pres = PresentationOrm(tema_id=1, usuario_id=1, archivo_pdf="example.pdf")
    session.add(pres)
    session.flush()
    slide1 = SlideOrm(presentacion_id=pres.id, numero_slide=1, img_slide="", texto_slide="Introduccion")
    slide2 = SlideOrm(presentacion_id=pres.id, numero_slide=2, img_slide="", texto_slide="Conclusion")
    session.add_all([slide1, slide2])
    # Insert analysis result
    result = AnalysisResult(velocidad_palabras=120, claridad=8.5, num_pausas=4, retroalimentacion="Buen ritmo")
    session.add(result)
    session.flush()
    # Insert grade
    grade = GradeOrm(grabacion_id=1, usuario_id=1, puntaje_global=9.0)
    session.add(grade)
    # Insert navigation
    nav = SlideNavigationOrm(presentacion_id=pres.id, slide_id=slide1.id, timestamp=0.0, tipo_navegacion="start")
    session.add(nav)
    session.commit()
print("Database initialized")
