elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
# Fiecare elev are o notă pe aceeași poziție.




# Partea A – Afișare și prelucrare (35p)

# A1. Listează elevii cu notele lor – 10p
# Folosește for și indici: afișează „Ana are nota 9” etc.
for i in range(len(elevi)):
	print(f"{elevi[i]} are nota {note[i]}")
	

# A2. Nota maximă și minimă – 10p
# Determină și afișează valorile maxime/minime din note și numele elevilor corespunzători.
mxv = mnv = note[0]
mxp = mnp = 0

for i in range(len(note)):
    if note[i] > mxv:
        mxv = note[i]
        mxp = i
    if note[i] < mnv:
        mnv = note[i]
        mnp = i


print(elevi[mxp], ": ", mxv)
print(elevi[mnp], ": ", mnv)


# A3. Media clasei – 10p
# Calculează media aritmetică a notelor. Afișează cu două zecimale.
#media aritmetica : Ma = (a+b)/2
suma = 0
for i in range(len(note)):
     suma += note[i]
media = suma / len(note)
print(f"Media aritmetica: {media:.2f}")


# A4. Promovați – 5p
# Afișează numele elevilor cu notă ≥ 5 (folosește if în interiorul unui for).
for i in range(len(note)):
     #print(nota)
     if note[i] > 5:
        print(elevi[i], ":", note[i])



# Partea B – Actualizări (35p)

# B5. +1 punct fiecărei note (max 10) – 10p
# Parcurge note cu for pe indici și crește fiecare notă cu 1.
for i in range(len(note)):
     note[i] += 1
     print(note[i])


# B6. Adaugă elevul predefinit – 10p
# Adaugă elev_nou și nota_elev_nou la finalul listelor (append) și afișează listele actualizate. 
elevi.append(elev_nou)
print(elevi)

note.append(nota_elev_nou)
print(note)

# B7. Șterge elevul predefinit – 10p
# Găsește poziția lui elev_de_sters în elevi (dacă există) și elimină-l pe el și nota corespunzătoare.
print(elevi.index(elev_de_sters))
pozitie = elevi.index(elev_de_sters)
elevi.pop(pozitie)
note.pop(pozitie)
print(elevi)
print(note)
print(f"Elevul {elev_de_sters} a fost sters")

# B8. Afișează din nou lista – 5p
# Listează perechile elev–notă după actualizări.
for i in range(len(elevi)):
     print(elevi[i], ":", note[i])



# Partea C – Căutări și statistici fără input (30p)

# C9. Căutări de nume cu while – 12p
# Folosește while pentru a procesa elementele din interogari_nume în ordine. 
# Oprește-te când elementul curent este "stop". 
# Pentru fiecare nume (altul decât "stop"), dacă se găsește în elevi, afișează nota; altfel, afișează un mesaj că nu există.
i = 0
while i < len(interogari_nume) and interogari_nume[i] != "stop":
    nume = interogari_nume[i]
    if nume in elevi:
        pozitie = elevi.index(nume)
        print(f"{nume} are nota {note[pozitie]}")
    else:
        print(f"{nume} nu exista in lista elevilor.")
    i += 1

# C10. Număr promovați / respinși – 8p
# Numără câți au notă ≥ 5 și câți au < 5 și afișează rezultatul.
promovati = 0
respinsi = 0
for n in note:
    if n >= 5:
        promovati += 1
    else:
        respinsi += 1
print(f"Promovati: ", promovati, "\nRespinsi: ", respinsi)


# C11. Media promovaților – 10p
# Construiește o listă cu notele ≥ 5 și calculează media acesteia (tratare corectă a cazului listei goale).
note_promovati = [n for n in note if n >= 5]
print(note_promovati)
media_promovati = sum(note_promovati) / len(note_promovati)
print(f"Media promovatilor este {media_promovati:.2f}")