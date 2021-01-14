def encrypt(password, shift):
 
  cipher = ''
  for char in password: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher

password = "PASSWORD"
shift = 4

print ("Password: "  + password)
print ("Key: " + str(shift))
print ("Encrypted: " + encrypt(password,shift))
