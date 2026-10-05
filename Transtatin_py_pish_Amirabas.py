# IN THE NAME OF GOD
# PROJECT MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
# THE NAME OF PROJECT IS 'TRANSLASHON' . <> progect .5 <>

from abc import ABC, abstractmethod

# for translate 'abstract' this class
class BaseTranslator(ABC):

    def __init__(self):
        self._dic = dict() # Encapsulation
        self._org_word = list()

    # add world for child class
    @abstractmethod
    def add_word(self, org, translation):
        pass
        
    # for translation
    @abstractmethod
    def translate(self, sentence):
        pass

    # for evry line of program ...
    def _split_sentens(self, sentence):

        return sentence.split()
        
# child of Base_translator 'very languege translator ...'
class MultilingualTranslator(BaseTranslator):

    def __init__(self):

        # { org:{'en': ..., 'fr': ..., 'ge': ... ...
        super().__init__()  #import
        self.word_count = 0

    # add word to the dic
    # translation: [english, french, german]     
    def add_word(self, org, translation):

        if len(translation) != 3:
            raise ValueError('Each word most haveexactly 3 trans (en , fr, de) !!!')
        
        self._dic[org] = {  # import
            'en': translation[0],
            'fr': translation[1],
            'de': translation[2]
            }

    # get encapsolasion
    def get_dictionary(self):

        return self._dic.copy()

    # target_lan : 'orginal'
    def translate(self, sentence, target_lan = 'org'):

        words = self._split_sentens(sentence)
        trnslation_words = list()
        dic = self._dic
        spase = ' '
        
        for word in words:

            if word in dic:

                if target_lan == 'org': trnslation_words.append(word)

                else: trnslation_words.append(dic[word].get(target_lan, word))
                
            # if not word ,put self 
            else: trnslation_words.append(word)

        return spase.join(trnslation_words)

    # translate to engelish
    def translate_to_engelish(self, sentence):
        
        return self.translate(sentence, 'en')

    # translate to french
    def translate_to_frech(self, sentence):

        return self.translate(sentence, 'fr')
        
    # translate to germani
    def translate_to_germani(self, sentence):

        return self.translate(sentence, 'de')

# polymorphism and extensibility
class Smart_translator(MultilingualTranslator):

    def __init__(self):
        super().__init__()
        self._cache = dict()  # for fasten

    # override metode
    def translate(self, sentence, target_lan = 'org'):

        cache_key = f"{sentence} - {target_lan}"
        catch = self._cache
        
        if cache_key in catch:
            return self._cache[cache_key]
        
        result = super().translate(sentence, target_lan)
        catch[cache_key] = result
        
        return result

    # amar dictionory
    def get_amar(self):

        return {
            'total_words': len(self._dic),
            'cache_words': len(self._cache)
            }
    

class Programing:

    def main(self):
        #child of father ;)
        result = Smart_translator()

        #inputs
        n = input('enter number of words: ')
        n = int(n)

        print(f'enter {n} words (orginal + 3 translation: en, fr, de):')
        for _  in range(n):
            line = input().split()
            org = line[0]
            translation = line[1:4] # 3 translation next
            result.add_word(org, translation)

        sentence = input('\n enter the sentence')

        print('\n --start--')
        print(f'orginal: {result.translate(sentence, "org")}')
        print(f'english: {result.translate_to_engelish(sentence)}')
        print(f'french:  {result.translate_to_frech(sentence)}')
        print(f'germani: {result.translate_to_germani(sentence)}')

        print(f'\namar: {result.get_amar()}')
if __name__ == "__main__":
    result = Programing()
    result.main()
    print("THE END")

print('\n AMIRABAS KHAJEH')
## MADE IN AMIRABAS KHAJEH
