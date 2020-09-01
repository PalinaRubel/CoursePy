#Создать класс Student: id, Фамилия, Имя, Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс,
#Группа. Функции-члены реализуют запись и считывание полей (проверка корректности), расчет
#возраста студента Создать список объектов. Вывести:
#a) список студентов заданного факультета;
#d) список студентов одного курса.

class Student:
    __id = 0
    __surname = ''
    __name = ''
    __middleName = ''
    __birthday = ''
    __faculty = ''
    __course = 0


    def __init__(self, id0, surname0, name0, middleName0, birthday0, faculty0, course0):
        self.__id = id0
        self.__surname = surname0
        self.__name = name0
        self.__middleName = middleName0
        self.__birthday = birthday0
        self.__faculty = faculty0
        self.__course = course0
        print
        'New object created!'

    def get_id(self):
        return self.__id

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_middleName(self):
        return self.__middleName

    def get_birthday(self):
        return self.__birthday

    def get_faculty(self):
        return self.__faculty

    def get_course(self):
        return self.__course

def get_info(self):
    print('Student id: ' + str(students[i].get_id()))
    print('Student surname: ' + students[i].get_surname())
    print('Student name: ' + students[i].get_name())
    print('Student middleName: ' + students[i].get_middleName())
    print('Student birthday: ' + students[i].get_birthday())
    print('Student faculty: ' + students[i].get_faculty())
    print('Student course: ' + str(students[i].get_course()))

i = 0

students = [Student(1, 'Svik', 'Oleg', 'Victorovich', '7.10.1997', 'FMO', 3),
            Student(2, 'Romanova', 'Olga', 'Alexandrovna', '7.10.1997', 'FITU', 2),
            Student(3, 'Makar', 'Victor', 'Ivanovich', '7.10.1997', 'FKP', 1),
            Student(4, 'Kurtas', 'Sasha', 'Olegovich', '7.10.1997', 'FMO', 5),
            Student(5, 'Rubel', 'Kostya', 'Alexeevich', '7.10.1997', 'FITU', 4),
            Student(6, 'Mozar', 'Masha', 'Vadimovna', '7.10.1997', 'FKP', 2),
            Student(7, 'Shiman', 'Marina', 'Victorovna', '7.10.1997', 'FMO', 1),
            ]

facult = input('Введите факультет: ')

for i in range(len(students)):
    if students[i].get_faculty() == facult:
        get_info(i)
    print('***************************')
    i += 1

print('***************************************')
course = int(input('Введите курс: '))

for i in range(len(students)):
    if students[i].get_course() == course:
        get_info(i)
    print('**************************')
    i += 1

