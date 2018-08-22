/*
	Orders
*/
create table mtt_tx_orders
(
	order_no 				int 			not null auto_increment,
	order_id 				varchar(50)		not null,
	user_no 				int 			not null,
	order_status 			smallint		not null,
	platform_type			varchar(50)		not null,
	app_type				varchar(50)		not null,
	created_at		        datetime 		not null,
	updated_at 		        datetime 		not null,
	order_amount 			decimal(12, 2) 	not null,
	tax_amount 				decimal(12, 2)	not null,
	total_amount 			decimal(12, 2)	not null,

    constraint pk_mtt_tx_orders
		primary key (order_no)
);