from django.shortcuts import render
from django.http import HttpResponse

import json
    
import hfc
from hfc.fabric import Client

## get connection
def get_connection():
    print(hfc.VERSION)
    cli = Client(net_profile="./network.json")
    org1_admin = cli.get_user(org_name = 'org1.example.com', name='Admin')
    print("###################")
    print(org1_admin)
    

def get_connection():
    pass
## invoke
def init_wallet ( id ):
    lis = []
    dic = {}
    dic['test'] = "test"
    lis.append(dic)
    json_format = json.dumps(lis)
    get_connection()
    return HttpResponse(json_format, content_type="application/json:charset=UTF-8")

def publish( id , value ):
    pass
def transfer(_from, to, value, type, date):
    pass
## query
def get_account( id ):
    pass
def get_txList( txid ):
    pass
