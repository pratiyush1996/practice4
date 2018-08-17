fw = open("sample.txt","w")
fw.write("hey! my name is pratiyush\n")
fw.write("i am searching for a job\n")
fw.close()

fr = open("sample.txt","r")
txt=fr.read()
print(txt)
fr.close()