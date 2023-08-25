std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
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