"""Building a Markov Babbler."""
import random

def read_file(filename):
    with open(filename, "r") as file:
        contents = file.read().replace('\n\n',' ')
    return contents

def build_chain(text, chain = {}):
    if not text: text = "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible." + "The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
    
    words = text.split(" ")

    for i in range(1, len(words)): #start at index 1 since we're comparing *pairs* of words
        key = words[i - 1]
        word = words[i]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]

    return chain

def generate_message(chain, extra: bool, word_count=100):
    if not chain: return "no chain :("
    
    current_word = random.choice(list(chain.keys()))
    message = current_word.capitalize()
    
    #print(f"Initial message: {message}")
    
    while len(message.split(" ")) < word_count:
        #print(f"Message split: {message.split(' ')}")
        #print(f"Word count: {word_count}")
        #print(f"Type of len(message.split(' ')): {type(len(message.split(' ')))}")
        if current_word in chain:
            next_word = random.choice(chain[current_word])
            current_word = next_word # continues the chain
            message += ' ' + next_word # adding to word count
        else:
            if not extra:
                break
            else:
                current_word = random.choice(list(chain.keys()))
                message += ' ' + current_word.lower()
    
    return message


def input_message():
    print("Insert Text Below:")
    text: str = input()
    
    print("Building Chain")
    chain = build_chain(text=text)
    
    print("How long would you like the output to be?")
    count: int = int(input())
    if count == 0: count = 100
    extra = len(text.split(" ")) >= count
    if not extra:
        decision = input("It seems the input text is shorter than the output. Would you like the babbler to keep babbling? (Y/N) ")
        if decision not in ["Y", "N"]:
            decision = input("Invalid input. Would you like the babbler to keep babbling? (Y/N) ")
        extra = (decision == "Y")
    print(generate_message(chain, extra, count))
    
if __name__ == "__main__":
    input_message()