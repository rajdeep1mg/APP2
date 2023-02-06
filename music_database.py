from sanic import Blueprint, request, Request, text, response
from .models import Songs

music_database_bp = Blueprint("music_database", version = 1, url_prefix='/search')


@music_database_bp.route("/")
async def search_results():
    songs = await Songs.all()
    newdict = []
    for song in songs:
        newdict.append({"song_id": song.music_id, "name": song.song_name})

    return response.json({"user": newdict})
