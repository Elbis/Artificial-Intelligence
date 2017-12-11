Matrix = [["Yakisikli","Zengin","Odun","Zeki","EVET"],
          ["Yakisikli","Zengin","Romantik","Salak","EVET"],
          ["Yakisikli","Zengin","Romantik","Zeki","EVET"],
          ["Çirkin","Fakir","Romantik","Zeki","HAYIR"],
          ["Yakisikli","Zengin","Odun","Aptal","EVET"]] // Listeyi istediğiniz gibi düzenleyebilirsiniz.
Olumlu=[]
Olumsuz=[]
for i in range(len(Matrix)):
    if (Matrix[i][-1])=="EVET": Olumlu.append(Matrix[i][:-1]) // Son girdisinde "EVET" alanları olumluya, almayanları olumsuz 
    else: Olumsuz.append(Matrix[i][:-1])                      // listesine atıyoruz.

h=Olumlu[0]                                               // ilk olumlu elemanımızı referans alarak find-s algoritmasını başlatıyoruz.

for a in range(len(Olumlu)):
    for b in range(len(Olumlu[a])):
        if Olumlu[a][b]==h[b]:
            print("Hipotezdeki {} elemanıyla, {} . satırda ele alınan {} verisi hala aynı!".format(h[b],a,Olumlu[a][b]))
        else: h[b]="?"

print("Evleneceğin kişi : ---- {} ---- olsa yeter, soru işaretlerine takılma ;) ".format(h))

