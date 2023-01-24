# PrintData печатает всю базу данных в терминал
 
from Model.I__PrintData import I__PrintData


class PrintDataMod(I__PrintData):
    """Печатает всю базу данных в терминал"""

    def printData(staff):
        for  man in staff:
            print(man)
        