import boto3
import json


def createtable():
    client = boto3.client('dynamodb')
    response = client.create_table(
        TableName='moviedb',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition Key
            }, {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sortkey
            },
        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print response


def exportdata():
    client = boto3.client('dynamodb')
    # step 1 - read json file

    file = open("moviedata.json", "r")
    rows = json.loads(file.read())

    for row in rows:
        # print row
        year = int(row['year'])
        title = row['title']

        item = {
            'year': {
                'N': str(year)
            },
            'title': {
                'S': title
            }
        }

        response = client.put_item(
            TableName='moviedb',
            Item=item
        )


if __name__ == '__main__':
    # createtable()
    exportdata()
