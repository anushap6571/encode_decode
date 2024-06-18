
def encode(message, key):
    new_message = ""
    for element in message:
        mber = ord(element)
        asc = mber + int(key)
        new_message += chr(asc)
    return new_message

def decode(message, key):
    new_message = ""
    for element in message:
        mber = ord(element)
        asc = mber - int(key)
        new_message += chr(asc)
    return new_message

prompt = input("Do you want to encode or decode a message? Type 1 or 2 ")
message = input("Enter Message: ")
key = input("Enter the correct key: ")

if prompt == "1":
    encoded_message = encode(message, key)
    print(encoded_message)
elif prompt == "2":
    decoded_message = decode(message, key)
    print(decoded_message)