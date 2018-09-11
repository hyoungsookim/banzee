/*
	Order Payments
*/
create table mtt_tx_order_payments
(
	payment_no				int				not null auto_increment,
	order_no 				int 			not null,
	method_code 			varchar(10) 	not null,
	payment_status 			smallint		not null,
	created_at		        datetime		not null,
	updated_at 		        datetime 		not null,
	payment_currency		varchar(3)		not null,
	payment_amount 			decimal(12, 2)	not null,
	trx_id					varchar(50)		null,
	ref_id 				    varchar(50)		null,
	approval_code 			varchar(50)		null,
	reason_code 			varchar(50)		null,
	avs_result 				varchar(50)		null,
	cvv_result 				varchar(50)		null,

    constraint pk_mtt_tx_order_payments
		primary key (payment_no)
);