import json
import botocore
import boto3

print('botocore vertion: {0}'.format(botocore.__version__))
print('boto3 vertion: {0}'.format(boto3.__version__))
client = boto3.client('connect');
#     instanceId = event['ResourceProperties']['InstanceId']
#     botName = event['ResourceProperties']['BotName']
#     lexRegion = event['ResourceProperties']['LexRegion']

#     if event['RequestType'] == 'Delete':
#       response = client.disassociate_lex_bot(
#         InstanceId=instanceId,
#         BotName=botName,
#         LexRegion=lexRegion
#       )
#       cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
#     else: 
instanceId = 'db46751d-34d8-495c-98a1-0e5f69275895'
botName='MyBot'
lexRegion='ap-northeast-1'
response = client.associate_bot(
    InstanceId=instanceId,
    LexV2Bot={
      'AliasArn': 
    }
)
#       cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
#   except Exception as e:
#     print(e)
#     cfnresponse.send(event, context, cfnresponse.FAILED, {})