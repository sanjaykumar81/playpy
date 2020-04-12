import re

def abbreviate(words:str):
    words = re.sub("[!@£$%^&*:,._-]", " ", words)
    words = words.title()

    acronym =""
    for word in words.split():
        acronym = acronym + word[0]

    return acronym

