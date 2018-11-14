/*
    Account type data
*/
insert into mtt_md_account_types 
    (account_type, account_type_name, account_type_status, created_at, updated_at)
values
    (0,   'Reward Account', 200, current_timestamp(), current_timestamp()),
    (840, 'Cash Account',   200, current_timestamp(), current_timestamp());
