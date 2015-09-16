from pprint import pprint

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

class Employeee:
    """Employee class"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __lt__(self,other):
        return self.age<other.age
        
    def __repr__(self):
        return 'Employee Name:'+repr(self.name) + 'Age:'+repr(self.age)
        

if __name__ == "__main__":
    employeees = [
        Employeee("UNiVeRsE", 26),
        Employeee("Arteezy", 18),
        Employeee("Fear", 27),
        Employeee("Ppd", 23),
        Employeee("Suma1l", 16)]
    pprint(sorted(employeees))
    