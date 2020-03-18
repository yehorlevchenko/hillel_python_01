'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ipList):
        pass

    @property
    def ipList(self):
        pass

    @ipList.setter
    def ipList(self, newList):
        pass

    def reverse_IP(self):
        """Return it's IPs reversed"""
        pass

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        pass

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""


'''У вас несколько JSON файлов. В каждом из этих файлов есть
произвольная структура данных. Вам необходимо написать
класс (без реализации конструктора) который будет описывать работу с
этими файлами, а именно:
1) Запись в файл
2) Чтение из файла
3) Получить путь относительный путь к файлу
4) Получить абсолютный путь к файлу'''


class JSONhandler:
    """Handles .json files: read, write, get abs/rel path"""
    def read(self, file):
        """Reads json file"""
        pass

    def write(self, input_data, file):
        """Writes json-formatted data to provided file"""
        pass

    def get_absolute_path(self, file):
        """Returns absolute path to provided file"""
        pass

    def get_relative_path(self, file):
        """Returns relative path to provided file"""
        pass


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password


'''Создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __repr__(self):
        pass

    def __str__(self):
        pass


'''Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер
группы, успеваемость (массив из пяти элементов).
Создайте список студентов из десяти элементов (10 экземпляров вашего класса).
Напиши функции:
1. Упорядочить массив по возрастанию среднего балла.
2. Вывести фамилии и номера групп студентов, имеющих оценки, равные
только 4 или 5.'''

class Student(object):
    pass

def sort_by_avg_mark(s_list):
    pass

def get_best_by_mark(s_list):
    pass
