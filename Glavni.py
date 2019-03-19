def unos_za_ponedeljak():
    print("Unesite raspored za ponedeljak:")
    radi=True;
    ponedeljak_lista=[]
    while radi:
        predmet = input("Unesite ime predmeta: ")
        vreme = input ("Unesite vreme predmeta (u formatu hh:mm - hh:mm): ")
        ponedeljak_lista.append(predmet)
        ponedeljak_lista.append(vreme)

        odgovor=input("Da li zelite da unesete jos jedan predmet? (Odgovoriti sa Da/Ne)")
        if odgovor == 'Da':
            radi=True
        else:
            radi=False

    return ponedeljak_lista

lista_ponedeljak=unos_za_ponedeljak()

print("Ponedeljak:")
i=len(lista_ponedeljak)
j=0

while j<i:
    print(lista_ponedeljak[j] + " " + lista_ponedeljak[j+1])
    j+=2


print("Provera")