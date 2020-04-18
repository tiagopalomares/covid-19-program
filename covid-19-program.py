#new-program
print ('COVID-19 ')
import time
#introdução
time.sleep(2)
print ('Esse Programa foi desenvolvido por Tiago Palomares')
time.sleep(2)
print ('Iniciando Programa . . . ')
time.sleep(2)
nome = (input('Qual o seu nome? '))
time.sleep(1)
print  ('Bem vindo {}'.format(nome))
time.sleep(1)
idade = int(input('Qual a sua idade? '))
time.sleep(2)
print ('Responda se SIM ou NÃO para as perguntas a seguir ...')
time.sleep(1)

sim = 0
não = 1

f = int(input('Você está febril ? '))
time.sleep(1)
r = int(input('Você tem dificuldade para respirar ? '))
time.sleep(1)
t =  int(input('Você está com tosse ? '))
time.sleep(1)
c = int(input('Você se sente cansado ? '))
time.sleep(1)

while f == 0 & r == 0 & t == 0 & c == 0:
#if febre == sim respirar == sim tosse == sim cansado == sim:
    print ('Por favor {}, procure urgente um hospital e faça um exame de sangue'.format(nome))