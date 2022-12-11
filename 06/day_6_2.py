data = open("..\\inputs\\6.txt").read()

# Iterate over string in chunks of 4
chunk_size = 14
for idx in range(len(data)-chunk_size-1):
    chunk = data[idx:idx+chunk_size]
    # Check for unique characters
    if len(set(chunk)) == chunk_size:
        print(idx+chunk_size)
        break