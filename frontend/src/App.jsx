import { useState, useEffect } from "react";
import LaptopForm from "./components/LaptopForm";
import PredictionResult from "./components/PredictionResult";

function App() {
    const [result, setResult] = useState(null);
    const [submittedData, setSubmittedData] = useState(null);
    const [apiStatus, setApiStatus] = useState("checking");

    useEffect(() => {
        // Quick healthcheck on load
        fetch("http://127.0.0.1:8000/health")
            .then(res => res.json())
            .then(data => {
                if (data.status === "healthy") setApiStatus("online");
                else setApiStatus("offline");
            })
            .catch(() => {
                // Fallback check through proxy
                fetch("/health")
                    .then(res => res.json())
                    .then(data => {
                        if (data.status === "healthy") setApiStatus("online");
                        else setApiStatus("offline");
                    })
                    .catch(() => setApiStatus("offline"));
            });
    }, []);

    return (
        <div className="app">
            <header className="app-header">
                <div className="header-badge">
                    <span className={`status-dot ${apiStatus}`} />
                    <span>ML Backend: {apiStatus === "online" ? "Connected" : apiStatus === "checking" ? "Connecting..." : "Offline (Port 8000)"}</span>
                </div>
                <h1>Laptop Price Valuation AI</h1>
                <p className="header-subtitle">
                    Estimate accurate market prices using Random Forest & Gradient Boosting regression trained on comprehensive laptop hardware metrics.
                </p>
            </header>

            <main className="app-main">
                <LaptopForm
                    setResult={setResult}
                    setSubmittedData={setSubmittedData}
                />

                <PredictionResult
                    result={result}
                    submittedData={submittedData}
                />
            </main>

            <footer className="app-footer">
                <p>Built with FastAPI, Scikit-Learn, and React + Vite</p>
            </footer>
        </div>
    );
}

export default App;