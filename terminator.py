"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   08.19.2020
 *
 **/"""
import os

from pyrh import Robinhood

u = os.getenv('user')
p = os.getenv('pass')
q = os.getenv('qr')
if not u or not p or not q:
    print("\nCheck your local environment variables. It should be set as:\n"
          "'user=<login_email>'\n'pass=<password>'\n'qr=<qr_code>'")
    exit(1)
rh = Robinhood()
rh.login(username=u, password=p, qr_code=q)
