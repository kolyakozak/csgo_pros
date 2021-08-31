mkdir -p shard1a shard1b shard1c

mongod --shardsvr --dbpath shard1a --port 43001 --replSet Shard1CSGO_ProsMonitoringReplSet --fork --logpath shard1a/shard1a.log &
mongod --shardsvr --dbpath shard1b --port 43002 --replSet Shard1CSGO_ProsMonitoringReplSet --fork --logpath shard1b/shard1b.log &
mongod --shardsvr --dbpath shard1c --port 43003 --replSet Shard1CSGO_ProsMonitoringReplSet --fork --logpath shard1c/shard1c.log &

sleep 1s
ps -ef | grep mongo

mongo -port 43001 shard1_init.js