import random
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


class ComputeEmployeeWage:
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    emp_wage_per_month = 0

    def __init__(self, company, emp_rate, num_of_days, max_hours):
        self.company = str(company)
        self.emp_rate = emp_rate
        self.num_of_days = num_of_days
        self.max_hours = max_hours

    def calculate_employee_wage_for_company(self):

        total_emp_hours = 0
        total_working_days = 0
        while total_emp_hours <= self.max_hours and total_working_days < self.num_of_days:
            total_working_days += total_working_days
            emp_check = int(random.randint(0, 2))
            if emp_check == self.IS_FULL_TIME:
                emp_hrs = 8
            elif emp_check == self.IS_PART_TIME:
                emp_hrs = 4
            else:
                emp_hrs = 0
            total_emp_hours += emp_hrs
            emp_wage_per_day = emp_hrs * self.emp_rate
            self.emp_wage_per_month += emp_wage_per_day
            print("Employee Wage per Day {}".format(emp_wage_per_day))

        print("Employee Wage Per Month {}".format(self.emp_wage_per_month))

    def display(self):
        print("Company Name= {}".format(self.company))
        print("Employee Wage Per Month {}".format(self.emp_wage_per_month))


if __name__ == "__main__":
    try:
        company1 = ComputeEmployeeWage("Bridgelabz", 24, 24, 24)
        company2 = ComputeEmployeeWage("Alas", 12, 22, 209)
        company1.calculate_employee_wage_for_company()
        company2.calculate_employee_wage_for_company()
    except Exception as e:
        print(e)
        logging.error(e)
    list_of_company = list()
    list_of_company.append(company1)
    list_of_company.append(company2)
    for item in list_of_company:
        print(item.display())
