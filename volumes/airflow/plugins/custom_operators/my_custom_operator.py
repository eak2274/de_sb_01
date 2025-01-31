from airflow.models.baseoperator import BaseOperator

class MyCustomOperator(BaseOperator):

    def __init__(self, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        print(f"This is my param: {self.param}")