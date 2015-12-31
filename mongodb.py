from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id, connections_current, mem_resident, mem_virtual, alerts_list):

    connection_current = 100
    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

    if "mongodb" in alerts_list:
                    api.Monitor.create(type="metric alert",
                               query="min(last_5m):avg:mongodb.connections.current{*} by {host,name,region} >" + str(connections_current),
                               name="["+str(customer_name)+"]" + " - " + "Mongodb Number of database connection is high",
                               message="Team,Mongodb Number of database connection is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                               tags=tags,
                               options=options2),
                    api.Monitor.create(type="metric alert",
                               query="min(last_5m):avg:mongodb.connections.current{*} by {host,name,region} >" + str(connections_current),
                               name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb Number of database connection is high",
                               message="Team,Mongodb Number of database connection is high. Please take a look into this. @"+str(support_mail),
                               tags=tags,
                               options=options),
                    api.Monitor.create(type="metric alert",
                               query="min(last_30m):avg:mongodb.connections.current{*} by {host,name,region} >" + str(connections_current),
                               name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb Number of database connection is high",
                               message="Team,Mongodb Number of database connection is high. Please take a look into this. @cloudops-business@minjar.com ",
                               tags=tags,
                               options=options),
                    api.Monitor.create(type="metric alert",
                               query="min(last_1h):avg:mongodb.connections.current{*} by {host,name,region} >" + str(connections_current),
                               name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb Number of database connection is high",
                               message="Team,Mongodb Number of database connection is high. Please take a look into this. @cloudops-business@minjar.com ",
                               tags=tags,
                               options=options),
#Memory_Resident
                    api.Monitor.create(type="metric alert",
                               query="min(last_5m):avg:mongodb.mem.resident{*} by {host,name,region} >" + str(mem_resident),
                               name="["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb resident memory is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                               tags=tags,
                               options=options2),
                    api.Monitor.create(type="metric alert",
                               query="min(last_5m):avg:mongodb.mem.resident{*} by {host,name,region} >" + str(mem_resident),
                               name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb resident memory is high. Please take a look into this. @"+str(support_mail),
                               tags=tags,
                               options=options),
                    api.Monitor.create(type="metric alert",
                               query="min(last_30m):avg:mongodb.mem.resident{*} by {host,name,region} >" + str(mem_resident),
                               name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb resident memory is high. Please take a look into this. @cloudops-business@minjar.com ",
                               tags=tags,
                               options=options),
                    api.Monitor.create(type="metric alert",
                               query="min(last_1h):avg:mongodb.mem.resident{*} by {host,name,region} >" + str(mem_resident),
                               name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb resident memory is high. Please take a look into this. @cloudops-business@minjar.com ",
                               tags=tags,
                               options=options),
#Memory_Resident
                    api.Monitor.create(type="metric alert",
                               query="min(last_5m):avg:mongodb.mem.virtual{*} by {host,name,region} >" + str(mem_virtual),
                               name="["+str(customer_name)+"]" + " - " + "Mongodb virtual memory is high",
                               message="Team,Mongodb virtual memory is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                               tags=tags,
                               options=options2),
                    api.Monitor.create(type="metric alert",
                               query="min(last_5m):avg:mongodb.mem.virtual{*} by {host,name,region} >" + str(mem_virtual),
                               name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb virtual memory is high. Please take a look into this. @"+str(support_mail),
                               tags=tags,
                               options=options),
                    api.Monitor.create(type="metric alert",
                               query="min(last_30m):avg:mongodb.mem.virtual{*} by {host,name,region} >" + str(mem_virtual),
                               name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb virtual memory is high. Please take a look into this. @cloudops-business@minjar.com ",
                               tags=tags,
                               options=options),
                    api.Monitor.create(type="metric alert",
                               query="min(last_1h):avg:mongodb.mem.virtual{*} by {host,name,region} >" + str(mem_virtual),
                               name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "Mongodb resident memory is high",
                               message="Team,Mongodb virtual memory is high. Please take a look into this. @cloudops-business@minjar.com ",
                               tags=tags,
                               options=options),
                    return True