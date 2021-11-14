from abc import abstractmethod


class Warehouse:
    technique = {}
    technique_econom = {}

    def take_the_technique(self, device):
        # использовать тернанрный оператор не дает
        if device.price <= 4000:
            # если такой тип оргтехники уже добавляли в эконом
            if device.office_type in self.technique_econom:
                self.technique_econom[device.office_type] = self.technique_econom.get(device.office_type) + device.model_count
            else:
                self.technique_econom[device.office_type] = device.model_count
        else:
            # если такой тип оргтехники уже добавляли в премиум
            if device.office_type in self.technique:
                self.technique[device.office_type] = self.technique.get(device.office_type) + device.model_count
            else:
                self.technique[device.office_type] = device.model_count

    def __str__(self):
        all_device = OfficeEquipment()
        return f"На складе всего {all_device} устройств.\n" \
               f"Из них\nэконом класса: {'; '.join([f'{key}: {value}' for key, value in self.technique_econom.items()])}\n" \
               f"премиум класса: {'; '.join([f'{key}: {value}' for key, value in self.technique.items()])}\n" \


class OfficeEquipment:
    __count_equipment: int = 0
    office_type = ""

    def __init__(self, count: int = 0):
        OfficeEquipment.__count_equipment += count

    @abstractmethod
    def get_count(self) -> int:
        pass

    def __str__(self):
        return f"{self.__count_equipment}"


class Printer(OfficeEquipment):
    __count: int = 0

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0, *args):
        """
               name - название фирмы устройства
               price - цена
               number_of_lists - колчество листов в минуту
               count - количество устройств
        """
        Printer.office_type = "Принтер"
        if name and price and number_of_lists and count:
            Printer.__count += count
            super().__init__(count)
            self.name = name
            self.model_count = count
            self.price = price
            self.number_of_lists = number_of_lists

    @staticmethod
    def get_count() -> int:
        return Printer.__count

    def to_print(self):
        return f"{self.name} печатает со скоростью {self.number_of_lists} л/мин."


class Scaner(OfficeEquipment):
    __count: int = 0

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0, *args):
        """
               name - название фирмы устройства
               price - цена
               number_of_lists - колчество листов в минуту
               count - количество устройств
        """
        Scaner.office_type = "Сканер"
        if name and price and number_of_lists and count:
            Scaner.__count += count
            super().__init__(count)
            self.name = name
            self.model_count = count
            self.price = price
            self.number_of_lists = number_of_lists

    @staticmethod
    def get_count() -> int:
        return Scaner.__count

    def to_scan(self):
        return f"{self.name} сканирует со скоростью {self.number_of_lists} л/мин."


class Xerox(OfficeEquipment):
    __count: int = 0

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0, *args):
        """
               name - название фирмы устройства
               price - цена
               number_of_lists - колчество листов в минуту
               count - количество устройств
        """
        Xerox.office_type = "Копировальный аппарат"
        if name and price and number_of_lists and count:
            Xerox.__count += count
            super().__init__(count)
            self.name = name
            self.model_count = count
            self.price = price
            self.number_of_lists = number_of_lists

    @staticmethod
    def get_count() -> int:
        return Xerox.__count

    def to_xerox(self):
        return f"{self.name} делает {self.number_of_lists} копий(и) в минуту."


def get_type_tehnics(user_index):
    it = user_index
    try:
        it = int(it)
    except ValueError:
        print("Вы ввели не число")
        it = get_type_tehnics(input("Попробуйте еще раз: "))
    else:
        while it not in range(1, len(org_tehnics) + 1):
            it = get_type_tehnics(input("Вы ввели не правильный индекс\nПопробуйте еще раз: "))
    return it

sklad = Warehouse()

first_printer = Printer("LG", 5000, 18, 2)
sec_printer = Printer("Samsung", 5200, 22, 1)
sklad.take_the_technique(first_printer)
sklad.take_the_technique(sec_printer)

fist_scan = Scaner("HP", 3000, 6, 6)
sec_scan = Scaner("HP", 5700, 7, 3)
sklad.take_the_technique(fist_scan)
sklad.take_the_technique(sec_scan)

fist_xerox = Xerox("Xerox", 3000, 6, 10)
sec_xerox = Xerox("Dell", 4100, 7, 5)
sklad.take_the_technique(fist_xerox)
sklad.take_the_technique(sec_xerox)


features = {'название (модель)': '', 'цена': '', 'количество листов в минуту': '', 'количество устройств': ''}
org_tehnics = [Printer(), Scaner(), Xerox()]
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        print(sklad)
        break
    print("Укажите, какую технику привезли:")
    for ind, el in enumerate(org_tehnics):
        print(ind + 1, el.office_type)
    ind = get_type_tehnics(input())
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        f_copy[f] = int(pro) if f == 'цена' or f == 'количество листов в минуту' or\
                                f == 'количество устройств' else pro  # Меняем тип числовых свойства
    if ind == 1:
        user_device = Printer(*list(f_copy.values()))
    elif ind == 2:
        user_device = Scaner(*list(f_copy.values()))
    else:
        user_device = Xerox(*list(f_copy.values()))
    sklad.take_the_technique(user_device)