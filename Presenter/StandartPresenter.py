from View.Menu import Menu
from Logger.Read import Read
from Logger.Write import Write
from Model.PrintDataMod import PrintDataMod
from Model.DeleteEmployeeMod import DeleteEmployeeMod
from View.SetId import SetId
from View.SetReplaceInfo import SetReplaceInfo
from Model.StandartReplaceMod import StandartReplaceMod
from View.SetNewStandartEmployee import SetNewStandartEmployee as new_employee
from Employee.StandartEmployee import StandartEmployee
from View.SetSearchInfo import SetSearchInfo as search_info
from Model.SearchStandartEmployeeMod import SearchStandartEmployeeMod as Search
# from View.NextStep import continueStep as step

 # Presenter берет данные из методов View и применяет на конкретных моделях из папки Model, 
 # применяя для сохранения/загрузки Logger. 
 
class StandartPresenter():
    def startWork(path):
        staff = Read.read(path)
        chooseMod = Menu.setMod()
        
        match chooseMod:
            case 1:
                print("     СПИСОК СОТРУДНИКОВ")
                print("------------------------------")
                PrintDataMod.printData(staff)
            case 2:
                staff = DeleteEmployeeMod.deleteEmployee(staff, SetId.setIdForDelete())
                Write.write(path, staff)
            case 3:
                re = SetReplaceInfo.setReplacementInfo()
                staff = StandartReplaceMod.replaceInfo(staff, int(re.get("id")), re.get("column"), re.get("newData"))
                Write.write(path, staff)
            case 4:      
                inf = new_employee.setNewEmployee()
                newEmpl = StandartEmployee(int(inf.get("id")), inf.get("sName"), inf.get("fName"), inf.get("patronymic"), inf.get("phone"), inf.get("address"), inf.get("passport"))
                staff.append(newEmpl)
                Write.write(path, staff)
            case 5:
                Search.employeeSearch(staff, search_info.setSearchInfo())
            
        # answ = step()
        # if(answ.equals("yes")):
        #     startWork(path)
    