from abc import abstractmethod

# Интерфейс I__PrintData отвечает за загрузку базы данных в терминал

class I__PrintData:
    """Отвечает за загрузку базы данных в терминал"""

    @abstractmethod
    def printData(staff):
        print(staff)
