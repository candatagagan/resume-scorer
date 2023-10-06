from boto3 import resource


class _Actions:

    def __init__(self, table_name):
        self.table_name = table_name



    def insert(self, item):
        dynamo_table = resource('dynamodb').Table(self.table_name)
        response = dynamo_table.put_item(
            Item=item)

