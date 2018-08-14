/*
	Payment status types
*/
insert into mtt_md_payment_status_types
	(payment_status, payment_status_name, created_at, updated_at, payment_status_description)
values
	(102, 'pending',            current_timestamp(), current_timestamp(), 'The payment is pending.'),
	(200, 'completed',          current_timestamp(), current_timestamp(), 'The payment has been successfuly completed.'),
	(201, 'created',            current_timestamp(), current_timestamp(), 'The payment has been created.'),
	(202, 'processed',          current_timestamp(), current_timestamp(), 'A payment has been accepted.'),
	(205, 'refunded',           current_timestamp(), current_timestamp(), 'The payment refunded.'),
	(301, 'reversed',           current_timestamp(), current_timestamp(), 'A payment was reversed due to a chargeback or other type of reversal.'),
	(303, 'canceled_reversal',  current_timestamp(), current_timestamp(), 'A reversal has been canceled.'),
	(400, 'invalid',            current_timestamp(), current_timestamp(), 'The payment is invalid.'),
	(401, 'voided',             current_timestamp(), current_timestamp(), 'This authorization has been voided.'),
	(402, 'required',           current_timestamp(), current_timestamp(), 'Payment required.'),
	(404, 'not_found',          current_timestamp(), current_timestamp(), 'Transaction not found.'),
	(405, 'not_allowed',        current_timestamp(), current_timestamp(), 'Operation not allowed.'),
	(406, 'not_acceptable',     current_timestamp(), current_timestamp(), 'Function or service is not acceptable.'),
	(408, 'expired',            current_timestamp(), current_timestamp(), 'This authorization has expired and cannot be captured.'),
	(409, 'duplicated',         current_timestamp(), current_timestamp(), 'Transaction duplicated.'),
	(412, 'failed',             current_timestamp(), current_timestamp(), 'Transaction failed.'),
	(451, 'denied',             current_timestamp(), current_timestamp(), 'The payment denied.'),
	(500, 'server_error',       current_timestamp(), current_timestamp(), 'Internal server error.'),
	(503, 'unavailable',        current_timestamp(), current_timestamp(), 'Service unavailable.'),
	(504, 'timeout',            current_timestamp(), current_timestamp(), 'Time out.'),
	(520, 'unknown',            current_timestamp(), current_timestamp(), 'Unknown error.');
