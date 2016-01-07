from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id, performance_slow_queries, innodb_row_lock_time, innodb_row_lock_waits, alerts_list):

    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

    if "mysql" in alerts_list:
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:mysql.performance.slow_queries{*} by {host,name,region} >" + str(performance_slow_queries),
                       name="["+str(customer_name)+"]" + " - " + "mysql.performance.slow_queries",
                       message="Team,We are finding slow queries. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:mysql.performance.slow_queries{*} by {host,name,region} >" + str(performance_slow_queries),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "mysql.performance.slow_queries",
                       message="Team,We are finding slow queries. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
#innodb_row_lock_time
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:mysql.innodb.row_lock_time{*} by {host,name,region} >" + str(innodb_row_lock_time),
                       name="["+str(customer_name)+"]" + " - " + "mysql.innodb.row_lock_time",
                       message="Team,There was innodb row locktime is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:mysql.innodb.row_lock_time{*} by {host,name,region} >" + str(innodb_row_lock_time),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "mysql.innodb.row_lock_time",
                       message="Team,There was innodb row locktime is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
#innodb_row_lock_wait
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:mysql.innodb.row_lock_waits{*} by {host,name,region} >" + str(innodb_row_lock_waits),
                       name="["+str(customer_name)+"]" + " - " + "mysql.innodb.row_lock_waits",
                       message="Team,There was innodb row lock waits is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:mysql.innodb.row_lock_waits{*} by {host,name,region} >" + str(innodb_row_lock_waits),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "mysql.innodb.row_lock_waits",
                       message="Team,There was innodb row lock waits is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),

            return True