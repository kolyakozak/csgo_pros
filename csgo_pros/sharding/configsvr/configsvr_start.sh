mkdir -p configsvr1 configsvr2 configsvr3

mongod --configsvr --replSet configserver --port 43007 --dbpath configsvr1 --fork --logpath configsvr1/configsvr1.log
mongod --configsvr --replSet configserver --port 43008 --dbpath configsvr2 --fork --logpath configsvr2/configsvr2.log
mongod --configsvr --replSet configserver --port 43009 --dbpath configsvr3 --fork --logpath configsvr3/configsvr3.log

sleep 1s
ps -ef | grep mongo

mongo -port 43007 configsvr_init.js