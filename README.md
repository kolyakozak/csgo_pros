# csgo_pros

sh crawl.sh for filling database

jupyter notebook visualize_data.ipynb for visualization

python3 backup.py backup/restore [filepath] for saving or restoring data


cd replication
sh start_dbs.sh/stop_dbs.sh
to start/stop mongo with configured replica sets

cd sharding
sh start.sh/stop.sh/delete_data.sh
to start/stop mongo with configured local sharding
and remove all local dbs