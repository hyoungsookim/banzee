/*
    Transactions
*/
create table mtt_tx_transactions
(
    trx_no          integer             not null auto_increment,
    trx_id          varchar(50)         not null,
    account_no      integer             not null,
    trx_type        smallint            not null,
    trx_status      smallint            not null,
    created_at      datetime            not null,
    updated_at      datetime            not null,
    trx_amount      decimal(12, 2)      not null,
    trx_note        varchar(50)         null,

    constraint pk_mtt_tx_transactions
        primary key (trx_no)
);
