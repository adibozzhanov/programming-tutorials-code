import random
import math


# prints an attempt in a fancy way
def print_attempt(best_alph, current_alph, text):
    ret = ""
    for char in text:
        if best_alph.index(char) == current_alph.index(char):
            ret = ret + "\033[0;37;40m" + char
        else:
            ret = ret + "\033[1;31;40m" + char

    print("\n" * 100, ret, "\n" * 10, "\033[0;37;40m")


# removes all non-alpha characters
def clean_text(text):
    ret = ""
    alph = {chr(i + 65) for i in range(26)}
    new_text = text.upper()
    for char in new_text:
        if char in alph:
            ret = ret + char
    return ret


# reads the quadgrams file and returns a dictionary
def init_quadgrams():
    quadgrams = {}

    with open("english_quadgrams.txt", "r") as f:
        content = f.readlines()
        for line in content:
            quad, freq = line.strip().split()
            quadgrams[quad] = int(freq)

    return quadgrams


# quad-gram fitness
def fitness_quad(text, quadgrams):
    fit = 0
    for i in range(len(text) - 3):
        substr = text[i:i + 4]
        if substr in quadgrams:
            fit += math.log(quadgrams[substr])
    return fit


# swap 2 random letters in the alphabet
def mutate(alphabet):
    pos1 = random.randint(0, 25)
    pos2 = random.randint(0, 25)
    alphabet[pos1], alphabet[pos2] = alphabet[pos2], alphabet[pos1]


# hill climbing
# depth - number of times you need to attempt improving last best attempt
def mono_decrypt(text, depth):

    quadgrams = init_quadgrams()
    c_text = clean_text(text)
    best_alph = random_alphabet()
    best_fit = fitness_quad(mono_encrypt(best_alph, c_text), quadgrams)

    count = 0
    while count < depth:
        attempt = best_alph.copy()
        mutate(attempt)
        encryption = mono_encrypt(attempt, c_text)
        fit = fitness_quad(encryption, quadgrams)

        if (count % 20 == 0):
            print_attempt(best_alph, attempt, encryption)

        if fit > best_fit:
            best_alph = attempt
            best_fit = fit
            count = 0
        else:
            count += 1

    return mono_encrypt(best_alph, text)


# initialises an array of random letter permutation
def random_alphabet():
    choices = [chr(i + 65) for i in range(26)]
    random.shuffle(choices)
    return choices


# encrypts the text using a given alphabet
# alphabet - array of all letters
def mono_encrypt(alphabet, text):
    # maps [A,B,C,D,E,...] to [Z,F,A,E,...] (a given alphabet)
    mapping = {}
    cipher_text = ""
    t = text.upper()

    for i, char in enumerate(alphabet):
        mapping[chr(i + 65)] = char

    for char in t:
        if char in mapping:
            cipher_text = cipher_text + mapping[char]
        else:
            cipher_text = cipher_text + char

    return cipher_text


if __name__ == "__main__":
    text = """
Career and research

While at the International Computer Science Institute (ICSI), Handley co-founded the AT&T Center for Internet Research, as well as the XORP open-source router project (2000).[7]

Handley is a contributor to Internet Engineering Task Force (IETF) standards and a member of the IETF Routing Area Directorate and the Transport Area Directorate.[8] Previously he was a member of the Internet Architecture Board (IAB)[9] and chaired the IETF Multiparty Multimedia Session Control working group[10] and the IRTF Reliable Multicast Research Group.[11] He is the author or co-author of 34 Request for Comments (RFCs), including the Session Initiation Protocol,[12] Multipath TCP[13] and a series of other network protocols.
Awards and honours

Handley was awarded a Royal Society Wolfson Research Merit Award in 2003, and received the 2007 Roger Needham Award.[14][15] He was the recipient of the 2012 IEEE Internet Award[16] "For contributions to Internet multicast, telephony, congestion control and the shaping of open Internet standards and open-source systems in all these areas.", and the 2019 SIGCOMM Award "For fundamental contributions to Internet multimedia, multicast, congestion control and multi-path networks, and the standardization of Internet protocols in these domains".

Handley was elected Fellow of the Royal Society (FRS) in 2019 for substantial contributions to the improvement of natural knowledge.[17]  
    """
    alph = random_alphabet()

    cipher_text = mono_encrypt(alph, text)

    print(cipher_text)
    input("Start?")

    print(mono_decrypt(cipher_text, 10000))
