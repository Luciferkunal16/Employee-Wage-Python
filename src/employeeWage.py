import random


def calculate_employee_wage_for_company(company, emp_rate, num_of_days, max_hours):
    print("Welcome to Employee wage problem ")
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
        print("Empoyee Wage per Day {}".format(emp_wage_per_day))

    print("Employee Wage Per Month {}".format(emp_wage_per_month))
    return emp_wage_per_month


if __name__ == "__main__":
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    calculate_employee_wage_for_company("Bridgelabz", 20, 2, 20)
    calculate_employee_wage_for_company("Quanavis", 30, 4, 35)
