from boto3.session import Session
from datadog import initialize, api
import json

# rds_cpu_threshold = 85
# rds_volume_threshold = '2G'

class Boto3Connecton(object):
    @staticmethod
    def get_boto3_session(access_key,
                          secret_key):
        sess = Session(aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key)
        return sess

    @staticmethod
    def get_rds_boto3_connection(access_key, secret_key,region):
        sess = Boto3Connecton.get_boto3_session(access_key, secret_key)
        rds_conn = sess.client(service_name='rds', region_name=region)
        return rds_conn


def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key, access_key, secret_key, support_mail, slack_channels, customer_email_id, rds_cpuutilization, rds_free_storage_space, alerts_list):

    region_list = ["us-east-1","us-west-2"]
    db_instance_class_set = set()
    for region in region_list:
        conn = Boto3Connecton.get_rds_boto3_connection(access_key, secret_key,region=region)
        db_instances = conn.describe_db_instances()['DBInstances']
        db_instances_class = []

        options = {
                'api_key': str(api_key),
                'app_key': str(app_key)
        }
        initialize(**options)
        options = dict(notify_no_data=False, no_data_timeframe=0)
        options2 = dict(notify_no_data=False, no_data_timeframe=10)
        tags = 'datadog'
        m = None
        dictVar = {'db.m4.large':{'memory': 7150000},'db.m4.xlarge':{'memory': 15150000},'db.m4.2xlarge':{'memory': 31150000},'db.m4.4xlarge':{'memory': 63150000},'db.m4.10xlarge':{'memory': 159150000},'db.m3.medium':{'memory': 2900000},'db.m3.large':{'memory': 6650000},'db.m3.xlarge':{'memory': 14150000},'db.m3.2xlarge':{'memory': 29150000},'db.r3.large':{'memory': 14150000},'db.r3.xlarge':{'memory': 29650000},'db.r3.2xlarge':{'memory': 60150000},'db.r3.4xlarge':{'memory': 121150000},'db.r3.8xlarge':{'memory': 243150000},'db.t2.micro':{'memory': 150000},'db.t2.small':{'memory': 1150000},'db.t2.medium':{'memory': 3150000},'db.t2.large':{'memory': 7150000},}


        for rds_db in db_instances:
            db_instance_class = rds_db['DBInstanceClass']
            db_instance_class_set.add(db_instance_class)
        print db_instance_class_set
        for db_instance_class in db_instance_class_set:
            if db_instance_class in dictVar:
                m = dictVar[db_instance_class]['memory']

                if 'rds' in alerts_list:
    #Freeable Memory
                    print json.dumps(api.Monitor.create(type="metric alert",
                           query="min(last_5m):avg:aws.rds.freeable_memory{instance-type:" + str(db_instance_class) +"} by {hostname,region} <"+str(m),
                           name="["+str(customer_name)+"]" + " - " + "RDS Usable Memory is low",
                           message="Team,RDS Usable Memory is low on this RDS. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                           tags=tags,
                           options=options2)),
        # print json.dumps(api.Monitor.create(type="metric alert",
        #                    query="min(last_5m):avg:aws.rds.freeable_memory{instance-type:" + str(db_instance_class) +"} by {hostname,region} <"+str(m),
        #                    name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS Usable Memory is low",
        #                    message="Team,RDS Usable Memory is low on this RDS. Please take a look into this. @"+str(support_mail),
        #                    tags=tags,
        #                    options=options)),
        # print json.dumps(api.Monitor.create(type="metric alert",
        #                    query="min(last_30m):avg:aws.rds.freeable_memory{instance-type:" + str(db_instance_class) +"} by {hostname,region} <"+str(m),
        #                    name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS Usable Memory is low",
        #                    message="Team,RDS Usable Memory is low on this RDS. Please take a look into this. @cloudops-business@minjar.com ",
        #                    tags=tags,
        #                    options=options)),
        # print json.dumps(api.Monitor.create(type="metric alert",
        #                    query="min(last_1h):avg:aws.rds.freeable_memory{instance-type:" + str(db_instance_class) +"} by {hostname,region} <"+str(m),
        #                    name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS Usable Memory is low",
        #                    message="Team,RDS Usable Memory is low on this RDS. Please take a look into this. @cloudops-business@minjar.com",
        #                    tags=tags,
        #                    options=options)),
    #RDS CPU Utilization
    
    print json.dumps(api.Monitor.create(type="metric alert",
               query="min(last_5m):avg:aws.rds.cpuutilization{*} by {hostname,region} >"+str(rds_cpuutilization),
               name="["+str(customer_name)+"]" + " - " + "RDS CPU utilization high",
               message="Team,RDS CPU utilization high on this RDS. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
               tags=tags,
               options=options2)),
        # print json.dumps(api.Monitor.create(type="metric alert",
        #                query="min(last_5m):avg:aws.rds.cpuutilization{*} by {hostname,region} >"+str(rds_cpu_threshold),
        #                name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS CPU utilization high",
        #                message="Team,RDS CPU utilization high on this RDS. Please take a look into this. @"+str(support_mail),
        #                tags=tags,
        #                options=options)),
        # print json.dumps(api.Monitor.create(type="metric alert",
        #                query="min(last_30m):avg:aws.rds.cpuutilization{*} by {hostname,region} >"+str(rds_cpu_threshold),
        #                name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS CPU utilization high",
        #                message="Team,RDS CPU utilization high on this RDS. Please take a look into this. @cloudops-business@minjar.com ",
        #                tags=tags,
        #                options=options)),
        # print json.dumps(api.Monitor.create(type="metric alert",
        #                query="min(last_1h):avg:aws.rds.cpuutilization{*} by {hostname,region} >"+str(rds_cpu_threshold),
        #                name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS CPU utilization high",
        #                message="Team,RDS CPU utilization high on this RDS. Please take a look into this. @cloudops-business@minjar.com ",
        #                tags=tags,
        #                options=options)),

    #RDS-Storage

    print json.dumps(api.Monitor.create(type="metric alert",
               query="min(last_5m):avg:aws.rds.free_storage_space{*} by {hostname,region} >"+str(rds_free_storage_space),
               name="["+str(customer_name)+"]" + " - " + "RDS Storage space is low",
               message="Team,RDS Storage space is low on this RDS. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
               tags=tags,
               options=options2)),
    print json.dumps(api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:aws.rds.free_storage_space{*} by {hostname,region} >"+str(rds_free_storage_space),
                   name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS Storage space is low",
                   message="Team,RDS Storage space is low on this RDS. Please take a look into this. @"+str(support_mail),
                   tags=tags,
                   options=options)),
    print json.dumps(api.Monitor.create(type="metric alert",
                   query="min(last_30m):avg:aws.rds.free_storage_space{*} by {hostname,region} >"+str(rds_free_storage_space),
                   name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS Storage space is low",
                   message="Team,RDS Storage space is low on this RDS. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options)),
    print json.dumps(api.Monitor.create(type="metric alert",
                   query="min(last_1h):avg:aws.rds.free_storage_space{*} by {hostname,region} >"+str(rds_free_storage_space),
                   name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "RDS Storage space is low",
                   message="Team,RDS Storage space is low on this RDS. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options)),
    return True