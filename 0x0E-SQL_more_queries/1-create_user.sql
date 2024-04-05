-- script that creates the MySQL server user user_0d_1.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON example_database.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
