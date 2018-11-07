DELIMITER //
/*
	$trx_status: 200 - Succeeded.
				   0 - Voided.
				  -1 - Failed.
*/
create procedure mtp_tx_write_transaction
(
    $account_no                 integer,
    $trx_type                   smallint,
    $trx_amount                 decimal(12, 2),
    $sender_no                  integer, 
    $trx_note                   varchar(50),

    out $trx_id 				varchar(50),
	out $error_code				int
)
main:begin
    declare $new_trx_id varchar(50) default null;
	declare $created_at datetime default current_timestamp();

	declare $data_not_found tinyint default false;
	declare continue handler for 1329
		set $data_not_found = true;

    set $error_code = 0;

    if $account_no is null then
		set $error_code = 30400;			/* invalid request */
		leave main;
    end if;

    set $new_trx_id = new_id();

    insert into mtt_tx_transactions 
        (trx_id, account_no, trx_type, trx_status, created_at, 
         updated_at, trx_amount, sender_no, trx_note)
    values
        ($new_trx_id, $account_no, $trx_type, 200, $created_at, 
         $created_at, $trx_amount, $sender_no, $trx_note);

    /*
    set $trx_no = last_insert_id();
    */
    set $trx_id = $new_trx_id;
end;
//
DELIMITER ;
