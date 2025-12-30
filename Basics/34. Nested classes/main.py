# NESTED CLASS = A classs defined within another class
#                   class Outer:
#                       class Inner:

# Benefits - 1. Allows you logically group classes that are closely related
#            2. Encapsulates private details that aren't relevant outside of the outer class
#            3. Keeps the namespace clean; reduces the possiblity of naming conflicts 

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name 
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
        
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employee.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employee]


company1 = Company("Panoptis Network")
company2 = Company("Atlas IQ")

company1.add_employee("Tushar", "Manager")
company1.add_employee("Dilip", "Cook")
company1.add_employee("Sandhya", "Cashier")

company2.add_employee("Naresh", "Manager")
company2.add_employee("Arun", "Assitant")

for employee in company2.list_employees():
    print(employee)

