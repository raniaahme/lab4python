class Person:
    def _init_(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate

    def sleep(self, shours):
        if shours == 7:
            print("happy")
        elif shours > 7:
            print("lazy")
        else:
            print("tired")

    def eat(self, meals):
        if meals == 1:
            print("50%")
        elif meals == 2:
            print("75%")
        if meals == 3:
            print("100%")

    def buy(self, items):
        for i in range(items):
            self.money -= 10


class Employee(Person):
    def _init_(self, id, name, email, mood, money, car, healthrate, salary, distance):
        super(Employee, self)._init_(name, money, mood, healthrate)
        self.id = id
        self.email = email
        self.car = car
        self.__salary = salary
        self.distance = distance

    @property
    def Salary(self):
        return self._salary

    @Salary.setter
    def Salary(self, newsalary):
        if newsalary < 1000:
            print("the salary is invalid ")
        else:
            self.__salary = newsalary

    def work(self, hours):
        if hours > 8:
            print("tired")
        elif hours == 8:
            print("happy")
        else:
            print("lazy")

    def drive(self, distance):
        Car.run(velocity, distance)
        pass

    def refuel(self, gasAmount):
        Car.fuelRate = self.gasAmount

    def send_mail(self):
        pass


class Office:
    def _init_(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def fire(self):
        pass

    def hire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


class Car:
    def _init_(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        km_no = int(self.distance / 10)
        for i in range(km_no):
            self.fuelRate = int(self.fuelRate - (self.fuelRate * 0.1))
            self.distance -= 10
            if self.fuelRate == 0:
                stop(self.Distance)
        self.velocity = velocity

    def stop(self, Distance):
        self.velocity = 0
        if Distance == 0:
            print("arrived done")
        else:
            print("the distance remaining = " + Distance)

