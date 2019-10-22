# coding:iso-8859-9 Türkçe

from tkinter import *
from tkinter.messagebox import *
kök = Tk()
kök.title ("Mesaj Kutuları")

def kapatılacak():
    cevap = askquestion (title='Kapatılsın mı?', message='Programı kapatmak istediğinden emin misin?')
    if cevap== 'yes': kök.quit() # veya "kök.destroy()"
    else: göster (cevap)

def göster (dönen):
    dönen = str (dönen).upper()
    etiket.config (text="\n\nMesajdan dönen cevap: ["+dönen+"]'dir.")

def bilgi(): göster (showinfo (title="Bilgi", message="Bu sadece bir enformasyon mesaj kutusudur!..") )
def ikaz(): göster (showwarning (title="İkaz", message="Dikkat, bu biçimleme MS Windows tarafından desteklenmemektedir!..") )
def hata(): göster (showerror (title="Hata", message="Dikkat, yaptığınız işlem hatalıdır!..") )
def sorEH(): göster (askquestion (title="SoruEH", message="Sorumuza cevabın Evet mi, Hayır mı?") )
def sorEHİ(): göster (askyesnocancel (title="SoruEHİ", message="Sorumuza cevabın Evet mi, Hayır mı, İptal mi?") )
def sorTİ(): göster (askokcancel (title="SoruTİ", message="Sorumuza cevabın Tamam mı, İptal mi?") )
def sorYİ(): göster (askretrycancel (title="SoruYİ", message="Sorumuza cevabın Yinele mi, İptal mi?") )


if __name__ == "__main__":
    çerçeve = Frame (kök)
    çerçeve.pack()
    Button (çerçeve, text="Bilgi", command=bilgi ).pack (side=LEFT)
    Button (çerçeve, text="İkaz", command=ikaz ).pack (side=LEFT)
    Button (çerçeve, text="Hata", command=hata ).pack (side=LEFT)
    Button (çerçeve, text="Sor EH", command=sorEH ).pack (side=LEFT)
    Button (çerçeve, text="Sor EHİ", command=sorEHİ ).pack (side=LEFT)
    Button (çerçeve, text="Sor Tİ", command=sorTİ ).pack (side=LEFT)
    Button (çerçeve, text="Sor Yİ", command=sorYİ ).pack (side=LEFT)

    etiket = Label (kök)
    etiket.pack()

    kök.protocol ('WM_DELETE_WINDOW', kapatılacak) # WM: PencereYönetimi, sil pencereyi...

mainloop()
