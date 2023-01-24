
 # BaseEmployee - базовый сотрудник, с наименьшим набором данных, который возможен для создания карточки сотрудника
 
class BaseEmployee():
    """Базовый класс сотрудников"""
    __emp_count = 0

    def __init__(self, id, sName, fName, passport):
        self.id = id
        self.sName = sName
        self.fName = fName
        self.passport = passport
        BaseEmployee.__emp_count += 1
    
    def print_employee(self):
        print('id: {}. Фамилия: {}. Имя: {}. Пасспорт: {}'.format(self.id, self.sName, self.fName, self.passport))

    def get_id(self):
        return self.id

    def get_sName(self):
        return self.sName

    def get_fName(self):
        return self.fName

    def get_passport(self):
        return self.passport

    def set_passport(self, pas):
        self.passport = pas
    
    def set_fName(self, first):
        self.fName = first
    
    def set_sName(self, second):
        self.sName = second

   

    
   

