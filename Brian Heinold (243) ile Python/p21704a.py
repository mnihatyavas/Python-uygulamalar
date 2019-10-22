# coding:iso-8859-9 Türkçe

from tkinter import *
from tkinter.messagebox import *
kök = Tk()
kök.title ("Mesaj Kutuları")

def kapatılacak():
    cevap = askquestion (title='Kapatılsın mı?', message='Programı kapatmak istediğinden emin misin?')
    if cevap== 'yes': kök.destroy()

def göster (dönen):
    dönen = str (dönen).upper()
    etiket.config (text="Mesajdan dönen cevap: ["+dönen+"]'dir.")

etiket = Label (kök)
etiket.pack()

kök.protocol ('WM_DELETE_WINDOW', kapatılacak) # WM: PencereYönetimi, sil pencereyi...

mesaj1 = showinfo (title="Bilgi", message="Bu sadece bir enformasyon mesaj kutusudur!..")
göster (mesaj1)
mesaj2 = askquestion (title="SoruEH", message="Sorumuza cevabın Evet mi, Hayır mı?")
göster (mesaj2)
mesaj3 = showwarning (title="İkaz", message="Dikkat, bu biçimleme MS Windows tarafından desteklenmemektedir!..")
göster (mesaj3)

mesaj4 = askokcancel (title="SoruTİ", message="Sorumuza cevabın Tamam mı, İptal mi?")
göster (mesaj4)
mesaj5 = askretrycancel (title="SoruYİ", message="Sorumuza cevabın Yinele mi, İptal mi?")
göster (mesaj5)
mesaj6 = askyesnocancel (title="SoruEHİ", message="Sorumuza cevabın Evet mi, Hayır mı, İptal mi?")
göster (mesaj6)
mesaj7 = showerror (title="Hata", message="Dikkat, yaptığınız işlem hatalıdır!..")
göster (mesaj7)

mainloop()
