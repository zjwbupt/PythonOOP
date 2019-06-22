from src.developer import Developer
from src.employee import Employee
from src.manager import Manager

dev_1 = Developer('Jianwei','Zhang',40000, 'Python')
mgr_1 = Manager('BJ', 'Lee', 100000, [dev_1])
dev_2 = Employee('First', "Last", 10000)

print(isinstance(mgr_1, Employee))