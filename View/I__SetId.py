from abc import abstractmethod

# интерфейс I__SetId с методом setIdForDelete, получающий от пользователя id сотрудника для его удаления
 
class I__SetId:
    """Получает id сотрудника для его удаления из бд"""

    @abstractmethod
    def setIdForDelete():
        id = -1
        return id