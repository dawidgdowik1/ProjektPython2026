Krok 1: Logowanie do Panelu pgAdmin 4 Web
Adres URL: Otwórz przeglądarkę internetową (Mozilla Firefox) i przejdź pod adres:
http://localhost/pgadmin4
Logowanie: Użyj danych podanych podczas instalacji pakietu pgadmin4-web (e-mail: student@wsiz.edu.pl hasło
student).
Krok 2: Tworzenie Kont użytkownika i bazy danych
CREATE DATABASE db_lab_3
Należy przełączyć się do stworzonej bazy danych. Utworzenie użytkowników (ról z prawem logowania)
CREATE ROLE pracownik;
CREATE ROLE kierownik;
Utworzenie roli nielogowanych:
CREATE ROLE jan_kowalski WITH LOGIN PASSWORD 'HasloJana123';
CREATE ROLE anna_nowak WITH LOGIN PASSWORD 'HasloAnny123';
CREATE ROLE audytor WITH LOGIN PASSWORD 'Audytor123' VALID UNTIL '2026-12-31';
Sprawdzenie ról na bazie
Krok 3: Stworzyć tabele na bazie danych i schematy
Stworzyć schemat a na nim tabele pracownicy i zamówienia wraz z przykładowymi kolumnami.
CREATE TABLE pracownicy (
 id SERIAL PRIMARY KEY,
 imie VARCHAR(50),
 nazwisko VARCHAR(50),
 pensja NUMERIC(10,2)
);
CREATE TABLE zamowienia (
 id_zamowienia SERIAL PRIMARY KEY,
 klient VARCHAR(100),
 wartosc NUMERIC(10,2)
);
INSERT INTO pracownicy (imie, nazwisko, pensja) VALUES
('Jan', 'Kowalski', 5000.00),
('Anna', 'Nowak', 8500.00);
INSERT INTO zamowienia (klient, wartosc) VALUES
('Firma A', 1200.50),
('Firma B', 450.00);
Krok 4: Testowe Logowanie na Konto Nowego Użytkownika
Nadać uprawnienia grupom
-- 1. Zezwolenie na połączenie z bazą
GRANT CONNECT ON DATABASE db_lab_3 TO pracownik, kierownik;
-- 2. Zezwolenie na korzystanie ze schematu publicznego
GRANT USAGE ON SCHEMA public TO pracownik, kierownik;
-- 3. Uprawnienia dla roli 'pracownik' (tylko odczyt zamówień)
GRANT SELECT ON TABLE zamowienia TO pracownik;
-- 4. Uprawnienia dla roli 'kierownik' (pełna kontrola nad zamówieniami i pracownikami)
GRANT ALL PRIVILEGES ON TABLE zamowienia, pracownicy TO kierownik;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO kierownik;
-- 5. Uprawnienia na poziomie kolumn (audytor widzi pracowników, ale bez kolumny pensja)
GRANT CONNECT ON DATABASE db_lab_3 TO audytor;
GRANT USAGE ON SCHEMA public TO audytor;
GRANT SELECT (id, imie, nazwisko) ON TABLE pracownicy TO audytor;
Krok 5: Przypisanie userów do grup
-- Przypisanie użytkowników do grup
GRANT pracownik TO jan_kowalski;
GRANT kierownik TO anna_nowak;
-- Zezwolenie Annie na przekazywanie uprawnień roli kierownik dalej (ADMIN OPTION)
GRANT kierownik TO anna_nowak WITH ADMIN OPTION;
Krok 6: Test użytkowników
-- Test 1: Jan Kowalski (grupa pracownik)
SET ROLE jan_kowalski;
SELECT CURRENT_USER;
-- Zadziała:
SELECT * FROM zamowienia;
-- Zwróci błąd (Permission denied):
SELECT * FROM pracownicy;
-- Powrót do administratora
RESET ROLE;
-- Test 2: Audytor (uprawnienia kolumnowe)
SET ROLE audytor;
-- Zadziała:
SELECT id, imie, nazwisko FROM pracownicy;
-- Zwróci błąd:
SELECT pensja FROM pracownicy;
RESET ROLE;
Krok 7: Odbieranie uprawnień i usuwanie ról (REVOKE / DROP)
-- 1. Odebranie uprawnienia
REVOKE SELECT ON TABLE zamowienia FROM pracownik;
-- 2. Usunięcie użytkownika z roli
REVOKE pracownik FROM jan_kowalski;
-- 3. Bezpieczne usunięcie roli (wymaga uprzedniego zrzucenia przypisanych
obiektów/uprawnień)
DROP OWNED BY audytor;
DROP ROLE audytor;
