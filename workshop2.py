name = int(input("ชื่อ?"))
age = int(input("อายุ?"))
height = int(input("สูง?"))
power = int(input("พละกำลัง?"))
money = int(input("เงินติดตัว?"))

if age>=18 and height>=170 and power>=100 and money>20:
    print("ผ่าน")
else:
    print("ไม่ผ่าน")