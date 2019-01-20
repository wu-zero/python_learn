# 2. 自定义轿车元类CarMeta，实现元类为CarMeta的类至少有生产日期(production_date)、发动机编号(engine_number)及载客量(capacity)三个基本属性，没有就不行


class CarMeta(type):
    def __init__(cls, class_name, class_base, class_dic):
        super(CarMeta, cls).__init__(class_name, class_base, class_dic)

    def __call__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj, *args, **kwargs)

        if 'production_date' not in dir(obj):
            raise TypeError('not include production_date')
        if 'engine_number' not in dir(obj):
            raise TypeError('not include engine_number')
        if 'production_date' not in dir(obj):
            raise TypeError('not include production_date')

        return obj


# 正确Car类
class Car(metaclass=CarMeta):
    def __init__(self, name, production_date, engine_number, capacity):
        self.name = name
        self.production_date = production_date
        self.engine_number = engine_number
        self.capacity = capacity

    def show(self):
        print('di di')


# 错误Car类
class Car2(metaclass=CarMeta):
    def __init__(self, name, engine_number, capacity):
        self.name = name
        self.engine_number = engine_number
        self.capacity = capacity

    def show(self):
        print('di di')



if __name__ == '__main__':
    car1 = Car('bmw', '2019.1.20', '2333', '5')
    car1.show()
    print(car1)

    car2 = Car2('bmw', '2333', '5')  # 报错,类Car2不包含production_date这个基本属性
    car2.show()
    print(car2)
