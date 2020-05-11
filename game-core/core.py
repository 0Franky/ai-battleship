from game_status import GameStatus
from field import Field

# Numero di righe nella griglia
rowLenght = 9

# Numero di colonne nella griglia
columnLenght = 9

# Numero massimo di navi: 6 [prima avevo scelto 5 con 1 sola da due]
# Orgnizzate come segue:
#   2 navi da 2 celle
#   1 nave da 3 celle
#   1 nave da 4 celle
#   1 nave da 5 celle
#
# GUARDARE es.jpg

# Variabile che indica di chi è il turno corrente
# Può assumere i vaoli 1 o 2 
# rispettivamente al turno del player corrente
currentTurn = 1

# Callback degli utenti:
# Verranno chiamate dopo un attacco e verranno
# passati valori per capirne il risultato:
# # Nave colpita, affondata, vittoria, ecc
callbackPlayer1 = None
callbackPlayer2 = None

FieldPl1 = Field(rowLenght, columnLenght)
StatusPl1 = GameStatus.POSITIONING_SHIPS

FieldPl2 = Field(rowLenght, columnLenght)
StatusPl2 = GameStatus.POSITIONING_SHIPS

def setPlayer1Callback(_callback):
  global callbackPlayer1
  callbackPlayer1 = _callback

def setPlayer2Callback(_callback):
  global callbackPlayer2
  callbackPlayer2 = _callback

# Setta il turno successivo
# Valori 1-2 rispettivamente:
# Player1-Player2
def setNextTurn():
  global currentTurn
  currentTurn = (currentTurn % 2) + 1

