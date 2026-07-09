import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app) # Yeh frontend ko block hone se bachayega

# API Route jo video extract karega
@app.route('/api/extract', methods=['GET'])
def extract_link():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "Link provide karein"}), 400

    ydl_opts = {'format': 'best'}
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            direct_url = info.get('url')
            title = info.get('title')
            
            return jsonify({
                "success": True,
                "title": title,
                "direct_link": direct_url
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Test karne ke liye ek simple home route
@app.route('/', methods=['GET'])
def home():
    return "Vawvi Video API is running perfectly!"

if __name__ == '__main__':
    # Render automatic port assign karta hai, uske liye ye logic zaroori hai
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
