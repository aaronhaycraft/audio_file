def soundExplore():
  fileName=pickAFile()
  aSound=makeSound(fileName)
  print "Information about aSound", aSound
  print "Getting first sample:", getSampleValueAt(aSound, 0)
  print "Getting the length:", getLength(aSound)
  print "Getting sampling rate:", getSamplingRate(aSound)
  play(aSound)
  blockingPlay(aSound)
  playAtRate(aSound,2.0)
  explore(aSound)
  return aSound
  
def returnSound():
  filename=pickAFile()
  newSound=makeSound(filename)
  print getLength(newSound)
  return newSound
  
def increaseVolume(sound):
   for sample in getSamples(sound):
     value =getSampleValue(sample)
     setSampleValue(sample,value*2)
  
def increaseVolume2(sound):
  for index in range(0, getLength(sound)):
    value =getSampleValueAt(sound,index)
    setSampleValueAt(sound,index,value*2)
    
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
    
def increaseRange(sound):
  soundValue = 0
  first = int(getLength(sound)/3)
  second = int(2*getLength(sound)/3)  
  file1 = makeEmptySound(first, 44100)
  file2 = makeEmptySound(second, 44100)
  file3 = makeEmptySound(getLength(sound), 44100)
  
  #play(sound)
  
  for sample in range(0, first):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(file1, sample, value*200)
  
  
  
  for sample in range(first-1, second):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(file2, sample, value*200)
  
  
  
  for sample in range(second-1, getLength(sound)):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(file3, sample, value*200)
  
  blockingPlay(file1)
  blockingPlay(file2)
  blockingPlay(file3)
    
  #play(file3)
  
  #for sample in range(0, first):
    #setSampleValueAt(file1, sample, getSampleValueAt(sound, sample)*150)
   # soundValue = soundValue + 1
  #explore(file1)
  
  #blockingPlay(file1)        
  
  