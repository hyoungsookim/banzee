/*
    Payment Status Types
*/
create table mtt_md_payment_status_types
(
    payment_status              smallint        not null,
    payment_status_name         varchar(50)     not null,
    created_at                  datetime        not null,
    updated_at                  datetime        not null,
    payment_status_description  varchar(250)    null,

    constraint pk_mtt_md_payment_status_types
        primary key (payment_status)
);
