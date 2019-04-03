'''-------------------------------------------------------
   --------------------- Instructions --------------------
   -------------------------------------------------------'''
'''
    - Open the terminal and locate piggypoo.py
    - Input: piggypoo.py
    - Once it is running you may enter in a "Snake Case" string.
      For example, "iqra_is_thirty_eight"

    - Each word should be seperated by underscores
    - Each word should be lowercase
'''
'''-------------------------------------------------------
   ------------------- Helper Functions ------------------
   -------------------------------------------------------'''
#prints the length of a string/list
def recursiveLen(text):
  if(text):
    return recursiveLen(text[1:]) + 1
  return 0

#returns the list without an empty string at the end
#(due to makeList() base case/exit condition)
def fixList(text):
    return text[:-1]

'''-------------------------------------------------------
   ------------------- Recursive function 1: -------------
   Validates if a string contains no upper case letters
   -------------------------------------------------------'''
def noUppers(text):
  if(text):
    letter = text[0]
    textLen = recursiveLen(text)

    #upper case letters
    if('A' <= letter <= 'Z'):
      print("  invalid input: all letters must be lowercase")
      return False

    #lower case letters
    elif('a' <= letter <= 'z'):
      if (textLen == 1): return True
      return noUppers(text[1:])

    #non letters - e.g. -, (), é
    else:
      if (textLen == 1): return True
      return noUppers(text[1:])

'''-------------------------------------------------------
   ------------------- Recursive function 2: -------------
    Returns the index of the leftmost underscore in a string
   -------------------------------------------------------'''
def leftUnder(text):
  if text:
    textLen = recursiveLen(text)
    if(text[0] != '_'):
      if(textLen == 1): #Case: Last remaining char is not '_'.
        return 1 #So we add 1 to the return value to account for the char & stop
      else:      # right there.
        return leftUnder(text[1:]) + 1
    return 0

'''-------------------------------------------------------
   ------------------- Recursive function 3: -------------
   Splits a string based on underscores
   -------------------------------------------------------'''
def makeList(text):
  if (text == "" or text == '_'): #Case: End of text
    return (text,)

  count = leftUnder(text)

  return (text[:count],) + makeList(text[count+1:])

'''-------------------------------------------------------
   ------------------- Recursive function 4: -------------
    Returns the index of the leftmost vowel in a string
   -------------------------------------------------------'''
def leftVowel(text):
  if text:
    textLen = recursiveLen(text)
    if(text[0] != 'a' and text[0] != 'e' and text[0] != 'i' and text[0] != 'o' and text[0] != 'u'):
      if(textLen == 1):
        return 1
      else:
        return leftVowel(text[1:]) + 1
    return 0

'''-------------------------------------------------------
   ------------------- Let's do some pig latin! ----------
   -------------------------------------------------------'''
def pigLatin(text):
  count = leftVowel(text)
  return (text[count:] + text[:count] + "ay")

'''-------------------------------------------------------
   ------------------- Recursive function 5: -------------
    Passes a list of strings into pig latin
   -------------------------------------------------------'''
def pigList(text):
  textLen = recursiveLen(text)
  if (textLen == 1):
    return (pigLatin(text[0]),)
  return (pigLatin(text[0]),) + pigList(text[1:])

  '''-------------------------------------------------------
     ------------------- Main Program ----------------------
     -------------------------------------------------------'''
def main():
  prompt = input("Enter a snake case: ")
  print()

  if(noUppers(prompt)):
      print(fixList(pigList(makeList(prompt))))
  else:
    print("  please try again")
    print()
    main()

#The program runs!
main()
