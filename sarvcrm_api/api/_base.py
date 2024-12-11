
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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(client: SarvClient)'

    def __str__(self) -> str:
        return f'<SarvModule {self.label_en}>'