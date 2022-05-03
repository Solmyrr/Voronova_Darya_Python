nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(number_of_jokes, nouns, adverbs, adjectives):
    joke_list = []
    count = 0
    # number_of_jokes = 3
    while count < number_of_jokes:
        from random import choice
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke_list.append([noun, adverb, adjective])
        count += 1
    for jokes in joke_list:
        jokes = " ".join(jokes)
        print([jokes])


get_jokes(5, nouns, adverbs, adjectives)
