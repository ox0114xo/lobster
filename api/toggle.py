from http.server import BaseHTTPRequestHandler
import requests
import json

# 填入你的 GitHub Token (需有 gist 權限) 和 GIST_ID
GITHUB_TOKEN = "你的_GITHUB_TOKEN"
GIST_ID = "你的_GIST_ID"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        signal = json.loads(post_data).get('status') # 'ON' 或 'OFF'

        url = f"https://api.github.com/gists/{GIST_ID}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        payload = {"files": {"signal.txt": {"content": signal}}}
        
        r = requests.patch(url, headers=headers, json=payload)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"result": "success"}).encode())

