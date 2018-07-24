/*
	Accounts
*/
create table bat_user_accounts
(
    user_id					varchar(50)		not null,
    partner_no 			    int				not null,
    account_status 		    smallint		not null,
    account_type			smallint		not null,
    account_level			smallint		not null,
    cc_emails				varchar(250)	null,
    first_name			    varchar(50)		null,
    last_name				varchar(50)		null,
    registered_at	        datetime		not null,
    created_at 		        datetime		not null,
    updated_at		        datetime		not null,

    constraint pk_bat_user_accounts
		    primary key (user_id)
);
