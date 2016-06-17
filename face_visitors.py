#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lista pessoas mais ligadas a você no Facebook
#
# ins3ct, Maio 2016
#
# Nova versão
#


import urllib2, os, random, time, facebook

graph = facebook.GraphAPI('EAACEdEose0cBAFpyokHFV9wAsxDMYEdxb1RKf0tmwESVjA9qhRmIJZCueKI92F8YEjZC8Qs3Rp6VrQrwBm0BoqCUaQzvHESymoaa8Ko61Q7XsmpI2aBC1m3vefFDNm5oC0W1dsU92K1rxXJoGahxWnZAJCTfQbGbfPYzlDKVwZDZD')
 
qtd   = 1000
limit = 50
lists = '"list":['
 
def procurar():
       
        f = open("profile.htm", "r")
        text = f.readline()
       
        while 1:
                if text.find(lists) != -1:
                        return text
                else:
                        text = f.readline()
 
        return False
 
def filtrar(num):
        i = 0
        lista = []
        text = procurar()
        if text:       
                if len(text) <= 1:
                        print "Nada encontrado..."
                else:
                        profiles = text.split('"list":[')[1].split("]")[0].replace("-", "\n").replace(",", "\n").replace('"', "\n").split()
                        for x in profiles:
                                if i < num:
                                        if len(x) < 5:
                                                continue
                                        else:
                                                lista.append(x)
                                        i += 1
                                else:
                                        break
                        return lista
        else:
                print "O programa falhou."
                exit()
 
def profile():
        num = 1
        owned = []
        lista = filtrar(qtd)
        for x in lista:
                if num <= limit:
                        user = graph.get_object(id=x)
                        nome = user['name']
                        # nome = nome[0:6] + len(nome[6:]) * '*'
                        if nome not in owned:
                                print "%.2d" % num, "-", nome#, "\nPerfil: ", "http://www." + url.split("m.")[1], "\n"
                                owned.append(nome)
                                num += 1
                else:
                        break
        print "\nFIM DA LISTA.\n"
 
def wait(min):
        for x in range(min * 10):
                os.system("clear")
                load = "Carregando"
                print load, random.choice(["\\", "-", "/"]), "\n", str(random.randrange(1000)) + "%", "[" + "#" * x + "]"
                #print load[random.randrange(len(load)):] + load[:random.randrange(len(load))]
                time.sleep(0.05)
 
 
wait(2)
time.sleep(2)
os.system("reset")
print "Amigos que mais visitaram seu perfil:\n"
profile()
