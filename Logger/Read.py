import json
from Employee.StandartEmployee import StandartEmployee
from Logger.I__Load import I__Load

class Read(I__Load):
    """Считываем из файла"""

    def read(path):
        with open(path, 'r', encoding = 'utf-8') as fh:
            BD = json.load(fh)

        return BD