DELIMITER //
CREATE DEFINER=`root`@`%` FUNCTION `new_id`()
RETURNS varchar(36) CHARSET utf8
    NO SQL
    DETERMINISTIC
begin
	declare $id char(36);

    set $id = uuid();

    return concat(substr($id, 15, 4), '-', 
                  substr($id, 10, 4), '-', 
                  substr($id, 1, 8), '-', 
                  substr($id, 20, 4), '-', 
                  substr($id, 25));
end;
//
DELIMITER ;
