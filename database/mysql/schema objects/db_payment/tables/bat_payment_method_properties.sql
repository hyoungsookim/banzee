/*
	Extended Properties of Payment Method
*/
create table bat_payment_method_properties
(
	method_code 		varchar(10) 	not null,
    property_type 		smallint 		not null,
    property_value 		varchar(200)	null,
    updated_at 		    datetime 		not null,

    constraint pk_bat_payment_method_properties
		primary key (method_code, property_type)
);
