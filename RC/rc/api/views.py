from django.shortcuts import render
from django.http import HttpResponse

import json
    
import hfc
from hfc.fabric import Client
from hfc.fabric_ca import CAClient

import os


## get connection
def get_connection():

    # base_dir = os.path.dirname(os.path.realpath(__file__))
    # network_setting_dir = os.path.join(base_dir, 'network.json')
    # ca_certs_path = "/home/bcadmin/fabric-samples/first-network/crypto-config/peerOrganizations/org1.example.com/ca"

    # with open(network_setting_dir, 'rb') as f:
    #     data = json.load(f)
    # print("data#################################################")
    # print(data['certificateAuthorities']['ca-org1']['tlsCACerts']['path'])
    # csr = data['certificateAuthorities']['ca-org1']['tlsCACerts']['path']
    # csr_dir = os.path.join(base_dir, csr)
    # csr_dir = csr_dir.replace("\\", "/")
    # with open(csr_dir, 'rb') as f:
    #     data_csr = f.read()
    # print(str(data_csr))

    # client = CAClient(ca_name="ca.example.com", ca_certs_path=ca_certs_path, target="http://localhost:7054")
    # print("################################################client", client)
    # try:
        
    #     admin = client.enroll(enrollment_id="admin", enrollment_secret="adminpw", csr=data_csr) # now local will have the admin user
    # except ValueError as v:
    #     print("####################################")
    #     print("valueerror: ", v)
    # except RequestException as r:
    #     print("####################################")
    #     print("RequestException: ", r)
    # admin.register(username="user1", password="pass1", attributions={}) # register a user to ca
    # user1 = client.enroll(enrollment_id="user1", enrollment_secret="pass1") # now local will have the user
        

    base_dir = os.path.dirname(os.path.realpath(__file__))
    network_setting_dir = os.path.join(base_dir, 'network.json')
    client = Client(net_profile=network_setting_dir)
    org1_admin = client.get_user(org_name = 'org1.example.com', name='Admin')
    org = client.organizations  # orgs in the network
    peers = client.peers  # peers in the network
    orderers = client.orderers  # orderers in the network
    cas = client.CAs  # ca nodes in the network
    network_info = client.network_info 
    # print(org1_admin)
    # print(org)
    # print(peers)
    # print(orderers)
    # print(cas)
    print(network_info)
    
    # response = client.channel_create(
    #         orderer_name='orderer.example.com',
    #         channel_name='businesschannel',
    #         requestor=org1_admin,
    #         config_yaml='test/fixtures/e2e_cli/',
    #         channel_profile='TwoOrgsChannel'
    #         )

    # print(response.config_yaml)

    # print("client", str(client._organizations['orderer.example.com']))
    # print("client", client._users)
    # print("client", client._channels)
    # print("client", client._orderers)
    # print("client", client._CAs)
    return client

## invoke
def init_wallet ( id ):
    client = get_connection()
    args = []
    response = client.chaincode_invoke(
               requestor=org1_admin,
               channel_name='mychannel',
               peer_names=['peer0.org1.example.com'],
               args=args,
               cc_name='rc',
               cc_version='v1.0'
               )
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
