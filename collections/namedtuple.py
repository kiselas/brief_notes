from collections import namedtuple
#Создаем именованый кортеж
Car = namedtuple('Car', 'color mileage')
#А из него создаем экземпляр
my_car = Car('red', 3242)
print(my_car)

#так же здесь будет работать распаковка аргументов

color, mileage = my_car
print(f'Цвет: {color}, Пробег: {mileage}')

#Можно обращаться к значениям через индекс
print(my_car[0])


#Можно строить класс унаследованный от именованного кортежа и добавить к нему методы
Car = namedtuple('Car', 'color mileage')
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'
            
c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

#Для добавления нового поля необходимо использование свойства ._fields

Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',)

#Дополнительные методы: _asdict()

json.dumps(my_car._asdict())
    
#Именованные кортежи могут быть простым способом 
#для построения вашего кода, делая его более читаемым и 
#обеспечивая лучшее структурирование данных.
    
    
