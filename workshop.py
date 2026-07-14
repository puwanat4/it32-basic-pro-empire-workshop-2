quantity = int(input("จำนวนปืนที่รับมาขายกี่กระบอก?"))
cost_price = float(input("ต้นทุนของปืนที่รับมากี่บาท?"))
sell_price = float(input("ราคาที่จะนำไปขายต่อกี่บาท?"))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงานกี่คน?"))

base_cost = cost_price * quantity
income = sell_price * quantity
profit = income - base_cost
boss = profit * 0.8
team = profit * 0.2
t = team / team_members

print("ต้นทุนทั้งหมด:", base_cost, "รายรับทั้งหมด:", income, "กำไรสุทธิ", profit, "จำนวนเงินที่หักไปให้บอส", boss,"จำนวนเงินที่ลูกน้องแต่ละคนได้", t) 
