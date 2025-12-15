from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Table
from sqlalchemy.orm import relationship,declarative_base

Base=declarative_base()
engine=create_engine("sqlite:///lottery.db")

user_loan=Table(
    "user_loan",
    Base.metadata,
    Column("user_ID",Integer,ForeignKey("karbar.ID"),primary_key=True),
    Column("loan_ID",Integer,ForeignKey("vam.ID"))
)

class User(Base):
    __tablename__="karbar"
    ID=Column(Integer,primary_key=True)
    Name=Column(String)
    Email=Column(String)
    Amount=Column(Integer)
    loans=relationship("Loan", secondary=user_loan, back_populates="users")
    def __init__(self,name,email,amount):
        self.Name=name
        self.Email=email
        self.Amount=amount

class Loan(Base):
    __tablename__="vam"
    ID=Column(Integer,primary_key=True)
    Name=Column(String)
    Amount=Column(String)
    Installment=Column(String)
    Date_from=Column(String)
    Date_to=Column(String)
    users=relationship("User",secondary=user_loan,back_populates="loans")
    def __init__(self,name,amount,installment,date_from,date_to):
        self.Name=name
        self.Amount=amount
        self.Installment=installment
        self.Date_from=date_from
        self.Date_to=date_to

class Ghorekeshi(Base):
    __tablename__="ghorekeshi"
    ID=Column(Integer,primary_key=True)
    user=Column(String)
    loan=Column(String)
    priority=Column(Integer)
    def __init__(self,user,loan,priority):
        self.user=user
        self.loan=loan
        self.priority=priority
Base.metadata.create_all(engine)
