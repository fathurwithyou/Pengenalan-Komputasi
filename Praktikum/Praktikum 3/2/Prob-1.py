kil = input("Masukkan kata Tuan Kil: ")
leo = input("Masukkan kata Tuan Leo: ")

if len(kil) != len(leo):
    print("Kunci yang dicatat Tuan Leo tidak sama dengan kunci Tuan Kil.")
else:
    j = len(kil) - 1
    sama = True
    for i in range(len(kil)):
        if kil[i] != leo[j]:
            sama = False
            i = len(kil)
        j -= 1
    if sama:
        print("Kunci yang dicatat Tuan Leo sama dengan kunci Tuan Kil.")
    else:
        print("Kunci yang dicatat Tuan Leo tidak sama dengan kunci Tuan Kil.")

'''
Kunci
icnuK

puhsepuh
hupespuh

stressed
desserts
'''
