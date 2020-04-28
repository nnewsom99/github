class State:
  def __init__(self, name, capital, abbr, popul, region, seats):
    self.name=name
    self.capitalCity=capital
    self.abbreviation=abbr
    self.population=popul
    self.region=region
    self.usHouseSeats=seats

  def __str__(self):#might print on a new line
    n = self.name.ljust(15)
    c = self.capitalCity.ljust(15)
    a = self.abbreviation.ljust(15)
    p = str(self.population).ljust(12)
    r = self.region.ljust(16)
    s = self.usHouseSeats.ljust(15)

    return n+c+a+p+r+s
    
  def __gt__(self, strComp):
    i = 0
    s1 = self.name
    s2 = strComp.name
    if len(s1) > len(s2):
      n = len(s2)
    elif len(s1) < len(s2):
      n = len(s1)
    else:
      n = len(s1)

    for x in range(0, n-1):
      if s1[i] > s2[i]:
        return False
      elif s1[i] < s2[i]:
        return True
      else:
        i = i+1


  #getter methods
  def getName(self):
    return self.name
  
  def getCapital(self):
    return self.capitalCity

  def getAbbr(self):
    return self.abbreviation

  def getPopulation(self):
    return str(self.population)

  def getRegion(self):
    return self.region

  def getSeats(self):
    return self.usHouseSeats

"""
setter methods
"""
def setName(self, name):
  self.name = name

def setCapital(self, cap):
  self.capitalCity=cap

def setAbbr(self, ab):
  self.abbreviation=ab

def setPopulation(self, pop):
  self.population=pop

def setRegion(self, reg):
  self.region=reg

def setSeats(self, num):
  self.usHouseSeats=num