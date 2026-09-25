import re
import pandas as pd


def extract_cpu_brand(cpu):
    if "Intel" in cpu:
        return "Intel"
    elif "AMD" in cpu:
        return "AMD"
    elif "Samsung" in cpu:
        return "Samsung"
    else:
        return "Other"


def extract_cpu_speed(cpu):

    match = re.search(r"(\d+(?:\.\d+)?)GHz", cpu)

    if match:
        return float(match.group(1))

    return 0.0


def extract_screen_width(resolution):

    match = re.search(r"(\d+)x(\d+)", resolution)

    if match:
        return int(match.group(1))

    return 0


def extract_screen_height(resolution):

    match = re.search(r"(\d+)x(\d+)", resolution)

    if match:
        return int(match.group(2))

    return 0


def extract_storage(memory):

    memory = memory.lower()

    ssd = 0
    hdd = 0
    flash = 0
    hybrid = 0

    if "ssd" in memory:
        match = re.search(r"(\d+(?:\.\d+)?)gb", memory)

        if match:
            ssd = float(match.group(1))

    if "hdd" in memory:
        match = re.search(r"(\d+(?:\.\d+)?)tb", memory)

        if match:
            hdd = float(match.group(1)) * 1024

        else:
            match = re.search(r"(\d+(?:\.\d+)?)gb", memory)

            if match:
                hdd = float(match.group(1))

    if "flash" in memory:
        match = re.search(r"(\d+(?:\.\d+)?)gb", memory)

        if match:
            flash = float(match.group(1))

    if "hybrid" in memory:
        match = re.search(r"(\d+(?:\.\d+)?)tb", memory)

        if match:
            hybrid = float(match.group(1)) * 1024

    return pd.Series([
        ssd,
        hdd,
        flash,
        hybrid
    ])


def feature_engineering(df):

    df = df.copy()

    # CPU features
    df["CPU_Brand"] = df["Cpu"].apply(extract_cpu_brand)

    df["CPU_Speed"] = df["Cpu"].apply(extract_cpu_speed)

    # Screen resolution
    df["Screen_Width"] = (
        df["ScreenResolution"]
        .apply(extract_screen_width)
    )

    df["Screen_Height"] = (
        df["ScreenResolution"]
        .apply(extract_screen_height)
    )

    # Screen features
    df["Touchscreen"] = (
        df["ScreenResolution"]
        .str.contains(
            "Touchscreen",
            case=False,
            regex=False
        )
        .astype(int)
    )

    df["IPS"] = (
        df["ScreenResolution"]
        .str.contains(
            "IPS",
            case=False,
            regex=False
        )
        .astype(int)
    )

    # Storage
    storage_features = df["Memory"].apply(
        extract_storage
    )

    storage_features.columns = [
        "SSD_GB",
        "HDD_GB",
        "Flash_GB",
        "Hybrid_GB"
    ]

    df = pd.concat(
        [df, storage_features],
        axis=1
    )

    return df