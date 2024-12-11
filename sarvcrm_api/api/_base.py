
class SarvModule:
    api_path = ''
    label_en = 'BASE_CLASS'
    label_pr = 'کلاس اصلی'

    def __init__(self, client):
        self.client = client

    def create(*Args, **KWArgs) -> str:
        ...

    def read(*Args, **KWArgs) -> list:
        ...

    def read_list(*Args, **KWArgs) -> list:
        ...

    def update(*Args, **KWArgs) -> str:
        ...

    def delete(*Args, **KWArgs) -> str:
        ...
    
    def __str__(self):
        return f'<SarvModule {self.label_en}>'