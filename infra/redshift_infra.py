import configparser
import os

config = configparser.ConfigParser()
config.read_file(open('config\dwh.cfg'))

# AWS Credentials
KEY                    = config.get('AWS','KEY')
SECRET                 = config.get('AWS','SECRET')

#Redshift Cluster
DWH_CLUSTER_TYPE       = config.get("DWH","DWH_CLUSTER_TYPE")
DWH_NUM_NODES          = config.get("DWH","DWH_NUM_NODES")
DWH_NODE_TYPE          = config.get("DWH","DWH_NODE_TYPE")

DWH_CLUSTER_IDENTIFIER = config.get("DWH","DWH_CLUSTER_IDENTIFIER")
DWH_DB                 = config.get("DWH","DWH_DB")
DWH_DB_USER            = config.get("DWH","DWH_DB_USER")
DWH_DB_PASSWORD        = config.get("DWH","DWH_DB_PASSWORD")
DWH_PORT               = config.get("DWH","DWH_PORT")

DWH_IAM_ROLE_NAME      = config.get("DWH", "DWH_IAM_ROLE_NAME")

def create_iam_role():
    """Cria uma Role IAM para o Redshift com permissão de AmazonS3ReadOnlyAccess"""
    try:

    except:
        