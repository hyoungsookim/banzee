/*
    Account type data
*/
insert into mtt_uw_account_types 
    (account_type, account_type_name, created_at, updated_at)
values
    (0,   'Reward Account', current_timestamp(), current_timestamp()),
    (840, 'Cash Account',   current_timestamp(), current_timestamp());
