class Employee:

    def __init__(self,id,name,age,salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_data(self):
        return self.id

class Company:

    def __init__(self):
        self.employee = []
    
    def add_employee(self,employee):
        self.employee.append(employee)
    
    def sort_by_salary(self):
        self.employee.sort(key=lambda x:x.salary,reverse=True)
    
    def sort_by_age(self):
        self.employee.sort(key=lambda x:x.age,reverse=True)

    def sort_by_name(self):
        self.employee.sort(key=lambda x:x.name,reverse=True)

    def sort_by_id(self):
        self.employee.sort(key=lambda x:x.id,reverse=True)
    
    def __str__(self):
        return '\n'.join([str(i.get_data()) for i in self.employee])

if __name__ == '__main__':
    e1 = Employee('161E90','Ramu',35,59000)
    e2 = Employee('171E22','Tejas',30,82100)
    e3 = Employee('171G55','Abhi',25,100000)
    e4 = Employee('152K46','Jaya',32,85000)
    c = Company()
    c.add_employee(e1)
    c.add_employee(e2)
    c.add_employee(e3)
    c.add_employee(e4)

    print('Before Sorting')
    print(c)

    opt = int(input('Enter 1 to sort by id, 2 to sort by name, 3 to sort by age, 4 to sort by salary: '))
    if opt == 1:
        c.sort_by_id()
    elif opt == 2:
        c.sort_by_name()
    elif opt == 3:
        c.sort_by_age()
    elif opt == 4:
        c.sort_by_salary()
    else:
        print('Invalid option')
    
    print('After Sorting')
    print(c)