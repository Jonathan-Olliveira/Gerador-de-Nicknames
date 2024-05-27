import random as rd
import time


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


print("Bem-Vindo ao gerador de Nicknames!")

print("Deseja gerar quantos nomes por rodada?")
rodada = int(input())
print("Diga qual estilo de nick você prefere: ")

print("""
1- Brasileiro
2- Estrangeiro
3- Medievais
4- Fodastico
""")
Estilo = int(input())

for i in range(rodada):
    if Estilo == 1:
        print("Nick",i+1,":",rd.choice(Brasileiro))
        time.sleep(1)
    elif Estilo == 2:
        print("Nick",i+1,":",rd.choice(Estrangeiro))
        time.sleep(1)
    else:
        print("Valor não encontrado")





