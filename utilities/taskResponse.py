from typing import Union

class startTask:
    def __init__(self, json) -> None:
        self.data = json

    @property
    def status(self) -> Union[str, None]:
        return self.data.get('status')
    
    @property
    def createdAt(self) -> Union[str, None]:
        return self.data.get('created_at')
    
    @property
    def id(self) -> Union[str, None]:
        return self.data.get('id')
    
    def json(self) -> dict:
        return self.data

class taskResult:
    def __init__(self, json) -> None:
        self.data = json

    @property
    def status(self) -> Union[str, None]:
        return self.data.get('status')
    
    @property
    def remainingSeconds(self) -> Union[str, None]:
        return self.data.get('remaining seconds')
    
    @property
    def transcript(self) -> Union[str, None]:
        return self.data.get('results').get('transcript')
    
    @property
    def word_time_offsets(self) -> Union[str, None]:
        return self.data.get('results').get('word_time_offsets')
    
    def json(self) -> dict:
        return self.data