from enum import Enum

class FireResult(Enum):
  HITTED = 1
  HITTED_AND_SUNK = 2
  MISS = 3
  BAD_REQUEST_404 = 3 # xD 
                      # Questa situazione si verifica quando 
                      # si tenta di colpire una zona già colpita