-- SQL-команды для создания таблиц
CREATE TABLE customers
(
    customer_id varchar(100) NOT NULL,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100) NOT NULL
    UNIQUE (customer_id)
);


CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    title varchar(100) NOT NULL,
    birthdate varchar(100) NOT NULL,
    notes text
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id_ varchar(100) REFERENCES customers(customer_id) NOT NULL,
    employee_id_ int REFERENCES employees(employee_id) NOT NULL,
    order_data varchar(100) NOT NULL,
    ship_city varchar(100) NOT NULL
);
