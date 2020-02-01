## Guidelines for adding your own 'Tasks'

Any functionality of the Personal Assistant is called a 'Task'. All task related files are in the [modules](https://github.com/pranjaldatta/PAforLinux/tree/master/src/modules) directory. So if you are adding a custom task, follow the 
guidelines below: 

1. All Task related files **must** remain in modules directory. Any folder that the files may need must be in the *src/modules/*
directory. If the task needs multiple .py files and/or other dependencies, they all must be put inside a task specific folder *src/modules/task_name/*  with a single driver file outside that can be referenced. Essentially, a single driver must be there that acts as the driver file that can be referenced by the personal-assistant.

2. In the *src/modules/* directory, run the following command
```
python3 add_task.py -t <task-name> -p <driver py file> 
```
 Your task has been added!

