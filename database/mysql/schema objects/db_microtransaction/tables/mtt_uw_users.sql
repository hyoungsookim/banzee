/*
    Users
*/
create table mtt_uw_users
(
    user_no             int             not null auto_increment,
    user_id				varchar(50)		not null,
    partner_id 			varchar(50)		not null,
    user_status 	    smallint		not null,
    user_type		    smallint		not null,
    user_level		    smallint		not null,
    first_name			varchar(50)		not null,
    last_name			varchar(50)     not null,
    created_at 		    datetime		not null,
    updated_at		    datetime		not null,

    constraint pk_mtt_uw_users
        primary key (user_no)
);
