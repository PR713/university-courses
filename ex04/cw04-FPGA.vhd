library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity cw04FPGA is
    port (
        clk     : in  std_logic;                     -- zegar (np. 50 MHz)
        pb1     : in  std_logic;                     -- przycisk lewy (aktywny w '0')
        pb2     : in  std_logic;                     -- przycisk prawy (aktywny w '0')
        hex0    : out std_logic_vector(6 downto 0);  -- wyœwietlacz lewy
        hex1    : out std_logic_vector(6 downto 0)   -- wyœwietlacz prawy
    );
end entity;

architecture rtl of cw04FPGA is
    signal left_val     : unsigned(3 downto 0) := (others => '0');
    signal selected_val : unsigned(3 downto 0) := (others => '0');
    
    -- Sygna³y do debouncingu
    constant DEBOUNCE_TIME : integer := 50000;
    signal pb1_db_cnt : integer range 0 to DEBOUNCE_TIME := 0;
    signal pb2_db_cnt : integer range 0 to DEBOUNCE_TIME := 0;
    signal pb1_db     : std_logic := '1';
    signal pb2_db     : std_logic := '1';
    signal pb1_prev   : std_logic := '1';
    signal pb2_prev   : std_logic := '1';
    
    -- Rejestry synchronizuj¹ce
    signal pb1_sync   : std_logic_vector(1 downto 0) := "11";
    signal pb2_sync   : std_logic_vector(1 downto 0) := "11";

    function to_7seg(n : unsigned(3 downto 0)) return std_logic_vector is
        variable seg : std_logic_vector(6 downto 0);
    begin
        case n is
            when "0000" => seg := "1000000"; -- 0
            when "0001" => seg := "1111001"; -- 1
            when "0010" => seg := "0100100"; -- 2
            when "0011" => seg := "0110000"; -- 3
            when "0100" => seg := "0011001"; -- 4
            when "0101" => seg := "0010010"; -- 5
            when "0110" => seg := "0000010"; -- 6
            when "0111" => seg := "1111000"; -- 7
            when "1000" => seg := "0000000"; -- 8
            when "1001" => seg := "0010000"; -- 9
            when others => seg := "1111111"; -- blank
        end case;
        return seg;
    end function;

begin
    process(clk)
    begin
        if rising_edge(clk) then
            -- Synchronizacja wejœæ (2-stopniowa)
            pb1_sync <= pb1_sync(0) & pb1;
            pb2_sync <= pb2_sync(0) & pb2;
            
            -- Debouncing PB1
            if pb1_sync(1) = '0' then  -- Przycisk wciœniêty (aktywny w '0')
                if pb1_db_cnt < DEBOUNCE_TIME then
                    pb1_db_cnt <= pb1_db_cnt + 1;
                else
                    pb1_db <= '0';
                end if;
            else
                pb1_db_cnt <= 0;
                pb1_db <= '1';
            end if;
            
            -- Debouncing PB2
            if pb2_sync(1) = '0' then  -- Przycisk wciœniêty (aktywny w '0')
                if pb2_db_cnt < DEBOUNCE_TIME then
                    pb2_db_cnt <= pb2_db_cnt + 1;
                else
                    pb2_db <= '0';
                end if;
            else
                pb2_db_cnt <= 0;
                pb2_db <= '1';
            end if;
            
            -- Wykrywanie zbocza opadaj¹cego (przejœcie z '1' na '0')
            pb1_prev <= pb1_db;
            pb2_prev <= pb2_db;
            
            -- Logika dla PB1 (zwiêkszanie wartoœci)
            if pb1_db = '0' and pb1_prev = '1' then
                if left_val = "1001" then
                    left_val <= (others => '0');
                else
                    left_val <= left_val + 1;
                end if;
            end if;
            
            -- Logika dla PB2 (zapisywanie wartoœci)
            if pb2_db = '0' and pb2_prev = '1' then
                selected_val <= left_val;
            end if;
        end if;
    end process;

    hex0 <= to_7seg(left_val);
    hex1 <= to_7seg(selected_val);
end rtl;