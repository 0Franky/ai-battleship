from ship import Ship
from fire_result import FireResult

class Field:

  # Init della classe (costruttore)
  # Params:
  # # rowLenght: lunghezza delle righe (passata dal core)
  # # columnLenght: lunghezza delle colonne (passata dal core)
  def __init__(self, rowLenght, columnLenght):
    self.rowLenght = rowLenght
    self.columnLenght = columnLenght
    # Crea il dataset delle navi disponibili da posizionare
    self.ships = [
      Ship(2, "v", 0, 0), 
      Ship(2, "v", 0, 0), 
      Ship(3, "v", 0, 0), 
      Ship(4, "v", 0, 0), 
      Ship(5, "v", 0, 0), 
      Ship(6, "v", 0, 0)
    ]

  # Metodo che resituisce quante navi si possono posizionare
  def getNumerShips(self):
    return len(self.ships)

  # Metodo che permette di posizionare una nave 
  # del dataset all'interno del campo di battaglia
  def shipPositioning(self, indexShip, orientation, startLocationX, startLocationY):
    # Setto l'orientamento [
    # # v = verticale ; 
    # # o = orizzontale ## mai usata -> usato != v
    # ] : stringa
    self.ships[indexShip].setOrientation(orientation)
    # posizionamento della nave tramite le coordinate x-y
    self.ships[indexShip].setPosition(startLocationX, startLocationY)
    # verifico che la posizione sia corretta
    # simulo che la nave sia piazzata nella posizione
    # se corretta la lascio, altrimenti ritorno errore
    self.ships[indexShip].place(True)
    if self.validatePosition(indexShip) == False:
      self.ships[indexShip].place(False)
      # return error
      print("error") # temporaneamente solo scritta errore
    
  # Metodo che verifica che la posizione sia corretta:
  # nessuna collisione o posizionamento oltre il bordo
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
  
  # Metodo che verifica che non ci siano 
  # collisioni tra le navi (navi sovrapposte)
  def detectCollision(self, indexShip1, indexShip2):
    valid = True
    startShip1 = self.ships[indexShip1].getStartLocationX()
    startShip2 = self.ships[indexShip2].getStartLocationX()
    if self.ships[indexShip1].isPlaced() == True and self.ships[indexShip2].isPlaced() == True:
      if self.ships[indexShip1].getOrientation() == self.ships[indexShip2].getOrientation():
        if self.ships[indexShip1].getOrientation() != "v":
          startShip1 = self.ships[indexShip1].getStartLocationY()
          startShip2 = self.ships[indexShip2].getStartLocationY()
        totMaxLenght = min(startShip1, startShip2) + self.ships[indexShip1].getSize() + self.ships[indexShip2].getSize()
        actualLenght = max(startShip1 + self.ships[indexShip1].getSize(), startShip2 + self.ships[indexShip2].getSize()) - min(startShip1, startShip2)
        valid = actualLenght >= totMaxLenght
      else:
        verticalShip = None
        horizzontalShip = None
        if self.ships[indexShip1].getOrientation() == "v":
          verticalShip = self.ships[indexShip1]
          horizzontalShip = self.ships[indexShip2]
        else:
          verticalShip = self.ships[indexShip2]
          horizzontalShip = self.ships[indexShip1]
        valid = not ((verticalShip.getStartLocationX() >= horizzontalShip.getStartLocationX() and verticalShip.getStartLocationX() < horizzontalShip.getStartLocationX() + horizzontalShip.getSize()) and (horizzontalShip.getStartLocationY() >= verticalShip.getStartLocationY() and horizzontalShip.getStartLocationY() < verticalShip.getStartLocationY() + verticalShip.getSize()))
        #code different orientation
    return valid
    
  # Metodo che verifica che la nave 
  # non vada oltre il bordo del campo
  def detectOutBound(self, indexShip):
    start = self.ships[indexShip].getStartLocationX()
    end = self.columnLenght
    if self.ships[indexShip].getOrientation() == "v":
      start = self.ships[indexShip].getStartLocationY()
      end = self.rowLenght
    return start + self.ships[indexShip].getSize() < end

  def fire(self, x, y):
    if x >= 0 and x < self.columnLenght and y >= 0 and y < self.rowLenght:
      return self.isHitted(x, y)
    else: 
      return FireResult.BAD_REQUEST_404

  # Verifica se date due coordinate, il colpo colpisce, 
  # affonda e colpisce una nave, 
  # avviene un miss oppure 
  # è una richiesta non valida 
  # (ad esempio si cerca di colpire 
  # un punto già colpito)
  def isHitted(self, x, y):
    result = FireResult.MISS
    hitted = False
    for ship in self.ships:
      hitted = (ship.getOrientation() != "v" and ship.getStartLocationX() == x and  y >= ship.getStartLocationY() and y <= ship.getStartLocationY() + ship.getSize()) or (ship.getOrientation() == "v" and ship.getStartLocationY() == y and  x >= ship.getStartLocationX() and x <= ship.getStartLocationX() + ship.getSize())
      if hitted == True:
        hittedCell = None
        if (ship.getOrientation() == "v"):
          hittedCell = x - ship.getStartLocationX()
        else:
          hittedCell = y - ship.getStartLocationY()
        
        if ship.isHittable(hittedCell) == True:
          ship.hit(hittedCell)
          if ship.isDestroyed():
            result = FireResult.HITTED_AND_SUNK
          else:
            result = FireResult.HITTED
        else:
            result = FireResult.BAD_REQUEST_404
        break
    return result

  # Metodo che verifica se si ha perso,
  # ovvero se le tutte le proprie (posizionate)
  # navi sono distrutte
  def isLostGame(self):
    isLost = True
    for ship in self.ships:
      if ship.isPlaced() and ship.isDestroyed() == False:
        isLost = False
        break
    return isLost


# # QUICK TEST
# field = Filed(9,9)
# field.shipPositioning(0, "v", 0, 0)
# field.shipPositioning(1, "o", 0, 0)
# field.shipPositioning(1, "o", 1, 0)
# field.shipPositioning(1, "v", 2, 0)
# print(field.ships[0].getSize())
# print(field.ships[0].getOrientation())
# print(field.fire(0,0))
# print(field.fire(1,0))
# print(field.ships[0].hittedCells)
# print(field.isLostGame())