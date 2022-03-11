import random
import logging
from EmployeeWageFactory.empoyee_wage_IF import EmployeeWageInterface

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


class ComputeEmployeeWage(EmployeeWageInterface):

    def calculate_employee_wage_for_company(self, emp_rate, num_of_days, max_hours):
        """
        Used to Calculate the Employee Wage per month
        :param emp_rate: Employee Rate at which they will wor for company
        :param num_of_days: Nummer of Working Days of Employee
        :param max_hours: Maximum hoursthey can work
        :return: Employee wage per month
        """
        IS_FULL_TIME = 1
        IS_PART_TIME = 2
        emp_wage_per_month = 0
        total_emp_hours = 0
        total_working_days = 0
        while total_emp_hours <= max_hours and total_working_days < num_of_days:
            total_working_days += total_working_days
            emp_check = int(random.randint(0, 2))
            if emp_check == IS_FULL_TIME:
                emp_hrs = 8
            elif emp_check == IS_PART_TIME:
                emp_hrs = 4
            else:
                emp_hrs = 0
            total_emp_hours += emp_hrs
            emp_wage_per_day = emp_hrs * emp_rate
            emp_wage_per_month += emp_wage_per_day

        print("Employee Wage Per Month {}".format(emp_wage_per_month))
        return emp_wage_per_month

    def display(self, company, emp_wage_per_month):
        """
        used to display company name and Employee Wage per Month to Console
        :param company: Take Company name
        :param emp_wage_per_month: Get emp wage per month  and print it
        :return:
        """
        print("Company Name= {}".format(company))
        print("Employee Wage Per Month {}".format(emp_wage_per_month))
        return company

    def initialize(self):
        """
        used to start the program by calling all function
        :return:
        """
        try:
            print("Welcome to the Employee Wage Computaion program for Single Company")
            company_name = input("Enter the company name")
            emp_rate = int(input("Enter Employee rate"))
            num_of_days = int(input("Enter the Number of Days"))
            max_hours = int(input("Enter the Max Hours"))
            emp_wage_per_month = self.calculate_employee_wage_for_company(emp_rate, num_of_days, max_hours)
            self.display(company_name, emp_wage_per_month)

        except TypeError as t:
            print(t)
            logging.error(t)

        except Exception as e:
            print(e)
            logging.error(e)
