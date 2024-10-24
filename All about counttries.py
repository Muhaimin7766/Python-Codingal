class China():
    def capital(self):
        print("Beijing is the capital of China")

    def language(self):
        print("Mandarin  is the most widely spoken language of China. ")

    def type(self):
        print("China is a developed country")

class USA:
    def capital(self):
        print("Washington D.C is the capital of USA")

    def language(self):
        print("English and Spanish is the most widely spoken languages in USA")

    def type(self):
        print("USA is developed country.")

obj_chn=China()
obj_USA=USA()

for country in (obj_chn, obj_USA):
    country.capital()
    country.language()
    country.type()