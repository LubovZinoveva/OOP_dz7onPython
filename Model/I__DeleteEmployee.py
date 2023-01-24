from abc import abstractmethod

# I__DeleteEmployee удаляет сотрудника из бд по id
 
class I__DeleteEmployee:
    """Удаляет сотрудника из бд по id"""

    @abstractmethod
    def deleteEmployee(staff, id):
        return staff 
