"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission, commission_pay):
        self.name = name
        self.number_of_commissions = commission
        self.commission_pay = commission_pay

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    
    def add_commission_string(self):
        if self.number_of_commissions > 1:
            commission_str = ' and receives a commission for ' + str(self.number_of_commissions) + ' contract(s) at ' + str(self.commission_pay) + '/contract. '
        else:
            commission_str = ' and receives a bonus commission of ' + str(self.commission_pay) + '. '
        return commission_str
    
class MonthlyEmployee(Employee):
    def __init__(self, name, commission, commission_pay, pay):
        super().__init__(name, commission, commission_pay)
        self.monthly_salary = pay

    def get_pay(self):
        total = 0
        total += self.monthly_salary 
        if self.number_of_commissions > 0:
            total += self.number_of_commissions * self.commission_pay
        return total
    
    def __str__(self):
        result_str = self.name + ' works on a monthly salary of ' + str(self.monthly_salary)
        if self.number_of_commissions > 0:
            result_str += self.add_commission_string()
        else:
            result_str += '. '
        result_str += 'Their total pay is ' + str(self.get_pay()) + '.'
        return result_str
    
class ContractEmployee(Employee):
    def __init__(self, name, commission, commission_pay, hours, pay):
        super().__init__(name, commission, commission_pay)
        self.pay = pay
        self.hours = hours

    def get_pay(self):
        total = 0
        total += self.pay * self.hours
        if self.number_of_commissions > 0:
            total += self.number_of_commissions * self.commission_pay
        return total
    
    def __str__(self):
        result_str = self.name + ' works on a contract of ' + str(self.hours) + ' hours at ' + str(self.pay) + '/hour'
        if self.number_of_commissions > 0:
            result_str += self.add_commission_string()
        else:
            result_str += '. '
        result_str += 'Their total pay is ' + str(self.get_pay()) + '.'
        return result_str



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 0, 0, 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 0, 0, 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 4, 200, 3000)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 3, 220, 150, 25)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 1, 1500, 2000)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 1, 600, 120, 30)
