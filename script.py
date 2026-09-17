
def character_count(text):
    return len(text)

print(character_count("Inazuma Eleven"))

def word_count(text):
    if text == "" or text ==" ": return 0
    count = 1
    for elm in text:
        if elm == " ":
            count+=1
    if text[-1]==" ":
        count = count -1
    return count

print(word_count("Inazuma Eleven"))
print(word_count("Hello there "))

def reverse(text):
    L=[]
    for elm in text:
        L.append(elm)
    N = L[::-1]
    new_text = ""
    for elm in N:
        new_text = new_text + elm
    return new_text

print(reverse("hello there"))

def capitalize_words(text):
    return text.upper()

print(capitalize_words("inazuma"))


