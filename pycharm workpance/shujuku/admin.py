from Chaxun import chaxun
from Add_student import add_student
from Delect_student import delect_student
from Update_student import update_student


def admin():
    print("*" * 30)
    print("所有可执行的操作列表")
    print("执行数据表增加操作，请按1")
    print("执行数据表删除操作，请按2")
    print("执行数据表更新操作，请按3")
    print("执行数据表单条数据查询操作，请按4")
    print("退出请按其他键")
    print("*" * 30)
    while True:
        i = int(input("请输入您要进行的操作："))
        if i == 1:
            add_student()
        elif i == 2:
            delect_student()
        elif i == 3:
            update_student()
        elif i == 4:
            chaxun()
        else:
            break


admin()
