/*
    User Balances
*/
create table mtt_uw_user_balances
(
    user_id         varchar(50)         not null,
    balance_type    smallint            not null,
    balance_amount  integer             not null,
    updated_at      datetime            not null,

    constraint pk_mtt_uw_user_balances
        primary key (user_id, balance_type)
);
