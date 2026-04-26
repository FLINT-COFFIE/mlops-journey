# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    sum = 0
    
    for emp in employee.subordinates:
        sum += 1 + count_subordinates(emp)
        
    return sum