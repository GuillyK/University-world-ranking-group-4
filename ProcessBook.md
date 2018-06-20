Process book --- Together with your completed analysis, you will hand in a process book that documents the analysis process as well as the finalized product. It contains your daily resume of decisions and other considerations.

4 juni:
democratisch in twee rondes university world ranking gekozen
Research

5 juni:
Tobias csv gemaakt
landen in aparte kolommen doen zodat we daarmee data kunnen bekijken
explore weghalen
n\a vervangen door 'None'
Tabellen samenvoegen ranking en scores naar één tabel

6 juni:
outliers van ratio bekijken \\
  aangepast:
  * Washington University 
  * Griffith University
  * Czech tech
  * AGH Poland
zelf scores bereken waar deze missen met gegeven formule

size of universities added. small <= 5000. 5000 < medium <= 15000. Large > 15000
https://www.collegedata.com/cs/content/content_choosearticle_tmpl.jhtml?articleId=10006


8 juni:<br />
Besloten hoe de missinde waarden ingevuld worden:
  * Wanneer er een van de drie jaar bekend is; gebruik deze waarde voor de andere jaren 
  * Wanneer er twee van de drie jaar bekend is; gebruik het gemiddelde van die waarden 
      Wanneer er bij bijvoorbeeld 'ratio' .5 uitkwam dit afronden naar boven
  * Wanneer er geen andere waarden bekend zijn; gebruik het gemiddelde van alle waarden uit die kolom.
        Ratio ; 49
        ...

11 juni: <br />
Uitvoeren wat er op 8 juni is besloten.
Missende industry incomes en ratios uitgerekend op basis van omliggende jaren

12 juni: <br />
* Kijken welke verbanden er te vinden zijn in de data en welke hiervan interessant zijn. 
* Beginnen met het uitzoeken hoe Bokeh werkt.

13 juni: <br />
* De 'overall' score uitrekenen op basis van de formule en de ingevulde waarden
* Verder kijken naar mogelijke verbanden in data en de functies van Bokeh

14 juni: <br />
* Lijst met continenten gebruikt om de universiteiten ook op te delen per categorie 'continent' 
* Begonnen met het vinden van alle Engelstalige universiteiten <br />
      Hierbij zijn uit de lijst kleine landen verwijderd die niet in de ranking voorkomen. <br />
      (Australia, Canada, New Zealand, United Kingdom, United States, Ireland, Jamaica) <br /> <br />
      Er is niet rekening gehouden met of er universiteiten zijn in engelstalige landen die niet engelstalig zijn.

15 juni: <br />
* toevoegen van continenten in csv-files 
* toevoegen van engelstalige landen in csv-files  <br />
    Bij de Engelstalige universiteiten staat een 1; niet Engelstalig 0 <br />
    Engelstalige Universiteiten hebben een hogere score
    
18 juni: <br />
* Nieuw verband: citations heeft een sterk verband met research en teaching
* Begonnen met kaart van alle universiteiten
* Percentages per land (aantal uni's in ranking)
* Uploaden multivariates van alle jaren 
* Begonnen met alle string waarden te veranderen naar integers

Datum | Charlotte | Guilly | Nienke | Tobias
--- | --- | --- | --- | --- 
19/06 | verbanden zoeken tussen landen | Landen verbeterd + anomalies | added ints + Landen verbeterd | Started scraping universities
20/06 | Pie charts maken + verbanden zoeken tussen landen | Radar charts maken | added missing universities | Scraped all universities, completed map


