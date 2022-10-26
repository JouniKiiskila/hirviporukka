-- AN EXAMPLE FOR PROCEDURE WICH ADDS A NEW GROUP

-- Create a procedure with 2 arguments, in is default
CREATE PROCEDURE public.add_jakoryhma(
    seurue integer,
    ryhman_nimi character varying)
-- Lanquage standard sql    
LANGUAGE SQL
AS $$ -- BEGIN
    INSERT INTO public.jakoryhma (seurue_id, ryhman_nimi)
    VALUES (seurue, ryhman_nimi);
$$; -- END