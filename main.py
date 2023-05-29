from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)

total = {}

for contact in contacts_list[1:]:
    res = contact[1].split() #если в имени есть отчество, то отчество указываем отдельно
    if len(res) == 2:
        contact[2] = res[1]
        contact[1] = res[0]

    res = contact[0].split() #если в фамилии есть имя и отчество, то имя и отчество указываем отдельно

    for i in range(len(res)):
        contact[i] = res[i]

    print(contact[5])
    #pattern = r'(\+7|8|7)?\s*\(?(\d{3,5})\)?\s*(\d{1,3})[- ]?(\d{2})[- ]?(\d{2})'
    pattern = r'(\+7|8|7)?\s*\(?(\d{3})\)?\-?\s*(\d{1,3})[- ]?(\d{2})[- ]?(\d{2})\s*?(\D*\s*\d*\))?'
    new_pattern = r'+7(\2)\3-\4-\5 \6'
    result = re.sub(pattern, new_pattern,contact[5])
    contact[5] = result
    print(result)

    if contact[0] in total:
        n1 = (contact[1] if total[contact[0]][0] == '' else total[contact[0]][0])
        n2 = (contact[2] if total[contact[0]][1] == '' else total[contact[0]][1])
        n3 = (contact[3] if total[contact[0]][2] == '' else total[contact[0]][2])
        n4 = (contact[4] if total[contact[0]][3] == '' else total[contact[0]][3])
        n5 = (contact[5] if total[contact[0]][4] == '' else total[contact[0]][4])
        n6 = (contact[6] if total[contact[0]][5] == '' else total[contact[0]][5])

        total[contact[0]]=[n1, n2, n3, n4, n5, n6]
    else:
        total[contact[0]]=[contact[1], contact[2], contact[3], contact[4], contact[5],contact[6]]

#pprint(contacts_list)
## 1. Выполните пункты 1-3 задания.
## Ваш код
#pprint(total)
contacts_list_new =[]
for key  in total.keys():
    res = []
    res.append(key)
    res.extend(total[key])
    contacts_list_new.append(res)


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list_new)
