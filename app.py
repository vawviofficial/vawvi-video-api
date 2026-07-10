from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def health():
    return jsonify({'status': 'ok', 'service': 'vawvi-video-api'})

@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json(silent=True) or {}
    url = (data.get('url') or '').strip()
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except yt_dlp.utils.DownloadError as e:
        return jsonify({'error': f'Could not process this link: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

    formats = []
    seen = set()
    for f in info.get('formats', []):
        has_audio = f.get('acodec') not in (None, 'none')
        has_video = f.get('vcodec') not in (None, 'none')
        if not (has_audio and has_video) or not f.get('url'):
            continue  # skip video-only/audio-only streams so downloads always have sound
        quality = f.get('format_note') or (f'{f.get("height")}p' if f.get('height') else 'unknown')
        key = (quality, f.get('ext'))
        if key in seen:
            continue
        seen.add(key)
        formats.append({
            'quality': quality,
            'ext': f.get('ext'),
            'filesize': f.get('filesize') or f.get('filesize_approx'),
            'url': f.get('url'),
        })

    def quality_num(q):
        digits = ''.join(ch for ch in q if ch.isdigit())
        return int(digits) if digits else 0

    formats.sort(key=lambda x: quality_num(x['quality']), reverse=True)

    return jsonify({
        'title': info.get('title'),
        'thumbnail': info.get('thumbnail'),
        'duration': info.get('duration'),
        'uploader': info.get('uploader'),
        'formats': formats,
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
