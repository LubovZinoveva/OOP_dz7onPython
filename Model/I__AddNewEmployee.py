from abc import abstractmethod

# I__AddNewEmployee<T> задает метод добавления нового сотрудника
 
class I__AddNewEmployee:
    """Задает метод добавления нового сотрудника"""

    @abstractmethod
    def addNewEmployee(staff, new_man):
        print("Добавляем нового сотрудника")

