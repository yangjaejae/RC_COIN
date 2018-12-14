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
    org1_admin = client.get_user(org_name = 'org1.example.com', name='Admin')
    # org = client.organizations  # orgs in the network
    # peers = client.peers  # peers in the network
    # orderers = client.orderers  # orderers in the network
    # cas = client.CAs  # ca nodes in the network
    # network_info = client.network_info 
    
    print(org1_admin)

    return client

## invoke
def init_wallet ( id ):
    client = get_connection()
    print("###############",client, "###############")

    # response = client.chaincode_invoke(
    #            requestor=org1_admin,
    #            channel_name='mychannel',
    #            peer_names=['peer0.org1.example.com'],
    #            args=["init_wallet", id],
    #            cc_name='rc',
    #            cc_version='v1.0'
    #            )

    lis = []
    dic = {}
    dic['result'] = "TEST"
    lis.append(dic)
    json_format = json.dumps(lis)
    get_connection()
    return HttpResponse(json_format, content_type="application/json:charset=UTF-8")
    # return response

def publish( id , value ):
    pass
def transfer(_from, to, value, type, date):
    pass
## query
def get_account( id ):
    pass
def get_txList( txid ):
    pass