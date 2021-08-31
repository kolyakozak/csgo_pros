config = 
    {"_id" : "Shard1CSGO_ProsMonitoringReplSet", 
        members : [
            {"_id" : 0, host : "localhost:43001"},
            {"_id" : 1, host : "localhost:43002"},
            {"_id" : 2, host : "localhost:43003", arbiterOnly : true}
        ]
    };

rs.initiate(config);