import { useState } from "react";
import { predictLaptopPrice } from "../services/api";


function LaptopForm({ setResult }) {

    const [formData, setFormData] = useState({

        Company: "Dell",
        Product: "Inspiron",
        TypeName: "Notebook",
        Inches: 15.6,
        ScreenResolution: "Full HD 1920x1080",
        Cpu: "Intel Core i5 7200U 2.5GHz",
        Ram: "8GB",
        Memory: "256GB SSD",
        Gpu: "Intel HD Graphics 620",
        OpSys: "Windows 10",
        Weight: "1.86kg"
    });


    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");


    function handleChange(event) {

        const { name, value } = event.target;

        setFormData({
            ...formData,
            [name]: value
        });
    }


    async function handleSubmit(event) {

        event.preventDefault();

        setLoading(true);
        setError("");
        setResult(null);

        try {

            const result =
                await predictLaptopPrice(formData);

            setResult(result);

        } catch (error) {

            setError(
                "Unable to predict price. Check whether the FastAPI server is running."
            );

        } finally {

            setLoading(false);
        }
    }


    return (

        <form
            className="laptop-form"
            onSubmit={handleSubmit}
        >

            <input
                name="Company"
                placeholder="Company"
                value={formData.Company}
                onChange={handleChange}
            />

            <input
                name="Product"
                placeholder="Product"
                value={formData.Product}
                onChange={handleChange}
            />

            <input
                name="TypeName"
                placeholder="Laptop Type"
                value={formData.TypeName}
                onChange={handleChange}
            />

            <input
                name="Inches"
                type="number"
                step="0.1"
                placeholder="Screen Size"
                value={formData.Inches}
                onChange={handleChange}
            />

            <input
                name="ScreenResolution"
                placeholder="Screen Resolution"
                value={formData.ScreenResolution}
                onChange={handleChange}
            />

            <input
                name="Cpu"
                placeholder="CPU"
                value={formData.Cpu}
                onChange={handleChange}
            />

            <input
                name="Ram"
                placeholder="RAM"
                value={formData.Ram}
                onChange={handleChange}
            />

            <input
                name="Memory"
                placeholder="Storage"
                value={formData.Memory}
                onChange={handleChange}
            />

            <input
                name="Gpu"
                placeholder="GPU"
                value={formData.Gpu}
                onChange={handleChange}
            />

            <input
                name="OpSys"
                placeholder="Operating System"
                value={formData.OpSys}
                onChange={handleChange}
            />

            <input
                name="Weight"
                placeholder="Weight"
                value={formData.Weight}
                onChange={handleChange}
            />

            <button
                type="submit"
                disabled={loading}
            >

                {loading
                    ? "Predicting..."
                    : "Predict Laptop Price"
                }

            </button>


            {error && (
                <p className="error">
                    {error}
                </p>
            )}

        </form>
    );
}


export default LaptopForm;