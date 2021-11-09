from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1

ssl_context = SSLContext(PROTOCOL_TLSv1)

cluster = Cluster(['cas-teb-doc001s.infra.azion.net'], ssl_context=ssl_context)
session = cluster.connect()

rows = session.execute('SELECT cluster_name, listen_address FROM system.local;')
for row in rows:
    print(row.cluster_name, row.listen_address)

