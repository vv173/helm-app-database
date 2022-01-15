# Simple app with databese

This repo includes a helm chart with the Python Flask application.
The application creates two endpoints:

`/api/count/add` - which adds the count of page views to the database

`/api/count` - which returns the number of views.

For the database, I'm using a PostgreSQL helm chart.





**To run our flask helm chart, we need to:**

*Deploy ConfigMap for PostgreSQL, which includes SQL code for our database.*
    kubectl apply -f postgresql/postgres-configmap.yml
    \
*Install PostgreSQL helm chart*

        helm install postgres -f postgresql/values.yml 
            --create-namespace -n flask-app bitnami/postgresql 
            --set global.postgresql.postgresqlPassword=<Admin Password>
            --set global.postgresql.postgresqlPassword=<User Password>
            
*Now we can install our flask helm chart, by running:*

        helm install flask Chart-Flask/ --create-namespace -n flask-app -f Chart-Flask/values.yaml
