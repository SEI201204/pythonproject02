#1. ใช้ ,
print("Hello...",147,'Hi',True,201+204,"Hey")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่เอามาต่อกันต้องเป็น String ไม่มี space ต้องเว้นเอง
# print("Hello..."+147+'Hi'+True+(201+204)+"Hey") จะ Error เพราะบางตัวไม่ใช่ String
print("Hello... "+str(147)+' Hi '+str(True)+' '+str(201+204)+" Hey")
#3. ใช้เมธอด format
print("Hello... {} Hi {} {} Hey" .format(147,True,201+204))
print("Hello... {0} Hi {1} {2} Hey" .format(147,True,201+204)) #index number
#4. ใช้ f-string 
print(f"Hello... {147} Hi {True} {201+204} Hey")
#5. ใช้ modulo/modulas operator (%) -> %d, %f, %C, %s, .....
print("Hello... %d Hi %s %d Hey" %(147,True,201+204))