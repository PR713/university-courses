create sequence s_person_seq
    start with 1
    increment by 1;
create table person
(
    person_id int not null
        constraint pk_person
            primary key,
    firstname varchar(50),
    lastname  varchar(50)
);
alter table person
    modify person_id int default s_person_seq.nextval;



create sequence s_trip_seq
    start with 1
    increment by 1;
create table trip
(
    trip_id       int not null
        constraint pk_trip
            primary key,
    trip_name     varchar(100),
    country       varchar(50),
    trip_date     date,
    max_no_places int
);
alter table trip
    modify trip_id int default s_trip_seq.nextval;



create sequence s_reservation_seq
    start with 1
    increment by 1;
create table reservation
(
    reservation_id int not null
        constraint pk_reservation
            primary key,
    trip_id        int,
    person_id      int,
    status         char(1),
    no_tickets     int
);
alter table reservation
    modify reservation_id int default s_reservation_seq.nextval;
alter table reservation
    add constraint reservation_fk1 foreign key
        (person_id) references person (person_id);
alter table reservation
    add constraint reservation_fk2 foreign key
        (trip_id) references trip (trip_id);
alter table reservation
    add constraint reservation_chk1 check
        (status in ('N', 'P', 'C'));



create sequence s_log_seq
    start with 1
    increment by 1;

create table log
(
    log_id         int  not null
        constraint pk_log
            primary key,
    reservation_id int  not null,
    log_date       date not null,
    status         char(1),
    no_tickets     int
);
alter table log
    modify log_id int default s_log_seq.nextval;
alter table log
    add constraint log_chk1 check
        (status in ('N', 'P', 'C')) enable;
alter table log
    add constraint log_fk1 foreign key
        (reservation_id) references reservation (reservation_id);



insert into person(firstname, lastname)
values ('Jan', 'Nowak');
insert into person(firstname, lastname)
values ('Jan', 'Kowalski');
insert into person(firstname, lastname)
values ('Jan', 'Nowakowski');
insert into person(firstname, lastname)
values ('Novak', 'Nowak');



insert into reservation(trip_id, person_id, status, no_tickets)
values (1, 1, 'P', 1);
insert into reservation(trip_id, person_id, status, no_tickets)
values (1, 2, 'N', 2);
insert into reservation(trip_id, person_id, status, no_tickets)
values (2, 1, 'P', 1);
insert into reservation(trip_id, person_id, status, no_tickets)
values (3, 4, 'C', 3);
insert into reservation(trip_id, person_id, status, no_tickets)
values (4, 4, 'P', 4);


SELECT *
FROM TRIP;
--DELETE FROM TRIP
--alter sequence s_trip_seq restart start with 1;
alter sequence s_person_seq restart start with 6;

SELECT *
FROM PERSON;
SELECT *
FROM RESERVATION;


--czy dodać constraint na no_tickets i max_no_places

insert into reservation(trip_id, person_id, status, no_tickets)
values (5, 4, 'P', 4);



BEGIN
    INSERT INTO trip(trip_name, country, trip_date, max_no_places)
    VALUES ('Słoneczna Chorwacja', 'Chorwcja', to_date('2025-06-10', 'YYYY-MM-DD'), 5);
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        raise;
END;


BEGIN
    INSERT INTO reservation(trip_id, person_id, status, no_tickets) VALUES (1000, 11, 'P', 2);
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Transaction reversed due to: ' || SQLERRM);
        raise;
END;



SELECT *
FROM PERSON;


BEGIN
    INSERT INTO reservation(trip_id, person_id, status, no_tickets) VALUES (3, 11, 'ABC', 2);
    INSERT INTO person (firstname, lastname) VALUES ('Anna', 'Kowalczyk');
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Transaction reversed due to: ' || SQLERRM);
END;


---------------------------------------------


create or replace view vw_available_trip
as
select t.trip_id,
       t.trip_name,
       t.country,
       t.trip_date,
       t.max_no_places,
       t.max_no_places - COALESCE(sum(r.no_tickets), 0) as number_left
from TRIP t
         left join RESERVATION r on r.trip_id = t.trip_id and r.status != 'C'
where t.trip_date > SYSDATE
group by t.trip_id, t.trip_name, t.country, t.trip_date, t.max_no_places
having t.max_no_places - COALESCE(sum(r.no_tickets), 0) > 0;


select *
from vw_available_trip;


-------------------------------------


CREATE OR REPLACE FUNCTION f_available_trips_to(p_country VARCHAR2, p_date_from DATE, p_date_to DATE) RETURN SYS_REFCURSOR AS
    v_cursor SYS_REFCURSOR;
    v_exists NUMBER;
BEGIN
    SELECT COUNT(*)
    INTO v_exists
    FROM TRIP t
    WHERE t.COUNTRY = p_country
      AND t.TRIP_DATE BETWEEN p_date_from AND p_date_to;

    IF v_exists = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'There are no trips to this country between specified dates.');
    END IF;

    OPEN v_cursor FOR
        SELECT trip_id, country, trip_date, trip_name, max_no_places, number_left
        FROM vw_available_trip
        WHERE country = p_country
          AND trip_date BETWEEN p_date_from AND p_date_to;
    RETURN v_cursor;
END f_available_trips_to;



SELECT f_available_trips_to('Polska', CURRENT_DATE, '2025-06-30')
from dual;

select f_available_trips_to('FRANCJA', CURRENT_DATE, '2025-06-30')
from dual;

SELECT *
from TRIP;


------------------procedures

CREATE OR REPLACE PROCEDURE p_modify_max_no_places(
    trip_id IN NUMBER,
    max_no_places IN NUMBER
) AS
    v_no_reserved_places NUMBER;
    v_trip_exists        NUMBER;
BEGIN

    SELECT COUNT(*)
    INTO v_trip_exists
    FROM TRIP t
    WHERE t.trip_id = p_modify_max_no_places.trip_id;

    IF v_trip_exists = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Trip does not exist');
    END IF;

    IF p_modify_max_no_places.max_no_places IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'New number of places cannot be null!');
    END IF;

    IF p_modify_max_no_places.max_no_places <= 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'New number of places have to be greater than 0!');
    END IF;


    SELECT SUM(r.no_tickets)
    INTO v_no_reserved_places
    FROM reservation r
    WHERE r.trip_id = p_modify_max_no_places.trip_id
      AND status IN ('N', 'P');

    IF (max_no_places < v_no_reserved_places) THEN
        RAISE_APPLICATION_ERROR(-20004, 'New number of places is less than number of reserved places');
    END IF;

    UPDATE TRIP
    SET TRIP.max_no_places = p_modify_max_no_places.max_no_places
    WHERE TRIP.trip_id = p_modify_max_no_places.trip_id;

    DBMS_OUTPUT.PUT_LINE('Zaktualizowano max_no_places');
    COMMIT;
END;


begin
    P_MODIFY_MAX_NO_PLACES(1, 9);
end;

SELECT *
FROM TRIP;


--------procedura nr 3


CREATE OR REPLACE PROCEDURE p_modify_reservation(
    reservation_id IN NUMBER,
    no_tickets IN NUMBER
) AS
    v_trip_id          NUMBER;
    v_old_no_tickets   NUMBER;
    v_old_status       VARCHAR(1);
    v_new_status       VARCHAR(1);
    v_max_places       NUMBER;
    v_available_places NUMBER;
BEGIN

    IF no_tickets < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'The no_tickets have to be greater than 0!');
    end if;

    SELECT r.TRIP_ID, r.NO_TICKETS, r.STATUS
    INTO v_trip_id, v_old_no_tickets, v_old_status
    FROM RESERVATION r
    WHERE r.reservation_id = p_modify_reservation.reservation_id;

    IF v_trip_id IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'Such a reservation does not exist!');
    END IF;

    SELECT NO_AVAILABLE_PLACES, MAX_NO_PLACES
    INTO v_available_places, v_max_places
    FROM VW_TRIP vwt
    WHERE vwt.TRIP_ID = v_trip_id;

    IF NO_TICKETS > v_available_places + v_old_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20003, 'There are not that number of available places');
    END IF;

    IF no_tickets = 0 THEN
        v_new_status := 'C';
    ELSIF no_tickets = v_old_no_tickets THEN
        v_new_status := v_old_status;
    ELSE
        v_new_status := 'N'; -- C -> N no_tickets > 0
    END IF;

    UPDATE RESERVATION
    SET NO_TICKETS = p_modify_reservation.no_tickets,
        STATUS     = v_new_status
    WHERE RESERVATION_ID = p_modify_reservation.reservation_id;

    IF V_NEW_STATUS != V_OLD_STATUS THEN
        INSERT INTO LOG(RESERVATION_ID, LOG_DATE, STATUS, NO_TICKETS)
        VALUES (p_modify_reservation.reservation_id, SYSDATE, V_NEW_STATUS, NO_TICKETS);
    END IF;

    COMMIT;
END;



BEGIN
    P_MODIFY_RESERVATION(8, 5);
end;



SELECT *
FROM VW_TRIP;


------------------------------ TRIGGERS


CREATE OR REPLACE TRIGGER trg_update_log_no_tickets
    AFTER UPDATE OF no_tickets
    ON reservation
    FOR EACH ROW
    WHEN (NEW.no_tickets <> OLD.no_tickets)
BEGIN
    INSERT INTO log(log_id, reservation_id, log_date, status, no_tickets)
    VALUES (s_log_seq.nextval, :NEW.reservation_id, SYSDATE, :NEW.status, :NEW.no_tickets);
end;


CREATE OR REPLACE TRIGGER trg_prevent_delete_reservation
    BEFORE DELETE
    ON reservation
    FOR EACH ROW
BEGIN
    RAISE_APPLICATION_ERROR(-20001, 'You cannot delete reservation. You can only cancel it.');
end;


--------------- procedures_4


CREATE OR REPLACE PROCEDURE p_modify_reservation_4(
    reservation_id IN NUMBER,
    no_tickets IN NUMBER
) AS
    v_trip_id          NUMBER;
    v_old_no_tickets   NUMBER;
    v_old_status       VARCHAR(1);
    v_new_status       VARCHAR(1);
    v_max_places       NUMBER;
    v_available_places NUMBER;
BEGIN

    IF no_tickets < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'The no_tickets have to be greater than 0!');
    end if;

    SELECT r.TRIP_ID, r.NO_TICKETS, r.STATUS
    INTO v_trip_id, v_old_no_tickets, v_old_status
    FROM RESERVATION r
    WHERE r.reservation_id = p_modify_reservation_4.reservation_id;

    IF v_trip_id IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'Such a reservation does not exist!');
    END IF;

    SELECT NO_AVAILABLE_PLACES, MAX_NO_PLACES
    INTO v_available_places, v_max_places
    FROM VW_TRIP vwt
    WHERE vwt.TRIP_ID = v_trip_id;

    IF NO_TICKETS > v_available_places + v_old_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20003, 'There are not that number of available places');
    END IF;

    IF no_tickets = 0 THEN
        v_new_status := 'C';
    ELSIF no_tickets = v_old_no_tickets THEN
        v_new_status := v_old_status;
    ELSE
        v_new_status := 'N'; -- C -> N no_tickets > 0
    END IF;

    UPDATE RESERVATION
    SET NO_TICKETS = p_modify_reservation_4.no_tickets,
        STATUS     = v_new_status
    WHERE RESERVATION_ID = p_modify_reservation_4.reservation_id;

    COMMIT;
END;


SELECT *
from vw_available_trip;

BEGIN
    p_modify_reservation_4(3, 3);
end;


-----procedures 5

CREATE OR REPLACE PROCEDURE p_add_reservation_5(
    p_trip_id IN NUMBER,
    p_person_id IN NUMBER,
    p_no_tickets IN NUMBER
) AS
    v_person_exists NUMBER;
    v_trip_exists   NUMBER;
BEGIN

    IF p_no_tickets <= 0 THEN
        RAISE_APPLICATION_ERROR(-20010, 'The number of tickets has to be greater than 0.');
    END IF;

    SELECT COUNT(*) INTO v_person_exists FROM person WHERE person_id = p_person_id;
    IF v_person_exists = 0 THEN
        RAISE_APPLICATION_ERROR(-20011, 'That person does not exist!');
    END IF;

    SELECT COUNT(*) INTO v_trip_exists FROM trip WHERE trip_id = p_trip_id;
    IF v_trip_exists = 0 THEN
        RAISE_APPLICATION_ERROR(-20012, 'The trip does not exist!');
    END IF;

    INSERT INTO reservation (trip_id, person_id, no_tickets, status)
    VALUES (p_trip_id, p_person_id, p_no_tickets, 'N');

    COMMIT;
END;



CREATE OR REPLACE PROCEDURE p_modify_reservation_5(
    reservation_id IN NUMBER,
    no_tickets IN NUMBER
) AS
    v_trip_id        NUMBER;
    v_old_no_tickets NUMBER;
    v_old_status     VARCHAR(1);
    v_new_status     VARCHAR(1);
BEGIN

    IF no_tickets < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'The no_tickets have to be greater than 0!');
    end if;

    SELECT r.TRIP_ID, r.NO_TICKETS, r.STATUS
    INTO v_trip_id, v_old_no_tickets, v_old_status
    FROM RESERVATION r
    WHERE r.reservation_id = p_modify_reservation_5.reservation_id;

    IF v_trip_id IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'Such a reservation does not exist!');
    END IF;

    IF no_tickets = 0 THEN
        v_new_status := 'C';
    ELSIF no_tickets = v_old_no_tickets THEN
        v_new_status := v_old_status;
    ELSE
        v_new_status := 'N'; -- C -> N no_tickets > 0
    END IF;

    UPDATE RESERVATION
    SET NO_TICKETS = p_modify_reservation_5.no_tickets,
        STATUS     = v_new_status
    WHERE RESERVATION_ID = p_modify_reservation_5.reservation_id;

    COMMIT;
END;


----- triggers 5


CREATE OR REPLACE TRIGGER trg_check_reservation_availability
    BEFORE INSERT
    ON reservation
    FOR EACH ROW
DECLARE
    v_available_places NUMBER;
BEGIN

    SELECT NO_AVAILABLE_PLACES
    INTO v_available_places
    FROM VW_TRIP
    WHERE VW_TRIP.TRIP_ID = :NEW.trip_id;

    IF :NEW.no_tickets > v_available_places THEN
        RAISE_APPLICATION_ERROR(-20020, 'A lack of places! Available: ' || v_available_places);
    END IF;
END;


CREATE OR REPLACE TRIGGER trg_change_no_tickets
    BEFORE UPDATE OF no_tickets
    ON reservation
    FOR EACH ROW
DECLARE
    old_no_tickets     NUMBER;
    new_no_tickets     NUMBER;
    v_available_places NUMBER;
BEGIN
    old_no_tickets := :OLD.no_tickets;
    new_no_tickets := :NEW.no_tickets;

    SELECT NO_AVAILABLE_PLACES
    INTO v_available_places
    FROM VW_TRIP vwt
    WHERE vwt.TRIP_ID = :NEW.trip_id;

    IF new_no_tickets > v_available_places + old_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20003, 'There are not that number of available places');
    END IF;
end;


------------------------------------ ZAD 6


ALTER TABLE trip
    ADD no_available_places INT NULL;

CREATE OR REPLACE PROCEDURE p_recalculate_available_places
AS
BEGIN
    UPDATE TRIP t
    SET no_available_places = t.max_no_places - COALESCE(
            (SELECT sum(r.no_tickets)
             FROM RESERVATION r
             WHERE r.trip_id = t.trip_id
               AND r.status IN ('N', 'P'))
        , 0);

    COMMIT;

    DBMS_OUTPUT.PUT_LINE('The available number of places have been recalculated.');
end;


BEGIN
    P_RECALCULATE_AVAILABLE_PLACES();
end;
--poprawnie bierze 'N' || 'P'


----PROCEDURES 6a


create or replace PROCEDURE p_modify_reservation_6a(
    reservation_id IN NUMBER,
    no_tickets IN NUMBER
) AS
    v_trip_id          NUMBER;
    v_old_no_tickets   NUMBER;
    v_old_status       VARCHAR(1);
    v_new_status       VARCHAR(1);
    v_max_places       NUMBER;
    v_available_places NUMBER;
    v_trip_date        DATE;
BEGIN

    IF no_tickets < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'The no_tickets have to be greater than 0!');
    end if;

    SELECT r.TRIP_ID, r.NO_TICKETS, r.STATUS, t.trip_date
    INTO v_trip_id, v_old_no_tickets, v_old_status, v_trip_date
    FROM RESERVATION r
             JOIN TRIP t ON r.TRIP_ID = t.TRIP_ID
    WHERE r.reservation_id = p_modify_reservation_6a.reservation_id;

    IF v_trip_id IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'Such a reservation does not exist!');
    END IF;

    IF v_trip_date <= SYSDATE THEN
        RAISE_APPLICATION_ERROR(-20003, 'That trip has already taken place, cannot modify details of reservation!');
    END IF;

    SELECT NO_AVAILABLE_PLACES, MAX_NO_PLACES
    INTO v_available_places, v_max_places
    FROM VW_TRIP vwt
    WHERE vwt.TRIP_ID = v_trip_id;

    IF NO_TICKETS > v_available_places + v_old_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20003, 'There are not that number of available places');
    END IF;

    IF no_tickets = 0 THEN
        v_new_status := 'C';
    ELSIF no_tickets = v_old_no_tickets THEN
        v_new_status := v_old_status;
        COMMIT;
    ELSE
        v_new_status := 'N'; -- C -> N no_tickets > 0
    END IF;

    UPDATE RESERVATION
    SET NO_TICKETS = p_modify_reservation_6a.no_tickets,
        STATUS     = v_new_status
    WHERE RESERVATION_ID = p_modify_reservation_6a.reservation_id;

    UPDATE TRIP t
    SET no_available_places = t.max_no_places - COALESCE(
            (SELECT sum(r.no_tickets)
             FROM RESERVATION r
             WHERE r.trip_id = v_trip_id
               AND r.status IN ('N', 'P'))
        , 0)
    WHERE trip_id = v_trip_id;

    COMMIT;
END;
/


---

create PROCEDURE p_modify_max_no_places_6a(
    trip_id IN NUMBER,
    max_no_places IN NUMBER
) AS
    v_no_reserved_places NUMBER;
    v_trip_exists        NUMBER;
    v_trip_date          DATE;
BEGIN

    SELECT COUNT(*), t.trip_date
    INTO v_trip_exists, v_trip_date
    FROM TRIP t
    WHERE t.trip_id = p_modify_max_no_places_6a.trip_id
    GROUP BY t.trip_date;
    --dla nieistniejącej wycieczki COUNT(*) powoduje że trip_date jest NULL
    -- i wyjątek nie poleci, jeśli nie użylibyśmy f. agregującem to wtedy
    -- mamy DATA_NOT_FOUND exception :)

    IF v_trip_exists = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Trip does not exist');
    END IF;

    IF p_modify_max_no_places_6a.max_no_places IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'New number of places cannot be null!');
    END IF;

    IF p_modify_max_no_places_6a.max_no_places <= 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'New number of places have to be greater than 0!');
    END IF;

    IF v_trip_date <= SYSDATE THEN
        RAISE_APPLICATION_ERROR(-20005, 'Nie można modyfikować wycieczki, która już się odbyła');
    END IF;


    SELECT SUM(r.no_tickets)
    INTO v_no_reserved_places
    FROM reservation r
    WHERE r.trip_id = p_modify_max_no_places_6a.trip_id
      AND status IN ('N', 'P');

    IF (max_no_places < v_no_reserved_places) THEN
        RAISE_APPLICATION_ERROR(-20004, 'New number of places is less than number of reserved places');
    END IF;

    UPDATE TRIP t
    SET t.max_no_places       = p_modify_max_no_places_6a.max_no_places,
        t.no_available_places = t.max_no_places - COALESCE(
                (SELECT sum(r.no_tickets)
                 FROM RESERVATION r
                 WHERE r.trip_id = p_modify_max_no_places_6a.trip_id
                   AND r.status IN ('N', 'P'))
            , 0)
    WHERE t.trip_id = p_modify_max_no_places_6a.trip_id;


    DBMS_OUTPUT.PUT_LINE('Filed max_no_places has been updated');
    COMMIT;
END;
/


--- modyfikacja widoku, zakładamy, że dzięki procedurom mamy aktualne dane w bazie

create or replace view vw_available_trip_6a
as
select t.trip_id,
       t.trip_name,
       t.country,
       t.trip_date,
       t.max_no_places,
       t.no_available_places
from TRIP t
where t.trip_date > SYSDATE
  and t.no_available_places > 0;


------ zad 6b


CREATE OR REPLACE PROCEDURE p_modify_reservation_6b(
    reservation_id IN NUMBER,
    no_tickets IN NUMBER
) AS
    v_trip_id          NUMBER;
    v_old_no_tickets   NUMBER;
    v_old_status       VARCHAR2(1);
    v_new_status       VARCHAR2(1);
    v_trip_date        DATE;
    v_available_places NUMBER;
    v_max_places       NUMBER;
BEGIN
    IF no_tickets < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'The no_tickets have to be greater than 0!');
    END IF;


    SELECT r.TRIP_ID, r.NO_TICKETS, r.STATUS, t.trip_date
    INTO v_trip_id, v_old_no_tickets, v_old_status, v_trip_date
    FROM RESERVATION r
             JOIN TRIP t ON r.TRIP_ID = t.TRIP_ID
    WHERE r.reservation_id = p_modify_reservation_6b.reservation_id;

    IF v_trip_date <= SYSDATE THEN
        RAISE_APPLICATION_ERROR(-20003, 'That trip has already taken place, cannot modify details of reservation!');
    END IF;

    SELECT NO_AVAILABLE_PLACES, MAX_NO_PLACES
    INTO v_available_places, v_max_places
    FROM VW_TRIP vwt
    WHERE vwt.TRIP_ID = v_trip_id;

    IF NO_TICKETS > v_available_places + v_old_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20003, 'There are not that number of available places');
    END IF;


    IF no_tickets = 0 THEN
        v_new_status := 'C';
    ELSIF no_tickets = v_old_no_tickets THEN
        v_new_status := v_old_status;
    ELSE
        v_new_status := 'N';
    END IF;


    UPDATE reservation
    SET no_tickets = p_modify_reservation_6b.no_tickets,
        status     = v_new_status
    WHERE reservation_id = p_modify_reservation_6b.reservation_id;

    COMMIT;
END;
/


CREATE OR REPLACE TRIGGER tr_reservation_manage_6b
    AFTER UPDATE ON reservation
    FOR EACH ROW
DECLARE
    v_trip_date DATE;
    v_max_places NUMBER;
BEGIN
    UPDATE TRIP t
    SET no_available_places = t.max_no_places - COALESCE(
            (SELECT sum(r.no_tickets)
             FROM RESERVATION r
             WHERE r.trip_id = :NEW.trip_id
               AND r.status IN ('N', 'P'))
        , 0)
    WHERE trip_id = :NEW.trip_id;
END;
/



------------------------------------------------------------------------------








-------------------


SELECT trigger_name, table_name, triggering_event, status
FROM user_triggers
ORDER BY table_name, trigger_name;