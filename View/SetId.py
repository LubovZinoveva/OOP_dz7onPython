# Узнаем id сотрудника, которого будем удалять
 
from View.I__SetId import I__SetId

class SetId(I__SetId):
    """Узнаем id сотрудника, которого будем удалять"""

    def setIdForDelete():
        return input("Введите id сотрудника для удаления из базы: ")