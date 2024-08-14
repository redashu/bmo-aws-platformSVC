import os 
import boto3 
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def handler(event, context):
    items = [
        {'id': 1 , 'name': 'ashutoshh',  'remarks': 'good one'},
        {'id': 2 , 'name': 'pascal',  'remarks': 'very good one'}
    ]
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': 'data inserted successfully'
    }