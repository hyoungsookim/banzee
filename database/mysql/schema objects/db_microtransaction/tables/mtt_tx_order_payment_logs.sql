/*
	Order Payment Logs
*/
create table mtt_tx_order_payment_logs
(
	log_no 					int 			not null auto_increment,
	order_no 				int 			not null,
	method_code 			varchar(10) 	not null,
	payment_status 			smallint		not null,
	created_at		        datetime		not null,
	remote_ip	 			varchar(50)		null,
	log_text 				text			null,

    constraint pk_mtt_tx_order_payment_logs
		primary key (log_no)
);
