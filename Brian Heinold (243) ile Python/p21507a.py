# coding:iso-8859-9 Türkçe
# 2 oyunculu (3x3) matrisli Kazı_Kazan uyunu

from tkinter import *
Tk()

def Kazı_Kazan (r,c):
    global oyuncu

    if oyuncu == 'X' and durum[r][c] == 0 and oyun_bitti==False:
        pano[r][c].configure (text='X', fg='blue', bg='white')
        durum[r][c] = 'X'
        kazanmaKontrolu()
        oyuncu = 'O'
    elif oyuncu == 'O' and durum[r][c] == 0 and oyun_bitti==False:
        pano[r][c].configure (text='O', fg='orange', bg='black')
        durum[r][c] = 'O'
        kazanmaKontrolu()
        oyuncu = 'X'

def kazanmaKontrolu():
    global oyun_bitti

    for i in range (3):
        if durum[i][0]==durum[i][1]==durum[i][2]!=0:
            pano[i][0].configure (bg='grey')
            pano[i][1].configure (bg='grey')
            pano[i][2].configure (bg='grey')
            oyun_bitti = True

    for i in range (3):
        if durum[0][i]==durum[1][i]==durum[2][i]!=0:
            pano[0][i].configure (bg='grey')
            pano[1][i].configure (bg='grey')
            pano[2][i].configure (bg='grey')
            oyun_bitti = True

    if durum[0][0]==durum[1][1]==durum[2][2]!=0:
        pano[0][0].configure (bg='grey')
        pano[1][1].configure (bg='grey')
        pano[2][2].configure (bg='grey')
        oyun_bitti = True

    if durum[2][0]==durum[1][1]==durum[0][2]!=0:
        pano[2][0].configure (bg='grey')
        pano[1][1].configure (bg='grey')
        pano[0][2].configure (bg='grey')
        oyun_bitti = True

    if oyun_bitti==True:
        sonuç = Label (font= ("times new roman", 25, "italic bold"),
            fg="#f4e", text="Kazanan oyuncu: {}".format (oyuncu) )
        sonuç.grid (row=3, column=0, columnspan=3, pady=5)


pano = [[0,0,0],
    [0,0,0],
    [0,0,0]]

durum = [[0,0,0],
    [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        pano[i][j] = Button (font=('Verdana', 56), width=3, bg='yellow',
            command = lambda satır=i,sütun=j: Kazı_Kazan (satır,sütun))
        pano[i][j].grid (row = i, column = j)

oyuncu = 'X'
oyun_bitti = False

mainloop()
