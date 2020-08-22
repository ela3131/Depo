from taban import *
from fonksiyonlar import bakalim, dongu

#-----------------------------------#
def acilisSayfasi():
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    print(f"""
    {Fore.GREEN}[{Fore.YELLOW} 1 {Fore.GREEN}] {Fore.CYAN}Bunu Seçersem
    {Fore.GREEN}[{Fore.YELLOW} 2 {Fore.GREEN}] {Fore.CYAN}Şunu Seçersem
    """) # Seçeneklerimizi ayarladık

    konum = os.getcwd()
    if isletim_sistemi == "Windows":
        konum = konum.split("\\")
    else:
        konum = konum.split("/")

    secenek = str(input(f"{Fore.RED}{oturum}:{Fore.LIGHTBLUE_EX}~/../{konum[-2] + '/' + konum[-1]} >> {Fore.GREEN}")) # Kullanıcı için input oluşturduk

    #-----------------------#
    if secenek == '1':
        temizle()
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)


        bakalim.kurek()
        sleep(2)
        acilisSayfasi()
    #-----------------------#
    elif secenek == '2':
        temizle()
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)


        dongu.kisir()
        sleep(2)
        acilisSayfasi()
    #-----------------------#
    elif secenek == 'q':
        import sys
        sys.exit()
    #-----------------------#
    else:
        temizle()
        acilisSayfasi()


if __name__ == '__main__':
    acilisSayfasi()