from abc import abstractmethod

# I__ReplaceInfo<T, E> Обновляет информацию о сотруднике. E - тип списка сотрудиков. 

class I__ReplaceInfo:
    """Обновляет информацию о сотруднике. E - тип списка сотрудиков."""

    @abstractmethod
    def replaceInfo(staff, id, info1, info2):
        return staff
