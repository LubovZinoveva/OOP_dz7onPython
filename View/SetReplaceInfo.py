 # В классе SetReplaceInfo собираем с пользователя id сотрудника, название столбца, 
 # где заменим информацию на актуальную
 
from View.I__SetReplaceInfo import I__SetReplaceInfo

class SetReplaceInfo(I__SetReplaceInfo):
    """Собираем id сотрудника, название столбца, где заменим информацию на актуальную"""
    
    def setReplacementInfo():
        result = {}
        result = \
        {
            'id' : input('id = '),
            'column' : input('Напишите название столбца для замены(sName, fName, patronymic, phone, address, passport) =  '),
            'newData' : input('Новые данные = ')
        }
        
        return result

