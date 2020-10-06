

class IceCream:
    price = 1
    ingre = 'sokolad'
    yagliliq = 10
    
    forma = 'romb'
    # ceki = 100
    erime_tempraturu = 2
    cari_veziyyet = 'donmus'

    def __init__(self, new_ingre, new_forma, new_ceki, new_yagliliq, new_price=None): # constructor
        self.ceki = new_ceki
        
        self.ingre = new_ingre
        self.yagliliq = new_yagliliq
        self.forma = new_forma
        if new_price:
            self.price = new_price

    def tempratur_deyisdi(self, temp):
        if temp > self.erime_tempraturu:
            self.cari_veziyyet = 'Erimis'
        else:
            self.cari_veziyyet = 'Donmus'
    
    def __del__(self):
        print('Obyekt silindi!')

    def __str__(self,):
        return f'ingre: {self.ingre} forma: {self.forma} cari veziyyet: {self.cari_veziyyet}'
    # def set_form(self, yeni_forma):
    #     self.forma = yeni_forma


class Eskimo(IceCream):
    # erime_tempraturu = 3

    def __init__(self, new_forma, new_ceki, new_yagliliq, new_price=None): # constructor
        super().__init__('sokaladli', new_forma, new_ceki, new_yagliliq, new_price=None)


esk = Eskimo('romb', 200, 10)

print('Eskimo 1-in xususiyyetleri')
print('Eskimo ingre:', esk.ingre)
print('Eskimo forma:', esk.forma)
print('Eskimo ceki:', esk.ceki)
print('Eskimo yagliliq:', esk.yagliliq)
print('Eskimo price:', esk.price)

print('Eskimonin cari veziyyeti:', esk.cari_veziyyet)
print('Eskimo dondurucudan cixarildi!')
esk.tempratur_deyisdi(3)
print('Eskimonin cari veziyyeti:', esk.cari_veziyyet)

print(esk)

# print(plombir)
# # del plombir.cari_veziyyet

# # print(plombir.cari_veziyyet)
# # del plombir
# # print(plombir)

# plombir2 = IceCream('Sokaladli', 'konus', 100, 15, 5)

# print('Plombir 2-in xususiyyetleri')
# print('Plombir ingre:', plombir2.ingre)
# print('Plombir forma:', plombir2.forma)
# print('Plombir ceki:', plombir2.ceki)
# print('Plombir yagliliq:', plombir2.yagliliq)
# print('Plombir price:', plombir2.price)


# plombir3 = IceCream()

# print('Plombirin formasi:', plombir.forma)

# plombir.forma = 'konus'

# print('Plombirin formasi:', plombir.forma)

# print('cekisi:', plombir.ceki)
# print('yagliligi:', plombir.yagliliq)

# print('cari veziyyeti', plombir.cari_veziyyet)
# print('Plombir dondurucudan cixarildi')
# plombir.tempratur_deyisdi(10)
# print('Plombir cari veziyyeti', plombir.cari_veziyyet)

# eskimo = IceCream()

# print('Eskimo cari veziyyet', eskimo.cari_veziyyet )