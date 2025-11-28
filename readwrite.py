
    #print(file.read(7))
    #print(file.readline())
    #print(file.readline())

  #  for line in file.readlines():
   #     print(line)
  # line = file.readline()
   #while line!="":
  #      print(line)
   #     line = file.readline()
with open('test.txt') as reader:
    content = reader.readlines()
    reversed(content)
with open('test.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)


   # for line in file.readlines():
      #  print(line)