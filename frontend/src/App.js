import { useState } from "react";
import "./App.css";


function App() {
  const [math, setMath] = useState("");
  const [science, setScience] = useState("");
  const [english, setEnglish] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log({ math, science, english });

    const response = await fetch("http://localhost:8000/api/predict/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
  math: parseInt(math),
  science: parseInt(science),
  english: parseInt(english),
}),

    });

    const data = await response.json();
    setResult(data.result);
  };
return (
  <div className="container">
    <h2>Student Performance Predictor</h2>
    <form onSubmit={handleSubmit}>
      <input type="number" placeholder="Math" value={math} onChange={(e) => setMath(e.target.value)} required />
      <input type="number" placeholder="Science" value={science} onChange={(e) => setScience(e.target.value)} required />
      <input type="number" placeholder="English" value={english} onChange={(e) => setEnglish(e.target.value)} required />
      <button type="submit">Predict</button>
    </form>
    {result && <div className="result">Result: {result}</div>}
  </div>
);

}

export default App;
