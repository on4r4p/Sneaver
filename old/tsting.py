#!/usr/bin/python3
import psutil,subprocess,re

#checkproc= [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'snes9x' in p.info['name']]

#while len(checkproc) > 0:
#     checkproc= [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'snes9x' in p.info['name']]

#print("\nSnes9x exited")


sneaver = subprocess.Popen("xrandr",shell=True,stdout=subprocess.PIPE)
snout = str(sneaver.communicate()[0])
reslist = []
goodone = False

if "connected primary" in snout:
     device = str(snout.split("connected primary")[0].split("\\n")[-1]).replace(" ","")
     snit = "".join(snout.split("connected primary")[1]).split("\\n")

for item in snit:
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
               goodone = True
          else:
               regex = re.compile(r'\d+[x]\d+')
               bingo =regex.search(item)

          if bingo:
               if not bingo.group() in reslist:
                    reslist.append(bingo.group())
  else:
          break

if goodone == True:
     sorting =[]
     for resolution in reslist:
          tmp = resolution.split("x")[0]
          sorting.append(tmp)
     sorting.sort(key=int)
     minwidth = sorting[0]

     for resolution in reslist:
               if resolution.startswith(minwidth) == True:
                    newscreen = "xrandr --output "+device+" --mode "+ str(resolution)
                    break
print()
print("--Backing up Current Screen Config ==")
oldscreen = "xrandr --output "+device+" --mode "+res
print(oldscreen)

print("--Changing Screen Resolution now--")
print(newscreen)
print()

