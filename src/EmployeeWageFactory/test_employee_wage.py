from Employee_wage.employeeWage import ComputeEmployeeWage


def test_compute_employee_wagePer_month():
    test_obj = ComputeEmployeeWage("Bridgelabz", 12, 12, 12)
    assert test_obj.calculate_employee_wage_for_company() == 192


def test_display_function():
    test_string = "Atlas"
    test_obj = ComputeEmployeeWage(test_string, 12, 123, 124)
    assert test_obj.display() == "Atlas"
