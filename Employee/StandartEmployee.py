# Класс StandartEmployee - экземпляры данного класса являются стандартными сотрудниками некой компании. 
# У сотрудника есть id, ФИО, телефон, адрес и номер паспорта.
 
from Employee.BaseEmployee import BaseEmployee

class StandartEmployee(BaseEmployee):
    """Стандартный сотрудник"""
    
    def __init__(self, id, sName, fName, patronymic, phone, address, passport):
        self.id = id
        self.sName = sName
        self.fName = fName
        self.passport = passport
        self.patronymic = patronymic
        self.phone = phone
        self.address = address

    def print_employee(self):
        print('id: {}. Фамилия: {}. Имя: {}. Отчество: {}. Телефон: {}. Адрес: {}. Пасспорт: {}'.format(self.id, self.sName, self.fName, self.patronymic, self.phone, self.address, self.passport))

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_patronymic(self):
        return self.patronymic

    def set_address(self, adrs):
        self.address = adrs

    def set_phone(self, ph):
        self.phone = ph

    def set_patronymic(self, pt):
        self.patronymic = pt

   