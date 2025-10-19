import json
import os

# Global variables
tasks = []  # List to store all tasks
task_counter = 1  # Counter for generating unique task IDs

def add_task():
    global task_counter
    print("\n=== เพิ่มงานใหม่ ===")
    
    # รับข้อมูลจากผู้ใช้
    title = input("ชื่อเรื่อง: ")
    description = input("รายละเอียด: ")
    due_date = input("วันครบกำหนด (เช่น 2025-12-31): ")
    
    # สร้าง task ใหม่
    task = {
        "id": task_counter,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    
    # เพิ่ม task ลงในรายการ
    tasks.append(task)
    print(f"\nเพิ่มงาน '{title}' เรียบร้อยแล้ว")
    
    # เพิ่ม counter สำหรับ ID ถัดไป
    task_counter += 1

def view_tasks():
    print("\n=== รายการงานทั้งหมด ===")
    
    if not tasks:  # ถ้าไม่มีงานในรายการ
        print("ยังไม่มีงานในรายการ")
        return
    
    # แสดงรายการงานทั้งหมด
    print("\nลำดับ | ชื่องาน | วันครบกำหนด | สถานะ")
    print("-" * 50)
    
    for i, task in enumerate(tasks, 1):
        status = "✓ เสร็จแล้ว" if task["completed"] else "✗ ยังไม่เสร็จ"
        print(f"{i}. {task['title']} | {task['due_date']} | {status}")

def edit_task():
    # แสดงรายการงานก่อน
    view_tasks()
    
    if not tasks:  # ถ้าไม่มีงานในรายการ
        return  # ออกจากฟังก์ชันเลย เพราะไม่มีงานให้แก้ไข
    
    # รับ index จากผู้ใช้
    try:
        index = int(input("\nกรุณาเลือกลำดับงานที่ต้องการแก้ไข: ")) - 1
        
        # ตรวจสอบว่า index ถูกต้องหรือไม่
        if index < 0 or index >= len(tasks):
            print("ลำดับงานไม่ถูกต้อง")
            return
            
        # แสดงเมนูการแก้ไข
        print("\n=== เมนูแก้ไขงาน ===")
        print("1. แก้ไขชื่อเรื่อง")
        print("2. แก้ไขรายละเอียด")
        print("3. เปลี่ยนสถานะงาน")
        
        edit_choice = input("เลือกรายการที่ต้องการแก้ไข (1-3): ")
        
        if edit_choice == "1":
            new_title = input("ชื่อเรื่องใหม่: ")
            tasks[index]["title"] = new_title
            print("แก้ไขชื่อเรื่องเรียบร้อยแล้ว")
            
        elif edit_choice == "2":
            new_description = input("รายละเอียดใหม่: ")
            tasks[index]["description"] = new_description
            print("แก้ไขรายละเอียดเรียบร้อยแล้ว")
            
        elif edit_choice == "3":
            current_status = tasks[index]["completed"]
            tasks[index]["completed"] = not current_status
            status_text = "เสร็จแล้ว" if not current_status else "ยังไม่เสร็จ"
            print(f"เปลี่ยนสถานะเป็น: {status_text}")
            
        else:
            print("ตัวเลือกไม่ถูกต้อง")
            
    except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น")

def delete_task():
    # แสดงรายการงานก่อน
    view_tasks()
    
    if not tasks:  # ถ้าไม่มีงานในรายการ
        return  # ออกจากฟังก์ชันเลย เพราะไม่มีงานให้ลบ
    
    # รับ index จากผู้ใช้
    try:
        index = int(input("\nกรุณาเลือกลำดับงานที่ต้องการลบ: ")) - 1
        
        # ตรวจสอบว่า index ถูกต้องหรือไม่
        if index < 0 or index >= len(tasks):
            print("ลำดับงานไม่ถูกต้อง")
            return
            
        # แสดงข้อมูลงานที่จะลบและขอคำยืนยัน
        task = tasks[index]
        print(f"\nงานที่จะลบ: {task['title']}")
        confirmation = input("ต้องการลบงานนี้จริงหรือไม่ (y/n): ").lower()
        
        if confirmation == 'y':
            deleted_task = tasks.pop(index)
            print(f"\nลบงาน '{deleted_task['title']}' เรียบร้อยแล้ว")
        else:
            print("\nยกเลิกการลบงาน")
            
    except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น")

def save_tasks():
    try:
        with open('tasks.json', 'w', encoding='utf-8') as f:
            # บันทึกทั้ง tasks และ task_counter
            data = {
                'tasks': tasks,
                'task_counter': task_counter
            }
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("\nบันทึกข้อมูลเรียบร้อยแล้ว")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")

def load_tasks():
    global tasks, task_counter
    try:
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                tasks = data['tasks']
                task_counter = data['task_counter']
            print("\nโหลดข้อมูลเรียบร้อยแล้ว")
        else:
            tasks = []
            task_counter = 1
            print("\nเริ่มต้นโปรแกรมด้วยรายการว่าง")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาดในการโหลดข้อมูล: {e}")
        tasks = []
        task_counter = 1

def main():
    # โหลดข้อมูลเมื่อเริ่มโปรแกรม
    load_tasks()
    
    while True:
        print("\n=== Todo List Menu ===")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด")
        print("3. แก้ไขงาน")
        print("4. ลบงาน")
        print("5. ออกจากโปรแกรม")
        
        choice = input("\nกรุณาเลือกเมนู (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()  # บันทึกข้อมูลก่อนออกจากโปรแกรม
            print("ขอบคุณที่ใช้บริการ!")
            break
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()