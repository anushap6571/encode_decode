import base64

prompt = input("Do you want to encode or decode a message? Type 1 or 2 ")
message = input("Enter Message: ")

if prompt == "1":
    encoded_message = message.encode('utf-8')
    print(encoded_message)
elif prompt == "2":
    decoded_message = message.decode('utf-8')
    print(decoded_message)