from flask import Flask,jsonify,request
from scrapper import get_download_link,get_anime_watch_link
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


PORT = 8000


@app.route('/api/search',methods=["GET"])
def anime_search():
    anime_name = request.args.get('query')
    episode = request.args.get('episode')
    watch_link = get_anime_watch_link(query=anime_name,episode=episode)
    data = {
        'data':watch_link,
    }
    return jsonify(data)


@app.route('/api/download',methods=["GET"])
def anime_download():
    anime_name = request.args.get('query')
    episode = request.args.get('episode')
    download_link = get_download_link(anime_name=anime_name,episode=episode)
    data = {
        'data':download_link,
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True,port=PORT)