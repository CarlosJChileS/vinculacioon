import React from "react";
import "./HomePage.css";

export default function HomePage() {
  return (
    <div className="homepage">
      <header className="header">
        <div className="container header-content">
          <div className="logo">ExposIA</div>
          <nav className="nav">
            <a href="#">Inicio</a>
            <a href="#">Características</a>
            <a href="#">Precios</a>
            <a href="#">Contacto</a>
            <button className="btn-secondary">Iniciar Sesión</button>
          </nav>
        </div>
      </header>

      <section className="hero">
        <h1>Mejora tus habilidades de<br />oratoria con IA</h1>
        <p>
          ExposIA te ayuda a perfeccionar tus presentaciones a través de práctica estructurada, retroalimentación automatizada y análisis de desempeño.
        </p>
        <div className="hero-buttons">
          <button className="btn-primary">Registrarse</button>
          <button className="btn-secondary">Ver Demo</button>
        </div>
      </section>

      <section className="funciona">
        <h2>¿Cómo funciona?</h2>
        <div className="steps">
          <div className="step">
            <div className="circle">1</div>
            <strong>Sube tu presentación</strong>
            <span>Carga el archivo PDF de tu presentación para iniciar el análisis con IA.</span>
          </div>
          <div className="step">
            <div className="circle">2</div>
            <strong>Practica tu exposición</strong>
            <span>Graba tu voz o video practicando con apoyo de la plataforma.</span>
          </div>
          <div className="step">
            <div className="circle">3</div>
            <strong>Recibe retroalimentación</strong>
            <span>Obtén análisis automático, sugerencias y métricas de desempeño.</span>
          </div>
          <div className="step">
            <div className="circle">4</div>
            <strong>Mejora continuamente</strong>
            <span>Aplica los consejos y realiza nuevas prácticas para perfeccionar tus presentaciones.</span>
          </div>
        </div>
      </section>

      <section className="caracteristicas">
        <h2>Características principales</h2>
        <div className="features">
          <div className="feature">
            <span className="icon">📄</span>
            <strong>Procesamiento de PDF</strong>
            <span>Compatible con archivos PDF para análisis estructurado y recomendaciones personalizadas.</span>
          </div>
          <div className="feature">
            <span className="icon">🎤</span>
            <strong>Grabación inteligente</strong>
            <span>Graba y analiza tu exposición, detectando pausas, entonación y muletillas.</span>
          </div>
          <div className="feature">
            <span className="icon">🤖</span>
            <strong>Análisis con IA</strong>
            <span>Análisis automático de tu oratoria mediante inteligencia artificial.</span>
          </div>
          <div className="feature">
            <span className="icon">📊</span>
            <strong>Evaluación detallada</strong>
            <span>Recibe reportes de métricas clave y recomendaciones en cada práctica.</span>
          </div>
        </div>
      </section>

      <section className="cta">
        <h2>Comienza a mejorar tus presentaciones hoy</h2>
        <p>
          Únete a miles de estudiantes y profesionales que ya están mejorando sus habilidades orales con ExposIA.
        </p>
        <button className="btn-primary">Crear cuenta gratuita</button>
      </section>

      <footer className="footer">
        <div className="container footer-content">
          <div className="footer-col">
            <strong>ExposIA</strong>
            <div>Mejora tu habilidad de oratoria con inteligencia artificial.</div>
          </div>
          <div className="footer-col">
            <strong>Producto</strong>
            <div>Características<br />Precios<br />Demo</div>
          </div>
          <div className="footer-col">
            <strong>Empresa</strong>
            <div>Contacto<br />Equipo</div>
          </div>
          <div className="footer-col">
            <strong>Legal</strong>
            <div>Términos<br />Privacidad</div>
          </div>
        </div>
        <div className="footer-copy">
          © 2024 ExposIA. Todos los derechos reservados.
        </div>
      </footer>
    </div>
  );
}
