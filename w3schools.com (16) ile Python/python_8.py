# coding:iso-8859-9 "Türkçe"

import mysql.connector

# Eğer bu program hata vermezse "mysql.connector" modülü kurulmuş demektir...

veriTabanım = mysql.connector.connect (
    host="localhost",
    user="myusername",
    passwd="mypassword"
)

print (veriTabanım)
