calls = 0
def count_calls(): # функция счетчик обращений к функциям
    global calls
    calls += 1
    return calls
def string_info(string): # первая функция
    string_1 = (len(string),string.upper(),string.lower()) # формирование строки ответа для вывода на экран
    count_calls() # включаю счетчик
    return string_1
def is_contains(string, list_to_search): # вторая функция
    string = string.lower() # перевожу в нижний регистр строку
    for i in range(len(list_to_search)): # цикл для перевода всех элементов списка в нижний регистр
        list_to_search[i] = list_to_search[i].lower()
    otvet = string in list_to_search # проверка есть ли строка в списке
    count_calls() # включаю счетчик
    return otvet
print(string_info('Поезд'))
print(string_info('Велосипед'))
print(string_info('Самолет'))
print(is_contains('Луна',['лУнтик','ЛуНаТиК','ЛУНАпарк','ЛУнА']))
print(is_contains('Ветер',['вЕрЕтено','ветровкА','ВЕтиР','ВерТИКАль']))
print(calls)

