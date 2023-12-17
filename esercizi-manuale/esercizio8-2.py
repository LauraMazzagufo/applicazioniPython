prefissi = "JKLMNOPQ"
suffisso = "ack"

for lettera in prefissi:
    if (lettera != "O") and (lettera != "Q"):
        print(lettera + suffisso)
    else:
        aggiunta = "u"
        print(lettera + aggiunta + suffisso)


