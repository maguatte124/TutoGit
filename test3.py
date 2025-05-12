import psycopg2
import sshtunnel

sshtunnel.SSH_TIMEOUT = 10.0
sshtunnel.TUNNEL_TIMEOUT = 10.0

postgres_hostname = "yourusername-1234.postgres.pythonanywhere-services.com"  # You will have your own here
postgres_host_port = 1234  #  You will have your own port here

with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='your PythonAnywhere username',
        ssh_password='the password you use to log in to the PythonAnywhere website',
        remote_bind_address=(postgres_hostname, postgres_host_port)
) as tunnel:
    connection = psycopg2.connect(
        user='a postgres user', password='password for the postgres user',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='your database name',
    )
    # Do stuff inside the context manager block
    connection.close()