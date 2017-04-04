import time
#main class
class employees(object):
    salary
    salary_month
    salary_year
    
    def init(self):
        self.salary_month = time.strftime("%m")
        self.salary_year = time.strftime("%m")
        
    def set_salary(self,salary):
        self.salary = salary
        
    def get_salary(self):
        return self.salary
    
    def set_deductions(self,salary):
        self.salary = salary
    def get_deductions(self):
        return self.deductions
        
#managers
class managers(employees):
    allowances

    def set_allowances(self,allowance):
        self.allowances = allowance
        
    def get_allowances(self):
        return self.allowances
        
#surbordinate staff
class surbodinate(employees):
    tips

    def set_tips(self,tip):
        self.tips = tip
        
    def get_tips(self):
        return self.tips
