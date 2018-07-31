/*
    Payment Methods

    method_type :   'CC' - Credit Card
                    'CP' - Coupon Code
                    'WT' - Wire Transfer
                    'CK' - Check
*/
create table bat_md_payment_methods 
(
    method_code     varchar(10)         not null,
    method_status   smallint            not null,
    method_name     varchar(50)         not null,
    method_type     varchar(10)         not null,
    created_at      datetime            not null,
    updated_at      datetime            not null,

    constraint pk_bat_md_payment_methods
        primary key (method_code)
);
