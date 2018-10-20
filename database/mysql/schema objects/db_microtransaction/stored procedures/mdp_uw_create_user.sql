DELIMITER //
create procedure odp_cm_create_user
(
    $user_id 				varchar(50),
    $partner_id 			varchar(50),
    $user_email 			varchar(150),
    $user_type 				smallint(3),
    $user_level 			smallint(3),
    $first_name 			varchar(50),
    $last_name 				varchar(50),

	out $user_no 			int,
    out $error_code			int
)
main:begin
    declare $user_no int default null;
    declare $created_at datetime default current_timestamp();

    set $error_code = 0;

    if  ($user_id is null or trim($user_id) = '') then
		set $error_code = 30400;			/* invalid request */
		leave main;
    end if;

    if ($user_email is null or trim($user_email) = '') then 
		set $error_code = 30400;			/* invalid request */
		leave main;
    end if;

	/*
		Escape as success status if user_no or user_id is already in table.
    */
    /*
    if not exists (select 1 from odt_cm_accounts where user_no = $user_no or user_id = $user_id) then
	*/
    if not exists (select 1 from mtt_uw_users where user_id = $user_id) then
    	insert into mtt_uw_users
			(user_id, partner_id, user_status, user_type, user_level, 
			 first_name, last_name, created_at, updated_at)
		values
			($user_id, $partner_id, $user_status, $user_type, $user_level, 
			 $first_name, $last_name, $created_at, $created_at);

        set $user_no = last_insert_id();

        insert into mtt_uw_user_accounts
            (user_no, account_type, account_status, balance_amount, updated_at)
        values
            ($user_no, 1, 200, 0, $created_at);
	end if;
end;
//
DELIMITER ;
