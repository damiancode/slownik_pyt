import re
fp=open("polimorf2.tab","r",encoding="utf-8")




slownik={}
for line in fp:
    tmp=line.split("\t")
    slownik[tmp[0].lower()]=tmp[1].lower()+" "+tmp[2]

for klucz in slownik :
    if re.search("^absorbować .*(?!:neg)",slownik[klucz]) :
         print(klucz+"  "+slownik[klucz])

 
while True:
    search=input("podaj slowo: ").lower()

    try:
        print(slownik[search])
    except KeyError:
        print("slowo "+search+" nie istnieje w slowniku")
    

       
