/*
    Account Types
*/
create table mtt_md_account_types
(
    account_type                smallint            not null,
    account_type_name           varchar(50)         not null,
    account_type_status         smallint            not null, 
    created_at                  datetime            not null,
    updated_at                  datetime            not null,
    account_type_description    varchar(250)        null,

    constraint pk_mtt_md_account_types
        primary key (account_type)
);
