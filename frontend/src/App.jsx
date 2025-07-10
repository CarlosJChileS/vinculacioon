import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import HomePage from './HomePage';
import DashboardPage from './DashboardPage';
import PracticePage from './PracticePage';
import PracticeFeedbackPage from './PracticeFeedbackPage';

function Home() {
  return <h2>Bienvenido a ExposIA</h2>;
}

function Presentaciones() {
  const [file, setFile] = React.useState(null);
  const handleSubmit = async () => {
    if (!file) return;
    const data = new FormData();
    data.append('file', file);
    await fetch('http://localhost:8000/presentaciones/upload', {
      method: 'POST',
      body: data,
    });
    alert('PDF subido');
  };
  return (
    <div>
      <h2>Subir Presentación</h2>
      <input type="file" accept="application/pdf" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleSubmit}>Enviar</button>
    </div>
  );
}

function Practicas() {
  return <h2>Módulo de Prácticas</h2>;
}

function IA() {
  const [recorder, setRecorder] = React.useState(null);
  const [recording, setRecording] = React.useState(false);
  const [result, setResult] = React.useState(null);

  const start = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const rec = new MediaRecorder(stream);
    const chunks = [];
    rec.ondataavailable = e => chunks.push(e.data);
    rec.onstop = async () => {
      const blob = new Blob(chunks, { type: 'audio/wav' });
      const data = new FormData();
      data.append('audio', blob, 'recording.wav');
      const res = await fetch('http://localhost:8000/ia/analisis', {
        method: 'POST',
        body: data,
      });
      setResult(await res.json());
    };
    rec.start();
    setRecorder(rec);
    setRecording(true);
  };

  const stop = () => {
    recorder.stop();
    setRecording(false);
  };

  return (
    <div>
      <h2>Analizar Audio</h2>
      {!recording ? (
        <button onClick={start}>Grabar</button>
      ) : (
        <button onClick={stop}>Detener</button>
      )}
      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

function Calificacion() {
  return <h2>Módulo de Calificación</h2>;
}

export default function App() {
  return (
    <div>
      <nav>
        <Link to="/">Inicio</Link> |{' '}
        <Link to="/dashboard">Dashboard</Link> |{' '}
        <Link to="/practicar">Práctica</Link> |{' '}
        <Link to="/feedback">Feedback</Link>
      </nav>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/practicar" element={<PracticePage />} />
        <Route path="/feedback" element={<PracticeFeedbackPage />} />
      </Routes>
    </div>
  );
}
