class TestClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # インスタンスメソッド
    def sample_instancemethod(self, display_x=True, display_y=True):
        if display_x:
            print('x is {}'.format(self.x))
        if display_y:
            print('y is {}'.format(self.y))


test_class_1 = TestClass(100, 50)
test_class_1.sample_instancemethod(display_x=False)
