DELIMITER //
create procedure mtp_uw_open_account
(
    $user_id 				varchar(50),
    $account_type           smallint,

	out $account_id 		varchar(50),
    out $error_code			int
)
main:begin
    declare $user_no int default null;
    declare $account_no int default null;
    declare $new_id varchar(50) default null;
    declare $created_at datetime default current_timestamp();

    set $error_code = 0;

    if  ($user_id is null or trim($user_id) = '') then 
        set $error_code = 400;			/* invalid request */
		leave main;
    end if;

    set $user_no = check_user($user_id);
    if ($user_no is null) then 
		set $error_code = 404;			/* resource not found */
		leave main;
    end if;

    set $account_no = check_user_account($user_no, $account_type);
    if ($account_no > 0) then 
		set $error_code = 409;			/* resource duplicated */
		leave main;
    end if;

    set $new_id = new_id();
    insert into mtt_uw_user_accounts
        (account_id, user_no, account_type, account_status, balance_amount, 
         created_at, updated_at)
    values
        ($new_id, $user_no, $account_type, 200, 0, 
         $created_at, $created_at);
    
    set $account_id = $new_id;
end;
//
DELIMITER ;
