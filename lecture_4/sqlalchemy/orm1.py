from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///sales1.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"Customer({self.id}, {self.name}, {self.address}, {self.email})"


Base.metadata.create_all(engine)


####################

Session = sessionmaker(bind=engine)
session = Session()

c1 = Customer(name="Ahmad Fadi", address="Giza", email="afadi@gmail.com")
c2 = Customer(name="Samir Ahmad", address="Giza", email="ssamir@yahoo.com")
c3 = Customer(name="Ashraf Fozy", address="Alex", email="afozy@hotmail.com")
c4 = Customer()
c4.name = "Alaa"
c4.address = "Haram"
c4.email = "alaa@gmail.com"

session.add_all([c1, c2, c3, c4])
session.commit()

####################

# result = session.query(Customer).all()
# result = session.query(Customer).filter(Customer.address == "Alex")
result = session.query(Customer).filter(Customer.name.like("%Ahmad%"))

for row in result:
    print(row)
