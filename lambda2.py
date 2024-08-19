import json
import base64
import boto3
s3 = boto3.resource('s3')
runtime= boto3.client('runtime.sagemaker')

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2024-08-19-10-52-35-440'  # Adjust if needed
def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    # Instantiate a Predictor
    predictor= runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='image/png', Body=image)
    # For this model the IdentitySerializer needs to be "image/png"
    #predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction and deserialize:
    event["inferences"] = json.loads(predictor['Body'].read().decode('utf-8'))
    return {
        'statusCode': 200,
        # 'body': json.dumps(event)
        "body": {
            "image_data": event["body"]['image_data'],
            "s3_bucket": event["body"]['s3_bucket'],
            "s3_key": event["body"]['s3_key'],
            "inferences": event['inferences'],
       }
    }