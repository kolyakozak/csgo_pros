mkdir -p routerdb

mongos --port 43010 --configdb configserver/localhost:43007,localhost:43008,localhost:43009 --fork --logpath routerdb/routerdb.log

sleep 1s
ps -ef | grep mongo

mongo -port 43010 routerdb_init.js