class employee:
    def __init__(self,salary,name):
        self.salary=salary
        self.name=name
        
ram=employee(20000,"Ram")
shyam=employee(22000,"Shayam")
print(ram.salary,shyam.name)
