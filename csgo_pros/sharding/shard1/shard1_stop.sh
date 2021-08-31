mongo localhost:43003/admin --eval "db.shutdownServer()"
mongo localhost:43002/admin --eval "db.shutdownServer()"
mongo localhost:43001/admin --eval "db.adminCommand({ shutdown: 1, force: true })"