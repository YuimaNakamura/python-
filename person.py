class Person(): #クラス名
    def __init__(self, name): #インスタンス化メソッド
        self.myname = name #名前をつける
    def hello(self):
        print("Hello! I am {}.".format(self.myname))
Peter = Person('Peter') #Classの名前(selfの次に書いてある引数に代入する値)
Peter.hello()
