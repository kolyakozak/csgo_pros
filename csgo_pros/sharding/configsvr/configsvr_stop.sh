mongo localhost:43009/admin --eval "db.adminCommand({ shutdown: 1, force: true })"
mongo localhost:43008/admin --eval "db.adminCommand({ shutdown: 1, force: true })"
mongo localhost:43007/admin --eval "db.adminCommand({ shutdown: 1, force: true })"