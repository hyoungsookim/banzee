/*
    Payment Method Response Types
*/
create table mtt_md_payment_method_response_types
(
    method_code         varchar(10)         not null,
    payment_response    varchar(50)         not null,
    payment_status      smallint            not null,
    created_at          datetime            not null,
    updated_at          datetime            not null,
    type_description    text                null,

    constraint pk_mtt_md_payment_method_response_types
        primary key (method_code, payment_response, payment_status)
);
