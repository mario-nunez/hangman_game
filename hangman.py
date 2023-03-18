from utils.utils import hangman_levels

class HangmanGame:
    def __init__(self):
        pass

    def game_set_up(self):
        """
        Welcome message and set up game difficulty.
        """
        print("""Welcome to Hangman!\nPlease select a level of difficulty:\n
            1. Beginner (9 lives)
            2. Intermediate (6 lives)
            3. Expert (4 lives)
        """)

        # TODO: not let the user pick a non-existent option. Let him exit the game.
        user_level = input("Please choose a difficulty by typing its number: ") 

        print(f'You have chosen {hangman_levels[user_level]["level_type"]} difficulty')

    def display_hangman(tries):
        """
        Display hangman based on the numbers of tries left.
        """
        pass
    

if __name__ == "__main__":
    g = HangmanGame()
    g.game_set_up()
