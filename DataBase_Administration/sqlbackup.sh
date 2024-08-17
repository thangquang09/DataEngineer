!#/bin/sh

DATABASE='sakila'

echo "Pulling Database: This may take a few minutes"

backupfolder=/home/theia/backups
keepday=30

sqlfile=$backupfolder/all-database-$(date +%d-%m-%Y_%H-%M-%S).sql
zipfile=$backupfolder/all-database-$(date +%d-%m-%Y_%H-%M-%S).gz

if mysqldump $DATABASE > $sqlfile ; then
    echo 'Sql dump created'
    # Compress backup
    if gzip -c $sqlfile > $zipfile; then
        echo 'The backup was successfully compressed'
    else
        echo 'Error compressing backup. Backup was not created!'
        exit
    fi
    rm $rm $sqlfile
else
    echo 'pg_dump return non-zero code No backup was created!'
    exit
fi

# Delete old backups
find $backupfolder -mtime + $keepday -delete