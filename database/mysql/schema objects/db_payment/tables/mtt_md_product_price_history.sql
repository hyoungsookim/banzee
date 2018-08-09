/*
    Prduct Price History
*/
create table mtt_md_product_price_history
(
    change_no           integer             not null auto_increment,
    product_no          integer             not null,
    account_type        smallint            not null,
    updated_at          datetime            not null,
    unit_price          decimal(12, 2)      not null,

    constraint pk_mtt_md_product_price_history
        primary key ()
);
