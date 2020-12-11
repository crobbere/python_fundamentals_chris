import keyword
def contains_keyword(*argv):
    for arg in argv:
        if keyword.iskeyword(arg):
            return True
        else:
            return False

print(contains_keyword("while", "for", "lol"))