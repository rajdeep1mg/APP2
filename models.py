from tortoise.models import Model
from tortoise import fields


class Songs(Model):
    music_id = fields.IntField(pk=True,null=False)
    song_name = fields.CharField(100)
    artist = fields.CharField(100)
    top_genre = fields.CharField(100)
    year = fields.SmallIntField()
    length = fields.IntField()
    popularity = fields.SmallIntField()
