#!/usr/bin/python3
import os,sys,random,subprocess,datetime

ScriptDir = os.path.dirname(os.path.abspath(__file__))
DirMovies = ScriptDir+"/Movies/"

if len(sys.argv) >1:
     
     if sys.argv[1] == "-record":
          RECMOD = True
     else:
          RECMOD = False
     if sys.argv[1] == "-h" or sys.argv[1] == "--help":
          print("\n**Sneaver is a script playing random movie from snes games.\n\n**Download a rom put it in its folder inside the Movies directory\n\n**Then launch sneaver ^^\n\n**Use : sneaver -record to play and record a random game (there are no sounds during recording to avoid desync)\n\n**Have fun !!\n")
          print()
          sys.exit(1)
     
else:
     RECMOD = False


def rename(name,srcdir):

  badchar= ["(",")","[","!","]"," ","_","--","'",'"',","]

  mv = False
  for char in badchar:
     if char in name:
          mv = True
  if mv == True:
     print("English Mothar Fuckar Do You Speak It ?!\nHave To Rename : ",name)
     newname = name.replace("(","-").replace(")","-").replace("[","-").replace("!","-").replace("]","").replace(" ","-").replace("_","-").replace("'","-").replace('"',"-").replace(",","-").replace("--","-")
     newname = newname.replace("--","-")
     os.rename(srcdir+name,srcdir+newname.replace("--","-"))
     print("\nNew Name is : ",newname)


while True:
     movfile = None
     romfile = None
     insertcoin = True


     MovLst = [i for i in os.listdir(DirMovies)]
     for name in MovLst:
          rename(name,DirMovies)

     MovLst = [i for i in os.listdir(DirMovies)]

     try:
          rnd = random.randint(0,len(MovLst)-1)
          DirChosen = DirMovies+MovLst[rnd]
     except:
          print("Can't find anything !!!\nWhere am i ?\nPlease check what's in the Movies Folder ..")
          sys.exit(0)
     print("\nSneaver chose :",DirChosen)

     files = os.listdir(DirChosen)

     for name in files:
          rename(name,DirChosen+"/")

     files = os.listdir(DirChosen)

     movfiles = []

     for i in files:
          if i.endswith(".smc"):
               romfile = i
          if i.endswith(".sfc"):
               romfile = i
          if i.endswith(".smv"):
               movfiles.append(i)
     try:
          rnd = random.randint(0,len(movfiles)-1)
          movfile = movfiles[rnd]
     except:
          pass

     if movfile and romfile and RECMOD == False:

       cmd = "/usr/games/snes9x -nostdconf -conf "+ str(ScriptDir)+"/sneaver.conf -maxaspect -fullscreen -xvideo "+ str(DirChosen)+ "/" + str(romfile) + " -playmovie " + str(DirChosen)+ "/"  +str(movfile)

       print("\nLaunching : \n",cmd)

       sneaver = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       output,error = sneaver.communicate()
       snout= output.decode()

       if "Movie replay" in snout:
                    insertcoin = False
                    break

       if "Movie end" in snout:
                    insertcoin = False
                    break
       if "usage: snes9x [options]" in snout:
                    print("!!!!!!!!!!!\nError while launching snes9x!!\n!!!!!!!!!!!\n")
     
                    insertcoin = False
                    break

       if insertcoin == True:
               newromname = movfile+".notworking"
               print("\n Renaming %s to %s ..\n"%(movfile,newromname))
               os.rename(DirChosen+"/"+movfile,DirChosen+"/"+newromname)
               break

     else:

         

          if movfile == None:
               print("!!!!!\nHavn't found any movie files ..\n!!!!!!")
               insertcoin = True

          if romfile == None:
               print("!!!!!\nHavn't found any rom files ..\n!!!!!")
               insertcoin = False

          if RECMOD == True and romfile != None:
               print("!!!!!\nRECMOD Activated .\n!!!!!")
               break


if insertcoin == True:

  if RECMOD == False:
     credit = input("\n!!!!!!!!!!!!!!!!!!!!!!\nSomething went wrong with that replay ..\nWould you like to save your own movie ?\nYou may need to edit sneaver.record.conf according to your controller device.\n\nType 'yes' or anything else to quit :")
     if credit == "yes":
          newmovie =str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))+".smv"
          print("\nRecording now to : ",newmovie)

          cmd = "/usr/games/snes9x -nostdconf -conf "+ str(ScriptDir)+"/sneaver.record.conf -maxaspect -fullscreen -xvideo "+ str(DirChosen)+ "/" + str(romfile) + " -recordmovie " + str(DirChosen)+ "/" +str(newmovie)

          print("\nLaunching : \n",cmd)

          sneaver = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
          snout = sneaver.communicate()[0]
          print(snout)
          wait = sneaver.wait()
          print("\n--!!Recorded!!--\n")

  if RECMOD == True:

          newmovie =str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))+".smv"
          print("\nRecording now to : ",newmovie)

          cmd = "/usr/games/snes9x -nostdconf -conf "+ str(ScriptDir)+"/sneaver.record.conf -maxaspect -fullscreen -xvideo "+ str(DirChosen)+ "/" + str(romfile) + " -recordmovie " + str(DirChosen)+ "/" +str(newmovie)

          print("\nLaunching : \n",cmd)

          sneaver = subprocess.Popen(cmd,shell=True)
          snout = sneaver.communicate()[0]
          print(snout)
          wait = sneaver.wait()
          print("\n--!!Recorded!!--\n")



else:
     print("\n\t\t==Sneaver exited==\n\n")
     sys.exit(1)

print("\n\t\t==Sneaver exited==\n\n")
sys.exit(1)
