#Задание 1


def odd_nums(max_value):
    n=1
    while n <= max_value:
        yield n
        n += 2

odd_to_15 = odd_nums(15)


#Задание 2

max_val = 3
odd_nums_gen = (n for n in range(1, max_val + 1,2))
print(next(odd_nums_gen))


#Задание 3

tutors = ['Иван', 'Анастасия' ,'Петр' ,
          'Сергей' ,'Дмитрий' ,'Борис',]
klasses = ['9A','7B','9Б','9B','8Б','10A','10B']

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))

from itertools import zip_longest

gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)
print(next(gen))


#Задание 4

src = [300, 2, 12, 44, 1, 8, 3, 10, 7, 4, 78, 123, 55]
new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)


#Задание 5


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])