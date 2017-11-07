import boto3

def createtopic():
    snsclient = boto3.client('sns')
    response = snsclient.create_topic(
        Name='awsboto3'
    )
    print response

def subscribetotopic():
    snsclient = boto3.client('sns')
    response = snsclient.subscribe(
        TopicArn='topic arn',
        Protocol='email',
        Endpoint='hariawsclass@gmail.com')

    print response

def publishMessage():
    snsclient = boto3.client('sns')
    response = snsclient.publish(
        TopicArn='topicarn',
        Subject='testing through code',
        Message='Looks like there is some issues.')

    print response

if __name__ == '__main__':
    #createtopic()
    #subscribetotopic()
    publishMessage()
