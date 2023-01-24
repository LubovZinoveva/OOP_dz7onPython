# Класс StandartReplaceInfo заменяет информацию о стандартном сотруднике на актуальную(info2) в определенном столбце(info1)
 
from Model.BaseReplaceMod import BaseReplaceMod


class StandartReplaceMod(BaseReplaceMod):
    """Заменяет информацию о стандартном сотруднике на актуальную"""
    
    def replaceInfo(staff, id, info1, info2):
        super.replaceInfo(staff, id, info1, info2)
        for man in staff:
            if(id == man.getId()):
                match info1:
                    case "patronymic":
                        man.set_patronymic(info2)
                    case "phone":
                        man.set_phone(info2)
                    case "address":
                        man.set_address(info2) 
        return staff