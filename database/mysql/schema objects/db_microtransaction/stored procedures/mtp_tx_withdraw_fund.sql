DELIMITER //
/*
    mtp_tx_withdraw_fund
        Process fund withrawal from a specific user account.

    params:
        $account_id: account id. 
        $withdrawal_amount: amount to withdraw from $account_id
        $source_transaction_id: transaction id value of order. (order_id)
        $reason: 
*/
create procedure mtp_tx_withdraw_fund
(
    $account_id             varchar(50),
    $withdrawal_type        smallint, 
    $withdrawal_amount      decimal(12, 2),
    $source_transaction_id  varchar(50), 
    $reason                 varchar(50),

    out $error_code		    int
)
main:begin
    declare $account_no int default null;
    declare $account_type smallint default null;
    declare $account_status smallint default null;
    declare $balance_amount decimal(12, 2) default null;
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

    /* $deposit_amount should be bigger than 0.0 */
    if ($withdrawal_amount < 0.0) then 
        /* operation not accepted */
        set $error_code = 405;
        leave main;
    end if;

    select  account_no, account_type, account_status, balance_amount 
    into $account_no, $account_type, $account_status, $balance_amount 
    from mtt_uw_user_accounts 
    where account_id = $account_id;

    if ($data_not_found = true or row_count() <= 0) then
        /* resource not found. */
        set $error_code = 404;
        leave main;
    end if;

    if ($account_status <> 200) then 
        /* operatioin not allowed. account is not activated status */
        set $error_code = 405;
        leave main;
    end if;

    if ($balance_amount - $withdrawal_amount < 0) then 
        /* operation not accepted. Insufficient balance */
        set $error_code = 406;
        leave main;
    end if;
    
    start transaction;

    update mtt_uw_user_accounts 
    set balance_amount = balance_amount - $withdrawal_amount,
        updated_at = $updated_at  
    where account_no = $account_no;

    call mtp_tx_write_transaction_for_withdrawal
    (
        $account_no,
        $withdrawal_type,
        $withdrawal_amount,
        $source_transaction_id, 
        $reason,

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
