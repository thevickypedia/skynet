import boto3


class AWSClients:
    client = boto3.client('ssm')

    def robinhood_user(self):
        response = AWSClients.client.get_parameter(Name='/Jarvis/robinhood_user', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def robinhood_pass(self):
        response = AWSClients.client.get_parameter(Name='/Jarvis/robinhood_pass', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def robinhood_qr(self):
        response = AWSClients.client.get_parameter(Name='/Jarvis/robinhood_qr', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def send(self):
        response = AWSClients.client.get_parameter(Name='SEND', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def receive(self):
        response = AWSClients.client.get_parameter(Name='/Jarvis/phone', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def sid(self):
        response = AWSClients.client.get_parameter(Name='SID', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def token(self):
        response = AWSClients.client.get_parameter(Name='TOKEN', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val
