"""
This library has some utils function to manipulate and analyse texts.
"""
def character_count(text):
    """
    This function takes a text (string) as input and returns the number of character in it
    """
    return len(text)

# Usage exemple
print(character_count("Inazuma Eleven"))

def word_count(text):
    """
    This function takes a text (String) as input and returns the number of words in it
    """
    if text == "" or text ==" ": return 0
    count = 1
    for elm in text:
        if elm == " ":
            count+=1
    if text[-1]==" ":
        count = count -1
    return count

# Usage exemple
print(word_count("Inazuma Eleven"))
print(word_count("Hello there "))

def reverse(text):
    """
    This function takes a text (string) as input and makes it backwards.
    """
    L=[]
    for elm in text:
        L.append(elm)
    N = L[::-1]
    new_text = ""
    for elm in N:
        new_text = new_text + elm
    return new_text

# Usage exemple
print(reverse("hello there"))

def capitalize_words(text):
    """
    This function takes a text (string) as input and capitalize all letters in it
    """
    return text.upper()

# Usage exemple
print(capitalize_words("inazuma"))


