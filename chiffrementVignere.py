def chiffrementVignere(msg, cle):
    k = 0
    msg_chiffre = ""
    for char in msg:
        rang_char = lettre.index(char)
        rang_cle = lettre.index(cle[k % len(cle)])
        k = k + 1
        msg_chiffre = msg_chiffre + TableVignere[rang_cle][rang_char]
    return msg_chiffre

def dechiffrementVignere(msg_chiffre, cle):
    k = 0
    msg_clair = ""
    for char in msg_chiffre:
        rang_cle = lettre.index(cle[k % len(cle)])
        msg_clair = msg_clair + lettre[TableVignere[rang_cle].index(char)]
        k = k + 1

    return msg_clair



lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

TableVignere = [[ 0 for j in range(26)] for i in range(26) ]

for i in range(26):
    k = i
    for j in range(26):
        TableVignere[i][j] = lettre[k % 26]
        k = k + 1
"""
for i in range(26):
    print(TableVignere[i])
"""
"""
TableVignere = [[ 0 for j in range(4)] for i in range(4) ]

for i in range(4):
    k = i
    for j in range(4):
        TableVignere[i][j] = lettre[k % 4]
        k = k + 1
for i in range(4):
    print(TableVignere[i])
"""

msg = input("saisir le message claire: ")
cle = input("saisir la cle: ")
msg_chiffre = chiffrementVignere(msg, cle)

print("le message claire: ", msg)
print("le message chiffre est: ",msg_chiffre)
print("le message déchiffre est: ",dechiffrementVignere(msg_chiffre, cle))