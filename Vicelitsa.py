import random
#-----START_FUNCTION-------#
def one_letter():
    index = 0
    #len_word = list(len(word) * '_')
    word1 = word
    word1 = ''.join(word1)
    index = word1.find(letter)
    del len_word[index]
    len_word.insert(index, letter)
    print(*len_word)
    word1 = list(word1)
    del word1[index]
    word1.insert(index, '.')
    #print(word1)

def two_letter():
    index = 0
    # len_word = list(len(word) * '_')
    word1 = word
    word1 = ''.join(word1)
    index = word1.find(letter)
    del len_word[index]
    len_word.insert(index, letter)
    #print(*len_word)
    word1 = list(word1)
    del word1[index]
    word1.insert(index, '.')
    #print(word1)
    word1 = ''.join(word1)
    index = word1.find(letter)
    del len_word[index]
    len_word.insert(index, letter)
    print(*len_word)
    word1 = list(word1)
    del word1[index]
    word1.insert(index, '.')
    #print(word1)

def three_letter():
    index = 0
    # len_word = list(len(word) * '_')
    word1 = word
    word1 = ''.join(word1)
    index = word1.find(letter)
    del len_word[index]
    len_word.insert(index, letter)
    #print(*len_word)
    word1 = list(word1)
    del word1[index]
    word1.insert(index, '.')
    #print(word1)
    word1 = ''.join(word1)
    index = word1.find(letter)
    del len_word[index]
    len_word.insert(index, letter)
    #print(*len_word)
    word1 = list(word1)
    del word1[index]
    word1.insert(index, '.')
    #print(word1)
    word1 = ''.join(word1)
    index = word1.find(letter)
    del len_word[index]
    len_word.insert(index, letter)
    print(*len_word)
    word1 = list(word1)
    del word1[index]
    word1.insert(index, '.')
    #print(word1)
#------END_FUNCTION-------#

n = 0
count_try = 0
print('Как тебя зовут?')
name = input()
print('Привет', name, '!')
print('Не хочешь сыграть в виселицу(Да/Нет)?')
answer = input().lower()
if answer == 'да':
    print('ООооотлично! Тогда сейчас выберу слово и начнем играть')
    print('. . .')
    sp_words = ['радуга', 'записка', 'хачапури', 'айсберг', 'телескоп', 'сдача', 'троллейбус', 'экватор']
    sp_help = ['Находится на небе','Лист для кого-то или чего-то','Еда из грузинской кухни','Плавает по воде','Помогает увидеть то,что находится очень далеко','Выдают в пятёрочке','Наземный транспорт','Теплая линия']
    num = random.randint(0,8)
    word = sp_words[num]
    word1 = word
    print('Игра началась! Начинай угадывать буквы')
    print('И вот тебе подсказка', sp_help[num])
    print(len(word) * ' _')
    len_word = list(len(word) * '_')
    while n == 0:
        letter = input()
        if letter in word1:
            if word1.count(letter) == 1:
                one_letter()
                if ''.join(len_word).isalpha() == True:
                    print('Поздравляю ты угадал(а) слово!')
            if word1.count(letter) == 2:
                two_letter()
                if ''.join(len_word).isalpha() == True:
                    print('Поздравляю ты угадал(а) слово!')
            if word1.count(letter) == 3:
                three_letter()
                if ''.join(len_word).isalpha() == True:
                    print('Поздравляю ты угадал(а) слово!')

        else:
            count_try += 1
            print('Не верно. Этой буквы в этом слове нет. Число попыток:', 6 - count_try)
            if count_try == 6:
                print('Ты проиграл. Игра окончена')
                break

