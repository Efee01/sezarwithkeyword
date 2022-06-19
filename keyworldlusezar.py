import string#string kütüphanesini aktif ettim
alfabe = list(string.ascii_lowercase)#asciideki bütün küçük harfleri string halinde listeledim

mesaj = input("şifrelemek istediğiniz metni giriniz: ")#şifrelemek istenilen cümleyi kullanıcıdan alıyoruz

msj = []# kullanıcının yazdığı mesajı listeye dönüştürmesi için boş bir dizi oluşturdum
for i in mesaj:#for döngüsü oluşturdum kullanıcının verdiği cümleyi msjnin içine atsın diye
	msj.append(i.lower())#append komutuyla ekledim

anahtarkelime = input("Anahtar Kelimeyi giriniz: ")
anahtarkelime1 = anahtarkelime.lower()#anahtar kelimeyi küçük harfe çevirdim

def anhtrfnk(listee):#define fonk oluşturdum
	anahtar = []
	for i in listee:
		if i not in anahtar:
			anahtar.append(i)

	return anahtar

anahtarkelime1 = anhtrfnk(anahtarkelime1)#fonksiyonu anahtarkelimeyle bağladım

encrypting = anhtrfnk(anahtarkelime1+alfabe)# burada şifreleme işlemini gerçekleştiriyoruz

for i in encrypting:
	if(i == ' '):
		encrypting.remove(' ')#boşlukları for dönügüsü oluşturup sildim

sifrelimetin = ""

for i in range(len(msj)):#şifrelenmiş mesaj için keywordu ve alfabeyi saklayan bir for döngüsü oluşturdum
	if(msj[i]!= ' '):
		sifrelimetin = sifrelimetin+encrypting[alfabe.index(msj[i])]
	else:
		sifrelimetin = sifrelimetin+' '

print("Şifrelenmek istenilen mesaj : ", mesaj)
print("anahtar kelime : ", anahtarkelime)
print("Mesajın Şifrelenmiş Hali : ", sifrelimetin)

