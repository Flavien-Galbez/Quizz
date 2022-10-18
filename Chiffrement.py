# Conversion table of remainders to
# hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}


# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal

def is_a_letter (lettre) :
  if ord('a')<= ord(lettre)<= ord('z') or ord('A')<= ord(lettre)<= ord('Z'):
    return True
  else :
    return False

def decaller_char (cle, lettre):
  if ord('a')<= ord(lettre)<= ord('z'):
    result = chr(ord(lettre)+(cle%26))
    if ord(result) > ord('z') :
      return chr(ord(result) - 26)
    else :
      return result
  elif ord('A')<= ord(lettre)<= ord('Z'):
    result = chr(ord(lettre)+(cle%26))
    if ord(result) > ord('Z') :
      return chr(ord(result) - 26)
    else :
      return result
  else :
    return lettre


def decaller_texte(cle, texte):
  result=""
  for i in range (len(texte)):
    result = result + str((decaller_char(cle,texte[i])))
  return result

def decaller_texte_v2(cle, texte):
  result=""
  j = True
  for i in range (len(texte)):
    if j :
      char_ = str((decaller_char(cle,texte[i])))
    else :
      char_ = str((recaller_char(cle,texte[i])))
    result = result + char_
    if is_a_letter(char_):
      j = not(j)
  return result

def recaller_char(cle,lettre) :
  if ord('a')<= ord(lettre)<= ord('z'):
    result = chr(ord(lettre)-(cle%26))
    if ord(result) < ord('a') :
      return chr(ord(result) + 26)
    else :
      return result
  elif ord('A')<= ord(lettre)<= ord('Z'):
    result = chr(ord(lettre)-(cle%26))
    if ord(result) < ord('A') :
      return chr(ord(result) + 26)
    else :
      return result
  else :
    return lettre

def chiffrement (cle, text):
  return str(decimalToHexadecimal(int(cle)))+"!"+decaller_texte(int(cle), text)

def chiffrement_v2 (cle, text):
  return str(decimalToHexadecimal(int(cle)))+"!"+decaller_texte_v2(int(cle), text)

def dechiffrement(text):
  cle_hexa=""
  reponse=""
  i=0
  while (text[i] != '!'):
    cle_hexa+=text[i]
    i+=1
  cle=int(cle_hexa,16)
  reponse+= str(cle)
  while i<len(text):
    reponse+= recaller_char(cle,text[i])
    i+=1
  return reponse

def dechiffrement_v2(text):
  cle_hexa=""
  reponse=""
  i=0
  while (text[i] != '!'):
    cle_hexa+=text[i]
    i+=1
  cle=int(cle_hexa,16)
  reponse+= str(cle)
  j=False
  while i<len(text):
    if j :
      char_ = str((decaller_char(cle,text[i])))
    else :
      char_ = str((recaller_char(cle,text[i])))
    reponse = reponse + char_
    i+=1
    if is_a_letter(char_):
      j = not(j)
  return reponse
