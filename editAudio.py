def useAudio():
  dir='C:\\Users\\Pilot\\My Documents\\CST 205\\pictures\\'
  if not os.path.exists(dir):
    os.makedirs(dir)
  total=0
  data = requestInteger("Please enter a picture size: ")
  picture=makeEmptyPicture(data,data)
  for num in range(0,data/3):
    addLine(picture, num, 0, num, data, blue)
    total=total+1
    if(total<10):
      writePictureTo(picture, dir+'photo000'+str(total)+'.jpg')
    elif(total<100):
      writePictureTo(picture, dir+'photo00'+str(total)+'.jpg')
  for num in range(data/3,2*data/3):
    addLine(picture, num, 0, num, data, white)
    total=total+1
    if(total<100):
      writePictureTo(picture, dir+'photo00'+str(total)+'.jpg')
    elif(total<1000):
      writePictureTo(picture, dir+'photo0'+str(total)+'.jpg')
  for num in range(2*data/3,data):
    addLine(picture, num, 0, num, data, red)
    total=total+1
    if(total<1000):
      writePictureTo(picture, dir+'photo0'+str(total)+'.jpg')
  show(picture)
  mov = makeMovieFromInitialFile(pickAFile())
  writeAVI(mov, dir+'newMovie.avi', 20)
  #setcolor(getpixel, getcolor)
  avg=0
  file=pickAFile()
  sound=makeSound(file)
  overall=(getNumSamples(sound))/data
  int(overall)
  for i in range (0, overall):
    for x in range (0, data):
      avg+=(i*overall)+x
      print avg
      #setcolor(getPixel, getcolor)

def getAudio():
  file=pickAFile()
  sound=makeSound(file)
  print getLength(sound)
  print getSamplingRate(sound)
  explore(sound)
  
def deleteDir():
  import shutil
  shutil.rmtree('C:\\Users\\Pilot\\My Documents\\CST 205\\pictures\\')
  
def useAudio2():
  total=0
  data = requestInteger("Please enter a picture size: ")
  picture=makeEmptyPicture(data,data)
  #setcolor(getpixel, getcolor)
  file=pickAFile()
  sound=makeSound(file)
  overall=(getNumSamples(sound))/data
  int(overall)
  printNow (overall)
  printNow (data)
  printNow (getNumSamples(sound))
  for i in range (0, overall):
    avg=0
    for x in range (0, data):
      avg+=getSampleValueAt(sound, (i*data)+x)
    total=avg/data
    printNow(total)