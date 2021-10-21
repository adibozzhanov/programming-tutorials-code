import random
import math

# alphabet - array of characters in a random order
# text - text to encrypt


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
    return fit / (len(text) - 3)


def mutate(alphabet):
    pos1 = random.randint(0, 25)
    pos2 = random.randint(0, 25)
    alphabet[pos1], alphabet[pos2] = alphabet[pos2], alphabet[pos1]


def mono_decrypt(text, num_gen):

    quadgrams = init_quadgrams()
    c_text = clean_text(text)
    best_alph = random_alphabet()
    best_fit = 0

    count = 0
    while count < num_gen:
        attempt = best_alph.copy()
        mutate(attempt)
        encryption = mono_encrypt(attempt, c_text)
        fit = fitness_quad(encryption, quadgrams)
        if fit > best_fit:
            best_alph = attempt
            best_fit = fit
            count = 0
            print("\n" * 100, encryption)
        else:
            count += 1

    return mono_encrypt(best_alph, text)


def random_alphabet():
    choices = [chr(i + 65) for i in range(26)]
    random.shuffle(choices)
    return choices


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
Psychologists believe that over-explaining is a trauma response. You’ve probably heard of the fight, flight or freeze responses to trauma, but one lesser known response is fawn. Fawn refers to people pleasing and over-explaining. You are trying to diffuse conflict and make yourself less than, to present yourself as a ‘non-threat’.

How many times have you sent a long text explaining your reasons for saying no? Or your reasons for saying yes? Or your reasons for feeling a certain way? Brevity in texting is a power move. You don’t need to over-explain the way you feel or the reasons for saying yes or no. When you overcome your trauma response, you are able to live by your values. When you are value-driven and self-assured, you don’t feel the need to explain away every act or decision.

When you over-explain in a long text, you are also opening yourself up to subconscious interpretation. You are presenting yourself as a ‘non-threat’ which unfortunately can make you look weak, needy or desperate. While these things aren’t inherently bad, they can deeply affect your self-esteem and worthiness in a relationship (social or intimate).

That doesn’t mean that you should never express how you feel, but a text isn’t the right platform for it. Opt to meet in person to have a free flowing conversation — like you are playing a game of tennis. Sending a long text is like serving 100 tennis balls into someone’s court and expecting them to still want to play.

Instead of the texting essay, go for “can we meet for coffee later?”. It makes you come across as assured and confident. Plus, when you do make your point, it will be better received. 
    """
    alph = random_alphabet()

    cipher_text = mono_encrypt(alph, text)

    print(cipher_text)
    input("Start?")

    print(mono_decrypt(cipher_text, 10000))
