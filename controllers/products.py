import os

from models.products import Product
#from .files import save_file

def get_all_products():
    products = Product.read()

    return [product.toJSON() for product in products]

def get_product_with_id(product_id, return_object=True):
    product = Product.read(product_id)

    if product is None:
        return None
    
    return product.toJSON() if not return_object else product

def save_product(product_name, quantity, price, category, product_id=None):
    if product_id is not None:
        existing_product = get_product_with_id(product_id,return_object=True)
        #if an existing product is found, update details
        if existing_product is not None:
            existing_product.product_name = product_name
            existing_product.quantity = quantity
            existing_product.price = price
            existing_product.category = category
            existing_product.save()
            return f"product with ID {product_id} updated successfully"
        else:
            #if no existing product is found with given id
            return f"product with ID {product_id} not found"
    else:
        new_product = Product(product_name=product_name,quantity=quantity,price=price,category=category)
        new_product.save()
        return new_product if isinstance(new_product,dict) else new_product.toJSON()
       

def delete_products(id):
    product = get_product_with_id(product_id=id)
    product.delete()