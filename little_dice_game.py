import random as R


class Die:
    def __init__(self):
        self.value = R.randint(1, 6)


class Hand:
    def __init__(self):
        self.hand()

    def hand(self):
        return (Die().value, Die().value, Die().value, Die().value, Die().value)


class Player:
    won_hands = 0

    def __init__(self, name):
        self.name = name
        self.hand = None


class Game:
    hand_number = 0

    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]

    def __str__(self):
        return "%s got: %s --> %s points\n%s got: %s --> %s points" % (
            self.player1.name,
            ", ".join([str(d) for d in self.player1.hand]),
            self.get_points()[0],
            self.player2.name,
            ", ".join([str(d) for d in self.player2.hand]),
            self.get_points()[1],
        )

    def get_game_result(self):
        if not self.it_is_a_tie(self.player1.won_hands, self.player2.won_hands):
            name = self.get_game_winner()
            return "%s WON THE GAME AFTER %s HANDS!!!" % (
                name.upper(),
                self.hand_number,
            )
        else:
            return "THE GAME ENDED IN A TIE"

    def get_game_winner(self):
        if self.player1.won_hands > self.player2.won_hands:
            return self.player1.name
        else:
            return self.player2.name

    def get_hand_result(self):
        if not self.it_is_a_tie(self.get_points()[0], self.get_points()[1]):
            name, score = self.get_hand_winner()
            return "*** Hand winner: %s (%s) ***" % (name, score)
        else:
            return "It's tie on %s points ### Score: %s %s | %s %s" % (
                self.get_points()[0],
                self.player1.name,
                self.player1.won_hands,
                self.player2.name,
                self.player2.won_hands,
            )

    def get_hand_winner(self):
        if self.get_points()[0] > self.get_points()[1]:
            self.player1.won_hands += 1
            return (self.player1.name, self.player1.won_hands)
        else:
            self.player2.won_hands += 1
            return (self.player2.name, self.player2.won_hands)

    def get_points(self):
        return (sum(self.player1.hand), sum(self.player2.hand))

    def it_is_a_tie(self, puntos1, puntos2):
        return puntos1 == puntos2

    def play(self):
        self.player1.hand = Hand().hand()
        self.player2.hand = Hand().hand()


if __name__ == "__main__":
    print("\n")
    print("#" * 20, "DICE GAME", "#" * 20)
    name_player1 = input("Player 1: ")
    name_player2 = input("Player 2: ")
    print("#" * 51, "\n")

    player1 = Player(name_player1)
    player2 = Player(name_player2)

    game = Game([player1, player2])

    while game.hand_number < 10:
        if player1.won_hands < 6 and player2.won_hands < 6:
            game.play()
            game.hand_number += 1
            print("------------ HAND %s ------------" % (game.hand_number))
            print(game)
            print(game.get_hand_result())
            input()
        else:
            break

    print(game.get_game_result())
