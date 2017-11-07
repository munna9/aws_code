import boto3


def create_queue():
    sqs = boto3.resource('sqs')
    response = sqs.create_queue(QueueName='test1',
                                Attributes={'DelaySeconds': '5'})

    print response.url
    print response.attributes.get('DelaySeconds')


def create_queue_client():
    sqs = boto3.client('sqs')
    response = sqs.create_queue(QueueName='test21',
                                Attributes={'DelaySeconds': '5'})

    print response

def sendMessage():
    sqs = boto3.resource('sqs')
    queuename = sqs.get_queue_by_name(QueueName='test1')
    response = queuename.send_message(MessageBody="Hi there we are working with sqs")
    print response


def sendMessagesinBatch():
    sqs = boto3.resource('sqs')
    queuename = sqs.get_queue_by_name(QueueName='test1')
    response = queuename.send_messages(
        Entries=[
            {
                'Id': '1',
                'MessageBody': 'hi there'
            },
            {
                'Id': '2',
                'MessageBody': 'hi there1'
            },
            {
                'Id': '3',
                'MessageBody': 'hi there2'
            }
        ]
    )
    print response


def readmessages():
    sqsclient = boto3.client('sqs')
    response = sqsclient.receive_message(
        QueueUrl=' 	https://sqs.us-east-1.amazonaws.com/awsaccount/test1',
        AttributeNames=[
            'All'
        ]
    )
    print response


if __name__ == '__main__':
    # create_queue()
    #sendMessage()
    #sendMessagesinBatch()
    #create_queue_client()
    readmessages()
