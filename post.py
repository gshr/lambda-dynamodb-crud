import  json
import boto3
import os
from uuid import uuid4
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']
table = dynamodb.Table(TABLE_NAME)


def handler(event,context):
   
    try:
        body = json.loads(event['body'])
        print(body)
        item = {
        'uid': str(uuid4()),
        'name': body['name'],
        'age': body['age']
        }
        
        table.put_item(Item=item)
        response = {
        "statusCode": 201,
        "body": json.dumps(item)
        }
        return response
        
           
    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
                
        }
    
    
    
    