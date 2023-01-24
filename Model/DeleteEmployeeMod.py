# DeleteEmployeeMod удаляет сотрудика из базы 
 
from Model.I__DeleteEmployee import I__DeleteEmployee

class DeleteEmployeeMod(I__DeleteEmployee):
    """Удаляет сотрудика из базы даных"""

    def deleteEmployee(staff, id): 

        manDel = None

        for man in staff:
            if(id == man.get_id()):
                manDel = man
            
        staff.remove(manDel)
        print("Сотрудник успешно удален.")
        return staff
