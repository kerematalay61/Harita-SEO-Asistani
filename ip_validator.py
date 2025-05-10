"""
Proxy adreslerinin çalışıp çalışmadığını test eder.
"""
import requests

def validate_proxy(proxy):
    try:
        response = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
        return response.status_code == 200
    except Exception:
        return False
is_valid = validate_proxy("http://proxy1.example.com:8000")
print("Geçerli" if is_valid else "Geçersiz")
