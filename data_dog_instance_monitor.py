from datadog import initialize, api
import json
from boto.ec2.connection import EC2Connection

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key, access_key, secret_key, support_mail, slack_channels, customer_email_id,
                                             cpu_threshold, disk_threshold, memory_threshold, alerts_list):

    print "memory_threshold " + memory_threshold
    try:
        conn = EC2Connection(aws_access_key_id=str(access_key),
                             aws_secret_access_key=str(secret_key))

    # Provide the AWS tag key which we did for Datadog Monitoring
        tag1 = 'datadog'
        instance_type = []
        options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
        }
        initialize(**options)
        instances = conn.get_only_instances()
        for instance in instances:
            tag_dict = instance.tags
            if tag1 in tag_dict:
                instance_type.append(str(instance.instance_type))
        dictVar = {'t2.micro':{'load': 1},'t2.small':{'load': 1},'t2.medium':{'load': 2},'t2.large':{'load': 2},'m4.large':{'load': 2},'m4.xlarge':{'load': 4},'m4.2xlarge':{'load': 8},'m4.4xlarge':{'load': 16},'m4.10xlarge':{'load': 40},'m3.medium':{'load': 1},'m3.large':{'load': 2},'m3.xlarge':{'load': 4},'m3.2xlarge':{'load': 8},'c4.large':{'load': 2},'c4.xlarge':{'load': 4},'c4.2xlarge':{'load': 8},'c4.4xlarge':{'load': 16},'c4.8xlarge':{'load': 36},'c3.large':{'load': 2},'c3.xlarge':{'load': 4},'c3.2xlarge':{'load': 8},'c3.4xlarge':{'load': 16},'c3.8xlarge':{'load': 32},'g2.2xlarge':{'load': 8},'g2.8xlarge':{'load': 32},'r3.large':{'load': 2},'r3.xlarge':{'load': 4},'r3.2xlarge':{'load': 8},'r3.4xlarge':{'load': 16},'r3.8xlarge':{'load': 32},'i2.xlarge':{'load': 4},'i2.2xlarge':{'load': 8},'i2.4xlarge':{'load': 16},'i2.8xlarge':{'load': 32}}
        options = dict(notify_no_data=False, no_data_timeframe=0)
        options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
        tags = 'datadog'

        for instance in instance_type:
            if instance in dictVar:
                l = dictVar[instance]['load']

    #LOAD
                if 'load' in alerts_list:
                    api.Monitor.create(type="metric alert",
                                       query="min(last_5m):avg:system.load.15{instance-type:" + str(instance) + "} by {host,name,region}>"+ str(l),
                                       name= "["+str(customer_name)+"]" + " - " + "High system load on this server",
                                       message="Team, High system load on this server. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                                       options=options2,tags = tags)
                    api.Monitor.create(type="metric alert",
                                       query="min(last_5m):avg:system.load.15{instance-type:" + str(instance) + "} by {host,name,region}>"+str(l),
                                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "High system load on Microsoft SERVER",
                                       message="Team, High system load on this server. Please take a look into this. " + "@" +str(support_mail),
                                       options=options,tags=tags),
                    api.Monitor.create(type="metric alert",
                                       query="min(last_30m):avg:system.load.15{instance-type:" + str(instance) + "} by {host,name,region}>"+str(l),
                                       name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "High system load on Microsoft SERVER",
                                       message="Team, High system load on this server. Please take a look into this. @cloudops-business@minjar.com",
                                       options=options,tags=tags)
                    api.Monitor.create(type="metric alert",
                                       query="min(last_1h):avg:system.load.15{instance-type:" + str(instance) + "} by {host,name,region}>"+str(l),
                                       name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "High system load on Microsoft SERVER",
                                       message="Team, High system load on this server. Please take a look into this. @cloudops-business@minjar.com",
                                       options=options,tags=tags),

            print 'memory' in alerts_list
#Memory
            if 'memory' in alerts_list:
                print "1"
                print memory_threshold
                api.Monitor.create(type="metric alert",
                           query="min(last_5m):avg:system.mem.pct_usable{*} by {host,name,region} >"+str(memory_threshold),
                           name="["+str(customer_name)+"]" + " - " + "High memory is on high on this server",
                           message="Team, High system memory is high on this server. Please take a look into this." + "@"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                           tags=tags,
                           options=options2),
                api.Monitor.create(type="metric alert",
                           query="min(last_5m):avg:system.mem.pct_usable{*} by {host,name,region} >"+str(memory_threshold),
                           name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "High memory is on high on this server",
                           message="Team, High system memory is high on this server. Please take a look into this. @"+str(support_mail),
                           tags=tags,
                           options=options),
                api.Monitor.create(type="metric alert",
                           query="min(last_30m):avg:system.mem.pct_usable{*} by {host,name,region} >"+str(memory_threshold),
                           name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "High memory is on high on this server",
                           message="Team, High system memory is high on this server. Please take a look into this. @cloudops-business@minjar.com ",
                           tags=tags,
                           options=options),
                api.Monitor.create(type="metric alert",
                           query="min(last_1h):avg:system.mem.pct_usable{*} by {host,name,region} >"+str(memory_threshold),
                           name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "High memory is on high on this server",
                           message="Team, High system memory is high on this server. Please take a look into this. @cloudops-business@minjar.com ",
                           tags=tags,
                           options=options),
                print "33333333333333333"
    #Disk
            if 'disk' in alerts_list:
                api.Monitor.create(type="metric alert",
                           query="min(last_5m):avg:system.disk.in_use{region:ap-southeast-1} by {device,host,name,region} >"+str(disk_threshold),
                           name="["+str(customer_name)+"]" + " - " + "Root partition is getting full on this server",
                           message="Team,Root partition is getting full on this server. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                           tags=tags,
                           options=options2),
                api.Monitor.create(type="metric alert",
                           query="min(last_5m):avg:system.disk.in_use{region:ap-southeast-1} by {device,host,name,region} >"+str(disk_threshold),
                           name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "Root partition is getting full on this server",
                           message="Team,Root partition is getting full on this server. Please take a look into this. @"+str(support_mail),
                           tags=tags,
                           options=options),
                api.Monitor.create(type="metric alert",
                           query="min(last_30m):avg:system.disk.in_use{region:ap-southeast-1} by {device,host,name,region} >"+str(disk_threshold),
                           name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "Root partition is getting full on this server",
                           message="Team,Root partition is getting full on this server. Please take a look into this. @cloudops-business@minjar.com ",
                           tags=tags,
                           options=options),
                api.Monitor.create(type="metric alert",
                           query="min(last_1h):avg:system.disk.in_use{region:ap-southeast-1} by {device,host,name,region} >"+str(disk_threshold),
                           name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "Root partition is getting full on this server",
                           message="Team,Root partition is getting full on this server. Please take a look into this. @cloudops-business@minjar.com ",
                           tags=tags,
                           options=options),

    #EC2 CPU
            if 'cpu utilization' in alerts_list:
                api.Monitor.create(type="metric alert",
                           query="min(last_5m):avg:aws.ec2.cpuutilization{region:ap-southeast-1} by {host,name,region} >"+str(cpu_threshold),
                           name="["+str(customer_name)+"]" + " - " + "CPU utilization high on this server",
                           message="Team,CPU utilization high on this server. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                           tags=tags,
                           options=options2),
                # api.Monitor.create(type="metric alert",
                #            query="min(last_5m):avg:aws.ec2.cpuutilization{region:ap-southeast-1} by {host,name,region} >"+str(cpu_threshold),
                #            name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "CPU utilization high on this server",
                #            message="Team,CPU utilization high on this server. Please take a look into this. @"+str(support_mail),
                #            tags=tags,
                #            options=options),
                # api.Monitor.create(type="metric alert",
                #            query="min(last_30m):avg:aws.ec2.cpuutilization{region:ap-southeast-1} by {host,name,region} >"+str(cpu_threshold),
                #            name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "CPU utilization high on this server",
                #            message="Team,CPU utilization high on this server. Please take a look into this. @cloudops-business@minjar.com ",
                #            tags=tags,
                #            options=options),
                # api.Monitor.create(type="metric alert",
                #            query="min(last_1h):avg:aws.ec2.cpuutilization{region:ap-southeast-1} by {host,name,region} >"+str(cpu_threshold),
                #            name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "CPU utilization high on this server",
                #            message="Team,CPU utilization high on this server. Please take a look into this. @cloudops-business@minjar.com ",
                #            tags=tags,
                #            options=options),

        # print instance
        data = json.dumps(api.Monitor.get_all(),sort_keys=True,indent=4, separators=(',', ': '))
        # print (data)
        print "5555"
        return True
    except Exception as e:
        print e
        return False

