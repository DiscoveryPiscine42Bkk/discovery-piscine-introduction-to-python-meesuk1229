reservations = []

def show_menu():
    print("\n📋 เมนูหลัก")
    print("1. เพิ่มการจอง")
    print("2. แสดงรายการจองทั้งหมด")
    print("3. ลบการจอง")
    print("4. สรุปจำนวนการจองตามช่วงเวลา")
    print("5. ออกจากโปรแกรม")

def add_reservation():
    print("\n📝 เพิ่มการจองโต๊ะ")
    name = input("ชื่อลูกค้า: ")
    time_slot = input("ช่วงเวลา (เช่น 17:00, 18:00, 19:00): ")
    people = input("จำนวนคน: ")
    reservations.append({'name': name, 'time_slot': time_slot, 'people': people})
    print("✅ จองโต๊ะเรียบร้อยแล้ว!")

def show_all_reservations():
    print("\n📋 รายการจองทั้งหมด")
    if not reservations:
        print("ยังไม่มีการจอง")
    else:
        for i, res in enumerate(reservations, start=1):
            print(f"{i}. {res['name']} - {res['time_slot']} น. ({res['people']} คน)")

def delete_reservation():
    show_all_reservations()
    if reservations:
        try:
            choice = int(input("เลือกหมายเลขการจองที่ต้องการลบ: "))
            if 1 <= choice <= len(reservations):
                removed = reservations.pop(choice - 1)
                print(f"🗑 ลบการจองของ {removed['name']} เวลา {removed['time_slot']} น. เรียบร้อยแล้ว")
            else:
                print("❌ หมายเลขไม่ถูกต้อง")
        except ValueError:
            print("⚠️ กรุณากรอกตัวเลข")

def summarize_by_time():
    print("\n📊 สรุปจำนวนการจองตามช่วงเวลา")
    summary = {}
    for res in reservations:
        time = res['time_slot']
        summary[time] = summary.get(time, 0) + 1
    if not summary:
        print("ยังไม่มีข้อมูลการจอง")
    else:
        for time, count in summary.items():
            print(f"เวลา {time} น. : {count} โต๊ะ")

# เริ่มโปรแกรม
while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")
    if choice == '1':
        add_reservation()
    elif choice == '2':
        show_all_reservations()
    elif choice == '3':
        delete_reservation()
    elif choice == '4':
        summarize_by_time()
    elif choice == '5':
        print("👋 ขอบคุณที่ใช้บริการระบบจองโต๊ะ")
        break
    else:
        print("❌ กรุณาเลือกหมายเลขเมนูให้ถูกต้อง")