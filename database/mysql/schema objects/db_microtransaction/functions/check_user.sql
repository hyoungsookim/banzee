DELIMITER //
create function `check_user`($user_id varchar(50))
returns int
    deterministic
    reads sql data
begin
    declare $user_no int default null;

    select user_no into $user_no from mtt_uw_users where user_id = $user_id;

    return $user_no;
end;
//
DELIMITER ;
