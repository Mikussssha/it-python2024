# TODO Найдите количество книг, которое можно разместить на дискете
volume_disket = 1.44*1024*1024
pages = 100
lines = 50
symbols = 25
weight = 4
volume_book = pages*lines*symbols*weight
quantity = volume_disket//volume_book
quantity = int(quantity)
print("Количество книг, помещающихся на дискету:", quantity)
