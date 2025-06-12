from concurrent.futures import ThreadPoolExecutor
import time

def Squre_Num(num):
    time.sleep(1)
    return f"Squre : {num *num}"
num=[1,2,3,4,5,6,7,8,9]

with ThreadPoolExecutor(max_workers=2) as executor:
    results=executor.map(Squre_Num,num)
    
for result in results:
    print(result)