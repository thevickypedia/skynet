import logging
from pprint import pprint

import boto3

client = boto3.client('lambda')


def update_env_var(env_var_dict):
    """Updates the env variables to the lambda function."""
    response = client.update_function_configuration(
        FunctionName='skynet',  # lambda function name
        Environment={
            'Variables': env_var_dict  # alt format instead of json object: "{key: value}" in place of "env_var_dict"
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        logger.info('The following Environment Variables have been added successfully.')
        for key, value in env_var_dict.items():
            logger.info(f'{key}: {value}')
    else:
        logger.info('Unable to update env variables. Check response below.')
        pprint(response)


def get_env_var():
    """Gets the current environment variables for the lambda function."""
    response = client.get_function(FunctionName='skynet')
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        env_vars = response['Configuration']['Environment']['Variables']
        for ticker, value in env_vars.items():
            print(f'{ticker}={value}')
    else:
        logger.info('Unable to update env variables. Check response below.')
        pprint(response)


def get_json_obj():
    """Gets the dictionary from the stored json file."""
    import json
    with open('env_vars.json') as json_file:
        if data := json.load(json_file):
            return data


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    if content := get_json_obj():
        update_env_var(env_var_dict=content)
