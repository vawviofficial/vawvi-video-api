from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
# Enable CORS so your frontend can call this API even if hosted on a different domain
CORS(app) 

@app.route('/api/extract', methods=['GET'])
def extract_video_info():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"success": False, "error": "No URL provided"}), 400

    # Configure yt-dlp to extract information without downloading
    ydl_opts = {
        'format': 'best[ext=mp4]/best', # Prioritize mp4 formats
        'quiet': True,
        'no_warnings': True,
        'skip_download': True, # Crucial: Don't download the video to the server
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            # If the URL is a playlist, grab the first video
            if 'entries' in info_dict:
                info_dict = info_dict['entries'][0]

            # Extract the required fields
            title = info_dict.get('title', 'Unknown Title')
            thumbnail = info_dict.get('thumbnail', '')
            direct_link = info_dict.get('url', '')

            if not direct_link:
                return jsonify({"success": False, "error": "Could not extract a direct media link."}), 400

            return jsonify({
                "success": True,
                "title": title,
                "thumbnail": thumbnail,
                "direct_link": direct_link
            })

    except yt_dlp.utils.DownloadError as e:
        # Handle specific yt-dlp errors (e.g., private video, unsupported site)
        error_msg = str(e).replace('\x1b[0;31mERROR:\x1b[0m ', '') # Clean up CLI color codes
        return jsonify({"success": False, "error": error_msg}), 400
        
    except Exception as e:
        # Catch-all for other server errors
        return jsonify({"success": False, "error": str(e)}), 500

# For local testing
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
