/*
	Product Prices
*/
create table mtt_md_product_prices
(
	product_no				int 			not null,
	price_type 				smallint		not null,
	unit_price 			    decimal(12, 2)	not null,
	updated_datetime 		datetime 		not null,

    constraint pk_mtt_md_product_prices
		primary key (product_no, price_type)
);
