CREATE KEYSPACE IF NOT EXISTS {{ cassandra_keyspace }} WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1};
CREATE USER IF NOT EXISTS {{ cassandra_user }} WITH PASSWORD '{{ cassandra_password }}' SUPERUSER;
