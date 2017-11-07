import boto3
import json


def createUser():
    iam = boto3.client("iam")
    response = iam.create_user(UserName='hari123')
    print response


def updateuser():
    iam = boto3.client("iam")
    response = iam.update_user(UserName='hari123', NewUserName='haribabu')
    print response

def deleteuser():
    iam = boto3.client("iam")
    response = iam.delete_user(UserName='haribabu')
    print response



def createpolicy():
    iam = boto3.client('iam')

    mysnsolicy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1504140039000",
            "Effect": "Allow",
            "Action": [
                "sns:*"
            ],
            "Resource": [
                "arn:aws:sns:us-east-1:776955605071:weather_response"
            ]
        }
    ]
    }

    response = iam.create_policy(
        PolicyName = 'mySNSPolicy',
        PolicyDocument = json.dumps(mysnsolicy)
    )

    print response


def getPolicy():
    iam = boto3.client('iam')

    response = iam.get_policy(
        PolicyArn='arn:aws:iam::776955605071:policy/mySNSPolicy'
    )

    print response

if __name__ == '__main__':
    #createUser()
    #updateuser()
    #deleteuser()
    #createpolicy()
    getPolicy()
