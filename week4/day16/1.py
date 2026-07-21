import json
from DBHELPER3 import *
import datetime
from openai import OpenAI

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')

# OpenAI Initialization
openai_api_key = ''
client = OpenAI(api_key=openai_api_key)

# 1. Define a function to perfrom some action
def save_task(task):
     # Addint 2 more keys in task
     task['status'] = 'PENDING'
     task['created_at'] = datetime.datetime.now()
     db_helper.save(task)
     return 'Task saved successfully'

# 2. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "save_task",
        "description": "Save the task in MongoDB Atlas",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the Task",
                },
                "description": {
                    "type": "string",
                    "description": "Description of the Task",
                },
                "action": {
                    "type": "string",
                    "description": "Action of the Task can be call, message or email",
                },
                "contact_name": {
                    "type": "string",
                    "description": "Name of the contact person who will perfrom this Task",
                },
                "contact_phone": {
                    "type": "string",
                    "description": "Phone of the person who will perfrom this Task",
                }
            },
            "required": ["title", "description", "action", "contact_name", "contact_phone"],
        },
    },
]

# 4. Create a running input list we will add to over time
input_list = [
    {"role": "user", "content": "Call gourav on 9872898728 and assign a task to create 3 licenses for finlo for bus ticketing module for Jujhar group"}
]

# Prompt the model with tools defined
response = client.responses.create(
    model="gpt-4o-mini",
    tools=tools,
    input=input_list,
)

print("Output:")
llm_output = response.model_dump_json(indent=2) # string
# print(llm_output)

llm_output = json.loads(llm_output) # covert to dictionary


arguments = json.loads(llm_output['output'][0]['arguments'])
print('TASK Details')
print(arguments)

function_name = llm_output['output'][0]['name']
print('Function Name')
print(function_name)

type = llm_output['output'][0]['type']
print('type')
print(type)

if type == 'function_call':
     if function_name == 'save_task':
          save_task(arguments)