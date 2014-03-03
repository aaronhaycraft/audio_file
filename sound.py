def sound():
  file=pickAFile()
  s = makeSound(file)
  play(s)
  printNow(s)