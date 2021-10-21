import boto3
import csv

s3 = boto3.resource('s3',
	aws_access_key_id = 'AKIAU6PFDVGEZJCY6O2R',
	aws_secret_access_key = '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')

s3.create_bucket(Bucket = 'hw3dli3', CreateBucketConfiguration = {'LocationConstraint': 'us-west-2'})

dyndb = boto3.resource('dynamodb', region_name = 'us-west-2', aws_access_key_id = 'AKIAU6PFDVGEZJCY6O2R',
	aws_secret_access_key = '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')

table = dyndb.create_table(
    TableName='hw3table2',
    KeySchema=[
        {
            'AttributeName': 'Id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Id',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)

table = dyndb.Table('hw3table2')
urlbase = 'https://hw3dli3.s3.us-west-2.amazonaws.com/'
with open('experiments.csv', 'r') as csvfile:
    csvf = csv.reader(csvfile, delimiter  = ',', quotechar = '|')
    count = 0
    for item in csvf:
        if(count == 0):
            count += 1
            continue
        body = open(item[4], 'rb')
        s3.Object('hw3dli3', item[4]).put(Body = body)
        md = s3.Object('hw3dli3', item[4]).Acl().put(ACL = 'public-read')
        url = urlbase + item[4]
        metadata_item = {'Id': item[0], 'Temp': item[1], 'Conductivity': item[2], 'Concentration': item[3], 'url':url}
        table.put_item(Item = metadata_item)

for i in range(1, 4):
    print(table.get_item(Key = {'Id': str(i)})['Item'])


