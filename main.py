import  json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']
table = dynamodb.Table(TABLE_NAME)


def handler(event,context):
    print('--------------------------------')
    try:
        print(TABLE_NAME)
        response = table.scan()
        items   = response['Items']
        print(json.dumps(items))
        print(len(response['Items']))
        
        if len(response['Items']) == 0:
            res = {
            "statusCode": 200,
            "body":"No data"
        }
           
        else:
            res = {
                'statusCode': 200,
                 'headers': {
                'Content-Type': 'application/json',
        },
                'body': json.dumps(items)
            }
        return res
           
    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
                
        }
    
    
    
    