
def character_count(text):
    return len(text)

print(character_count("Inazuma Eleven"))

def word_count(text):
    if text == "" or text ==" ": return 0
    count = 1
    for elm in text:
        if elm == " ":
            count+=1
    return count

print(word_count("Inazuma Eleven"))

