import sqlite3
from models.constant import PATH_TO_DB
class Product:
    TABLE_NAME="product"
    def __init__(self, product_id=None, product_name=None, quantity=None, price=None, category=None):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.category = category
    def save(self):
        table_name = __class__.TABLE_NAME
        if self.product_id:
            query = f"UPDATE {table_name} SET product_name=?,quantity=?,price=?,category=?, WHERE product_id=?"

            
            with sqlite3.connect(PATH_TO_DB) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.product_name, self.quantity, self.price,self.category,self.product_id))
                connection.commit()
        else:
            # save into the database
            query = f"INSERT INTO {table_name} (product_name, quantity,price,category) VALUES(?,?,?,?)"
            with sqlite3.connect(PATH_TO_DB) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.product_name, self.quantity, self.price,self.category))
                
                new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {table_name}").fetchone()
                self.product_id = new_instance_id
                connection.commit()

    def read(product_id=None):
        table_name = __class__.TABLE_NAME
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if product_id!=None:
                query = f"SELECT product_name, quantity, price, category FROM {table_name} WHERE product_id=?"

                result = cursor.execute(query, (product_id, )).fetchone()

                single_product = __class__(product_name=result[1], quantity=result[2],  price=result[4],category=[3])
                single_product.product_id = result[0]

                return single_product
            else:
                query = f"SELECT * FROM {table_name}"
                results = cursor.execute(query).fetchall()
                products = []

                for result in results:
                    product = __class__(product_id = result[0],product_name=result[1], quantity=result[2],  price=result[4],category=[3])
                
                    products.append(product)
                
                return products
    
    def delete(product_id=None):
        table_name = __class__.TABLE_NAME
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if product_id!=None:
                cursor.execute(f"DELETE FROM {table_name} WHERE product_id=?", (product_id, ))
                connection.commit()

    def toJSON(self):
        return{
            "product_name":self.product_name,
            "quantity":self.quantity,
            "price":self.price,
            "category":self.category,
            "id":self.product_id
        }