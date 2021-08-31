config = 
    {"_id" : "configserver",
        configsvr: true,
        version: 1,
        members : [
            {"_id" : 0, host : "localhost:43007"},
            {"_id" : 1, host : "localhost:43008"},
            {"_id" : 2, host : "localhost:43009"}
        ]
    };

rs.initiate(config);
rs.status();