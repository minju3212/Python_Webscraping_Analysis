text = "Python is awesome"
vowels = "aeiou"
count = 0
for v in text:
    if v.lower() in vowels:
        count += 1
        
print(f"모음 개수 : {count}")