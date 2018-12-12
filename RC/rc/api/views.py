from django.shortcuts import render
from hfc.fabric import Client

cli = Client(net_profile="test/fixtures/network.json")

def get_connection():
    pass
## invoke
def init_wallet ( id ):
    print(cli)
    pass
def publish( id, value, date ):
    pass
def transfer(_from, to, value, type, date):
    pass
## query
def get_account( id ):
    pass
def get_txList( txid ):
    pass
