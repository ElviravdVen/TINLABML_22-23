class Employee:
    # Constructor
    def __init__(self, firstname, lastname, pay, bonus=0):
        self.firstName = firstname
        self.lastName = lastname
        self.pay = pay
        self.bonus = bonus

    def getFullName(self):
        return "{} {}".format(self.firstName, self.lastName)

    # Docstring
    """
    This function calculates and
    returns the annual salary
    """

    def getAnnualSalary(self):
        payYear = 12 * self.pay
        return payYear + self.bonus

    def moreThanMe(self, other):
        return self.getAnnualSalary() < other.getAnnualSalary()

    # def __gt__(self, other):
    #     # other.salary > self.salary
    #     return
