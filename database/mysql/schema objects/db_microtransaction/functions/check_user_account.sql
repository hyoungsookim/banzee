DELIMITER //
create definer=`root`@`%` function `check_user_account`($user_id varchar(50), $account_type smallint)
returns int
    deterministic
    reads sql data
begin
    declare $account_no int default null;

    select account_no into $account_no 
    from mtt_uw_user_accounts 
    where user_id = $user_id and account_type = $account_type;

    return $account_no;
end;
//
DELIMITER ;
