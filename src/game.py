
class WordleGame:
    def __init__(self, target_word, valid_words, max_attempts):
        self.target_word = target_word
        self.valid_words = valid_words
        self.max_attemps = max_attempts
        self.attempted_words = []
        self.attempts_count = 0
        self.game_won = False

    def is_valid_word(self, word):
        return word in self.valid_words
    
    def is_victory(self):
        return self.game_won
    
    def game_over(self):
        return self.game_won or self.attempts_count >= self.max_attemps
    
    def remaining_attemps(self):
        return self.max_attemps - self.attempts_count
    
    def check_guess(self, guess):
        result = []
        target_letters = list(self.target_word)

        for i in range(len(guess)):
            if self.target_word[i] == guess[i]:
                result.append()
                target_letters[i] = None
            else:
                result.append()
        
        for i in range(len(guess)):
            if guess[i] in self.target_word:
                result.append()
                target_letters[i] = None
            else:
                result.append()

        return result
    
    def make_a_guess(self, guess):
        ...