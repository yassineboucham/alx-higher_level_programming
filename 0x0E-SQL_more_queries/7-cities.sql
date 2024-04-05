-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY(state_id) REFERENCES TO hbtn_0d_usa.state(id),
    name VARCHAR(256) NOT NULL
    );
