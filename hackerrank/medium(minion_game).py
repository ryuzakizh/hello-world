  def minion_game(string):
  # your code goes here
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin = kevin + (len(string)-i) #Since number of substrings we can make out of a string equals the length of a string, e.g Elnura - length 6 and substrings are E, El, Eln, Elnu, Elnur, Elnura.
        else:
            stuart+=(len(string)-i)
    if kevin>stuart:
        print('Kevin', kevin)
    elif stuart>kevin:
        print('Stuart', stuart)
    else:
        print('Draw')
