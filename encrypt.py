#encrypting
letters = 'abdcefghijklmnopqrstuvwxyz'
key = ("\U0001F600"), ("\U0001F50C"), ("\U0001F604"), ("\U0001F4B5"), ("\U0001F923 "), ("\U0001F973"), ("\U0001F609"), ("\U0001F970"), ("\U0001F60D"), ("\U0001F929"), ("\U0001F619"), ("\U0001F9B5"), ("\U0001F911"), ("\U0001F92D"), ("\U0001F60F"), ("\U0001F634"),("\U0001F92C"),("\U0001F47D"),("\U0001F922"),("\U0001F90E"),("\U0001F4A4"),("\U0001F92E"),("\U0001F44C"),("\U0001F595"),("\U0001F445"),("\U0001F507")
message = input("Enter your message:")
i = ''
ciphertext = ""
for ch in message:
    for i in range(len(letters)):
        if letters[i] == ch:
            ciphertext += key[i]
print(ciphertext)