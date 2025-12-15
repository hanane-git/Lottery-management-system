from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///lottery.db")
session1=sessionmaker(bind=engine)
session2=session1()

class Repository():
    def create(self,obj):
        session2.add(obj)
        session2.commit()

    def select_all(self,classname):
        return session2.query(classname).all()

    def update(self,classname,ID,**kwargs):
        row=self.selectByID(classname,ID)
        if row is not None:
            for key,val in kwargs.items():
                setattr(row,key,val)
            session2.commit()
            return True
        else:
            return False

    def Delete(self,classname,ID):
        row=self.selectByID(classname,ID)
        if row is not None:
            session2.delete(row)
            session2.commit()
            return True
        else:
            return False

    def selectByID(self,classname,ID):
        return session2.query(classname).filter(classname.ID==ID).first()

    def selectByName(self,classname,name):
        return session2.query(classname).filter(classname.NAME==name).first()

