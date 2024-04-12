import sqlite3
from typing import Self

class Order:
    TABLE_NAME="order"
    def __init__(self, order_id=None,  product_id=None)->None:
        self.order_id = order_id
        self.product_id = product_id
        pass
    def save(self):
         if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET order_id=?,product_id=? WHERE order_id=?"
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.order_id, self.product_id))
      
            # save into the database     
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (order_id, product_id) VALUES(?,?,?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.order_id, self.product_id))

                new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id = new_instance_id
    def read(self,id=None):
        pass
    def delete(self):
        pass