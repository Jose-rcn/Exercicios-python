from random import randint
nove_digitos = ''
for contador in range (0,9,1):
    nove_digitos += str(randint(0,9))

#primeiro digito de validação(penultimo digito)
contador_regressivo = 10
somatorio_digitos = 0
for digito in nove_digitos:
    digito_int = int(digito)
    somatorio_digitos += digito_int * contador_regressivo
    contador_regressivo -= 1
validador_por_onze = (somatorio_digitos * 10) % 11

penultimo_digito = validador_por_onze if validador_por_onze <= 9 else 0

#segundo digito de validação(ultimo digito)
cpf_dez_digitos = nove_digitos + str(penultimo_digito)
contador_regressivo = 11
somatorio_digitos = 0
for digito in cpf_dez_digitos:
    digito_int = int(digito)
    somatorio_digitos += digito_int * contador_regressivo
    contador_regressivo -= 1
validador_por_onze = (somatorio_digitos * 10) % 11

ultimo_digito = validador_por_onze if validador_por_onze <= 9 else 0

#validador
cpf_final = nove_digitos + str(penultimo_digito) + str(ultimo_digito)
print(cpf_final)