''' Cifrado Cesar '''

def encrypt(text, key):
    ''' Encrypts a string using key as the displacement on the Caesar
    Algorithm '''
    result = ""
    for letter in text:
        if letter.isupper():
            result += chr((ord(letter) + key - 65) % 26 + 65)
        elif letter.islower():
            result += chr((ord(letter) + key - 97) % 26 + 97)
        else:
            result += letter
    return result

def ingest_data():
    ''' Receives the data needed for the decryption or encryption. '''
    message = input("Enter the message to work with: ")
    key = int(input("Enter the key: "))
    return message, key

def print_menu():
    ''' Prints the menu to make the program easy to use. '''
    print("Please select and option:")
    print("  1. Encrypt a message")
    print("  2. Decrypt a message")
    print("  0. Exit")
    return int(input("Select an option: "))


# Main
print("=====================================")
print("Welcome to the Caesar Cypher Suite.")
print("=====================================")
while True:
    option = print_menu()
    if option == 0:
        break
    message, key = ingest_data()
    if option == 1:
        print("The result is: ", encrypt(message, key))
    elif option == 2:
        print("The result is: ", encrypt(message, 26-key))
    else:
        print("Not a valid option.")
print("=====================================")
print("Bye from the Caesar Cypher Suite.")
print("=====================================")
