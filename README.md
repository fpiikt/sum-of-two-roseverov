ссылка на образ, созданный с помощью докера:

https://hub.docker.com/repository/docker/romanseverov/node/general

# sum-of-two
Сумма двух чисел

Для данного набора целых чисел, содержащихся в кортеже или списке, вернуть индексы двух таких чисел, что их сумма будет равна целевому числу (целочисленный тип данных), заданному в переменной ```target```.

Можно предположить, что каждый входной набор (список/кортеж и целое число) будет иметь ровно одно решение, элемент списка/кортежа не может быть использован дважды. 

## Требования к оформлению решения
1. Программа должна быть написана или внутри функции (```find_sum```), или внутри класса (```SumOfTwo```).
2. Программа должна содержать набор тестов для проверки корректности её выполнения (5-10 штук), тесты пишутся с помощью оператора [assert](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert-stmt).
3. Внутри функции/класса должен находится [docstring](https://www.python.org/dev/peps/pep-0257/) с описанием входных аргументов функции и результата.
4. В начале файла должен быть указан копирайт в формате:

```python
"""
  Автор: Фамилия имя, группа №__
  Ссылка на сайт-портфолио: https://fpiikt.github.io/prg-lng/
  
  Дополнительные комментарии по решению
  
"""
```

Примерная схема файла с решением:
- файл ```main.py```

```python

"""
  Автор: Константинопольский Константин, группа №P4224
  
  Решение реализовано внутри класса SumOfTwo и содержится внутри метода find_sum
 
"""

class SumOfTwo():

    ...
   
    def find_sum(self): 
        ...
   


if __name__ == '__main__':
    res1 = SumOfTwo([2, 7, 11, 15], target=9)
    
    assert res1 == [0, 1], 'ошибка в тестовом примере 1'
    ...
    
```
