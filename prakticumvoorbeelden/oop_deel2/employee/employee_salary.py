# Encapsulation / Information hiding
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    # Dunder method with Arguments
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        # Composition
        self.obj_salary = Salary(self.pay)

    # Docstring
    """
    This function calculates and 
    returns the annual salary
    """

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


#  Object
employee1 = Employee(600, 500)
employee2 = Employee(800, 0)
print(f"Annual salary of employee1 : {employee1.annual_salary()}")
print(f"Annual salary of employee2 : {employee2.annual_salary()}")
