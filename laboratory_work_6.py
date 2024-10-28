# 11111111111111111111111111
class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        if self.password == password:
            return True
        else: return False


user001 = UserAccount('admin', 'adminadmin@gmail.com', \
                      'qwerty123')

print(user001.check_password('111'))
user001.set_password('111')
print(user001.check_password('111'))

# 222222222222222222222222222222222222222

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return [self.make, self.model]

class Car(Vehicle):

    def __init__(self, make, model, fuel):
        super().__init__(make, model)
        self.fuel = fuel

    def get_info(self):
        return [self.make, self.model, self.fuel]

my_car = Car('Tesla', 'Model X', 'Electricity')
print(*my_car.get_info())
