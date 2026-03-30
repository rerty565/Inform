# TODO Напишите функцию find_common_participants
def find_common_participants(p1, p2, raz=','):
    participants1 = p1.split(raz)
    participants2 = p2.split(raz)

    unik = list(set(participants1).intersection(participants2))
    unik.sort()

    return unik
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
