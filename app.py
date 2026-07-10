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
        return jsonify({"error": "Link provide karein"}), 400

    # Advanced YouTube Bypass Logic
    ydl_opts = {
        'format': 'best',
        'nocheckcertificate': True,
        'source_address': '0.0.0.0', # Render ke IPv6 ko bypass karke IPv4 force karega
        'force_ipv4': True,
        'http_headers': {
            # YouTube ko lagega kisi asli Windows PC ke Chrome se request aayi hai
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        },
        'extractor_args': {
            'youtube': {
                # Multiple platforms ko ek sath ping karega
                'player_client': ['android', 'ios', 'tv', 'web'] 
            }
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            direct_url = info.get('url')
            title = info.get('title', 'Vawvi Downloaded Video')
            thumbnail = info.get('thumbnail', '')
            
            return jsonify({
                "success": True,
                "title": title,
                "direct_link": direct_url,
                "thumbnail": thumbnail
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Vawvi Video API is running perfectly!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
