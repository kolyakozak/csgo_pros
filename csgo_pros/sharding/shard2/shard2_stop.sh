mongo localhost:43006/admin --eval "db.shutdownServer()"
mongo localhost:43005/admin --eval "db.shutdownServer()"
mongo localhost:43004/admin --eval "db.adminCommand({ shutdown: 1, force: true })"