import requests
import json

BASE = "https://httpbin.org"

def print_resp(label, resp):
    print(f"\n=== {label} ===")
    print(f"Status: {resp.status_code}")
    print(f"Content-Type: {resp.headers.get('Content-Type')}")
    # Try to parse JSON if possible
    if 'application/json' in resp.headers.get('Content-Type', ''):
        try:
            data = resp.json()
            print("JSON:")
            print(json.dumps(data, indent=2))
        except Exception as e:
            print("Failed to parse JSON:", e)
            print("Raw text:", resp.text[:200])
    else:
        print("Body (first 200 chars):")
        print(resp.text[:200])

# GET
r = requests.get(f"{BASE}/get", params={"q": "test"})
print_resp("GET", r)

# POST
payload = {"name": "Ada", "age": 30}
r = requests.post(f"{BASE}/post", json=payload)
print_resp("POST", r)

# PUT
payload = {"title": "New Title", "completed": False}
r = requests.put(f"{BASE}/put", json=payload)
print_resp("PUT", r)

# DELETE
r = requests.delete(f"{BASE}/delete")
print_resp("DELETE", r)

# 404
r = requests.get(f"{BASE}/status/404")
print_resp("404 Not Found", r)

# 422
r = requests.get(f"{BASE}/status/422")
print_resp("422 Unprocessable Entity", r)