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

graph = facebook.GraphAPI('GET_YOUT_TOKEN_CODE')
 
qtd   = 1000
limit = 50
lists = 'list:["'
 
def procurar():
       
        f = open("profile.htm", "r")
        text = f.readlines()
        t = ''.join(text)       
        return t.split('groups:[],list:["')[1].split('],shortProfiles:')[0].split('","')


def filtrar(num):
        i = 0
        text = procurar()
        return text
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
                        try:
                                user = graph.get_object(id=x.split('-')[0])
                                nome = user['name']
                                # nome = nome[0:6] + len(nome[6:]) * '*'
                                if nome not in owned:
                                        print "%.2d" % num, "-", nome#, "\nPerfil: ", "http://www." + url.split("m.")[1], "\n"
                                        owned.append(nome)
                                        num += 1
                        except:
                                pass
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
