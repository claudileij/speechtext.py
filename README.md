# Speechtext.py
## Initialization
Clonning speechtext repository:
```bash
git clone https://github.com/nxSlayer/speechtext.py.git
cd speechtext.py
```
Installing the requirements:
```bash
pip install -r requirements.txt
```

## Usage
In your project, import the speechtext.py class:
```py
from speechtext import SpeechText
```
and init this class with api_key argument:
```py
api = SpeechText('your_api_key')
```
start an task:
```py
file = "your file path, url or bytes"
task = api.startTask(file=file)

print(task.status)
print(task.createdAt)
print(task.id)

# GETTING TASK RESULT
# Obs: time.sleep is recommended

result = api.taskResult(taskId=task.id)
print(result.status) # failed | finished
print(result.remainingSeconds) # int
print(result.transcript) # transcribed text
print(result.word_time_offsets) #list
```

## Get your free api key
Register in [speechtext.ai](https://speechtext.ai/signup/) and receive your free trial key in email

## Documentation
If you are looking for other solutions, you can look at the [speechtext.ai docs](https://speechtext.ai/speech-api-docs`enter code here`)
