from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///sales2.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"Customer({self.id}, {self.name}, {self.address}, {self.email})"


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey('customers.id'))
    inv_no = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")

    def __repr__(self):
        return f"Invoice({self.id}, {self.cust_id}, {self.inv_no}, {self.amount})"


Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
Base.metadata.create_all(engine)


# ##################

Session = sessionmaker(bind=engine)
session = Session()

c1 = Customer(name="Ahmad Fadi", address="Giza", email="afadi@gmail.com")
c1.invoices = [Invoice(inv_no=10, amount=15000), Invoice(inv_no=14, amount=3850)]

c2 = Customer(name="Samir Ahmad", address="Giza", email="ssamir@yahoo.com")
c2.invoices = [Invoice(inv_no=10, amount=5000), Invoice(inv_no=20, amount=4400)]

c3 = Customer(name="Ashraf Fozy", address="Alex", email="afozy@hotmail.com")
c3.invoices = [Invoice(inv_no=14, amount=17000), Invoice(inv_no=11, amount=5450)]

session.add_all([c1, c2, c3])
session.commit()


####################

c1 = session.query(Customer).filter(Customer.name == "Ahmad Fadi").one()

for row in c1.invoices:
    print(row)
