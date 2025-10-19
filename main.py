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
    pass

def edit_task():
    pass

def delete_task():
    pass

def main():
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
            print("ขอบคุณที่ใช้บริการ!")
            break
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()