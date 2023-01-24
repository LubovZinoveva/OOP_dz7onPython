from abc import abstractmethod

class I__Save:
    """Отвечает за сохрнанение сотрудников в базу данных"""
    
    @abstractmethod
    def write(path, list_employee):
        print('Файл успешно cохранен.')