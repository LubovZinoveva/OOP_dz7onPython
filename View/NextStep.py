

# NextStep получает ответ, нужно ли продолжить работу с базой данных
 
from View.I__NextStep import I__NextStep

class NextStep(I__NextStep):
    """получает ответ, нужно ли продолжить работу с базой данных"""
    
    def continueStep():
        
        answer = input("Хотите продолжить работу с базой сотрудников? Напишите yes/no. ")
        
        return answer.lower()