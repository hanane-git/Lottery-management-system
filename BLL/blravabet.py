from BE.mojodiatha import User
from BE.mojodiatha import Loan
from BE.mojodiatha import Ghorekeshi
from DAL.repository import Repository


class BLuser():
    def Add(self,obj):
            repose=Repository()
            repose.create(obj)
    def selectAll(self,classname):
        repose=Repository()
        return repose.select_all(classname)

class BLloan():
    def Add2(self,obj):
        repose2=Repository()
        repose2.create(obj)
    def readAll(self,classname):
        repose2=Repository()
        return repose2.select_all(classname)
    def readByID(self,classname,id):
        repose2=Repository()
        return repose2.selectByID(classname,id)
    def update(self,classname,id,**kwargs):
        repose2=Repository()
        return repose2.update(classname,id,**kwargs)
    def Del(self,classname,id):
        repose2=Repository()
        repose2.Delete(classname,id)

class BLGhorekeshi:
    def Add2(self,obj):
        repose3=Repository()
        return repose3.create(obj)
    def ReadAll(self,classname):
        repose3=Repository()
        return repose3.select_all(classname)



