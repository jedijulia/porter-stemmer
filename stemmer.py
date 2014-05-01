def isCons(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return False
    else:
        return True

def isConsonant(word, i):
    letter = word[i]
    if isCons(letter):
        if letter == 'y' and isCons(word[i-1]):
            return False
        else:
            return True
    else:
        return False

def isVowel(word, i):
    return not(isConsonant(word, i))

# *s
def endsWith(stem, letter):
    if stem.endswith(letter):
        return True 
    else: 
        return False

# *v*
def containsVowel(stem):
    for i in stem:
        if not isCons(i):
            return True
    return False  

# *d
def doubleCons(stem):
    if len(stem) >= 2:
        if isConsonant(stem, -1) and isConsonant(stem, -2):
            return True
        else: 
            return False
    else:
        return False

def getForm(word):
    form = []
    formStr = ''
    for i in range (len(word)):
        if isConsonant(word, i):
            if i != 0:
                prev = form[-1]
                if prev != 'C':
                    form.append('C')
            else:
                form.append('C')
        else:
            if i != 0:
                prev = form[-1]
                if prev != 'V':
                    form.append('V')
            else:
                form.append('V')
    for j in form:
        formStr += j
    return formStr

def getM(word):
    form = getForm(word)
    m = form.count('VC')
    return m

# *o
def cvc(word):
    if len(word) >= 3:
        f = -3
        s = -2
        t = -1
        third = word[t]
        if isConsonant(word, f) and isVowel(word, s) and isConsonant(word, t):
            if third != 'w' and third != 'x' and third != 'y':
                return True
            else:
                return False
        else:
            return False
    else: 
        return False

def step1a(word):
    if word.endswith('sses'):
        word = word.rstrip('sses') 
        #e removed by rstrip
        word += 'ess' 
    elif word.endswith('ies'):
        word = word.rstrip('ies') 
        word += 'i'
    elif word.endswith('ss'):
        word = word.rstrip('ss') 
        word += 'ss'
    elif word.endswith('s'):
        word = word.rstrip('s')
    else:
        pass
    return word
    
def step1b(word):
    flag = False
    if word.endswith('eed'):
        base = word.rstrip('eed')
        if getM(base) > 0:
            word = base
            word += 'ee'
    elif word.endswith('ed'):
        base = word.rstrip('ed')
        if containsVowel(base):
            word = base
            flag = True
    elif word.endswith('ing'):
        base = word.rstrip('ing')
        if containsVowel(base):
            word = base
            flag = True
    if flag:
        if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
            word += 'e'
        elif doubleCons(word) and not endsWith(word, 'l') and not endsWith(word, 's') and not endsWith(word, 'z'):
            word = word[:-1]
        elif getM(word) == 1 and cvc(word):
            word += 'e'
        else:
            pass
    else:
        pass
    return word





        
