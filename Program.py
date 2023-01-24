from Presenter.StandartPresenter import StandartPresenter

# Через класс Program осуществляется запуск программы. Задается путь к файлу и вызывается метод для начала работы
# программы с базой данных. 

class Program:
    def start():
        pathFile = "log.json"
        StandartPresenter.startWork(pathFile)
    
    start()
