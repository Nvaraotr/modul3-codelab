random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_list = list(filter(lambda x: isinstance(x, float), random_list))
int_list = list(filter(lambda x: isinstance(x, int), random_list))
str_list = list(filter(lambda x: isinstance(x, str), random_list))

def int_dict(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_mapped = list(map(int_dict, int_list))

print("Data Float :", float_list)
print("Data Int :")
for item in int_mapped:
    print(item)
print("Data String :", [str for str in str_list])