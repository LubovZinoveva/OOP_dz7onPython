from abc import abstractmethod
 #  I__Load<T> отвечает за загрузку сотрудников из базы данных
 
class I__Load:
    """Отвечает за загрузку сотрудников из базы данных"""

    @abstractmethod
    def read(path):
        print('Файл успешно загружен.')
        
