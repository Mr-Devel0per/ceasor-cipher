def is_int(number):
  try:
    int(number)
    return True
  except ValueError:
    return False

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

message = input('What message would you like to code/decode? ')
message = message.lower()

while True:
    code_decode = input('Would you like to code or decode this message? ')
    
    if code_decode.lower() == 'code':
        while True:
            shift = input('How much do you want the message to shift by? ')
            if is_int(shift):
                shift = int(shift)

                coding_message = ''
                for letter in message:
                    if letter in letters:
                        shift = shift % 26
                        coding_message += letters[
                            (letters.index(letter) + shift) % 26]
                    else:
                        coding_message += letter

                break
            else:
                print('Please input a valid number')

        print(coding_message)
        break

    elif code_decode.lower() == 'decode':
        while True:
            shift = input(
                'How much was the message shifted by? type \'unknown\' if you do not know '
            )
            decoding_message = ''
            if is_int(shift):
                shift = int(shift)

                for letter in message:
                    if letter in letters:
                        shift = shift % 26
                        decoding_message += letters[
                            (letters.index(letter) - shift) % 26]
                    else:
                        decoding_message += letter

                break

            elif shift == 'unknown':
                i = 0
                while i <= 26:
                    shift = i

                    for letter in message:
                        if letter in letters:
                            shift = shift % 26
                            decoding_message += letters[
                                (letters.index(letter) - shift) % 26]
                        else:
                            decoding_message += letter
                    print(f'a possible solution is: {decoding_message}')
                    print()
                    decoding_message = ''
                    i = i + 1
                break

            else:
                print('Please input a valid number or type \'unknown\'')

        print(decoding_message)
        break

    else:
        print('Please type \'code\' or \'decode\'')