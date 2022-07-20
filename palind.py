def palin(TheWord : str) -> bool :
    TheWord = TheWord.lower().replace(" ", "")
    return TheWord == TheWord[::-1]
    


def run():
    PickAWord : str = input("Enter the word: ")
    # There is some good old practices declaring the variable type using that format above. in Python you can not specify if
    # you choose not to, but, again, it is a good old practice.
    #palin(PickAWord)
    if palin(PickAWord) == True:
            print('IT IS PALINDROME')
    else:
            print ('ITS NOT PALINDROME ')

if __name__ == '__main__':
    run()