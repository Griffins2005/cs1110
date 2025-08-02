points = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4,  'i':1,
          'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,
          's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

def score_word(word, mults):
    """ Given `word` & its letter multipliers `mults`, returns word's score, an int

    Precondition (no need to assert): 
        word [str]:  contains only lowercase letters, length >= 1. 
        mults:  list of ints with same length as `word`. 
                Each entry is either 1, 2, or 3. 

        `points` is a dictionary in **global space** (not a parameter of this
        function) as described in the problem text. """

if __name__ == '__main__':

    w0 = "eww"
    w1 = "box"
    w2 = "hi"
    w3 = "we"

    m0 = [1, 1, 1]
    m00 = [1, 2, 3]
    m1 = [1,1,3]
    m2 = [3,1,1]
    m3 = [2,3]

    testcases = [[[w0, m0], 9],
                 [[w0, m00], 21],
                 [[w1,m1], 28],
                 [[w1,m2], 18],
                 [[w2,m3], 11],
                 [[w3, m3], 11]
                 ]

    for item in testcases:
        word = item[0][0]
        ms = item[0][1]
        expected = item[1]

        result = score_word(word, ms)
        print(word + " with mults " + str(ms) + ": "+str(result)) 
        assert result == expected, \
        "Bad result on word " + word + " with mults " + str(ms) + ": " + str(result)
    print("Tests ran without crashing")

