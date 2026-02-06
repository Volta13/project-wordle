from enum import Enum

class LetterStatus(Enum):
    CORRECT = "correct"
    PRESENT = "present"
    ABSENT = "absent"
    UNKNOWN = "unknown"


class WordleGame:
    def __init__(self, target_word, valid_words, max_attempts):
        self.target_word = target_word
        self.valid_words = [word.upper() for word in valid_words]
        self.max_attemps = max_attempts
        self.attempted_words = []
        self.attempts_count = 0
        self.game_won = False

    def is_valid_word(self, word):
        return word.upper() in self.valid_words 
    
    def is_victory(self):
        return self.game_won
    
    def game_over(self):
        return self.game_won or self.attempts_count >= self.max_attemps
    
    def remaining_attemps(self):
        return self.max_attemps - self.attempts_count
    
    def check_guess(self, guess):
        result = []
        target_letters = list(self.target_word)
        guess = guess.upper()

        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                result.append({
                    'letter': letter,
                    'status': LetterStatus.CORRECT
                })
                target_letters[i] = None
            else:
                result.append({
                    'letter': letter,
                    'status': LetterStatus.UNKNOWN
                })
        
        for i, item in enumerate(result):
            if item['status'] is LetterStatus.UNKNOWN:
                letter = item['letter']
                if letter in target_letters:
                    item['status'] = LetterStatus.PRESENT
                    target_letters[target_letters.index(letter)] = None
                else:
                    item['status'] = LetterStatus.ABSENT

        return result
    
    def make_a_guess(self, guess):
        result = self.check_guess(guess)
        self.attempted_words.append(guess)
        self.attempts_count += 1

        if all(letter['status'] == LetterStatus.CORRECT for letter in result):
            self.game_won = True
            
        return result
    