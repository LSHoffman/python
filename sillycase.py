def sillycase(string):
  mid = round((len(string) + 1) / 2)
  firstHalf = string[:mid].lower()
  secondHalf = string[mid:].upper()
  return firstHalf + secondHalf  

string = input("Please give me a silly word: ")

sillycase = sillycase(string)

print(sillycase)