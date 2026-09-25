from pydantic import BaseModel


class LaptopInput(BaseModel):

    Company: str
    Product: str
    TypeName: str
    Inches: float
    ScreenResolution: str
    Cpu: str
    Ram: str
    Memory: str
    Gpu: str
    OpSys: str
    Weight: str