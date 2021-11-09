from cassandra.cluster import Cluster

cluster = Cluster(['cas-teb-doc001s.infra.azion.net'])

session = cluster.connect()

rows = session.execute('SELECT cluster_name, listen_address FROM system.local;')
for row in rows:
    print(row.cluster_name, row.listen_address)

