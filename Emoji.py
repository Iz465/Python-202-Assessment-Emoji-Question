sport_Emojis = {
  "Soccer":"⚽",
  "Cricket":"🏏",
  "Rugby":"🏉",
  "Golf":"⛳",
  "Volleyball": "🏐",
  "Hockey": "🏑",
  "Squash":"🎾",
  "Bowling":"🎳",
  "Table-tennis": "🏓",
  "Handball": "🥎",
  "Basketball": "🏀",
  "Boxing": "🥊"
}


while True: 
  emoji = input("Enter five emojis: ")
  words = emoji.split(',') # A comma lets the code know its separating two words each time a comma occurs. These words are added to the words list.
  convert = "" # This will store the converted emojis 
  word_Count = 0
  repeat_count = 0
  duplicate_Words = [] # Made another list to hold words that arent in it so it can check for duplicate words. 
  for word in words:
    convert += sport_Emojis.get(word,"🤔") + " " # Adds the emoji from the dictionary to the convert. if that emoji key is not there then it will be replaced with the confusion emoji.
    word_Count += 1
    if word not in duplicate_Words:
      duplicate_Words.append(word)
    else: 
      repeat_count += 1
  if word_Count < 5:
    print("Error. Number of keywords is less than 5. Re-enter keywords")   
  elif word_Count > 5:
    print("Error. Number of keywords is more than 5. Re-enter keywords")   
  elif repeat_count > 0:
    print("Error. Repeating words. Re-enter keywords")
  else:
    break # Stops the loop as users have followed the rules correctly.

print(convert)
      
    




