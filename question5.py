def main():

    def reverce_words(str):
        tmpstr = str.split()
        tmpstr.reverse()
        tmpstr = ' '.join(tmpstr)
        return tmpstr

    str = "Then took the other, as just as fair, And having perhaps the better claim, \nBecause it was grassy and wanted wear; Though as for that the passing there \nHad worn them really about the same,"
    print(reverce_words(str))
 

if __name__ == '__main__':

 

    main()
