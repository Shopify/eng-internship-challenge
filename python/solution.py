from grid import Grid
from encrypt import Encryptor
from decrypt import Decryptor
from utils import Utils

def main():
    """
    Main function to run the encryption and decryption process.
    """
    # Example messages
    message_to_encrypt = 'pursueagain'
    encrypted_message_to_decrypt = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    
    # Create and fill the grid
    input_string = "superspy"
    rows, cols = 5, 5  # Define the size of the matrix
    alpha_string = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    grid = Grid(input_string, rows, cols)
    matrix = grid.create_unique_matrix()
    filled_matrix = grid.fill_remaining_matrix(matrix, alpha_string)

    # Initialize encryptor and decryptor
    encryptor = Encryptor()
    decryptor = Decryptor()

    # Encrypt a message (if needed)
    encrypted_message = encryptor.encrypt_message(message_to_encrypt, filled_matrix)
    
    # Decrypt the provided encrypted message
    decrypted_message = decryptor.decrypt_message(encrypted_message_to_decrypt, filled_matrix)

    # Print the final decrypted message for the test to capture
    print(decrypted_message)

if __name__ == "__main__":
    main()
