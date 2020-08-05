from botAlani import betikUserBot

from rich.console import Console
import sys
from pyrogram import __version__
from pyrogram.api.all import layer

konsol = Console()

def hata (yazi):
   konsol.print(yazi, style="bold red")
def bilgi (yazi):
   konsol.print(yazi, style="blue")
def basarili (yazi):
   konsol.print(yazi, style="bold green")
def onemli (yazi):
   konsol.print(yazi, style="bold cyan")
def soru (soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def logo ():
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   konsol.print(f"\t[bold blue]@betikUserBot[/] [yellow]:bird:[/]\t[bold red]Python: [/][i]{surum}[/]")

logo()

basarili(
    f"betikUserBot v{__version__} pyrogram tabanında çalışıyor,"
    f" {layer} katman başlatıldı..."
    )


if __name__ == '__main__':
    betikUserBot.run()