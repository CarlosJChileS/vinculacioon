import React from "react";
import "./DashboardPage.css";

export default function DashboardPage() {
  return (
    <div className="dashboard-bg">
      <div className="dashboard-container">
        {/* Header */}
        <header className="dashboard-header">
          <div className="logo">ExposIA</div>
          <div className="dashboard-header-right">
            <span className="dashboard-header-icon">
              <i className="fas fa-bell"></i>
            </span>
            <div className="user-info">
              <div className="user-avatar">JP</div>
              <div>
                <div className="user-name">Juan Pérez</div>
                <div className="user-role">Estudiante</div>
              </div>
            </div>
          </div>
        </header>

        {/* Main Content */}
        <main>
          {/* Welcome and Stats */}
          <section className="dashboard-welcome">
            <h2>Bienvenido, Juan</h2>
            <p>Continúa mejorando tus habilidades de oratoria</p>
            <div className="dashboard-stats">
              <div className="stat">
                <div className="stat-value">8</div>
                <div className="stat-label">Presentaciones</div>
                <div className="stat-desc">Presentaciones subidas</div>
              </div>
              <div className="stat">
                <div className="stat-value">12</div>
                <div className="stat-label">Prácticas</div>
                <div className="stat-desc">Sesiones de práctica</div>
              </div>
              <div className="stat">
                <div className="stat-value">8.5/10</div>
                <div className="stat-label">Puntuación Media</div>
                <div className="stat-desc">Calificación promedio</div>
              </div>
              <div className="stat">
                <div className="stat-value">3.5h</div>
                <div className="stat-label">Tiempo Total</div>
                <div className="stat-desc">Tiempo de práctica</div>
              </div>
            </div>
          </section>

          {/* Recent Activity */}
          <section className="dashboard-section">
            <div className="section-title">Actividad Reciente</div>
            <div className="activity-list">
              <div className="activity-item">
                <div>
                  <div className="activity-title">Presentación de Marketing Digital</div>
                  <div className="activity-desc">Práctica evaluada con IA</div>
                </div>
                <div className="activity-time">Hace 7 horas</div>
              </div>
              <div className="activity-item">
                <div>
                  <div className="activity-title">Preparación para Ingeniería</div>
                  <div className="activity-desc">Nueva presentación subida</div>
                </div>
                <div className="activity-time">Ayer</div>
              </div>
              <div className="activity-item">
                <div>
                  <div className="activity-title">Análisis de Debates Empresariales</div>
                  <div className="activity-desc">Práctica evaluada con IA</div>
                </div>
                <div className="activity-time">Hace 3 días</div>
              </div>
              <div className="activity-item">
                <div>
                  <div className="activity-title">Introducción a la Psicología</div>
                  <div className="activity-desc">Práctica en progreso</div>
                </div>
                <div className="activity-time">Hace 5 días</div>
              </div>
            </div>
            <div className="see-history">Ver todo el historial</div>
          </section>

          {/* Quick Actions */}
          <section className="dashboard-section dashboard-actions">
            <button className="btn-primary">Subir Presentación</button>
            <button className="btn-outline">Iniciar Práctica</button>
            <button className="btn-outline">Ver Ítems</button>
          </section>

          {/* Tips */}
          <section className="dashboard-section dashboard-tips">
            <div className="tips-title">Consejos para mejorar</div>
            <ul>
              <li>Practica mirando un timer visible durante toda la presentación.</li>
              <li>Realiza autoevaluaciones con ítems “clarity” antes de cada exposición.</li>
              <li>Mejora el tono de tu pronunciación, especialmente en términos técnicos.</li>
            </ul>
          </section>
        </main>
      </div>
    </div>
  );
}
