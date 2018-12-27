/*
    Carts
*/
create table mtt_tx_carts
(
    user_no             int             not null,
    product_no          int             not null,
    product_quantity    int             not null, 
    created_at          datetime        not null,
    updated_at          datetime        not null,

    constraint pk_mtt_tx_carts
        primary key (user_no, product_no)
);
