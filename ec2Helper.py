import boto3
import sys

def createEc2Instance():
    amiid = 'ami-4fffc834'
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=amiid,
        InstanceType='t2.micro',
        MaxCount = 1,
        MinCount = 1,
    )

    print instance

def listofEc2Instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print response

def terminateInstance():
    instanceids  = ['i-00eb2e68f3b43d8bf','i-01fc01e08b13ca7e6']

    ec2 = boto3.resource('ec2')
    for i in instanceids:
        instance = ec2.Instance(i)
        response = instance.terminate()
        print response

def getRegionsandAZ():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    regionslist = response['Regions']
    for r in regionslist:
        print r["RegionName"]

    azresponse = ec2.describe_availability_zones()
    azlist = azresponse['AvailabilityZones']
    for az in azlist:
        print "Region : " + az["RegionName"] +  ",Availability_zone : " + az["ZoneName"]

def getlistofkeypairs():
    ec2 = boto3.client("ec2")
    response = ec2.describe_key_pairs()
    print response

def createkeypairs(keypairname):
    ec2 = boto3.client("ec2")
    response = ec2.create_key_pair(KeyName=keypairname)
    print response

def deletekeypairs(keypairname):
    ec2 = boto3.client("ec2")
    response = ec2.delete_key_pair(KeyName=keypairname)
    print response

'''Security Groups'''
def getSecurityGroupDetails():
    ec2 = boto3.client("ec2")
    response = ec2.describe_security_groups()
    sglist = response['SecurityGroups']
    for sg in sglist:
        print sg

def createSecurityGroup():
    ec2 = boto3.client("ec2")
    response = ec2.describe_vpcs()
    print response


if __name__ == '__main__':
    #createEc2Instance()
    #terminateInstance()
    #getRegionsandAZ()
    #listofEc2Instances()
    #deletekeypairs("codetesting")
    #getlistofkeypairs()
    #getSecurityGroupDetails()

    createSecurityGroup()
