/*
    User Accounts
*/
create table mtt_uw_user_accounts
(
    account_no      integer             not null auto_increment,
    user_no         integer             not null,
    account_type    smallint            not null,
    account_status  smallint            not null,
    balance_amount  integer             not null,
    updated_at      datetime            not null,

    constraint pk_mtt_uw_user_accounts
        primary key (account_no)
);
