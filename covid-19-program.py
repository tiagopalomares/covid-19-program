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
idade = int(input('Quantos anos você tem? '))
time.sleep(2)
print('Responda se SIM ou NÃO para as perguntas a seguir \n sendo 1 para sim e 0 para não...')
time.sleep(1)

sim = 1
não = 0

f = int(input('Você está febril ? '))
time.sleep(1)
r = int(input('Você tem dificuldade para respirar ? '))
time.sleep(1)
t = int(input('Você está com tosse ? '))
time.sleep(1)
c = int(input('Você se sente cansado ? '))
time.sleep(1)
saude = f + r + t + c
vu = saude + idade

if vu <= 5 :
	print ('\n está tudo bem, na sua idade a taxa de mortalidade é de 0,00% ')

elif vu <= 19 :
	print ('\n está tudo bem, na sua idade a taxa de mortalidade é de 0,2% ')

elif vu <= 30 :
	print ('\n está tudo bem, na sua idade a taxa de mortalidade é de 0,2% ')
	
elif vu <= 40 :
	print ('\n está tudo bem, na sua idade a taxa de mortalidade é de 0,2% ')
	
elif vu <= 50 :
	print ('\n está tudo bem, na sua idade a taxa de mortalidade é de 0,4% ')
	
elif vu <= 60 :
	print ('\n está tudo bem,deve ser apenas uma gripe, fique calmo na sua idade a taxa de mortalidade é de 1,3% ')
	
elif vu <= 70 :
	print ('\n está tudo bem,deve ser apenas uma gripe, fique em casa e se acalme, na sua idade a taxa de mortalidade é de 3,6% ')
	
elif vu <= 80 :
	print ('\n está tudo bem,deve ser apenas uma gripe,mas fique em casa e fique calmo, na sua idade a taxa de mortalidade é de 8,0% ')
	
elif vu >= 81 :
	print ('\n deve ser apenas uma gripe, fique em casa e calmo na sua idade a taxa de mortalidade é alta, se os sintomas persistirem procure ajuda médica urgente e solicite um exame! ')
time.sleep(2)
print ('  Dicas importantes para evitá-lo:')
time.sleep(1)
print ('\n Fique em casa \n Use a máscara')
time.sleep(1)
print ('\n Lave as mãos com sabão \n ou use álcool em gel')
time.sleep(1)
print('\n Obrigado...')

#elif vu >= 70:
   # print('Por favor {}, procure urgente um hospital e faça um exame de sangue'.format(nome))
#elif vu :
    #print('Você esta bem, fique em casa {} '.format(nome))
#elif vu <= 30:
  #  print('Fique tranquilo deve ser apenas uma gripe, fique em casa {} '.format(nome))
