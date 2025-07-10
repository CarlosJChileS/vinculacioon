import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import HomePage from './HomePage';
import DashboardPage from './DashboardPage';
import PracticePage from './PracticePage';
import PracticeFeedbackPage from './PracticeFeedbackPage';

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
