from ship import Ship
from fire_result import FireResult

class Filed:

  def __init__(self, rowLenght, columnLenght):
    self.rowLenght = rowLenght
    self.columnLenght = columnLenght
    self.ships = [
      Ship(2, "v", 0, 0), 
      Ship(2, "v", 0, 0), 
      Ship(3, "v", 0, 0), 
      Ship(4, "v", 0, 0), 
      Ship(5, "v", 0, 0), 
      Ship(6, "v", 0, 0)
    ]

  def shipPositioning(self, indexShip, orientation, startLocationX, startLocationY):
    self.ships[indexShip].setOrientation(orientation)
    self.ships[indexShip].setPosition(startLocationX, startLocationY)
    if self.validatePosition(indexShip) == False:
      self.ships[indexShip].place()
    else:
      # return error
      print("error")
    
  def validatePosition(self, indexShip):
    valid = True
    for i in range(len(self.ships)):
      if i != indexShip:
        valid = self.detectCollision(indexShip, i)
      else:
        valid = self.detectOutBound(indexShip)

      if valid == False:
        break
    return valid
    
  def detectCollision(self, indexShip1, indexShip2, recalculateInvers = True):
    valid = True
    startShip1 = self.ships[indexShip1].getStartLocationX()
    startShip2 = self.ships[indexShip2].getStartLocationX()
    if self.ships[indexShip1].getOrientation() == self.ships[indexShip2].getOrientation():
      if self.ships[indexShip1].getOrientation() != "v":
        startShip1 = self.ships[indexShip1].getStartLocationY()
        startShip2 = self.ships[indexShip2].getStartLocationY()
      valid = startShip2 < startShip1 or startShip2 > startShip1 + self.ships[indexShip1].getSize()
    else:
      if startShip2 >= startShip1 and startShip2 <= startShip1 + self.ships[indexShip1].getSize():
        if self.ships[indexShip1].getOrientation() == "v":
          valid = self.ships[indexShip2].getStartLocationX() >= self.ships[indexShip1].getStartLocationX() and self.ships[indexShip2].getStartLocationX() <= self.ships[indexShip1].getStartLocationX() + self.ships[indexShip1].getSize()
        else:
          valid = self.ships[indexShip1].getStartLocationX() >= self.ships[indexShip2].getStartLocationX() and self.ships[indexShip1].getStartLocationX() <= self.ships[indexShip2].getStartLocationX() + self.ships[indexShip2].getSize()

    if (valid == True):
      valid = (indexShip1, indexShip2, False)
    return valid
    
  def detectOutBound(self, indexShip):
    start = self.ships[indexShip].getStartLocationX()
    end = self.columnLenght
    if self.ships[indexShip].getOrientation() == "v":
      start = self.ships[indexShip].getStartLocationY()
      end = self.rowLenght
    return start + self.ships[indexShip].getSize() < end

  def fire(self, x, y):
    return self.isHitted(x, y) # ricordo che volevo scrivere qualcos'altro qui ma non ricordo cosa

  def isHitted(self, x, y):
    result = FireResult.MISS
    hitted = False
    for ship in self.ships:
      hitted = (ship.getOrientation() == "v" and ship.getStartLocationX() == x and  y >= ship.getStartLocationY() and y <= ship.getStartLocationY() + ship.getSize()) or (ship.getOrientation() != "v" and ship.getStartLocationY() == y and  x >= ship.getStartLocationX() and x <= ship.getStartLocationX() + ship.getSize())
      if hitted == True:
        hittedCell
        if (ship.getOrientation() == "v"):
          hittedCell = y - ship.getStartLocationY()
        else:
          hittedCell = x - ship.getStartLocationX()
        
        if ship.isHittable(hittedCell):
          if ship.isDestroyed():
            result = FireResult.HITTED_AND_SUNK
          else:
            result = FireResult.HITTED
        else:
            result = FireResult.BAD_REQUEST_404
        break
    return result

  def isLostGame(self):
    isLost = True
    for ship in self.ships:
      if ship.isDestroyed() == False:
        isLost = False
        break
    return isLost