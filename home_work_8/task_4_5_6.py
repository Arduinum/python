'''
4 - Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5 - Продолжить работу над первым заданием. Разработать методы, отвечающие за приём 
оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь.

6 - Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных на склад, 
нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
максимум возможностей, изученных на уроках по ООП.
'''

class Storage:
    _storage = {
    'printer':[['white', 'Canon Pixma TS3340', 'SH122Y', 4000.00, 15]],
    'scanner':[['black', 'Charge-Coupled Device', 'RH224U', 6000.00, 30]], 
    'xerox':[['gray', 'Epson L3100', 'TN678R', 100000.00, 18]]
    }

    def __init__(self, name, street):
        self.name = name
        self.street = street

    @staticmethod
    def get_org(device, model, amount, where):
        _item = [dev for dev in Storage._storage.get(device) if model in dev][0]
        result = _item.copy()
        result[-1] = amount
        _item[-1] = _item[-1] - amount
        where.get(device).append(result)


class Office(Storage):
    _office = {'printer':[], 'scanner':[], 'xerox':[]}


class Shop(Storage):
    _shop = {'printer':[], 'scanner':[], 'xerox':[]}


class OfficeEquipment:
    def __init__(self, color, model, vendor_code, price, things):
        self.color = color
        self.model = model
        self.vendor_code = vendor_code
        self.price = price
        self.things = things
    
    def reception(self, *args):
        args = list(args)
        Storage._storage.get(args.pop(-1)).append(args)


class Printer(OfficeEquipment):
    def __init__(self, color, model, vendor_code, price, things, printer):
        super().__init__(color, model, vendor_code, price, things)
        self.printer = printer
        super().reception(self.color, self.model, self.vendor_code, self.price, self.things, self.printer)

class Scanner(OfficeEquipment):
    def __init__(self, color, model, vendor_code, price, things, scanner):
        super().__init__(color, model, vendor_code, price, things)
        self.scanner = scanner
        super().reception(self.color, self.model, self.vendor_code, self.price, self.things, self.scanner)

class Xerox(OfficeEquipment):
    def __init__(self, color, model, vendor_code, price, things, xerox):
        super().__init__(color, model, vendor_code, price, things)
        self.xerox = xerox
        super().reception(self.color, self.model, self.vendor_code, self.price, self.things, self.xerox)


st = Storage('OrgKom', 'Ограномов 3б')
of = Office('бизнес центр LONODA' , 'Ошарская 2б')
sh = Shop('OrgDisk', 'Сталиваров 7б')

print('Программа склад:\nВведите команду чтоб продолжить;\nДля просмотра команд введите help.')

while True:
    command = input('введите команду: ')
    if command == 'exit':
        break
    elif command == 'help':
        print('look - просмотр товаров на складе, в магазине, в офисе;\n'\
              'add_storage - добавить товары на склад;\n'\
              'add_office - добавить товары в офис;\n'\
              'add_shop - добавить товары в магазин.')
    elif command == 'look':
        print('Введите stop для выхода из просмотра товаров;\n'\
              'Введите storage для просмотра товаров на складе;\n'\
              'Введите office для просмотра товаров в офисе;\n'\
              'Введите shop для просмотра товаров в магазине.')
        while True:
            command = input('введите команду: ')
            if command == 'storage':
                print(f'Склад {st.name}, адрес {st.street}:')
                print('Принтеры:')
                for item in st._storage.get("printer"):
                    print(item)
                print('\nСканеры:')
                for item in st._storage.get("scanner"):
                    print(item)
                print('\nКсероксы:')
                for item in st._storage.get("xerox"):
                    print(item)
            elif command == 'office':
                print(f'Офис {of.name}, адрес {of.street}:')
                print('Принтеры:')
                for item in of._office.get("printer"):
                    print(item)
                print('\nСканеры:')
                for item in of._office.get("scanner"):
                    print(item)
                for item in of._office.get("xerox"):
                    print(item)
            elif command == 'shop':
                print(f'Магазин {sh.name}, адрес {sh.street}:')
                print('Принтеры:')
                for item in sh._shop.get("printer"):
                    print(item)
                print('\nСканеры:')
                for item in sh._shop.get("scanner"):
                    print(item)
                for item in sh._shop.get("xerox"):
                    print(item)
            elif command == 'stop':
                print('Вы вышли из просмотра товаров.')
                break
    elif command == 'add_storage':
        print('Добавление на склад новой позиции:')
        color = input('Введите цвет: ')
        model = input('Введите название модели: ')
        code = input('Введите артикул: ')
        while True:
            try:
                cost = float(input('Введите цену в рублях: '))
                sum_items = int(input('Введите введите колличество товара: '))
            except ValueError:
                print('Ошибка - вы ввели буквы вместо числа!')
            else:
                type_item = input('Введите тип устройства: ')
                pr = Printer(color, model, code, cost, sum_items, type_item)
                break
    elif command == 'add_office':
        type_item = input('Введите тип устройства: ')
        model = input('Введите название модели: ')
        while True:
            try:
                sum_items = int(input('Введите введите колличество товара для отправки в офис: '))
            except ValueError:
                print('Ошибка - вы ввели буквы вместо числа!')
            else:
                st.get_org(type_item, model, sum_items, of._office)
                break       
        print('Операция произведена успешно!')
    elif command == 'add_shop':
        type_item = input('Введите тип устройства: ')
        model = input('Введите название модели: ')
        while True:
            try:
                sum_items = int(input('Введите введите колличество товара для отправки в магазин: '))
            except ValueError:
                print('Ошибка - вы ввели буквы вместо числа!')
            else:
                st.get_org(type_item, model, sum_items, sh._shop)
                break
        print('Операция произведена успешно!')

# образцы чтоб проверить программу:
# чтоб забить товары на склад:
# 'black', 'Epson WorkForce WF-7210DTW', 'MT344L', 21000.00, 10, 'printer'
# 'gray', 'HP ScanJet Pro 4500 FN', 'TB899K', 10000.00, 9, 'scanner'
# 'white', 'Canon i-SENSYS MF3010', 'TX975W', 102000.00, 12, 'xerox'
# чтоб добавить в офис или магазин:
# 'printer', 'Canon Pixma TS3340', 3
# 'xerox', 'Epson L3100', 7
