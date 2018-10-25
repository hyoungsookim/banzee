/*
    Account Types
*/
create table mtt_uw_account_types
(
    account_type        smallint        not null,
    account_type_name   varchar(50)     not null,
    created_at 		    datetime		not null,
    updated_at		    datetime		not null,

    constraint pk_mtt_uw_account_types
        primary key (account_type)
);
