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
