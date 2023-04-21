with open("text.txt", "r") as f:
    text = f.readlines()

unique_text = list(set(text))

with open("nodupes.txt", "w") as f:
    f.writelines(unique_text)

### If you actually needed this tool from my github u must be either high or a frog, it is literally 5 lines.......