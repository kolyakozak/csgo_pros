sh.addShard("Shard1CSGO_ProsMonitoringReplSet/localhost:43001")
sh.addShard("Shard1CSGO_ProsMonitoringReplSet/localhost:43002")
sh.addShard("Shard1CSGO_ProsMonitoringReplSet/localhost:43003")

sh.addShard("Shard2CSGO_ProsMonitoringReplSet/localhost:43004")
sh.addShard("Shard2CSGO_ProsMonitoringReplSet/localhost:43005")
sh.addShard("Shard2CSGO_ProsMonitoringReplSet/localhost:43006")

sh.enableSharding("csgo_pros")

db = db.getSiblingDB('csgo_pros')
db.csgo_pros.ensureIndex( { _id : "hashed" } )
sh.shardCollection( "csgo_pros.players", { "_id" : "hashed" } )