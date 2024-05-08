class PlayFairCipherDecoder:
  def __init__(self, key):
    self.pf_grid = self.__generate_playfair_grid(key)
  
  def __generate_playfair_grid(self, key: str):
    """
    Generates a Playfair Cipher grid, given a key.
    
    Parameters:
      key (str): The encoded message
    Returns:
      grid (list(list(str))): The Playfair Grid generated with key
    """
    return [["a"]]

  def decode(self, message: str):
    """
    Returns a decoded message which has been encrypted with
    a Playfair cipher.
    
    Parameters:
      message (str): The encoded message
    returns:
      decoded_message (str): The decoded message
    """
    return "init"

message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

playFairCipher = PlayFairCipherDecoder(key)
print(playFairCipher.decode(message))