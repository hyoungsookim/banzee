/*
    Transaction Types
*/
create table mtt_tx_transaction_types
(
    trx_type                smallint            not null,
    trx_type_name           varchar(50)         not null,
    created_at              datetime            not null,
    updated_at              datetime            not null,
    trx_type_description    varchar(250)        null,

    constraint pk_mtt_tx_transaction_types
        primary key (trx_type)
);
