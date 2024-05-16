import re

class Playfair:
  """Allows for the decrypting of a message encrypted with the Playfair cipher"""
  def __init__(self, cipherKey, letterToIgnore="J"):
    """
        Parameters
        ----------
        encryptedMessage : str
            The encrypted message (must be an even length)
        cipherKey : str
            The key for the cipher
        letterToIgnore : str, optional
            The letter to ignore in the cipher (default J)
    """    
    self.cipherKey = cipherKey
    self.grid = [[0 for column in range(5)] for row in range(5)]
    self.gridPositions = {}
    self.letterToIgnore = letterToIgnore
  
  """Creates the 5x5 grid for the cipher based on the key"""
  def createPlayfairGrid(self):
    #Remove duplicates for the grid
    cipherDict = dict.fromkeys(self.cipherKey)
    cipherKey = "".join(cipherDict)
    
    #Keep track of what index we are inserting of the cipher key and the alphabet respectively
    keyIndex = 0
    charIndex = ord("A")
    
    #Iterate through the grid and add the cipher key first and then the leters of the alphabet
    for R in range(5):
      for C in range(5):
        if keyIndex < len(cipherKey):
          self.grid[R][C] = cipherKey[keyIndex]
          #Since we're already know the position of the letter in the grid here, lets put it into a dictionary for fast lookup later
          self.gridPositions[cipherKey[keyIndex]]=(R,C)
          keyIndex += 1     
        else:         
          #Skip values that are already inserted and skip the letter J 
          while chr(charIndex) in cipherDict.keys() or chr(charIndex)==self.letterToIgnore:
               charIndex += 1          
          self.grid[R][C] = chr(charIndex)  
          #Put it in the dictionary!
          self.gridPositions[chr(charIndex)]=(R,C)
          charIndex += 1
  
  def decrypt(self, encryptedMessage)-> str:
    """Decrypts the encrypted message and returns the decrypted string"""   
    
    #Lets check and sanitize the string
    encryptedMessage = encryptedMessage.replace(" ","").upper()
    if not encryptedMessage.isalpha():
      return "ERROR: The encrypted message must contain ONLY letters!"   
    if len(encryptedMessage) % 2 != 0:
      return "ERROR: The encrypted message must be an even number of letters!"     
    
    #Set up some variables
    res = ""    
    self.createPlayfairGrid()    
    
    for i in range(0,len(encryptedMessage),2):
      #Lets get the positions of both the left and right characters of the pair that we are looking at
      try:
        left = self.gridPositions[encryptedMessage[i]]
        right = self.gridPositions[encryptedMessage[i + 1]]
      except KeyError:
        return "ERROR: Key not found. Does your encrypted message contain the letter you want to ignore?"

      #If in the same column, we substitute the letter with the letter ABOVE it (wrap around to BOTTOM if bounds are exceeded).
      if (left[1]==right[1]):
        res+=self.decryptColumnPair(left,right)
      #If in the same row, we substitute the letter with the letter to the LEFT of it (wrap around to RIGHT if bounds are exceeded).
      elif (left[0]==right[0]):
        res+=self.decryptRowPair(left,right)
      #Else they form a box, we substitute the ltter with the letter horizontally opposite of the letter in the box.
      else:
        res+=self.decryptBoxPair(left,right)
        
    #Remove special characters, spaces, Xs and return
    res = re.sub('[^A-Za-z0-9]+', '', res).replace("X","").replace(" ","").upper()
    return res  
  
  def decryptColumnPair(self, leftPair, rightPair):
    """Helper to get the decrypted coordinates of a pair of coordinates in the same column"""   
      
    #Account for wrapping
    leftChar = self.grid[leftPair[0]-1 % 5] [leftPair[1]]
    rightChar = self.grid[rightPair[0]-1 % 5] [rightPair[1]]    
    return leftChar + rightChar
  
  def decryptRowPair(self, leftPair, rightPair):
    """Helper to get the decrypted coordinates of a pair of coordinates in the same row"""     
    
    #Account for wrapping
    leftChar = self.grid[leftPair[0]] [leftPair[1]-1 % 5]
    rightChar = self.grid[rightPair[0]] [rightPair[1]-1 % 5]    
    return leftChar + rightChar
  
  def decryptBoxPair(self,leftPair,rightPair):    
    """Helper to get the decrypted coordinates of a pair of coordinates not in the same row or column"""   
    
    #Just swap the columns to get the right coordinates
    leftChar = self.grid[leftPair[0]][rightPair[1]]
    rightChar = self.grid[rightPair[0]][leftPair[1]]    
    return leftChar + rightChar    
  
if __name__ == '__main__':
  #Create an instance of the class and specify our encrypted string, the key, and the leter we want to ignore.
  encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  KEY = "SUPERSPY"
  playfair = Playfair(KEY,"J")  
  print(playfair.decrypt(encryptedMessage)) 