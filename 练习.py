# 定义一个学生类
# 要求：
# 1.属性包括学生姓名、学号，以及语数英三科的成绩
# 2.能够设置学生某科目的成绩
# 3.能够打印出该学生的所有科目成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

        def set_grade(self, course, grade):
            if course in self.grades:
                self.grades[course] = grade
            else:
                print("科目不存在")

        def print_grades(self):
            print(f"学生{self.name}(学号：{self.student_id})的成绩为：")
            for course in self.grades:
                print(f"{course}：{self.grades[course]}")

chen = Student("小陈", "100618")
zeng = Student("小曾", "100622")
print(chen.name, chen.student_id, chen.grades)
zeng.set_grade("数学", 95)
print(zeng.name, zeng.student_id, zeng.grades)
