from abc import abstractmethod

# I__NextStep узнает у пользователя нужно ли закрыть базу данных или же продолжить работу

class I__NextStep:
    """узнает у пользователя нужно ли закрыть базу данных"""

    @abstractmethod
    def continueStep():
        step = "Yes or no"
        return step

