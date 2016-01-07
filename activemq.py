from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id, queue_consumer_count, queue_producer_count, queue_memory_pct, queue_size, alerts_list):

    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

    if "activemq" in alerts_list:
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.consumer_count{*} by {host,name,region} >" + str(queue_consumer_count),
                       name="["+str(customer_name)+"]" + " - " + "JVM Thread count is high",
                       message="Team,JVM Thread count is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.consumer_count{*} by {host,name,region} >" + str(queue_consumer_count),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM Thread count is high",
                       message="Team,JVM Thread count is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),

#Producer_Count
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.producer_count{*} by {host,name,region} >" + str(queue_producer_count),
                       name="["+str(customer_name)+"]" + " - " + "JVM heap memory is high",
                       message="Team,JVM heap memory is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.producer_count{*} by {host,name,region} >" + str(queue_producer_count),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM heap memory is high",
                       message="Team,JVM heap memory is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),

#queue.memory_pct
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.memory_pct{*} by {host,name,region} >" + str(queue_memory_pct),
                       name="["+str(customer_name)+"]" + " - " + "JVM heap memory is high",
                       message="Team,JVM heap memory is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.memory_pct{*} by {host,name,region} >" + str(queue_memory_pct),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM heap memory is high",
                       message="Team,JVM heap memory is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),

#queue_size
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.size{*} by {host,name,region} >" + str(queue_size),
                       name="["+str(customer_name)+"]" + " - " + "JVM heap memory is high",
                       message="Team,JVM heap memory is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:activemq.queue.size{*} by {host,name,region} >" + str(queue_size),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM heap memory is high",
                       message="Team,JVM heap memory is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),

            return True