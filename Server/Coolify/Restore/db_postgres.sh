#!/usr/bin/env bash
set -euo pipefail

DB_USER= #dbuser
DB_DATABASE= #db-name
SSH_USER= #root
REMOTE_HOST= #192.168.0.2
BACKUP_PATH= #home/user/Downloads
BACKUP_FILE= #pg-dump.pcap
DOCKER_ID= #Container ID
BACKUP_FILE_PATH=$BACKUP_PATH/$BACKUP_FILE

if [[ ! -f "$BACKUP_FILE_PATH" ]]; then
  echo "Error: Backup file '$BACKUP_FILE' not found."
  exit 1
fi

echo "Start restore from '$BACKUP_FILE' on '$SSH_USER@$REMOTE_HOST'"

cat "$BACKUP_FILE_PATH" | ssh  "$SSH_USER@$REMOTE_HOST" \
  "docker exec -i $DOCKER_ID pg_restore \
     --verbose --clean --no-acl --no-owner \
     -U $DB_USER -d $DB_DATABASE"

echo "✅ Database import completed."

rm $BACKUP_FILE_PATH

echo "✅ Backup file deleted."


$argon2id$v=19$m=65536,t=1,p=4$zbx9XMPNVutH6Zx3KvXfhA$K8GsWWXpcrTWFuh5GD9josebGcsj4f4DR3SOhu+AhBA

$argon2id$v=19$m=65536,t=1,p=4$zbx9XMPNVutH6Zx3KvXfhA$K8GsWWXpcrTWFuh5GD9josebGcsj4f4DR3SOhu+AhBA