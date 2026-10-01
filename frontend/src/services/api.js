const API_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api";

export async function predictLaptopPrice(laptopData) {
    try {
        const response = await fetch(`${API_BASE}/predict`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(laptopData)
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => null);
            throw new Error(
                errorData?.detail || `Prediction request failed with status ${response.status}`
            );
        }

        return await response.json();
    } catch (error) {
        // Attempt fallback through relative /api if direct connection had network error
        if (API_BASE.startsWith("http")) {
            try {
                const retryResponse = await fetch("/api/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(laptopData)
                });
                if (retryResponse.ok) {
                    return await retryResponse.json();
                }
            } catch {
                // fall through to throw original error
            }
        }
        throw error;
    }
}