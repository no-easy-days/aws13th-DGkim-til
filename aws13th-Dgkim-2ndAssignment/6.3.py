# #6.1
# class Student:
#     def __init__(self, name, student_id,grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#
#     def introduce(self):
#         print(f"안녕하세요 {self.grade} 학년, {self.name} 입니다. 학번은 {self.student_id} 입니다")
#
#
# my_student = Student("철수", 123132, "1")
# my_student.introduce()

#6.2
# class BankAccount:
#     def __init__(self, owner):
#         self.balance = 0
#         self.owner = owner
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if  self.balance < amount:
#             print("잔액이 부족합니다.")
#         else:
#             self.balance -= amount
#     def get_balance(self):
#         return self.balance
#
# account = BankAccount("홍길동")
# account.deposit(10000)
# account.withdraw(3000)
# print(account.get_balance())  # 7000
#
# account.withdraw(10000)
# print(account.get_balance())# 잔액이 부족합니다

# #6.3
# class TodoList:
#     def __init__(self):
#         self.tasks = []
#     def add_task(self, task):
#         self.tasks.append(task)
#     def complete_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#         else:
#             print("없는 테스크 입니다")
#     def show_tasks(self):
#         for task in self.tasks:
#             print(task)
# my_todo = TodoList()
#
# my_todo.add_task("First task")
# my_todo.add_task("Second task")
# my_todo.show_tasks()
#
# print(my_todo.tasks)
#
# my_todo.complete_task("irst task")
# my_todo.show_tasks()

#6.4
#
# from dataclasses import dataclass
#
# @dataclass
# class DatabaseConfig:
#     def __init__(self,host,port,username,password,database):
#         self.host = host
#         self.port = port
#         self.username = username
#         self.password = password
#         self.database = database
#         self.timeout = 30
#         self.pool_size = 5
#
# config = DatabaseConfig(
#     host="localhost",
#     port=3306,
#     username="admin",
#     password="secret123",
#     database="myapp"
# )
#
# print(config)
#


#6.5
# class Ec2instance:
#     def __init__(self,instance_id,name):
#         self.instance_id  = instance_id
#         self.name = name
#         self.status = "stopped"
#     def start(self):
#         self.status = "running"
#     def stop(self):
#         self.status = "stopped"
#
# class Ec2manager:
#     def __init__(self):
#         self.instance_list = []
#
#     def add_instance(self,instance):
#         self.instance_list.append(instance)
#     def start_all(self):
#         for instance in self.instance_list:
#             instance.start()
#     def stop_all(self):
#         for instance in self.instance_list:
#             instance.stop()
#     def get_runnung_count(self):
#         runnung_count = sum(1 for i in self.instance_list if i.status == "running")
#         return runnung_count
#
# web = Ec2instance("i-001", "web-server")
# db = Ec2instance("i-002", "db-server")
# cache = Ec2instance("i-003", "cache-server")
#
# manager = Ec2manager()
# manager.add_instance(web)
# manager.add_instance(db)
# manager.add_instance(cache)
#
# manager.start_all()
# print(manager.get_runnung_count())
#
