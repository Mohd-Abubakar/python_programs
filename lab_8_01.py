from pathlib import Path
import os
print(Path.cwd())
print(Path.home())
#Path(r'C:\Users\lenovo\ISE').mkdir()
file1 = open(r'C:\Users\lenovo\ISE\mce.txt','w')
file1.write('Hello Mce Hsn')
file1.close()
print(os.path.getsize(r'C:\Users\lenovo\ISE\mce.txt'))
print(os.listdir(r'C:\Users\lenovo\ISE'))
