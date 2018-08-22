insert into mtt_md_payment_methods 
    (method_code, method_status, method_name, method_type, created_at, updated_at)
values
    ('STRIPECARD', 200, 'Credit Card', 'CC', current_timestamp(), current_timestamp());
