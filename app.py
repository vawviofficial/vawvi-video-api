from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/api/extract', methods=['GET'])
def extract_video_info():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"success": False, "error": "No URL provided"}), 400

    # Facebook/Insta ke liye best settings
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Info extract karo
            info_dict = ydl.extract_info(video_url, download=False)
            
            # Agar URL ek playlist/reel hai, toh main video object lo
            if 'entries' in info_dict:
                info_dict = info_dict['entries'][0]

            return jsonify({
                "success": True,
                "title": info_dict.get('title', 'Facebook/Insta Video'),
                "thumbnail": info_dict.get('thumbnail', ''),
                "direct_link": info_dict.get('url', '')
            })

    except Exception as e:
        return jsonify({"success": False, "error": "Video formats not found or link is private."}), 400

if __name__ == '__main__':
    app.run(debug=True)
