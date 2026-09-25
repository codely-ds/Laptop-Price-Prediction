function PredictionResult ({ result }) {

    if (!result) {
        return null;
    }

    return (
        
        <div className = "prediction-result">

            <h2>
                Prediction Laptop Price
            </h2>

            <div className="Price">
                €{result.predicted_price ?? result.predict_price}
            </div>

            <p>
                Currency : {result.currency}
            </p>

        </div>
    );
}

export default PredictionResult;