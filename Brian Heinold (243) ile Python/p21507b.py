# coding:iso-8859-9 Türkçe
# 3 oyunculu (6x6) matrisli Kazı_Kazan oyunu

from tkinter import *
Tk()

def Kazı_Kazan (i, j):
    global oyuncu

    if oyuncu == 'A' and durum[i][j] == 0 and oyun_bitti==False:
        pano[i][j].configure (text='A', fg='blue', bg='pink')
        durum[i][j] = 'A'
        kazanmaKontrolu()
        oyuncu = 'B'
    elif oyuncu == 'B' and durum[i][j] == 0 and oyun_bitti==False:
        pano[i][j].configure (text='B', fg='orange', bg='black')
        durum[i][j] = 'B'
        kazanmaKontrolu()
        oyuncu = 'C'
    elif oyuncu == 'C' and durum[i][j] == 0 and oyun_bitti==False:
        pano[i][j].configure (text='C', fg='cyan', bg='green')
        durum[i][j] = 'C'
        kazanmaKontrolu()
        oyuncu = 'A'

def kazanmaKontrolu():
    global oyun_bitti

    for i in range (uz):
        if durum[i][0]==durum[i][1]==durum[i][2]==durum[i][3]==durum[i][4]==durum[i][5] != 0:
            pano[i][0].configure (bg='grey')
            pano[i][1].configure (bg='grey')
            pano[i][2].configure (bg='grey')
            pano[i][3].configure (bg='grey')
            pano[i][4].configure (bg='grey')
            pano[i][5].configure (bg='grey')
            oyun_bitti = True

    for i in range (uz):
        if durum[0][i]==durum[1][i]==durum[2][i]==durum[3][i]==durum[4][i]==durum[5][i] != 0:
            pano[0][i].configure (bg='grey')
            pano[1][i].configure (bg='grey')
            pano[2][i].configure (bg='grey')
            pano[3][i].configure (bg='grey')
            pano[4][i].configure (bg='grey')
            pano[5][i].configure (bg='grey')
            oyun_bitti = True

    if durum[0][0]==durum[1][1]==durum[2][2]==durum[3][3]==durum[4][4]==durum[5][5] != 0:
        pano[0][0].configure (bg='grey')
        pano[1][1].configure (bg='grey')
        pano[2][2].configure (bg='grey')
        pano[3][3].configure (bg='grey')
        pano[4][4].configure (bg='grey')
        pano[5][5].configure (bg='grey')
        oyun_bitti = True

    if durum[2][0]==durum[1][1]==durum[0][2]==durum[0][3]==durum[0][4]==durum[0][5] != 0:
        pano[5][0].configure (bg='grey')
        pano[4][1].configure (bg='grey')
        pano[3][2].configure (bg='grey')
        pano[2][3].configure (bg='grey')
        pano[1][4].configure (bg='grey')
        pano[0][5].configure (bg='grey')
        oyun_bitti = True

    if oyun_bitti==True:
        sonuç = Label (font= ("times new roman", 25, "italic bold"),
            fg="maroon", text="Kazanan oyuncu: {}".format (oyuncu) )
        sonuç.grid (row=6, column=0, columnspan=6, pady=5)


pano = [[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

durum = [[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

uz = len (pano)
for i in range (uz):
    for j in range (uz):
        pano[i][j] = Button (font=('Verdana', 20), width=3, bg='yellow',
            command = lambda satır=i,sütun=j: Kazı_Kazan (satır, sütun))
        pano[i][j].grid (row = i, column = j)

oyuncu = 'A'
oyun_bitti = False

mainloop()
