# coding:iso-8859-9 "T�rk�e"

import mysql.connector

# E�er bu program hata vermezse "mysql.connector" mod�l� kurulmu� demektir...

veriTaban�m = mysql.connector.connect (
    host="localhost",
    user="myusername",
    passwd="mypassword"
)

print (veriTaban�m)
