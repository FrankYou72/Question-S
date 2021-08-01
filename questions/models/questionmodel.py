from django.db import models
from django.db.models import manager,CASCADE, ForeignKey, JSONField
from django.db.models.fields import CharField, TextField, DateTimeField
from ..utils.Question_S.questionS import get_vars, opes
from sympy.solvers import solve
from random import randint, choice
from .area import Area
from rest_framework import serializers
from math import sqrt, sin, cos, tan, asin, atan, acos, pi

class QuestionModel(models.Model):
    area = ForeignKey(Area, on_delete=CASCADE,default = '', blank=True , null=True)
    tema = CharField(max_length=200)
    equacao = CharField(max_length=200, blank=True)
    enunciado = TextField(blank=True, null=True)
    variaveis = JSONField(blank=True, null=True)
    grandezas = JSONField(blank=True, null=True)
    unidades = JSONField(blank=True, null=True)
    equacoes = JSONField(blank=True, null=True)
    objects = manager.Manager()
    
    def __str__(self):
        return self.area.area + ' - ' + self.tema

    def get_question(self):

        global opes
        dados = self.variaveis
        print('dados ao iniciar: ', dados)
        print('self.variaveis: ', self.variaveis)
        print('Tipo de self.variaveis: ', type(self.variaveis))
        escolha = str(choice(self.equacoes))
        escolha_copia = escolha
        print('Escolha: ', escolha)
        
        for o in opes:
            if o in str(escolha_copia):
                escolha = escolha.replace(o, f' {o} ')
        escolha_com_opes = escolha
        print('Escolha após separação: ', escolha)

        for o in opes:
            if o in str(escolha_copia):
                escolha = escolha.replace(o, ' ')
        print('Escolha sem opes: ', escolha)

        sf = self.variaveis
        es = escolha.split()
        print('Dados: ', dados)
        print('Escolha split: ', es)
        for v in sf:
            ('Agora vamos comparar ', v, 'com ', es)
            if v not in es:
                icognita = v
                dados.remove(icognita)
        print('Dados sem icognita: ', dados)
        
        escolha = escolha.strip('[]')
        valores = {}
        print('unidades: ', self.unidades.keys())
        for d in dados: #Parâmetros para valores de variável
            for u in self.unidades.keys():
                if d == u:
                    print(d, 'de dados é igual a ', u, 'de self.unidades')
                    if len(self.unidades[u][1]) == 3:
                        A = self.unidades[u][1][0]
                        B = self.unidades[u][1][1]
                        C = self.unidades[u][1][2]
                        valores[d] = randint(A, B)/C
                    elif len(self.unidades[u][1]) == 5:
                        A = self.unidades[u][1][0]
                        B = self.unidades[u][1][1]
                        C = self.unidades[u][1][2]
                        D = self.unidades[u][1][3]
                        E = self.unidades[u][1][4]
                        valores[d] = (randint(A, B)/C)*10**(randint(D, E))
        print('Valores dict: ', valores )
        
        for g in self.grandezas.keys():
            if icognita == g:
                ic = self.grandezas[g]
        print('ic: ', ic)
        
        escolha_copia_2 = escolha_com_opes
        
        #for o in opes:
        #    if o in escolha:
        #        escolha_copia = escolha_copia.replace(o, f' {o} ')
        
        escolha = escolha_copia_2.split()
        valores_keys = []
        
        for k in valores.keys():
            valores_keys.append(k)
        
        for v in valores_keys:
            for e in escolha:
                if str(v) == str(e):
                    i = escolha.index(e)
                    escolha.remove(e)
                    escolha.insert(i, str(valores[e]))
        print('Escolha após substituição: ', escolha)
        escolha = ''.join(escolha)

        E = self.enunciado + '\n'
        for k in valores.keys():
            for g in self.grandezas.keys():
                if g == k:
                    E += self.grandezas[g] + ' = ' + str(valores[k]) + ' ' + str(self.unidades[g][0]) + ',\n '
        E += 'assim, calcule o valor do(a)\n' + ic + '\n'

        resposta = eval(escolha)

        if type(resposta) == tuple or type(resposta) == list and len(resposta) >= 2:
            Gabarito = [r for r in resposta]
            Gabarito = ' ou '.join(Gabarito)
            for r in resposta:
                if str(r)[0] != '-':
                    resposta = float(r)
                    break
        else:
            resposta = str(resposta)
            resposta = resposta.replace('[', '')
            resposta = resposta.replace(']', '')
            Gabarito = round(float(resposta), 2)

        for u in self.unidades:
            unidade = self.unidades[icognita]

        #try:
        #    resposta = eval(escolha)
        #    if type(resposta) == tuple or type(resposta) == list:
        #        print('resposta composta:', resposta)
        #        for r in resposta:
        #            if str(r)[0] != '-':
        #                resposta = float(r)
        #                break
        #    Gabarito = round(float(resposta), 2)
        #except:
        #    Gabarito = 5*'-=' + 'Sem solução Real' +  5*'=-'
        
        return Question(enunciado = E, gabarito = f'{Gabarito} {unidade[0]}')

class Question(models.Model):
    criado = DateTimeField(auto_now=True)
    questao = ForeignKey(QuestionModel, on_delete=CASCADE)
    enunciado = TextField()
    gabarito = CharField(max_length=100)

    def __str__(self):
        return str(self.criado)+ '/' +self.area + ' - ' + self.tema

# Create your models here.
