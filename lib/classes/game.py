class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 0 < len(title) and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception
    

        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        
    
    def players(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        return sum(
            [result.score for result in self._results if result.player == player]
        ) / len(self._results)
