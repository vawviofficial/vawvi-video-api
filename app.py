import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/api/extract', methods=['GET'])
def extract_link():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "Link provide karein", "success": False}), 400

    # Vawvi's Independent Extractor (No Third-Party APIs)
    ydl_opts = {
        'format': 'best',
        'nocheckcertificate': True,
        'geo_bypass': True,
        'quiet': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        },
        'extractor_args': {
            'youtube': {
                'client': ['android', 'ios'] # YouTube block bypass
            }
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            # Agar user kisi playlist ka link daal de, toh usme se first video nikal lenge
            if 'entries' in info:
                info = info['entries'][0]
                
            direct_url = info.get('url')
            title = info.get('title', 'Vawvi_Downloaded_Video')
            
            if not direct_url:
                 return jsonify({"success": False, "error": "Direct link fetch failed"}), 400
            
            return jsonify({
                "success": True,
                "title": title,
                "direct_link": direct_url,
            })
    except Exception as e:
        return jsonify({"success": False, "error": "Extraction Error: " + str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Vawvi Independent Backend is Live!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
