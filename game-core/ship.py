import numpy as np

class Ship:
  
  # Init della classe (costruttore)
  # Params:
  # # size: lunghezza della nave
  # # orientation
  # # startLocationX
  # # startLocationY
  def __init__(self, size, orientation, startLocationX, startLocationY):
    self.size = size
    # creo un array lungo quanto la lunghezza della nave
    # indica quali celle della nave sono state colpite
    # per questo inizialmente tutte a false
    self.hittedCells = np.empty(size)
    # setto tutte le celle a false
    self.hittedCells.fill(False)
    self.startLocationX = startLocationX
    self.startLocationY = startLocationY
    self.orientation = orientation
    # setto che la nave non è distrutta
    self._isDestroyed = False
    # setto che la nave non è ancora posizionata
    self._isPlaced = False

  def getSize(self):
    return self.size

  def setOrientation(self, orientation):
    self.orientation = orientation

  def getOrientation(self):
    return self.orientation

  def setPosition(self, startLocationX, startLocationY):
    self.startLocationX = startLocationX
    self.startLocationY = startLocationY

  def getStartLocationX(self):
    return self.startLocationX

  def getStartLocationY(self):
    return self.startLocationY

  def isPlaced(self):
    return self._isPlaced

  def place(self):
    self._isPlaced = True

  def setDestroyed(self):
    self._isDestroyed = True

  def isDestroyed(self):
    return self._isDestroyed

  def isHittable(self, indexCell):
    return not self.hittedCells[indexCell]

  def hit(self, indexCell):
    self.hittedCells[indexCell] = True

    # Verifico se la nave sia distrutta
    # se così è, la setto come distrutta
    _isDestroyed = True
    for cell in self.hittedCells:
      if cell == False:
        _isDestroyed = False
        break
    if _isDestroyed == True:
      self.setDestroyed()