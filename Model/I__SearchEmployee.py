from abc import abstractmethod

 # интерфейс I__SearchEmployee находит сотрудника по инфорамции criteria
 
class I__SearchEmployee:
    """Находит сотрудника по инфорамции criteria"""

    @abstractmethod
    def employeeSearch(staff, criteria):
        print("Печать сотрудника")

