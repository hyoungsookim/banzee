DELIMITER //
create definer=`root`@`%` function `check_user_account`
(
    $user_no        int, 
    $account_type   smallint
)
returns int
    deterministic
    reads sql data
begin
    declare $account_no int default null;

    select account_no into $account_no 
    from mtt_uw_user_accounts 
    where user_no = $user_no and account_type = $account_type;

    return $account_no;
end;
//
DELIMITER ;
