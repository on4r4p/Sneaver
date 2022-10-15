#!/usr/bin/python3
from shutil import which, rmtree
from pyfiglet import Figlet
from inputs import devices
from PIL import Image
from pynput.keyboard import Key, Controller
import os, sys, random, shutil, subprocess, datetime, re, time, signal, pygame

ScriptDir = os.path.dirname(os.path.abspath(__file__))
DirMovies = ScriptDir + "/Movies/"
DirData = ScriptDir + "/Data/"
DirCheat = DirData + "cheat/"
DirGif = DirData + "Gifs/"
DirSaves = DirData + "savestate/"
Category = [
    "action",
    "adventure",
    "fighting",
    "platform",
    "puzzle",
    "racing",
    "rpg",
    "shooter",
    "simulation",
    "sport",
    "strategy",
]

keyboard = Controller()
CrashDate = ""
LastCrashDate = ""
CrashRom = ""
CrashCounter = 0
GoodToGo = False
RomIndex = 0
WALLET = 0
KILLLOAD = ""
OLDSCREEN = ""
NEWSCREEN = ""
NEWRES = ""
SEGFAULTLIST = []
LASTSEGFAULT = ""
GlobStart = ""
GlobSelect = ""
GlobExit = ""
SearchRom = ""
BADROMS = []
LASTBAD = ""
IGNOREBAD = False
GENRE = False
SEARCH = False
ERROR = False
GODMODE = False
LASTONE = False
CHEAT = ""
CHEATER = False
NOJP = False
NOEU = False
NOUS = False
JP = False
EU = False
US = False
NOLENCHECK = False
COMPRESS = False
RESPAWN = False
SMARTCRASH = False
CHANGEGAME = False
RECORD = False
REPLAY = False
CONFIG = False
ONESHOT = False


print(
    """
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
"""
)
time.sleep(1)


def signal_handler(sig, frame):
    if OLDSCREEN != "":
        ScreenResize("revert")
    GetOut()


def RwFile(filename, data, mode):

    try:

        if "roms." in filename and mode == "r":
            with open(DirData + filename, mode) as file:
                lines = file.readlines()
                lines = [l.strip() for l in lines]
                return lines

        if filename == "cheats.bml":
            if mode == "r":
                with open(DirCheat + filename, mode) as file:
                    lines = file.readlines()
                    lines = "\n".join([l.strip() for l in lines]).split("cartridge")
                    return lines

        if filename.endswith(".cht"):
            if mode == "r":
                with open(DirCheat + filename, mode) as file:
                    lines = file.read()
                    return lines
            if mode == "w":
                with open(DirCheat + filename, mode) as file:
                    file.write(str(data))

        if filename == "bad.roms":
            if mode == "r":
                with open(DirData + filename, mode) as file:
                    lines = file.readlines()
                    lines = [l.strip() for l in lines]
                    return lines
            else:
                FoundBad = False
                with open(DirData + filename, "a+") as file:
                    lines = file.readlines()
                    lines = [l.strip() for l in lines]
                    for item in lines:
                        if str(data) == item:
                            FoundBad = True
                    if FoundBad == False:
                        file.write("\n" + str(data))
        if filename == "compress.video":
            if mode == "r":
                with open(DirData + filename, mode) as file:
                    lines = file.readlines()
                    lines = [l.strip() for l in lines]
                    return lines
            elif mode == "a+":
                with open(DirData + filename, mode) as file:
                    file.write("\n" + str(data))
            elif mode == "w":
                with open(DirData + filename, mode) as file:
                    file.close()

        if filename == "last.played" and mode == "r":
            ctn = None
            dch = None
            with open(DirData + filename, mode) as file:
                lines = file.readlines()
                lines = [l.strip() for l in lines]
                for l in lines:
                    if "DirChosen=" in l:
                        dch = l.split("DirChosen=")[1]
                    if "Container=" in l:
                        ctn = l.split("Container=")[1]

                return (ctn, dch)

        else:

            with open(DirData + filename, mode) as file:
                if mode == "w":
                    file.write(str(data))
                if mode == "r":
                    for l in file:
                        return l
    except Exception as e:
        print("Error! : " + str(e))


def Segfault():
    global LASTSEGFAULT
    global SEGFAULTLIST
    dmesg = str(subprocess.check_output(["dmesg"])).split("\\n")
    for line in dmesg:
        if "snes9x" in line and "segfault at" in line:
            if line not in SEGFAULTLIST:
                SEGFAULTLIST.append(line)
    try:
        if len(SEGFAULTLIST) > 0 and LASTSEGFAULT in SEGFAULTLIST:
            Snesisdead = False
        elif LASTSEGFAULT == "":
            Snesisdead = False
        else:
            print("LASTSEGFAULT:", LASTSEGFAULT)
            print("SEGFAULTLIST:", SEGFAULTLIST)
            Snesisdead = True
        if len(SEGFAULTLIST) > 0:
            LASTSEGFAULT = SEGFAULTLIST[-1]

    except Exception as e:
        Pfig("digital", "Error LASTSEGFAULT", e)
        Snesisdead = False
    return Snesisdead


def Pfig(txt):
    Fig = Figlet(font="digital")
    print(Fig.renderText(txt))
    return


def AutoSaveState():
    global CHECKPOINT

    if CHECKPOINT >= 10:
        CHECKPOINT = 0

        print("\n!!AutoSaveState!!\n")

        while True:
            if not os.path.exists(
                DirSaves
                + str(Container).replace(".smc", ".000").replace(".sfc", ".000")
            ):
                print("\n-AutoSaving-\n")
                keyboard.press(Key.insert)
                time.sleep(0.5)
                keyboard.release(Key.insert)
                time.sleep(1)
            else:
                try:
                    shutil.copy(
                        DirSaves
                        + str(Container)
                        .replace(".smc", ".000")
                        .replace(".sfc", ".000"),
                        DirSaves
                        + str(Container)
                        .replace(".smc", ".old.000")
                        .replace(".sfc", ".old.000"),
                    )
                    os.remove(
                        DirSaves
                        + str(Container).replace(".smc", ".000").replace(".sfc", ".000")
                    )
                    print(
                        "-Saved a copy of autosave :",
                        DirSaves
                        + str(Container)
                        .replace(".smc", ".000")
                        .replace(".sfc", ".000"),
                        DirSaves
                        + str(Container)
                        .replace(".smc", ".old.000")
                        .replace(".sfc", ".old.000"),
                    )
                    break
                except Exception as e:
                    Pfig("Error: " + str(e))
                Pfig("\n-AutoSaved-\n")
        Pfig("\n-AutoSaved-\n")


#     else:
#          print("\n\nDebug CHECKPOINT : "+str(CHECKPOINT))


def WaitForMe(process):

    global ERROR
    global CHECKPOINT
    if process != "snes9x":
        while True:
            try:
                checkproc = int(subprocess.check_output(["pidof", "-s", process]))
                time.sleep(1)
            except Exception as e:
                if "returned non-zero exit status 1" in str(e):
                    # Pfig("-Process %s has ended-" % process)
                    return
                else:
                    Pfig("Error WaitForMe:" + str(e))

    else:
        while True:
            try:
                checksnes9x = int(subprocess.check_output(["pidof", "-s", process]))
                time.sleep(1)
                try:

                    snesfault = Segfault()
                    if snesfault == True:
                        Pfig("Segfault found :" + str(LASTSEGFAULT))
                        ERROR = True
                        try:
                            time.sleep(1)
                            checkproc = int(
                                subprocess.check_output(["pidof", "-s", process])
                            )
                            pfig("-Snes9x still alive...-")
                            ERROR = False
                        except Exception as e:
                            Pfig("-Snes9x already dead..-")
                            ERROR = True
                            pkill = subprocess.Popen("pkill snes9x", shell=True)
                            return
                    else:
                        ERROR = False
                except Exception as e:
                    Pfig("Segfault Error:" + str(e))
                    ERROR = True
                try:
                    crashbandicoot = ManualExit()
                    if crashbandicoot == True:
                        Pfig("\nCaught Manual Exit.\n")
                        ERROR = True
                        pkill = subprocess.Popen("pkill snes9x", shell=True)
                        return
                    else:
                        ERROR = False

                except Exception as e:
                    Pfig("ManualExit Error:" + str(e))

                CHECKPOINT = CHECKPOINT + 1
                AutoSaveState()

            except Exception as e:
                if "returned non-zero exit status 1" in str(e):
                    ERROR = False
                    return
                else:
                    Pfig("Proc/Status Error:" + str(e))


def GifLauncher(mode):

    global ONESHOT
    global KILLLOAD
    global WALLET

    Pfig("\nLaunching animation : " + str(mode))
    #     print("mode:",mode)
    if mode != "Wheel":

        Categorie = [i for i in os.listdir(DirGif)]
        Gif = ""
        for name in Categorie:
            if str(name) == str(mode):
                Gifiles = [i for i in os.listdir(DirGif + str(name))]
                rnd = random.randint(0, len(Gifiles) - 1)
                Gif = DirGif + str(name) + "/" + Gifiles[rnd]
        try:
            if mode != "Loading":
                GifImg = Image.open(Gif)
                GifImg.seek(0)
                duration = 0
                while True:
                    try:
                        frame_duration = GifImg.info["duration"]
                        duration += frame_duration
                        GifImg.seek(GifImg.tell() + 1)
                    except EOFError:
                        duration = duration / 1000
                        if duration >= 3:
                            timer = str(int((duration * 2)))
                        elif int(duration) != 0:
                            timer = str(int((duration * 3)))
                        elif int(duration) == 0:
                            timer = "4"
                        if int(timer) >= 10:
                            timer = "10"
                        # print("Gif name =", Gif)
                        # print("Gif duration = %s timer set to %s:" % (duration, timer))
                        break
            else:
                timer = "0"

        except Exception as e:
            print("Error Gif Duration: ", str(e))
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
                cmd = "timeout " + timer + " sxiv -abfp -sf " + str(Gif)
            else:
                KILLLOAD = "sxiv"
                cmd = "sxiv -abfp -sf " + str(Gif)
        elif which("eog") != True:
            if mode != "Loading":
                cmd = "timeout " + timer + " eog --fullscreen " + str(Gif)
            else:
                KILLLOAD = "eog"
                cmd = "eog --fullscreen " + str(Gif)
        elif which("animate") != True:
            if mode == "Loading":
                KILLLOAD = "animate"
            Geo8 = str(ScreenResize("height"))
            cmd = (
                "animate -immutable -loop "
                + timer
                + " -geometry "
                + Geo8
                + " "
                + str(Gif)
            )
        else:
            # ascimatics ?
            Pfig("\n\n!!!!Can't Display Animation" + str(mode) + "!!!!\n\n")

            return

        try:
            if mode != "Loading":
                anim = subprocess.Popen(
                    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                output, error = anim.communicate()
                aout = output.decode()
            else:

                anim = subprocess.Popen(
                    cmd,
                    shell=True,
                    stdin=None,
                    stdout=None,
                    stderr=None,
                    close_fds=True,
                )

        except Exception as e:
            Pfig("Error: " + str(e))

        if mode == "Loose":
            return

    if mode == "Wheel":
        playlist = []
        Avifiles = [i for i in os.listdir(DirGif + "Wheel/Roucoups")]
        rnd = random.randint(0, len(Avifiles) - 1)
        playlist.append(DirGif + "Wheel/Roucoups/" + Avifiles[rnd] + " ")
        Avifiles = [i for i in os.listdir(DirGif + "Wheel/Cutscenes")]
        rnd = random.randint(0, len(Avifiles) - 1)
        playlist.append(DirGif + "Wheel/Cutscenes/" + Avifiles[rnd] + " ")
        Avifiles = [i for i in os.listdir(DirGif + "Wheel/Fireworks")]
        rnd = random.randint(0, len(Avifiles) - 1)
        fireworks = Avifiles[rnd]
        playlist.append(DirGif + "Wheel/Fireworks/" + Avifiles[rnd] + " ")

        #          cmd = "cvlc --fullscreen --no-volume-save --no-osd --play-and-exit --volume-step 100 "+ str(playlist)
        Pfig("\nLaunching : Wheel Of Roucoups")
        for item in playlist:
            cmd = "ffplay -hide_banner -fs -loglevel panic -autoexit -volume 50 " + str(
                item
            )
            #              print(cmd)
            cvlc = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            output, error = cvlc.communicate()

        if "BonusCoins3.mp4" in fireworks:
            WALLET = 3
            RwFile("credits.save", WALLET, "w")
            ONESHOT = True
            GifLauncher("Win")
            return LoadCoin("firstload")
        elif "BonusCoins5.mp4" in fireworks:
            WALLET = 5
            RwFile("credits.save", WALLET, "w")
            ONESHOT = True
            GifLauncher("Win")
            return LoadCoin("firstload")
        elif "BonusCoins10.mp4" in fireworks:
            WALLET = 10
            RwFile("credits.save", WALLET, "w")
            ONESHOT = True
            GifLauncher("Win")
            return LoadCoin("firstload")
        elif "QUESTIONBLOCK.avi" in fireworks:
            luck = random.randint(10, 32)
            WALLET = luck
            RwFile("credits.save", WALLET, "w")
            ONESHOT = True
            GifLauncher("Win")
            return LoadCoin("firstload")
        elif "BonusCoins1.mp4" in fireworks:
            WALLET = 1
            RwFile("credits.save", WALLET, "w")
            ONESHOT = True
            GifLauncher("Loose")
            return LoadCoin("firstload")
        elif "BonusCoins2.mp4" in fireworks:
            WALLET = 2
            RwFile("credits.save", WALLET, "w")
            ONESHOT = True
            GifLauncher("Loose")
            return LoadCoin("firstload")


def CompressVids():

    global KILLLOAD

    Pfig("\n-Compressing videos files found in compress.video-\n")
    VidLst = RwFile("compress.video", None, "r")
    if len(VidLst) > 0:
        Pfig("\n-%s videos files in compress.video-\n" % len(VidLst))
        time.sleep(1)
    else:
        Pfig("\n-No video found to be compressed-\n")
        time.sleep(1)
        return ()
    for vfile in VidLst:
        if len(vfile) > 2:
            GifLauncher("Loading")

            cmd = (
                "ffmpeg -y -i "
                + vfile
                + " -acodec libvorbis -ab 128k -ac 2 -vcodec libx264 -preset superfast -crf 32 -maxrate 400k -bufsize 400k -threads 1 -stats "
                + vfile.replace(".mkv", ".mp4")
            )
            print(cmd)
            #              ffmpeg = subprocess.Popen(cmd,shell=True)
            ffmpeg = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            output, error = ffmpeg.communicate()
            fout = output.decode()

            if "No such file or directory" in fout:
                Pfig("!!!!!!!!!!!\nError while Trying to Open File!!\n!!!!!!!!!!!\n")
                ffmpeg.terminate()
                cmd = "pkill ffmpeg"
                pkill = subprocess.Popen(cmd, shell=True)
                time.sleep(1)
            WaitForMe("ffmpeg")

            time.sleep(1)

            if KILLLOAD != "":
                cmd = "pkill " + KILLLOAD
                pkill = subprocess.Popen(cmd, shell=True)
                KILLLOAD = ""

            Pfig("\n-Finished-\n")
            Pfig(
                "\n-Done Encoding "
                + str(vfile).replace(".mkv", ".mp4")
                + "-\n-Removing old "
                + str(vfile)
                + "-\n\n"
            )
            try:
                os.remove(str(vfile))
            except:
                Pfig("\n Failed to remove file ..\n")
    Pfig("\n-All Videos have been processed-\n")
    Pfig("\n-Flushing compress.video-\n")
    RwFile("compress.video", None, "w")
    Pfig("\n-Done-\n")


def GetOut():
    if COMPRESS is True:
        CompressVids()

    cmd = "xset r on"
    xset = subprocess.Popen(cmd, shell=True)
    GifLauncher("Exit")
    Pfig("\n\n==Sneaver exited==\n\n")
    sys.exit(1)


##ARGH!

if len(sys.argv) > 1:

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

    if "--cheat" in sys.argv:
        CHEAT = "-cheat "

    if "--config" in sys.argv:
        CONFIG = True

    if "--nolencheck" in sys.argv:
        NOLENCHECK = True

    if "--search" in sys.argv:
        SEARCH = True
        pos = sys.argv.index("--search")
        try:
            SearchRom = str(sys.argv[pos + 1])
        except:
            print("Search Argument is empty.")
            sys.exit(0)

    if "--genre" in sys.argv:
        GENRE = True
        pos = sys.argv.index("--genre")
        try:
            SearchCat = str(sys.argv[pos + 1])
        except:
            print("Genre Argument is empty.")
            print("Genre Argument must be one of those keywords:\n%s" % Category)
            sys.exit(0)
        if SearchCat not in Category:
            print("Genre Argument must be one of those keywords:\n%s" % Category)
            sys.exit(0)

    if "--respawn" in sys.argv:
        RESPAWN = True
    if "--lastone" in sys.argv:
        LASTONE = True

    if "--smartcrash" in sys.argv:
        SMARTCRASH = True
    if "--allowbad" in sys.argv:
        IGNOREBAD = True

    if "--flushbad" in sys.argv:
        RwFile("bad.roms", "", "w")
        sys.exit(1)

    if "--compress" in sys.argv and len(sys.argv) == 2:
        CompressVids()
        GetOut()

    elif "--compress" in sys.argv:
        COMPRESS = True

    if "--badkid" in sys.argv:
        try:
            with open(DirData + "credits.save") as cs:
                for coin in cs:
                    Coins = int(coin)
        except Exception as e:
            print("Error:", e)
            sys.exit(1)
        print("Coins in wallet : ", Coins)
        print()
        while True:
            spanknbr = input(
                "How many coins do you want to remove from the wallet ? (Enter a number between 1 to 32) :"
            )
            if spanknbr.isdigit() == True:
                if int(spanknbr) <= 99 and int(spanknbr) != 0:
                    break
        GifLauncher("BadBoy")
        if Coins != 0:
            Totalcoin = Coins - int(spanknbr)
            RwFile("credits.save", Totalcoin, "w")
        GifLauncher("GameOver")
        GetOut()

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(
            "\n**Sneaver is a script using snes9x and ffmpeg to play or watch a snes game at random.\n\n**Download a rom put it in its folder inside the Movies directory\n\n**Then launch sneaver ^^\n\n\n**Use :\n\n./sneaver.py --config (To configure your gamepads [Must be used at first launch])  \n\n./sneaver.py --record (For recording a random game.)\n./sneaver.py --replay (For watching all the movies recorded with ffplay.)\n\n./sneaver.py --record --nojp/--jp (Avoid or Only recording Japenese games.)\n./sneaver.py --record --noeu/--eu (Avoid or Only recording European games.)\n./sneaver.py --record --nous/--us (Avoid or Only recording American games.)\n\n./sneaver.py --record/--replay --search [Name] To search for and select a specific rom.\n\n./sneaver.py --record/--replay --genre [GENRE] To select a game by its genre.\n./sneaver.py --record --nolencheck Do not erase recorded videos that are less than 60s\n./sneaver.py --record --respawn Start the rom using its last auto save state.\n./sneaver.py --record --lastone To launch the last game played normally.\n./sneaver.py --record --smartcrash Same as --respawn but without asking you after a crash.\n./sneaver.py --record --allowbad Ignore Blacklisted Roms.\n./sneaver.py --flushbad To erase bad roms list .\n\n./sneaver.py --compress To compress recorded videos before quitting.\n\n\nWhile in record mode Sneaver is using a credit system.\nWhen credits reaches Zero you can't play anymore.\nYou are able to gain one coin each hour once sneaver is closed.\nseaver --badkid to remove some coins.\n./sneaver.py --record --godmode (Unlimited coins)\n\n./sneaver.py --record --cheat To enable cheat saved in Datas\cheat\somefile.cht\n\n\nKeep pressing the Exit button on your joypad (configured with --config) multiple times if Snes9x ever crash.\n**Have fun !!\n"
        )
        print()
        sys.exit(1)
else:
    print(
        "\n**Sneaver is a script using snes9x and ffmpeg to play or watch a snes game at random.\n\n**Download a rom put it in its folder inside the Movies directory\n\n**Then launch sneaver ^^\n\n\n**Use :\n\n./sneaver.py --config (To configure your gamepads [Must be used at first launch]).\n\n./sneaver.py --record (For recording a random game.)\n./sneaver.py --replay (For watching all the movies recorded with ffplay.)\n\n./sneaver.py --record --nojp/--jp (Avoid or Only recording Japenese games.)\n./sneaver.py --record --noeu/--eu (Avoid or Only recording European games.)\n./sneaver.py --record --nous/--us (Avoid or Only recording American games.)\n\n./sneaver.py --record/--replay --genre [GENRE] To select a game by its genre.\n./sneaver.py --record/--replay --search [Name] To search for and select a specific rom.\n\n./sneaver.py --record --nolencheck Do not erase recorded videos that are less than 60s\n./sneaver.py --record --respawn Start the rom using its last auto save state.\n./sneaver.py --record --lastone To launch the last game played normally.\n./sneaver.py --record --smartcrash Same as --respawn but without asking you after a crash.\n./sneaver.py --record --allowbad Ignore Blacklisted Roms.\n./sneaver.py --flushbad To erase bad roms list .\n\n./sneaver.py --compress To compress recorded videos before quitting.\n./sneaver.py --record --cheat To enable cheat saved in Datas\cheat\somefile.cht\n\n\n\nWhile in record mode Sneaver is using a credit system.\nWhen credits reaches Zero you can't play anymore.\nYou are able to gain one coin each hour once sneaver is closed.\n\n./sneaver.py -badkid to remove some coins.\n./sneaver.py --record --godmode (Unlimited coins)\n\nKeep pressing the Exit button on your joypad (configured with --config) multiple time if Snes9x ever crash.\n**Have fun !!\n"
    )
    print()
    sys.exit(1)

if RECORD == True and REPLAY == True:
    print("\nArguments record and replay can't be used at the same time.\n\n")
    sys.exit(1)


def BonusCoins():

    try:
        currentdate = datetime.datetime.now()
        datefile = RwFile("last.closed", None, "r")
        date_object = datetime.datetime.strptime(
            str(datefile).strip(), "%Y-%m-%d %H:%M:%S.%f"
        )
        laps = int((currentdate - date_object).total_seconds() / 3600)
        RwFile("last.closed", currentdate, "w")
        return laps

    except Exception as e:
        RwFile("last.closed", currentdate, "w")
        Pfig("Error:" + str(e))
        return 0


def LoadCoin(mode):
    global WALLET

    print(
        """
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
"""
    )
    if mode == "firstload":
        if GODMODE == False:
            Coins = int(RwFile("credits.save", None, "r"))
            if Coins < 0:
                Coins = 0
            Bonus = BonusCoins()
            Coins = int(Coins) + Bonus

            if Coins > 100:
                Coins = 99

            WALLET = int(Coins)
            return

        else:
            Coins = 8
            WALLET = Coins
            return

    if mode == "printcoins":
        Coins = WALLET

    print(
        """
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
"""
    )
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    coint = int(Coins)
    cointer = 1

    while cointer <= coint:
        print(
            """
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
          """
        )
        time.sleep(0.1)
        cointer = cointer + 1
        if cointer >= coint:
            break

        print(
            """
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
          """
        )
        cointer = cointer + 1
        time.sleep(0.1)
        if cointer >= coint:
            break

        print(
            """
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
     """
        )

        cointer = cointer + 1
        time.sleep(0.1)
        if cointer >= coint:
            break

        print(
            """
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
     """
        )
        cointer = cointer + 1
        time.sleep(0.1)
        if cointer >= coint:
            break

        print(
            """
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
          """
        )
        time.sleep(0.1)
        cointer = cointer + 1
        if cointer >= coint:
            break

        print(
            """
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
          """
        )
        cointer = cointer + 1
        time.sleep(0.1)
        if cointer >= coint:
            break

        print(
            """
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
     """
        )

        cointer = cointer + 1
        time.sleep(0.1)
        if cointer >= coint:
            break

        print(
            """
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
     """
        )
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

            Pfig(
                "\n\n!!!---LUCKY DAY---!!!\n!!!--WELCOME TO THE--!!!\n!!!---ROUCOUPS---!!!\n!!!---OF---!!!\n!!!---FORTUNE---!!!\n"
            )

            GifLauncher("Wheel")

        else:

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
            RwFile("credits.save", coinsleft - 1, "w")


def Cointing(credits):

    numbers = [
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """    ▄▄▄▄     
  ▄█░░░░▌    
 ▐░░▌▐░░▌    
  ▀▀ ▐░░▌    
     ▐░░▌    
     ▐░░▌    
     ▐░░▌    
     ▐░░▌    
 ▄▄▄▄█░░█▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ 
▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """ ▄         ▄ 
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
          ▐░▌
          ▐░▌
           ▀ """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ 
▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
         ▐░▌ 
        ▐░▌  
       ▐░▌   
      ▐░▌    
     ▐░▌     
    ▐░▌      
   ▐░▌       
    ▀        """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
 ▐░░░░░░░░░▌ 
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
        """ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ """,
    ]

    tab = "                                               "
    middle = ""

    if GODMODE is True:
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
    else:

        nbrlst = list(str(credits).zfill(2))
        n1 = numbers[int(nbrlst[0])]
        n2 = numbers[int(nbrlst[1])]
        l1 = n1.split("\n")
        l2 = n2.split("\n")
        ln = max([len(l) for l in l1])
        f = "{:<" + str(ln) + "}{}{}"
        middle = "\n".join([f.format(tab, s1, s2) for s1, s2 in zip(l1, l2)])

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


def ParseConf():
    global GlobStart
    global GlobSelect
    global GlobExit

    try:
        with open(DirData + "sneaver.conf", "r") as conf:
            for setting in conf:
                if "ExitEmu" in setting and "J00:B" in setting:
                    GlobExit = setting.split(" = ExitEmu")[0].replace("J00:B", "")
                if "Joypad1 Start" in setting:
                    GlobStart = setting.split(" = Joypad1 Start")[0].replace(
                        "J00:B", ""
                    )
                if "Joypad1 Select" in setting:
                    GlobSelect = setting.split(" = Joypad1 Select")[0].replace(
                        "J00:B", ""
                    )
    except Exception as e:
        Pfig("Error:" + str(e))
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
            Pfig(
                "\nNo gamepad have been found .\n\nIs it connected ? \nHere is what iv found :\n\n"
            )
            for device in devices:
                print(device)
        else:
            Pfig("\nError :" + str(e))
    try:
        while Loop <= 200:
            events = pygame.event.get()
            for event in events:

                try:
                    checksnes9x = int(
                        subprocess.check_output(["pidof", "-s", "snes9x"])
                    )
                except Exception as e:
                    if "returned non-zero exit status 1" in str(e):
                        return False
                    else:
                        Pfig("Proc/Status Error:" + str(e))

                if event.type == pygame.JOYBUTTONUP:
                    if str(event.button) == str(Exit):
                        if PushedCnt >= 3:
                            return True
                        else:
                            PushedCnt = PushedCnt + 1
                else:
                    Loop = Loop + 1

    except Exception as e:
        Pfig("Error:" + str(e))

    return False


def PressStart(gamename):
    global CHECKPOINT
    global CHANGEGAME
    CHECKPOINT = 0

    pygame.init()

    Start = GlobStart
    Select = GlobSelect

    time.sleep(1)
    print(
        """


█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ 

██     ██████  ██████  ███████ ███████ ███████       ███████ ████████  █████  ██████  ████████      █ 
██     ██   ██ ██   ██ ██      ██      ██            ██         ██    ██   ██ ██   ██    ██         █ 
██     ██████  ██████  █████   ███████ ███████ █████ ███████    ██    ███████ ██████     ██         █ 
██     ██      ██   ██ ██           ██      ██            ██    ██    ██   ██ ██   ██    ██         █ 
██     ██      ██   ██ ███████ ███████ ███████       ███████    ██    ██   ██ ██   ██    ██         █ 

█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ 
"""
    )
    Pfig("-(Start) To play:-")
    print(gamename)
    print(
        """ 
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████

██     ██████  ██████  ███████ ███████ ███████     ███████ ███████ ██      ███████  ██████ ████████      █ 
██     ██   ██ ██   ██ ██      ██      ██          ██      ██      ██      ██      ██         ██         █ 
██     ██████  ██████  █████   ███████ ███████     ███████ █████   ██      █████   ██         ██         █ 
██     ██      ██   ██ ██           ██      ██          ██ ██      ██      ██      ██         ██         █ 
██     ██      ██   ██ ███████ ███████ ███████     ███████ ███████ ███████ ███████  ██████    ██         █ 

█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████
"""
    )
    Pfig("-(SELECT) To choose another game-")

    try:
        joypad1 = pygame.joystick.Joystick(0)
        joypad1.init()
    except Exception as e:
        if str(e) == "Invalid joystick device number":
            Pfig(
                "\nNo gamepad have been found .\n\nIs it connected ? \nHere is what iv found :\n\n"
            )
            for device in devices:
                print(device)
        else:
            Pfig("\nError :" + str(e))
        GetOut()
    try:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONUP:
                    if str(event.button) == str(Start):
                        GifLauncher("NewGame")
                        return True
                    if str(event.button) == str(Select):
                        CHANGEGAME = True
                        GifLauncher("InsertCoin")
                        return False
                elif event.type == pygame.JOYBUTTONDOWN:
                    if str(event.button) == str(Start):
                        GifLauncher("NewGame")
                        return True
                    if str(event.button) == str(Select):
                        CHANGEGAME = True
                        GifLauncher("InsertCoin")
                        return False
    #                    else:
    #                         print("full ev:",event)
    #                         print("ev.b:",str(event.button))
    #                         print("strSelect:",str(Select))
    #                         print("len ev.b:",len(str(event.button)))
    #                         print("len select:",len(str(Select)))
    except Exception as e:
        Pfig("Error:" + str(e))
        GetOut()


def Configuration():
    next = False

    joymap = {
        "Start": "",
        "Select": "",
        "Up": "",
        "Down": "",
        "Right": "",
        "Left": "",
        "BtnA": "",
        "BtnB": "",
        "BtnX": "",
        "BtnY": "",
        "BtnL": "",
        "BtnR": "",
        "BtExit": "",
    }

    joymap2 = {
        "Start": "",
        "Select": "",
        "Up": "",
        "Down": "",
        "Right": "",
        "Left": "",
        "BtnA": "",
        "BtnB": "",
        "BtnX": "",
        "BtnY": "",
        "BtnL": "",
        "BtnR": "",
        "BtExit": "",
    }

    if (
        os.path.exists("/dev/input/js0") == False
        and os.path.exists("/dev/input/js1") == False
    ):
        Pfig(
            "\nNo gamepad have been found .\n\nIs it connected ? \nHere is what iv found :\n\n"
        )
        for device in devices:
            print(device)
        Pfig(
            "\nIf this error persist you may have to edit sneaver.conf yourself sorry.\n"
        )
        GetOut()

    if which("jstest") != True:
        Pfig("\njstest is not found please install : apt install joystick")
        GetOut()
    if which("sxiv") != True:
        Pfig("\nunbuffer is not found please install : apt install except")
        GetOut()

    Pfig("\nOk lets Configure Joypad 1:\n\n")

    if os.path.exists("/dev/input/js0") == True:
        for button, code in joymap.items():
            next = False
            if str(button) == "BtExit":
                Pfig("Please press a button to close Snes9x emulator.")
            else:
                Pfig("Please press a button for " + str(button) + " :\n\n")
            proc = subprocess.Popen(
                ["unbuffer", "jstest", "--select", "/dev/input/js0"],
                bufsize=1,
                universal_newlines=True,
                stdout=subprocess.PIPE,
            )
            while next == False:
                for line in proc.stdout:
                    proc.send_signal(signal.SIGSTOP)
                    if "type 1," in line or "type 2," in line:
                        if "value" in line:
                            p = re.compile(
                                "number (\d+)?,",
                            )
                            num = p.findall(line)[0]
                            print("\nYou've just pressed Button Nbr :" + num + "\n")
                            confirm = input("\nIs this correct ?(y/n) :")
                            try:
                                if "y" in confirm.lower():
                                    Pfig("\nMapping key ..\n\n")
                                    joymap[button] = str(num)
                                    next = True
                                    proc.terminate()
                                    break
                                else:
                                    Pfig(
                                        "\nOk then Please press a button for "
                                        + str(button)
                                        + ": \n\n"
                                    )
                                    proc.send_signal(signal.SIGCONT)
                            except:
                                Pfig(
                                    "Ok then Please press a button for  "
                                    + str(button)
                                    + ":\n\n"
                                )
                                proc.send_signal(signal.SIGCONT)

                        else:
                            proc.send_signal(signal.SIGCONT)
                    else:
                        proc.send_signal(signal.SIGCONT)

        Pfig("\nOk here is the config for Joypad 1:\n\n")
        for button, code in joymap.items():
            print("Button %s = code %s" % (button, code))
        print("\n\n")

    if os.path.exists("/dev/input/js1") == True:
        question = input("Do you want to configure Joypad 2(Y/N):")
    else:
        question = "n"

    if "y" in question.lower():

        for button, code in joymap2.items():
            next = False
            if str(button) == "BtExit":
                Pfig("Please press a button to close Snes9x emulator.")
            else:
                Pfig("Please press a button for " + str(button) + " :\n\n")
            proc = subprocess.Popen(
                ["unbuffer", "jstest", "--select", "/dev/input/js1"],
                bufsize=1,
                universal_newlines=True,
                stdout=subprocess.PIPE,
            )
            while next == False:
                for line in proc.stdout:
                    proc.send_signal(signal.SIGSTOP)
                    if "type 1," in line or "type 2," in line:
                        if "value 1" in line:
                            p = re.compile(
                                "number (\d+)?,",
                            )
                            num = p.findall(line)[0]
                            print("\nYou've just pressed Button Nbr :" + num + "\n")
                            confirm = input("\nIs this correct ?(y/n) :")
                            try:
                                if "y" in confirm.lower():
                                    Pfig("\nMapping key ..\n\n")
                                    joymap2[button] = str(num)
                                    next = True
                                    proc.terminate()
                                    break
                                else:
                                    Pfig(
                                        "\nOk then Please press a button for "
                                        + str(button)
                                        + ": \n\n"
                                    )
                                    proc.send_signal(signal.SIGCONT)
                            except:
                                Pfig(
                                    "Ok then Please press a button for  "
                                    + str(button)
                                    + ":\n\n"
                                )
                                proc.send_signal(signal.SIGCONT)

                        else:
                            proc.send_signal(signal.SIGCONT)
                    else:
                        proc.send_signal(signal.SIGCONT)

        print("\nOk here are the config for Joypad 2:\n\n")
        for button, code in joymap2.items():
            print("Button %s = code %s" % (button, code))
    else:
        joymap2 = joymap
    print()

    Snes9xConf = (
        """#-----------------------------------------
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
BaseDir = """
        + str(DirData)
        + """
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
J00:B"""
        + str(joymap["Up"])
        + """ = Joypad1 Up
J00:B"""
        + str(joymap["Down"])
        + """ = Joypad1 Down
J00:B"""
        + str(joymap["Left"])
        + """ = Joypad1 Left
J00:B"""
        + str(joymap["Right"])
        + """ = Joypad1 Right
J00:B"""
        + str(joymap["BtnA"])
        + """ = Joypad1 A
J00:B"""
        + str(joymap["BtnB"])
        + """ = Joypad1 B
J00:B"""
        + str(joymap["BtnX"])
        + """ = Joypad1 X
J00:B"""
        + str(joymap["BtnY"])
        + """ = Joypad1 Y
J00:B"""
        + str(joymap["BtnL"])
        + """ = Joypad1 L
J00:B"""
        + str(joymap["BtnR"])
        + """ = Joypad1 R
J00:B"""
        + str(joymap["Select"])
        + """ = Joypad1 Select
J00:B"""
        + str(joymap["Start"])
        + """ = Joypad1 Start
J00:B"""
        + str(joymap["BtExit"])
        + """ = ExitEmu


#Controller 2
J01:Axis1 = Joypad2 Axis Up/Down T=50%
J01:Axis0 = Joypad2 Axis Left/Right T=50%
J01:B"""
        + str(joymap2["Up"])
        + """ = Joypad2 Up
J01:B"""
        + str(joymap2["Down"])
        + """ = Joypad2 Down
J01:B"""
        + str(joymap2["Left"])
        + """ = Joypad2 Left
J01:B"""
        + str(joymap2["Right"])
        + """ = Joypad2 Right
J01:B"""
        + str(joymap2["BtnA"])
        + """ = Joypad2 A
J01:B"""
        + str(joymap2["BtnB"])
        + """ = Joypad2 B
J01:B"""
        + str(joymap2["BtnX"])
        + """ = Joypad2 X
J01:B"""
        + str(joymap2["BtnY"])
        + """ = Joypad2 Y
J01:B"""
        + str(joymap2["BtnL"])
        + """ = Joypad2 L
J01:B"""
        + str(joymap2["BtnR"])
        + """ = Joypad2 R
J01:B"""
        + str(joymap2["Select"])
        + """ = Joypad2 Select
J01:B"""
        + str(joymap2["Start"])
        + """ = Joypad2 Start
J01:B"""
        + str(joymap2["BtExit"])
        + """ = ExitEmu 

K00:Escape = ExitEmu
K00:Insert = QuickSave000

#Full config list :  https://github.com/snes9xgit/snes9x/blob/master/unix/snes9x.conf.default
"""
    )
    RwFile("sneaver.conf", Snes9xConf, "w")
    GetOut()


def Rename(name, srcdir):

    badchar = ["(", ")", "[", "!", "]", " ", "_", "--", "'", '"', ",", "&", "#"]
    goodchar = "abcdefghijklmnopqrstuvwxyz1234567890"
    mv = False

    if name.endswith(".mkv"):

        tocompress = RwFile("compress.video", None, "r")
        for mkv in tocompress:
            if name in mkv:
                return

        print("\n-Found a new .mkv to compress later :%s\n" % name)
        RwFile("compress.video", str(srcdir) + str(name), "a+")
        return

    for char in badchar:
        if char in name:
            mv = True
    if name.endswith("-U"):
        mv = True
    elif name.endswith("-J"):
        mv = True
    elif name.endswith("-G"):
        mv = True
    elif name.endswith("-EU"):
        mv = True

    if mv == True:
        print("Renaming : ", name)
        newname = (
            name.replace("&", "-")
            .replace("(", "-")
            .replace(")", "-")
            .replace("[", "-")
            .replace("!", "-")
            .replace("]", "")
            .replace(" ", "-")
            .replace("_", "-")
            .replace("'", "-")
            .replace('"', "-")
            .replace("#", "-")
            .replace(",", "-")
            .replace("--", "-")
        )
        newname = newname.replace("---", "-").replace("--", "-").strip()

        while True:
            if newname[-1].lower() not in goodchar:
                newname = newname[:-1]
            else:
                if newname.endswith("-U"):
                    newname = newname[:-2]
                elif newname.endswith("-J"):
                    newname = newname[:-2]
                elif newname.endswith("-G"):
                    newname = newname[:-2]
                elif newname.endswith("-EU"):
                    newname = newname[:-3]
                break

        if os.path.exists(srcdir + newname) is True:
            print()
            if os.path.isdir(srcdir + newname) is True:
                print("Directory already exist :", newname)
                print("Existing Directory %s content:\n" % newname)
                [print(i) for i in os.listdir(srcdir + newname)]
                print("\nAbout to DELETE this Directory:", srcdir + name)
                dircontent = [i for i in os.listdir(srcdir + name)]
                while True:
                    answer = input(
                        "Do you want to remove this folder?\nContent of this Directory:\n %s \n\nDelete entire folder (yes/no)?:"
                        % (dircontent)
                    )
                    if answer == "yes":
                        print("\n%s is deleted...\n\n" % srcdir + name)
                        rmtree(srcdir + name)
                        break
                    elif answer != "no":
                        print("\nKeeping:", name)
                        break
            else:
                print("File already exist :", newname)
                print("\nAbout to DELETE this file:", srcdir + name)
                while True:
                    answer = input(
                        "Do you want to remove this file\nDeleting %s \n(yes/no)?:"
                        % (srcdir + name)
                    )
                    if answer == "yes":
                        print("\n\n%s is Deleted...\n\n" % srcdir + name)
                        os.remove(srcdir + name)
                        break
                    elif answer != "no":
                        print("\nKeeping:", name)
                        break

        else:
            os.rename(srcdir + name, srcdir + newname)
            print("\nNew Name is : ", newname)


def ScreenResize(mode):

    global OLDSCREEN
    global NEWSCREEN
    global NEWRES

    if mode == "change":

        if OLDSCREEN != "" and NEWSCREEN != "" and NEWRES != "":
            Pfig("\n-Changing Screen Resolution now-\n")
            Pfig(NEWSCREEN)
            print()
            xrandr = subprocess.Popen(str(NEWSCREEN), shell=True)
            return

        xrandr = subprocess.Popen("xrandr", shell=True, stdout=subprocess.PIPE)
        xout = str(xrandr.communicate()[0])
        reslist = []
        NEWRES = ""
        goodone = False

        if "connected primary" in xout:
            device = str(xout.split("connected primary")[0].split("\\n")[-1]).replace(
                " ", ""
            )
            xit = "".join(xout.split("connected primary")[1]).split("\\n")

        for item in xit:
            if item.startswith(" ") == True:

                if "(" not in item:

                    if "*" in item:
                        tmp = item.split("x")
                        height = tmp[0]
                        width = tmp[1].split(" ")[0]
                        res = str(str(height) + "x" + str(width)).replace(" ", "")
                    else:

                        if "640x480" in item:
                            NEWSCREEN = "xrandr --output " + device + " --mode 640x480"
                            NEWRES = "640x480"
                            goodone = True
                        else:
                            regex = re.compile(r"\d+[x]\d+")
                            bingo = regex.search(item)

                            if bingo:
                                if not bingo.group() in reslist:
                                    reslist.append(bingo.group())
            else:
                break

        if goodone == False:
            sorting = []
            for resolution in reslist:
                tmp = resolution.split("x")[0]
                sorting.append(tmp)
            sorting.sort(key=int)
            minwidth = sorting[0]

            for resolution in reslist:
                if resolution.startswith(minwidth) == True:
                    NEWSCREEN = (
                        "xrandr --output " + device + " --mode " + str(resolution)
                    )
                    NEWRES = str(resolution)

                    break

        Pfig("\n-Saving Current Screen Config-\n")
        OLDSCREEN = "xrandr --output " + device + " --mode " + res
        Pfig(OLDSCREEN)

        Pfig("\n-Changing Screen Resolution now-\n")
        Pfig(NEWSCREEN)
        print()

        xrandr = subprocess.Popen(str(NEWSCREEN), shell=True)

    if mode == "revert":
        if OLDSCREEN != "" and NEWSCREEN != "" and NEWRES != "":
            xrandr = subprocess.Popen(str(OLDSCREEN), shell=True)
            return
        NEWRES = ""
        xrandr = subprocess.Popen(str(OLDSCREEN), shell=True)

    if mode == "height":
        height = "640"
        xrandr = subprocess.Popen("xrandr", shell=True, stdout=subprocess.PIPE)
        xout = str(xrandr.communicate()[0])

        if "connected primary" in xout:
            device = str(xout.split("connected primary")[0].split("\\n")[-1]).replace(
                " ", ""
            )
            xit = "".join(xout.split("connected primary")[1]).split("\\n")

        for item in xit:
            if item.startswith(" ") == True:

                if "(" not in item:

                    if "*" in item:
                        tmp = item.split("x")
                        height = tmp[0]
        return height


def BlackList():
    global BADROMS
    global LASTBAD

    BADROMS = RwFile("bad.roms", None, "r")

    try:
        if LASTBAD != BADROMS:
            Pfig(str(len(BADROMS)) + " Roms Blacklisted .\n\n")
            LASTBAD = BADROMS
    except Exception as e:
        print("Error:", e)
        BADROMS = []
        Pfig("0 Roms Blacklisted .\n\n")


def Speaker():
    cmd = "pacmd list-sources"
    cmd = cmd.split(" ")
    answer = subprocess.check_output(cmd).decode(errors="ignore")

    if "index:" in answer:
        answersplit = answer.split("index:")
        for line in answersplit:
            line = [l.strip("\n") for l in line.splitlines() if l.strip()]
            devname = ""
            for l in line:
                if "name: <" in l:
                    devname = l.strip().split("name: <")[1][:-1]
                    if "monitor" in devname:
                        return devname
                if "microphone" in l.lower():
                    devname = ""
                    break

        print("Couldn't find current soundcard output Using default recording device")
        return "default"


def RanDef():
    global SEARCH
    global GENRE
    global RESPAWN
    global SearchRom
    global SearchCat
    global RomIndex
    global CHANGEGAME
    global GoodToGo

    MovLst = []
    if SEARCH is True:
        romret = ""
        romfiles = []
        movfile = []
        DirChosen = []
        FOUNDONE = False

        if RECORD is True:

            if IGNOREBAD == False:
                BlackList()
            if GENRE is True:
                AllowedRoms = RwFile("roms." + SearchCat + ".snes", None, "r")
                Pfig(
                    "\n-%s roms in list matching %s genre-\n"
                    % (len(AllowedRoms), SearchCat)
                )
            if RESPAWN is True or LASTONE is True:
                FOUNDONE = True
            else:
                for dirpath, dirnames, filenames in os.walk(DirMovies):
                    for name in filenames:
                        if GENRE is True:
                            Bingo = False
                            for rms in AllowedRoms:
                                if rms.lower().replace(" ", "-") in name.lower():
                                    Bingo = True
                                    break
                                elif rms.lower() in name.lower():
                                    Bingo = True
                                    break
                            if Bingo is False:
                                continue

                        if name.endswith(".sfc") or name.endswith(".smc"):
                            if SearchRom.lower().replace(" ", "-") in name.lower():
                                if NOJP == True:
                                    if not "-J-" in name and name not in BADROMS:
                                        romfiles.append(name)
                                        DirChosen.append(dirpath + "/")
                                        FOUNDONE = True
                                elif NOEU == True:
                                    if not "-E-" in name and name not in BADROMS:
                                        romfiles.append(name)
                                        DirChosen.append(dirpath + "/")
                                        FOUNDONE = True
                                elif NOUS == True:
                                    if not "-U-" in name and name not in BADROMS:
                                        romfiles.append(name)
                                        DirChosen.append(dirpath + "/")
                                        FOUNDONE = True
                                elif JP == True:
                                    if "-J-" in name and name not in BADROMS:
                                        romfiles.append(name)
                                        DirChosen.append(dirpath + "/")
                                        FOUNDONE = True
                                elif EU == True:
                                    if "-E-" in name and name not in BADROMS:
                                        romfiles.append(name)
                                        DirChosen.append(dirpath + "/")
                                        FOUNDONE = True
                                elif US == True:
                                    if "-U-" in name and name not in BADROMS:
                                        romfiles.append(name)
                                        DirChosen.append(dirpath + "/")
                                        FOUNDONE = True
                                else:
                                    romfiles.append(name)
                                    DirChosen.append(dirpath + "/")
                                    FOUNDONE = True

        if REPLAY == True:
            if GENRE is False:
                MovLst = [i for i in os.listdir(DirMovies)]
            else:
                OldLst = [i for i in os.listdir(DirMovies)]
                AllowedRoms = RwFile("roms." + SearchCat + ".snes", None, "r")
                Pfig(
                    "\n-%s roms in list matching %s genre-\n"
                    % (len(AllowedRoms), SearchCat)
                )
                for dname in OldLst:
                    for rms in AllowedRoms:
                        if rms.lower().replace(" ", "-") in dname.lower():
                            if dname not in MovLst:
                                MovLst.append(dname)
                        elif rms.lower() in dname.lower():
                            if dname not in MovLst:
                                MovLst.append(dname)
                if len(MovLst) == 0:
                    Pfig(
                        "\n-Couldn't find any roms matching %s genre inside Movies Folder-\n"
                        % SearchCat
                    )
                    GENRE = False
                else:
                    Pfig(
                        "\n-Found %s roms matching %s genre-\n"
                        % (len(MovLst), SearchCat)
                    )

            for dir in MovLst:
                if SearchRom.lower().replace(" ", "-") in dir.lower():
                    FOUNDONE = True
                    currentdir = DirMovies + dir + "/"
                    try:
                        for i in os.listdir(currentdir):
                            if (
                                i.endswith(".mp4")
                                or i.endswith(".mkv")
                                or i.endswith(".avi")
                            ):
                                print(currentdir + i)
                                movfile.append(currentdir + i)
                    except Exception as e:
                        Pfig("\n\nError:" + str(e))
                        print()
                        pass

            if len(movfile) > 0:
                try:
                    random.shuffle(movfile)

                    return movfile, DirChosen

                except Exception as e:
                    Pfig("Error:" + str(e))
                    pass
            else:
                Pfig("\n\nHaven't Found any Movie Containing %s .\n\n" % SearchRom)
                GetOut()

        if RECORD == True and FOUNDONE == True:
            try:
                if SMARTCRASH is True and GoodToGo is True and CHANGEGAME is False:
                    return (romfiles[RomIndex], DirChosen[RomIndex])
                elif CHANGEGAME is True:
                    GoodToGo = False
                    CHANGEGAME = False
                for n, rom in enumerate(romfiles):
                    print("-To choose: %s type number: %s" % (rom, n))
                print("-To search for another game type: search")
                print("-To search for a genre type: genre")
                print("-To search both for a genre and a specific game type: both")
                print("-To play a random game type: random")
                print("-To respawn from the last game autosave type: respawn")
                print("-To quit type: quit\n")

                while True:
                    answer = input("Please type your choice:")
                    if answer.isdigit() is True:
                        if int(answer) in range(0, len(romfiles)):
                            RomIndex = int(answer)
                            return (romfiles[int(answer)], DirChosen[int(answer)])
                    if answer == "respawn":
                        SEARCH = False
                        GENRE = False
                        RESPAWN = True
                        Pfig("\n\n-RESPAWN FROM LAST GAME-\n\n")
                        return RwFile("last.played", None, "r")

                    if answer == "search":
                        SEARCH = True
                        GENRE = False
                        SearchRom = input(
                            "Please enter the rom you would like to search:"
                        )
                        return RanDef()
                    if answer == "genre":
                        while True:
                            GENRE = True
                            SEARCH = True
                            SearchCat = input(
                                "Please enter a genre you would like to search:"
                            )
                            if SearchCat not in Category:
                                print(
                                    "Genre Argument must be one of those keywords:\n%s"
                                    % Category
                                )
                            else:
                                GENRE = True
                                return RanDef()
                    if answer == "both":
                        SEARCH = True
                        GENRE = True
                        SearchRom = input("Please enter a name of rom:")
                        while True:
                            SearchCat = input("Please enter a genre:")
                            if SearchCat not in Category:
                                print(
                                    "Genre Argument must be one of those keywords:\n%s"
                                    % Category
                                )
                            else:
                                break
                        return RanDef()
                    if answer == "random":
                        SEARCH = False
                        return RanDef()
                    if answer == "quit":
                        return GetOut()

            #                         rnd = random.randint(0,len(romfiles)-1)
            #                         romret = romfiles[rnd]
            #                         return romret,DirChosen[rnd]

            except Exception as e:
                Pfig("\n\nError:" + str(e))
                pass
        else:
            Pfig("\n\nHaven't Found any Game Containing the word : %s \n\n" % SearchRom)
            while True:
                answer = input(
                    "Type search to search for another game or random to play a random one:"
                )
                if answer == "search":
                    SearchRom = input(
                        "Please enter the name of rom you would like to search:"
                    )
                    return RanDef()
                if answer == "random":
                    SEARCH = False
                    return RanDef()
            GetOut()

    if SEARCH is False:

        while True:

            romret = ""
            romfiles = []
            movfile = []
            FOUNDONE = False

            if GENRE is False:
                MovLst = [i for i in os.listdir(DirMovies)]
            else:
                OldLst = [i for i in os.listdir(DirMovies)]
                AllowedRoms = RwFile("roms." + SearchCat + ".snes", None, "r")
                Pfig(
                    "\n-%s roms in list matching %s genre-\n"
                    % (len(AllowedRoms), SearchCat)
                )
                for dname in OldLst:
                    for rms in AllowedRoms:
                        if rms.lower().replace(" ", "-") in dname.lower():
                            if dname not in MovLst:
                                MovLst.append(dname)
                        elif rms.lower() in dname.lower():
                            if dname not in MovLst:
                                MovLst.append(dname)
                if len(MovLst) == 0:
                    Pfig(
                        "\n-Couldn't find any roms matching %s genre inside Movies Folder-\n"
                        % SearchCat
                    )
                    GENRE = False
                else:
                    Pfig(
                        "\n-Found %s roms matching %s genre-\n"
                        % (len(MovLst), SearchCat)
                    )

            try:
                rnd = random.randint(0, len(MovLst) - 1)
                DirChosen = DirMovies + MovLst[rnd]
            except:
                Pfig(
                    "Can't find anything !!!\nWhere am i ?\nPlease check what's in the Movies Folder .."
                )
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
                    currentdir = DirMovies + dir + "/"
                    try:
                        for i in os.listdir(currentdir):
                            if (
                                i.endswith(".mp4")
                                or i.endswith(".mkv")
                                or i.endswith(".avi")
                            ):
                                print(currentdir + i)
                                movfile.append(currentdir + i)
                    except Exception as e:
                        Pfig("\n\nError:" + str(e))
                        print()
                        pass

            if RECORD == True and FOUNDONE == True:
                try:
                    rnd = random.randint(0, len(romfiles) - 1)
                    romret = romfiles[rnd]

                    return romret, DirChosen

                except Exception as e:
                    Pfig("\n\nError:" + str(e))
                    pass

            if REPLAY == True:
                if len(movfile) > 0:
                    try:
                        random.shuffle(movfile)

                        return movfile, DirChosen

                    except Exception as e:
                        Pfig("Error:" + str(e))
                        pass
                else:
                    Pfig(
                        "\n\nHaven't Found any Movie\n\nUse sneaver -record to fill the playlist.\n\n"
                    )
                    GetOut()


def LenCheck(DirChosen, newmovie):

    if not os.path.exists(str(DirChosen) + "/" + str(newmovie)):
        Pfig("\n-File not saved :-")
        print(str(str(DirChosen) + "/" + str(newmovie)).replace("//", "/") + "\n")
        return ()

    if NOLENCHECK is False:
        cmd = (
            "ffprobe -v quiet -print_format compact=print_section=0:nokey=1:escape=csv -show_entries format=duration "
            + str(DirChosen)
            + "/"
            + str(newmovie)
        ).replace("//", "/")
        ffprobe = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = ffprobe.communicate()

        try:
            videolen = int(float(output.decode().strip()))
        except Exception as e:
            print(
                "Error:%s\nFfprobe output:%s\nFfprobe error:%s"
                % (str(e), output.decode(), error.decode())
            )
            videolen = 60

        if videolen >= 60:
            Pfig("\n-Your game session has been recorded with success !-\n")
            Pfig("\n-Saving video path to compress it later-\n")
            RwFile(
                "compress.video",
                str(str(DirChosen) + "/" + str(newmovie)).replace("//", "/"),
                "a+",
            )
            print(
                "Added %s to Data/compress.video"
                % str(str(DirChosen) + "/" + str(newmovie)).replace("//", "/")
            )
            Pfig("\n-Done-\n")
        else:
            Pfig("\n-Recorded Video duration is less than 60 seconds-\n")
            Pfig("\n-Removing (use --nolencheck to prevent this) ...-\n")
            try:
                os.remove(str(DirChosen) + "/" + str(newmovie))
            except Exception as e:
                print("Error:", str(e))
                Pfig("\n-Failed to remove file ...-\n")
    else:
        Pfig("\n-Your game session has been recorded with success !-\n")
        Pfig("\n-Saving video path to compress it later-\n")
        RwFile(
            "compress.video",
            str(str(DirChosen) + "/" + str(newmovie)).replace("//", "/"),
            "a+",
        )
        print(
            "Added %s to Data/compress.video"
            % str(str(DirChosen) + "/" + str(newmovie)).replace("//", "/")
        )
        Pfig("\n-Done-\n")
    time.sleep(1)


def CheatBuilder(gamename, gamefolder):

    global CHEAT
    global CHEATER

    namesave = gamename
    gamename = gamename.replace(".sfc", "").replace(".smc", "")
    gamefolder = gamefolder.split("/")[-2].replace("-", " ").lower()

    if CHEATER is True:
        return
    else:
        Pfig("-CHEAT BUILDER-")

    for dirpath, dirnames, filenames in os.walk(DirCheat):
        for name in filenames:
            if name.endswith(".cht"):
                if gamename in name:
                    Pfig("\n-Found One Cheat File Matching: %s-" % (name))
                    print(RwFile(name, None, "r"))
                    print("\n-To use this file type: yes")
                    print(
                        "-To use this file type and don't ask again until sneaver is closed: always"
                    )
                    print("-To change which cheat code to use type: change")
                    print("-To not use this file type: disable\n")
                    while True:
                        answer = input("Choice:")
                        if answer == "yes":
                            return
                        if answer == "always":
                            CHEATER = True
                            return
                        elif answer == "change":
                            break
                        elif answer == "disable":
                            CHEAT = ""
                            return

    cheats = RwFile("cheats.bml", None, "r")

    matchingames = {}
    gameslist = []

    for data in cheats:
        gamecheats = []
        gameversion = ""
        code = ""
        description = ""
        data = data.splitlines()
        for line in data:
            if "name:" in line:
                if gameversion == "" and gamefolder in line.lower():
                    gameversion = line.split("name:")[1]
            if gameversion != "":

                if description != "" and code != "":
                    gamecheats.append((description, code))
                    description, code = "", ""
                elif "name:" in line:
                    description = line.split("name:")[1]
                elif "code:" in line:
                    code = line.split("code:")[1]

        if len(gamecheats) > 0:
            matchingames[gameversion] = gamecheats

    if len(matchingames) == 0:
        Pfig("\n-DID NOT FIND ANY CHEAT IN DATABASE FOR: %s-" % (gamefolder))
        CHEAT = ""
        return

    elif len(matchingames) == 1:
        Pfig("\n-CHEATS HAS BEEN FOUND IN DATABASE !-")
    else:
        Pfig("\n-SEVERAL CHEATS HAS BEEN FOUND IN DATABASE !-\n")
    for n, key in enumerate(matchingames):
        print("-To choose : %s Type number: %s " % (key, n))
        gameslist.append(key)

    print("-Type skip to cancel.")
    print(
        "\nPlease choose in the list a name which is matching this version:\n\t-",
        namesave,
    )
    print()
    while True:
        answer = input("Please type your choice:")
        if answer.isdigit() is True:
            if int(answer) in range(0, len(matchingames)):
                choice = int(answer)
                break
        elif answer == "skip":
            CHEAT = ""
            return

    cheat2write = ""

    print("\n-Type stop to write the file.\n")

    for info in matchingames[gameslist[choice]]:
        print("\nCheat:", info[0])
        print("Code:", info[1])
        while True:
            useit = input("\nWould you like to use this cheat ? (y/n/stop) :")
            if useit == "n":
                break
            elif useit == "stop":
                if len(cheat2write) > 0:
                    Pfig("\n-Writing cheat file.\n")
                    RwFile(gamename + ".cht", cheat2write, "w")
                    return ()
                else:
                    Pfig("\n-No cheats to write.\n")
                    return ()
            elif useit == "y":
                cheat2write += "cheat\n  name: %s\n  code: %s\n  enable\n" % (
                    info[0],
                    info[1],
                )
                break
    if len(cheat2write) > 0:
        Pfig("\n-Writing cheat file.\n")
        RwFile(gamename + ".cht", cheat2write, "w")
        return ()
    else:
        Pfig("\n-No cheats to write.\n")


##PressStart#
signal.signal(signal.SIGINT, signal_handler)

if 1 == 1:
    print()

    ##Renaming
    MovLst = [i for i in os.listdir(DirMovies)]
    for name in MovLst:
        if name.endswith(".sfc") or name.endswith(".smc"):
            if not os.path.exists(
                DirMovies + name.replace(".sfc", "").replace(".smc", "")
            ):
                newdir = DirMovies + name.replace(".sfc", "").replace(".smc", "")
                os.mkdir(newdir)
                print(
                    "Found a Rom without any folder.\nPlacing %s inside it's new folder:\n%s"
                    % (name, newdir)
                )
                os.rename(DirMovies + name, newdir + "/" + name)
            else:
                print("Found Rom outside it's folder :", name)
                print("Folder Already Exist...")
        Rename(name, DirMovies)
    MovLst = [i for i in os.listdir(DirMovies)]
    for currentdir in MovLst:
        files = os.listdir(DirMovies + currentdir)
        for name in files:
            Rename(name, DirMovies + currentdir + "/")

    if CONFIG == True:
        Configuration()
    elif os.path.exists(DirData + "sneaver.conf") == False:
        Configuration()
    elif os.path.exists(DirData + "sneaver.conf") == True:
        newfile = []
        thegoodplace = False
        with open(DirData + "sneaver.conf", "r") as f:
            lines = f.readlines()
            lines = [l.strip() for l in lines if l.strip()]
        for l in lines:
            if "BaseDir = " in l:
                basedir = l.split("BaseDir = ")[1]
                if basedir != str(DirData):
                    Pfig("-Sneaver Data folder's emplacement has changed-")
                    Pfig("-Saving current emplacement to sneaver.conf-")
                    newfile.append("BaseDir = " + str(DirData))
                else:
                    thegoodplace = True
                    break
            else:
                newfile.append(l)
        if thegoodplace is False:
            with open(DirData + "sneaver.conf", "w") as f:
                f.writelines("\n".join(newfile))
            Pfig("-Done-")
            time.sleep(1)

    if REPLAY == True:

        Container, DirChosen = RanDef()
        print("Found " + str(len(Container)) + " Movies !\n\n")

        #       cmd = "cvlc --fullscreen --play-and-exit "+ str(playlist)

        Pfig("\nLaunching : \n")
        for item in Container:
            cmd = "ffplay -fs -loglevel panic -autoexit " + str(item)
            cvlc = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            output, error = cvlc.communicate()

        #              if "filesystem access error:" in output:
        #                    Pfig("!!!!!!!!!!!\nError while Trying to Open File!!\n!!!!!!!!!!!\n")
        #                    cvlc.terminate()

        GetOut()

    ##

    if RECORD == True:

        ParseConf()
        devsound = Speaker()
        time.sleep(1)
        LoadCoin("firstload")
        while True:
            WaitForMe("snes9x")
            WaitForMe("ffmpeg")

            if RESPAWN:
                Container, DirChosen = RwFile("last.played", None, "r")

                if not Container and not DirChosen:
                    print("-Error with file last.played : opening a random rom instead")
                    Container, DirChosen = RanDef()
            elif LASTONE:
                Container, DirChosen = RwFile("last.played", None, "r")
                if not Container and not DirChosen:
                    print("-Error with file last.played : opening a random rom instead")
                    Container, DirChosen = RanDef()

            else:
                Container, DirChosen = RanDef()

            if CHEAT == "-cheat ":
                CheatBuilder(Container, DirChosen)

            WALLET = int(WALLET)

            InsertCoin(WALLET)

            LoadCoin("printcoins")

            WaitForMe("ffmpeg")

            Pfig("\nSneaver chose to open :" + str(DirChosen))

            time.sleep(1)

            while True:
                Reslt = PressStart(str(DirChosen))
                if Reslt is False:
                    Pfig("\n-Choosing another random game..-\n")
                    RESPAWN = False
                    LASTONE = False
                    Container, DirChosen = RanDef()
                    time.sleep(1)
                else:
                    RwFile(
                        "last.played",
                        str(
                            "DirChosen="
                            + str(DirChosen)
                            + "\nContainer="
                            + str(Container)
                        ).replace("//", "/"),
                        "w",
                    )
                    break

            ScreenResize("change")
            time.sleep(1)
            newmovie = str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M")) + ".mkv"

            Pfig("\n-Recording now-\n" + (newmovie))

            if RESPAWN is True:

                if (
                    os.path.exists(
                        DirSaves
                        + str(Container).replace(".smc", ".000").replace(".sfc", ".000")
                    )
                    is True
                ):
                    cmd = (
                        "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                        + str(DirData)
                        + "sneaver.conf -maxaspect -fullscreen -xvideo "
                        + CHEAT
                        + str(DirChosen)
                        + "/"
                        + str(Container)
                        + " -loadsnapshot "
                        + str(
                            DirSaves
                            + str(Container)
                            .replace(".smc", ".000")
                            .replace(".sfc", ".000")
                        ).replace("//", "/")
                    )
                    Pfig("-Respawn using QuickSave.000-")
                    print(str(cmd) + "\n")

                elif (
                    os.path.exists(
                        DirSaves
                        + str(Container)
                        .replace(".smc", ".oops")
                        .replace(".sfc", ".oops")
                    )
                    is True
                ):

                    cmd = (
                        "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                        + str(DirData)
                        + "sneaver.conf -maxaspect -fullscreen -xvideo "
                        + CHEAT
                        + str(DirChosen)
                        + "/"
                        + str(Container)
                        + " -loadsnapshot "
                        + str(
                            DirSaves
                            + str(Container)
                            .replace(".smc", ".oops")
                            .replace(".sfc", ".oops")
                        ).replace("//", "/")
                    )
                    Pfig("\n-Respawn using AutoSave.oops-\n")
                    print(str(cmd) + "\n")

                else:
                    Pfig("\n-Error: [RESPAWN] No Auto-Save Found.-\n")
                    cmd = (
                        "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                        + str(DirData)
                        + "sneaver.conf -maxaspect -fullscreen -xvideo "
                        + CHEAT
                        + str(DirChosen)
                        + "/"
                        + str(Container)
                    ).replace("//", "/")
            else:
                cmd = (
                    "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                    + str(DirData)
                    + "sneaver.conf -maxaspect -fullscreen -xvideo "
                    + CHEAT
                    + str(DirChosen)
                    + "/"
                    + str(Container)
                ).replace("//", "/")

            Pfig("\n-Launching Snes9x-\n")
            print(cmd)
            sneaver = subprocess.Popen(cmd, shell=True)

            cmd = (
                "padsp ffmpeg -y -loglevel error -f pulse -ar 32000 -i "
                + str(devsound)
                + " -f x11grab -r 24 -s "
                + str(NEWRES)
                + " -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 "
                + str(DirChosen)
                + "/"
                + str(newmovie)
            ).replace("//", "/")

            Pfig("\n-Recording Screen-\n")
            print(cmd)
            ffmpeg = subprocess.Popen(cmd, shell=True)
            failsafe = False
            while True:
                WaitForMe("snes9x")

                if ERROR is True:
                    GifLauncher("Error")
                    time.sleep(1)
                    WALLET = WALLET + 1
                    pkill = subprocess.Popen("pkill ffmpeg", shell=True)
                    time.sleep(1)
                    WaitForMe("ffmpeg")
                    pkill = subprocess.Popen("pkill ffmpeg", shell=True)  # just in case
                    LenCheck(DirChosen, newmovie)
                    time.sleep(1)
                    if SMARTCRASH is False:
                        Pfig("\n-Changing back Screen Resolution-\n" + str(OLDSCREEN))
                        ScreenResize("revert")
                        time.sleep(
                            1
                        )  # tmpfix to wait for screen before launchin ffmpeg
                    cmd = "xset r on"
                    xset = subprocess.Popen(cmd, shell=True)
                    while True:
                        if SMARTCRASH is True:
                            GoodToGo = False
                            CrashDate = datetime.datetime.now().replace(tzinfo=None)

                            if CrashRom != Container:
                                CrashRom = Container
                                CrashCounter = 1
                                LastCrashDate = datetime.datetime.now().replace(
                                    tzinfo=None
                                )
                                Pfig("-SmartCrash:-")
                                Pfig("-Crash timer started-")
                                GoodToGo = True
                            else:

                                try:
                                    ElapsedCrash = CrashDate - LastCrashDate
                                    if ElapsedCrash.total_seconds() <= 300:
                                        CrashCounter += 1
                                        Pfig("-SmartCrash:")
                                        Pfig("-CrashCounter:%s-" % str(CrashCounter))
                                    else:
                                        if CrashCounter > 1:
                                            CrashCounter -= 1
                                        GoodToGo = True
                                except Exception as e:
                                    print("SmartCrashError:", str(e))

                                if CrashCounter >= 3:
                                    Pfig("-SmartCrash:-")
                                    RwFile("bad.roms", str(Container), "a")
                                    Pfig("-Rom: " + str(Container) + " Blacklisted..-")
                                    CrashCounter = 0
                                else:
                                    LastCrashDate = datetime.datetime.now().replace(
                                        tzinfo=None
                                    )
                                    GoodToGo = True

                            if GoodToGo is True:
                                newmovie = (
                                    str(
                                        datetime.datetime.now().strftime(
                                            "%y-%m-%d-%H-%M"
                                        )
                                    )
                                    + ".mkv"
                                )

                                if (
                                    os.path.exists(
                                        DirSaves
                                        + str(Container)
                                        .replace(".smc", ".000")
                                        .replace(".sfc", ".000")
                                    )
                                    is True
                                ):

                                    cmd = (
                                        "padsp ffmpeg -y -loglevel error -f pulse -ar 32000 -i "
                                        + str(devsound)
                                        + " -f x11grab -r 24 -s "
                                        + str(NEWRES)
                                        + " -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 "
                                        + str(DirChosen)
                                        + "/"
                                        + str(newmovie)
                                    ).replace("//", "/")

                                    Pfig("\n-Recording Screen-\n")
                                    #                                    ScreenResize("change")
                                    print(cmd)
                                    time.sleep(1)
                                    ffmpeg = subprocess.Popen(cmd, shell=True)
                                    cmd = (
                                        "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                                        + str(DirData)
                                        + "sneaver.conf -maxaspect -fullscreen -xvideo "
                                        + CHEAT
                                        + str(DirChosen)
                                        + "/"
                                        + str(Container)
                                        + " -loadsnapshot "
                                        + str(
                                            DirSaves
                                            + str(Container)
                                            .replace(".smc", ".000")
                                            .replace(".sfc", ".000")
                                        ).replace("//", "/")
                                    )
                                    Pfig("-Respawn using QuickSave.000-")
                                    print(str(cmd) + "\n")
                                    sneaver = subprocess.Popen(cmd, shell=True)
                                elif (
                                    os.path.exists(
                                        DirSaves
                                        + str(Container)
                                        .replace(".smc", ".oops")
                                        .replace(".sfc", ".oops")
                                    )
                                    is True
                                ):

                                    cmd = (
                                        "padsp ffmpeg -y -loglevel error -f pulse -ar 32000 -i "
                                        + str(devsound)
                                        + " -f x11grab -r 24 -s "
                                        + str(NEWRES)
                                        + " -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 "
                                        + str(DirChosen)
                                        + "/"
                                        + str(newmovie)
                                    ).replace("//", "/")
                                    Pfig("\n-Recording Screen-\n")
                                    print(cmd)
                                    ffmpeg = subprocess.Popen(cmd, shell=True)

                                    cmd = (
                                        "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                                        + str(DirData)
                                        + "sneaver.conf -maxaspect -fullscreen -xvideo "
                                        + CHEAT
                                        + str(DirChosen)
                                        + "/"
                                        + str(Container)
                                        + " -loadsnapshot "
                                        + str(
                                            DirSaves
                                            + str(Container)
                                            .replace(".smc", ".oops")
                                            .replace(".sfc", ".oops")
                                        ).replace("//", "/")
                                    )
                                    Pfig("\n-Respawn using AutoSave.oops-\n")
                                    print(str(cmd) + "\n")
                                    sneaver = subprocess.Popen(cmd, shell=True)
                                else:
                                    failsafe = True
                                    Pfig("\n-Error: [RESPAWN] No Auto-Save Found.-\n")

                                break

                        answer = input(
                            "Snes9x has crashed would you like to restart the game using the last autosave ? (y/n):"
                        )
                        if answer == "y":

                            newmovie = (
                                str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
                                + ".mkv"
                            )

                            if (
                                os.path.exists(
                                    DirSaves
                                    + str(Container)
                                    .replace(".smc", ".000")
                                    .replace(".sfc", ".000")
                                )
                                is True
                            ):

                                cmd = (
                                    "padsp ffmpeg -y -loglevel error -f pulse -ar 32000 -i "
                                    + str(devsound)
                                    + " -f x11grab -r 24 -s "
                                    + str(NEWRES)
                                    + " -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 "
                                    + str(DirChosen)
                                    + "/"
                                    + str(newmovie)
                                ).replace("//", "/")

                                ScreenResize("change")
                                time.sleep(1)
                                Pfig("\n-Recording Screen-\n")
                                print(cmd)
                                ffmpeg = subprocess.Popen(cmd, shell=True)

                                cmd = (
                                    "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                                    + str(DirData)
                                    + "sneaver.conf -maxaspect -fullscreen -xvideo "
                                    + CHEAT
                                    + str(DirChosen)
                                    + "/"
                                    + str(Container)
                                    + " -loadsnapshot "
                                    + str(
                                        DirSaves
                                        + str(Container)
                                        .replace(".smc", ".000")
                                        .replace(".sfc", ".000")
                                    ).replace("//", "/")
                                )
                                Pfig("-Respawn using QuickSave.000-")
                                print(str(cmd) + "\n")
                                sneaver = subprocess.Popen(cmd, shell=True)
                            elif (
                                os.path.exists(
                                    DirSaves
                                    + str(Container)
                                    .replace(".smc", ".oops")
                                    .replace(".sfc", ".oops")
                                )
                                is True
                            ):

                                cmd = (
                                    "padsp ffmpeg -y -loglevel error -f pulse -ar 32000 -i "
                                    + str(devsound)
                                    + " -f x11grab -r 24 -s "
                                    + str(NEWRES)
                                    + " -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 "
                                    + str(DirChosen)
                                    + "/"
                                    + str(newmovie)
                                ).replace("//", "/")
                                Pfig("\n-Recording Screen-\n")
                                print(cmd)
                                ffmpeg = subprocess.Popen(cmd, shell=True)

                                cmd = (
                                    "/usr/bin/padsp snes9x -setrepeat -nostdconf -conf "
                                    + str(DirData)
                                    + "sneaver.conf -maxaspect -fullscreen -xvideo "
                                    + CHEAT
                                    + str(DirChosen)
                                    + "/"
                                    + str(Container)
                                    + " -loadsnapshot "
                                    + str(
                                        DirSaves
                                        + str(Container)
                                        .replace(".smc", ".oops")
                                        .replace(".sfc", ".oops")
                                    ).replace("//", "/")
                                )
                                Pfig("\n-Respawn using AutoSave.oops-\n")
                                print(str(cmd) + "\n")
                                sneaver = subprocess.Popen(cmd, shell=True)
                            else:
                                failsafe = True
                                Pfig("\n-Error: [RESPAWN] No Auto-Save Found.-\n")
                            break

                        if answer == "n":
                            while True:
                                badanswer = input(
                                    "Would you like to blacklist this rom ? (y/n):"
                                )
                                if badanswer == "y":
                                    RwFile("bad.roms", str(Container), "a")
                                    Pfig("Rom: " + str(Container) + " Blacklisted..")
                                    break
                                if badanswer == "n":
                                    break
                            break
                if ERROR is True:
                    ERROR = False
                else:
                    break
            pkill = subprocess.Popen("pkill ffmpeg", shell=True)
            WaitForMe("ffmpeg")
            time.sleep(1)

            Pfig("\n-Changing back Screen Resolution-\n" + str(OLDSCREEN))
            ScreenResize("revert")
            time.sleep(1)
            if failsafe is False:
                LenCheck(DirChosen, newmovie)
            time.sleep(1)


##TouchDown##


GetOut()
