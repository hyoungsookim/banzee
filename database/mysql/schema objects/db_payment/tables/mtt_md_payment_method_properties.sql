/*
	Payment Method Properties
*/
create table mtt_md_payment_method_properties
(
	method_code 			varchar(10) 	not null,
    property_type 			smallint 		not null,
    property_value 			varchar(250)	null,
    created_at              datetime        not null, 
    updated_at 		        datetime 		not null,

    constraint pk_mtt_md_payment_method_properties
		primary key (method_code, property_type)
);
