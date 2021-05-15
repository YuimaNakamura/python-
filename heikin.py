
#構造体もどき。4つの変数をカプセル化
class Tokuten_data:
    def __init__(self):
        self.name = ''
        self.kokugo =0
        self.sansuu =0
        self.heikin =0.0

    def heikin_c(self):
        #入力:国語の点数、算数の点数
        #戻り値：国語と算数の平均
        self.heikin=(self.kokugo + self.sansuu) / 2

taro =Tokuten_data()
taro.name ='太郎'
taro.kokugo =80
taro.sansuu =90
taro.heikin_c()

hanako =Tokuten_data()
hanako.name='花子'
hanako.kokugo=78
hanako.sansuu=90
hanako.heikin_c()

print(taro.name, 'の平均点：', taro.heikin)
