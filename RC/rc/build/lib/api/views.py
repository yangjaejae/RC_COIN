from django.shortcuts import render
from django.http import HttpResponse

import json
    
import hfc
from hfc.fabric import Client
from hfc.fabric_ca import CAClient

import os


## get connection
def get_connection():

    base_dir = os.path.dirname(os.path.realpath(__file__))
    network_setting_dir = os.path.join(base_dir, 'network.json')
    client = Client(net_profile=network_setting_dir)
    print("######################", client )
    ca_certs_path = "/home/bcadmin/fabric-samples/first-network/crypto-config/peerOrganizations/org1.example.com/ca"

    cli = CAClient(ca_name="ca.example.com", ca_certs_path=ca_certs_path)
    admin = cli.enroll(enrollment_id="admin", enrollment_secret="pass", csr=network_setting_dir) # now local will have the admin user
    admin.register(username="user1", password="pass1", attributions={}) # register a user to ca
    user1 = cli.enroll(username="user1", password="pass1") # now local will have the user
    # print(hfc.VERSION)
    # base_dir = os.path.dirname(os.path.realpath(__file__))
    # client = Client(net_profile=os.path.join(base_dir, 'network.json'))
    # org1_admin = client.get_user(org_name = 'org1.example.com', name='Admin')
    # print("org1_admin", org1_admin)
    return cli

## invoke
def init_wallet ( id ):
    client = get_connection()
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
