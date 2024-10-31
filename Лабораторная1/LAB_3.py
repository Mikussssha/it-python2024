# TODO Найдите количество книг, которое можно разместить на дискете
volume_disket=1.44*1024*1024
stranici=100
stroki=50
simvoli=25
ves=4
volume_kniga=stranici*stroki*simvoli*ves
kolvo=volume_disket//volume_kniga
print("Количество книг, помещающихся на дискету:", kolvo)
