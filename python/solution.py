from playfair_cipher.decryption_service import DecryptionService

CIPHER_KEY = 'SUPERSPY'
ENCRYPTED_MESSAGE = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

decrypt_service = DecryptionService(CIPHER_KEY)
decrypted_message = decrypt_service.decrypt(ENCRYPTED_MESSAGE)
print(decrypted_message)