import json

# Example dictionary
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "FastAPI"],
    "address": {
        "city": "Wonderland",
        "zip": "12345"
    }
}

print("Original dictionary:")
print(person)
print("\nAccessing values:")
print("Name:", person["name"])
print("Age:", person.get("age"))
print("Skills:", person["skills"])
print("City:", person["address"]["city"])

# Modifying
person["age"] = 31
person["skills"].append("SQL")
person["address"]["country"] = "Imagination"

print("\nAfter modifications:")
print(person)

# Convert to JSON string
json_str = json.dumps(person, indent=2)
print("\nJSON representation:")
print(json_str)

# Parse JSON back to dictionary
parsed = json.loads(json_str)
print("\nParsed back to dict:")
print(parsed)
print("\nType of parsed:", type(parsed))

# Example of sending/receiving with web API simulation
def simulate_api_response():
    # Simulate receiving JSON from an API
    api_json = '{"id": 42, "title": "Learn FastAPI", "published": true}'
    data = json.loads(api_json)
    return data

response = simulate_api_response()
print("\nSimulated API response as dict:")
print(response)