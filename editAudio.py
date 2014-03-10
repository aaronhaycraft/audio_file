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
  dir='C:\\Users\\Pilot\\My Documents\\CST 205\\pictures\\'
  if not os.path.exists(dir):
    os.makedirs(dir)
  x=0
  y=0
  value=0
  data = requestInteger("Please enter a picture size: ")
  picture=makeEmptyPicture(data,data)
  #setcolor(getpixel, getcolor)
  file=pickAFile()
  sound=makeSound(file)
  overall=(getNumSamples(sound))/(data*data)
  int(overall)
  #printNow (overall)
  #printNow (data)
  #printNow (getNumSamples(sound))
  pixelArray=getPixels(picture)
  pixelIndex=0
  for k in range (0, data):
    for i in range (0, data):
      total=0
      for j in range (0, overall):
        total+=getSampleValueAt(sound, ((k*i)*overall)+j)
      avg=total/overall
      if (avg<-50):
        pixelArray[pixelIndex].setColor(red)
      elif(avg>20):
        pixelArray[pixelIndex].setColor(blue)
      elif(avg>-50):
        pixelArray[pixelIndex].setColor(yellow)
      pixelIndex+=1
    value=value+1
    if(value<10):
      writePictureTo(picture, dir+'photo000'+str(value)+'.jpg')
    elif(value<100):
      writePictureTo(picture, dir+'photo00'+str(value)+'.jpg')
    elif(value<1000):
      writePictureTo(picture, dir+'photo0'+str(value)+'.jpg')
    else:
      writePictureTo(picture, dir+'photo'+str(value)+'.jpg')
  show(picture)
  mov = makeMovieFromInitialFile(pickAFile())
  writeAVI(mov, dir+'newMovie.avi', 20)