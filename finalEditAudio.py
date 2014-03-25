# Aaron Haycraft
# March 26, 2014
# 2nd Project
# Creating picture/video from audio file.

# Libraries imported for GUI
import javax.swing as swing
import os
import java

# deleteDir() function is necessary to delete the directory if it exists.
def deleteDir():
  if os.path.exists(dir):
    import shutil
    shutil.rmtree('C:\\Users\\Pilot\\My Documents\\CST 205\\pictures\\')
  
# The class GUI is where the Graphical User Interface (GUI) is stored. By using this class
# and creating an object for it, you will be able to use the value that is entered and pass
# it into the audio function to edit the audio files. 
class GUI(swing.JFrame):
    def __init__(self):
      # Initializes the window
      swing.JFrame.__init__(self, title="Video Maker", size=(200,200))
      
      # Sets the layout for the window
      self.contentPane.layout=java.awt.FlowLayout()
      
      # Adds a text field to enter data into
      self.field=swing.JTextField(size=(200,60))
      self.field.text="200"
      self.contentPane.add(self.field)
      
      # Provides a button to send the number entered in the text field to the variable
      setSize = swing.JButton("Create Size", size=(65,30), actionPerformed=self.checkContents)
      self.contentPane.add(setSize)
      
      # Makes the GUI visible
      self.visible=1
    
    # This function will set the value that will be passed into the function below    
    def checkContents(self,event):
      if self.field.text=="200":
        self.value=200
      elif self.field.text=="300":
        self.value=300
      elif self.field.text=="400":
        self.value=400

# This function will set a directory, and will start by accepting the value that is created back in the class.
# After the size of the picture is passed in, the user will be prompted to choose a .wav file. After the .wav
# is chosen, the program will then set pixels in a picture to a specific color, depending on what the average
# sample value is. After a row is formed, the picture will then be output to files, preparing for the creation
# of a movie. Once all the pictures are created, there will be a prompt to select the first photo of the file
# to use for the movie. A movie will then be created of the pictures and how they were created piece by piece.
def useAudio(t):
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