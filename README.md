# 🔧 Projektowanie Układów Cyfrowych – Ćwiczenia laboratoryjne

Repozytorium zawiera projekty zrealizowane w ramach laboratorium z projektowania układów cyfrowych. Projekty wykorzystują środowiska takie jak **Multisim** oraz **Quartus**, a także języki opisu sprzętu **VHDL** i **SystemVerilog**.

---

## 📋 Spis ćwiczeń

### 😃 Ćwiczenie 1 – Transkoder binarny na wyświetlacz emotikon

**Zadanie:**  
Zaprojektować układ kombinacyjny realizujący **transkoder 3-bitowej liczby binarnej** na graficzną emotikonę wyświetlaną na 16-punktowym układzie (np. LED).

**Wymagania:**
- Użycie **wyłącznie bramek NAND**
- Implementacja w formie **Subcircuit** (podukładu)
- Wyświetlanie na układzie zrealizowanym z próbników w **Multisim**
- Projekt można rozbudować o dodatkowe funkcje graficzne

**Cele:**
- Zrozumienie zasady działania bramek NAND jako bramek uniwersalnych
- Projektowanie układów kombinacyjnych od podstaw

---

### 🔢 Ćwiczenie 2 – Czterobitowy licznik Fibonacciego

**Zadanie:**  
Zaprojektować licznik 4-bitowy działający zgodnie z ciągiem Fibonacciego: 0, 1, 1, 2, 3, 5, 8, 13, 0, 1, 1, 2, ...


**Wymagania:**
- Użycie **jednego, konkretnego typu przerzutników** (D)
- Dowolne bramki logiczne
- Wyświetlanie wartości na **wyświetlaczach siedmiosegmentowych**
- Trudniejsza wersja - 1 występuje dwa razy w każdym cyklu

**Cele:**
- Analiza i projektowanie liczników niestandardowych
- Praktyczne zastosowanie pamięci w logice sekwencyjnej

---

### 🎵 Ćwiczenie 3 – Automat sterujący odtwarzaczem MP3

**Zadanie:**  
Zaprojektować automat sterujący prostym odtwarzaczem plików mp3 z obsługą przycisków:

- `STOP`
- `PLAY`
- `NEXT`
- `PREVIOUS`

**Dodatkowe wymagania:**
- Automat powinien posiadać 2-bitowe wyjście binarne określające numer utworu
- Wskazane jest zaprojektowanie sygnałów i wskaźników stanu (np. diody LED lub wyświetlacz)

**Cele:**
- Zastosowanie automatów Moore’a lub Mealy’ego w praktyce
- Projektowanie logiki sterującej z użyciem wejść/wyjść binarnych

---

### 🧠 Ćwiczenie 4 – System wyboru menu na układzie FPGA

**Zadanie:**  
Zaimplementować system wyboru menu na **układzie FPGA** (np. UP2, DE2, DE2-70) z użyciem środowiska **Quartus Altera**.

**Funkcjonalność:**
- Dwa przyciski (`lewy`, `prawy`)
- Dwa wyświetlacze siedmiosegmentowe (`lewy`, `prawy`)
- Lewy przycisk: zwiększa wartość na lewym wyświetlaczu (cyklicznie 0–9)
- Prawy przycisk: zapamiętuje wartość z lewego na prawym wyświetlaczu
- Po uruchomieniu: oba wyświetlacze pokazują `0`

**Technologia:**
- Implementacja w języku **VHDL**
- Środowisko: **Quartus Altera II**
