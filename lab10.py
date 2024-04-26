#!/usr/bin/python3


#Problem 1

def throw_me_an_error():
  val1 = 14
  val2 = 0
  return val1 / val2

try:
  throw_me_an_error()
except Exception as e:
  print(e)


#Problem 2
#The purpose of the finally block is to run regardless of whether or not there is 
#an error in the try block. In this case, if the file was successfully opened in the try
#block, then the finally block makes sure that the file was closed.


#Problem 3:
import json

# Invalid JSON data
data = "{'invalid_json_key': 'value'}"

try:
  # Attempt to load the JSON data
  dataLoad = json.loads(data)
except json.JSONDecodeError as e:
  # Print the JSON import error
  print(f"JSON import error: {e}")
