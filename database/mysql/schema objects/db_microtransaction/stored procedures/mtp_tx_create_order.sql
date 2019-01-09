DELIMITER //
create procedure mtp_tx_create_order
(
    $user_id 				varchar(50),
    $platform_type          varchar(50),
    $app_type               varchar(50), 

	out $order_no 			int,
    out $order_id           varchar(50),
    out $error_code			int
)
main:begin
    declare $new_id varchar(50) default null;
    declare $created_at datetime default current_timestamp();

    declare exit handler for SQLEXCEPTION, SQLWARNING
    begin
        rollback;
        resignal;
    end;

    set $error_code = 0;

    if  ($user_id is null or trim($user_id) = '') then 
		set $error_code = 400;			/* invalid request */
		leave main;
    end if;

    set @user_no = check_user($user_id);
    if (@user_no is null) then 
		set $error_code = 404;			/* resource not found */
		leave main;
    end if;

    select  sum(pp.unit_price) as order_amount, 
            sum(pp.unit_price) * 0.1 as tax_amount, 
            sum(pp.unit_price) + (sum(pp.unit_price) * 0.1) as total_amount 
	into @order_amount, @tax_amount, @total_amount
    from mtt_tx_carts c 
    join mtt_md_products p 
    on c.product_no = p.product_no 
    join mtt_md_product_prices pp 
    on p.product_no = pp.product_no 
    where c.user_no = @user_no 
    and pp.account_type = 840;

    if (@order_amount is null) then
        set $error_code = 406;          /* not accepted */
        leave main;
    end if;

    set $new_id = new_id();

    start transaction;

    /* Create an order */
    insert into mtt_tx_orders
        (order_id, user_no, order_status, created_at, updated_at, 
         order_amount, tax_amount, total_amount, platform_type, app_type)
    values
        ($new_id, @user_no, 201, $created_at, $created_at, 
         @order_amount, @tax_amount, @total_amount, $platform_type, $app_type);

    set $order_no = last_insert_id();
    set $order_id = $new_id;

    /* Move product data from cart to order products */
    insert into mtt_tx_order_products 
        (order_no, product_no, account_type, unit_price, order_quantity, 
         total_product_amount)
    select 	$order_no as order_no, 
			pp.product_no, 
            840 as account_type, 
            pp.unit_price, 
            c.product_quantity, 
			unit_price * product_quantity as total_product_amount 
    from mtt_tx_carts c 
    join mtt_md_products p 
    on c.product_no = p.product_no 
    join mtt_md_product_prices pp 
    on p.product_no = pp.product_no 
    where c.user_no = @user_no 
    and pp.account_type = 840;
    
    commit;
end;
//
DELIMITER ;
