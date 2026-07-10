import os
import json
import urllib.request
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/extract', methods=['GET'])
def extract_link():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "Link provide karein"}), 400

    api_url = 'https://co.wuk.sh/api/json'
    
    payload = json.dumps({
        "url": video_url,
        "vQuality": "720"
    }).encode('utf-8')
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        req = urllib.request.Request(api_url, data=payload, headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

        if data.get('status') == 'error':
            return jsonify({"success": False, "error": data.get('text', 'Download not supported')}), 400

        direct_url = data.get('url')
        if not direct_url:
            return jsonify({"success": False, "error": "Direct link fetch failed"}), 400

        return jsonify({
            "success": True,
            "title": "Vawvi_Download",
            "direct_link": direct_url,
            "thumbnail": ""
        })
    except Exception as e:
        return jsonify({"success": False, "error": "Server API Error: " + str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Vawvi Proxy API is running perfectly!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
