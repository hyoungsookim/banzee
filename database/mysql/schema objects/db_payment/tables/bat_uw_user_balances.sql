/*
    User Balances

    balance_type: 'MILEAGE', 'CASH'
*/
create table bat_uw_user_balances
(
    user_id         varchar(50)         not null,
    balance_type    varchar(10)         not null,
    balance_amount  integer             not null,
    updated_at      datetime            not null,

    constraint pk_bat_uw_user_balances
        primary key (user_id, balance_type)
);
