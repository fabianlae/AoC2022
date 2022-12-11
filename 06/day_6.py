data = open("..\\inputs\\6.txt").read()

# Iterate over string in chunks of 4
for idx in range(len(data)-3):
    chunk = data[idx:idx+4]
    # Check for unique characters
    if len(set(chunk)) == 4:
        print(idx+4)
        break