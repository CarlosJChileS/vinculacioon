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
      const presRes = await fetch("http://localhost:8000/presentaciones/upload", { method: "POST", body: form });
      const presData = await presRes.json();
      addLog("Presentación subida");

      // Paso 3: Generación de Slides
      addLog("Generando slides...");
      const slides = ["¿Qué es la IA?", "Aplicaciones de la IA"];
      for (let i = 0; i < slides.length; i++) {
        await fetch("http://localhost:8000/presentaciones/slides/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ presentacion_id: 1, numero_slide: i + 1, texto_slide: slides[i] }),
        });
      }
      addLog(`Slides generados: ${slides.join(" | ")}`);

      // Paso 4: Práctica de Exposición
      addLog("Enviando grabación...");
      const audioBlob = new Blob(["dummy"], { type: "audio/wav" });
      const audioForm = new FormData();
      audioForm.append("audio", audioBlob, "grab1.wav");
      const recRes = await fetch("http://localhost:8000/practicas/recordings/upload?usuario_id=1&presentacion_id=1", {
        method: "POST",
        body: audioForm,
      });
      const recData = await recRes.json();
      await fetch("http://localhost:8000/practicas/navigation/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ presentacion_id: 1, slide_id: 1, timestamp: 0, tipo_navegacion: "start" }),
      });
      await fetch("http://localhost:8000/practicas/navigation/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ presentacion_id: 1, slide_id: 2, timestamp: 30, tipo_navegacion: "next" }),
      });
      const iaRes = await fetch(`http://localhost:8000/ia/analisis/grabaciones/${recData.id}`, { method: "POST" });
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
