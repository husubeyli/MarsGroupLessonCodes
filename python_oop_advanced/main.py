import pymysql.cursors
from datetime import datetime

class Model():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345',
                             db='blog',
                             port=3306,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    @classmethod
    def create(cls, **kwargs):
        field_name = ', '.join(kwargs.keys())
        with cls.connection.cursor() as cursor:
            sql = """insert into {}
                ({}) values
                (%s, %s, %s, %s);
                """.format(cls.__name__.lower(), field_name)
            cursor.execute(sql, tuple(kwargs.values()))
        cls.connection.commit()

    @classmethod
    def all(cls):
        with cls.connection.cursor() as cursor:
            sql = """select * from {};""".format(cls.__name__.lower(), )
            cursor.execute(sql)
        return cursor.fetchall()


class Books(Model):
    
    def __init__(self):
        with self.connection.cursor() as cursor:
            sql = """create table if not exists books(
                id int unsigned AUTO_INCREMENT PRIMARY KEY,
                title varchar(150) NOT NULL,
                description text NOT NULL,
                price decimal(7,2),
                author varchar(50) NOT NULL
                );"""
            cursor.execute(sql)
        self.connection.commit()



# Books.create(title='Sefiller 2', description='Description', price='12.50', author='Viktor Huqo')

# print(Books.all())
