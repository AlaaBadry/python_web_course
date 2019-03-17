from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# engine = create_engine("mysql://user:pwd@localhost/school", echo=True)
engine = create_engine('sqlite:///school.db', echo=True)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('address', String)
)

meta.create_all(engine)
conn = engine.connect()

ins = students.insert().values(first_name="Fatma", last_name="Samy", address="Giza")
conn.execute(ins)

conn.execute(students.insert(), [
    {"first_name": "Fatma", "last_name": "Samy", "address": "Cairo"},
    {"first_name": "Ahmad", "last_name": "Akram", "address": "Giza"},
    {"first_name": "Abdo", "last_name": "Mohamed", "address": "Giza"},
    {"first_name": "Arwa", "last_name": "Osama", "address": "Alex"},
])


print("#####################")

stmt = students.select().where(students.c.address == "Giza")
result = conn.execute(stmt).fetchall()
print(result)
