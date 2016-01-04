from flask import Flask, jsonify
from flask import render_template
from flask import request
import data_dog_instance_monitor,elb,rds,apache_tomcat,activemq,nginx,mysql,psql,mongodb,java
app = Flask(__name__, static_url_path='/static/stylesheets')

@app.route("/")
def render_index():
    return render_template('index.html')

@app.route('/',methods=['GET', 'POST'])
def handle_data():
    try:
        input_form = request.form
        print input_form
        print input_form.getlist('check_list')

        if input_form["customer_name"] is None or input_form["api_key"] is None or input_form["app_key"] is None or input_form["access_key"] is None or input_form["secret_key"] is None or input_form["email_id"] is None or input_form["slack_channels"] is None or input_form["customer_email"] is None or input_form["cpu_threshold"] is None or input_form["disk_threshold"] is None or input_form["memory_threshold"] is None or input_form["elb_httpcode_backend_4xx"] is None or input_form["elb_httpcode_backend_5xx"] is None or input_form["rds_cpuutilization"] is None or input_form["rds_free_storage_space"] is None or input_form["apache_net_hits"] is None or input_form["tomcat_threads_max"] is None or input_form["tomcat_request_count"] is None or input_form["thread_count"] is None or input_form["heap_memory"] is None or input_form["queue_consumer_count"] is None or input_form["queue_producer_count"] is None or input_form["queue_memory_pct"] is None or input_form["queue_size"] is None or input_form["nginx_net_connections"] is None or input_form["performance_slow_queries"] is None or input_form["innodb_row_lock_time"] is None or input_form["innodb_row_lock_waits"] is None or input_form["mongodb_connections_current"] is None or input_form["mongodb_mem_resident"] is None or input_form["mongodb_mem_virtual"] is None or len(input_form.getlist("check_list")) == 0:
            return "Invalid Input please provide all the fileds"
        else:
            print "Creating Basic Monitoring"
            is_created = data_dog_instance_monitor.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["cpu_threshold"], input_form["disk_threshold"], input_form["memory_threshold"], input_form.getlist('check_list'))
            print "Creatiing ELB Monitoring."
            is_created_elb = elb.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"], input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form['elb_httpcode_backend_4xx'], input_form["elb_httpcode_backend_5xx"], input_form.getlist('check_list'))
            print "Creating RDS Services."
            is_created_rds = rds.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["rds_cpuutilization"], input_form["rds_free_storage_space"], input_form.getlist('check_list'))
            print "Creating Apache Seervices"
            is_created_apache = apache_tomcat.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["apache_net_hits"], input_form["tomcat_threads_max"], input_form["tomcat_request_count"], input_form.getlist('check_list'))
            is_created_java = java.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["thread_count"], input_form["heap_memory"],input_form.getlist('check_list'))
            print "Creating AQ Services"
            is_created_activemq = activemq.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["queue_consumer_count"], input_form["queue_producer_count"], input_form["queue_memory_pct"], input_form["queue_size"], input_form.getlist('check_list'))
            print "Creating NGINX Services"
            is_created = nginx.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["nginx_net_connections"] ,input_form.getlist('check_list'))
            print "Creating MYSQL Services"
            is_created = mysql.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["performance_slow_queries"], input_form["innodb_row_lock_time"] , input_form["innodb_row_lock_waits"],input_form.getlist('check_list'))
            print "Creating PSQL Services"
            is_created = psql.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["postgresql_connections"], input_form["postgresql_locks"] ,input_form.getlist('check_list'))
            print "Creating mongo services"
            is_created = mongodb.get_all_input_fields_and_add_to_data_dog(input_form["customer_name"] , input_form["api_key"] , input_form["app_key"] , input_form["access_key"] , input_form["secret_key"] , input_form["email_id"] , input_form["slack_channels"] , input_form["customer_email"], input_form["mongodb_connections_current"], input_form["mongodb_mem_resident"], input_form["mongodb_mem_virtual"], input_form.getlist('check_list'))

            if is_created:
                return "Your request is submitted. Go back to Index at <a href='/'> / </a>"
                # data = json.dumps(api.Monitor.get_all(),sort_keys=True,indent=4, separators=(',', ': '))
                # return data
            else:
                return "Failed to serve your request, aplogies, please try by providing all valid input. <a href='/'> / </a>"
    except Exception as e:
        print e
        return "Fatal error, aplogies, please try again by providing all valid input. <a href='/'> / </a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",
        port=int("8080")
            )
