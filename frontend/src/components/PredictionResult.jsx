function PredictionResult({ result, submittedData }) {
    if (!result) {
        return null;
    }

    const price = result.predicted_price ?? result.predict_price ?? 0;
    // Approximate USD conversion for helpful context
    const approxUsd = Math.round(price * 1.08);
    // Approximate INR conversion for global context
    const approxInr = Math.round(price * 90);

    return (
        <div className="prediction-result animate-fade-in">
            <div className="result-header">
                <span className="result-badge">AI Valuation Result</span>
                <h2>Estimated Market Value</h2>
            </div>

            <div className="price-display">
                <div className="price-main">
                    <span className="currency-symbol">€</span>
                    <span className="price-number">{price.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
                </div>
                <div className="price-sub">
                    <span>≈ ${approxUsd.toLocaleString()} USD</span>
                    <span className="dot-divider">•</span>
                    <span>≈ ₹{approxInr.toLocaleString()} INR</span>
                </div>
            </div>

            {submittedData && (
                <div className="specs-summary">
                    <h3>Evaluated Specifications</h3>
                    <div className="specs-grid">
                        <div className="spec-item">
                            <span className="spec-label">Model</span>
                            <span className="spec-value">{submittedData.Company} {submittedData.Product}</span>
                        </div>
                        <div className="spec-item">
                            <span className="spec-label">Category</span>
                            <span className="spec-value">{submittedData.TypeName}</span>
                        </div>
                        <div className="spec-item">
                            <span className="spec-label">Processor</span>
                            <span className="spec-value">{submittedData.Cpu}</span>
                        </div>
                        <div className="spec-item">
                            <span className="spec-label">RAM & Storage</span>
                            <span className="spec-value">{submittedData.Ram} • {submittedData.Memory}</span>
                        </div>
                        <div className="spec-item">
                            <span className="spec-label">Display</span>
                            <span className="spec-value">{submittedData.Inches}" ({submittedData.ScreenResolution})</span>
                        </div>
                        <div className="spec-item">
                            <span className="spec-label">GPU & OS</span>
                            <span className="spec-value">{submittedData.Gpu} • {submittedData.OpSys}</span>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default PredictionResult;