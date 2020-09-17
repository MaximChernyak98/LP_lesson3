# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
print(len([char for char in word.lower() if char in vowels]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
num_word = len(sentence.split())
num_char = len(sentence.replace(' ', ''))
print(num_char/num_word)
