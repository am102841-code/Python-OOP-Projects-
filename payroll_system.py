import random, time

print("Welcome to the Employee Payroll System!")
print("Please enter three employees' details.")

class Employee:
    def __init__(self):
        self.name = input("Name: \n < ")
        self.hourly_wage = input("Hourly Wage: \n < ")
        self.hours_worked = input("Hours worked this week: \n < ")
        self.salary = None
        self.tax = input("Tax (%): \n < ")
        print("\n")
        self.overtime_hours = None
        self.overtime_pay = None
        self.bonus = None
        self.bonus_chance = None

    def calculate_salary(self): # with tax deduction
        self.salary = int(self.hourly_wage) * int(self.hours_worked)
        self.tax = int(self.tax)
        self.salary -= self.salary * (self.tax / 100)

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Hourly Wage: ${self.hourly_wage}")
        print(f"Total Weekly Pay: ${self.salary}")
        print("\n")

    def overtime(self):
        if int(self.hours_worked) > 40:
            self.overtime_hours = int(self.hours_worked) - 40
            self.overtime_pay = self.overtime_hours * (int(self.hourly_wage) * 1.5)
            self.salary += self.overtime_pay

    def bonus(self):
        self.bonus_chance = random.randint(1, 100)
        if self.bonus_chance == 67:
            self.bonus = self.salary * 0.1
            self.salary += self.bonus
        else:
            self.bonus = 0

worker1 = Employee()
worker2 = Employee()
worker3 = Employee()

workers = [worker1, worker2, worker3]

for worker in workers:
    worker.calculate_salary()
    worker.overtime()
    worker.bonus()
    worker.display()
