from typing import TypedDict


class ProfileInterface(TypedDict):
    name: str
    title: str
    email: str


profile_objects: ProfileInterface = {
    "name": "mamushi",
    "title": "typescriptのinterfaceみたいに書きたい。",
    "email": "test@hoge.com",
}
