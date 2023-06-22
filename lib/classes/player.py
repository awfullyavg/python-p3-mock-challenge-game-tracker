class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception
    
        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result) and new_result not in self._results:
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        if game in self._games_played:
            return True
        else:
            return False 
    
    def num_times_played(self, game):
       return len([game_played for game_played in self._games_played if game_played == game])
    
    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            # Create a baseline / starting point
            max_player = None
            max_score = 0

            for player in Player.all:
                player_avg = game.average_score(player)

                if player_avg > max_score:
                    max_player = player
                    max_score = player_avg
            return max_player
        return None
