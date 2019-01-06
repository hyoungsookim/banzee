/* Test purpose */
insert into mtt_md_products 
    (product_id, product_status, product_name, product_type, created_at, updated_at, product_description)
values
    ('TEST_PRODUCT_A', 200, 'Test product A', 'ITEM', now(), now(), 'product description'),
    ('TEST_PRODUCT_B', 200, 'Test product B', 'ITEM', now(), now(), 'product description');
