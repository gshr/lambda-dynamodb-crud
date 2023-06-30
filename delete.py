import  json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']
table = dynamodb.Table(TABLE_NAME)


def handler(event,context):
    try:
        query_params = event['queryStringParameters']
        value = query_params.get('uid')
        primary_key = {
        'uid':value
        }
        response  =table.delete_item(Key=primary_key)
        res = {
            'statusCode': 200,
                'headers': {
            'Content-Type': 'application/json',},
            'body': 'Data deleted successfully'
            }
        return res
           
    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
                
        }
    
    
    
    