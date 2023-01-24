

# Узнаем все поля для создания экземпляра класса StandartEmployee
 
from View.SetBaseEmployee import SetBaseEmployee

class SetNewStandartEmployee(SetBaseEmployee):

    def setNewEmployee():
        result = SetBaseEmployee.setNewEmployee()
    
        result["patronumic"] = input('Отчество = ')
        result["phone"] = input('Телефон = ')
        result["address"] = input('Адрес = ')
    
        return result