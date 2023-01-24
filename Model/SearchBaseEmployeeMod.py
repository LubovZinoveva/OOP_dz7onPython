

# В классе SearchBaseEmployeeMod поиск базового сотрудника по имеющейся информации
 
from Model.I__SearchEmployee import I__SearchEmployee


class SearchBaseEmployeeMod(I__SearchEmployee):
    """Поиск базового сотрудника по имеющейся информации"""
    
    def employeeSearch(staff, criteria):
        result = set()
        for man in staff:
            if(str(man.getId()) == criteria or man.get_fName() == criteria or 
            man.get_sName() == (criteria) or man.get_passport() == criteria):
                result.add(man)
         
        for item in result:
            print(item)
    