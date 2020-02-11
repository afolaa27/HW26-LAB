import datetime

from peewee import * 


DATABASE=SqliteDatabase('shoes.sqlite')


class Shoe(Model):
	name = CharField()
	brand = CharField()
	color = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)


	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Shoe], safe=True)
	DATABASE.close()