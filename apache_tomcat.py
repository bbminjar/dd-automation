from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id, apache_net_hits, tomcat_threads_max, tomcat_request_count,  alerts_list):

    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

#APACHE - NET HITS
    if "apache" in alerts_list:
        api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:apache.net.hits{*} by {host,name,region} >"+str(apache_net_hits),
                       name="["+str(customer_name)+"]" + " - " + "High apache hit on this server",
                       message="Team,High apache hit on this server. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2),
        api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:apache.net.hits{*} by {host,name,region} >"+str(apache_net_hits),
                   name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "High apache hit on this server",
                   message="Team,High apache hit on this server. Please take a look into this. @"+str(support_mail),
                   tags=tags,
                   options=options),
        api.Monitor.create(type="metric alert",
                   query="min(last_30m):avg:apache.net.hits{*} by {host,name,region} >"+str(apache_net_hits),
                   name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "High apache hit on this server",
                   message="Team,High apache hit on this server. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options),
        api.Monitor.create(type="metric alert",
                   query="min(last_1h):avg:apache.net.hits{*} by {host,name,region} >"+str(apache_net_hits),
                   name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "High apache hit on this server",
                   message="Team,High apache hit on this server. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options),
#TOMCAT-THREAD_MAX
        api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:tomcat.threads.max{*} by {host,name,region} >"+str(tomcat_threads_max),
                   name="["+str(customer_name)+"]" + " - " + "High tomcat thread",
                   message="Team,High tomcat thread. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                   tags=tags,
                   options=options2),
        api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:tomcat.threads.max{*} by {host,name,region} >"+str(tomcat_threads_max),
                   name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "High tomcat thread",
                   message="Team,High tomcat thread. Please take a look into this. @"+str(support_mail),
                   tags=tags,
                   options=options),
        api.Monitor.create(type="metric alert",
                   query="min(last_30m):avg:tomcat.threads.max{*} by {host,name,region} >"+str(tomcat_threads_max),
                   name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "High tomcat thread",
                   message="Team,High tomcat thread. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options),
        api.Monitor.create(type="metric alert",
                   query="min(last_1h):avg:tomcat.threads.max{*} by {host,name,region} >"+str(tomcat_threads_max),
                   name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "High tomcat thread",
                   message="Team,High tomcat thread. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options),
#TOMCAT-THREAD_count
        api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:tomcat_request_count{*} by {host,name,region} >"+str(tomcat_request_count),
                   name="["+str(customer_name)+"]" + " - " + "High tomcat request count",
                   message="Team,High tomcat request count. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                   tags=tags,
                   options=options2),
        api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:tomcat_request_count{*} by {host,name,region} >"+str(tomcat_request_count),
                   name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "High tomcat request count",
                   message="Team,High tomcat request count. Please take a look into this. @"+str(support_mail),
                   tags=tags,
                   options=options),
        api.Monitor.create(type="metric alert",
                   query="min(last_30m):avg:tomcat_request_count{*} by {host,name,region} >"+str(tomcat_request_count),
                   name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "High tomcat request count",
                   message="Team,High tomcat request count. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options),
        api.Monitor.create(type="metric alert",
                   query="min(last_1h):avg:tomcat_request_count{*} by {host,name,region} >"+str(tomcat_request_count),
                   name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "High tomcat request count",
                   message="Team,High tomcat request count. Please take a look into this. @cloudops-business@minjar.com ",
                   tags=tags,
                   options=options)

        return True