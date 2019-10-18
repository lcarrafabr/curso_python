url = r"C:/Users/luciano.cb/Desktop/users02.txt"
f = open('C:/Users/luciano.cb/Desktop/saida.csv', 'w')
nomeId = ''
userBloqueado = ''
nomeCompleto = ''
concatena = ''

qtdNome = 0
qtdUserBloqueado = 0
qtdNOmeCOmpleto = 0

compras = ''
estoque = ''
faturamento = ''
livrosFiscais = ''
gestaoDeTransportes = ''
automacaoFiscal = ''
administradores = ''
ti = ''

samsungMatriz = ''
samsungManaus = ''
samsungCampinas = ''
samsungGuarulhos = ''
samsungItapoa = ''
samsungCajamar = ''
samsungSantaCatarina = ''
samsungMinasgerais = ''
samsungDistritoFederal = ''

arquivo = open(url)
print('Iniciando...')

f.write('\"Login\",\"Nome Completo\",\"Usuário bloqueado\",\"Compras\",\"Estoque\",\"Faturamento\",'
        '\"Livros Fiscais\",\"Gestão de Transportes\",\"Automação Fiscal\",\"Administradores\",\"T.I\"'
        ',\"Samsung matriz\",\"Samsung Manauz\",\"Samsung Campinas\",\"Samsung Guarulhos\",\"Samsung Itapoa\"'
        ',\"Samdung Cajamar\",\"Samsung Santa Catarina\",\"Samsung Minas Gerais\",\"Samsung Distrito federal\"')
f.write("\n")

for line in arquivo:

    if line.strip().__contains__('N o m e :'):
        #  print(line)
        nomeId = line.replace("N o m e : ", '').replace(' ', '')
        qtdNome += 1

    if line.strip().__contains__("U s u á r i o b l o q u e a d o"):
        # print(line)
        userBloqueado = line.replace('U s u á r i o b l o q u e a d o : ', '').replace(' ', '')
        qtdUserBloqueado += 1

    if line.__contains__("N o m e C o m p l e t o"):
        nomeCompleto = line.replace('N o m e C o m p l e t o : ', '')
        qtdNOmeCOmpleto += 1

    if nomeId != '' and userBloqueado != '' and nomeCompleto != '':
        concatena = '\"' + nomeId.strip() + '\",\"' + nomeCompleto.strip() + '\",\"' + userBloqueado.strip() + '\",'
        f.write(concatena)
        #  f.write("\n")
        concatena = ''
        nomeId = ''
        userBloqueado = ''
        nomeCompleto = ''

    if line.strip().__contains__("0 2 - C O M P R A S"):
        compras = 'X'

    if line.strip().__contains__('0 4 - E S T O Q U E'):
        estoque = 'X'

    if line.strip().__contains__('0 5 - F A T U R A M E N T O'):
        faturamento = 'X'

    if line.strip().__contains__('0 9 - L I V R O S F I S C A I S'):
        livrosFiscais = 'X'

    if line.strip().__contains__('4 3 - G E S T A O D E T R A N S P O R T E'):
        gestaoDeTransportes = 'X'

    if line.strip().__contains__('8 4 - A U T O M A C A O F I S C A L'):
        automacaoFiscal = 'X'

    if line.strip().__contains__('A d m i n i s t r a d o r e s'):
        administradores = 'X'

    if line.strip().__contains__('T I'):
        ti = 'X'

#  ***************************************************************************************************************

    if line.strip().__contains__('S A M S U N G M A T R I Z'):
        samsungMatriz = 'X'

    if line.strip().__contains__('S A M S U N G - M A N A U S'):
        samsungManaus = 'X'

    if line.strip().__contains__('S A M S U N G - C A M P I N A S'):
        samsungCampinas = 'X'

    if line.strip().__contains__('S A M S U N G - G U A R U L H O S'):
        samsungGuarulhos = 'X'

    if line.strip().__contains__('S A M S U N G - I T A P O A'):
        samsungItapoa = 'X'

    if line.strip().__contains__('S A M S U N G - C A J A M A R'):
        samsungCajamar = 'X'

    if line.strip().__contains__('S A M S U N G - S A N T A C A T A R I N A'):
        samsungSantaCatarina = 'X'

    if line.strip().__contains__('S A M S U N G - M I N A S G E R A I S'):
        samsungMinasgerais = 'X'

    if line.strip().__contains__('S A M S U N G - D I S T R I T O F E D E R A L'):
        samsungDistritoFederal = 'X'

    if line.strip().__contains__("I D :"):
        concatena02 = '\"' + compras + '\",' + '\"' + estoque + '\",' + '\"' + faturamento + '\",' + '\"' \
            + livrosFiscais + '\",' + '\"' + gestaoDeTransportes + '\",' + '\"' + automacaoFiscal + '\",' \
            + '\"' + administradores + '\",' + '\"' + ti + '\",' + '\"' + samsungMatriz + '\",' \
            + '\"' + samsungManaus + '\",' + '\"' + samsungCampinas + '\",' + '\"' + samsungGuarulhos + '\",' \
            + '\"' + samsungItapoa + '\",' + '\"' + samsungCajamar + '\",' + '\"' + samsungSantaCatarina + '\",' \
            + '\"' + samsungMinasgerais + '\",' + '\"' + samsungDistritoFederal + '\",'

        f.write(concatena02)
        f.write("\n")
        compras = ''
        estoque = ''
        faturamento = ''
        livrosFiscais = ''
        gestaoDeTransportes = ''
        automacaoFiscal = ''
        administradores = ''
        ti = ''
        samsungMatriz = ''
        samsungManaus = ''
        samsungCampinas = ''
        samsungGuarulhos = ''
        samsungItapoa = ''
        samsungCajamar = ''
        samsungSantaCatarina = ''
        samsungMinasgerais = ''
        samsungDistritoFederal = ''

#  print(i)
f.close()
arquivo.close()

print('Finalizado!!')
print(qtdNome, ' ', qtdUserBloqueado, ' ', qtdNOmeCOmpleto)
