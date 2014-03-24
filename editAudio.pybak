import javax.swing as swing
import os
import java

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
  
class VideoMaker(swing.JFrame):
    def __init__(self):
      #self.value=200
      swing.JFrame.__init__(self, title="Video Maker", size=(200,200))
      
      self.contentPane.layout=java.awt.FlowLayout()
      
      self.field=swing.JTextField(size=(200,60))
      self.field.text="200"
      self.contentPane.add(self.field)
      
      setSize = swing.JButton("Create Size", size=(65,30), actionPerformed=self.checkContents)
      self.contentPane.add(setSize)
      
      self.visible=1
      
    def checkContents(self,event):
      if self.field.text=="200":
        self.value=200
      elif self.field.text=="300":
        self.value=300
      elif self.field.text=="400":
        self.value=400

def useAudio3(t):
  dir='C:\\Users\\Pilot\\My Documents\\CST 205\\pictures\\'
  if not os.path.exists(dir):
    os.makedirs(dir)
  x=0
  y=0
  value=0
  data = t.value
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
        total+=getSampleValueAt(sound, ((k*overall*data)+(i*overall)+j))
      avg=total/overall
      if (avg<-50):
        pixelArray[pixelIndex].setColor(red)
      elif(avg<-25 and avg>=-50):
        pixelArray[pixelIndex].setColor(green)
      elif(avg<0 and avg>=-25):
        pixelArray[pixelIndex].setColor(blue)
      elif(avg<25 and avg>=0):
        pixelArray[pixelIndex].setColor(yellow)
      elif(avg<50 and avg>=25):
        pixelArray[pixelIndex].setColor(magenta)
      elif(avg>=50):
        pixelArray[pixelIndex].setColor(orange)
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