import sys
sys.dont_write_bytecode = True
import requests
from utilities import taskResponse
from typing import Union

class SpeechText(requests.Session):
    """
    `SpeechText` - A class to wrapper the speechtext.ai api

    `**Parameters**``
    - `api_key` - The speechtext.ai api key.
    - `lang` - The transcribe language.
    """

    def __init__(self, api_key: str, lang: str = "en-US") -> None:
        super().__init__()
        self.api = "https://api.speechtext.ai"
        self.api_key = api_key
        self.lang = lang

    def prepare_task(self, file, format, punctuation):
        params = {"key": self.api_key, "language": self.lang, "format": format, "punctuation": punctuation}
        if isinstance(file, str) and any(schema in file for schema in ["http://", "https://"]):
            params['url'] = file
            return (params, self.get, None)
        else:
            self.headers['content-type'] = 'application/octet-stream'
            return (params, self.post, file)
        

    def startTask(self, file: Union[str, bytes], format: str = "mp3", punctuation: bool = False):
        """
        `startTask` - A function to start transcribe task

        `**Parameters**``
        - `file` - str (File path, file url) or bytes of the file.
        - `lang` - The transcribe language.
        """

        if isinstance(file, str) and not any(schema in file for schema in ["http://", "https://"]):
            with open(file, 'rb') as f:
                file = f.read()

        request = self.prepare_task(file, format, punctuation)
        response = request[1](f"{self.api}/recognize", params=request[0], data=request[2])
        if response.status_code == 200:
            return taskResponse.startTask(response.json())
        else:
            raise Exception(response.text)
    
    def taskResult(self, taskId: str):
        """
        `taskResult` - get transcribed task result

        `**Parameters**``
        - `taskId` - the id of created task
        """

        response = self.get(f"{self.api}/results", params={"key": self.api_key, "task": taskId})
        if response.status_code == 200:
            return taskResponse.taskResult(response.json())
        else:
            raise Exception(response.text)
    
