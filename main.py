# Ejercicio 10: Clasificación de notas
# Escribe un programa que asigne una calificación basada en una nota numérica.
# Enunciado:
# Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).

note=int(input("Please enter your note : "))

if note>=90 and note<=100:
    print(" is note A")
elif note>=80 and note<=89:
    print("note is B")
elif note>=70 and note<=79:
    print("note is C")
elif note>=60 and note<=69:
    print("note is D")
elif note<60:
    print("note is F")