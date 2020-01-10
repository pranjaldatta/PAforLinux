import json
import argparse
import os
import requests

def main(task, pyfile):
    with open("/home/pranjal/Projects/PAforLinux/src/modules/tasks.json",mode="r") as f:
        tasks_file = json.load(f)
        #print(f.read())
        #f.close()
    tasks_file['available_tasks'][task] = pyfile    
    with open(os.path.join(os.path.dirname(__file__), "tasks.json"), mode='w') as f:
        json.dump(tasks_file, f, indent=4)

parser = argparse.ArgumentParser(description="Adds a new task to tasks.json")
parser.add_argument("-t", "--task", help="task name",action="store")
parser.add_argument("-p", "--pyfile", help="name of task entry file", action="store")
args = parser.parse_args()

main(args.task, args.pyfile)