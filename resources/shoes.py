import models

from flask import Blueprint, request


shoes = Blueprint('shoes', 'shoes')


@shoes.route('/', methods=['GET'])
def dogs_index():
	return 'dog controller work'


@shoes.route('/', methods=['POST'])
def create_shoe():
	# print(request.get_json())
	payload = request.get_json()
	shoe = models.Shoe.create(name=payload['name'], 
		brand=payload['brand'], 
		color=payload['color'])
	
	return "You hit shoe create route"

