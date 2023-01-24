import json
from Logger.I__Save import I__Save

class Write(I__Save):
    """Записываем в файл"""

    def write(path, a):
        staff = []
        for man in a:
            man_map = {}
            man_map = \
            {
                'id' : man.get_id(),
                'sName' : man.get_sName(),
                'fName' : man.get_fName(),
                'passport' : man.get_passport(),
                'patronymic' : man.get_patronymic(),
                'phone' : man.get_phone(),
                'address' : man.get_address()
            }
            staff.append(man_map)
        with open('log.json', 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(staff))