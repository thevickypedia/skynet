"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   08.19.2020
 *
 **/"""
from pyrh import Robinhood

from lib.aws_client import AWSClients

u = AWSClients().user()
p = AWSClients().pass_()
q = AWSClients().qr_code()
rh = Robinhood()
rh.login(username=u, password=p, qr_code=q)
print(rh)
