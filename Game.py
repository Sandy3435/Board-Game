class Game():
    def __init__(self, num_players, curent_player, winner, turn_counter):
        self.num_players = num_players
        self.curent_player = curent_player
        self.winner = winner
        self.turn_counter = turn_counter

class Chess(Game):
    def __init__(self, num_players, curent_player, winner, turn_counter, board, Player1pieces, Player2pieces, checkmate):
        super().__init__(num_players, curent_player, winner, turn_counter)
        self.board = board
        self.Player1pieces = Player1pieces
        self.Player2pieces = Player2pieces
        self.checkmate = checkmate

class Monopoly(Game):
    def __init__(self, num_players, curent_player, winner, turn_counter, properties, BankBalance, DiceRoll, jailstatus):
        super().__init__(num_players, curent_player, winner, turn_counter)
        self.properties = properties
        self.BankBalance = BankBalance
        self.DiceRoll = DiceRoll
        self.jailstatus = jailstatus

class Scabble(Game):
    def __init__(self, num_players, curent_player, winner, turn_counter):
        super().__init__(num_players, curent_player, winner, turn_counter)
        self.
        self.
        self.
        self.






        