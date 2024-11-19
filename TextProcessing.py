def NotEmpty(text):
    if str(text) == "" or str(text) == None or str(text) == " " or len(text) <= 1:
        return False
    else:
        return True
    