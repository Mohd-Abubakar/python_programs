cam = int(input('Enter the cost of camera:'))
cam_s = int(input('Enter the number of camera sold:'))
bonus = cam_s*200
commission = cam*(12/100)
salary = 25000+bonus+commission
print('Total salary is',salary)
