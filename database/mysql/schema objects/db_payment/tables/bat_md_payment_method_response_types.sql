/*
*/
create table bat_md_payment_method_response_types
(
    method_code         varchar(10)         not null,
    payment_response    smallint            not null,
    payment_status      smallint            not null,
    created_at          datetime            not null,
    updated_at          datetime            not null,
    type_description    varchar(250)        null,

    constraint pk_bat_md_payment_method_response_types
        primary key (method_code, payment_response)        
);
