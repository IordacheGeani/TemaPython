from employee import Employee

class Manager(Employee):
    numar_manageri = 0 

    def __init__(self, nume, salariu, departament):
        super().__init__(nume, salariu)
        self.departament = f"F10-{departament}" 
        Manager.numar_manageri += 1

    def display_employee(self):
        print(f"Departament: {self.departament}")

    def __del__(self):
        Manager.numar_manageri -= 1
        super().__del__()


manager1 = Manager("Andrei", 7000, "Resurse Umane")
manager2 = Manager("Ioana", 7500, "Financiar")
manager3 = Manager("Maria", 7200, "Marketing")
manager4 = Manager("Cristian", 6800, "IT")

manager1.display_employee()
manager2.display_employee()
manager3.display_employee()
manager4.display_employee()

angajat1 = Employee("Elena", 5000)

angajat1.display_employee()

print(f"Numărul total de angajați (clasa Employee): {Employee.empCount}")
print(f"Numărul total de manageri (clasa Manager): {Manager.numar_manageri}")
