insert into trip(trip_name, country, trip_date, max_no_places)
values ('Wycieczka do Paryza', 'Francja', to_date('2023-09-12', 'YYYY-MM-DD'), 5);

insert into trip(trip_name, country, trip_date, max_no_places)
values ('Piekny Krakow', 'Polska', to_date('2025-05-03','YYYY-MM-DD'), 4);

insert into trip(trip_name, country, trip_date, max_no_places)
values ('Znow do Francji', 'Francja', to_date('2025-05-01','YYYY-MM-DD'), 6);

insert into trip(trip_name, country, trip_date, max_no_places)
values ('Hel', 'Polska', to_date('2025-05-01','YYYY-MM-DD'), 4);

create or replace view vw_reservation as
select
    r.reservation_id,
    t.country,
    t.trip_date,
    t.trip_name,
    p.firstname,
    p.lastname,
    r.status,
    t.trip_id,
    p.person_id,
    r.no_tickets
from RESERVATION r
join TRIP t on r.TRIP_ID = t.TRIP_ID
join PERSON p on r.PERSON_ID = p.PERSON_ID;

create or replace view vw_trip as
select
    t.trip_id,
    t.COUNTRY,
    t.TRIP_DATE,
    t.TRIP_NAME,
    t.MAX_NO_PLACES,
    (t.max_no_places - COALESCE(SUM(r.no_tickets), 0)) AS no_available_places
from TRIP t
left join RESERVATION r on t.TRIP_ID = r.TRIP_ID and r.STATUS != 'C'
group by t.trip_id, t.COUNTRY, t.TRIP_DATE, t.TRIP_NAME, t.MAX_NO_PLACES;

create or replace function f_trip_participants(p_trip_id int) RETURN SYS_REFCURSOR AS v_cursor SYS_REFCURSOR;
begin
    open v_cursor for
    SELECT reservation_id, country, trip_date, trip_name, firstname, lastname, status, trip_id, person_id, no_tickets
    FROM vw_reservation
    WHERE trip_id = p_trip_id;
    RETURN v_cursor;
end f_trip_participants;

select f_trip_participants(2) from dual;

create or replace function f_person_reservations(p_person_id int) return sys_refcursor as v_cursor sys_refcursor;
begin
    open v_cursor for
    select reservation_id, country, trip_date, trip_name, firstname, lastname, status, trip_id, person_id, no_tickets
    from vw_reservation
    where person_id = p_person_id;
    return v_cursor;
end f_person_reservations;

select f_person_reservations(4) from dual;

CREATE OR REPLACE FUNCTION f_available_trips_to(p_country VARCHAR2, p_date_from DATE, p_date_to DATE) RETURN SYS_REFCURSOR AS
    v_cursor SYS_REFCURSOR;
BEGIN
    OPEN v_cursor FOR
    SELECT trip_id, country, trip_date, trip_name, max_no_places, NUMBER_LEFT
    FROM vw_available_trip
    WHERE country = p_country AND trip_date BETWEEN p_date_from AND p_date_to;
    RETURN v_cursor;
END f_available_trips_to;


CREATE OR REPLACE PROCEDURE p_add_reservation(
    p_trip_id INT,
    p_person_id INT,
    p_no_tickets INT) AS
    v_available_places INT;
BEGIN
    SELECT no_available_places INTO v_available_places FROM vw_trip WHERE trip_id = p_trip_id;

    IF v_available_places IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'Nie znaleziono wycieczki o podanym ID.');
    END IF;

    IF v_available_places < p_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20002, 'Brak wystarczającej liczby miejsc.');
    END IF;

    INSERT INTO reservation (trip_id, person_id, status, no_tickets)
    VALUES (p_trip_id, p_person_id, 'N', p_no_tickets);

    COMMIT;
END p_add_reservation;

CREATE OR REPLACE PROCEDURE p_modify_reservation_status(
    p_reservation_id INT,
    p_status CHAR) AS
    v_old_status CHAR;
BEGIN
    SELECT status INTO v_old_status FROM vw_reservation WHERE reservation_id = p_reservation_id;

    IF v_old_status = 'C' THEN
        RAISE_APPLICATION_ERROR(-20003, 'Nie można zmienić statusu anulowanej rezerwacji.');
    END IF;

    UPDATE reservation
    SET status = p_status
    WHERE reservation_id = p_reservation_id;

    INSERT INTO log (reservation_id, log_date, status)
    VALUES (p_reservation_id, SYSDATE, p_status);

    COMMIT;
END p_modify_reservation_status;

CREATE OR REPLACE TRIGGER trg_log_insert_reservation
AFTER INSERT ON reservation
FOR EACH ROW
BEGIN
    INSERT INTO log (reservation_id, log_date, status, no_tickets)
    VALUES (:NEW.reservation_id, SYSDATE, :NEW.status, :NEW.no_tickets);
END;
/

CREATE OR REPLACE TRIGGER trg_log_update_status
AFTER UPDATE OF status ON reservation
FOR EACH ROW
WHEN (OLD.status != NEW.status)
BEGIN
    INSERT INTO log (reservation_id, log_date, status, no_tickets)
    VALUES (:NEW.reservation_id, SYSDATE, :NEW.status, :NEW.no_tickets);
END;
/

CREATE OR REPLACE PROCEDURE p_add_reservation_4(
    p_trip_id INT,
    p_person_id INT,
    p_no_tickets INT) AS
    v_available_places INT;
BEGIN
    -- Sprawdzenie dostępności miejsc na podstawie vw_trip
    SELECT no_available_places INTO v_available_places FROM vw_trip WHERE trip_id = p_trip_id;

    IF v_available_places IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'Nie znaleziono wycieczki o podanym ID.');
    END IF;

    IF v_available_places < p_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20002, 'Brak wystarczającej liczby miejsc.');
    END IF;

    -- Dodanie rezerwacji (trigger automatycznie doda wpis do log)
    INSERT INTO reservation (trip_id, person_id, status, no_tickets)
    VALUES (p_trip_id, p_person_id, 'N', p_no_tickets);

    -- Zatwierdzenie transakcji
    COMMIT;
END p_add_reservation_4;
/

CREATE OR REPLACE PROCEDURE p_modify_reservation_status_4(
    p_reservation_id INT,
    p_status CHAR) AS
    v_old_status CHAR;
BEGIN
    -- Pobranie aktualnego statusu rezerwacji
    SELECT status INTO v_old_status FROM vw_reservation WHERE reservation_id = p_reservation_id;

    IF v_old_status = 'C' THEN
        RAISE_APPLICATION_ERROR(-20003, 'Nie można zmienić statusu anulowanej rezerwacji.');
    END IF;

    -- Aktualizacja statusu (trigger doda wpis do log)
    UPDATE reservation
    SET status = p_status
    WHERE reservation_id = p_reservation_id;

    -- Zatwierdzenie transakcji
    COMMIT;
END p_modify_reservation_status_4;
/

CREATE OR REPLACE TRIGGER trg_check_availability_on_status_change
BEFORE UPDATE OF status ON reservation
FOR EACH ROW
WHEN (NEW.status = 'P' AND OLD.status != 'P')
DECLARE
    v_available_places INT;
BEGIN
    -- Pobranie liczby dostępnych miejsc z widoku vw_trip
    SELECT no_available_places INTO v_available_places
    FROM vw_trip
    WHERE trip_id = :NEW.trip_id;

    IF v_available_places < :NEW.no_tickets THEN
        RAISE_APPLICATION_ERROR(-20010, 'Nie ma wystarczającej liczby wolnych miejsc na tę wycieczkę.');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_check_availability_on_status_change
BEFORE UPDATE OF status ON reservation
FOR EACH ROW
WHEN (NEW.status = 'P' AND OLD.status != 'P')
DECLARE
    v_max_places INT;
    v_reserved_places INT;
BEGIN
    -- Maksymalna liczba miejsc na wycieczkę
    SELECT max_no_places INTO v_max_places
    FROM trip
    WHERE trip_id = :NEW.trip_id;

    -- Liczba już potwierdzonych biletów (bez tej zmienianej rezerwacji)
    SELECT COALESCE(SUM(no_tickets), 0) INTO v_reserved_places
    FROM reservation
    WHERE trip_id = :NEW.trip_id AND status = 'P' AND reservation_id != :NEW.reservation_id;

    -- Sprawdzenie dostępności
    IF (v_max_places - v_reserved_places) < :NEW.no_tickets THEN
        RAISE_APPLICATION_ERROR(-20010, 'Brak wolnych miejsc na tę wycieczkę.');
    END IF;
END;
/

CREATE OR REPLACE PROCEDURE p_modify_reservation_status_5(
    p_reservation_id INT,
    p_status CHAR) AS
    v_old_status CHAR;
BEGIN
    -- Pobranie obecnego statusu rezerwacji
    SELECT status INTO v_old_status FROM reservation WHERE reservation_id = p_reservation_id;

    -- Nie można zmieniać statusu anulowanej rezerwacji
    IF v_old_status = 'C' THEN
        RAISE_APPLICATION_ERROR(-20011, 'Nie można zmienić statusu anulowanej rezerwacji.');
    END IF;

    -- Aktualizacja statusu (trigger sprawdzi dostępność i zapisze do logu)
    UPDATE reservation
    SET status = p_status
    WHERE reservation_id = p_reservation_id;

    -- Zatwierdzenie transakcji
    COMMIT;
END p_modify_reservation_status_5;
/

CREATE OR REPLACE PROCEDURE p_add_reservation_6a(
    p_trip_id INT,
    p_person_id INT,
    p_no_tickets INT) AS
    v_available_places INT;
BEGIN
    -- Sprawdzenie dostępności miejsc z trip.no_available_places
    SELECT no_available_places INTO v_available_places FROM trip WHERE trip_id = p_trip_id;

    IF v_available_places IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'Wycieczka nie istnieje.');
    END IF;

    IF v_available_places < p_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20002, 'Brak wystarczającej liczby miejsc.');
    END IF;

    -- Dodanie rezerwacji
    INSERT INTO reservation (trip_id, person_id, status, no_tickets)
    VALUES (p_trip_id, p_person_id, 'P', p_no_tickets); -- zakładamy od razu 'P'

    -- Aktualizacja dostępnych miejsc
    UPDATE trip
    SET no_available_places = no_available_places - p_no_tickets
    WHERE trip_id = p_trip_id;

    COMMIT;
END p_add_reservation_6a;
/

CREATE OR REPLACE PROCEDURE p_modify_reservation_status_6a(
    p_reservation_id INT,
    p_status CHAR) AS
    v_old_status CHAR;
    v_trip_id INT;
    v_no_tickets INT;
BEGIN
    SELECT status, trip_id, no_tickets INTO v_old_status, v_trip_id, v_no_tickets
    FROM reservation
    WHERE reservation_id = p_reservation_id;

    IF v_old_status = 'C' THEN
        RAISE_APPLICATION_ERROR(-20003, 'Nie można zmienić statusu anulowanej rezerwacji.');
    END IF;

    -- Aktualizacja statusu
    UPDATE reservation
    SET status = p_status
    WHERE reservation_id = p_reservation_id;

    -- Zmiana dostępnych miejsc jeśli status przechodzi na/z 'P'
    IF v_old_status != 'P' AND p_status = 'P' THEN
        UPDATE trip
        SET no_available_places = no_available_places - v_no_tickets
        WHERE trip_id = v_trip_id;
    ELSIF v_old_status = 'P' AND p_status != 'P' THEN
        UPDATE trip
        SET no_available_places = no_available_places + v_no_tickets
        WHERE trip_id = v_trip_id;
    END IF;

    COMMIT;
END p_modify_reservation_status_6a;
/

CREATE OR REPLACE TRIGGER trg_update_no_available_on_insert_6b
AFTER INSERT ON reservation
FOR EACH ROW
WHEN (NEW.status = 'P')
BEGIN
    UPDATE trip
    SET no_available_places = no_available_places - :NEW.no_tickets
    WHERE trip_id = :NEW.trip_id;
END;
/

CREATE OR REPLACE TRIGGER trg_update_no_available_on_status_change_6b
AFTER UPDATE OF status ON reservation
FOR EACH ROW
BEGIN
    IF :OLD.status != 'P' AND :NEW.status = 'P' THEN
        -- Zmiana na status 'P' – zmniejszamy liczbę dostępnych miejsc
        UPDATE trip
        SET no_available_places = no_available_places - :NEW.no_tickets
        WHERE trip_id = :NEW.trip_id;
    ELSIF :OLD.status = 'P' AND :NEW.status != 'P' THEN
        -- Zmiana ze statusu 'P' na inny – przywracamy dostępne miejsca
        UPDATE trip
        SET no_available_places = no_available_places + :NEW.no_tickets
        WHERE trip_id = :NEW.trip_id;
    END IF;
END;
/

CREATE OR REPLACE PROCEDURE p_add_reservation_6b(
    p_trip_id INT,
    p_person_id INT,
    p_no_tickets INT) AS
    v_available_places INT;
BEGIN
    -- Sprawdzenie dostępnych miejsc z trip
    SELECT no_available_places INTO v_available_places FROM trip WHERE trip_id = p_trip_id;

    IF v_available_places IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'Wycieczka nie istnieje.');
    END IF;

    IF v_available_places < p_no_tickets THEN
        RAISE_APPLICATION_ERROR(-20002, 'Brak wolnych miejsc.');
    END IF;

    -- Dodanie rezerwacji ze statusem 'P' (trigger zadba o aktualizację)
    INSERT INTO reservation (trip_id, person_id, status, no_tickets)
    VALUES (p_trip_id, p_person_id, 'P', p_no_tickets);

    COMMIT;
END p_add_reservation_6b;
/

CREATE OR REPLACE PROCEDURE p_modify_reservation_status_6b(
    p_reservation_id INT,
    p_status CHAR) AS
    v_old_status CHAR;
BEGIN
    SELECT status INTO v_old_status FROM reservation WHERE reservation_id = p_reservation_id;

    IF v_old_status = 'C' THEN
        RAISE_APPLICATION_ERROR(-20003, 'Nie można zmienić statusu anulowanej rezerwacji.');
    END IF;

    UPDATE reservation
    SET status = p_status
    WHERE reservation_id = p_reservation_id;

    COMMIT;
END p_modify_reservation_status_6b;
/