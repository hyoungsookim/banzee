DELIMITER //
create procedure mtp_uw_deposit_fund
(
    $sender_id              varchar(50),
    $recipient_account_id   varchar(50),
    $deposit_amount         decimal(12, 2),
    $source_trx_id          varchar(50),
    $reason                 varchar(50),

    out $error_code		    int
)
main:begin
    declare $recipient_account_no int default null;
    declare $recipient_account_type smallint default null;
    declare $updated_at datetime default current_timestamp();

    set $error_code = 0;

    if (check_user($sender_id) is null) then
        set $error_code = 30400;            /* invalid request */
        leave main;
    end if; 

    if ($recipient_account_id is null or trim($recipient_account_id) = '') then
		set $error_code = 30400;			/* invalid request */
		leave main;
    end if;

    /* $deposit_amount should be bigger than 0.0 */
    if ($deposit_amount < 0.0) then 
        set $error_code = 30400;            /* invalid request */
        leave main;
    end if;

    if ($source_trx_id is null or trim($source_trx_id) = '') then
		set $error_code = 30400;			/* invalid request */
		leave main;
    end if;

    #set $account_no = check_user_account($user_id, $account_type);
    select  account_no, account_type 
    into $recipient_account_no, $recipient_account_type 
    from mtt_uw_user_accounts 
    where account_id = $recipient_account_id;

    if ($recipient_account_no is null) then 
        set $error_code = 30404;            /* resource not found */
        leave main;
    end if;

    /* start transaction; */

    update mtt_uw_user_accounts 
    set balance_amount = balance_amount + $deposit_amount,
        updated_at = $updated_at  
    where account_no = $recipient_account_no;

    /*
    call mtp_tx_create_transaction
    (
        $recipient_account_no,
        $trx_type,
        $deposit_amount,
        $reason,

        $trx_no, 
        $error_code
    );

    if ($error_code = 0) then 
        commit;
    else
        rollback;
    
    */
end;
//
DELIMITER ;
