#encoding:utf-8
'''
#属性方法：
公有属性，私有属性，内置属性
方法：def lambda
公有方法和私有方法，静态方法
'''
class Person:
    def __init__(self,id):
        self.id=id
#         属性测试
class Student(Person):
    attr1="li"      #类公有属性
    __attr2="wang"  # 私有属性
    def __init__(self,id,name,age,num):
        super().__init__(id)
        self.name=name
        self.age=age
        self.__num=num
    def getAge(self):
        return self.age
    def printAttributes(self):
        # print(self.__attr2)
        print("id:{},name:{},age:{}".format(self.id,self.name,self.age))
stu1=Student(213,"zbn",12,121)
# print(stu1.name)       对象属性
# stu1.attr1="tet1" #找实例的属性，没有则创建一个属性并赋值
# Student.attr1="test1"  #
# print(stu1.attr1)       #找实例的属性，没有去类中找
# print(Student.attr1)  #类属性
# print(Student.age)   'Student' has no attribute 'age'
# print(Student._Student__attr2)  #可以访问
# stu1.printAttributes()
# print(dir(stu1))
# print(dir(Student))
# print(Student.__doc__)
# print(Student.__module__)
# print(Student.__class__)
# print(Student.__dict__)
# print(stu1.__class__)

# 方法测试
class Teacher(Person):
    def foo(self, x):
        # super.id=id
        # 类实例方法
        print("executing foo(%s,%s)" % (self, x))
    @classmethod
    def class_foo(cls, x):
        # 类方法
        print("executing class_foo(%s,%s)" % (cls, x))
    @staticmethod
    def static_foo(x):
        # 静态方法
        print("executing static_foo(%s)" % x)

#第一个参数表示父类的属性
tea1=Teacher(2)
tea1.foo('zbn')
# Teacher.foo('zbn')

tea1.class_foo('zbn')
Teacher.class_foo('zbn')

tea1.static_foo('zbn')
Teacher.static_foo('zbn')
# 类方法和静态方法都可以被类和类实例调用，类实例方法仅可以被类实例调用
# 类方法的隐含调用参数是类，而类实例方法的隐含调用参数是类的实例，静态方法没有隐含调用参数