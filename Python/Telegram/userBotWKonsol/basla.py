from konsolTaban import *
from userBot import kekikUserBot

#-----------------------------------#
def acilisSayfasi():
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    
    kekikUserBot.botBaslat()

if __name__ == '__main__':
    acilisSayfasi()
