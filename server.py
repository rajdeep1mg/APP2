import logging
from sanic import Sanic
from Middleware.music_database import music_database_bp
from tortoise.contrib.sanic import register_tortoise

logging.basicConfig(level=logging.DEBUG)

app = Sanic(__name__)
app.blueprint(music_database_bp)

register_tortoise(
    app, db_url="sqlite://db.sqlite3", modules={"models": ["Middleware.models"]}, generate_schemas=True
)

if __name__ == '__main__':
    app.run(port=9999, debug=True, auto_reload=True)
