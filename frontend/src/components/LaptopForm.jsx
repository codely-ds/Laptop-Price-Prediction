import { useState } from "react";
import { predictLaptopPrice } from "../services/api";

const PRESETS = [
    {
        name: "💻 Everyday Laptop (Dell Inspiron)",
        data: {
            Company: "Dell",
            Product: "Inspiron 3567",
            TypeName: "Notebook",
            Inches: 15.6,
            ScreenResolution: "Full HD 1920x1080",
            Cpu: "Intel Core i5 7200U 2.5GHz",
            Ram: "8GB",
            Memory: "256GB SSD",
            Gpu: "Intel HD Graphics 620",
            OpSys: "Windows 10",
            Weight: "1.86kg"
        }
    },
    {
        name: "⚡ Apple MacBook Pro 13",
        data: {
            Company: "Apple",
            Product: "MacBook Pro",
            TypeName: "Ultrabook",
            Inches: 13.3,
            ScreenResolution: "IPS Panel Retina Display 2560x1600",
            Cpu: "Intel Core i5 2.3GHz",
            Ram: "8GB",
            Memory: "128GB SSD",
            Gpu: "Intel Iris Plus Graphics 640",
            OpSys: "macOS",
            Weight: "1.37kg"
        }
    },
    {
        name: "🎮 Asus ROG Gaming Rig",
        data: {
            Company: "Asus",
            Product: "ROG GL553VE",
            TypeName: "Gaming",
            Inches: 15.6,
            ScreenResolution: "Full HD 1920x1080",
            Cpu: "Intel Core i7 7700HQ 2.8GHz",
            Ram: "16GB",
            Memory: "128GB SSD + 1TB HDD",
            Gpu: "Nvidia GeForce GTX 1050 Ti",
            OpSys: "Windows 10",
            Weight: "2.5kg"
        }
    },
    {
        name: "💼 Lenovo ThinkPad Business",
        data: {
            Company: "Lenovo",
            Product: "ThinkPad T470",
            TypeName: "Notebook",
            Inches: 14.0,
            ScreenResolution: "Full HD 1920x1080",
            Cpu: "Intel Core i7 7500U 2.7GHz",
            Ram: "16GB",
            Memory: "512GB SSD",
            Gpu: "Intel HD Graphics 620",
            OpSys: "Windows 10",
            Weight: "1.65kg"
        }
    }
];

const COMPANIES = ["Dell", "Lenovo", "HP", "Asus", "Acer", "MSI", "Apple", "Toshiba", "Samsung", "Razer", "Medion", "Microsoft", "Xiaomi", "Huawei"];
const TYPE_NAMES = ["Notebook", "Ultrabook", "Gaming", "2 in 1 Convertible", "Workstation", "Netbook"];
const RAM_OPTIONS = ["4GB", "6GB", "8GB", "12GB", "16GB", "24GB", "32GB", "64GB"];
const RESOLUTIONS = [
    "Full HD 1920x1080",
    "1366x768",
    "IPS Panel Full HD 1920x1080",
    "IPS Panel Retina Display 2560x1600",
    "IPS Panel 4K Ultra HD 3840x2160",
    "Quad HD+ 3200x1800",
    "Touchscreen Full HD 1920x1080",
    "Touchscreen 1366x768"
];
const STORAGE_OPTIONS = [
    "256GB SSD",
    "512GB SSD",
    "1TB SSD",
    "1TB HDD",
    "500GB HDD",
    "128GB SSD + 1TB HDD",
    "256GB SSD + 1TB HDD",
    "512GB SSD + 1TB HDD",
    "128GB Flash Storage",
    "64GB Flash Storage"
];
const OP_SYS_OPTIONS = ["Windows 10", "macOS", "Linux", "No OS", "Chrome OS", "Windows 10 S", "Windows 7"];

function LaptopForm({ setResult, setSubmittedData }) {
    const [formData, setFormData] = useState({
        Company: "Dell",
        Product: "Inspiron 3567",
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
        setFormData(prev => ({
            ...prev,
            [name]: name === "Inches" ? (value === "" ? "" : parseFloat(value) || value) : value
        }));
    }

    function applyPreset(preset) {
        setFormData({ ...preset.data });
        setError("");
    }

    async function handleSubmit(event) {
        event.preventDefault();
        setLoading(true);
        setError("");
        setResult(null);

        try {
            // Format weight and inches cleanly
            const payload = {
                ...formData,
                Inches: parseFloat(formData.Inches) || 15.6,
                Weight: formData.Weight.toString().includes("kg") 
                    ? formData.Weight 
                    : `${formData.Weight}kg`
            };

            const result = await predictLaptopPrice(payload);
            setResult(result);
            if (setSubmittedData) {
                setSubmittedData(payload);
            }
        } catch (err) {
            setError(
                err.message || "Unable to predict price. Please check if the FastAPI backend server is running on port 8000."
            );
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="form-container">
            <div className="presets-section">
                <span className="presets-label">⚡ Quick Presets:</span>
                <div className="preset-buttons">
                    {PRESETS.map((preset, idx) => (
                        <button
                            key={idx}
                            type="button"
                            className="preset-btn"
                            onClick={() => applyPreset(preset)}
                        >
                            {preset.name}
                        </button>
                    ))}
                </div>
            </div>

            <form className="laptop-form" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="company">Brand / Company</label>
                    <select
                        id="company"
                        name="Company"
                        value={formData.Company}
                        onChange={handleChange}
                        required
                    >
                        {COMPANIES.map(c => <option key={c} value={c}>{c}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="product">Model / Product Name</label>
                    <input
                        id="product"
                        name="Product"
                        placeholder="e.g. Inspiron, XPS 13, Pavilion"
                        value={formData.Product}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="typeName">Laptop Category</label>
                    <select
                        id="typeName"
                        name="TypeName"
                        value={formData.TypeName}
                        onChange={handleChange}
                        required
                    >
                        {TYPE_NAMES.map(t => <option key={t} value={t}>{t}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="inches">Screen Size (Inches)</label>
                    <input
                        id="inches"
                        name="Inches"
                        type="number"
                        step="0.1"
                        min="10"
                        max="20"
                        placeholder="15.6"
                        value={formData.Inches}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="screenResolution">Screen Resolution</label>
                    <input
                        id="screenResolution"
                        name="ScreenResolution"
                        list="resolutions-list"
                        placeholder="e.g. Full HD 1920x1080"
                        value={formData.ScreenResolution}
                        onChange={handleChange}
                        required
                    />
                    <datalist id="resolutions-list">
                        {RESOLUTIONS.map(r => <option key={r} value={r} />)}
                    </datalist>
                </div>

                <div className="form-group">
                    <label htmlFor="cpu">Processor (CPU)</label>
                    <input
                        id="cpu"
                        name="Cpu"
                        list="cpu-list"
                        placeholder="e.g. Intel Core i5 7200U 2.5GHz"
                        value={formData.Cpu}
                        onChange={handleChange}
                        required
                    />
                    <datalist id="cpu-list">
                        <option value="Intel Core i5 7200U 2.5GHz" />
                        <option value="Intel Core i7 7700HQ 2.8GHz" />
                        <option value="Intel Core i7 8550U 1.8GHz" />
                        <option value="Intel Core i3 6006U 2GHz" />
                        <option value="AMD Ryzen 5 2500U 2GHz" />
                        <option value="AMD A9-Series 9420 3GHz" />
                        <option value="Intel Core i5 2.3GHz" />
                        <option value="Intel Celeron Dual Core N3060 1.6GHz" />
                    </datalist>
                </div>

                <div className="form-group">
                    <label htmlFor="ram">RAM Memory</label>
                    <select
                        id="ram"
                        name="Ram"
                        value={formData.Ram}
                        onChange={handleChange}
                        required
                    >
                        {RAM_OPTIONS.map(r => <option key={r} value={r}>{r}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="memory">Storage (SSD / HDD)</label>
                    <input
                        id="memory"
                        name="Memory"
                        list="storage-list"
                        placeholder="e.g. 256GB SSD or 1TB HDD"
                        value={formData.Memory}
                        onChange={handleChange}
                        required
                    />
                    <datalist id="storage-list">
                        {STORAGE_OPTIONS.map(s => <option key={s} value={s} />)}
                    </datalist>
                </div>

                <div className="form-group">
                    <label htmlFor="gpu">Graphics Card (GPU)</label>
                    <input
                        id="gpu"
                        name="Gpu"
                        list="gpu-list"
                        placeholder="e.g. Intel HD Graphics 620, Nvidia GeForce GTX 1050"
                        value={formData.Gpu}
                        onChange={handleChange}
                        required
                    />
                    <datalist id="gpu-list">
                        <option value="Intel HD Graphics 620" />
                        <option value="Intel UHD Graphics 620" />
                        <option value="Nvidia GeForce GTX 1050" />
                        <option value="Nvidia GeForce GTX 1060" />
                        <option value="Nvidia GeForce MX150" />
                        <option value="Intel Iris Plus Graphics 640" />
                        <option value="AMD Radeon R5" />
                        <option value="AMD Radeon 530" />
                    </datalist>
                </div>

                <div className="form-group">
                    <label htmlFor="opSys">Operating System</label>
                    <select
                        id="opSys"
                        name="OpSys"
                        value={formData.OpSys}
                        onChange={handleChange}
                        required
                    >
                        {OP_SYS_OPTIONS.map(o => <option key={o} value={o}>{o}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="weight">Weight (kg)</label>
                    <input
                        id="weight"
                        name="Weight"
                        placeholder="e.g. 1.86kg"
                        value={formData.Weight}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-actions">
                    <button
                        type="submit"
                        className="submit-btn"
                        disabled={loading}
                    >
                        {loading ? (
                            <span className="spinner-text">
                                <span className="spinner" /> Calculating Estimate...
                            </span>
                        ) : (
                            "⚡ Calculate Predicted Price"
                        )}
                    </button>
                </div>

                {error && (
                    <div className="error-banner">
                        <span className="error-icon">⚠️</span>
                        <div className="error-text">{error}</div>
                    </div>
                )}
            </form>
        </div>
    );
}

export default LaptopForm;