from EmployeeWageFactory.empoyee_wage_for_multiple_companies import ComputeEmployeeWageMultipleCompanies
from EmployeeWageFactory.employee_wage_for_single_company import ComputeEmployeeWage


class EmployeeWageFactory:
    def object_factory(self, object_type="single"):
        """
        use to get object of specific type
        :param object_type:
        :return: object of specific type
        """
        emp_object = {
            "single": ComputeEmployeeWage,
            "multiple": ComputeEmployeeWageMultipleCompanies
        }
        return emp_object[object_type]()


if __name__ == "__main__":
    # DEMO OF GETTING OBJECT FROM FACTORY

    employee_wage_factory = EmployeeWageFactory()
    single_obj = employee_wage_factory.object_factory("single")
    single_obj.initialize()
    multi_obj = employee_wage_factory.object_factory("multiple")
    multi_obj.initialize()
