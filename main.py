from src.game import WordleGame
from src.constant import MAX_ATTEMPTS

def main():
    ...


if __name__ == "__main__":
    main()

game = WordleGame('apple', [], MAX_ATTEMPTS)
x = game.check_guess('pears')
print(x)

