CREATE DATABASE clgws;

USE clgws;

CREATE TABLE Inventory(
    `Car_ID` INT PRIMARY KEY,
    `Make` VARCHAR(255) ,
    `Model` VARCHAR(255) ,
    `Colour` VARCHAR(255) ,
    `Quantity` INT 
);

CREATE TABLE Active_orders(
    `Order_ID` INT  PRIMARY KEY,
    `Date_of_order` DATE ,
    `Car_ID` INT ,
    `Cust_ID` INT 
);

CREATE TABLE Customer(
    `Cust_ID` INT PRIMARY KEY,
    `Name` VARCHAR(255) ,
    `Phone` BIGINT ,
    `Email` VARCHAR(255) 
);

CREATE TABLE Completed_orders(
    `Order_ID` INT PRIMARY KEY,
    `Date_of_order` DATE ,
    `Car_ID` INT ,
    `Cust_ID` INT ,
    `Date_completed` DATE 
);

ALTER TABLE Completed_orders 
ADD FOREIGN KEY(`Cust_ID`) REFERENCES Customer(`Cust_ID`);

ALTER TABLE Completed_orders
ADD FOREIGN KEY(`Car_ID`) REFERENCES Inventory(`Car_ID`);

ALTER TABLE Active_orders
ADD FOREIGN KEY(`Cust_ID`) REFERENCES Customer(`Cust_ID`);

ALTER TABLE Active_orders
ADD  FOREIGN KEY(`Car_ID`) REFERENCES Inventory(`Car_ID`);

INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity) 
    VALUES(1, "Mahindra", "Thar", "Black", 10);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(2, "Mahindra", "Thar", "White", 20);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(3, "Hyundai", "Creta", "Black", 30);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(4, "Hyundai", "Creta", "White", 40);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(5, "Kia", "Sonet", "Black", 50);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(6, "Kia", "Sonet", "Black", 60);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(7, "Maruti", "Swift", "Black", 70);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(8, "Maruti", "Swift", "White", 80);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(9, "Tata", "Nexon", "Black", 90);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(10, "Tata", "Nexon", "White", 100);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(11, "Toyota", "Fortuner", "Black", 120);
INSERT INTO INVENTORY(Car_ID, Make, Model, Colour, Quantity)
    VALUES(12, "Toyota", "Fortuner", "White", 110);

INSERT INTO Customer(Cust_ID, Name, Phone, Email)
    VALUES(1, "Ram Sharma", 0000, "ram_sharma@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email)
    VALUES(2, "Shyam Lal", 0000, "shyam_lal@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email)
    VALUES(3, "Iqbal Singh", 0000, "iqbal_singh@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email) 
    VALUES(4, "Ayaan Khan", 0000, "ayaan_khan@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email) 
    VALUES(5, "Sahil Kumar", 0000, "sahil_kumar@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email) 
    VALUES(6, "Harshit Agarwal", 0000, "harshit_agarwal@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email) 
    VALUES(7, "Rajeev Ahuja", 0000, "rajeev_ahuja@gmail.com");
INSERT INTO Customer(Cust_ID, Name, Phone, Email) 
    VALUES(8, "Rahul Yadav", 0000, "rahul_yadav@gmail.com");

desc Inventory;

desc Customer;

desc Active_orders;

desc Completed_orders;

SELECT * FROM Customer;

SELECT * FROM Inventory;