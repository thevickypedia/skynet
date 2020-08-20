import boto3


class AWSClients:
    client = boto3.client('ssm')

    def user(self):
        response = AWSClients.client.get_parameter(Name='user', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def pass_(self):
        response = AWSClients.client.get_parameter(Name='pass', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def qr_code(self):
        response = AWSClients.client.get_parameter(Name='qr', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def access_key(self):
        response = AWSClients.client.get_parameter(Name='ACCESS_KEY', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def secret_key(self):
        response = AWSClients.client.get_parameter(Name='SECRET_KEY', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def sender(self):
        response = AWSClients.client.get_parameter(Name='SENDER', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def recipient(self):
        response = AWSClients.client.get_parameter(Name='RECIPIENT', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def send(self):
        response = AWSClients.client.get_parameter(Name='SEND', WithDecryption=True)
        param = response['Parameter']
        val = param['Value']
        return val

    def receive(self):
        response = AWSClients.client.get_parameter(Name='RECEIVE', WithDecryption=True)
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
