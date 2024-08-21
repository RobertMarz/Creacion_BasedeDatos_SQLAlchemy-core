from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey)
from sqlalchemy import (create_engine, Insert)

metadata = MetaData()
#definicion de Tablas
cookies = Table("cookies",metadata,
                Column("cookie_id", Integer(), primary_key=True),
                Column("cookie_name", String(50), index=True),#index para ordenar todas las cookies
                Column("cookie_recipe_url", String(255)),
                Column("cookie_sku", String(55)),
                Column("quantity", Integer()),
                Column("unit_cost", Integer())# como sqlite no usa numerico no  usamos Numeric(12,2)
                )

users = Table("users",metadata,
              Column("user_id", Integer(), primary_key=True),
              Column("customer_number", Integer(), autoincrement=True),
              Column("username", String(15), nullable = False, unique=True),
              Column("email_address", String(255), nullable = False),
              Column("phone", String(20), nullable = False),
              Column("password", String(25), nullable = False),
              Column("create_on", DateTime(), default = datetime.now()),
              Column("update_on", DateTime(), default = datetime.now(),onupdate=datetime.now())
              ) 
#Relacion entre tablas

orders = Table("orders",metadata,
               Column("order_id", Integer(), primary_key=True),
               Column("user_id", Integer(), ForeignKey("users.user_id")),
               )

line_items = Table("line_items",metadata,
               Column("line_items_id", Integer(), primary_key=True),
               Column("order_id", Integer(), ForeignKey("orders.order_id")),
               Column("cookie_id", Integer(), ForeignKey("cookies.cookie_id")),
               Column("quantity", Integer()),
               Column("extend_cost", String(15))# como sqlite no usa numerico no  usamos Numeric(12,2)
               )
# aqui queremos que nuestra tabla se grabe en la carpeta virtual
engine = create_engine("sqlite:///c:\\Users\\Maryanni\\Desktop\\datos\\virtual\\coredata.db")
#engine = create_engine("MySQL:///c:\\Users\\Maryanni\\Desktop\\datos\\virtual\\bd_fullstack.db")
#engine = create_engine("MySQL:///C:\\ProgramData\MySQL\\MySQL Server 8.4\\Data\\otra.sql")
conenction = engine.connect()
# creamos nuestro motor
metadata.drop_all(engine)
metadata.create_all(engine)