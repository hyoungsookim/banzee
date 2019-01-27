DELIMITER //
create procedure mtp_tx_create_order_payment
(
    $order_id               varchar(50),
    $method_code            varchar(10),
    $payment_currency       varchar(3),
    $payment_amount         decimal(12, 2),

	out $payment_no 		int,
    out $error_code			int
)
main:begin
    declare $user_no int default null;
    declare $order_no int default null;
    declare $created_at datetime default current_timestamp();

	declare $data_not_found tinyint default false;
	declare continue handler for 1329
		set $data_not_found = true;

    declare exit handler for SQLEXCEPTION, SQLWARNING
    begin
        rollback;
        resignal;
    end;

    set $error_code = 0;

    /*
    if  ($user_id is null or trim($user_id) = '') then 
		set $error_code = 400;
		leave main;
    end if;
    */

    if ($payment_amount is null or $payment_amount <= 0) then
        set $error_code = 406;          /* not accepted */
        leave main;
    end if;

    select o.order_no, o.user_no 
    into $order_no, $user_no  
    from mtt_tx_orders o 
    where o.order_id = $order_id;

    if ($data_not_found = true or row_count() <= 0) then
        set $error_code = 404;          /* resource not found */
        leave main;
    end if;

    start transaction;

    /* Create an order */
    insert into mtt_tx_order_payments
        (order_no, method_code, payment_status, created_at, updated_at, 
         payment_currency, payment_amount)
    values
        ($order_no, $method_code, payment_status, $created_at, $created_at, 
         $payment_currency, $payment_amount);

    set $payment_no = last_insert_id();
    
    /* change order status 
    update mtt_tx_orders
    set order_status = 200 
    where order_id = $order_id
    */

    commit;
end;
//
DELIMITER ;
