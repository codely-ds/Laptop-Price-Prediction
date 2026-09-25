const API_URL = "http://localhost:8000/api";

export async function predictLaptopPrice(laptopData) {
    const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(laptopData)
    });

    if (!response.ok) {
        throw new Error("Prediction request failed");
    }

    return await response.json();
}