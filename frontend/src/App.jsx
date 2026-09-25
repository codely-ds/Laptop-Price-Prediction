import { useState } from "react";

import LaptopForm
    from "./components/LaptopForm";

import PredictionResult
    from "./components/PredictionResult";


function App() {

    const [result, setResult] = useState(null);


    return (

        <div className="app">

            <header>

                <h1>
                    💻 Laptop Price Predictor
                </h1>

                <p>
                    Predict laptop prices using
                    Machine Learning
                </p>

            </header>


            <main>

                <LaptopForm
                    setResult={setResult}
                />

                <PredictionResult
                    result={result}
                />

            </main>

        </div>
    );
}


export default App;