from abc import abstractmethod


class EmployeeWageInterface:
    @abstractmethod
    def calculate_employee_wage_for_company(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def initialize(self):
        pass
