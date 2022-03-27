# Cryptocurrency-Investment-Portfolio

Zakładamy, że użytkownik naszego programu dysponuje zasobami finansowymi różnego pokroju: akcje zagraniczne, akcje polskie, kryptowaluty, waluty, ... 
Można rozszerzyć/zmodyfikować zbiór - modyfikacje do konsultacji. Nasz program ma w praktyczny sposób podsumować portfolio inwestycyjne. 
Wykorzystując nabyte podczas semestru umiejętności programistyczne piszemy namiastkę klienta inwestycyjnego.

1. Program ma czytać z JSONa konfiguracyjnego informacje o posiadanych zasobach, ich ilościach oraz średniej cenie ich nabycia. Ma się tam również znaleźć info o walucie bazowej USD/EUR/PLN

2. Ściągamy z dostępnych API notowania zasobów w stosunku do waluty bazowej. 
a) Jeśli są dostępne informacje o kupnie/sprzedaży - patrzymy na kursy kupna i liczymy z którymi ofertami trzeba sparować zasób użytkownika, by wyprzedać całą posiadaną ilość (patrzymy wgłąb tabeli bids) 
b) Jeśli dla danego zasobu nie mamy dostępu o kursach kupna/sprzedaży (np bezpłatne api dla akcji) upraszczamy proces - bierzemy cenę ostatniej transakcji i nie liczymy wolumenu 
W wyniku zadania 2 wyświetlamy listę zasobów użytkownika w tabeli (nazwa zasobu, ilość, cena(cena ostatniej transakcji), wartość(liczona wg cen jak w punktach a i b) ). 
W ostatnim wierszu tabeli uwzględnić sumy poszczególnych pól z kolumny wartość (i dla przyszłej kolumny z zadania 3 i 4).

3. Analogicznie do zadania 2 liczymy to samo tylko do zadanej głębokości portfolio. 
Użytkownik wprowadza informację, że chciałby sprzedać przykładowo 10% swoich zasobów i dla tej ilości robimy wycenę jak z zadania 2. 
Dodajemy do tabeli kolumnę "wartość 10%"
(uwaga kontrolna - cena z podpunktu a) będzie korzystniejsza, bo patrzymy "płycej" w książce ofert kupna, czyli patrzymy tylko na korzystniejsze oferty)

4. Uwzględnić w przybliżeniu należny podatek od zysków kapitałowych. W Polsce jest to 19% od zysków. By policzyć zysk musimy najpierw policzyć całkowity koszt nabycia zasobu lub części zasobu którą zamierzamy sprzedać.
Do tabeli dodać kolumnę wartość netto (wartość danego zasobu po odjęciu należnego podatku od zysku. Zysk to obecna wartość DANEJ ILOŚCI ZASOBU pomniejszona o koszt JEJ nabycia). 
Analogicznie dodajemy "wartość 10% netto" dla uzupełnienia kwoty netto do zad 3 

5. Do tabeli dodać skrótową informację o rekomendowanym miejscu sprzedaży - gdzie spośród dostępnych giełd najbardziej opłaca się sprzedać dany zasób. 
Mogą to być 3 pierwsze litery giełdy z najkorzystniejszą w danym momencie ceną. 

6. Wykorzystać zadanie realizowane w ramach poprzedniej listy i do tabeli z zasobami dodać informację o możliwym arbitrażu. Arbitraż sprawdzać tylko na zbiorze zasobów dostępnych w portfolio. 
Kolumnę nazwać arbitraż, wpisać do niej skrótowo nazwy giełd i parę walutową na której jest możliwy arbitraż oraz potencjalny zysk. Można założyć, że ten punkt dotyczy tylko kryptowalut.
Przykładowo BB-BITT, LTCBTC, +0.6LTC

ENG

We assume that the user of our program has financial resources of various types: foreign shares, Polish shares, cryptocurrencies, currencies, ...
You can extend / modify the set - modifications for consultation. Our program is designed to sum up the investment portfolio in a practical way.
Using the programming skills acquired during the semester, we write a substitute for an investment client.

1. The program is to read from the configuration JSON information about the resources, their quantity and the average purchase price. There will also be information about the base currency USD / EUR / PLN 

2. We download stock quotes in relation to the base currency from the available APIs.
a) If there is information about buying / selling - we look at the buying rates and count with which offers the user's resource needs to be paired to sell off the entire amount (look deep into the bids table) 
b) If we do not have access to buy / sell rates for a given resource (e.g. free api for shares), we simplify the process - we take the price of the last transaction and do not count the volume 
As a result of task 2, we display the list of user's resources in the table (resource name, quantity, price (price of the last transaction), value (calculated according to prices as in points a and b)).
In the last row of the table, include the sums of individual fields from the Value column (and for the future column from tasks 3 and 4).

3. Similarly to task 2, we count the same only for a given portfolio depth.
The user enters the information that he would like to sell, for example, 10% of his resources and for this amount we make a valuation as in task 2.
We add the column "value 10%" to the table
(control note - the price from sub-point a) will be more favorable, because we look "shallower" in the book of purchase offers, i.e. we only look at more favorable offers) 

4.Calculate the approximate capital gains tax due. In Poland, it is 19% of profits. To calculate the profit, we must first calculate the total cost of acquiring the resource or part of the resource that we intend to sell.
To the table, add the column net value (value of a given resource after deducting the tax due on profit. Profit is the present value of the GIVEN AMOUNT OF THE RESOURCE minus the cost of its acquisition).
Similarly, we add "10% net value" to supplement the net amount to task 3

5. Add to the table brief information about the recommended point of sale - where, from among the available exchanges, it is most profitable to sell a given resource.
These can be the first 3 letters of the exchange with the most advantageous price at a given moment.

6. Use the task from the previous list and add information about possible arbitration to the resource table. Arbitration to be checked only on the set of resources available in the portfolio.
Name the column arbitration, enter abbreviated names of exchanges and the currency pair on which arbitration is possible and potential profit. It can be assumed that this point only applies to cryptocurrencies.
For example BB-BITT, LTCBTC, + 0.6LTC 

7. Convenient graphic interface to the program, it can be placed as a front to the project. The interface is to allow you to enter resources, their quantity and the average cost of purchasing a unit, and to save the portfolio to json 

Hint: if in any case you need to convert currencies between each other, e.g. USD to PLN, and there is no reliable information on the exchange rate on the stock exchange, please use the NBP API, average exchange rates from the last available day.

7. Wygodny interfejs graficzny do programu, może być jako front postawiony do projektu. Interfejs ma umożliwiać wprowadzenie zasobów, ich ilości i średniego kosztu nabycia jednostki oraz zapis portfela do jsona

Hint: jeśli w którymś przypadku wystąpi u Was konieczność przeliczenia walut pomiędzy sobą np USD na PLN a na giełdzie nie będzie wiarygodnej informacji o kursie proszę wykorzystać API NBP, kursy średnie z ostatniego dostępnego dnia.

