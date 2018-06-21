
from celery_server.library import *

from pathlib import Path
from celery import chain
from celery import group

allCommands=['add','minus','mul']
allWorkflows=['chain','group']
def main():
	commands=[]
	workflow=[]
	file1=open('workflow.txt','r')
	data=file1.read().splitlines()

	for line in data:
		newList=line.split(",")
		checkValid(newList)
		if(newList[0] in allCommands):

			commands.append(newList)
		elif(newList[0] in allWorkflows):
			workflow.append(newList)


	##print (commands)
	##print (workflow)
	parallelProcess(commands,workflow)







def checkValid(input):
	title=input[0]
	##print (title)
	if(not (title in allCommands or title in allWorkflows)):
		raise Exception('Library does not have such command!')
	if(title in allCommands):

		if(len(input)!=4):
			raise Exception('argument number incorrect!')


def parallelProcess(commands,workflow):
	if(len(workflow)==0 or workflow[0]=='group'):
		for i in commands:
			string=runCommand(i)+".delay()"
			exec(string)


	else:
		overallflow=""

		for i in workflow:
			groupString=""
			chainString=""
			if(i[0]=='group'):
				for j in range(1,len(i)):
					index=int(i[j])
					if(groupString==""):
						groupString+=runCommand(commands[index])
					else:
						groupString+=","+runCommand(commands[index])
				groupString="group("+groupString+")"
				if(overallflow==""):
					overallflow+=groupString
				else:
					overallflow+="|"+groupString
			elif(i[0]=='chain'):
				for j in range(1,len(i)):
					index=int(i[j])
					##print (index)
					##print (allCommands)
					if(chainString==""):
						chainString+=runCommand(commands[index])
					else:
						chainString+=","+runCommand(commands[index])

				chainString="chain("+chainString+")"
				if(overallflow==""):
					overallflow+=chainString
				else:
					overallflow+="|"+chainString

		
		##print (overallflow)	
		#overallflow+=".apply_async()"		
		overallflow="("+overallflow+").delay()"
		print (overallflow)
		exec (overallflow)
		
		##res=chain(library.add.s(/home/derek/celery_client_combined/sample0.txt,/home/derek/celery_client_combined/result0.txt,3),library.mul.s(/home/derek/celery_client_combined/sample1.txt,/home/derek/celery_client_combined/result1.txt,3))
		##res=chain(haha.s())
		##add.delay("sample0.txt","result0.txt",3)
		##res=chain(add.s(sample0.txt,result0.txt,3))
		##res.apply_async()




def runCommand(input):
	##print(input[1])
	##print(input[2])
	##print(input[3])
	if(input[0]=='add'):
		return 'add.si('+str(input[1])+","+str(input[2])+","+str(int(input[3]))+")"
	elif(input[0]=='minus'):
		return 'minus.si('+str(input[1])+","+str(input[2])+","+str(int(input[3]))+")"
	elif(input[0]=='mul'):
		return "mul.si("+str(input[1])+","+str(input[2])+","+str(int(input[3]))+")"


main()