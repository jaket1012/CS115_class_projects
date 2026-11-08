# === CS 115 Lab 10 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 10 ===
class Employee:
    def __init__(self, name, eid):
        self.manager = None
        self.name = name
        self.id = eid
        self.salary = 0

    def assign(self, report):
        """assigns an employee to self"""
        report.manager = self

    def org_depth(self):
        """returns how far down an employee is in the orginizations with the top of the org being 1"""
        if self.manager is None:
            return 1
        return 1 + self.manager.org_depth()

    def promote(self):
        """promotes the employee so their manager is now their managers manager"""
        if self.manager is not None:
                self.manager = self.manager.manager

    def give_raise(self, amount):
        """sets the employees salary to a given amount. If the employees new salary is higher than their managers, promotes the employee"""
        if amount < self.salary:
            return print("you cannot lower an employees salary")
        self.salary = amount
        if self.manager is not None:
            if self.manager.salary < self.salary:
                self.manager.give_raise(amount)

class Mentor(Employee):
    def __init__(self, name, eid):
        super().__init__(name, eid)
        self.mentee = None
        
    def assign_mentee(self, employee):
        """sets the mentors mentee to employee unless the mentor is the employees manager"""
        if employee.manager is self:
            return
        self.mentee = employee

    def recommend(self):
        """promotes the mentee if they are 2 spots down the org chart or more""" 
        if (self.mentee.org_depth() - self.org_depth()) > 1:
            self.mentee.promote()

class Embezzler(Employee):
    def give_raise(self, amount):
        new_amt = self.salary + ((amount - self.salary) * 2)
        if amount < self.salary:
            return print("you cannot lower and employees salary")
        self.salary = new_amt
        if self.manager is not None:
            if self.manager.salary < self.salary:
                self.manager.give_raise(new_amt)

class Manager(Employee):
    def __init__(self, name, eid):
        super().__init__(name, eid)
        self.reports = []

    def assign(self, report):
        """assigns an employee to self and adds that employee to the managers reports if the reports former manager wasn't also an instance of Manager"""
        current_manager = report.manager
        report.manager = self
        if not isinstance(current_manager, Manager):
            self.reports += [report]

    def reassign(self, employee):
        """reassigns all of selfs employees to the given employee"""
        employee.reports = self.reports
        def assign_to_employee(self, employee):
            if self.reports == []:
                return []
            employee.assign(self.reports[0])
            self.reports = self.reports[1:]
            assign_to_employee(self, employee)
        assign_to_employee(self, employee)

myfile = open("lab10_report.txt", "r")

    
        
        
