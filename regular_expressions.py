import re


"""
Метод re.match(pattern, string)
"""
result = re.match('AV', 'AV Analytics Vidhya AV') # метод match ищет указанную подстроку по шаблону в НАЧАЛЕ строки
print(result) # находит  "<re.Match object; span=(0, 2), match='AV'>"

print(result.group(0)) # выводит её содержимое  "AV"
print(result.start()) # начальная позиция подстроки "0"
print(result.end()) # конечная позиция подстроки "2"

result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print(result) # "None"

print('_'*100)

"""
Метод re.search(pattern, string)
"""
result = re.search('Analytics', 'AV Analytics Vidhya AV') # метод search ищет шаблон ПО ВСЕЙ строке, но возвращает
                                                           # только ПЕРВОЕ найденное совпадение
print(result) #   <re.Match object; span=(3, 12), match='Analytics'>

print(result.group(0)) # выводит её содержимое  "Analytics"
print(result.start()) # начальная позиция подстроки "3"
print(result.end()) # конечная позиция подстроки "12"
print('_'*100)


"""
Метод re.findall(pattern, string): этот метод возвращает СПИСОК ВСЕХ найденных СОВПАДЕНИЙ. Он может работать и как re.match()
и как re.search(). Поэтому  рекомендуется использовать для поиска именно его
"""
result = re.findall('AV', 'AV Analytics Vidhya AV')
print(result) # "['AV', 'AV']"
print('_'*100)

"""
Метод re.split(pattern, string, [maxsplit=0]): Этот метод разделяет строку по заданному шаблону
"""

result = re.split('y', 'Analytics')
print(result) # "['Anal', 'tics']"
print('_'*100)

# Если указать аргумент maxsplit, не равное 0 (т.к. по умолчанию этот аргумент равен 0) -
# то разделение будет произведено не более указанного количества раз


result = re.split('i', 'Analytics Vidhya') # всевозможные варианты
print(result) # ['Analyt', 'cs V', 'dhya']

result = re.split('i', 'Analytics Vidhya', maxsplit=1)
print(result) # ['Analyt', 'cs Vidhya']

print('_'*100)

"""
Метод re.sub(pattern, repl, string) ищет  шаблон в строке и заменяет его на указанную подстроку(repl). 
Если шаблон не найден, строка остается неизменной
"""

result = re.sub('India', 'the World', 'AV is largest Analytics community of India')
print(result) # "AV is largest Analytics community of the World"

"""
Mетод re.compile(pattern, repl, string).
Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска
"""
pattern = re.compile('AV')

result = pattern.findall('AV Analytics Vidhya AV')
print(result) # "['AV', 'AV']"

result2 = pattern.findall('AV is largest Analytics community of India')
print(result2) # ['AV']
