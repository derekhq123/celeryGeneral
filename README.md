# celeryGeneral
general celery framework for data parallel processing

Author: Du Li

How to use it:

This framework has two parts: server part and job submission part.


Server: 

build the framework and start the service.

change path to celery_client_combined file

open terminal and enter in:

celery -A celery_server worker --loglevel=info -c N (N: number of processers, default value: number of CPU in your computer)

and it will run successfully

(tips: if you want to change the server configuration, please edit celerycongi.py file)



Job submission:

Users can define function they want to use and the workflow to run these functions

All functions is defined in celery_server/library.py file

Users can write their command in workflow.txt


workflow.txt format:

two types of command: function call and workflow call

one command per line

function call: function name,parameter

eg :add,sourcefile,targetfile,number

workflow call: workflow type, index of function call (starting from 0)

workflow type:

  chain: functions are run in sequence
  
  group: functions are run in parallel

eg: group,0,1

    chain,2,3
    
(tips: workflow command are set in chain execution in default. Take eg as example, the chain,2,3 command will run after group,0,1
  
