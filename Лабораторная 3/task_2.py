# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, n=","):
    set_first_group = set(str1.split(n))
    set_second_group = set(str2.split(n))
    common_list = set_first_group.intersection(set_second_group)
    common_list = list(common_list)
    common_list.sort()
    return(common_list)

# Указанные группы участников
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"



# Вызов функции с запятой в качестве разделителя

print(find_common_participants(participants_first_group, participants_second_group, n="|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
