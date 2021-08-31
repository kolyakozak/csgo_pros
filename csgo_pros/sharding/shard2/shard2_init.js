config = 
{"_id" : "Shard2CSGO_ProsMonitoringReplSet", 
    members : [
        {"_id" : 0, host : "localhost:43004"},
        {"_id" : 1, host : "localhost:43005"},
        {"_id" : 2, host : "localhost:43006", arbiterOnly : true}
    ]
};

rs.initiate(config);
rs.status();