class CountryMedals:
    def __init__(self, name, NumofGold = 0 , NumofSilver = 0, NumofBronze = 0):
        self.name = name
        self.NumofGold = NumofGold
        self.NumofSilver = NumofSilver
        self.NumofBronze = NumofBronze
    def get_place(self, ranking):
        if ranking == 1:
            self.NumofGold += 1
        elif ranking == 2:
            self.NumofSilver += 1
        elif ranking == 3:
            self.NumofBronze += 1
        else:
            print('The ranking is unacceptable.')
    def getMedal(self):
        print('The num of Gold Medal is : %s'%(self.NumofGold))
        print('The num of Silver Medal is : %s' % (self.NumofSilver))
        print('The num of Bronze Medal is : %s' % (self.NumofBronze))

    @property
    def count(self):
        return ('The total num of Medals is : %s' % (self.NumofGold + self.NumofSilver + self.NumofBronze))

    def __str__(self):
        return ('%s: %d Gold %d Sliver %d Bronze' %(self.name, self.NumofGold, self.NumofSilver, self.NumofBronze))


if __name__ == '__main__':
    china = CountryMedals("中国", 26, 18, 26)
    us = CountryMedals("美国", 46, 37, 38)
    uk = CountryMedals("英国", 27, 23, 17)
    print(china)
    print(us)
    print(uk)
    print("中国获得一个冠军：")
    china.get_place(1)
    print(china)
    print("中国获得一个亚军：")
    china.get_place(2)
    print(china)
    medal_list = [us, uk, china]
    print("按金牌数排序：")
    order_by_count = sorted(medal_list, key=lambda x:x.NumofGold, reverse=True)
    for Country in order_by_count:
        print(Country)
    print("按奖牌数排序：")
    order_by_count = sorted(medal_list, key=lambda x:x.count, reverse=True)
    for Country in order_by_count:
        print(Country)