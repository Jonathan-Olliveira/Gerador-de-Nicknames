import random as rd
import time

#criar novas listas de nomes, inclusive separados que se concatenam.
#mais opções de listas


Brasileiro = [
    "GuerreiroBR", "CaçadorDeNoobs", "MestreDasLâminas", "FúriaTropical",
    "SenhorDosAnéis", "DragãoDoSul", "FantasmaNegro", "NinjaCarioca",
    "VingadorMístico", "CaveiraVoadora", "MestreDoCaos", "ReiDaSelva",
    "GladiadorBR", "SamuraiDoBrasil", "RainhaDosGames", "PrincesaGamer", "MagaMística", "FeiticeiraDasTrevas",
    "FênixDourada", "DeusaDaGuerra", "NinjaGata", "ValquíriaDoSul",
    "CaçadoraDeFantasmas", "SenhoraDoCaos", "ImperatrizBR", "DivaDosGames"
]

Estrangeiro = [
    "ShadowHunter", "DragonSlayer", "BladeMaster", "IronFist",
    "NightStalker", "WarLord", "PhoenixKnight", "GhostRider",
    "ThunderWolf", "DarkRaven", "StormBringer", "IceWarrior",
    "FireMage", "SteelSamurai", "MysticQueen", "LunaSorceress", "ShadowPriestess", "StarGoddess",
    "PhoenixEmpress", "MoonlightDiva", "StormEnchantress", "FireSiren",
    "IceQueen", "DarkEnchantress", "CrystalMaiden", "WarriorPrincess",
    "CelestialMage", "ShadowValkyrie"
]
#print(rd.choice(names))

#Criar embaralhamento de lista
def cria_nick():
    for i in range(qtde):
        if Estilo == 1:
            print("Nick", i + 1, ":", rd.choice(Brasileiro))
            time.sleep(1)
        elif Estilo == 2:
            print("Nick", i + 1, ":", rd.choice(Estrangeiro))
            time.sleep(1)
        else:
            print("Valor não encontrado")


#loop
print("Bem-Vindo ao gerador de Nicknames!")
while True:

    print("Deseja gerar quantos nomes?")
    qtde = int(input())
    print("Diga qual estilo de nick você prefere: ")

    print("""
    1- Brasileiro
    2- Estrangeiro
    3- Medievais
    4- Fodastico
    """)
    Estilo = int(input())
    cria_nick()
    loop= str(input("Deseja Criar mais dos mesmo modo?"))
    #Arrumar tratamento de erros caso não for uma string
    #Arrumar variavel loop para repertir sem voltar ao inicio
    #criar novos caminhos de loop, podendo alterar quantidade criada e modo do nick
    try:
        if loop.lower() == "sim" or "s":
            cria_nick()
    except ValueError:
        print("Aceito somente texto")
   # else:
        #break