#Alyce Gaines
#CSI261
#SQL

CREATE_TABLE: phone
phone_id = INT(PRIMARY KEY)
country_code = INT(NOT NULL)
phone_number = INT(NOT NULL)
phone_type = VARCHAR()
CHECK (phone_type INT('Home','Mobile','Other')):


ALTER_TABLE: customer 
ADD COLUMN
ADD FOREIGN KEY 
REFERENCES phone(phone_id)
ON DELETE SET NULL
ON UPDATE CASCADE:

ALTER TABLE: address DROP phone

in case you need to delete a foreign key
ALTER TABLE: table_name
DROP FOREIGN KEY: foreign_keys_name