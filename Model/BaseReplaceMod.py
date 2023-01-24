from Model.I__ReplaceInfo import I__ReplaceInfo
# Класс BaseReplaceInfo заменяет информацию о базовом сотруднике на актуцальную(info2) в определенном столбце(info1)
 
class BaseReplaceMod(I__ReplaceInfo):
    """Заменяет информацию о базовом сотруднике на актуцальную"""
    
    def replaceInfo(staff, id, info1, info2):
        for man in staff:
            if(id == man.get_id()):
                match info1:
                    case "id":
                        print("id нельзя поменять.")
                    case "sName":
                        man.set_sName(info2)
                    case "fName":
                        man.set_fName(info2)
                    case "passport":
                        man.set_Passport(info2)         
        return staff
 