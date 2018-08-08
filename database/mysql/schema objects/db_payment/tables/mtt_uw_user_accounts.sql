/*
    User Accounts
*/
create table mtt_uw_user_accounts
(
    user_id				varchar(50)		not null,
    partner_id 			varchar(50)		not null,
    account_status 	    smallint		not null,
    account_type		smallint		not null,
    account_level		smallint		not null,
    first_name			varchar(50)		not null,
    last_name			varchar(50)     not null,
    created_at 		    datetime		not null,
    updated_at		    datetime		not null,

    constraint pk_mtt_uw_user_accounts
        primary key (user_id)
);