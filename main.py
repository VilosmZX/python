import os
import requests
import json

class main:

    def __init__(self, name, pw):
        self.name = name
        self.pw = pw

    def login(self):
        name = input("Masukan nama: ").upper()
        pw = input("Masukan pw: ").lower()
        print(name)
        if(name == self.name and pw == self.pw):
            print("Login Sucess")
        else:
            print("Login gagal")

a = main("username", "password")
a.login()

