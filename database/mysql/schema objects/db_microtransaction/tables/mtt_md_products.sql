/*
    Products

    product_type: 'SERVICE', 'ITEM'
*/
create table mtt_md_products
(
    product_no          integer             not null auto_increment,
    product_id          varchar(50)         not null,
    product_status      smallint            not null,
    product_name        varchar(50)         not null,
    product_type        varchar(20)         not null,
    created_at          datetime            not null,
    updated_at          datetime            not null,
    product_description text                null,

    constraint pk_mtt_md_products
        primary key (product_no)
);
