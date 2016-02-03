class Game:
  def __init__(self):
    self.current_score = [0, 0]
    
  def score(self, player):
    if player == 1:
      