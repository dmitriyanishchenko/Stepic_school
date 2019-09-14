import re


"""
Метод re.match(pattern, string)
"""
result = re.match(r'AV', 'AV Analytics Vidhya AV') # метод match ищет указанную подстроку по шаблону в начале строки
print(result) # находит  "<re.Match object; span=(0, 2), match='AV'>"

print(result.group(0)) # выводит её содержимое  "AV"
print(result.start()) # начальная позиция подстроки "0"
print(result.end()) # конечная позиция подстроки "2"

result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print(result) "None"

"""
Метод re.search(pattern, string)
"""
result = re.search(r'Analytics', 'AV Analytics Vidhya AV') # метод search ищет шаблон по всей строке, но возвращает
                                                           # только первое найденное совпадение
print(result) #   <re.Match object; span=(3, 12), match='Analytics'>
print(result.group(0))
print(result.start())
print(result.end())
