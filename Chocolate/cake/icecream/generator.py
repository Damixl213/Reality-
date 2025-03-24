from random import randint
def generateAccountNumber():
  card_number= randint(1000000,9999999)
  return f'102{card_number}'

