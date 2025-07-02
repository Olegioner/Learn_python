name = input()
with open(f'C:/new/{name}', 'r', encoding='utf-8') as file:
    data_file = set(el.strip() for el in file.readlines())

with open(f'C:/new/with_out_dublicates.txt', 'w', encoding='utf') as result:
    for el in data_file:
        print(el, file=result)