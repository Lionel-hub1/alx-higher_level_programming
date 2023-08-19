-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
SELECT * FROM mysql.user WHERE User='user_0d_1' OR User='user_0d_2';