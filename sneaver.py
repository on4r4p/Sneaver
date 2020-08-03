#!/usr/bin/python3
from shutil import which
from pyfiglet import Figlet
from inputs import devices
from pynput.keyboard import Key, Controller
import os,sys,random,subprocess,datetime,re,time,signal,pygame
ScriptDir = os.path.dirname(os.path.abspath(__file__))
DirMovies = ScriptDir+"/Movies/"
DirData = ScriptDir+"/Data/"
DirGif = DirData+"Gifs/"
DirSaves = DirData+"savestate/"
WALLET = 0
KILLLOAD = ""
OLDSCREEN = ""
NEWRES = ""
LASTSEGFAULT = ""
GlobStart = ""
GlobExit = ""
SearchRom = ""
BADROMS = []
RESPAWN = False
IGNOREBAD = False
SEARCH = False
ERROR = False
GODMODE = False
NOJP = False
NOEU = False
NOUS = False
JP = False
EU = False
US = False
RECORD = False
REPLAY = False
CONFIG = False
ONESHOT= False




print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄            
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌           
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀            




              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
             ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
             ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
             ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌  ▐░▌         ▐░▌  ▐░▌          ▐░▌       ▐░▌
 ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄▄▄      
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀▀▀      
                       ▐░▌▐░▌    ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌      ▐░▌ ▐░▌      ▐░▌          ▐░▌     ▐░▌
              ▄▄▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌
             ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌        ▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌
              ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀          ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀





 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄            
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌           
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀            
\n
""")
time.sleep(2)

def signal_handler(sig, frame):
        if OLDSCREEN != "":
               ScreenResize("revert")
        GetOut()

def RwFile(filename,data,mode):

     try:


          if filename == "bad.roms":
               if mode == "r":
                    with open(DirData+filename,mode) as file:
                         lines = file.readlines()
                         lines = [l.strip() for l in lines ]
                         return lines
               else:
                    FoundBad = False
                    with open(DirData+filename,"a+") as file:
                         lines = file.readlines()
                         lines = [l.strip() for l in lines ]
                         for item in lines:
                              if str(data) == item:
                                   FoundBad = True
                         if FoundBad == False:
                              file.write("\n"+str(data))
          else:

               with open(DirData+filename,mode) as file:
                    if mode == "w":
                        file.write(str(data))
                    if mode =="r":
                         for l in file:
                              return l 
     except Exception as e:
          print("Error! : "+str(e))


def Segfault():
     global LASTSEGFAULT
     dmesg = str(subprocess.check_output(["dmesg"])).split("\\n")
     lastone = []
     for line in dmesg:
          if "snes9x" in line and "segfault at" in line:
               lastone.append(line)
     try:
          if len(lastone) > 0 and LASTSEGFAULT == lastone[-1]:
               Snesisdead = False
          elif LASTSEGFAULT == "":
               Snesisdead = False
          else:
               Snesisdead = True
          if len(lastone) > 0:
               LASTSEGFAULT = lastone[-1]

     except Exception as e:
               Pfig("digital","Error LASTSEGFAULT",e)
               Snesisdead = False

     return Snesisdead

def Pfig(txt):
     Fig = Figlet(font='digital')
     print(Fig.renderText(txt))
     return


def AutoSaveState():
     global CHECKPOINT

     if CHECKPOINT >= 23:
          CHECKPOINT = 0
          print("\n!!AutoSaving!!\n")
          keyboard = Controller()

          keyboard.press(Key.insert)
          keyboard.release(Key.insert)

          time.sleep(1)

          keyboard.press(Key.insert)
          time.sleep(1)
          keyboard.release(Key.insert)


#     else:
#          print("\n\nDebug CHECKPOINT : "+str(CHECKPOINT))

def WaitForMe(process):

      global ERROR
      global CHECKPOINT
      if process != "snes9x":
              while True:
                    try:
                         checkproc = int(subprocess.check_output(["pidof","-s",process]))
                         time.sleep(1)
                    except Exception as e:
                         if "returned non-zero exit status 1" in str(e):
                              return
                         else:
                              Pfig("Error WaitForMe:"+str(e))

      else:
          while True:
              try:
                    checksnes9x = int(subprocess.check_output(["pidof","-s",process]))
                    time.sleep(1)
                    try:
                         snesfault = Segfault()
                         if snesfault == True:
                              Pfig("Segfault found :"+str(LASTSEGFAULT))
                              ERROR = True
                              pkill = subprocess.Popen("pkill snes9x",shell=True)
                              return
                         else :
                              ERROR = False
                    except Exception as e:
                         Pfig("Segfault Error:"+str(e))
                         ERROR = True
                    try:
                         crashbandicoot = ManualExit()
                         if crashbandicoot == True:
                                   Pfig("\nCaught Manual Exit.\n")
                                   ERROR = True
                                   pkill = subprocess.Popen("pkill snes9x",shell=True)
                                   return
                         else:
                                   ERROR = False

                    except Exception as e:
                              Pfig("ManualExit Error:"+str(e))

                    CHECKPOINT = CHECKPOINT + 1
                    AutoSaveState()

              except Exception as e:
                         if "returned non-zero exit status 1" in str(e):
                              ERROR = False
                              return
                         else:
                              Pfig("Proc/Status Error:"+str(e))


def GifLauncher(mode):

     global ONESHOT
     global KILLLOAD
     global WALLET

     Pfig("\nLaunching animation : " +str(mode))

     if mode != "Wheel":

          Categorie = [i for i in os.listdir(DirGif)]
          Gif= ""
          for name in Categorie:
                    if str(name) == str(mode):
                         Gifiles = [i for i in os.listdir(DirGif+str(name))]
                         rnd = random.randint(0,len(Gifiles)-1)
                         Gif = DirGif+str(name)+"/"+Gifiles[rnd]

          if mode == "Continue":
               timer = "10.5"
          elif mode == "Exit":
               timer = "10"
          elif mode == "Loading":
               timer = "0"
          elif mode == "GameOver":
               timer = "10"
          elif mode == "BadBoy":
               timer = "10"
          elif mode == "Error":
               timer = "7"
          elif mode == "NewGame":
               timer = "7"
          elif mode == "Win":
               timer = "10"
          elif mode == "Loose":
               timer = "8"
          elif mode == "InsertCoin":
               timer = "7"


          if which("sxiv") != True:
               if mode != "Loading":
                    cmd = "timeout "+timer+" sxiv -abfp -sf " + str(Gif)
               else:
                    KILLLOAD = "sxiv"
                    cmd = "sxiv -abfp -sf " + str(Gif)
          elif which("eog") != True:
               if mode != "Loading":
                    cmd = "timeout "+timer+" eog --fullscreen " + str(Gif)
               else:
                    KILLLOAD = "eog"
                    cmd = "eog --fullscreen " + str(Gif)
          elif which("animate") != True:
               if mode == "Loading":
                    KILLLOAD = "animate"
               Geo8= str(ScreenResize("height"))
               cmd = "animate -immutable -loop "+timer+" -geometry "+ Geo8 + " "+str(Gif)
          else :
               #ascimatics ?
               Pfig("\n\n!!!!Can't Display Animation"+str(mode)+"!!!!\n\n")

               return 

          try:
               if mode != "Loading":
                    anim = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output,error = anim.communicate()
                    aout =output.decode()
               else:

                    anim = subprocess.Popen(cmd, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)

          except Exception as e:
               Pfig("Error: "+str(e))

          if mode =="Loose":
               return

     if mode == "Wheel":
          Categorie = [i for i in os.listdir(DirGif)]
          Avi= ""
          for name in Categorie:
                    if str(name) == str(mode):
                         Avifiles = [i for i in os.listdir(DirGif+str(name))]
                         rnd = random.randint(0,len(Avifiles)-1)
                         Avi = DirGif+str(name)+"/"+Avifiles[rnd]
          cmd = "cvlc --fullscreen --no-osd --play-and-exit "+ str(Avi)

          Pfig("\nLaunching : Wheel Of Roucoups")
          #print(cmd)

          cvlc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          output,error = cvlc.communicate()

          if "COIN.avi" in Avi:
              WALLET = 3
              RwFile("credits.save",WALLET,"w")
              ONESHOT = True
              return GifLauncher("Win")
          elif "GHOST.avi" in Avi:
              WALLET = 5
              RwFile("credits.save",WALLET,"w")
              ONESHOT = True
              return GifLauncher("Win")
          elif "YOSHICOIN.avi" in Avi:
              WALLET = 10
              RwFile("credits.save",WALLET,"w")
              ONESHOT = True
              return GifLauncher("Win")
          elif "QUESTIONBLOCK.avi" in Avi:
              luck = random.randint(10,32)
              WALLET = luck
              RwFile("credits.save",WALLET,"w")
              ONESHOT = True
              return GifLauncher("Win")
          elif "DEADBLOCK.avi" in Avi:
              WALLET = 1 
              RwFile("credits.save",WALLET,"w")
              ONESHOT = True
              return GifLauncher("Loose")

def GetOut():
     GifLauncher("Exit")
     Pfig("\n\n==Sneaver exited==\n\n")
     sys.exit(1)



##ARGH!

if len(sys.argv) >1:

     if "--nojp" in sys.argv:
          NOJP = True

     if "--noeu" in sys.argv:
          NOEU = True

     if "--nous" in sys.argv:
          NOUS = True

     if "--jp" in sys.argv:
          JP = True

     if "--eu" in sys.argv:
          EU = True

     if "--us" in sys.argv:
          US = True

     if "--godmode" in sys.argv:
          GODMODE = True

     if "--record" in sys.argv:
          RECORD = True

     if "--replay" in sys.argv:
          REPLAY = True

     if "--config" in sys.argv:
          CONFIG = True

     if "--search" in sys.argv:
          SEARCH = True
          pos = sys.argv.index("--search")
          try:
               SearchRom = str(sys.argv[pos+1])
          except:
             print("Search Argument is empty.")
             sys.exit(0)

     if "--respawn" in sys.argv:
          RESPAWN = True
          IGNOREBAD = True

     if "--allowbad" in sys.argv:
          IGNOREBAD = True

     if "--flushbad" in sys.argv:
          RwFile("bad.roms","","w")
          sys.exit(1)

     if "--badkid" in sys.argv:
          try:
             with open(DirData+"credits.save") as cs:
               for coin in cs:
                    Coins = int(coin)
          except Exception as e:
               print("Error:",e)
               sys.exit(1)
          print("Coins in wallet : ",Coins)
          print()
          while True:
               spanknbr = input("How many coins do you want to remove from the wallet ? (Enter a number between 1 to 32) :")
               if spanknbr.isdigit() == True:
                    if int(spanknbr) <= 32 and int(spanknbr) != 0:
                         break
          GifLauncher("BadBoy")
          if Coins != 0:
               Totalcoin = Coins - int(spanknbr)
               RwFile("credits.save",Totalcoin,"w")
          GifLauncher("GameOver")
          GetOut()


     if sys.argv[1] == "-h" or sys.argv[1] == "--help":
          print("\n**Sneaver is a script using snes9x and vlc to play or watch a snes game at random.\n\n**Download a rom put it in its folder inside the Movies directory\n\n**Then launch sneaver ^^\n\n\n**Use :\n\nsneaver --config (To configure your gamepads)  \n\nsneaver --record (For recording a random game.)\nsneaver --replay (For watching all the movies recorded with vlc.)\nsneaver --record --nojp/--jp (Avoid or Only recording Japenese games.)\nsneaver --record --noeu/--eu (Avoid or Only recording European games.)\nsneaver --record --nous/--us (Avoid or Only recording American games.)\nsneaver --record/--replay --search [Name] To search for a rom.\nsneaver --record --allowbad When a rom crash its filename is added in a list preventing it to be used again.\nUse this argument to ignore this list.\n\nsneaver --flushbad To erase bad roms list .\n\nsneaver --record --respawn After a crash try reloading the last auto save.\n\n\nWhile in record mode Sneaver is using a credit system.\nWhen credits reaches Zero you can't play anymore.\nseaver --badkid to remove some coins.\nsneaver --record --godmode (To get rich)\n\n\nKeep pressing the Exit button multiple times if Snes9x ever crash.\n**Have fun !!\n")
          print()
          sys.exit(1)
else:
          print("\n**Sneaver is a script using snes9x and vlc to play or watch a snes game at random.\n\n**Download a rom put it in its folder inside the Movies directory\n\n**Then launch sneaver ^^\n\n\n**Use :\n\nsneaver --config (To configure your gamepads)  \nsneaver --record (For recording a random game.)\nsneaver --replay (For watching all the movies recorded with vlc.)\nsneaver --record --nojp/--jp (Avoid or Only recording Japenese games.)\nsneaver --record --noeu/--eu (Avoid or Only recording European games.)\nsneaver --record --nous/--us (Avoid or Only recording American games.)\nsneaver --record/--replay --search [Name] To search for a rom.\nsneaver --record --allowbad When a rom crash it is add in a list preventing it to be used again .\nUse this argument to ignore this list.\nsneaver --flushbad To erase bad roms list .\nsneaver --record --respawn After a crash try reloading the last auto save.\n\n\nWhile in record mode Sneaver is using a credit system.\nseaver -badkid to remove some coins.\nsneaver --record --godmode (To get rich)\n\nKeep pressing the Exit button multiple time if Snes9x ever crash.\n**Have fun !!\n")
          print()
          sys.exit(1)

if RECORD == True and REPLAY == True:
            print("\nArguments record and replay can't be used at the same time.\n\n")
            sys.exit(1)


def LoadCoin(mode):
     global WALLET

     print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 

                   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
                  ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                   ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀
                       ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌
           ▄▄▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌ ▄▄▄▄▄▄▄▄▄▄▄
          ▐░░░░░░░░░░░▌▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌▐░░░░░░░░░░░▌             
           ▀▀▀▀▀▀▀▀▀▀▀ ▐░▌     ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀      ▐░▌ ▀▀▀▀▀▀▀▀▀▀▀
                       ▐░▌     ▐░▌    ▐░▌▐░▌          ▐░▌▐░▌          ▐░▌     ▐░▌       ▐░▌
                   ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌      ▐░▌
                  ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌
                   ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀

                        ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄
                       ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌
                       ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀
                       ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌
           ▄▄▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
          ▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
           ▀▀▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀▀▀
                       ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌          ▐░▌
                       ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌
                       ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌
                        ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
""")
     if mode == "firstload":
          if GODMODE == False:
               Coins = int(RwFile("credits.save",None,"r"))
               if Coins < 0:
                    Coins = 0

               if Coins > 32 :
                    Coins = 32

               WALLET = int(Coins)
               return

          else:
               Coins = 33
               WALLET = Coins
               return

     if mode == "printcoins":
          Coins = WALLET

     print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
 ▄▄        ▄  ▄         ▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄              
▐░░▌      ▐░▌▐░▌       ▐░▌▐░░▌     ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             
▐░▌░▌     ▐░▌▐░▌       ▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌             
▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌             
▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌             
▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             
▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀              
▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌               
▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌              
▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌             
 ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀              
                ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                                   
               ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                                  
               ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀                                                   
               ▐░▌       ▐░▌▐░▌                                                            
               ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄                                                   
               ▐░▌       ▐░▌▐░░░░░░░░░░░▌                                                  
               ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀                                                   
               ▐░▌       ▐░▌▐░▌                                                            
               ▐░█▄▄▄▄▄▄▄█░▌▐░▌                                                            
               ▐░░░░░░░░░░░▌▐░▌                                                            
                ▀▀▀▀▀▀▀▀▀▀▀  ▀                                                             
                          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  
                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌ 
                         ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀  
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌           
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄  
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌ 
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌ 
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌          ▐░▌ 
                         ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ 
                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌ 
                          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
""")
     time.sleep(2)
     print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
     coint = int(Coins)
     cointer = 1

     while cointer <= coint :
          print("""
             _.ooodIIIIIIIbooo._
         _.oII      _____    * IIo._
       oPI  _.oooIIII   IIIIo|o*_* IYo
     o8   oP  _.-I:          | |I._* `8o
    d`  o8`,-I    :          | |)  ,)* `b
   d`  d.-I      :           | |: (( `)
  8`  d` IIIII:  :           | |  ||)_/* `8
 8   8`      :  :       |)   _ |  || |`|   8
,8  8        :  :     /)| ) || |)_|| | |8  8.
8` ,8       :  :      I /_) |`:` | | | |8. `8
8  8`       :  :        _ _=`  ) ` __   __  8
8  8       :  :         )|__ |  | |  | | 8| 8
8  8.      :  :         ||   |  | |-:` | 8| 8
8. `8     /   |      __/ |__ |__| |  ) |__|,8
`8  8   .`    )     /     __ . . . . . .8LL8`
 8   8.`       `-. (    ,`  `.`. | | ,-|8  8
  8.(__________dd_) )__/ `  0|`.`: |: (8 ,8
   Y.  Y.                    | :/| |,)|* .P
    Y.  I8.          .,o     | | |,|I*  ,P
     I8.  IYo_               | |p|I* ,8I
       IY_   `Iooo.__   __.oo|I* * _PI
         ``Ioo_     IIIII    * _ooII`
              `IIIbooooooodIII`
          """)
          time.sleep(0.1)
          cointer = cointer + 1
          if cointer >= coint:
               break

          print('''
\t               ,,===IIIIII===,,
\t           ,==¨¨` |) |   /)   `¨¨==,
\t        ,=¨`|)    | )|  /__)   /)  `¨=,
\t      /¨    |,¨)  |  | /`  `) /  )     ¨)
\t    /¨  ,¨  |                 `)/    /|  ¨)
\t   /`  |   ,                       /¨,|   `)
\t  /`   ¨,/¨                           |    `)
\t /`      I=I=I               ,d8ba,___      `)
\t/`     I=8=8=8=I_I_          88888P¨¨¨       `)
\t|   xXXXXXXXXXXXXXXXxIxx    ,888¨             |
\t| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
\t| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
\t| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
\t) ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
\t`) -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /`
\t `) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /`
\t  `)    /¨)         1 9 9 4        ) /)    /`
\t   `)  ¨),/`                   |)   `) `  /`
\t     ¨)      /¨¨)   |    |     |,`)     /¨
\t       `¨=,_ )__/   |__  |__   |    ,=¨`
\t          `¨¨=,__             __,=¨¨`
\t               ``¨¨=========¨¨``
          ''')
          cointer = cointer + 1
          time.sleep(0.1)
          if cointer >= coint:
               break

          print("""
\t\t             _.ooodIIIIIIIbooo._
\t\t         _.oII   |`.  |    |   IIo._
\t\t       oPI  |`.  |  `.|    |    |  IYo
\t\t     o8 `.  |  `.|    |.   |    |    `8o
\t\t    d`    `.|    |.   | `. |    |      `b
\t\t   dI-------*====+====+====+====+-------Ib
\t\t  8`  `.    INNNNINNNNINNNNINNNNI        `8
\t\t 8      `.  INNNNINNNNINNNNINNNNI          8
\t\t,8----------+====*====+====+====+----------8.
\t\t8`  `.     `|    |`.  |gnnnnnnnn|.         `8
\t\t8     `.    |`.  |  `.|8   |.   | `.        8
\t\t8-----------+----+----*8---+----+-----------8
\t\t8        `. |   `|    |8,gnnnn:.|    `.     8
\t\t8.         `|    |`.  |8PI.| IYb|..png.`.  ,8
\t\t`8----------+----+----+----+---8+-8--`I----8`
\t\t 8          | `. |   `|n.  |`.dP| 8`. n    8
\t\t  8.        |   `|    |IYbnnndP.| `bnnP  ,8
\t\t   Y.-------+----+----+----+----+-------.P
\t\t    Y.      |    | `. |   `|    |`.    ,P
\t\t     I8.    | cg |   `|    |`.  |  `. 8I
\t\t       IY_  | mm |  19|89  |  `.|  _PI
\t\t         ``Ioo_  |    |  `.|  _ooII`
\t\t              `IIIbooooooodIII`
     """)

          cointer = cointer + 1
          time.sleep(0.1)
          if cointer >= coint:
               break

          print("""
\t\t\t             _.ooodIIIIIIIbooo._
\t\t\t         _.oII      _____    * IIo._
\t\t\t       oPI  _.oooIIII   IIIIo|o*_* IYo
\t\t\t     o8   oP                 | |I._* `8o
\t\t\t    d`  o8`_.--._            | |/  ,)* `b
\t\t\t   d`  d`.` __   I.          | |: (( `)
\t\t\t  8`  d`/,-I  `.   :         | |  ||)_/* `8
\t\t\t 8   8`|/      :   :    |)   _ |  || |`|   8
\t\t\t,8  8          :  :   /)| ) || |)_|| | |8  8.
\t\t\t8` ,8         /  :    I /_) |`:` | | | |8. `8
\t\t\t8  8`        /  /       _ _=`  ) ` __   __  8
\t\t\t8  8        /  /        )|__ |  | |  | | 8| 8
\t\t\t8  8.      /  /         ||   |  | |-:` | 8| 8
\t\t\t8. `8    ,` ,`       __/ |__ |__| |  ) |__|,8
\t\t\t`8  8  ,` ,`      _ /     __ . . . . . .8LL8`
\t\t\t 8   8I   `------`/(    ,`  `.`. | | ,-|8  8
\t\t\t  8.(_________dd_/  )__/ `  0|`.`: |: (8 ,8
\t\t\t   Y.  Y.                    | :/| |,)|* .P
\t\t\t    Y.  I8.          .,o     | | |,|I*  ,P
\t\t\t     I8.  IYo_               | |p|I* ,8I
\t\t\t       IY_   `Iooo.__   __.oo|I* * _PI
\t\t\t         ``Ioo_     IIIII    * _ooII`
\t\t\t              `IIIbooooooodIII`
     """)
          cointer = cointer + 1
          time.sleep(0.1)
          if cointer >= coint:
               break

          print("""
\t\t\t\t             _.ooodIIIIIIIbooo._
\t\t\t\t         _.oII      _____    * IIo._
\t\t\t\t       oPI  _.oooIIII   IIIIo|o*_* IYo
\t\t\t\t     o8   oP  _.-I:          | |I._* `8o
\t\t\t\t    d`  o8`,-I    :          | |/  ,)* `b
\t\t\t\t   d`  d.-I      :           | |: (( `)
\t\t\t\t  8`  d` IIIII:  :           | |  ||)_/* `8
\t\t\t\t 8   8`      :  :       |)   _ |  || |`|   8
\t\t\t\t,8  8        :  :     /)| ) || |)_|| | |8  8.
\t\t\t\t8` ,8       :  :      I /_) |`:` | | | |8. `8
\t\t\t\t8  8`       :  :        _ _=`  ) ` __   __  8
\t\t\t\t8  8       :  :         )|__ |  | |  | | 8| 8
\t\t\t\t8  8.      :  :         ||   |  | |-:` | 8| 8
\t\t\t\t8. `8     /   |      __/ |__ |__| |  ) |__|,8
\t\t\t\t`8  8   .`    )     /     __ . . . . . .8LL8`
\t\t\t\t 8   8.`       `-. (    ,`  `.`. | | ,-|8  8
\t\t\t\t  8.(__________dd_) )__/ `  0|`.`: |: (8 ,8
\t\t\t\t   Y.  Y.                    | :/| |,)|* .P
\t\t\t\t    Y.  I8.          .,o     | | |,|I*  ,P
\t\t\t\t     I8.  IYo_               | |p|I* ,8I
\t\t\t\t       IY_   `Iooo.__   __.oo|I* * _PI
\t\t\t\t         ``Ioo_     IIIII    * _ooII`
\t\t\t\t              `IIIbooooooodIII`
          """)
          time.sleep(0.1)
          cointer = cointer + 1
          if cointer >= coint:
               break

          print('''
\t\t\t\t               ,,===IIIIIII===,,
\t\t\t\t           ,==¨¨` |) |   /)   `¨¨==,
\t\t\t\t        ,=¨`|)    | )|  /__)   /)  `¨=,
\t\t\t\t      /¨    |,¨)  |  | /`  `) /  )     ¨)
\t\t\t\t    /¨  ,¨  |                 `)/    /|  ¨)
\t\t\t\t   /`  |   ,                       /¨,|   `)
\t\t\t\t  /`   ¨,/¨                           |    `)
\t\t\t\t /`      I=I=I               ,d8ba,___      `)
\t\t\t\t/`     I=8=8=8=I_I_          88888P¨¨¨       `)
\t\t\t\t|   xXXXXXXXXXXXXXXXxIxx    ,888¨             |
\t\t\t\t| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
\t\t\t\t| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
\t\t\t\t| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
\t\t\t\t) ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
\t\t\t\t`) -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /`
\t\t\t\t `) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /`
\t\t\t\t  `)    /¨)         1 9 9 4        ) /)    /`
\t\t\t\t   `)  ¨),/`                   |)   `) `  /`
\t\t\t\t     ¨)      /¨¨)   |    |     |,`)     /¨
\t\t\t\t       `¨=,_ )__/   |__  |__   |    ,=¨`
\t\t\t\t          `¨¨=,__             __,=¨¨`
\t\t\t\t               ``¨¨=========¨¨``
          ''')
          cointer = cointer + 1
          time.sleep(0.1)
          if cointer >= coint:
               break

          print("""
\t\t\t             _.ooodIIIIIIIbooo._
\t\t\t         _.oII   |`.  |    |   IIo._
\t\t\t       oPI  |`.  |  `.|    |    |  IYo
\t\t\t     o8 `.  |  `.|    |.   |    |    `8o
\t\t\t    d`    `.|    |.   | `. |    |      `b
\t\t\t   dI-------*====+====+====+====+-------Ib
\t\t\t  8`  `.    INNNNINNNNINNNNINNNNI        `8
\t\t\t 8      `.  INNNNINNNNINNNNINNNNI          8
\t\t\t,8----------+====*====+====+====+----------8.
\t\t\t8`  `.     `|    |`.  |gnnnnnnnn|.         `8
\t\t\t8     `.    |`.  |  `.|8   |.   | `.        8
\t\t\t8-----------+----+----*8---+----+-----------8
\t\t\t8        `. |   `|    |8,gnnnn:.|    `.     8
\t\t\t8.         `|    |`.  |8PI.| IYb|..png.`.  ,8
\t\t\t`8----------+----+----+----+---8+-8--`I----8`
\t\t\t 8          | `. |   `|n.  |`.dP| 8`. n    8
\t\t\t  8.        |   `|    |IYbnnndP.| `bnnP  ,8
\t\t\t   Y.-------+----+----+----+----+-------.P
\t\t\t    Y.      |    | `. |   `|    |`.    ,P
\t\t\t     I8.    | cg |   `|    |`.  |  `. 8I
\t\t\t       IY_  | mm |  19|89  |  `.|  _PI
\t\t\t         ``Ioo_  |    |  `.|  _ooII`
\t\t\t              `IIIbooooooodIII`
     """)

          cointer = cointer + 1
          time.sleep(0.1)
          if cointer >= coint:
               break

          print("""
\t\t             _.ooodIIIIIIIbooo._
\t\t         _.oII      _____    * IIo._
\t\t       oPI  _.oooIIII   IIIIo|o*_* IYo
\t\t     o8   oP                 | |I._* `8o
\t\t    d`  o8`_.--._            | |/  ,)* `b
\t\t   d`  d`.` __   I.          | |: (( `)
\t\t  8`  d`/,-I  `.   :         | |  ||)_/* `8
\t\t 8   8`|/      :   :    |)   _ |  || |`|   8
\t\t,8  8          :  :   /)| ) || |)_|| | |8  8.
\t\t8` ,8         /  :    I /_) |`:` | | | |8. `8
\t\t8  8`        /  /       _ _=`  ) ` __   __  8
\t\t8  8        /  /        )|__ |  | |  | | 8| 8
\t\t8  8.      /  /         ||   |  | |-:` | 8| 8
\t\t8. `8    ,` ,`       __/ |__ |__| |  ) |__|,8
\t\t`8  8  ,` ,`      _ /     __ . . . . . .8LL8`
\t\t 8   8I   `------`/(    ,`  `.`. | | ,-|8  8
\t\t  8.(_________dd_/  )__/ `  0|`.`: |: (8 ,8
\t\t   Y.  Y.                    | :/| |,)|* .P
\t\t    Y.  I8.          .,o     | | |,|I*  ,P
\t\t     I8.  IYo_               | |p|I* ,8I
\t\t       IY_   `Iooo.__   __.oo|I* * _PI
\t\t         ``Ioo_     IIIII    * _ooII`
\t\t              `IIIbooooooodIII`
     """)
          cointer = cointer + 1
          time.sleep(0.1)

     Cointing(Coins)

     time.sleep(1)
     return Coins


def InsertCoin(coinsleft):
     global WALLET

     coinsleft = int(coinsleft)
     if coinsleft <= 0:

          if ONESHOT == False:

               Pfig("\n\n!!!---LUCKY DAY---!!!\n!!!--WELCOME TO THE--!!!\n!!!---ROUCOUPS---!!!\n!!!---OF---!!!\n!!!---FORTUNE---!!!\n")

               GifLauncher("Wheel")

          else :

               GifLauncher("Continue")

               Pfig("\n\n===NOT ENOUGHT CREDIT TO PLAY==\n\n")
               GifLauncher("GameOver")
               GetOut()
     else:

          Pfig("\n\n--New Coin Inserted--\n--Get Ready--\n\n")
          time.sleep(1)
          GifLauncher("InsertCoin")
          if GODMODE == False:
               WALLET = coinsleft - 1
               RwFile("credits.save",coinsleft-1,"w")
          




def Cointing(credits):

          middle = ""
    


          if int(credits) == 1:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄     ▄▄▄▄                                                    
                                              ▐░░░░░░░░░▌  ▄█░░░░▌                                                   
                                             ▐░█░█▀▀▀▀▀█░▌▐░░▌▐░░▌                                                   
                                             ▐░▌▐░▌    ▐░▌ ▀▀ ▐░░▌                                                   
                                             ▐░▌ ▐░▌   ▐░▌    ▐░░▌                                                   
                                             ▐░▌  ▐░▌  ▐░▌    ▐░░▌                                                   
                                             ▐░▌   ▐░▌ ▐░▌    ▐░░▌                                                   
                                             ▐░▌    ▐░▌▐░▌    ▐░░▌                                                   
                                             ▐░█▄▄▄▄▄█░█░▌▄▄▄▄█░░█▄▄▄                                                
                                              ▐░░░░░░░░░▌▐░░░░░░░░░░░▌                                               
                                               ▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                                """
          if int(credits) == 2:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌▐░▌    ▐░▌          ▐░▌                                              
                                             ▐░▌ ▐░▌   ▐░▌          ▐░▌                                              
                                             ▐░▌  ▐░▌  ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░▌   ▐░▌ ▐░▌▐░░░░░░░░░░░▌                                              
                                             ▐░▌    ▐░▌▐░▌▐░█▀▀▀▀▀▀▀▀▀                                               
                                             ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                               ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀                                             """
          if int(credits) == 3:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌▐░▌    ▐░▌          ▐░▌                                              
                                             ▐░▌ ▐░▌   ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌                                              
                                             ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌    ▐░▌▐░▌          ▐░▌                                              
                                             ▐░█▄▄▄▄▄█░█░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                               ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) ==4:
               middle ="""
                                               ▄▄▄▄▄▄▄▄▄   ▄         ▄                                               
                                              ▐░░░░░░░░░▌ ▐░▌       ▐░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌▐░▌       ▐░▌                                              
                                             ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌                                              
                                             ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌                                              
                                             ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌                                              
                                             ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌    ▐░▌▐░▌          ▐░▌                                              
                                             ▐░█▄▄▄▄▄█░█░▌          ▐░▌                                              
                                              ▐░░░░░░░░░▌           ▐░▌                                              
                                               ▀▀▀▀▀▀▀▀▀             ▀                                              """
          if int(credits) == 5:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀                                               
                                             ▐░▌▐░▌    ▐░▌▐░█▄▄▄▄▄▄▄▄▄                                               
                                             ▐░▌ ▐░▌   ▐░▌▐░░░░░░░░░░░▌                                              
                                             ▐░▌  ▐░▌  ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌   ▐░▌ ▐░▌          ▐░▌                                              
                                             ▐░▌    ▐░▌▐░▌          ▐░▌                                              
                                             ▐░█▄▄▄▄▄█░█░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                               ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 6:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀                                               
                                             ▐░▌▐░▌    ▐░▌▐░▌                                                        
                                             ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄                                               
                                             ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌                                              
                                             ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌                                              
                                             ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄▄▄█░▌                                              
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                               ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 7:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                                
                                              ▐░░░░░░░░░▌▐░░░░░░░░░░░▌                                               
                                             ▐░█░█▀▀▀▀▀█░▌▀▀▀▀▀▀▀▀▀█░▌                                               
                                             ▐░▌▐░▌    ▐░▌        ▐░▌                                                
                                             ▐░▌ ▐░▌   ▐░▌       ▐░▌                                                 
                                             ▐░▌  ▐░▌  ▐░▌      ▐░▌                                                  
                                             ▐░▌   ▐░▌ ▐░▌     ▐░▌                                                   
                                             ▐░▌    ▐░▌▐░▌    ▐░▌                                                    
                                             ▐░█▄▄▄▄▄█░█░▌   ▐░▌                                                     
                                              ▐░░░░░░░░░▌   ▐░▌                                                      
                                               ▀▀▀▀▀▀▀▀▀     ▀                                                      """
          if int(credits) == 8:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌                                              
                                             ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌                                              
                                             ▐░▌  ▐░▌  ▐░▌ ▐░░░░░░░░░▌                                               
                                             ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌                                              
                                             ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄▄▄█░▌                                              
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                               ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 9:
               middle = """
                                               ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                               
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                             ▐░█░█▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌                                              
                                             ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌                                              
                                             ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌                                              
                                             ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░▌    ▐░▌▐░▌          ▐░▌                                              
                                             ▐░█▄▄▄▄▄█░█░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                              ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌                                              
                                               ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 10:
               middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄                                                 
                                               ▄█░░░░▌    ▐░░░░░░░░░▌                                                
                                              ▐░░▌▐░░▌   ▐░█░█▀▀▀▀▀█░▌                                               
                                               ▀▀ ▐░░▌   ▐░▌▐░▌    ▐░▌                                               
                                                  ▐░░▌   ▐░▌ ▐░▌   ▐░▌                                               
                                                  ▐░░▌   ▐░▌  ▐░▌  ▐░▌                                               
                                                  ▐░░▌   ▐░▌   ▐░▌ ▐░▌                                               
                                                  ▐░░▌   ▐░▌    ▐░▌▐░▌                                               
                                              ▄▄▄▄█░░█▄▄▄▐░█▄▄▄▄▄█░█░▌                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░▌                                                
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀                                                 """
          if int(credits) == 11:
                 middle = """
                                                 ▄▄▄▄         ▄▄▄▄                                                   
                                               ▄█░░░░▌      ▄█░░░░▌                                                  
                                              ▐░░▌▐░░▌     ▐░░▌▐░░▌                                                  
                                               ▀▀ ▐░░▌      ▀▀ ▐░░▌                                                  
                                                  ▐░░▌         ▐░░▌                                                  
                                                  ▐░░▌         ▐░░▌                                                  
                                                  ▐░░▌         ▐░░▌                                                  
                                                  ▐░░▌         ▐░░▌                                                  
                                              ▄▄▄▄█░░█▄▄▄  ▄▄▄▄█░░█▄▄▄                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                               """
          if int(credits) == 12:
                  middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄                                               
                                               ▄█░░░░▌    ▐░░░░░░░░░░░▌                                              
                                              ▐░░▌▐░░▌     ▀▀▀▀▀▀▀▀▀█░▌                                              
                                               ▀▀ ▐░░▌              ▐░▌                                              
                                                  ▐░░▌              ▐░▌                                              
                                                  ▐░░▌     ▄▄▄▄▄▄▄▄▄█░▌                                              
                                                  ▐░░▌    ▐░░░░░░░░░░░▌                                              
                                                  ▐░░▌    ▐░█▀▀▀▀▀▀▀▀▀                                               
                                              ▄▄▄▄█░░█▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 13:
               middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄                                               
                                               ▄█░░░░▌    ▐░░░░░░░░░░░▌                                              
                                              ▐░░▌▐░░▌     ▀▀▀▀▀▀▀▀▀█░▌                                              
                                               ▀▀ ▐░░▌              ▐░▌                                              
                                                  ▐░░▌     ▄▄▄▄▄▄▄▄▄█░▌                                              
                                                  ▐░░▌    ▐░░░░░░░░░░░▌                                              
                                                  ▐░░▌     ▀▀▀▀▀▀▀▀▀█░▌                                              
                                                  ▐░░▌              ▐░▌                                              
                                              ▄▄▄▄█░░█▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 14:
               middle = """
                                                 ▄▄▄▄  ▄         ▄                                                   
                                               ▄█░░░░▌▐░▌       ▐░▌                                                  
                                              ▐░░▌▐░░▌▐░▌       ▐░▌                                                  
                                               ▀▀ ▐░░▌▐░▌       ▐░▌                                                  
                                                  ▐░░▌▐░█▄▄▄▄▄▄▄█░▌                                                  
                                                  ▐░░▌▐░░░░░░░░░░░▌                                                  
                                                  ▐░░▌ ▀▀▀▀▀▀▀▀▀█░▌                                                  
                                                  ▐░░▌          ▐░▌                                                  
                                              ▄▄▄▄█░░█▄▄▄       ▐░▌                                                  
                                             ▐░░░░░░░░░░░▌      ▐░▌                                                  
                                              ▀▀▀▀▀▀▀▀▀▀▀        ▀                                                   """
          if int(credits) == 15:
               middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄                                               
                                               ▄█░░░░▌    ▐░░░░░░░░░░░▌                                              
                                              ▐░░▌▐░░▌    ▐░█▀▀▀▀▀▀▀▀▀                                               
                                               ▀▀ ▐░░▌    ▐░█▄▄▄▄▄▄▄▄▄                                               
                                                  ▐░░▌    ▐░░░░░░░░░░░▌                                              
                                                  ▐░░▌     ▀▀▀▀▀▀▀▀▀█░▌                                              
                                                  ▐░░▌              ▐░▌                                              
                                                  ▐░░▌              ▐░▌                                              
                                              ▄▄▄▄█░░█▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 16:
               middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄                                               
                                               ▄█░░░░▌    ▐░░░░░░░░░░░▌                                              
                                              ▐░░▌▐░░▌    ▐░█▀▀▀▀▀▀▀▀▀                                               
                                               ▀▀ ▐░░▌    ▐░▌                                                        
                                                  ▐░░▌    ▐░█▄▄▄▄▄▄▄▄▄                                               
                                                  ▐░░▌    ▐░░░░░░░░░░░▌                                              
                                                  ▐░░▌    ▐░█▀▀▀▀▀▀▀█░▌                                              
                                                  ▐░░▌    ▐░▌       ▐░▌                                              
                                              ▄▄▄▄█░░█▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                             """
          if int(credits) == 17:
               middle = """
                                                 ▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄                                                  
                                               ▄█░░░░▌ ▐░░░░░░░░░░░▌                                                 
                                              ▐░░▌▐░░▌  ▀▀▀▀▀▀▀▀▀█░▌                                                 
                                               ▀▀ ▐░░▌          ▐░▌                                                  
                                                  ▐░░▌         ▐░▌                                                   
                                                  ▐░░▌        ▐░▌                                                    
                                                  ▐░░▌       ▐░▌                                                     
                                                  ▐░░▌      ▐░▌                                                      
                                              ▄▄▄▄█░░█▄▄▄  ▐░▌                                                       
                                             ▐░░░░░░░░░░░▌▐░▌                                                        
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀                                                        """
          if int(credits) == 18:
               middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄                                               
                                               ▄█░░░░▌    ▐░░░░░░░░░░░▌                                              
                                              ▐░░▌▐░░▌    ▐░█▀▀▀▀▀▀▀█░▌                                              
                                               ▀▀ ▐░░▌    ▐░▌       ▐░▌                                              
                                                  ▐░░▌    ▐░█▄▄▄▄▄▄▄█░▌                                              
                                                  ▐░░▌     ▐░░░░░░░░░▌                                               
                                                  ▐░░▌    ▐░█▀▀▀▀▀▀▀█░▌                                              
                                                  ▐░░▌    ▐░▌       ▐░▌                                              
                                              ▄▄▄▄█░░█▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                               """
          if int(credits) == 19:
               middle = """
                                                 ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄                                               
                                               ▄█░░░░▌    ▐░░░░░░░░░░░▌                                              
                                              ▐░░▌▐░░▌    ▐░█▀▀▀▀▀▀▀█░▌                                              
                                               ▀▀ ▐░░▌    ▐░▌       ▐░▌                                              
                                                  ▐░░▌    ▐░█▄▄▄▄▄▄▄█░▌                                              
                                                  ▐░░▌    ▐░░░░░░░░░░░▌                                              
                                                  ▐░░▌     ▀▀▀▀▀▀▀▀▀█░▌                                              
                                                  ▐░░▌              ▐░▌                                              
                                              ▄▄▄▄█░░█▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                               """
          if int(credits) == 20:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄                                                
                                             ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌                                               
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌                                              
                                                       ▐░▌▐░▌▐░▌    ▐░▌                                              
                                                       ▐░▌▐░▌ ▐░▌   ▐░▌                                              
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░▌  ▐░▌  ▐░▌                                              
                                             ▐░░░░░░░░░░░▌▐░▌   ▐░▌ ▐░▌                                              
                                             ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌    ▐░▌▐░▌                                              
                                             ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄█░█░▌                                              
                                             ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌                                               
                                              ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀                                                """
          if int(credits) == 21:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄                                                   
                                             ▐░░░░░░░░░░░▌  ▄█░░░░▌                                                  
                                              ▀▀▀▀▀▀▀▀▀█░▌ ▐░░▌▐░░▌                                                  
                                                       ▐░▌  ▀▀ ▐░░▌                                                  
                                                       ▐░▌     ▐░░▌                                                  
                                              ▄▄▄▄▄▄▄▄▄█░▌     ▐░░▌                                                  
                                             ▐░░░░░░░░░░░▌     ▐░░▌                                                  
                                             ▐░█▀▀▀▀▀▀▀▀▀      ▐░░▌                                                  
                                             ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░░█▄▄▄                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                              """
          if int(credits) == 22:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                                       ▐░▌          ▐░▌                                              
                                                       ▐░▌          ▐░▌                                              
                                              ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                             ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀                                               
                                             ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                               """
          if int(credits) == 23:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                               
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                                       ▐░▌          ▐░▌                                              
                                                       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌                                              
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░░░░░░░░░░░▌                                              
                                             ▐░░░░░░░░░░░▌ ▀▀▀▀▀▀▀▀▀█░▌                                              
                                             ▐░█▀▀▀▀▀▀▀▀▀           ▐░▌                                              
                                             ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌                                              
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                              
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                               """
          if int(credits) == 24:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ 
                                             ▐░░░░░░░░░░░▌▐░▌       ▐░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
                                                       ▐░▌▐░▌       ▐░▌
                                                       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░░░░░░░░░░░▌
                                             ▐░░░░░░░░░░░▌ ▀▀▀▀▀▀▀▀▀█░▌
                                             ▐░█▀▀▀▀▀▀▀▀▀           ▐░▌
                                             ▐░█▄▄▄▄▄▄▄▄▄           ▐░▌
                                             ▐░░░░░░░░░░░▌          ▐░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀            ▀ 
                                                                       """
          if int(credits) == 25:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
                                                       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
                                                       ▐░▌▐░░░░░░░░░░░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌ ▀▀▀▀▀▀▀▀▀█░▌
                                             ▐░░░░░░░░░░░▌          ▐░▌
                                             ▐░█▀▀▀▀▀▀▀▀▀           ▐░▌
                                             ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                       """
          if int(credits) == 26:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
                                                       ▐░▌▐░▌          
                                                       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░░░░░░░░░░░▌
                                             ▐░░░░░░░░░░░▌▐░█▀▀▀▀▀▀▀█░▌
                                             ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌
                                             ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                       """

          if int(credits) == 27:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
                                                       ▐░▌         ▐░▌ 
                                                       ▐░▌        ▐░▌  
                                              ▄▄▄▄▄▄▄▄▄█░▌       ▐░▌   
                                             ▐░░░░░░░░░░░▌      ▐░▌    
                                             ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     
                                             ▐░█▄▄▄▄▄▄▄▄▄     ▐░▌      
                                             ▐░░░░░░░░░░░▌   ▐░▌       
                                              ▀▀▀▀▀▀▀▀▀▀▀     ▀        
                                                                       """
          if int(credits) == 28:
               middle = """

                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
                                                       ▐░▌▐░▌       ▐░▌
                                                       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌ ▐░░░░░░░░░▌ 
                                             ▐░░░░░░░░░░░▌▐░█▀▀▀▀▀▀▀█░▌
                                             ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌
                                             ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                       """
          if int(credits) == 29:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
                                                       ▐░▌▐░▌       ▐░▌
                                                       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░░░░░░░░░░░▌
                                             ▐░░░░░░░░░░░▌ ▀▀▀▀▀▀▀▀▀█░▌
                                             ▐░█▀▀▀▀▀▀▀▀▀           ▐░▌
                                             ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                       """

          if int(credits) == 30:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄  
                                             ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌ 
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌
                                                       ▐░▌▐░▌▐░▌    ▐░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌
                                             ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌
                                                       ▐░▌▐░▌    ▐░▌▐░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄█░█░▌
                                             ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌ 
                                              ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀  
                                                                       """
          if int(credits) == 31:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄     
                                             ▐░░░░░░░░░░░▌  ▄█░░░░▌    
                                              ▀▀▀▀▀▀▀▀▀█░▌ ▐░░▌▐░░▌    
                                                       ▐░▌  ▀▀ ▐░░▌    
                                              ▄▄▄▄▄▄▄▄▄█░▌     ▐░░▌    
                                             ▐░░░░░░░░░░░▌     ▐░░▌    
                                              ▀▀▀▀▀▀▀▀▀█░▌     ▐░░▌    
                                                       ▐░▌     ▐░░▌    
                                              ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░░█▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                       """
          if int(credits) == 32:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
                                                       ▐░▌          ▐░▌
                                              ▄▄▄▄▄▄▄▄▄█░▌          ▐░▌
                                             ▐░░░░░░░░░░░▌ ▄▄▄▄▄▄▄▄▄█░▌
                                              ▀▀▀▀▀▀▀▀▀█░▌▐░░░░░░░░░░░▌
                                                       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
                                              ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                       """

          if int(credits) > 32:
               middle = """
                                              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                             ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
                                             ▐░▌       ▐░▌▐░▌       ▐░▌
                                             ▐░▌       ▐░▌▐░▌       ▐░▌
                                             ▐░▌       ▐░▌▐░▌       ▐░▌
                                             ▐░▌       ▐░▌▐░▌       ▐░▌
                                             ▐░▌       ▐░▌▐░▌       ▐░▌
                                             ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
                                             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                                              ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """


          top = """
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """

          if int(credits) >= 2:
               bottom = """
                          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄                            
                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌                           
                         ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀                            
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌                                     
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄                            
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌                           
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌                           
                         ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌          ▐░▌                           
                         ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌                           
                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌                           
                          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀                            
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
"""


          elif int(credits) == 0:
               bottom = """
 ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌
▐░▌          ▐░▌       ▐░▌          ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ 
                                                                                                             
                                                                                                       
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                     """
          else:
               bottom = """
                                    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄                               
                                   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌                              
                                   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌                              
                                   ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌                              
                                   ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌                              
                                   ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌                              
                                   ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌                              
                                   ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌                              
                                   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌                              
                                   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌                              
                                    ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀                               
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                     """
          print(top)
          print(middle)
          print(bottom)
          return

def  ParseConf():
     global GlobStart
     global GlobExit

     try:
          with open(DirData+"sneaver.conf","r") as conf:
               for setting in conf:
                    if "ExitEmu" in setting and "J00:B" in setting:
                         GlobExit = setting.split(" = ExitEmu")[0].replace("J00:B","")
                    if "Joypad1 Start" in setting:
                         GlobStart = setting.split(" = Joypad1 Start")[0].replace("J00:B","")
     except Exception as e:
          Pfig("Error:"+str(e))
          GetOut()


def ManualExit():
     pygame.init()
     Loop = 0
     PushedCnt = 0
     Exit = GlobExit

     try:
         joypad1 = pygame.joystick.Joystick(0)
         joypad1.init()
     except Exception as e:
         if str(e) == "Invalid joystick device number":
            Pfig("\nNo gamepad have been found .\n\nIs it connected ? \nHere is what iv found :\n\n")
            for device in devices:
                print(device)
         else:
            Pfig("\nError :"+str(e))
     try:
        while Loop <= 200:
          events = pygame.event.get()
          for event in events:

              try:
                   checksnes9x= int(subprocess.check_output(["pidof","-s","snes9x"]))
              except Exception as e:
                         if "returned non-zero exit status 1" in str(e):
                              return False
                         else:
                              Pfig("Proc/Status Error:"+str(e))

              if event.type == pygame.JOYBUTTONUP:
                         if str(event.button) == str(Exit): 
                              if PushedCnt >= 3:
                                        return True
                              else:
                                        PushedCnt = PushedCnt + 1
              else:
                    Loop = Loop + 1

     except Exception as e:
          Pfig("Error:"+str(e))

     return False


def PressStart():
     global CHECKPOINT

     CHECKPOINT = 0

     pygame.init()
     Start = GlobStart

     time.sleep(1)
     print("""


                                                                                                                                                            
                                                                                                                                                            
                                                                                                                                                            
                                                                                                                                                            
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
              ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄         
             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌        
             ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀         
             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌               ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌             
 ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░▌ ▀▀▀▀▀▀▀▀▀▀▀ 
             ▐░▌          ▐░▌     ▐░▌  ▐░▌                    ▐░▌          ▐░▌               ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌             
             ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌      ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░▌      ▐░▌      ▐░▌             
             ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌             
              ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀         ▀       ▀              
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 

""")




     try:
         joypad1 = pygame.joystick.Joystick(0)
         joypad1.init()
     except Exception as e:
         if str(e) == "Invalid joystick device number":
            Pfig("\nNo gamepad have been found .\n\nIs it connected ? \nHere is what iv found :\n\n")
            for device in devices:
                print(device)
         else:
            Pfig("\nError :"+str(e))
         GetOut()
     try:
        while True: 
          events = pygame.event.get()
          for event in events:
              if event.type == pygame.JOYBUTTONUP:
                    if str(event.button) == str(Start): 
                         GifLauncher("NewGame")
                         return
     except Exception as e:
          Pfig("Error:"+str(e))
          GetOut()

def Configuration():
     next = False

     joymap = {
         "Start":"",
         "Select":"",
         "Up":"",
         "Down":"",
         "Right":"",
         "Left":"",
         "BtnA":"",
         "BtnB":"",
         "BtnX":"",
         "BtnY":"",
         "BtnL":"",
         "BtnR":"",
         "BtExit":""
          }

     joymap2 = {
         "Start":"",
         "Select":"",
         "Up":"",
         "Down":"",
         "Right":"",
         "Left":"",
         "BtnA":"",
         "BtnB":"",
         "BtnX":"",
         "BtnY":"",
         "BtnL":"",
         "BtnR":"",
         "BtExit":""
          }

     if os.path.exists("/dev/input/js0") == False and os.path.exists("/dev/input/js1") == False:
            Pfig("\nNo gamepad have been found .\n\nIs it connected ? \nHere is what iv found :\n\n")
            for device in devices:
                print(device)
            Pfig("\nIf this error persist you may have to edit sneaver.conf yourself sorry.\n")
            GetOut()


     Pfig("\nOk lets Configure Joypad 1:\n\n")


     if os.path.exists("/dev/input/js0") == True:
       for button,code in joymap.items():
        next = False
        if str(button) == "BtExit":
               Pfig("Please press a button to close Snes9x emulator.")
        else:
             Pfig("Please press a button for "+ str(button) + " :\n\n")
        proc = subprocess.Popen(["unbuffer","jstest", "--select","/dev/input/js0"],bufsize=1, universal_newlines=True, stdout=subprocess.PIPE)
        while next == False: 
          for line in proc.stdout:
               proc.send_signal(signal.SIGSTOP)
               if "type 1," in line or "type 2," in line:
                    if "value 1" in line:
                              p = re.compile("number (\d+)?,",)
                              num = p.findall(line)[0]
                              print("\nYou've just pressed Button Nbr :"+num+"\n")
                              confirm = input("\nIs this correct ?(y/n) :")
                              try:
                                   if "y" in confirm.lower():
                                        Pfig("\nMapping key ..\n\n")
                                        joymap[button] = str(num)
                                        next = True
                                        proc.terminate()
                                        break
                                   else:
                                        Pfig("\nOk then Please press a button for "+ str(button) + ": \n\n")
                                        proc.send_signal(signal.SIGCONT)
                              except:
                                        Pfig("Ok then Please press a button for  "+ str(button) + ":\n\n")
                                        proc.send_signal(signal.SIGCONT)

                    else:
                         proc.send_signal(signal.SIGCONT)
               else:
                    proc.send_signal(signal.SIGCONT) 


       Pfig("\nOk here is the config for Joypad 1:\n\n")
       for button,code in joymap.items():
          print("Button %s = code %s"%(button,code))
       print("\n\n")

     if os.path.exists("/dev/input/js1") == True:
          question = input("Do you want to configure Joypad 2(Y/N):")
     else:
          question = "n"

     if "y" in question.lower():

       for button,code in joymap2.items():
        next = False
        if str(button) == "BtExit":
               Pfig("Please press a button to close Snes9x emulator.")
        else:
             Pfig("Please press a button for "+ str(button) + " :\n\n")
        proc = subprocess.Popen(["unbuffer","jstest", "--select","/dev/input/js1"],bufsize=1, universal_newlines=True, stdout=subprocess.PIPE)
        while next == False: 
          for line in proc.stdout:
               proc.send_signal(signal.SIGSTOP)
               if "type 1," in line or "type 2," in line:
                    if "value 1" in line:
                              p = re.compile("number (\d+)?,",)
                              num = p.findall(line)[0]
                              print("\nYou've just pressed Button Nbr :"+num+"\n")
                              confirm = input("\nIs this correct ?(y/n) :")
                              try:
                                   if "y" in confirm.lower():
                                        Pfig("\nMapping key ..\n\n")
                                        joymap2[button] = str(num)
                                        next = True
                                        proc.terminate()
                                        break
                                   else:
                                        Pfig("\nOk then Please press a button for "+ str(button) + ": \n\n")
                                        proc.send_signal(signal.SIGCONT)
                              except:
                                        Pfig("Ok then Please press a button for  "+ str(button) + ":\n\n")
                                        proc.send_signal(signal.SIGCONT)

                    else:
                         proc.send_signal(signal.SIGCONT)
               else:
                    proc.send_signal(signal.SIGCONT)


       print("\nOk here are the config for Joypad 2:\n\n")
       for button,code in joymap2.items():
               print("Button %s = code %s"%(button,code))
     else:
          joymap2 = joymap
     print()

     Snes9xConf = """#-----------------------------------------
# snes9x.conf : Snes9x Configuration file
#   With Real Chunks Of Sneaver In It
#-----------------------------------------

[ROM] 

LoROM = FALSE
HiROM = FALSE
PAL = FALSE
NTSC = FALSE
Interleaved2 = FALSE
InterleaveGD24 = FALSE
Cheat = TRUE
Patch = TRUE
[Sound]

Sync= FALSE
16BitSound = TRUE
Stereo = TRUE
ReverseStereo = FALSE
Rate = 32000
InputRate = 32000
Mute = FALSE

[Display]
HiRes = FALSE
Transparency = TRUE
GraphicWindows = FALSE
DisplayFrameRate = FALSE
DisplayWatchedAddresses = FALSE
DisplayInput = FALSE
DisplayFrameCount = FALSE
MessagesInImage = FALSE
MessageDisplayTime = 120

[Settings]
BSXBootup = FALSE
# FrameTime = 
FrameSkip = Auto
TurboMode = FALSE
TurboFrameSkip = 15
MovieTruncateAtEnd = TRUE
MovieNotifyIgnored = FALSE
WrongMovieStateProtection = FALSE
StretchScreenshots = 1
SnapshotScreenshots = TRUE
DontSaveOopsSnapshot = FALSE
AutoSaveDelay = 3

[Controls]
MouseMaster = False
SuperscopeMaster = False
JustifierMaster = False
MP5Master = FALSE
AllowLeftRight = FALSE
Port1 = pad1
Port2 = pad2
Mouse1Crosshair = 1 White/Black
Mouse2Crosshair = 1 White/Black
SuperscopeCrosshair = 2 White/Black
Justifier1Crosshair = 4 Blue/Black
Justifier2Crosshair = 4 MagicPink/Black

[Hack]
EnableGameSpecificHacks = TRUE
AllowInvalidVRAMAccess = FALSE
SpeedHacks = FALSE
HDMATiming = 100

[Netplay]
Enable = FALSE
Port = 6096
Server = ""

[DEBUG]
Debugger = TRUE
Trace = TRUE

[Unix]
BaseDir = """+str(DirData)+"""
EnableGamePad = True
PadDevice1 = /dev/input/js0
PadDevice2 = /dev/input/js1
PadDevice3 = (null)
PadDevice4 = (null)
PadDevice5 = (null)
PadDevice6 = (null)
PadDevice7 = (null)
PadDevice8 = (null)
ThreadSound = FALSE
SoundBufferSize = 100
SoundFragmentSize = 2048
# SoundDevice = 
ClearAllControls = FALSE

[Unix/X11]
SetKeyRepeat = TRUE
VideoMode = 1

[Unix/X11 Controls]
#Controller 1
J00:Axis1 = Joypad1 Axis Up/Down T=50%
J00:Axis0 = Joypad1 Axis Left/Right T=50%
J00:B"""+str(joymap["Up"])+""" = Joypad1 Up
J00:B"""+str(joymap["Down"])+""" = Joypad1 Down
J00:B"""+str(joymap["Left"])+""" = Joypad1 Left
J00:B"""+str(joymap["Right"])+""" = Joypad1 Right
J00:B"""+str(joymap["BtnA"])+""" = Joypad1 A
J00:B"""+str(joymap["BtnB"])+""" = Joypad1 B
J00:B"""+str(joymap["BtnX"])+""" = Joypad1 X
J00:B"""+str(joymap["BtnY"])+""" = Joypad1 Y
J00:B"""+str(joymap["BtnL"])+""" = Joypad1 L
J00:B"""+str(joymap["BtnR"])+""" = Joypad1 R
J00:B"""+str(joymap["Select"])+""" = Joypad1 Select
J00:B"""+str(joymap["Start"])+""" = Joypad1 Start
J00:B"""+str(joymap["BtExit"])+""" = ExitEmu


#Controller 2
J01:Axis1 = Joypad2 Axis Up/Down T=50%
J01:Axis0 = Joypad2 Axis Left/Right T=50%
J01:B"""+str(joymap2["Up"])+""" = Joypad2 Up
J01:B"""+str(joymap2["Down"])+""" = Joypad2 Down
J01:B"""+str(joymap2["Left"])+""" = Joypad2 Left
J01:B"""+str(joymap2["Right"])+""" = Joypad2 Right
J01:B"""+str(joymap2["BtnA"])+""" = Joypad2 A
J01:B"""+str(joymap2["BtnB"])+""" = Joypad2 B
J01:B"""+str(joymap2["BtnX"])+""" = Joypad2 X
J01:B"""+str(joymap2["BtnY"])+""" = Joypad2 Y
J01:B"""+str(joymap2["BtnL"])+""" = Joypad2 L
J01:B"""+str(joymap2["BtnR"])+""" = Joypad2 R
J01:B"""+str(joymap2["Select"])+""" = Joypad2 Select
J01:B"""+str(joymap2["Start"])+""" = Joypad2 Start
J01:B"""+str(joymap2["BtExit"])+""" = ExitEmu 

K00:Escape = ExitEmu
K00:Insert = QuickSave000

#Full config list :  https://github.com/snes9xgit/snes9x/blob/master/unix/snes9x.conf.default
"""
     RwFile("sneaver.conf",Snes9xConf,"w")
     GetOut()

def Rename(name,srcdir):

  badchar= ["(",")","[","!","]"," ","_","--","'",'"',",","&"]

  mv = False
  for char in badchar:
     if char in name:
          mv = True
  if mv == True:
     print("Renaming : ",name)
     newname = name.replace("&","-").replace("(","-").replace(")","-").replace("[","-").replace("!","-").replace("]","").replace(" ","-").replace("_","-").replace("'","-").replace('"',"-").replace(",","-").replace("--","-")
     newname = newname.replace("---","-").replace("--","-")
     os.rename(srcdir+name,srcdir+newname)
     print("\nNew Name is : ",newname)


def ScreenResize(mode):

     global OLDSCREEN
     global NEWRES

     if mode == "change":
         OLDSCREEN = ""
         xrandr = subprocess.Popen("xrandr",shell=True,stdout=subprocess.PIPE)
         xout = str(xrandr.communicate()[0])
         reslist = []
         NEWRES = ""
         goodone = False

         if "connected primary" in xout:
              device = str(xout.split("connected primary")[0].split("\\n")[-1]).replace(" ","")
              xit = "".join(xout.split("connected primary")[1]).split("\\n")

         for item in xit:
              if item.startswith(" ")== True :

                   if "(" not in item:

                        if "*" in item:
                             tmp = item.split("x")
                             height = tmp[0]
                             width = tmp[1].split(" ")[0]
                             res = str(str(height)+"x"+str(width)).replace(" ","")
                        else:

                             if "640x480" in item:
                                  newscreen = "xrandr --output "+device+" --mode 640x480"
                                  NEWRES = "640x480"
                                  goodone = True
                             else:
                                  regex = re.compile(r'\d+[x]\d+')
                                  bingo =regex.search(item)

                                  if bingo:
                                       if not bingo.group() in reslist:
                                            reslist.append(bingo.group())
              else:
                   break

         if goodone == False:
              sorting =[]
              for resolution in reslist:
                   tmp = resolution.split("x")[0]
                   sorting.append(tmp)
              sorting.sort(key=int)
              minwidth = sorting[0]

              for resolution in reslist:
                   if resolution.startswith(minwidth) == True:
                        newscreen = "xrandr --output "+device+" --mode "+ str(resolution)
                        NEWRES = str(resolution)
                        break


         Pfig("\n-Saving Current Screen Config-\n")
         OLDSCREEN = "xrandr --output "+device+" --mode "+res
         Pfig(OLDSCREEN)


         Pfig("\n-Changing Screen Resolution now-\n")
         Pfig(newscreen)
         print()

         xrandr = subprocess.Popen(str(newscreen),shell=True)

     if mode == "revert":
         NEWRES = ""
         xrandr = subprocess.Popen(str(OLDSCREEN),shell=True)

     if mode =="height":
         height = "640"
         xrandr = subprocess.Popen("xrandr",shell=True,stdout=subprocess.PIPE)
         xout = str(xrandr.communicate()[0])

         if "connected primary" in xout:
              device = str(xout.split("connected primary")[0].split("\\n")[-1]).replace(" ","")
              xit = "".join(xout.split("connected primary")[1]).split("\\n")

         for item in xit:
              if item.startswith(" ")== True :

                   if "(" not in item:

                        if "*" in item:
                             tmp = item.split("x")
                             height = tmp[0]
         return height

def BlackList():
          global BADROMS


          BADROMS = RwFile("bad.roms",None,"r")
          try:
               Pfig(str(len(BADROMS)) + " Roms Blacklisted .\n\n")
          except:
               BADROMS = []
               Pfig("0 Roms Blacklisted .\n\n")

def RanDef():


     if SEARCH is True:
          romret = ""
          romfiles = []
          movfiles = []
          DirChosen = []
          FOUNDONE = False

          if RECORD is True:

               if IGNOREBAD == False:
                         BlackList()

               for dirpath, dirnames, filenames in os.walk(DirMovies):
                    for name in filenames:
                         if name.endswith(".sfc") or name.endswith(".smc"):
                              if SearchRom.lower() in name.lower():
                                   if NOJP == True:
                                        if not "-J-" in name and name not in BADROMS:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True
                                   elif NOEU == True:
                                        if not "-E-" in name and name not in BADROMS:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True
                                   elif NOUS == True:
                                        if not "-U-" in name and name not in BADROMS:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True
                                   elif JP == True:
                                        if "-J-" in name and name not in BADROMS:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True
                                   elif EU == True:
                                        if "-E-" in name and name not in BADROMS:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True
                                   elif US == True:
                                        if "-U-" in name and name not in BADROMS:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True
                                   else:
                                             romfiles.append(name)
                                             DirChosen.append(dirpath+"/")
                                             FOUNDONE = True

          if REPLAY == True:
                 MovLst = [i for i in os.listdir(DirMovies)]
                 for dir in MovLst:
                    if SearchRom.lower() in dir.lower():
                         FOUNDONE = True
                         currentdir = DirMovies+dir+"/"
                         try:
                              for i in os.listdir(currentdir):
                                   if i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi"):
                                             print(currentdir+i)
                                             movfiles.append(currentdir+i)
                         except Exception as e:
                              Pfig("\n\nError:"+str(e))
                              print()
                              pass

                 if len(movfiles) > 0:
                    try:
                         random.shuffle(movfiles)

                         return movfiles,DirChosen

                    except Exception as e:
                         Pfig("Error:"+str(e))
                         pass
                 else:
                        Pfig("\n\nHaven't Found any Movie Containing %s .\n\n"%SearchRom)
                        GetOut()





          if RECORD == True and FOUNDONE == True:
                    try:
                         rnd = random.randint(0,len(romfiles)-1)
                         romret = romfiles[rnd]

                         return romret,DirChosen[rnd]

                    except Exception as e:
                         Pfig("\n\nError:"+str(e))
                         pass
          else:
                        Pfig("\n\nHaven't Found any Game Containing the word : %s \n\n"%SearchRom)
                        GetOut()

     if SEARCH is False:

          while True:

               romret = ""
               romfiles = []
               movfiles = []
               FOUNDONE = False


               MovLst = [i for i in os.listdir(DirMovies)]

               try:
                    rnd = random.randint(0,len(MovLst)-1)
                    DirChosen = DirMovies+MovLst[rnd]
               except:
                    Pfig("Can't find anything !!!\nWhere am i ?\nPlease check what's in the Movies Folder ..")
                    sys.exit(0)


               files = os.listdir(DirChosen)

               for i in files:

                 if RECORD == True:

                    if IGNOREBAD == False:
                         BlackList()

                    if i.endswith(".sfc") or i.endswith(".smc"):
                         if NOJP == True:
                              if not "-J-" in i and i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True
                         elif NOEU == True:
                              if not "-E-" in i and i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True
                         elif NOUS == True:
                              if not "-U-" in i and i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True
                         elif JP == True:
                              if "-J-" in i and i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True
                         elif EU == True:
                              if "-E-" in i and i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True
                         elif US == True:
                              if "-U-" in i and i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True
                         else:
                             if i not in BADROMS:
                                   romfiles.append(i)
                                   FOUNDONE = True

               if REPLAY == True:
                    for dir in MovLst:
                         currentdir = DirMovies+dir+"/"
                         try:
                              for i in os.listdir(currentdir):
                                   if i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi"):
                                        print(currentdir+i)
                                        movfiles.append(currentdir+i)
                         except Exception as e:
                              Pfig("\n\nError:"+str(e))
                              print()
                              pass



               if RECORD == True and FOUNDONE == True:
                    try:
                         rnd = random.randint(0,len(romfiles)-1)
                         romret = romfiles[rnd]

                         return romret,DirChosen

                    except Exception as e:
                         Pfig("\n\nError:"+str(e))
                         pass


               if REPLAY == True :
                 if len(movfiles) > 0:
                    try:
                         random.shuffle(movfiles)

                         return movfiles,DirChosen

                    except Exception as e:
                         Pfig("Error:"+str(e))
                         pass
                 else:
                        Pfig("\n\nHaven't Found any Movie\n\nUse sneaver -record to fill the playlist.\n\n")
                        GetOut()



##PressStart#
signal.signal(signal.SIGINT, signal_handler)

if 1 == 1:
     print()

     ##Renaming
     MovLst = [i for i in os.listdir(DirMovies)]
     for name in MovLst:
                    Rename(name,DirMovies)
     MovLst = [i for i in os.listdir(DirMovies)]
     for currentdir in MovLst:
               files = os.listdir(DirMovies+currentdir)
               for name in files:
                    Rename(name,DirMovies+currentdir+"/")

     if CONFIG == True:
          Configuration()
     elif os.path.exists(DirData+"sneaver.conf") == False:
          Configuration()

     if REPLAY == True:

       Container,DirChosen = RanDef()
       print("Found "+str(len(Container))+" Movies !\n\n")

       playlist = ""

       for movfile in Container:

          playlist += str(movfile) + " "


       cmd = "cvlc --fullscreen --play-and-exit "+ str(playlist)

       Pfig("\nLaunching : \n")
       print(cmd)

       cvlc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       output,error = cvlc.communicate()
       cout= output.decode()

       if "filesystem access error:" in cout:
                    Pfig("!!!!!!!!!!!\nError while Trying to Open File!!\n!!!!!!!!!!!\n")
                    cvlc.terminate()

       GetOut()

##


     if RECORD == True:


          ParseConf()
          time.sleep(1)
          LoadCoin("firstload")
          while True:
              WaitForMe('snes9x')
              WaitForMe('ffmpeg')
              Container,DirChosen = RanDef()

              WALLET = int(WALLET)

              InsertCoin(WALLET)

              LoadCoin("printcoins")

              WaitForMe("ffmpeg")

              Pfig("\nSneaver chose to open :"+str(DirChosen))

              time.sleep(1)

              PressStart()

              ScreenResize("change")

              newmovie =str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))+".mkv"

              Pfig("\n-Recording now-\n"+(newmovie))

              cmd = "/usr/bin/padsp snes9x -nostdconf -conf "+ str(DirData)+"sneaver.conf -maxaspect -fullscreen -xvideo "+ str(DirChosen)+ "/" + str(Container)

              Pfig("\n-Launching Snes9x-\n")
              print(cmd)
              sneaver = subprocess.Popen(cmd,shell=True)

              cmd = "padsp ffmpeg -loglevel error -f alsa -ac 1 -ar 32000 -i pulse -f x11grab -r 24 -s "+str(NEWRES)+" -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 "+str(DirChosen)+"/"+str(newmovie)

              Pfig("\n-Recording Screen-\n")
              print(cmd)
              ffmpeg = subprocess.Popen(cmd,shell=True)

              while True:
                   WaitForMe('snes9x')

                   if ERROR == True:
                         GifLauncher("Error")
                         ERROR = False
                         WALLET = WALLET + 1
                         RwFile("bad.roms",str(Container),"a")
                         Pfig("Rom: "+str(Container)+" Blacklisted..")
                         
                         if RESPAWN is True:
                              if os.path.exists(DirSaves+str(Container).replace(".smc",".000"))is True: 
                                   cmd = "/usr/bin/padsp snes9x -nostdconf -conf "+ str(DirData)+"sneaver.conf -maxaspect -fullscreen -xvideo "+ str(DirChosen)+ "/" + str(Container) + " -loadsnapshot " + str(DirSaves+str(Container).replace(".smc",".000"))
                                   Pfig("-Respawn using QuickSave.000-")
                                   print(str(cmd)+"\n")
                                   sneaver = subprocess.Popen(cmd,shell=True)
                              elif os.path.exists(DirSaves+str(Container).replace(".smc",".oops"))is True:
                                   cmd = "/usr/bin/padsp snes9x -nostdconf -conf "+ str(DirData)+"sneaver.conf -maxaspect -fullscreen -xvideo "+ str(DirChosen)+ "/" + str(Container) + " -loadsnapshot " + str(DirSaves+str(Container).replace(".smc",".oops"))
                                   Pfig("\n-Respawn using AutoSave.oops-\n")
                                   print(str(cmd)+"\n")
                                   sneaver = subprocess.Popen(cmd,shell=True)
                              else:
                                   Pfig("\n-Error: [RESPAWN] No Auto-Save Found.-\n")
                                   break
                         else:
                              break
                   break 

              pkill = subprocess.Popen("pkill ffmpeg",shell=True)
              WaitForMe('ffmpeg')
              time.sleep(1)

              Pfig("\n-Your game session has been recorded with success !-\n")
              Pfig("\n-Changing back Screen Resolution-\n"+str(OLDSCREEN))

              ScreenResize("revert")

              Pfig("\n-Now let's encode the video to save some disk space..-\n")


              GifLauncher("Loading")

              cmd ="ffmpeg -i "+str(DirChosen)+"/"+str(newmovie)+" -acodec libvorbis -ab 128k -ac 2 -vcodec libx264 -preset superfast -crf 32 -maxrate 400k -bufsize 400k -threads 1 -stats "+str(DirChosen)+"/"+str(newmovie).replace(".mkv",".mp4")
              print(cmd)
#              ffmpeg = subprocess.Popen(cmd,shell=True)
              ffmpeg = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
              output,error = ffmpeg.communicate()
              fout = output.decode()

              if "No such file or directory" in fout:
                    Pfig("!!!!!!!!!!!\nError while Trying to Open File!!\n!!!!!!!!!!!\n")
                    ffmpeg.terminate()
                    cmd = "pkill ffmpeg"
                    pkill = subprocess.Popen(cmd,shell=True)

              WaitForMe("ffmpeg")

              time.sleep(1)

              if KILLLOAD != "":
                   cmd = "pkill " + KILLLOAD
                   pkill = subprocess.Popen(cmd,shell=True)
                   KILLLOAD = ""

              Pfig("\n-Finished-\n")
              Pfig("\n-Done Encoding "+str(newmovie).replace(".mkv",".mp4")+"-\n-Removing old "+str(newmovie)+"-\n\n")
              try:
                   os.remove(str(DirChosen)+"/"+str(newmovie))
              except:
                    Pfig("\n Failed to remove file ..\n")


##TouchDown##


GetOut()
