class Worker:
     def __init__(self, amount):
         self.salary = amount

     def bonus_salary( self ):
       if( self.salary < 4000 ):
         return self.salary + (self.salary * 0.15)
       else:
         return self.salary + (self.salary * 0.08)

     def show_data(self):
         print(":: This worker have the follow amounts ::")
         print("Salary: ", self.salary)
         print("Bonus: ", self.bonus_salary())

