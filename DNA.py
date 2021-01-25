class DNA:
  def __init__ (self, name, weight, worth, quantity):
    self.name = name
    self.weight = weight
    self.worth = worth
    self.quantity = quantity

  def getName(self):
    return self.name

  def getWeight(self):
    return self.weight

  def getQuantity(self):
    return self.quantity

  def getWorth(self):
    return self.worth

  def id(self):
    # template literal new style
    return '{0}, {1} (Worth: {2}, Weight: {3})'.format(self.quantity,self.name,self.worth,self.weight)
  
  def print(self):
    # template literal new style
    print('{0}, {1} (Worth: {2}, Weight: {3})'.format(self.quantity,self.name,self.worth,self.weight))
  