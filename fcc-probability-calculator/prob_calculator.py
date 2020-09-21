import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self,**kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for nOfTimes in range(v):
        self.contents.append(k)

  def draw(self,numBallsDrawn):
    if numBallsDrawn >= len(self.contents):
      return self.contents

    ballsRemoved = []
    for i in range(numBallsDrawn):
      color = random.choice(self.contents)
      ballsRemoved.append(color)
      self.contents.remove(color)
    return ballsRemoved

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0

  for n in range(num_experiments):
    hatCopy = copy.deepcopy(hat) 
    result = hatCopy.draw(num_balls_drawn)
    test = True
    listOfExpectedBalls = []

    #Dict to List: {'red':2} == ['red','red']
    for k,v in expected_balls.items():
      for color in range(v):
        listOfExpectedBalls.append(k)

    #Cheking if a item in listExpec.. == result
    for color in listOfExpectedBalls:
      if not color in result:
        test = False
      else: result.remove(color)
        

    if test == True:
      m = m + 1
  
  return m/num_experiments

