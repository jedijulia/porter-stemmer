class PorterStemmer:
    def isCons(self, letter):
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            return False
        else:
            return True

    def isConsonant(self, word, i):
        letter = word[i]
        if self.isCons(letter):
            if letter == 'y' and isCons(word[i-1]):
                return False
            else:
                return True
        else:
            return False

    def isVowel(self, word, i):
        return not(isConsonant(word, i))

    # *S
    def endsWith(self, stem, letter):
        if stem.endswith(letter):
            return True 
        else: 
            return False

    # *v*
    def containsVowel(self, stem):
        for i in stem:
            if not self.isCons(i):
                return True
        return False  

    # *d
    def doubleCons(self, stem):
        if len(stem) >= 2:
            if self.isConsonant(stem, -1) and self.isConsonant(stem, -2):
                return True
            else: 
                return False
        else:
            return False

    def getForm(self, word):
        form = []
        formStr = ''
        for i in range (len(word)):
            if self.isConsonant(word, i):
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

    def getM(self, word):
        form = self.getForm(word)
        m = form.count('VC')
        return m

    # *o
    def cvc(self, word):
        if len(word) >= 3:
            f = -3
            s = -2
            t = -1
            third = word[t]
            if self.isConsonant(word, f) and self.isVowel(word, s) and self.isConsonant(word, t):
                if third != 'w' and third != 'x' and third != 'y':
                    return True
                else:
                    return False
            else:
                return False
        else: 
            return False

    def replace(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.getM(base) > 0:
            replaced = base + rep
            return replaced
        else:
            return orig

    def replaceM1(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.getM(base) > 1:
            replaced = base + rep
            return replaced
        else:
            return orig

    def step1a(self, word):
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
        
    def step1b(self, word):
        flag = False
        if word.endswith('eed'):
            base = word.rstrip('eed')
            if self.getM(base) > 0:
                word = base
                word += 'ee'
        elif word.endswith('ed'):
            base = word.rstrip('ed')
            if self.containsVowel(base):
                word = base
                flag = True
        elif word.endswith('ing'):
            base = word.rstrip('ing')
            if self.containsVowel(base):
                word = base
                flag = True
        if flag:
            if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
                word += 'e'
            elif self.doubleCons(word) and not self.endsWith(word, 'l') and not self.endsWith(word, 's') and not self.endsWith(word, 'z'):
                word = word[:-1]
            elif self.getM(word) == 1 and self.cvc(word):
                word += 'e'
            else:
                pass
        else:
            pass
        return word

    def step1c(self, word):
        if word.endswith('y'):
            base = word.rstrip('y')
            if self.containsVowel(base):
                word = base
                word += 'i'
        return word

    def step2(self, word):
        if word.endswith('ational'):
            word = self.replace(word, 'ational', 'ate')
        elif word.endswith('tional'):
            word = self.replace(word, 'tional', 'tion')
        elif word.endswith('enci'):
            word = self.replace(word, 'enci', 'ence')
        elif word.endswith('anci'):
            word = self.replace(word, 'anci', 'ance')
        elif word.endswith('izer'):
            word = self.replace(word, 'izer', 'ize')
        elif word.endswith('abli'):
            word = self.replace(word, 'abli', 'able')
        elif word.endswith('alli'):
            word = self.replace(word, 'alli', 'al')
        elif word.endswith('entli'):
            word = self.replace(word, 'entli', 'ent')
        elif word.endswith('eli'):
            word = self.replace(word, 'eli', 'e')
        elif word.endswith('ousli'):
            word = self.replace(word, 'ousli', 'ous')
        elif word.endswith('ization'):
            word = self.replace(word, 'ization', 'ize')
        elif word.endswith('ation'):
            word = self.replace(word, 'ation', 'ate')
        elif word.endswith('ator'):
            word = self.replace(word, 'ator', 'ate')
        elif word.endswith('alism'):
            word = self.replace(word, 'alism', 'al')
        elif word.endswith('iveness'):
            word = self.replace(word, 'iveness', 'ive')
        elif word.endswith('fulness'):
            word = self.replace(word, 'fulness', 'ful')
        elif word.endswith('ousness'):
            word = self.replace(word, 'ousness', 'ous')
        elif word.endswith('aliti'):
            word = self.replace(word, 'aliti', 'al')
        elif word.endswith('iviti'):
            word = self.replace(word, 'iviti', 'ive')
        elif word.endswith('biliti'):
            word = self.replace(word, 'biliti', 'ble')
        return word

    def step3(self, word):
        if word.endswith('icate'):
            word = self.replace(word, 'icate', 'ic')
        elif word.endswith('ative'):
            word = self.replace(word, 'ative', '')
        elif word.endswith('alize'):
            word = self.replace(word, 'alize', 'al')
        elif word.endswith('iciti'):
            word = self.replace(word, 'iciti', 'ic')
        elif word.endswith('ful'):
            word = self.replace(word, 'ful', '')
        elif word.endswith('ness'):
            word = self.replace(word, 'ness', '')
        return word   

    def step4(self, word):
        if word.endswith('al'):
            word = self.replaceM1(word, 'al', '')
        elif word.endswith('ance'):
            word = self.replaceM1(word, 'ance', '')
        elif word.endswith('ence'):
            word = self.replaceM1(word, 'ence', '')
        elif word.endswith('er'):
            word = self.replaceM1(word, 'er', '')
        elif word.endswith('ic'):
            word = self.replaceM1(word, 'ic', '')
        elif word.endswith('able'):
            word = self.replaceM1(word, 'able', '')
        elif word.endswith('ible'):
            word = self.replaceM1(word, 'ible', '')
        elif word.endswith('ant'):
            word = self.replaceM1(word, 'ant', '')
        elif word.endswith('ement'):
            word = self.replaceM1(word, 'ement', '')
        elif word.endswith('ment'):
            word = self.replaceM1(word, 'ment', '')
        elif word.endswith('ent'):
            word = self.replaceM1(word, 'ent', '')
        elif word.endswith('ou'):
            word = self.replaceM1(word, 'ou', '')
        elif word.endswith('ism'):
            word = self.replaceM1(word, 'ism', '')
        elif word.endswith('ate'):
            word = self.replaceM1(word, 'ate', '')
        elif word.endswith('iti'):
            word = self.replaceM1(word, 'iti', '')
        elif word.endswith('ous'):
            word = self.replaceM1(word, 'ous', '')
        elif word.endswith('ive'):
            word = self.replaceM1(word, 'ive', '')
        elif word.endswith('ize'):
            word = self.replaceM1(word, 'ize', '')
        elif word.endswith('ion'):
            result = word.rfind('ion')
            base = word[:result]
            if self.getM(base) > 1 and (self.endsWith(base, 's') or self.endsWith(base, 't')):
                word = base
            word = self.replaceM1(word, '', '')
        return word

    def step5a(self, word):
        if word.endswith('e'):
            base = word[:-1]
            if self.getM(base) > 1:
                word = base
            elif self.getM(base) == 1 and not self.cvc(base):
                word = base
        return word

    def step5b(self, word):
        if self.getM(word) > 1 and self.doubleCons(word) and self.endsWith(word, 'l'):
            word = word[:-1]
        return word

    def stem(self, word):
        word = self.step1a(word)
        word = self.step1b(word)
        word = self.step1c(word)
        word = self.step2(word)
        word = self.step3(word)
        word = self.step4(word)
        word = self.step5a(word)
        word = self.step5b(word)
        return word