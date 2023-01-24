# SetBaseEmployee получает данные для заполнения полей базового сотрудника

from View.I__SetNewEmployee import I__SetNewEmployee

class SetBaseEmployee(I__SetNewEmployee):
    """Получает данные для заполнения полей базового сотрудника"""

    def setNewEmployee():
        print("Заполните поля.")
        id = -1
        sName = None 
        fName = None 
        passport = None

        result = {}
        result = \
        {
            'id' : input('id = '),
            'sName' : input('Фамилия = '),
            'fName' : input('Имя = '),
            'passport' : input('Паспорт = ')
        }
        
        return result;   
