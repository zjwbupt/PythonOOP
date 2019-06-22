from employee import Employee
from developer import Developer

dev_1 = Developer('Jianwei','Zhang',40000)
dev_2 = Employee('First', "Last", 10000)


print(dev_1.pay)
dev_1.apply_raise()

print(dev_1.pay)