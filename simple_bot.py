import re, random

print("\n*** Welcome to simple_bot. Enter 'q' to quit ***\n")
user_input_str = input("[SB] How are you doing?\n> ")

while (True):
    if user_input_str == 'q':
        print("\nGoodbye! :)\n")
        break

    if re.search(r'[nN]ot.*(?:[gG]ood|[gG]reat|[oO]k)|[sS]ad|[uU]nhappy|[tT]errible|[dD]epress|[dD]own', user_input_str):
        rand_response = random.randint(0, 1)
        if rand_response == 0:
            print("[SB] I am sorry to hear that :(")
        else:
            print("[SB] What makes you feel that way? :(")
    
    elif re.search(r'[nN]ot.*(?:[bB]ad|[sS]habby)|[gG]ood|[wW]ell|[gG]reat|[hH]appy|[aA]maz|[fF]antastic|[lL]ove|[eE]xcit|[bB]less|[oO]k|[cC]hill', user_input_str):
        print("[SB] I am glad to hear that you are doing well! :)")
    
    elif re.search(r'[hH](?:u|a)ngry|[sS]tarv|[fF]amished', user_input_str):
        if (re.search(r'(?:[iI] [aA]m)|(?:[iI]\'?m)', user_input_str)):
            match = re.search(r'(?:[iI] [aA]m|[iI]\'?m) (.*)', user_input_str)
            print("[SB] Hi,", match.group(1), end=", I'm SB! :D\n")
        print("[SB] Well, you better get something to eat! :D")

    elif re.search(r'[aA]ngry|[aA]nnoy|[aA]nxi|[uU]pset|[cC]oncern|[wW]orried|[fF]rustrat|[sS]car|[sS]trug', user_input_str):
        print("[SB] Then let's take some deep breaths!")
        print("_ _\t_ _\t_ _\t_ _\n -\t o\t -\t o")
    
    elif re.search(r'[sS]leep|[tT]ired', user_input_str):
        print("[SB] THEN YOU BETTER WAKE UP! :D")
    
    elif re.search(r'[bB]ad', user_input_str):
        print("[SB] Oh, what is making you feel that way? :(")
    
    elif re.search(r'[cC]onfus|[lL]ost|[dD]on\'?t [kK]now|[iI][dD][kK]|[bB]ored|[lL]onely|[eE]mpty', user_input_str):
        print("[SB] Well, my name is SB, and you can tell me more about how you're feeling! Enter 'q' to quit. :)")

    elif re.search(r'[aA]ll', user_input_str):
        print("[SB] In what way?")

    elif re.search(r'[aA]lways', user_input_str):
        print("[SB] Can you think of a specific example?")

    elif re.search(r'[bB]aa+', user_input_str):
        print("[SB] Baaaaa! :D")

    elif re.search(r'[tT]arnished', user_input_str):
        print("\n\tAH, ARISE! YE TARNISHED! YE DEAD, WHO LET LIVE!")
        print("\tAND CLAIM THE TITLE...OF ELDEN LORD!")

    else: 
        match = re.search(r'(.*)', user_input_str)
        print("[SB] What? ಠಿ_ಠ")
        print("[SB] What do you mean by", match.group(1), end="?\n")
    
    user_input_str = input("\n[SB] How are you doing?\n> ")