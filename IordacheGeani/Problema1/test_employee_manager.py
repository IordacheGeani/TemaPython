from employee import Employee
from Problema1 import Manager

def setup_function():
    Employee.empCount = 0
    Manager.numar_manageri = 0

def test_employee_creation():
    emp = Employee("Alex", 5000)
    assert emp.name == "Alex"
    assert emp.salary == 5000
    assert Employee.empCount == 1

def test_manager_creation():
    mgr = Manager("Maria", 7000, "Marketing")
    assert mgr.name == "Maria"
    assert mgr.salary == 7000
    assert mgr.departament == "F10-Marketing"
    assert Manager.numar_manageri == 1
    assert Employee.empCount == 1

def test_employee_count_increment():
    emp1 = Employee("Elena", 6000)
    emp2 = Employee("Ion", 5500)
    assert Employee.empCount == 2

def test_manager_count_increment():
    mgr1 = Manager("Andrei", 7500, "Resurse Umane")
    mgr2 = Manager("Ioana", 8000, "IT")
    assert Manager.numar_manageri == 2
    assert Employee.empCount == 2

def test_employee_count_decrement():
    emp = Employee("Vasile", 4500)
    initial_count = Employee.empCount
    del emp
    assert Employee.empCount == initial_count - 1

def test_manager_count_decrement():
    mgr = Manager("Diana", 7200, "Financiar")
    initial_mgr_count = Manager.numar_manageri
    initial_emp_count = Employee.empCount
    del mgr
    assert Manager.numar_manageri == initial_mgr_count - 1
    assert Employee.empCount == initial_emp_count - 1

def test_display_employee_method():
    emp = Employee("George", 5000)
    mgr = Manager("Alina", 7000, "Vânzări")
    assert emp.display_employee() is None
    assert mgr.display_employee() is None
