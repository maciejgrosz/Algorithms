def naive_alg(pattern, txt):
    m = len(pattern)
    n = len(txt)
    res = []
    if m == 0 or n == 0:
        print(f'Naive: Some string empty')
        return res
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if txt[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            # print(f'Naive: Pattern found at index {i}')
            res.append(i)
    if res == []: print(f'Naive: Pattern not found')
    return res

# TODO: fix for multiple pattern occurrences
def KMP_alg(pattern, txt):
    m = len(pattern)
    n = len(txt)
    res = []
    if m == 0 or n == 0:
        print(f'KMP: Some string empty')
        return res
    
    alphabet = set()
    for letter in pattern:
        alphabet.add(letter)

    dfa = {}
    for l in alphabet:
        dfa[l] = [0]*m  # {a: [0]} itd

    dfa[pattern[0]][0] = 1
    x = 0
    for j in range(1, m):
        for c in alphabet:
            dfa[c][j] = dfa[c][x]
        dfa[pattern[j]][j] = j + 1
        x = dfa[pattern[j]][x]

    x = 0  # stan startowy
    for i, letter in enumerate(txt):
        if letter in dfa:
            x = dfa[letter][x]
            if x == m:
                # print(f'KMP: Pattern found at index {i-m+1}')
                res.append(i - m + 1)
                x = m-1 # not perfect solution, there are some problems
        else:
            x = 0

    if res == []: print(f'KMP: Pattern not found')
    return res

def RK_alg(pattern, txt):

    d = 256  # number of characters in input alphabet
    q = 109  # prime number
    M = len(pattern)
    N = len(txt)
    i = 0
    j = 0
    p = 0   # hash value for pattern
    t = 0   # hash value for txt

    res = []

    if M > N:
        print(f'RK: Pattern longer than text')
        return res

    if M == 0 or N == 0:
        print(f'RK: Some string empty')
        return res
  
    # Calculate the hash value of pattern and first window 
    # of text
    # The number is represented in no. of characters base
    for i in range(M):
        p = (p + d**(M-1-i) * ord(pattern[i]))% q
        t = (t + d**(M-1-i) * ord(txt[i]))% q

    # unikanie potegowania w celu przyspieszenia kodu - mnożenie przez d
  
    # Slide the pattern over text one by one
    for i in range(N-M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pattern[j]:
                    break
  
            j+= 1
            # if p == t and pattern[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                # print("RP: Pattern found at index " + str(i))
                res.append(i)
  
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t - ord(txt[i])*(d**(M-1)) ) + ord(txt[i + M]))% q
  
            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q

    if res == []: print(f'RP: Pattern not found')
    return res