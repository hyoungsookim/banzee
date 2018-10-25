DELIMITER //
create procedure mtp_uw_create_user
(
    $user_id 				varchar(50),
    $partner_id 			varchar(50),
    $first_name 			varchar(50),
    $last_name 				varchar(50),

	out $user_no 			int,
    out $error_code			int
)
main:begin
    declare $created_at datetime default current_timestamp();

    set $error_code = 0;

    if  ($user_id is null or trim($user_id) = '') or 
        ($partner_id is null or trim($partner_id) = '') or 
        ($first_name is null or trim($first_name) = '') or 
        ($last_name is null or trim($last_name) = '') then
		set $error_code = 30400;			/* invalid request */
		leave main;
    end if;

    set $user_no = check_user($user_id);
    if ($user_no > 0) then 
		set $error_code = 30409;			/* resource duplicated */
		leave main;
    end if;

    insert into mtt_uw_users
        (user_id, partner_id, user_status, user_type, user_level, 
         first_name, last_name, created_at, updated_at)
    values
        ($user_id, $partner_id, 200, 1, 1, 
         $first_name, $last_name, $created_at, $created_at);

    set $user_no = last_insert_id();

    /* account type: 0 (reward), 840 (ISO 4217-USD) are default accounts */
    insert into mtt_uw_user_accounts
        (account_id, user_no, account_type, account_status, balance_amount, 
         created_at, updated_at)
    values
        (uuid(), $user_no, 0,   200, 0, $created_at, $created_at),
        (uuid(), $user_no, 840, 200, 0, $created_at, $created_at);
end;
//
DELIMITER ;
