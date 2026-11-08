# === CS 115 Lab 9 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 9 ===
class Employee:
    def __init__(self, name, eid):
        self.manager = None
        self.name = name
        self.id = eid

    def assign(self, report):
        """assigns an employee to self"""
        report.manager = self

    def __eq__(employee1, employee2):
        """returns if the 2 employees are the same"""
        return employee1.name == employee2.name and employee1.id == employee2.id

    def __str__(employee):
        """prints out the information of the employee"""
        if not employee.manager is None:
            return str(employee.id) + ": " + employee.name + " (Managed by " + str(employee.manager.id) + ": " + employee.manager.name + ")"
        return str(employee.id) + ": " + employee.name

    def promote(self):
        """promotes the employee so their manager is now their managers manager"""
        if self.manager is not None:
                self.manager = self.manager.manager

    def org_depth(self):
        """returns how far down an employee is in the orginizations with the top of the org being 1"""
        if self.manager is None:
            return 1
        return 1 + self.manager.org_depth()

myfile = open("lab9_report.txt", "w")
myfile.write("Jake Talvy")
myfile = open("lab9_report.txt", "r")
data = myfile.read()
print(data)

