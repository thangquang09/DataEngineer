# [Part 1 Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyMzFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvRmluYWwlMjBBc3NpZ25tZW50L0ZpbmFsX0Fzc2lnbm1lbnRfLV9EYXRhYmFzZV9BZG1pbmlzdHJhdGlvbl8tX1BhcnRfMS5tZCIsInRvb2xfdHlwZSI6InRoZWlhZG9ja2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjE4OTI4OTd9.42pMGvHTNN1Pe3gSK978LrW3bEEXzRQa_17GT80hTXQ)

## Exercise 1.1 - Set up the lab environment

### Task 1.1 - Find the settings in PostgreSQL

What is the maximum number of connections allowed for the postgres server on theia lab?

```
100
```

![max connection image](max-connections.PNG)


## Exercise 1.2 - User Management

### Task 1.2 - Create a User

Create a user named backup_operator.

![](create-user.PNG)

Task 1.3 - Create a Role

### Task 1.3 - Create a Role

Create a role named backup.

![](create-role.PNG)

### Task 1.4 - Grant privileges to the role

Grant the following privileges to the backup role.

`CONNECT ON DATABASE tolldata` , `SELECT ON ALL TABLES IN SCHEMA toll`.

![](grant-privs-to-role.PNG)

### Task 1.5 - Grant role to an user

Grant the role backup to backup_operator

![](grant-role.PNG)

## Exercise 1.3 - Backup

### Task 1.6 - Backup a database on PostgreSQL server

Backup the database tolldata using PGADMIN GUI.

Backup the database tolldata into a file named tolldatabackup.tar, select the backup format as Tar

# [Part 2 Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyMzFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvRmluYWwlMjBBc3NpZ25tZW50L0ZpbmFsX0Fzc2lnbm1lbnRfLV9EYXRhYmFzZV9BZG1pbmlzdHJhdGlvbl8tX1BhcnRfMi5tZCIsInRvb2xfdHlwZSI6InRoZWlhZG9ja2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjEzNzg2OTh9.IR5rTF3J5yZ19g8XrcNYLGBi5c5Sr6g940iu_eoo0LA)

## Exercise 2.1 - Set up the lab environment

Start MySQL

## Exercise 2.2 - Recovery

### Task 2.1 - Restore MySQL server using a previous backup

Download the backup file https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0231EN-SkillsNetwork/labs/Final%20Assignment/billingdata.sql.

Restore this file onto MySQL server.

List the tables in the billing database.

![](database-restore.PNG)

### Task 2.2 - Find the table data size

Find the data size of the table billdata.

![](table-data-size.PNG)

## Exercise 2.3 - Indexing

### Task 2.3 - Baseline query performance

Write a query to select all rows with a billedamount > 19999 in table billdata.

![](query-base-line.PNG)

### Task 2.4 - Create an index

Your customer wants to improve the execution time of the query you wrote in Task 2.3.

Create an appropriate index to make it run faster.

![](index-creation.PNG)

### Task 2.5 - Document the improvement in query performance

Find out if the index has any impact on query performance.

Re-run the baseline query of Task 2.3 after creating the index.

![](query-indexed.PNG)

## Exercise 2.4 - Storage Engines

### Task 2.6 - Find supported storage engines

Run a command to find out if your MySQL server supports the MyISAM storage engine.

![](storage-engine.PNG)

### Task 2.7 - Find the storage engine of a table

Fine out engine of billdata table

![](storage-engine-type.PNG)

# [Part 3 Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL3hBTFFZeElJbEo1V2dXN1AyanY2WHcvRmluYWwlMjBhc3NpZ25tZW50JTIwUGFydC0zJTIwdXNpbmclMjBEYXRhc2V0dGUtdjEubWQiLCJ0b29sX3R5cGUiOiJkYXRhc2V0dGUiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcxNzEyNTIzNH0.Yc8WHdIw4UJJo3YOjqL2LcKc8qQ03TmNRD192MhdkUY)

## Exercise 3.1 - Restore data

Data set [billing.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0231EN-SkillsNetwork/labs/Final%20Assignment/billing.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0231ENSkillsNetwork26763093-2022-01-01)

### Task 3.1 - Restore the table billing

Use the billing.csv and restore the CSV file into a table named billing. Write a query to display the total number of rows imported.

![](restore-table.PNG)

## Exercise 3.2 - Create a view

### Task 3.2 - Create a view named basicbilldetails with the columns customerid, month, billedamount

![](create-view.PNG)

## Exercise 3.3 - Indexing

### Task 3.3 - Baseline query performance

Write a query to find out all the rows with a billing amount of 19929. Hint: Use the command SELECT strftime(“%Y-%m-%d %H:%M:%f”, “now”); before and after your query to display the run time.

Note: There will not be much difference in the run time as the number of records is less for the above-given condition.

![](query-base-line_33.PNG)

![](index-creation34.PNG)

![](query-after-index.PNG)






