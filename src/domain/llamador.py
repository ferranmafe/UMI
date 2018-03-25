import SoundPlayer



def main():
    pn = SoundPlayer.PlayNotes()
    pn.inicializar()

    pn.tocar(['la','re','fa'])
    pn.tocar(['mi'])
    pn.tocar(['mi'])
    pn.tocar(['mi'])
    pn.tocar(['mi'])
    while 1:
        pass
main()