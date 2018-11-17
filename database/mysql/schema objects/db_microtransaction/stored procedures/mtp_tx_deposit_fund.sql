DELIMITER //
create procedure mtp_tx_deposit_fund
(
    $sender_id              varchar(50),
    $recipient_account_id   varchar(50),
    $deposit_type           smallint, 
    $deposit_amount         decimal(12, 2),
    $reason                 varchar(50),

    out $trx_id             varchar(50),
    out $error_code		    int
)
main:begin
    declare $sender_no int default null;
    declare $recipient_account_no int default null;
    declare $recipient_account_type smallint default null;
    declare $updated_at datetime default current_timestamp();

	declare $data_not_found tinyint default false;
	declare continue handler for 1329
		set $data_not_found = true;

    declare exit handler for SQLEXCEPTION, SQLWARNING
    begin
        rollback;
        resignal;
    end;

    set $error_code = 0;

    set $sender_no = check_user($sender_id);
    if ($sender_no is null) then
        set $error_code = 400;          /* invalid request */
        leave main;
    end if; 

    if ($recipient_account_id is null or trim($recipient_account_id) = '') then
		set $error_code = 400;          /* invalid request */
		leave main;
    end if;

    /* $deposit_amount should be bigger than 0.0 */
    if ($deposit_amount < 0.0) then 
        set $error_code = 406;          /* not accpeted. */
        leave main;
    end if;

    select  account_no, account_type 
    into $recipient_account_no, $recipient_account_type 
    from mtt_uw_user_accounts 
    where account_id = $recipient_account_id;

    if ($data_not_found = true or row_count() <= 0) then
        set $error_code = 404;          /* resource not found */
        leave main;
    end if;

    /* 
    $deposit_type is trx_type of mtt_tx_transaction_types
    account_type 0 means reward account.
    So $deposit_type 1200 means cash income and must go to account_type > 0 
    */
    if $recipient_account_type = 0 then 
        if $deposit_type <> 1100 then
            set $error_code = 400;        /* invalid request */
            leave main;
        end if;
    elseif $recipient_account_type > 0 then 
        if $deposit_type <> 1200 then 
            set $error_code = 400;        /* invalid request */
            leave main;
        end if;
    end if;

    start transaction;

    update mtt_uw_user_accounts 
    set balance_amount = balance_amount + $deposit_amount,
        updated_at = $updated_at  
    where account_no = $recipient_account_no;

    call mtp_tx_write_transaction_for_deposit
    (
        $recipient_account_no,
        $deposit_type,
        $deposit_amount,
        $sender_no, 
        $reason,

        $trx_id, 
        $error_code
    );

    if $error_code = 0 then 
        commit;
    else
        rollback;
	end if;
end;
//
DELIMITER ;
