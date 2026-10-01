from pydantic import BaseModel, Field, ConfigDict


class LaptopInput(BaseModel):
    Company: str = Field(..., description="Brand of the laptop (e.g. Dell, HP, Apple, Lenovo)")
    Product: str = Field(..., description="Laptop model name (e.g. Inspiron, MacBook Pro)")
    TypeName: str = Field(..., description="Laptop category (e.g. Notebook, Ultrabook, Gaming)")
    Inches: float = Field(..., description="Screen size in inches (e.g. 15.6, 13.3, 14.0)")
    ScreenResolution: str = Field(..., description="Display resolution (e.g. Full HD 1920x1080)")
    Cpu: str = Field(..., description="Processor specifications (e.g. Intel Core i5 7200U 2.5GHz)")
    Ram: str = Field(..., description="RAM size with unit (e.g. 8GB, 16GB)")
    Memory: str = Field(..., description="Storage specs (e.g. 256GB SSD, 1TB HDD, 512GB SSD)")
    Gpu: str = Field(..., description="Graphics card (e.g. Intel HD Graphics 620, Nvidia GeForce GTX 1050)")
    OpSys: str = Field(..., description="Operating system (e.g. Windows 10, macOS, Linux)")
    Weight: str = Field(..., description="Weight with unit (e.g. 1.86kg, 2.1kg)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "Company": "Dell",
                "Product": "Inspiron 3567",
                "TypeName": "Notebook",
                "Inches": 15.6,
                "ScreenResolution": "Full HD 1920x1080",
                "Cpu": "Intel Core i5 7200U 2.5GHz",
                "Ram": "8GB",
                "Memory": "256GB SSD",
                "Gpu": "Intel HD Graphics 620",
                "OpSys": "Windows 10",
                "Weight": "1.86kg"
            }
        }
    )