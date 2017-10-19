import re
fp=open("polimorf2.tab","r",encoding="utf-8")

tekst="Dyrektor Biura Edukacji miasta stołecznego Warszawy. Joanna Gospodarczyk zaznaczyła, że rok reformy edukacyjnej sprawia sporo niespodzianek, sporo nieprzewidzianych wydatków, sporo zaskoczeń, i kadrowych, i organizacyjnych"

a=re.split('[\s,.]+',tekst.lower())
print(a)

slownik={}
for line in fp:
    tmp=line.split("\t")
    slownik[tmp[0].lower()]=tmp[1].lower()

for slowo in a:
    print(slownik[slowo])


    





   
while True:
    search=input("podaj slowo: ").lower()

    try:
        print(slownik[search])
    except KeyError:
        print("slowo "+search+" nie istnieje w slowniku")
    

       
