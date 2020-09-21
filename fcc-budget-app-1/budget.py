import math
class Category:
  #Why cant pass ledger here???
  
  def __init__(self,category):
    self.category = category
    self.ledger = []

  def deposit(self,amount,description = ""):
    self.ledger.append({"amount": float(amount), "description": description})

  def withdraw(self,amount,description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -float(amount), "description": description})
      return True
    else: return False

  def get_balance(self):
    sum = 0
    for value in self.ledger:
      sum = sum + value["amount"]  
    return sum
    #return sum(obj["amount"] for obj in self.ledger)

  def transfer(self,amount,categoryObj):
    if self.check_funds(amount):
      self.ledger.append({"amount": -float(amount),"description": f"Transfer to {categoryObj.category}"})
      categoryObj.deposit(amount,f"Transfer from {self.category}")
      return True
    else: return False

  def check_funds(self,amount):
    if sum(obj["amount"] for obj in self.ledger) < amount: 
      return False
    else: return True
  
  def __str__(self):
    string = self.category
    string = string.center(30,"*")
    sumTotal = 0
    string = string + "\n"
    for obj in self.ledger:
      sumTotal = sumTotal + obj["amount"]
      string = string + obj["description"][:23]
      string = string + (30 - len(obj["description"][:23])-len("{:.2f}".format(obj["amount"])))*" " + "%0.2f" % obj["amount"] + "\n"

      #string += obj["description"][:23].ljust(23)+str("{:.2f}".format(obj["amount"]).rjust(7))+"\n"
    return string + "Total: %0.2f" % sumTotal


#Provisorio
def create_spend_chart(categories):
  string = "Percentage spent by category\n"
  i = 100
  withdraw = {}

  #Get thes withdraws
  for obj in categories:
    if obj.category not in withdraw:
      withdraw[obj.category] = 0
    for elemt in obj.ledger:
      if elemt["amount"] < 0:
        withdraw[obj.category] = withdraw[obj.category]+ abs(elemt["amount"])
  
  sumWithdraw = math.floor(sum(withdraw.values())/10)*10

  #Rounded down to the nearest 10
  #withdraw = dict(map(lambda x: (x[0], (math.floor(x[1]/10))*10), withdraw.items() ))
  
  
  while i >= 0:
    string = string + (3 - len(str(i)))*" "+str(i)+"| "
    for key in withdraw:
      if (withdraw[key]/sumWithdraw)*100 >= i:
        string = string + "o  "
      else: string = string + "   "
    i = i - 10
    string = string + "\n"
  
  string = string + "    -" + "---"*len(categories)+ "\n"
  
  initSpace = "     "
  maxWord = max([len(x.category) for x in categories])

  for i in range(maxWord):
    string = string + initSpace
    for obj in categories:
      if len(obj.category) > i:
        string = string + obj.category[i] + "  "
      else:
        string = string + "   "
    string = string + "\n"

  string = string.rstrip() + "  "
  return string