# new-program
print('COVID-19 ')
import time

# introdução
time.sleep(2)
print('Esse Programa foi desenvolvido por Tiago Palomares')
time.sleep(2)
print('Iniciando Programa . . . ')
time.sleep(2)
nome = (input('Qual o seu nome? '))
time.sleep(1)
print('Bem vindo {}'.format(nome))
time.sleep(1)
idade = int(input('Qual a sua idade? '))
time.sleep(2)
print('Responda se SIM ou NÃO para as perguntas a seguir \n sendo 1 para sim e 0 para não...')
time.sleep(1)

sim = int(1)
não = int(0)

f = int(input('Você está febril ? '))
time.sleep(1)
r = int(input('Você tem dificuldade para respirar ? '))
time.sleep(1)
t = int(input('Você está com tosse ? '))
time.sleep(1)
c = int(input('Você se sente cansado ? '))
time.sleep(1)
saude: int = f + r + t + c
vu = saude + idade

if vu >= 70:
    print('Por favor {}, procure urgente um hospital e faça um exame de sangue'.format(nome))
elif vu :
    print('Você esta bem, fique em casa {} '.format(nome))
#elif vu <= 30:
  #  print('Fique tranquilo deve ser apenas uma gripe, fique em casa {} '.format(nome))
