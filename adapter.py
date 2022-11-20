# Система №1
import re


class System: # Класс, представляющий систему
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


# Система №2
class WordCounter: # Обработчик, несовместимый с основной системой
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(WordCounter): # Адаптер к обработчику
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words, key=lambda x: self.adaptee.get_count(x),
                      reverse=True)


text = 'La bla $ la BLA la text text text test'
system_one = System(text)
system_two = WordCounter()
adapter_one_two = WordCounterAdapter(system_two)
system_one.get_processed_text(adapter_one_two)
