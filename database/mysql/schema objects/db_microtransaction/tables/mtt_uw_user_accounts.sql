/*
    User Accounts

    account_type: 1 - reward
*/
create table mtt_uw_user_accounts
(
    account_no      integer             not null auto_increment,
    account_id      varchar(50)         not null,
    user_no         integer             not null,
    account_type    smallint            not null,
    account_status  smallint            not null,
    balance_amount  integer             not null,
    created_at      datetime            not null,
    updated_at      datetime            not null,

    constraint pk_mtt_uw_user_accounts
        primary key (account_no)
);
