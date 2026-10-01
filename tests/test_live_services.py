import urllib.request
import json

def test_api():
    url = "http://127.0.0.1:8000/api/predict"
    payload = {
        "Company": "Apple",
        "Product": "MacBook Pro",
        "TypeName": "Ultrabook",
        "Inches": 13.3,
        "ScreenResolution": "IPS Panel Retina Display 2560x1600",
        "Cpu": "Intel Core i5 2.3GHz",
        "Ram": "8GB",
        "Memory": "128GB SSD",
        "Gpu": "Intel Iris Plus Graphics 640",
        "OpSys": "macOS",
        "Weight": "1.37kg"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        print("Backend Response Status:", res.status)
        print("Backend Response Body:", response_body)

def test_frontend():
    url = "http://127.0.0.1:5173"
    with urllib.request.urlopen(url) as res:
        print("Frontend Response Status:", res.status)

if __name__ == "__main__":
    print("Testing Backend...")
    test_api()
    print("\nTesting Frontend...")
    test_frontend()
    print("\nALL HTTP CHECKS PASSED SUCCESSFULLY!")
