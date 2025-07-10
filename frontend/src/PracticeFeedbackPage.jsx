import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";
import "./PracticeFeedbackPage.css";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

export default function PracticeFeedbackPage() {
  const muletillas = [
    { word: "eh", count: 8 },
    { word: "este", count: 6 },
    { word: "um", count: 4 },
    { word: "como", count: 4 },
  ];

  const tiempoSlides = [
    70, 65, 120, 58, 105, 67, 80, 73, 69, 72, 62, 64, 58, 54,
  ];

  const getBarColor = (index) => {
    if (index === 2) return "#fb7185";
    if (index === 4) return "#fbbf24";
    if (index >= 7) return "#22c55e";
    return "#6366f1";
  };

  const barColors = tiempoSlides.map((_, idx) => getBarColor(idx));

  const chartData = {
    labels: tiempoSlides.map((_, i) => (i + 1).toString()),
    datasets: [
      {
        label: "Segundos",
        data: tiempoSlides,
        backgroundColor: barColors,
        borderRadius: 8,
        borderSkipped: false,
      },
    ],
  };

  const chartOptions = {
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (ctx) => ` ${ctx.parsed.y}s`,
        },
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 130,
        grid: { color: "#ede9fe" },
        ticks: { color: "#3730a3", stepSize: 20 },
      },
      x: {
        grid: { display: false },
        ticks: { color: "#6366f1" },
      },
    },
  };

  return (
    <div className="feedback-bg">
      <div className="feedback-container">
        <div className="muletillas-section">
          <span className="muletillas-label">Muletillas más frecuentes:</span>
          {muletillas.map((m) => (
            <span className="muletilla-pill" key={m.word}>
              {m.word} <b>{m.count}</b>
            </span>
          ))}
        </div>

        <div className="chart-section">
          <div className="chart-title">Análisis de Tiempo por Diapositiva</div>
          <Bar data={chartData} options={chartOptions} height={220} />

          <div className="chart-observaciones">
            <div>
              <span className="legend-dot rojo"></span>
              La diapositiva 3 excedió significativamente el tiempo recomendado (120s vs 60s).
            </div>
            <div>
              <span className="legend-dot amarillo"></span>
              La diapositiva 5 estuvo ligeramente por encima del tiempo óptimo (105s).
            </div>
            <div>
              <span className="legend-dot verde"></span>
              Las diapositivas finales (8-14) se mantuvieron dentro del tiempo recomendado.
            </div>
          </div>
        </div>

        <div className="recomendaciones-section">
          <div className="recomendaciones-title">Recomendaciones para Mejorar</div>
          <ul>
            <li>
              <b className="blue-link">Reducir muletillas</b>
              <br />
              Practica siendo consciente de las palabras “eh” y “este”. Intenta hacer pausas silenciosas en lugar de usar muletillas cuando necesites pensar.
            </li>
            <li>
              <b className="blue-link">Equilibrar el tiempo por diapositiva</b>
              <br />
              Dedica menos tiempo a la diapositiva 3. Considera dividir ese contenido en dos diapositivas o simplificarlo para mantener un ritmo más constante.
            </li>
            <li>
              <b className="blue-link">Utilizar pausas estratégicas</b>
              <br />
              Incorpora pausas intencionales después de puntos importantes para permitir que la audiencia procese la información. Esto también te ayudará a reducir el uso de muletillas.
            </li>
          </ul>
        </div>

        <div className="proximos-section">
          <div className="proximos-title">Próximos Pasos</div>
          <ul>
            <li>Revisa la grabación de tu presentación con los puntos destacados.</li>
            <li>Practica nuevamente enfocándote en las áreas de mejora identificadas.</li>
            <li>Programa una nueva sesión de práctica para medir tu progreso.</li>
          </ul>
        </div>

        <div className="btn-feedback-row">
          <button className="btn-practicar-nuevamente">
            <span>&#9654;</span> Practicar Nuevamente
          </button>
        </div>
      </div>
    </div>
  );
}
