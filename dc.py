from flytekit import task, workflow
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class MyDataClass:
    a: int
    b: str

@task
def t(x: MyDataClass):
    ...


@workflow
def wf(x: MyDataClass):
    t()
