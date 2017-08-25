

class Car(object):
    """
    class Car is the base class

    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 0
        self.gas_per_mile = 0.7

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print ("This car has ", str(self.odometer_reading), " miles on it.\n")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer\n")

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't increase a minus value miles\n")

    def fill_gas_tank(self, gas):
        if gas > 0:
            self.gas += gas
            print ("added " + str(gas) + "liter gas. Now tank has " + str(self.gas) + " liters.\n")
        else:
            print "gas can't be less than or equal to 0"

    def read_gas_tank(self):
        print "This car has ", str(self.gas), " liter gas left.\n"
    def run(self, miles):
        if miles > 0:
            gas_mile = self.gas / self.gas_per_mile
            if miles < gas_mile:
                self.gas -= self.gas_per_mile * miles
                self.increment_odometer(miles)
                print "The car ran", str(miles), '\n'
            else:
                print "There's not enough gas for car to run ", miles, " miles.\n"
        else:
            print "car won't run miles less than 0.\n"


class ElectricCar(Car):
    """

        inheritance from parent class 'Car'
    """

    def __init__(self, make, model, year):
        # super().__init__(make, model, year)
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self, gas):
        # super(ElectricCar, self).fill_gas_tank(gas)
        print("This electric car doesn't need a gas tank fill.\n")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print ("This battery is " + str(self.battery_size) + "-kWh.\n")

##### main ######

my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank(12)

my_car = Car('Ford', "Falcon", 2015)
my_car.fill_gas_tank(100)
my_car.run(100)
my_car.read_gas_tank()

