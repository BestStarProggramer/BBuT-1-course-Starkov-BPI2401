class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return [self.name, self.id]

class Manager(Employee):

    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        print('Открывается какое-то меню для управления проектами...')

class Technician(Employee):

    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        print('Выполнение техобслуживания...')

class TechManager(Manager, Technician):

    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.subordinates = []

    def add_employee(self, name, id):
        new_employee = Employee(name, id)
        self.subordinates.append(new_employee)
        print(f"Сотрудник {new_employee.name} с ID {new_employee.id} добавлен в список подчиненных.")

    def get_team_info(self):
        return [employee.get_info() for employee in self.subordinates]

Jack = Employee('Jack', 100000)
Max = Manager('Max', 100001, 'Headquarters')
Luis = Technician('Luis', 100002, 'Engineer')
Keanu = TechManager('Keanu', 100003, 'York_branch', 'Problem_solver')

print(Jack.get_info())
Max.manage_project()
Luis.perform_maintenance()
Keanu.add_employee('Felix', 100004)
Keanu.add_employee('Mark', 100005)
Keanu.add_employee('Abram', 100006)
print(*Keanu.get_team_info())


