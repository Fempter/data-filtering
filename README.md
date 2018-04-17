# data-filtering
Filtering data using Pandas

**Analiza ABPM** <br />


1. Po PESEL, który będzie nazwą pliku (Patient name) będziemy wciągać surowe dane do naszej bazy danych. <br />
2. Do analizy nie bierzemy pomiarów mających inny znacznik niż „0” w pozycji „ERR” - error lub „EXC” - exclude <br />
3. Do naszej bazy danych chcemy, żeby system wyliczał i prezentował następujące parametry: <br />
    1. średnia i SD z całego okresu pomiaru dla: <br />
        1. SYS (systolic= SBP) <br />
        2. DIA (diastolic=DBP) <br />
        3. PUL (pulse = HR) <br />
        4. MAP (wg wzoru: DIA+1/3(SYS-DIA)) <br />
    2. % wyników SYS (ładunek SBP) >130 z całego okresu pomiaru <br />
    3. % wyników DIA (ładunek DBP) > 80 z całego okresu pomiaru <br />
    4. średnia, SD, najmniejszy wynik (min.) i największy wynik (maks.) z okresu snu (między „SLEEP TIME” a "WAKE TIME"): <br />
        1. SYS (systolic= SBP) <br />
        2. DIA (diastolic=DBP) <br />
        3. PUL (pulse = HR) <br />
        4. MAP (wg wzoru: DIA+1/3(SYS-DIA)) <br />
    5. % wyników SYS (ładunek SBP) >120 z okresu snu <br />
    6. % wyników DIA (ładunek DBP) > 70 z okresu snu <br />
    7. średnia, SD, najmniejszy wynik (min.) i największy wynik (maks.) z okresu czuwania (między „WAKE TIME” a " SLEEP TIME"): <br />
        1. SYS (systolic= SBP) <br />
        2. DIA (diastolic=DBP) <br />
        3. PUL (pulse = HR) <br />
        4. MAP (wg wzoru: DIA+1/3(SYS-DIA)) <br />
    8. % wyników SYS (ładunek SBP) >135 z okresu czuwania <br />
    9. % wyników DIA (ładunek DBP) > 85 z okresu czuwania <br />
    10. średnią i SD z trzech pierwszych pomiarów <br />
    11. MS (Morning surge) dla SYS, DIA i MAP zgodnie ze wzorem: średnia z 2 godzin po „WAKE TIME” – średnia z najmniejszego wyniku z okresu snu (między „SLEEP TIME” a "WAKE TIME") i po 1 wyniku sąsiadującym <br />
    12. dipping dla SBP, DBP i MAP zgodnie ze wzorem: średnia z pomiarów w czasie czuwania (między „WAKE TIME” a " SLEEP TIME") – średnia z pomiarów w czasie snu (między „SLEEP TIME” a "WAKE TIME") / średnia z pomiarów w czasie czuwania (między „WAKE TIME” a " SLEEP TIME") * 100% <br /> <br />

UWAGA! <br />
Jeśli WAKE TIME = czasowi pomiaru to pomiar jest zaliczany do okresu czuwania <br />
Jeśli SLEEP TIME = czasowi pomiaru to pomiar jest zaliczany do okresu czuwania <br />
