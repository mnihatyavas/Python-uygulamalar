# coding:iso-8859-9 Türkçe
# p_41203.py: Tkinter serilim yönetiminde grid kullanımı örneği.

from tkinter import *
from p_315 import Renk
    
kök = Tk()
kök.title ("grid()'le Renklerin Serilimi")

renkler1 = ['Aqua', 'Black', 'Blue', 'Fuchsia', 'Green', 'Gray', "Lime", "Maroon", "Navy", "Olive", "Purple", "Red", "Silver", "Teal", "White", "Yellow",
    "AliceBlue", "AntiqueWhite", "AquaMarine", "Azure", "Beige", "Bisque", "BlancheDalmond", "BlueViolet", "Brown", "BurlyWood", "CadetBlue",
    "Chartreuse", "Chocolate", "Coral", "CornFlowerBlue", "CornSilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray",
    "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen",
    "DarkSlateBlue", "DarkSlateGray", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "FireBrick",
    "FloralWhite", "ForestGreen", "GainsBoro", "GhostWhite", "Gold", "GoldenRod", "Gray", "GreenYellow", "HoneyDew", "HotPink", "IndianRed",
    "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan",
    "LightGoldenRodYellow", "LightGreen", "LightGrey", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray",
    "LightSteelBlue", "LightYellow", "LimeGreen", "Linen", "Magenta", "MediumBlue", "MediumOrchid", "MediumPurple", "MidnightBlue",
    "MistyRose", "Moccasin", "OldLace", "Orange", "Orchid", "PeachPuff", "Peru", "Pink", "Plum", "Purple", "RosyBrown", "RoyalBlue",
    "Salmon", "SandyBrown", "SeaGreen", "Sienna", "SkyBlue", "SlateBlue", "Tan", "Thistle", "Tomato", "Violet", "Wheat", "WhiteSmoke", "YellowGreen", "black", "black"]

renkler2 = ['#00ffff', '#000000', '#0000ff', '#ff00ff', '#008000', '#808080', "#00ff00", "#800000", "#000080", "#808000", "#800080", "#ff0000", "#c0c0c0", "#008080", "#ffffff", "#ffff00",
    "#f0f8ff", "#faebd7", "#7fffd4", "#f0ffff", "#f5f5dc", "#ffe4c4", "#ffebcd", "#8a2be2", "#a52a2a", "#deb887", "#5f9ea0",
    "#7fff00", "#d2691e", "#ff7f50", "#6495ed", "#fff8dc", "#dc143c", "#00ffff", "#00008b", "#008b8b", "#b8860b", "#a9a9a9",
    "#006400", "#bdb76b", "#8b008b", "#556b2f", "#ff8c00", "#9932cc", "#8b0000", "#e9967a", "#8fbc8f",
    "#483d8b", "#2f4f4f", "#00ced1", "#9400d3", "#ff1493", "#00bfff", "#696969", "#1e90ff", "#b22222",
    "#fffaf0", "#228b22", "#dcdcdc", "#f8f8ff", "#ffd700", "#daa520", "#808080", "#adff2f", "#f0fff0", "#ff69b4", "#cd5c5c",
    "#4b0082", "#fffff0", "#f0e68c", "#e6e6fa", "#fff0f5", "#7cfc00", "#fffacd", "#add8e6", "#f08080", "#e0ffff",
    "#fafad2", "#90ee90", "#d3d3d3", "#ffb6c1", "#ffa07a", "#20b2aa", "#87cefa", "#778899",
    "#b0c4de", "#ffffe0", "#32cd32", "#faf0e6", "#ff00ff", "#0000cd", "#ba55d3", "#9370db", "#191970",
    "#ffe4e1", "#ffe4b5", "#fdf5e6", "#ffa500", "#da70d6", "#ffdab9", "#cd853f", "#ffc0cb", "#dda0dd", "#800080", "#bc8f8f", "#4169e1",
    "#fa8072", "#f4a460", "#2e8b57", "#a0522d", "#87ceeb", "#6a5acd", "#d2b48c", "#d8bfd8", "#ff6347", "#ee82ee", "#f5deb3", "#f5f5f5", "#9acd32", "#000", "#000"]

kabartılar = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]

satır = 0
uz = len (renkler1) - 5
print (uz, len(renkler2))
for i in range (0, uz, 5):
    for j in range (5): Label (kök, text=(renkler1 [i+j] + ": " + renkler2 [i+j]), bg=renkler1 [i+j], relief=kabartılar [j], bd=5, width=25).grid (row=satır, column=j)
    satır +=1          

kök.mainloop()
