import javax.swing as swing
import os
import java

def GUI_start():
  window = swing.JFrame("Test",size=(300,300))
  text_field=swing.JTextField(preferredSize=(300, 20))
  text_field.text = "Welcome to test sample!"
  window.contentPane.add(text_field)
  window.visible=1
  button = swing.JButton("View", preferredSize=(300, 20))
  window.contentPane.add(button)
  window.visible=1
  window.pack()
  window.visible=1
  
class VideoMaker(swing.JFrame):
    def __init__(self):
      swing.JFrame.__init__(self, title="Video Maker", size=(200,200))
      self.contentPane.layout=java.awt.FlowLayout()
      
      self.field=swing.JTextField(size=(200,60))
      self.field.text="sample.jpg"
      self.contentPane.add(self.field)
      
      fileView = swing.JButton("Create Video", size=(65,30), actionPerformed=self.checkContents)
      self.contentPane.add(fileView)
      
      setFolder = swing.JButton("Set Folder", size=(65,40), actionPerformed=self.setFolder)
      self.contentPane.add(setFolder)
      
      self.visible=1
      
    def checkContents(self,event):
      if self.field.text.endswith(".jpg"):
        pic = makePicture(getMediaPath(self.field.text))
        show(pic)
      if self.field.text.endswith(".wav"):
        snd=makeSound(getMediaPath(self.field.text))
        play(snd)
    
    def setFolder(self,event):
      setMediaPath()

class FileContentsViewer(swing.JFrame):
  def __init__(self,directory):
    swing.JFrame.__init__(self, title="File Contents Viewer", size=(210,250))
    self.contentPane.layout = java.awt.BorderLayout()
    self.currentDirectory = directory
    self.files=swing.JList(os.listdir(self.currentDirectory))
    pane = swing.JScrollPane(self.files)
    self.contentPane.add(pane,java.awt.BorderLayout.CENTER)
    fileView = swing.JButton("View Contents", size=(65,30),
    actionPerformed=self.fileView)
    self.contentPane.add(fileView, java.awt.BorderLayout.SOUTH)
    self.pack()
    self.visible = 1
    
  def fileView(self,event):
    selected=self.files.getSelectedIndices()
    selectedFile = self.files.getModel( ).getElementAt( selected[0])
    selectedFile = self.currentDirectory+ "//"+ selectedFile
    if selectedFile.endswith(".jpg"):
      pic = makePicture(selectedFile)
      show(pic)
    if selectedFile.endswith(".wav"):
      snd = makeSound(selectedFile)
      play(snd)