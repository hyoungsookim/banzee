/*
    Trnasaction type data
*/
insert into mtt_tx_transaction_types 
    (trx_type, trx_type_name, io_type, parent_trx_type, created_at, updated_at)
values
    (1000, 'Income',              1, null, current_timestamp(), current_timestamp()),
    (1100, 'Reward',              1, 1000, current_timestamp(), current_timestamp()),
    (1200, 'Cash',                1, 1000, current_timestamp(), current_timestamp()),
    (2000, 'Expense',            -1, null, current_timestamp(), current_timestamp()),
    (2100, 'Item purchasing',    -1, 2000, current_timestamp(), current_timestamp()),
    (2200, 'Service purchasing', -1, 2000, current_timestamp(), current_timestamp());
