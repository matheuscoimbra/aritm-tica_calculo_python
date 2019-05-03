dizima = 0.11
nBinario = []
listRep = []
while (dizima != 0.0):
    dizima *= 2
    resto = int(dizima)
    nBinario.append(resto)
    dizima -= resto
    if dizima not in listRep:
        listRep.append(dizima)
    else:
        break


print("0.{}".format(str(nBinario).replace(",","").replace("[","").replace("]","").replace(" ",""))[0:9])