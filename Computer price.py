class Computer:
    def __init__(self):
        self.__maxprice= 2999

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.maxprice=price

c=Computer()
c.sell()

c.__maxprice= 3500
c.sell()

c.setMaxPrice(3500)
c.sell()