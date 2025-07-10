import React, { useState } from "react";

export default function DemoFlowPage() {
  const [log, setLog] = useState([]);
  const addLog = (msg) => setLog((l) => [...l, msg]);

  const runDemo = async () => {
    setLog([]);
    try {
      // Paso 1: Registro del Usuario
      addLog("Registrando usuaria...");
      await fetch("http://localhost:8000/presentaciones/users/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre: "Ana Pérez", email: "ana@example.com", password: "demo" })
      });
      addLog("Usuario registrado");

      // Paso 2: Subida de Presentación
      addLog("Subiendo presentación...");
      const pdf = new Blob(["dummy"], { type: "application/pdf" });
      const form = new FormData();
      form.append("file", pdf, "ia.pdf");
      await fetch("http://localhost:8000/presentaciones/upload", { method: "POST", body: form });
      addLog("Presentación subida");

      // Paso 3: Generación de Slides (simulado)
      addLog("Generando slides...");
      const slides = ["¿Qué es la IA?", "Aplicaciones de la IA"];
      addLog(`Slides generados: ${slides.join(" | ")}`);

      // Paso 4: Práctica de Exposición (simulada)
      addLog("Enviando grabación...");
      const audioBlob = new Blob(["dummy"], { type: "audio/wav" });
      const audioForm = new FormData();
      audioForm.append("audio", audioBlob, "grab1.mp3");
      const iaRes = await fetch("http://localhost:8000/ia/analisis", { method: "POST", body: audioForm });
      const iaData = await iaRes.json();
      addLog(`Resultados IA: claridad ${iaData.claridad}, velocidad ${iaData.velocidad_palabras}, pausas ${iaData.num_pausas}`);

      // Paso 5: Calificación Final
      addLog("Calculando calificación...");
      const gradeRes = await fetch("http://localhost:8000/calificacion/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          velocidad_palabras: iaData.velocidad_palabras,
          claridad: iaData.claridad,
          num_pausas: iaData.num_pausas
        })
      });
      const grade = await gradeRes.json();
      addLog(`Calificación: ${grade.nota_global}`);
    } catch (err) {
      addLog("Error: " + err.message);
    }
  };

  return (
    <div>
      <h2>Demo del Flujo Completo</h2>
      <button onClick={runDemo}>Ejecutar Demo</button>
      <pre style={{ background: '#f4f4f5', padding: '1em' }}>
        {log.map((l, i) => (<div key={i}>{l}</div>))}
      </pre>
    </div>
  );
}
