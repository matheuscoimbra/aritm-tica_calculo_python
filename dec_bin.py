#coding=utf-8

def antes_ponto(str=""):
	decimal = 0
	bitt = []
	for i in range(len(str)):
		bitt.append(int(str[i]))
	bitt.reverse()
	for i in range(len(bitt)):
		decimal += bitt[i]*(2**i)
	return decimal

bits = str(input("Informe o valor em bits.:"))
bit = []
lantes = []
lpos = []
if "." in bits:
#1111.1110 = 1∙23+1∙22+1∙21+1∙20+1∙2-1+1∙2-2+1∙2-3+0∙2-4 
#= 8+4+2+1+0.5+0.25+0.125+0 = 15.875
	bit = bits.split(".")
	dantes = antes_ponto(bit[0])
	pos = bit[1]
	for i in range(len(pos)):
		lpos.append(int(pos[i]))
	dpos = 0
	for i in range(len(lpos)):
		#print(lpos[i]*(2**-(i+1)))
		dpos += lpos[i]*(2**-(i+1))
	#print(dpos)
	print("decimal: ",dantes+dpos)
else:
	# 110 = 2x0^0  + 2x1 ^1 + 2*1^2 = 6
	decimal = antes_ponto(bits)
	print("decimal: ",decimal)