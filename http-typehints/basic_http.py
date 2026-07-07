import requests

BASE = "https://jsonplaceholder.typicode.com"

r = requests.get(f"{BASE}/posts")
r = requests.post(f"{BASE}/posts", json=new_post)
r = requests.put(f"{BASE}/posts/{post_id}",json=updated)
r = requests.delete(f"{BASE}/posts/{post_id}")


print(r.status_code, r.json())