from View.I__SetNewEmployee import I__SetNewEmployee

class AddNewEmployeeMod(I__SetNewEmployee):
    """Добавляет нового сотрудника в список сотрудников"""

    def addNewEmployee(staff, man):
        staff.add(man)
        return staff

