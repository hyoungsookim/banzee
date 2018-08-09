create table mtt_tx_order_products
(
    order_no                integer             not null,
    product_no              integer             not null,
    account_type            smallint            not null,
    unit_price              decimal(12, 2)      not null,
    order_quantity          integer             not null,
    total_product_amount    decimal(12, 2)      not null,
    
    constraint pk_mtt_tx_order_products 
        primary key (order_no, product_no, account_type)
);
