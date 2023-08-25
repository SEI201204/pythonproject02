#รับค่า/ป้อนทางแป้นพิมพ์ .ใช้ฟังก์ชั่น input() โดยสิ่งที่ป้อนทั้งหมดถือเป็น String ไม่สามารถนำไปใช้ทำอะไรต่อได้
input('ป้อนรหัสนักศึกษา : ')
input('ป้อนชื่อนักศึกษา : ')
input('ป้อนปีเกิด : ')

#ตัวแปร variable เป็น identifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม ข้อมูลที่เก็บจะอยู่ใน RAM
#identifier คือ ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ
std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
#stdAge = 2023 - stdYearBorn Error ต้องแปลง String เป็น number -> int(), float() 
stdAge = 2023 - int(stdYearBorn)
# ใช้ f-string
print('-----------------------------')
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
print(f"คุณเกิดปี {stdYearBorn} อายุ {stdAge} ปี")
# ใช้ ,
print('-----------------------------')
print("ยินดีต้อนรับ" ,std_id,"ชื่อ" ,std_name,)
print("คุณเกิดปี" ,stdYearBorn, "อายุ" ,stdAge, "ปี")
# ใช้ +
print('-----------------------------')
print("ยินดีต้อนรับ " +std_id+ " ชื่อ " +std_name)
print("คุณเกิดปี " +stdYearBorn+ " อายุ " +str(stdAge)+ " ปี")
# ใช้ เมธอด format
print('-----------------------------')
print("ยินดีต้อนรับ {} ชื่อ {}".format(std_id,std_name))
print("คุณเกิดปี {} อายุ {} ปี ".format(stdYearBorn,stdAge))
# ใช้ %
print('-----------------------------')
print("ยินดีต้อนรับ %s ชื่อ %s" %(std_id,std_name))
print("คุณเกิดปี %s อายุ %d ปี " %(stdYearBorn,stdAge))