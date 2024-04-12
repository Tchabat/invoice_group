from flask import Blueprint, request,jsonify,Response

from controllers.products import *

products_view = Blueprint('products', __name__, url_prefix='/products')

@products_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    
    if request.method == 'GET':
        return get_all_products()
    elif request.method =="POST":
        data = request.get_json()

        product_data = data
        try:
            product = save_product(product_data['product_name'],product_data['quantity'],product_data['price'],
                                        product_data['category'])
            return jsonify("Success"),201
        except Exception as e:
                   return f"An error occured: {e}"
    else:
        return Response({'error':'Method not allowed'}, status=405)
    
@products_view.route('/<id>', methods=['GET', 'PUT','DELETE'])
def get_or_update_instance(id):
    if request.method == 'GET':
        return get_product_with_id(id)
    elif request.method == "PUT":
        data = request.get_json()
        return Response(save_product(product_name=data['product_name'],quantity=data['qauntity'],price=data['price'],category=data['category'],product_id=data['id']))
    elif request.method == "DELETE":
        return Response(delete_products(id),status=201)
    else:
        return None
    
