from celery_server import app


@app.task
def add(sourcefile,targetfile,num):
	file1=open(sourcefile,"r")
	data=file1.readlines()
	file1.close()
	file2=open(targetfile,"w")
	output=[]
	for line in data:
		number=int(line)+int(num)
		output.append(str(number))

	file2.write("\n".join(output))
	file2.close()

@app.task
def minus(sourcefile,targetfile,num):
	file1=open(sourcefile,"r")
	data=file1.readlines()
	file1.close()
	file2=open(targetfile,'w')
	output=[]
	for line in data:
		number=int(line)-int(num)
		output.append(str(number))
	file2.write("\n".join(output))
	file2.close()



@app.task
def mul(sourcefile,targetfile,times):
	file1=open(sourcefile,'r')
	data=file1.readlines()
	file1.close()
	file2=open(targetfile,'w')
	output=[]
	for line in data:
		number=int(line)*int(times)
		output.append(str(number))
	file2.write("\n".join(output))
	file2.close()

@app.task
def haha():
	print ('haha')