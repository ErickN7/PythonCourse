dic = {'clave1': 100, 'Clave2': 500}
tupleA = dic.popitem()
print(tupleA)
print(dic)

text = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
result = text.lstrip(',:%_#')
print(result)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)