# File Meta Data 
import os 

try:
    if  os.path.exists('advanced.txt'):
        size = os.path.getsize('advanced.txt')
        print(size)
        mod_time = os.path.getmtime('advanced.txt')
        print(mod_time)
        os.rename('advanced.txt', 'new_advanced.txt')
        print('renamed')
        os.remove('new_advanced.txt')
        print('removed')
    else:
        print("chi ustgaa biz dee")
except ValueError:  
        print("advenced.txt file baihgui baina") 


