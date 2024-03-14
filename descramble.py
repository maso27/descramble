# descramble.py
# 3.14(159265...).2024
# Mason Stone
#
# With an input string of letters, iterate through all possible combinations
# and print out words that are created
# Note: repeated letters will yield duplicate results

try:
    import enchant
    d = enchant.Dict("en_US")
    enchanted = True
except:
    print('No enchant install found.\nShowing all possible combinations.')
    enchanted = False
    short_words = False

MIN_WORD_LENGTH = 3

# recursive function, trying all possible combinations of letters
def iterate(letters_in):
    if len(letters_in) < 2:
        return [letters_in]
    revolved = []
    results = []
    letters = letters_in[:]
    for a in range(len(letters)):
        revolved = revolved + [letters]
        letters = letters[1:] + [letters[0]]
    for word in revolved:
        first_letter = [word[0]]
        layer_1 = iterate(word[1:])
        for layer_1_line in layer_1:
            new_result = first_letter + layer_1_line
            if short_words and len(new_result) >= MIN_WORD_LENGTH:
                if d.check(''.join(new_result)):
                    print(''.join(new_result))
            results.append(new_result)
    return results


if enchanted:
    print("Do you want to detect shorter words? (y/n)")
    yesno = input()
    if yesno.lower() == 'y' or yesno.lower() == 'yes':
        short_words = True
        print(" Will do.")
    else:
        short_words = False
        print(" Gotcha. Only long words.")


letters = []
print("Type in a string of letters:")
str_in = input()
print(" Finding Results:\n")
for ch in str_in:
    letters.append(ch)

words_out = iterate(letters)

if short_words == False:
    for word in words_out:
        str_word = ''.join(word)
        if enchanted:
            if d.check(str_word):
                print(str_word)
        else:
            print(''.join(word))

print("\n --- Done ---")
