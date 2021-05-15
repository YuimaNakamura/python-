class Human:
    def __init__(me,name,age):
      me.name = name
      me.age = age
    def say_name(me):
        me.helloworld()
        print(me.name,me.age)
    def helloworld(me):
        print('a')

Human('中村',22).say_name()
"""s=Human('中村',22)
   s.say_name()   とおいてもプログラムは動く
"""
