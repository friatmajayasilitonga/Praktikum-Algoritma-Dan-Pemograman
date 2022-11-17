#input user
#data yang dimasukkan pasti string
from xmlrpc.client import boolean


data=input("masukkan data:")
print("data=",data,"type=",type(data))
#jika kita ingin mengambil int,maka
angka1=float(input("masukkan angka:"))
angka=int(input("masukkan angka:"))
print("data=",angka,",type=",type(angka))
print("data=",angka1,",type=",type(angka1))

#bagaimana dengan boolean

biner=bool(int(input("masukkan nilai bolean:")))
print("data=",biner,",type=",type(biner))