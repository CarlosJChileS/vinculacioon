import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';

function Home() {
  return <h2>Bienvenido a ExposIA</h2>;
}

function Presentaciones() {
  return <h2>Módulo de Presentaciones</h2>;
}

function Practicas() {
  return <h2>Módulo de Prácticas</h2>;
}

function IA() {
  return <h2>Módulo de IA</h2>;
}

function Calificacion() {
  return <h2>Módulo de Calificación</h2>;
}

export default function App() {
  return (
    <div>
      <nav>
        <Link to="/">Inicio</Link> |{' '}
        <Link to="/presentaciones">Presentaciones</Link> |{' '}
        <Link to="/practicas">Prácticas</Link> |{' '}
        <Link to="/ia">IA</Link> |{' '}
        <Link to="/calificacion">Calificación</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/presentaciones" element={<Presentaciones />} />
        <Route path="/practicas" element={<Practicas />} />
        <Route path="/ia" element={<IA />} />
        <Route path="/calificacion" element={<Calificacion />} />
      </Routes>
    </div>
  );
}
