from random import randint
def pogodiBroj():
  broj=randint(1,10)
  brojpogadjanja=0
  gotovo=False
  brojigre=1
  print("Napomena:Isključivo unosite brojeve sa tastature")
  while not gotovo
    unos=input("Pogodi broj: ")

    if not unos.isdigit():#provjerava da li je unos string
      print("Unijeli ste string!")
      brojpogadjanja += 1
    else:

      if int(unos)<1 or int(unos)>10: #provjerava da li je unos u rasponu od 1 do 10
        print("Unos nije dozvoljen! Unesite broj ponovo.")
        brojpogadjanja+=1
        continue
      elif broj<int(unos):
        print("Zao nam je,unijeli ste veci broj")
        brojpogadjanja+=1
        continue
      elif broj>int(unos):
        print("Zao nam je,unijeli ste manji broj")
        brojpogadjanja+=1
        continue
      else:
        print("Cestitamo,pogodili ste trazeni broj")
        brojpogadjanja+=1
        print("Pogodili ste iz ",brojpogadjanja,"puta")
        if brojigre < 3: #uslov da se igra ponavlja samo 3 kruga
          pitanje=(input("Da li zelite nastaviti igru? ")) #dio koda koji ispituje korisnika da li zeli nastaviti igru
          if pitanje=="Da" or pitanje=="da" or pitanje=="DA" or pitanje=="yass":
            broj=randint(1,10)
            brojpogadjanja=0
            gotovo=False
            brojigre+=1
          else:
            gotovo=True
            print("Kraj igre")
        else:
          print("Igra je gotova nakon treceg kruga! Hvala na druzenju. ")
          break

pogodiBroj() #poziv funkcije
