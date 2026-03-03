# TODO Найдите количество книг, которое можно разместить на дискете
inf_ob=1.44 # Информационный объем Мб
inf_sim=4 # Для хранения кода одного символа
kol_page=100 # Количество страниц
kol_str=50 # Число строк на странице
kol_sim=25 # Количество символов
convert_inf_ob=inf_ob*2**20 # Перевод в Байты
all_sim=kol_sim*kol_str*kol_page # Количество всех символов
inf_knigi=all_sim*inf_sim # Вес одной книги
kol_knig=convert_inf_ob/inf_knigi
print("Количество книг, помещающихся на дискету:", int(kol_knig))
