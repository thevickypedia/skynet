from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3

from lib.aws_client import AWSClients

acc_key = AWSClients().access_key()
secret_key = AWSClients().secret_key()


class Emailer:
    def __init__(self, sender: str, recipients: list, title: str, text: str):
        boto3_ses_client = boto3.Session(
            aws_access_key_id=acc_key,
            aws_secret_access_key=secret_key
        ).client('ses', region_name='us-west-2')

        response_ = self.send_mail(boto3_ses_client, sender, recipients, title, text)
        print(response_)

    def create_multipart_message(self, sender: str, recipients: list, title: str, text: str) -> MIMEMultipart:
        multipart_content_subtype = 'alternative' if text else 'mixed'
        msg = MIMEMultipart(multipart_content_subtype)
        msg['Subject'] = title
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        if text:
            part = MIMEText(text, 'plain')
            msg.attach(part)
        return msg

    def send_mail(self, boto3, sender: str, recipients: list, title: str, text: str) -> dict:
        print("Sending email...")
        msg = self.create_multipart_message(sender, recipients, title, text)
        ses_client = boto3
        return ses_client.send_raw_email(
            Source=sender,
            Destinations=recipients,
            RawMessage={'Data': msg.as_string()}
        )
