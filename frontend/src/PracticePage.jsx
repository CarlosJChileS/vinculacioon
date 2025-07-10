import React, { useState } from "react";
import "./PracticePage.css";

const slidesMock = [
  { title: "Introducción a la Inteligencia Artificial", content: "La inteligencia artificial (IA) es una rama de la informática..." },
  { title: "Historia de la IA", content: "La IA tiene sus orígenes en los años 50..." },
  { title: "Aplicaciones actuales", content: "Hoy en día la IA se utiliza en..." },
];

export default function PracticePage() {
  const [slide, setSlide] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [recording, setRecording] = useState(false);

  const totalTime = "02:45";

  return (
    <div className="practice-bg">
      {/* Top bar */}
      <div className="practice-topbar">
        <div>
          <div className="practice-title">{slidesMock[slide].title}</div>
          <div className="practice-progress">Diapositiva {slide + 1} de {slidesMock.length}</div>
        </div>
        <div className="practice-timer">
          <span className="practice-timer-dot"></span>
          <span>En tránsito · {totalTime}</span>
        </div>
        <button className="practice-exit">Salir</button>
      </div>

      {/* Main slide area */}
      <div className="practice-slide-area">
        <div className="practice-slide-content">
          <div className="slide-content">
            {slidesMock[slide].content}
          </div>
        </div>
        <div className="practice-controls">
          <button onClick={() => setSlide(slide - 1)} disabled={slide === 0}>
            <span>&lt;</span>
          </button>
          <button
            className="practice-play"
            onClick={() => setIsPlaying(!isPlaying)}
          >
            {isPlaying ? (
              <span className="pause-icon">&#10073;&#10073;</span>
            ) : (
              <span className="play-icon">&#9658;</span>
            )}
          </button>
          <button onClick={() => setSlide(slide + 1)} disabled={slide === slidesMock.length - 1}>
            <span>&gt;</span>
          </button>
          <button title="Ver todas las slides">
            <i className="fas fa-th"></i>
          </button>
          <button title="Mostrar/ocultar notas">
            <i className="fas fa-sticky-note"></i>
          </button>
        </div>
      </div>

      {/* Bottom bar - Recording */}
      <div className="practice-bottom-bar">
        <div>
          Diapositiva <b>{slide + 1}</b> / {slidesMock.length}
        </div>
        <button
          className={recording ? "btn-recording" : "btn-record"}
          onClick={() => setRecording(!recording)}
        >
          {recording ? "Grabando..." : "Empezar grabación"}
        </button>
      </div>
    </div>
  );
}
