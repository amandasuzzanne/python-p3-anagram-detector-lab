# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matched_array = []
        namearray = [letter for letter in self.word]
        
        for elem in possible_anagrams:
            elem_letters = [letters for letters in elem]
            if sorted(elem_letters) == sorted(namearray):
                matched_array.append(elem)
            else:
                return matched_array
        return matched_array