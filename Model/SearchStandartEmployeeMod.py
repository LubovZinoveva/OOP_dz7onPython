

# SearchStandartEmployeeMod осуществляет поиск стандартного сотрудника и выводит его на экран  

from Model.SearchBaseEmployeeMod import SearchBaseEmployeeMod


class SearchStandartEmployeeMod(SearchBaseEmployeeMod):
    """Oсуществляет поиск стандартного сотрудника и выводит его на экран"""

    def employeeSearch(staff, criteria):
        super.employeeSearch(staff, criteria)
        res = set()
        for man in staff:
            if(man.get_patronymic() == criteria or man.get_phone() == criteria or man.get_address == criteria):
                res.add(man)
            
        if(len(res) > 0):
            for item in res:
                print(item)
            