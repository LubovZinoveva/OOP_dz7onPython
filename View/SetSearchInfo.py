# В классе SetSearchInfo собираем информацию, по которой потом будем искать сотрудника
 
from View.I__SetSearchInfo import I__SetSearchInfo

class SetSearchInfo(I__SetSearchInfo):
    """собираем информацию, по которой потом будем искать сотрудника"""

    def setSearchInfo():
        return input("Введите любую информацию о сотруднике: ")
    