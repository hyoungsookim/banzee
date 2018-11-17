DELIMITER //
/*
	$trx_status: 200 - Succeeded.
				 412 - Failed.
*/
create procedure mtp_tx_write_transaction_for_withdrawal
(
    $account_no                 integer,
    $withdrawal_type            smallint,
    $withdrawal_amount          decimal(12, 2),
    $source_transaction_id      varchar(50), 
    $trx_note                   varchar(50),

	out $error_code				int
)
main:begin
	declare $created_at datetime default current_timestamp();

    set $error_code = 0;

    if $account_no is null then
		set $error_code = 400;			/* invalid request */
		leave main;
    end if;

    /* 
    $withdrawal_type is trx_type of mtt_tx_transaction_types
    $withdrawal_type should be expense (>= 2000 of transaction types) 
    */
    if ($withdrawal_type < 2000) then
        /* operation not accepted. */
        set $error_code = 405;
        leave main;
    end if;

    if $source_transaction_id is null or trim($source_transaction_id) = '' then
		set $error_code = 400;			/* invalid request */
		leave main;
    end if;

    insert into mtt_tx_transactions 
        (trx_id, account_no, trx_type, trx_status, created_at, 
         updated_at, trx_amount, trx_note)
    values
        ($source_transaction_id, $account_no, $withdrawal_type, 200, $created_at, 
         $created_at, $withdrawal_amount, $trx_note);
end;
//
DELIMITER ;
