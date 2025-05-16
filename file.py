file = input("flie.txt: ")

try:
    file = open(file.txt, 'r')
    content = file.read()
    print(content)


except fileNotFoundError: 
    print("File was not found")   