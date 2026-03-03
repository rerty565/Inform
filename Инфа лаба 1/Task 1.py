numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_dop=numbers[0:4]+numbers[5:] # номера без пропущенного
Sred_ar=sum(numbers_dop)/len(numbers)
numbers[4]=Sred_ar # добавление в строку среднего арифм
print("Измененный список:", numbers)
