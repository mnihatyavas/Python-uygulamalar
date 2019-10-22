# coding:iso-8859-9 Türkçe
# p_21401.py: Anahtar-değer çiftli sözlük verilerinde anahtar hatası istisnası örneği.

ilçeler = {
    "Akdenizz": "Mersin",
    "Kuşadas": "Aydın",
    "İskendurun": "Hatay",
    "Yeşilyurd": "Malatya",
    "Alenya": "Antalya",
    "Alşancak": "İzmir",
    "Kizalay": "Ankara",
    "Üskütar": "İstanbul",
    "Çekirke": "Bursa",
    "Bandırna": "Balıkesir" }

try:
    print ("İlçelerin bağlı oldukları iller:")
    print (ilçeler ["Akdeniz"] )
    print (ilçeler ["Kuşadası"] )
    print (ilçeler ["İskenderun"] )
    print (ilçeler ["Yeşilyurt"] )
    print (ilçeler ["Alanya"] )
    print (ilçeler ["Alsancak"] )
    print (ilçeler ["Kızılay"] )
    print (ilçeler ["Üsküdar"] )
    print (ilçeler ["Çekirge"] )
    print (ilçeler ["Bandırma"] )
except Exception as ist: print ("[KeyError/AnahtarHatası]:", ist)



"""Çıktı:
>python p_21401.py
İlçelerin bağlı oldukları iller:
[KeyError/AnahtarHatası]: 'Akdeniz'
"""