from playfair_cipher.cipher_matrix import CipherMatrix

class DecrptionService:
  def __init__(self, cipherKey) -> None:
    self.cipherkey=cipherKey
    self.cipherMatrix = CipherMatrix(cipherKey).get()

  def decrypt(self,message):
    character_pairs = self.__generateCharacterPairs(message)
    decrypted_message_indices = self.__findDecryptMessageIndices(character_pairs)
    decrypted_message = self.__getMessageFromIndices(decrypted_message_indices)
    revealed_decrypted_message = self.__revealDecryptedMessage(decrypted_message)
    return revealed_decrypted_message

  def __generateCharacterPairs(self, message):
    character_pairs=[]
    current_pair=""
    index=0
    while index<len(message):
      if len(current_pair)==1 and current_pair[0]==message[index]:
        current_pair+="X"
      else:
        current_pair+=message[index]
        index=index+1
      if len(current_pair)==2:
        character_pairs.append(current_pair)
        current_pair=""
    return character_pairs
  
  def __findIndices(self, character_pair):
    pair_index=[]
    for each_char in range(2):
      for column in range(0,5):
        for row in range(0,5):
          if self.cipherMatrix[column][row]==character_pair[each_char]:
            pair_index.append([column,row])
          elif character_pair[each_char] in ('I','J') and self.cipherMatrix[column][row] == 'I/J':
            pair_index.append([column,row])
    
    return pair_index
  
  def __findDecryptMessageIndices(self, character_pairs):
    decrypted_message_indices=[]

    for each_character_pair in character_pairs:
      pair_index=self.__findIndices(each_character_pair)
      
      if pair_index[0][1]==pair_index[1][1]:
        decrypted_message_indices.append(self.__sameColumn(pair_index))
      elif pair_index[0][0]==pair_index[1][0]:
        decrypted_message_indices.append(self.__sameRow(pair_index))
      else:
        decrypted_message_indices.append(self.__formsRectangle(pair_index))
    return decrypted_message_indices

  def __sameColumn(self,pair_index):
    new_pair=[[(pair_index[0][0]-1)%5,pair_index[0][1]],[(pair_index[1][0]-1)%5,pair_index[1][1]]]
    return new_pair

  def __sameRow(self,pair_index):
    new_pair=[[pair_index[0][0],(pair_index[0][1]-1)%5],[pair_index[1][0],(pair_index[1][1]-1)%5]]
    return new_pair

    
  def __formsRectangle(self,pair_index):
    new_pair=[[pair_index[0][0],pair_index[1][1]],[pair_index[1][0],pair_index[0][1]]]
    return new_pair
  
  def __getMessageFromIndices(self, decrypted_message_indices):
    newDecyptedMessage=""
    result=self.cipherMatrix
    for i,each_element in enumerate(decrypted_message_indices):
        firstCharIndex = each_element[0]
        e = result[firstCharIndex[0]][firstCharIndex[1]]
        if e == 'I/J':
          e = 'I'
        newDecyptedMessage+=e
        secondCharIndex = each_element[1]
        e = result[secondCharIndex[0]][secondCharIndex[1]]
        if e == 'I/J':
          e = 'I'
        newDecyptedMessage+=e
    return newDecyptedMessage
  
  def __revealDecryptedMessage(self,newDecyptedMessage):
    index=1
    while index<len(newDecyptedMessage)-1:
      if newDecyptedMessage[index]=="X" and newDecyptedMessage[index-1]==newDecyptedMessage[index+1]:
        newDecyptedMessage=newDecyptedMessage.replace(newDecyptedMessage[index],"")
      index=index+1
   
    if newDecyptedMessage[-1]=="X" and len(newDecyptedMessage)%2==0:
     newDecyptedMessage=newDecyptedMessage[:-1]

    return(newDecyptedMessage)

