
ECONSTOR
Make Your Publications Visible.
Di Casola, Paola; Stockhammar, Pär
A Service of
ZBW
Leibniz-InformationszentrumWirtschaft
Leibniz Information Centrefor Economics
Working Paper
When domestic and foreign QE overlap: Evidence fromSweden
Sveriges Riksbank Working Paper Series, No. 404
Provided in Cooperation with:
Central Bank of Sweden, Stockholm
Suggested Citation: Di Casola, Paola; Stockhammar, Pär (2021): When domestic and foreign QEoverlap: Evidence from Sweden, Sveriges Riksbank Working Paper Series, No. 404, SverigesRiksbank, Stockholm
This Version is available at:https://hdl.handle.net/10419/251302
Standard-Nutzungsbedingungen:
Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichenZwecken und zum Privatgebrauch gespeichert und kopiert werden.
Sie dürfen die Dokumente nicht für öffentliche oder kommerzielleZwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglichmachen, vertreiben oder anderweitig nutzen.
Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten,gelten abweichend von diesen Nutzungsbedingungen die in der dortgenannten Lizenz gewährten Nutzungsrechte.
Terms of use:
Documents in EconStor may be saved and copied for your personaland scholarly purposes.
You are not to copy documents for public or commercial purposes, toexhibit the documents publicly, to make them publicly available on theinternet, or to distribute or otherwise use the documents in public.
If the documents have been made available under an Open ContentLicence (especially Creative Commons Licences), you may exercisefurther usage rights as specified in the indicated licence.
WWW.ECONSTOR.EU
Mitglied der
Leibniz-Gemeinschaft
SVERIGES RIKSBANK
WORKING PAPER SERIES
404
SVERIGESRIKSBANK
When domestic and foreign QEoverlap: evidence from Sweden
Paola Di Casola and Pär Stockhammar
May 2021
WORKING PAPERS ARE OBTAINABLE FROM
www.riksbank.se/en/research
Sveriges Riksbank SE-103 37 StockholmFax international: +46 8 21 05 31Telephone international: +46 8 787 00 00
The Working Paper series presents reports on matters inthe sphere of activities of the Riksbank that are considered
to be of interest to a wider public.
The papers are to be regarded as reports on ongoing studiesand the authors will be pleased to receive comments.
The opinions expressed in this article are the sole responsibility of the author(s) and should not be
interpreted as reflecting the views of Sveriges Riksbank.
When domestic and foreign QE overlap: evidence
from Sweden*
Paola Di Casolat Pär Stockhammar+
Sveriges Riksbank Working Paper Series
No. 404
May 2021
Abstract
We estimate the effects of domestic and foreign quantitative easing (QE)programmes on a small open economy, Sweden, using a structural BVAR model.Domestic QE raised GDP, lowered unemployment and depreciated the currency,while effects on inflation are less clear. The ECB QE had large positive effectson both GDP and inflation in Sweden, also due to the endogenous response ofdomestic QE to the foreign one. In terms of transmission channels, domesticQE improved lending conditions for households and lowered expected futurerates, while foreign QE improved financing conditions for firms.
Keywords: Quantitative Easing, international spillovers, transmission channels,small open economy, Bayesian VAR models.
JEL classification: E44, E52, F41, G15.
*We thank Jan Alsterlind, Fabio Canova, Vesna Corbo, Jens Iversen, Mathias Klein, StefanLaséen, Jesper Lindé, Ricardo Reis, Anna Rogantini Picco, Spyridon Sichlimiris, Adi Sunderam, UlfSöderström, Karl Walentin, Francesco Zanetti and seminar participants at Sveriges Riksbank foruseful comments and suggestions. The opinions expressed in this article are the sole responsibilityof the authors and should not be interpreted as reflecting the views of Sveriges Riksbank. Any errorsare our own.
Sveriges Riksbank, SE-103 37 Stockholm, Sweden. E-mail: paola.dicasola@riksbank.se (corre-sponding author).#Sveriges Riksbank, SE-103 37 Stockholm, Sweden. E-mail: par.stockhammar@riksbank.se.
1 Introduction
The Covid-19 pandemic has forced many central banks around the world to interveneto help the functioning of the financial markets and cut their interest rates closeto the effective lower bound to stimulate the economy. The pandemic marked thereturn of unconventional monetary policy tools that were used during and after theGreat Financial Crisis, such as large-scale asset purchases.¹ Sveriges Riksbank (theSwedish central bank) also restarted its asset purchase programme. While it is fairlystraightforward to assess the effects of asset purchase programmes on the financialmarkets around the time of announcements, it has proven more difficult to evaluatetheir effects on the macroeconomy (Borio and Zabai, 2016). In a meta-analysis of themacroeconomic effects of asset purchases in the US, UK and the euro area providedby Fabo et al. (2020), effects are overall positive on output and inflation, but largevariations exist across countries and across different methodologies (Di Casola, 2021).Evaluating the effects of asset purchase programmes is particularly challenging insmall open economies, which may be also subject to spillovers from asset purchaseprogrammes conducted in large economies. This makes the estimation of the effectsof domestic unconventional monetary policy more complex, since it gives room to anendogenous response to the foreign unconventional monetary policy in expectationof its domestic repercussions. Indeed, the literature on the effects of domestic andforeign asset purchases in small open economies is scarce.2 Our paper fills this im-portant gap in the literature, by estimating the effects on the Swedish economy ofthe Quantitative Easing (QE) programme conducted by Sveriges Riksbank and theECB during the period 2015-2018. Sweden is a particularly interesting case to study,
1See Bernanke (2020) for a review of unconventional monetary policy tools used by the Fedand other central banks since the Great Financial Crisis. Bernanke (2009) distinguishes the as-set purchases conducted for expansionary purposes, labelled as Quantitative Easing policy, fromthose conducted with the purpose of improving the functioning of those financial markets that areexperiencing problems, known as Credit Easing.
2See Johnson et al. (2020) for an overview, where examples of small open economies are UK andSweden.
2
because it is a small open economy strongly affected by shocks originating from itsmain trading partners, such as the euro area (Corbo and Strid, 2020).3 Both assetpurchases programmes were aimed at making monetary policy more expansionary andwere not primarily aimed at improving the functioning of impaired financial markets(hence we label them QE). Moreover, interest rates in Sweden were cut into negativeterritory during the period the Riksbank purchased government bonds. Hence, QEwas conducted at the same time as conventional monetary policy.
In order to address the specific features of the Swedish QE programme, we usea structural BVAR model with two identification schemes with impact restrictions,inspired by Weale and Wieladek (2016). One identification strategy relies on zerorestrictions, while the other relies on zero and sign restrictions. The main benefitof this approach is the use of the cumulative announcement of purchases by boththe ECB and the Riksbank, scaled by GDP, as proxy for QE, thereby accountingfor the effects of foreign and domestic QE announcements in a BVAR model. Thedistinction of the two types of QE shocks relies on the assumption that only theSwedish QE programme was determined by Swedish economic conditions and theECB QE programme in line with the idea of a small open economy.
We find that the Riksbank QE programme had expansionary effects on the realeconomy, both in terms of output and unemployment, while the effects on prices areless clear, even though the Swedish krona weakened in real terms in response to QE.Using the scaling of purchases over GDP, the effects on output are comparable to theeffects found in the empirical literature for the US, the euro area and UK. At thesame time, the ECB QE programme had expansionary effects both on output andinflation in Sweden, despite the Swedish krona strengthening on impact. Followingthe ECB QE shock, inflation expectations and households' confidence increased inSweden. The effects on output and inflation are comparable to the effects found in3The share of Swedish imports and exports over GDP equalled 82 percent over the period 1995-2019. The euro area represents more than 40 percent of Sweden's trade.
3
the literature for the ECB QE on the euro area. The positive spillover effects arepartly due to the response of the Swedish asset purchase programme to the ECB'sprogramme, that limited the appreciation of the real exchange rate. To the bestof our knowledge, our paper is the first one to assess the spillovers of the ECB QEprogramme on a small open economy and the induced response from its domestic QE.
As explained in Haldane et al. (2016) and Borio and Zabai (2016), there are variouschannels through which large-scale asset purchases can affect the economy and makemonetary policy more expansionary: monetary policy signalling, portfolio balance andthe exchange rate channel. We find evidence of the exchange rate channel of QE andlow exchange rate pass-through. Regarding the signalling channel, the Riksbank QElowered the interest rate expectations six months, two and five years ahead, unlikethe ECB QE. There is also evidence of the portfolio balance channel for both thedomestic and foreign QE, but in different ways. The domestic QE shock improvedthe domestic financing conditions more than the ECB QE shock. The ECB QEtransmitted through a drop in risk premia, for both corporate and mortgage bonds inSweden. These results are consistent with the large role of funding in global financialmarkets of Swedish banks and firms. The Riksbank QE shock raised stock prices andhousing prices, lowered the term spread and households' lending rates.
Our work is related to the literature studying the effects of QE on the macroecon-omy. Overviews of the literature on the effects of large-scale asset purchases acrossvarious countries and methodologies are provided in Borio and Zabai (2016), Bhat-tarai and Neely (Forthcoming), Dell'Ariccia et al. (2018), Kuttner (2018) and BIS(2019).
One approach to study effects of QE on the macroeconomy is based on structural(DSGE) models with financial frictions or with a shadow rate as measure of themonetary policy stance. One such example is De Rezende and Ristiniemi (2020),4For the portfolio balance channel of QE see, among others, Chen et al. (2012), Gertler andKaradi (2013), Carlstrom et al. (2017) and Sims and Wu (2020). Mouabbi and Sahuc (2019) relies
4
the only other paper studying the effects of the Riksbank's 2015-2017 QE programmeon the macroeconomy.5 The authors first derive a shadow rate for Sweden withouta lower bound to track the stance of monetary policy when unconventional tools areused, in addition to conventional ones. Then, they introduce it into the Riksbank'sDSGE model at the time (Ramses II) and find positive effects of QE on the realeconomy (proxied by unemployment) and inflation.
Another approach is based on VAR models, where asset purchases are proxiedwith their effects on mortgage spreads (Walentin, 2014), term spreads (Baumeisterand Benati, 2013), government bond yields (Gilchrist et al., 2015) or the shadow rate(Wu and Xia, 2016).6 Examples of papers that directly use the amounts of centralbank's purchases in VAR models to identify asset purchase shocks are Gambacorta etal. (2014) Gambetti and Musso (2017), Boeckx et al. (2017) and Weale and Wieladek(2016). While the first three papers use effective purchases, Weale and Wieladek(2016) use announced purchases. Their methodology has been extended to othercountries and other sample periods in Haldane et al. (2016), Garcia Pascual andWieladek (2016) and Panizza and Wyplosz (2018), but none of these studies analysethe recent Swedish QE experience and the spillovers of the ECB QE to small openeconomies.
Few papers in the empirical literature on QE discuss the spillovers of foreign QEfor a small open economy. Covering the period before 2015, Bluwstein and Canova(2016) find positive effects for the real economy in advanced economies (includingSweden) from the ECB's unconventional monetary policy. However, effects on infla-tion are slightly negative. Chen et al. (2017) find positive spillovers from the Fed'son a shadow rate to account for the effects of QE. Alpanda and Kabaca (2020) and Kolasa andWesolowski (2020) focus on spillovers of foreign QE.
5 The announcement effects of the Riksbank QE on the financial market have been studied exten-sively in De Rezende (2017), de los Rios and Shamloo (2017), De Rezende and Ristiniemi (2020),Knezevic et al. (forthcoming) and Melander (2021). Blix Grimaldi et al. (2020) focus on the effectson the liquidity of the Swedish government bonds.
6See Rossi (2020) for a review of the time series approaches to identify the effects of unconventionalmonetary policy.
5
and the ECB's asset purchases in terms of GDP and inflation for advanced economies,including Sweden, for the period before 2015. Our paper shows that these conclusionshold also for the QE programme started in 2015 by the ECB. Our results on positivespillovers are also in line with studies of the effects of the Fed's QE programme onGDP and inflation of Canada, such as MacDonald and Popiel (2017) and Dahlhauset al. (2018).
The paper proceeds in the following way. Section 2 provides some historical back-ground on the Riksbank QE programme. Section 3 describes the theoretical trans-mission channels of QE. Section 4 and 5 describe the data and the methodology used,respectively. In section 6 we present the main results, study the response of domesticQE to foreign QE, and dig deeper into the transmission channels of the Riksbank andthe ECB QE in the Swedish economy. Section 7 contains robustness exercises andSection 8 concludes.
2 Some history and institutional details
The Riksbank has been an inflation-targeting central bank since 1993, in operationalterms since 1995. At the beginning of 2015, inflation in Sweden had been below the2 percent target for long, inflation expectations were low and trending downwards.Since Sweden is a small open economy with a large share of trade with the euroarea, the economic developments and the monetary policy decisions concerning theeuro area are closely followed in Sweden. In January 2015 the ECB announced toextend its private bond purchase programme to buy also government bonds, withpurchases divided between countries on the basis of its capital key. The programmeis known as APP (Asset Purchase Programme). At the monetary policy meetingof February 2015, the Riksbank decided to cut interest rates into negative territory
The ECB announced the total amount it intended to purchase on a monthly base, both forprivate and public bonds. In the end, though, the share of public bonds for those purchases wasaround 90 percent, hence we can consider it mostly a programme of public debt purchases.
6
for the first time in history. Thereby, it signalled that zero was not the lower boundfor the policy rate. At the same time, the Riksbank started its QE programme,by announcing purchases of SEK 10 billion of government bonds. The discussionsabout the decision involved, beyond domestic factors, also the extension of the assetpurchases programme announced by the ECB and its potential consequences for theSwedish krona.8
The Riksbank's asset purchases were funded by increasing reserves from the mon-etary policy counterparties. The Riksbank purchased bonds with the help of reverseauctions in which the Riksbank's monetary policy counterparties and the NationalDebt Office's dealers could participate. The National Debt Office is responsible formanaging the Swedish government debt. It is important to note a specific featureof the Swedish government debt market, that forces a lower bound on the level ofinterest rates on long-term government bonds. The National Debt Office providesa repo facility such that, at any point in time, without any volume restrictions, itendogenously supplies all government bonds at a one-day holding period interest rateamounting to the Riksbank policy rate minus 0.40 percentage points. Therefore, thereis a limit to how much asset purchases can lower the term premium on governmentbonds. This limit could of course affect the effectiveness of QE on the macroeconomicvariables.
The Riksbank concluded its active QE programme at the end of 2017, and carriedout only reinvestments from 2018 onwards. The ECB concluded its QE programmein 2018. Overall, the Riksbank' holdings at the end of the program amounted to SEK290 billions, corresponding to around 44 percent of the outstanding stock of nominalgovernment bonds and roughly 7 percent of GDP. As regards the ECB, accordingto data reported in BIS (2019), the share of purchases over the total outstandingstock corresponded to slightly less than 30 percent in 2019, while the share over GDPSee the minutes from the Executive Board's monetary policy meeting of February 11, 2015.
7
was roughly 25 percent. Therefore, the Riksbank QE programme was smaller thanthe ECB QE programme in terms of the country's GDP but larger in terms of theoutstanding stock.
3 How QE can affect the economy
There is a large literature discussing how the effects of asset purchases transmit to theeconomy to make monetary policy expansionary (Borio and Zabai (2016), Haldane etal. (2016)). The main channels discussed are the following:
- monetary policy signalling channel QE can convey extra information aboutthe future path of short-term interest rates.;
- portfolio balance channel QE can induce a switch into longer duration orhigher risk assets;
exchange rate channel - QE lowers the price of domestic asset relative to overseasassets.
Without frictions, general equilibrium effects make asset purchases irrelevant forthe economy, as first argued by Wallace (1981). For the channels of QE to be working,there should be frictions or imperfections in the functioning of financial markets. Inthe literature, different models have been suggested to rationalize these channels andstudy the effects of asset purchases on macroeconomic variables. Vayanos and Vila(2021) develop a model to understand how large-scale asset purchases affect long-term rates, based on the assumption of imperfect substitutability between short-term and long-term bonds and market segmentation. Building on the same type offrictions, Chen et al. (2012) study the macroeconomic effect of asset purchases in aNew Keynesian DSGE model, through their effect on long-term rates and the termThe outstanding value is proxied with the iBoxx market value for each asset class.
8
premium. On the other hand, Gertler and Karadi (2013), Carlstrom et al. (2017)and Sims and Wu (2020) build models with a banking sector that faces a leverageconstraint. The effects on the economy of central bank's purchases of public andprivate assets take place through their impact on risk premia, by easing financingconditions.
The models mentioned above focus on closed economies, hence they lack the ex-change rate channel of asset purchases. Greenwood et al. (2020) provide a generalizedversion of Vayanos and Vila (2021)'s model to explain how the US QE programmeaffect the US dollar exchange rate. Kolasa and Wesolowski (2020) and Alpanda andKabaca (2020) introduce the imperfect asset substitutability and segmented marketsin a two-country DSGE model. Cross-border holdings of government bonds imply thatthe exchange rate is affected by the change in term premia across two economies.According to the event-study analyses in De Rezende (2017) and Melander (2021),the announcement effects of the Riksbank's government bond purchases during 2015-2017 suggest that the above mentioned channels were at work. QE announcementscontributed to lower long-term government bond yields, together with corporate andmortgage bond yields, suggesting a drop in both term premia and risk premia ac-cording to the portfolio balance channel. The weaker exchange rate can be seen asevidence of the exchange rate channel. Lower interest rate expectations at varioushorizons suggest also a signalling channel at work. Our analysis can provide evidenceon whether these effects were short-lived or not and how they transmitted to outputand prices.
4
Data
We use data at monthly frequency, covering the period of active Swedish and ECBQE, from 2015 to 2018. More details on the data sources and graphs of the vari-
9
ables are reported in Appendix A. As measure of real economic activity, we use themonthly GDP indicator (activity indicator) published by Statistics Sweden. Pricesare measured with the Swedish CPIF price level.10 The stock market is measuredwith the OMX stock market index, transformed into real terms by dividing it by theprice level. In terms of interest rate variables, we include the difference between theten-year and the three-month government bond yields (the term spread). We alsouse the five-year corporate spread and mortgage spread, the households' lending rateand the Financial Conditions Index (FCI). The Financial Conditions Index, providedby Alsterlind et al. (2020), reflects financial conditions in Sweden, by summarisingthe status of five important submarkets in the Swedish financial system: the housingmarket, the bond market, the money market, the stock market and the foreign ex-change market. Inflation expectations are measured through the five-year break eveninflation and the real effective krona exchange rate is measured relative to Sweden'smain trading partners, the US and the euro area, with weights equal to 15 and 85percent, respectively. Interest rate expectations six months, two years and five yearsahead are measured through the forward rates implied by the RIBA contracts. 11
Finally, the most important variable is the measure of asset purchases. FollowingWeale and Wieladek (2016), we construct the cumulative announced purchases bythe Riksbank (Table A.2 in Appendix A) and divide it by the annualized nominalGDP of quarter 4 of 2014. By considering the purchases as ratio of 2014 GDP, i.e.before the start of QE, we can eliminate endogeneity effects coming from effects ofQE on contemporaneous GDP levels. We construct a similar measure of announcedpurchases for the ECB, as done in the analysis for the ECB QE in Garcia Pascualand Wieladek (2016). Since the ECB announced its monthly pace of purchases, we
10CPIF is the consumer price index inflation with fixed interest rate. The CPIF has been theRiksbank's operational target variable for several years and the formal inflation target variable formonetary policy as of September 2017.
11 RIBA contracts are three month swap contracts with the repo rate as the underlying asset. Thederivates curves are estimated using the extended Nelson Siegel method.
10
have aggregated these to obtain the total amount announced (Table A.3 in AppendixA). Figure 1 shows the announced purchases by the ECB and the Riksbank.
All the variables, except for the interest rates and the asset purchase series, areexpressed in natural logarithms.
30
-ECB-Riksbank
25
20
15
10
5
0
2015m1 2015m6 2015m11 2016m4 2016m9 2017m2 2017m7 2017m12 2018m5 2018m10
Figure 1: Asset purchases announced by the ECB (blue lines) and the Riksbank(red line). Shares over 2014:Q4 annualized GDP of each region.
5
Methodology
We use a BVAR model with 2 lags and Minnesota prior (see Appendix B for moredetails). 12 We use 2000 draws for the simulation and additional 500 initial draws ofburn-in.13 The baseline model contains 6 variables: ECB asset purchases, Swedishprice level, Swedish GDP indicator, Riksbank asset purchases, Swedish term spread(differences between the 10-year and the 3-month government bond yields) and theKrona real exchange rate. We modify the model in Weale and Wieladek (2016) to
12 Results are robust to replacing the Minnesota prior with the independent Wishart prior.13 We also carried out a sensitivity analysis with 10000 draws and results still hold.
11
fit the case of a small open economy. We introduce the ECB asset purchase variableas part of the exogenous block, meaning that it is assumed not to be affected bySwedish variables, since Sweden is a small open economy. With respect to Weale andWieladek (2016), our baseline system contains the Swedish real exchange rate, in orderto account for the exchange rate channel of QE. Our short sample period can rule outconcerns of structural breaks in the series of interest, due to the exceptional timesand tools used by central banks. However, it also restricts the degrees of freedom ofthe model. For this reason, we do not include one more variable to account for theconventional monetary policy carried out by the Riksbank, when it cut rates belowzero. Instead, we replace the long-term rate, as used in Weale and Wieladek (2016),with the term spread, i.e. the difference between long and short-term rates.
The main benefit of the identification proposed by Weale and Wieladek (2016)is the use of the cumulative announcement of purchases as a proxy to identify theeffects of QE, therefore allowing for the effects of QE announcements in a BVARmodel. Note that some of these variables may contain unit roots, but we includethem in levels, as done in Weale and Wieladek (2016).14 Given the large uncertaintyon the nature of a QE shock, we provide results with two identification strategiesrelying on zero and sign restrictions, inspired by Weale and Wieladek (2016) (Table1).15 The contemporaneous imposition of zero and sign restrictions is carried outthrough the algorithm developed in Arias et al. (2014). Compared to Weale andWieladek (2016), we identify also an exchange rate shock, that is usually found to bean important driver of the Swedish krona (see Corbo and Di Casola (2020)).
The first identification strategy relies on recursive ordering of the variables, wherethe Riksbank QE shock is assumed to affect the term spread and the exchange rate
14If one suspects that there are common trends among the variables (cointegration) but the natureof those trends is uncertain, Hamilton (1994) suggests to run the VAR in levels because the trendswould still be preserved, while running it in first difference would take away the trends.
15 Weale and Wieladek (2016) impose their restrictions for 5 months after the shock hits. Ourrestrictions are, therefore, less stringent.
12
|  | ECBpurchases | Prices GDP | Term | RER |
| --- | --- | --- | --- | --- |
|  |  | Identification I |  |  |
| ECB purchases | 1 | 0 | 0 | 0 |
| Prices |  | 1 | 0 | 0 |
| GDP |  | 1 | 0 | 0 |
| Riksbank purchases |  | 1 | 0 | 0 |
| Term spread |  |  | 1 | 0 |
| Stock prices |  |  |  | 1 |
|  |  | Identification II |  |  |
| ECB QE shockSupply shock | + | 0+ |  |  |
| Demand shock |  | 0+ |  | + |
| Exchange rate shock |  | + |  | + |

ECBpurchases
Prices GDP
Riksbank
purchases
Term
spread
RER
Identification I
ECB purchases
1
0
0
0
0
0
Prices
1
0
0
0
0
GDP
1
0
0
0
Riksbank purchases
1
0
0
Term spread
1
0
Stock prices
1
Identification II
ECB QE shockSupply shock
+
0+
Demand shock
Riksbank QE shock
0+
+
+
Exchange rate shock
+
+
Table 1: Identifying restrictions for the baseline model. The sign restrictions areimposed for five periods.
on impact, while it affects prices and GDP with a delay. Unlike Weale and Wieladek(2016), we assume that the Riksbank's asset purchases do not only respond on impactto GDP and prices, but also to the ECB's purchases.
The second identification strategy introduces sign restrictions. 16 The effect of theRiksbank QE shock on GDP and prices is always left unrestricted. The SwedishQE shock is assumed to decrease the term spread and depreciate the real exchangerate. The assumed effect on the term spread and exchange rate is in line with themechanism of the QE channels discussed before and also the results from studiesof effects of QE in the Swedish financial market (De Rezende, 2017). On the otherhand, the effects of the ECB shock are left unrestricted. Thanks to the exogeneityassumption, the ECB QE shock is the only shock that can affect all the Swedishvariables on impact and is a novelty with respect to Weale and Wieladek (2016).
16 This identification scheme is similar to identification scheme III in Weale and Wieladek (2016).We do not apply their second identification scheme because it relies on the presence of stock pricesin the system instead of the exchange rate. A version of identification scheme IV is provided inSection 7.4.
13
With this identification scheme, we can identify also domestic demand and supplyshocks, since the former generates positive comovement between prices and GDP andthe latter generates negative comovement. Both shocks are assumed to have no effecton the Riksbank's asset purchases on impact. This restriction is justified by the factthat it is usually difficult for monetary policy to respond to supply or demand shockswithin a month. Finally, the exchange rate shock is assumed to increase prices whenthe currency depreciates in real terms.
One key difference between the two identification schemes is that in Identification Ionly the ECB shock is allowed to affect prices and output on impact. In IdentificationII also the Riksbank QE shock can affect them on impact. A comparison of the resultscan inform us about whether this assumption affects the results and the relativeimportance of domestic versus foreign QE.
6 Results
In this section, we discuss the results from our baseline model, study the role ofthe response of domestic QE to foreign QE and focus on the transmission channelsat work. Due to the limited degrees of freedom, we replace the measure of theterm spread with, alternatively, measures of the corporate spread, mortgage spread,lending rates, inflation expectations, the financial conditions index, forward rates. Inaddition, we replace the GDP indicator with unemployment or households' consumerconfidence to understand how the QE shock transmits to the real economy.
6.1 Baseline model
Figure 2 reports the impulse response functions to the ECB and the Riksbank QEshock, using the two identification schemes presented above. Both the ECB and theRiksbank QE shocks are highly correlated across the two identification schemes (0.98
14
and 0.82, respectively). The signs and size of the median responses are very similaracross the identification schemes. However, the credible intervals are larger using signrestrictions, possibly due to the small data sample. Hence, the credible intervals forthe impulse responses of GDP and prices contain zero (Figure C.1 in Appendix C).
ECB assets
ECB QE shock
10-3 Riksbank QE shock
2
0.5
0
-2
10
20
30
40
0
10
-20
30
40
0.4
0.2
CPIF
0
0.2
-0.2
00
10
20
30
40
0
10
20
30
40
0.4
0.4
GDP
0.2
50.2
0
0
-0.2
0
10
20
30
40
0
10
20
30
40
Term spread Riksbank assets
0.1
0.05
0.5
0
0
0
10
20
30
40
0
10
20
30
40
0.04
0
0.02
-0.1-
0
-0.2
-0.3
0
10
20
30
40
0
10
20
30
40
0.5
2
RER
0
-0.5
0
10
20
30
40
0
10
20
30
40
Figure 2: Impulse response functions to the ECB QE shock and the Riksbank QEshock. We use the baseline Bayesian VAR model, Minnesota prior, 2 lags. Resultsrefer to Identification I (blue and black lines) and Identification II (red lines).Sample period is 2015:01-2018:12. We use 2000 simulations and 500 more forburn-in. Responses are in percentage terms. The blue and black solid linesrepresent the median responses of the ECB QE shock and the Riksbank QE shock,respectively. The dashed lines denotes a 68 per cent credible interval around themedian responses of Identification I.
The ECB shock has an expansionary effect on the Swedish economy, raising theGDP level and the price level. These results are in line with other studies on QE
15
spillovers, such as Chen et al. (2017). This happens despite the fact that the termspread rises and the krona appreciates on impact. 17 From studies on the euro areawe know that the ECB QE programme contributed to boost economic activity by,among other channels, lowering the long-term rate in the euro area (Garcia Pascualand Wieladek, 2016), hence through the portfolio balance channel. Here we find thatat the same time as lowering long-term rates in the euro area, the ECB QE increasedthe term spread in Sweden. The resulting appreciation of the Swedish krona, implyinga depreciation of the Euro, is in line with the exchange rate channel of the ECB QE.The additional value of our analysis is that we study the case of a small openeconomy running its QE programme at the same time as the ECB. In fact, theRiksbank responded to the ECB QE shock with its own QE programme, due tothe potential implications on the Swedish economy, as explained in Section 2. It ispossible that the positive contribution of the ECB QE to GDP and prices in Sweden,come also from the induced response of the small open economy's central bank. Infact, in the forecast error variance decomposition the ECB shock grows in importancefor GDP and the price level, while growing also in importance for the Riksbank QEprogramme. We will propose a way to disentangle the direct from the indirect effectof the ECB QE in the next section.
As regards the domestic QE shock, it increases the GDP level, and the size ofthe effect is larger with sign restrictions. The effect on the price level is very im-precisely estimated, since the credible intervals contain zero with both identificationschemes and the median value changes sign across identification schemes (the onlycase). As expected, the QE shock decreases the term spread and depreciates theSwedish krona. 18 These responses are in line with the portfolio balance and the ex-17In particular, in an extension of the model where we include both the long-term and the short-term rate, we observe that the effect on the spread comes mostly from an increase in the long-termrate.
18 From the extended model with both long-term and short-term rate, we know that the drop inthe term spread comes mostly from the drop in the long-term rate.
16
change rate channel of QE. One can also compare the spillovers of conventional andunconventional monetary policy. Corsetti et al. (2021) show that the ECB conven-tional monetary policy shocks generate a similar response of output and inflation inthe euro area as in its neighbouring countries. Therefore, our results for the ECB QEshocks are in line with evidence on spillovers of conventional monetary policy.
One should note also that the Riksbank QE shock is less persistent than theECB QE shock, hence part of the difference in effects may come from the expectedduration of the shock. Moreover, the responses of the price level and the exchangerate suggest a low exchange rate pass-through to consumer prices after the Riksbankand the ECB QE shocks. The fact that the pass-through may be low after a specificshock is not unusual for Swedish data. For example, Corbo and Di Casola (2020) findevidence of reverse-sign (negative) pass-through to consumers prices in Sweden afterdomestic and global demand shocks. This result implies that after specific shocks thepressure on prices stemming from demand may dominate the effect of exchange ratemovements on producers' costs.
Looking at the meta-analysis provided in Fabo et al. (2020), we can draw a com-parison of the effects of QE on GDP and prices across countries. The authors providestandardized effects, based on purchases equal to one percent of GDP, from 48 stud-ies published up to 2019 on US, UK and euro area data. Given the variability ofthe effects depending on the method used, we focus on the effects reported in VARmodels. In Table 2 we report this comparison for the standardized peak effect onGDP and total effect on inflation in VAR studies, along with the results from our twoidentification schemes. The results show that the effect of the ECB QE on SwedishGDP is comparable to the effect on the euro area GDP and larger for prices. This isnot surprising. Bluwstein and Canova (2016) and Chen et al. (2017) also find largespillovers of the ECB and Fed's QE conducted before 2015 on Swedish GDP, whereeffects are even larger than on the domestic economies. Our result may of course be
17
partly due to the endogenous response of the Riksbank to the ECB QE programme.
As for the domestic QE, the effects vary by identification scheme, being largerfor the one with sign restrictions. This is in line with results in Weale and Wieladek(2016), who attribute the larger effects to the stronger theoretical assumptions behindthe sign restrictions. The effect on GDP is on average equal to 0.29, hence betweenthe effects found in the US and the euro area. The effect on prices is never differentfrom zero in a probabilistic sense, and the average median effect (0.06) is comparableto the small effects found in UK and the euro area.
Another way to compare effects across countries would be to standardize themover the outstanding amount of assets. As mentioned before, in those terms thepurchases by the ECB were tree fourth of the ones by the Riksbank. If one uses thisform of normalization, the effects of the Riksbank QE on Sweden look smaller thanthe effects of the ECB QE in the euro area even in terms of GDP (roughly one fifthof those in the euro area).
| Country | Peak effect on GDP | Total effect on inflation |
| --- | --- | --- |
|  |  | Baseline model Identification I / II |
| ECB SwedenRiksbank → Sweden | $0.21^{*}/0.25$ | $0.22^{*}/0.23$ |
|  | VAR models in the | literature (Fabo et al., 2020) |
| USA | 0.32 | 0.24 |
| UK | 0.14 | 0.05 |
| Euro area | 0.26 | 0.08 |

Country
Peak effect on GDP
Total effect on inflation
Baseline model Identification I / II
ECB SwedenRiksbank → Sweden
$0.21^{*}/0.25$
$0.16^{*}/0.41$
$0.22^{*}/0.23$
$-0.06/0.17$
VAR models in the
literature (Fabo et al., 2020)
USA
0.32
0.24
UK
0.14
0.05
Euro area
0.26
0.08
Table 2: Standardized effects
Results for Sweden come from baseline model with Identification I and II, standardizedto one percent of GDP of the correspective economy. * refers only to results for Swedenand indicates that at the time of the effect the 68 per cent credible intervals are excludingzero. Data for UK, USA and euro area from Fabo et al. (2020), average values from 48studies. Effects in percentage terms.
Given the large uncertainty surrounding the responses with sign restrictions, weproceed our analysis relying on Identification scheme I, that is also more conservativein terms of size of effects.
18
6.2
Digging deeper into the effects of domestic and foreign
QE
In order to understand the transmission of the shock to domestic demand and house-holds, we consider a variation of the baseline model with additional variables. Figure3 shows the response of market-based inflation expectations, households' confidenceand unemployment to QE shocks, normalized to one percent purchases over GDP. Wecan notice that only the ECB QE shock increases inflation expectations and house-holds' confidence in Sweden and this may explain the large positive effect on prices.In terms of labor market, unemployment drops after the Riksbank QE shock, whileit increases temporarily after the ECB QE shock.
6.3 Direct and indirect effects of foreign QE
In order to disentangle the direct from the indirect effect of the ECB QE on Swedenwe need to evaluate the role of the Riksbank's response to the ECB QE programme.For this purpose, we conduct a conditional forecast exercise. This type of exerciseis also used in other studies of QE, such as Lenza et al. (2010) for the euro area,to evaluate the effects of QE. We follow these steps, each with specific assumptionsabout domestic and foreign QE:
1. We assume that neither the ECB, nor the Riksbank conducted their QE pro-gramme.
2. We assume that only the ECB conducted its QE programme.
3. We first assume that the ECB did not conduct its QE programme and filter
out the exogenous component of the Riksbank QE. In a second step, we assume
that the ECB conducted its QE programme and the Riksbank did not respondto it, but only executed the exogenous component of its QE.
19
Unemployment
Inflation expectations
Households Confidence
ECB QE shock
Riksbank QE shock
0.04
0.04
0.02
0.02
0
-0.02
-0.02
0
10
20
30
40
0
10
20
30
40
0.5
0.5
0
-0.5
-0.5
-1
-1
-1.50
-1.5
10
20
30
40
10
20
30
40
0.05
-0.05
0.05
-0.05
0
0
10
20
30
40
0
10
20
30
40
Figure 3: Impulse response functions to the ECB QE shock and the Riksbank QEshock, normalized to one percent of purchases over GDP. We use the baselineBayesian VAR model, Minnesota prior, 2 lags, where households' confidence orinflation expectations replace the term spread or unemployment replaces GDP.Results refer to Identification I. Sample period is 2015:01-2018:12. We use 2000simulations and 500 more for burn-in. Responses are in percentage terms. The blueand black solid lines represent the median responses of the ECB QE shock and theRiksbank QE shock, respectively. The dashed lines denotes a 68 per cent credible
interval.
Results are reported in Figure 4. Comparing the outcome to the case of ECBQE and only exogenous QE from the Riksbank (case 3), we can identify the indirecteffects of the ECB QE on Sweden. The endogenous QE response from the Riksbankaffected positively the GDP level and weakened the currency in real terms, whileresults for the term spread are mixed. The impact on prices is positive but small.The direct impact of the ECB QE can be gauged by comparing the case without QE(case 1) to the case with only ECB QE (case 2). The effect is very large for pricesand GDP, while the real exchange rate is first appreciated and then depreciated.
20
102
101,5
101
100,5
-outcome-only ECB QE
-no OE at all
-ECB OF
exog Riksbank QE
CPIF
99,52015m3
2015m9
2016m3
2016m9
2017m3
2017m9
2018m3
2018m9
-outcome
-only ECB QE
-ECB QE and exog Riksbank QE
Term spread
0,4
2015 m3 2015m9 2016m3 2016m9 2017m3 2017m9 2018m3 2018m9
-outcome
-only ECB QE
102,5
all
102
-ECB QE and exog Riksbank QE
101,5
100,5
GDP
992015m3
2015m9
2016m3
2016m9
2017m3 2017m9 2018m3 2018m9
103
outcome
-only ECB QEQE at all
102
-ECB QE and exog Riksbank QE
RER
2015m3
2015m9
2016m3 2016m9
2017m3
2017m9
2018m3
2018m9
Figure 4: Conditional forecasts of CPIF, GDP, term spread and real exchange ratefor outcomes (blue), the case of no QE (green), only ECB QE (red), ECB QE andexogenous Riksbank QE (violet). The level of CPIF, GDP and real exchange rate isnormalized to 100 in 2015:03.
Overall, taking together the conditional forecast exercise with the impulse re-sponses analysis we conclude that the endogenous response of the Riksbank didstrengthen the effect of the ECB QE on GDP and reduced the appreciation of theSwedish currency.
6.3.1 Role of the open economy
In the previous sections we have discussed the important role of foreign QE andthe exchange rate for the Swedish economy. As an additional confirmation of theirimportance, we now estimate the model omitting the ECB or omitting both theECB and the exchange rate (replaced with stock prices). In this way, our model
21
specification is the same as in Weale and Wieladek (2016) and it is likely that theeffects of foreign QE will be mixed with the effects of domestic QE. Indeed, we finda larger effect, even double in some specifications, of Swedish QE on GDP. Theeffect on prices is also larger and always positive, although the credible intervals stillcontain zero. We conclude that we need to account for the ECB QE in order not tooverestimate the effect of the Riksbank QE on the Swedish economy. On the otherhand, our experiment highlights that the exchange rate channel of QE does not seemcrucial for the effects on output and inflation.
Table 3: Role of the open economy
| Model | Peak effect on GDP | Total effect on inflation |
| --- | --- | --- |
|  | Identification I / II |  |
| model without RER& ECB | $0.37^{*}/0.57^{*}$ | 0.10/0.34 |
| model without ECB | $0.36^{*}/0.62^{*}$ | 0.10/0.40 |
| Baseline | $0.16^{*}/0.41^{*}$ | -0.06/0.17 |

Model
Peak effect on GDP
Total effect on inflation
Identification I / II
model without RER& ECB
$0.37^{*}/0.57^{*}$
0.10/0.34
model without ECB
$0.36^{*}/0.62^{*}$
0.10/0.40
Baseline
$0.16^{*}/0.41^{*}$
-0.06/0.17
Values come from baseline model with Identification I and II, standardized to one percentof GDP. * indicates that at the time of the effect the 68 per cent credible intervals areexcluding zero.
6.4 Exploring the channels of QE
The baseline model with and without exchange rate has provided evidence on theexchange rate channel of QE and its role for the macroeconomic effects. More analysisis required to delve deeper into the functioning of the portfolio balance and thesignalling channels. The next two subsections serve this purpose.
6.4.1 Signalling channel
In order to analyse the signalling channel of QE we need to analyse its effects onthe RIBA interest rate expectations. Therefore, we replace the term spread in thebaseline model with a measure of interest rate expectations six months, 2 years or 5years ahead. Results are reported in Figure 5. Interest rate expectations in the short
22
and the medium term drop after the Riksbank QE shock, while they slightly increaseor do not move in connection with the ECB shock. Combining these results with thebaseline model's results, we conclude that the signalling channel was at work afterthe Riksbank QE shock, but had stronger effects on the real economy than on prices.
5-year RIBA
2-year RIBA
6-month RIBA
0.02
0
-0.02
0.05
-0.05
ECB QE shock
0.02
0
-0.02
Riksbank QE shock
0
10
20
30
40
0
10
20
30
40
0.05
-0.05
0
0
10
20
30
40
0
10
20
30
40
0.05
0
0.05
0
-0.05
-0.05
-0.1
-0.1
-0.15
-0.15
0
10
20
30
40
0
10
20
30
40
Figure 5: Impulse response functions to the ECB QE shock and the Riksbank QEshock, normalized to one percent of purchases over GDP. We use the baselineBayesian VAR model, Minnesota prior, 2 lags, where the the 6-month, 2-year and5-year ahead interest rate expectations from RIBA contracts replace the termspread. Results refer to Identification I. Sample period is 2015:01-2018:12. We use2000 simulations and 500 more for burn-in. Responses are in percentage terms. Theblue and black solid lines represent the median responses of the ECB QE shock andthe Riksbank QE shock, respectively. The dashed lines denotes a 68 per centcredible interval.
23
6.4.2 Portfolio balance channel
We study more in details the transmission of QE through the financial sector. Fromthe baseline model we know that the Riksbank QE has a negative impact on theterm spread, through a negative impact on the long-term rate. Instead, the ECB QEhas a positive impact on the term spread and the long-term rate. This is evidenceof the portfolio balance channel, to analyse its effects on risk premia and financingconditions overall. We replace the term spread with various measures: corporatespread, mortgage spread, equity prices, housing prices, Financial Conditions Index(FCI), the component of the FCI related to housing prices and households' lendingrates.
Before discussing the results it is useful to note some distinctive features of theSwedish financial market, discussed in Gustafsson and von Brömsen (2021). Swedishbanks are funded using deposits but also largely through financial markets. In partic-ular, their short-term funding largely consists of borrowing in US dollars and euros.Moreover, mortgages represent a large share of the major Swedish banks' assets andabout 70 percent of them are funded through covered bonds. As for firms' financ-ing, most Swedish companies rely on bank loans, but many companies, especially thelarger ones, issue corporate bonds in foreign currency. For these reasons, corporateand mortgage spreads are important indicators of financing conditions for firms, butalso foreign market conditions are extremely important for Swedish banks and firms.In Figure 6 we can see that both the ECB and the Riksbank QE shocks improvefinancing conditions in Sweden (i.e. the FCI index increases), but the size and thereason for the improvements differ. The effect of the ECB QE shock on the FCI issmaller and transmitted through an improvement of financing conditions for financialand non-financial firms, that fund themselves in the market through corporate bondsand covered bonds backed by mortgages. The ECB QE effect on equity prices is small,while it is slightly negative for housing prices. On the other hand, the effect of the
24
Riksbank QE shock on the FCI is large and transmits mostly through equity prices,housing prices and households' lending rates. The Riksbank QE slightly increasescorporate and mortgage spreads.
Overall, we can conclude that the positive effect of the ECB QE on output andprices in Sweden was transmitted primarily through firms' financing conditions anddomestic demand. This points towards a portfolio balance channel at work afterthe ECB QE, through the effect on risk premia. The effects of the Riksbank QEwere transmitted primarily through the term premium and households' financingconditions. On a similar note, Kaat et al. (2021) propose a housing portfolio channelof QE, where intermediaries rebalance their portfolios from bonds to housing. Byusing German regional-level data, they find evidence of such channel for the ECBQE.
7 Robustness
In this section we discuss various robustness analyses we have carried out for ourbaseline model with Identification I.
7.1
Alternative measure of purchases
One of the advantages of Weale and Wieladek (2016) is to use announced asset pur-chases as proxy for QE, in order to account also for announcement effects. It is worthverifying whether our results change substantially if we instead use the effective pur-chases by the ECB and the Riksbank. The best proxy available for the effectivepurchases is the measure of asset holdings in the balance sheets of the ECB and theRiksbank, that we divide, as before, by the annualized nominal GDP of quarter 4 of2014 (Figure C.3 in Appendix C).
The direction of the effects and the size of the credible intervals are similar (see
25
0.06
0.04
0.02
ECB QE shock
Riksbank QE shock
0.06
0.04
0.02
0
0
-0.02-0.04
-0.02-0.04
0
10
20
30
40
0
10
20
30
40
0.02
0.02
0
0
-0.02
-0.02
0
10
20
30
40
0
10
20
30
40
Housing prices
Mortgage spread Corporate
spread
Equity prices
Household lending rate
32101
32101
0
10
20
30
40
0
10
20
30
40
0.05
0.05
0
0
-0.05
-0.05
-0.1
-0.1
0
10
20
30
40
0
10
20
30
40
0.2
0.2
0.1
0.1
0
0
0
10
20
30
40
0
10
20
30
40
0.01
0.01
0
0
-0.01
-0.01
0
10
20
30
40
0
10
20
30
40
Figure 6: Impulse response functions to the ECB QE shock and the Riksbank QEshock, normalized to one percent of purchases over GDP. We use the baselineBayesian VAR model, Minnesota prior, 2 lags, where the financial variable replacesthe term spread. Results refer to Identification I. Sample period is 2015:01-2018:12.We use 2000 simulations and 500 more for burn-in. Responses are in percentageterms. The blue and black solid lines represent the median responses of the ECBQE shock and the Riksbank QE shock, respectively. The dashed lines denotes a 68
per cent credible interval.
Table D.1 in Appendix D). The effects are slightly larger, possibly because balancesheet holdings have a different timing than the announcements and may account
26
differently for their expectations.
7.2 Other proxies for QE
As discussed before, the portfolio channel of the Riksbank QE seems to have workedthrough a drop in the long-term rate, while the ECB QE reduced risk premia. Herewe carry out a robustness exercise to verify this finding. By replacing the measuresof announced amounts for both the ECB and the Riksbank with the long-term rate,we can understand the importance of the term premium channel of QE, along thelines of the exercise carried out in Weale and Wieladek (2016). 19 The long-termrate in Sweden follows a similar pattern as the euro area long-term rate after theECB shock. However, after a one percent drop in the euro area long-term rate, weobserve an initial drop and then an increase in GDP, while the effect on prices is veryimprecisely estimated and the Swedish krona depreciates (Figure C.4 in AppendixC). These results are different from those found in the baseline model in Figure2, suggesting that the ECB QE did not transmit mostly through the effect on thelong-term rate.
Regarding the domestic QE, we observe a depreciation of the Swedish krona and anincrease in GDP after few months, as in the baseline model. The effects on inflationare still imprecisely estimated, but the median response is positive. These resultsconfirm that the Riksbank QE did transmit through the effect on the long-term rate.that the evidence suggests that the risk premium channel was more important thenthe portfolio balance channel for the spillover effects of the ECB QE in Sweden.19In order to avoid collinearity, we also replace the term spread with the short-term rate, thatcontrols for the conventional monetary policy conducted by the Riksbank.
27
7.3 Omitted variables and extended sample
The size of our model is limited by the short sample period available. However, wehave run some robustness exercises including a seventh variable. For instance, the Fedfunds rate has been added to make sure we are not confounding our shocks with theUS monetary policy shock. We have also included the euro area price level in orderto account for the possible comovement with the Swedish price level. Finally, real oilprices have been added to account for international energy price developments. In allcases, the variables have been added first in the VAR systems and are subject to theblock-exogeneity assumption. We have also extended the sample period to include allof 2019, a period without new purchases but only reinvestments, or to include all of2014, before the measure were announced. The main results are confirmed in terms ofdirection of effects and size of credible intervals and the shocks are highly correlated(above 0.9) across the specifications (Table D.1 in Appendix D). The extension ofthe sample makes the effects of ECB QE on Swedish inflation look negligible, due tothe inclusion of periods without asset purchases, as explained in Weale and Wieladek(2016).
7.4 Alternative identification
Weale and Wieladek (2016) provide an identification scheme for the QE shock basedon the assumption that it is the shock explaining the largest fraction of the fore-cast error variance of asset purchases from impact until a long-enough horizon. Themethodology, known as "max-FEV" approach, is based on Uhlig (2003) and Francis etal. (2014). This identification strategy is not suitable in our case, because we studya small open economy. The asset purchases decided by the Riksbank were partlyalso a response to the contemporaneous QE carried out by the ECB and its poten-tial repercussion in Sweden, as discussed in section 2 and confirmed by our analysis.Hence, there are at least two QE shocks, not just one, that can explain the forecast28
error variance of the Riksbank asset purchases. What we can do, however, is to applya "max-FEV" strategy to identify the ECB QE shock. We run a BVAR model asin baseline case, but do not assume that the ECB variable is exogenous to Sweden.We then identify the ECB QE shock as the shock that maximizes the forecast errorvariance of the ECB announced purchases at horizon 40 (the results hold if we slightlyvary the number of the horizon).
The ECB QE shock we obtain has a correlation equal to 0.88 with the shock fromthe baseline model, using either of the identification schemes. Impulse responses,shown in Figure C.2 in Appendix C, are comparable with Figure 2. The shock haspositive effects on GDP and prices and induces the Riksbank to announce purchases.In terms of standardized effects, the peak effect on the Swedish GDP is 0.28, comparedto 0.21 (0.25) with Identification I (II). The total effect on inflation in standardizedterms is 0.16, compared to 0.22 (0.23) with Identification I (II). The only difference isthat the response of the Swedish krona is roughly null in the first months, while it isstrengthening in the baseline model with Identification I. Overall, we conclude thatthe identification of the ECB QE shock is robust to different identification strategies.
8 Conclusion
Unconventional monetary policy has come back to the forefront of the internationalpolicy agenda due to the Covid-19 pandemic. This has forced many central banksaround the world to intervene to help the functioning of the financial markets withlarge-scale asset purchases. It is difficult to evaluate the effects of large-scale assetpurchases on the macroeconomy, possibly due to the short sample availability. Thereis even larger uncertainty on the effects of asset purchases in small open economies,such as Sweden, which may be subject to spillovers from contemporaneous QE con-ducted abroad.
29
Our contribution to the literature is to study the effects of domestic and foreignQE in a small open economy, namely Sweden, taking into account the endogenousresponse to foreign QE. The period of the analysis is 2015-2018, when both theRiksbank and the ECB conducted QE programmes to make monetary policy moreexpansionary. We have used a structural Bayesian VAR at monthly frequency, withidentification strategies inspired by Weale and Wieladek (2016) and we have identifiedboth domestic and foreign QE shocks.
We have found positive effects of the Swedish QE on Swedish GDP, with a decreasein unemployment, and a weakening currency in real terms. The effects come throughthe improved lending conditions for households and lowered expected future rates.The effects on Swedish inflation are less clear. The ECB QE programme had largepositive spillover effects on both GDP and inflation in Sweden and generated an initialappreciation of the krona real exchange rate. These spillovers are partly explainedby the response of domestic QE to foreign QE, in expectation of its repercussions onthe Swedish economy. The ECB QE transmitted to the economy through improvedfinancing conditions for firms.
The main contribution of our paper to the current policy debate is the importanceof evaluating the role of spillovers of foreign unconventional monetary policy for smallopen economies and the response of the central banks of those economies with theirdomestic unconventional monetary policy. This is particularly relevant in the currentsituation, when the Covid-19 pandemic has hit all over the world and central bankshave reacted with more expansionary monetary policy.
However, some caveats apply when comparing our estimates to the current sit-uation. Our analysis refers to asset purchases conducted with the aim of makingmonetary policy more expansionary (QE according to Bernanke (2009)), but notto improve the functioning of financial markets during a period of financial distress(credit easing, according to Bernanke (2009)). The current wave of unconventional
30
monetary policy has been initially aimed at alleviating financial market distress. Asargued by Bailey et al. (2020), in periods of financial market distress, large asset pur-chases programmes implemented quickly may be even more effective than in normaltimes.
31
References
Alpanda, Sami and Serdar Kabaca, "International Spillovers of Large-Scale AssetPurchases," Journal of the European Economic Association, 2020, 18 (1), 342-391.
Alsterlind, Jan, Magnus Lindskog, and Tommy von Brömsen, "An index forfinancial conditions in Sweden," Staff Memo, Sveriges Riksbank 2020.
Arias, Jonas E., Juan F. Rubio-Ramirez, and Daniel F. Waggoner, "In-ference Based on SVARs Identified with Sign and Zero Restrictions: Theory andApplications," International Finance Discussion Papers 1100, Board of Governorsof the Federal Reserve System (U.S.) April 2014.
Bailey, Andrew, Jonathan Bridges, Richard Harrison, Josh Jones, andAakash Mankodi, "The central bank balance sheet as a policy tool: past, presentand future," Bank of England working papers 899, Bank of England December 2020.
Baumeister, Christiane and Luca Benati, "Unconventional Monetary Policy andthe Great Recession: Estimating the Macroeconomic Effects of a Spread Compres-sion at the Zero Lower Bound," International Journal of Central Banking, June2013, 9 (2), 165-212.
Bernanke, Ben S., "The crisis and the policy response: a speech at the Stamp Lec-ture, London School of Economics, London, England, January 13, 2009," TechnicalReport 2009.
,
"The New Tools of Monetary Policy," American Economic Review, April 2020,
110 (4), 943-983.
Bhattarai, Saroj and Christopher J. Neely, "An Analysis of the Literature on
International Unconventional Monetary Policy," Journal of Economic Literature,Forthcoming.
32
BIS, Unconventional monetary policy tools: a cross-country analysis number 63. In'CGFS Papers.', BIS, Autumn 2019.
Blix Grimaldi, Marianna, Alberto Crosta, and Dong Zhang, "The Liquidityof the Government Bond Market - What Impact Does Quantitative Easing Have?Evidence from Sweden," Mimeo 2020.
Bluwstein, Kristina and Fabio Canova, "Beggar-Thy-Neighbor? The Interna-tional Effects of ECB Unconventional Monetary Policy Measures," InternationalJournal of Central Banking, September 2016, 12 (3), 69-120.
Boeckx, Jef, Maarten Dossche, and Gert Peersman, "Effectiveness and trans-mission of the ECB's balance sheet policies," International Journal of central bank-ing, 2017, 13 (1), 297-333.
Borio, Claudio and Anna Zabai, "Unconventional monetary policies: a re-appraisal," BIS Working Papers 570, Bank for International Settlements July 2016.
Carlstrom, Charles T, Timothy S Fuerst, and Matthias Paustian, "Target-ing long rates in a model with segmented markets," American Economic Journal:Macroeconomics, 2017, 9 (1), 205-42.
Chen, Han, Vasco Cúrdia, and Andrea Ferrero, "The macroeconomic effectsof large-scale asset purchase programmes," The economic journal, 2012, 122 (564),F289-F315.
Chen, Qianying, Marco Lombardi, Alex Ross, and Feng Zhu, "Global impactof US and euro area unconventional monetary policies: a comparison," BIS WorkingPapers 610, Bank for International Settlements January 2017.
33
Corbo, Vesna and Ingvar Strid, "MAJA: A two-region DSGE model for Swe-den and its main trading partners," Working Paper Series 391, Sveriges Riksbank(Central Bank of Sweden) July 2020.
and Paola Di Casola, "Drivers of consumer prices and exchange rates in smallopen economies," Working Paper Series 387, Sveriges Riksbank (Central Bank ofSweden) March 2020.
Corsetti, Giancarlo, Keith Kuester, Gernot Müller, and SebastianSchmidt, "The Exchange Rate Insulation Puzzle," Discussion Papers 15689,C.E.P.R. January 2021.
Dahlhaus, Tatjana, Kristina Hess, and Abeer Reza, "International Trans-mission Channels of US Quantitative Easing: Evidence from Canada," Journal ofMoney, Credit and Banking, 2018, 50 (2-3), 545-563.
de los Rios, Antonio Diez and Maral Shamloo, "Quantitative easing and long-term yields in small open economies," Working Paper, International Monetary Fund2017.
De Rezende, Rafael B., "The interest rate effects of government bond purchasesaway from the lower bound," Journal of International Money and Finance, 2017,74 (C), 165-186.
and Annukka Ristiniemi, "A shadow rate without a lower bound constraint,"Bank of England working papers 864, Bank of England May 2020.
Dell'Ariccia, Giovanni, Pau Rabanal, and Damiano Sandri, "UnconventionalMonetary Policies in the Euro Area, Japan, and the United Kingdom," Journal ofEconomic Perspectives, 2018, 32 (4), 147-172.
34
Di Casola, Paola, "What does research say about the effects of central bank assetpurchases?," Economic Commentary, Sveriges Riksbank February 2021.
Fabo, Brian, Martina Jančoková, Elisabeth Kempf, and Luboš Pástor,"Fifty Shades of QE: Conflicts of Interest in Economic Research," NBER WorkingPapers 27849, National Bureau of Economic Research, Inc September 2020.
Francis, Neville, Michael T. Owyang, Jennifer E. Roush, and RiccardoDiCecio, "A Flexible Finite-Horizon Alternative to Long-Run Restrictions withan Application to Technology Shocks," The Review of Economics and Statistics,October 2014, 96 (4), 638-647.
Gambacorta, Leonardo, Boris Hofmann, and Gert Peersman, "The effective-ness of unconventional monetary policy at the zero lower bound: A cross-countryanalysis," Journal of Money, Credit and Banking, 2014, 46 (4), 615-642.
Gambetti, Luca and Alberto Musso, "The macroeconomic impact of the ECB'sexpanded asset purchase programme (APP)," Working Paper Series 2075, Euro-pean Central Bank June 2017.
Garcia Pascual, Antonio and Tomasz Wieladek, "The European Central Bank'sQE: A new hope," CEPR Discussion Papers 11309, CEPR Discussion Papers June2016.
Gertler, Mark and Peter Karadi, "QE 1 vs. 2 vs. 3...: A Framework for AnalyzingLarge-Scale Asset Purchases as a Monetary Policy Tool," International Journal ofCentral Banking, 2013, 9 (1), 5-53.
Gilchrist, Simon, David López-Salido, and Egon Zakrajšek, "Monetary policyand real borrowing costs at the zero lower bound," American Economic Journal:Macroeconomics, 2015, 7 (1), 77-109.
35
Greenwood, Robin, Samuel G. Hanson, Jeremy C. Stein, and Adi Sun-deram, "A Quantity-Driven Theory of Term Premia and Exchange Rates," NBERWorking Papers 27615, National Bureau of Economic Research, Inc July 2020.
Gustafsson, Peter and Tommy von Brömsen, "Coronavirus pandemic: TheRiksbank's measures and financial developments during spring and summer 2020,"Economic Review 2021:1, Sveriges Riksbank 2021.
Haldane, Andrew, Matt Roberts-Sklar, Tomasz Wieladek, and ChrisYoung, "QE: The Story so far," Bank of England working papers 624, Bank ofEngland October 2016.
Hamilton, James D., Time Series Analysis, Princeton University Press, 1994.
Johnson, Grahame, Sharon Kozicki, Romanos Priftis, Lena Suchanek,Jonathan Witmer, and Jing Yang, "Implementation and Effectiveness of Ex-tended Monetary Policy Tools: Lessons from the Literature," Discussion Papers2020-16, Bank of Canada December 2020.
Knezevic, David, Martin Nordström, and Pär Österholm, "The relation be-tween municipal and government bond yields in an era of unconventional monetarypolicy," Economic Notes, forthcoming.
Kolasa, Marcin and Grzegorz Wesolowski, "International spillovers of quanti-tative easing," Journal of International Economics, 2020, 126.
Kuttner, Kenneth N., "Outside the Box: Unconventional Monetary Policy in theGreat Recession and Beyond," Journal of Economic Perspectives, November 2018,32 (4), 121-46.
Lenza, Michele, Huw Pill, and Lucrezia Reichlin, "Monetary policy in excep-tional times," Economic Policy, 2010, 25 (62), 295-339.
36
MacDonald, Margaux and Michal Ksawery Popiel, "Unconventional MonetaryPolicy in a Small Open Economy," IMF Working Papers $17/268$, InternationalMonetary Fund December 2017.
Melander, Ola, "Effects on financial markets of the Riksbank's government bondpurchases 2015-2017," Economic Review 2021:1, Sveriges Riksbank 2021.
Mouabbi, Sarah and Jean-Guillaume Sahuc, "Evaluating the macroeconomiceffects of the ECB's unconventional monetary policies," Journal of Money, Creditand Banking, 2019, 51 (4), 831-858.
Panizza, Ugo and Charles Wyplosz, "The Folk Theorem of Decreasing Effec-tiveness of Monetary Policy: What Do the Data Say?," Russian Journal of Moneyand Finance, March 2018, 77 (1), 71-107.
Rossi, Barbara, "Identifying and estimating the effects of unconventional monetarypolicy: How to do it and what have we learned?," The Econometrics Journal, 072020.
Sims, Eric and Jing Cynthia Wu, "Evaluating central banks' tool kit: Past,present, and future," Journal of Monetary Economics, 2020.
te Kaat, Daniel Marcel, Chang Ma, and Alessandro Rebucci, "Real Effectsof the ECB's Quantitative Easing: A Housing Portfolio Channel," Mimeo 2021.
Uhlig, Harald, "What moves GNP?," Mimeo, Mimeo 2003.
Vayanos, Dimitri and Jean-Luc Vila, "A Preferred-Habitat Model of the TermStructure of Interest Rates," Econometrica, 2021, 89 (1), 77-112.
Walentin, Karl, "Business cycle implications of mortgage spreads," Journal of Mon-etary Economics, 2014, 67 (C), 62-77.
37
Wallace, Neil, "A Modigliani-Miller theorem for open-market operations," TheAmerican Economic Review, 1981, 71 (3), 267-274.
Weale, Martin and Tomasz Wieladek, "What are the macroeconomic effects ofasset purchases?," Journal of Monetary Economics, 2016, 79 (C), 81-93.
Wu, Jing Cynthia and Fan Dora Xia, "Measuring the Macroeconomic Impact ofMonetary Policy at the Zero Lower Bound," Journal of Money, Credit and Banking,March 2016, 48 (2-3), 253-291.
38
A Data
Table A.1: Data description
| Series | Transformation | Source |
| --- | --- | --- |
| Activity monthly indicator | log | Statistics Sweden |
| Unemployment |  | Statistics Sweden |
| CPIF price level | log | Statistics Sweden |
| Household's confidence |  | Statistics Sweden |
| 10y yield on Swedish government debt |  | Macrobond |
| OMX all share index | log | Macrobond |
| Break-even 5y ahead inflation |  | Macrobond |
| 5y corporate bond spread |  | Sveriges Riksbank |
| 5y mortgage bond spread |  | Sveriges Riksbank |
| Households' lending rate |  | Sveriges Riksbank |
| Financial Conditions Index, |  | Sveriges Riksbank |
| 6m, 2y, 5y RIBA forward rates, |  | Sveriges Riksbank |
| Nominal effective krona exchange rate | log | Sveriges Riksbank |
| 10y yield on German government debt |  | Macrobond |
| Euro area price level | log | Fred database |
| Fed funds rate |  | Fred database |
| ECB balance sheet, assets |  | Macrobond |
| Riksbank balance sheet, assets |  | Sveriges Riksbank |

Series
Transformation
Source
Activity monthly indicator
log
Statistics Sweden
Unemployment
Statistics Sweden
CPIF price level
log
Statistics Sweden
Household's confidence
Statistics Sweden
10y yield on Swedish government debt
Macrobond
OMX all share index
log
Macrobond
Break-even 5y ahead inflation
Macrobond
5y corporate bond spread
Sveriges Riksbank
5y mortgage bond spread
Sveriges Riksbank
Households' lending rate
Sveriges Riksbank
Financial Conditions Index,
Sveriges Riksbank
6m, 2y, 5y RIBA forward rates,
Sveriges Riksbank
Nominal effective krona exchange rate
log
Sveriges Riksbank
10y yield on German government debt
Macrobond
Euro area price level
log
Fred database
Fed funds rate
Fred database
ECB balance sheet, assets
Macrobond
Riksbank balance sheet, assets
Sveriges Riksbank
39
Table A.2: Riksbank's announcements
| Date | Purchase announcements |
| --- | --- |
| February 2015 | 10 billions Sek |
| March 2015 | 30 billions Sek |
| April 2015 | 40-50 billions Sek |
| July 2015 | 45 billions Sek |
| October 2015 | 65 billions Sek |
| April 2016 | 45 billions Sek |
| December 2016 | 30 billions Sek |
| April 2017 | 15 billions Sek |

Date
Purchase announcements
February 2015
10 billions Sek
March 2015
30 billions Sek
April 2015
40-50 billions Sek
July 2015
45 billions Sek
October 2015
65 billions Sek
April 2016
45 billions Sek
December 2016
30 billions Sek
April 2017
15 billions Sek
| Date | Purchase announcements |
| --- | --- |
| January 2015 | 60 billions Eur per month from March 2015 until end of September 2016, tot. new=1140 $(60^{*}19m)$extension to end of March 2017, tot. new $=360$ $(60^{*}6m)$ |
| October 2017 | 30 billions Eur from January to September 2018, tot. $new=27C$ ( $(30^{*}9m)$ |
| June 2018 | 15 billions Eur from October to end of December 2018, tot. $new=45$ (15*3m) |

Date
Purchase announcements
January 2015
December 2015
March 2016December 2016
60 billions Eur per month from March 2015 until end of September 2016, tot. new=1140 $(60^{*}19m)$extension to end of March 2017, tot. new $=360$ $(60^{*}6m)$
80 billions Eur from April 2016 until end of March 2017, tot. new=240 $(20^{*}12)$
60 billions Eur per month from April 2017 to end of December 2017, tot. new=540 $(60^{*}9m)$
October 2017
30 billions Eur from January to September 2018, tot. $new=27C$ ( $(30^{*}9m)$
June 2018
15 billions Eur from October to end of December 2018, tot. $new=45$ (15*3m)
Table A.3: ECB's announcements
40
EA QE
CPIF
28
220
24
216
212
20
16
12
8
120
116
112
108
104
IIVIII IV
1.6
1.4
1.2
1.0
0.8
W
0.6
2015
2016
GDP
2017
2018
2015
2016
VIVIII IV2018
2017
Term spread
208
204
200
3
2
1
144
140
136
132
128
TIVI IV20152018
2016
2017
RB QE
IIVIII IV20172018
2015
2016
RER
124
VIVIVIV
VIVIVIV
2015
2016
2017
2018
2015
2016
2017
2018
Figure A.1: Data used in the baseline model.
41
BBVAR model
In this memo we use the Bayesian VAR model written in the following way:
$G(L)x_{t}=\eta_{t}$
(B.1)
where $G(L)=G_{1}L+G_{2}L^{2}+...+G_{m}L^{m}$, is a lag polynomial of order m. The laglength of the model is in all cases set to 2. $X_{t}$ is an nxl vector of variables and $\eta_{t}$is an nx1 vector of iid error terms fulfilling $E(\eta_{t})=0$ and $E(\eta_{t}\eta_{t}^{\prime})=\Sigma$. The priorsof the model largely follow convention in the literature. For the prior is given by$p(\Sigma)\propto|\Sigma^{-(n+1)/2}|$ and the prior on $vec(G)$ is given by $vec(G)\sim N_{mn}(\Theta_{G},\Omega_{G})$The priors on the dynamics have been modified, relative to the traditional Minnesotaprior. The prior mean on the first own lag for each variable is here set equal to 0.9and all other coefficients in G have a prior mean of zero. The hyperparameters of themodel are also in line with mainstream choices in the literature. We set the overalltightness to 0.2, the cross-variable tightness to 0.5 and the lag decay parameter to 1.Since Sweden is a small open economy, we need to assume that Swedish shocks donot affect the foreign economy. The block exogeneity parameter is set equal to 0.001so that the ECB variable is not affected by Swedish variables.
42
C Additional figures
CPIF
ECB QE shock, Id II
Riksbank QE shock, Id II
ECB assets
2
2
0
-2
10
20
30
40
0
10
20
30
40
0.6
0.4
4202
0.5
-0.5
-0.2
0
10
20
30
40
0
10
20
30
40
11
2
GDP
0
Term spread Riksbank assets6
우
T
4202
10
20
30
40
10
20
30
40
0
10
20
30
40
0
10
20
30
40
0.2
0
0.1
-0.2
-0.4
0.1
0
10
20
30
40
0
10
20
30
40
RER
12
10
20
30
40
0
10
20
30
40
Figure C.1: Impulse response functions to the ECB QE shock and the Riksbank QEshock. We use the baseline Bayesian VAR model, Minnesota prior, 2 lags. Resultsrefer to Identification II. Sample period is 2015:01-2018:12. We use 2000 simulationsand 500 more for burn-in. Responses are in percentage terms. The blue and black
solid lines represent the median responses of the ECB QE shock and the RiksbankQE shock, respectively. The dashed lines denotes a 68 per cent credible interval.
43
percent
percent
0.04
0.02
0
percent
$EA_{a}$
RB ssetsa
0.
-0.
5 10 15 20 25 30 35 40
periodsCPIF
percent
0.2
0.1
5 10 15 20 25 30 35 40
periodsGDP
0.4
20
5 10 15 20 25 30 35 40
periodsTerm spread
percent
percent
0.6
이
0.4
5 10
15 20 25 30 35 40periodsRER
0.2
5
10 15 20 25 30 35 40periods
5 10
15 20 25 30 35 40periods
Figure C.2: Impulse response to ECB QE shock. We use the Bayesian VAR model,Minnesota prior, 2 lags. Results refer to max FEV identification at 40 months.Sample period is 2015:01-2018:12. Responses are in percentage terms. The blacksolid lines represent the median response. The shaded area denotes a 68 per cent
credible interval.
44
50
-ECB announced
45
Riksbank announced
40
-ECB effective
35
Riksbank effective
30
25
20
15
10
5
0
2015m1 2015m6 2015m11 2016m4 2016m9 2017m2 2017m7 2017m12 2018m5 2018m10
Figure C.3: Announced asset purchases (continuous lines) and asset holdings in thebalance sheet (dashed lines) of the ECB (blue lines) and the Riksbank (red lines).Shares over 2014:Q4 annualized GDP of each region.
45
RER
GDP
6
0
CPIF
ECB QE shock
Riksbank QE shock
2
2
1.5
1.5
1
1
0.5
0.5
0
0
0
10
20
30
40
0
10
20
30
40
2
0
2
-1
-1
0
10
20
30
40
0
10
20
30
40
6
4
4
2
2
0
0
0
10
20
30
40
0
10
20
30
40
Figure C.4: Impulse response functions to the ECB QE shock and the Riksbank QEshock, normalized to one percent decrease in the long-term rate. We use thebaseline Bayesian VAR model, Minnesota prior, 2 lags, where the long-term ratesreplace the announced asset purchases and the short-term rate replaces the termspread. Results refer to Identification I. Sample period is 2015:01-2018:12. We use2000 simulations and 500 more for burn-in. Responses are in percentage terms. Theblue and black solid lines represent the median responses of the ECB QE shock andthe Riksbank QE shock, respectively. The dashed lines denotes a 68 per centcredible interval.
46
D Additional tables
Table D.1: Alternative model specifications
| Model | ECB | Riksbank QE shock |
| --- | --- | --- |
|  | Total effect inflation | Total effect inflation |
| Baseline | 0.21* | 0.16* |
| w Effective purchases | 0.33* | 0.29* |
| w Fed funds | 0.12* | 0.16* |
| w Euro area prices | 0.25* | 0.36* |
| w oil prices | 0.21* | 0.15* |
| up to 2019 | 0.13* | 0.17* |
| from 2014 | 0.12*0.05 | 0.33* |

Model
ECB
QE shock
Riksbank QE shock
Total effect inflation
Peak effect GDP
Total effect inflation
Peak effect GDP
Baseline
0.21*
0.22*
0.16*
-0.06
w Effective purchases
0.33*
0.29*
0.29*
0.13
w Fed funds
0.12*
0.13*
0.16*
-0.07
w Euro area prices
0.25*
0.26*
0.36*
0.002*
w oil prices
0.21*
0.20*
0.15*
-0.06
up to 2019
0.13*
0.09
0.17*
-0.05
from 2014
0.12*0.05
0.33*
-0.06
Values come from baseline model, model with effective purchases replacing announced purchases,baseline model with the addition of Fed funds rate, oil prices or euro area inflation and baselinemodel extended to 2019. All models use Identification I, effects are standardized to one percentof GDP. * indicates that at the time of the effect the 68 per cent credible intervals are mostlyexcluding zero.
47
Recent Working Papers:
For a complete list of Working Papers published by Sveriges Riksbank, see www.riksbank.se
| The Macroeconomic Effects of Trade Tariffs: Revisiting the Lerner Symmetry Resultby Jesper Lindé and Andrea Pescatori | 2019:363 |
| --- | --- |
| Biased Forecasts to Affect Voting Decisions? The Brexit Caseby Davide Cipullo and André Reslow | 2019:364 |
| The Interaction Between Fiscal and Monetary Policies: Evidence from Swedenby Sebastian Ankargren and Hovick Shahnazarian | 2019:365 |
| Designing a Simple Loss Function for Central Banks: Does a Dual Mandate Make Sense?by Davide Debortoli, Jinill Kim and Jesper Lindé | 2019:366 |
| Gains from Wage Flexibility and the Zero Lower Boundby Roberto M. Billi and Jordi Galí | 2019:367 |
| Fixed Wage Contracts and Monetary Non-Neutralityby Maria Björklund, Mikael Carlsson and Oskar Nordström Skans | 2019:368 |
| The Consequences of Uncertainty: Climate Sensitivity and Economic Sensitivity to the Climateby John Hassler, Per Krusell and Conny Olovsson | 2019: |
| Does Inflation Targeting Reduce the Dispersion of Price Setters' Inflation Expectations?by Charlotte Paulie | 2019:370 |
| Subsampling Sequential Monte Carlo for Static Bayesian Modelsby David Gunawan, Khue-Dung Dang, Matias Quiroz, Robert Kohn and Minh-Ngoc Tran | 2019:371 |
| Hamiltonian Monte Carlo with Energy Conserving Subsamplingby Khue-Dung Dang, Matias Quiroz, Robert Kohn, Minh-Ngoc Tran and Mattias Villani | 2019:372 |
| Institutional Investors and Corporate Investmentby Cristina Cella | 2019:373 |
| The Impact of Local Taxes and Public Services on Property Valuesby Anna Grodecka and Isaiah Hull | 2019:374 |
| Directed technical change as a response to natural-resource scarcityby John Hassler, Per Krusell and Conny Olovsson | 2019:375 |
| A Tale of Two Countries: Cash Demand in Canada and Swedenby Walter Engert, Ben Fung and Björn Segendorf | 2019:376 |
| Tax and spending shocks in the open economy: are the deficits twins?by Mathias Klein and Ludger Linnemann | 2019:377 |
| Mind the gap! Stylized dynamic facts and structural modelsby Fabio Canova and Filippo Ferroni | 2019:378 |
| Financial Buffers, Unemployment Duration and Replacement Labor Incomeby Mats Levander | 2019:379 |
| Inefficient Use of Competitors' Forecasts?by André Reslow | 2019:380 |
| How Much Information Do Monetary Policy Committees Disclose? Evidence from the FOMC's Minutesand Transcriptsby Mikael Apel, Marianna Blix Grimaldi and Isaiah Hull | 2019:381 |
| Risk endogeneity at the lender/investor-of-last-resortby Diego Caballero, André Lucas, Bernd Schwaab and Xin Zhang | 2019:382 |
| Heterogeneity in Households' Expectations of Housing Prices - Evidence from Micro Databy Erik Hjalmarsson and Pär Österholm | 2019:383 |
| Big Broad Banks: How Does Cross-Selling A Affect Lending?by Yingjie Qi | 2020:384 |
| Unemployment Fluctuations and Nominal GDP Targetingby Roberto Billi | 2020:385 |
| FAQ: How do I extract the output gap?by Fabio Canova | 2020:386 |

The Macroeconomic Effects of Trade Tariffs: Revisiting the Lerner Symmetry Resultby Jesper Lindé and Andrea Pescatori
2019:363
Biased Forecasts to Affect Voting Decisions? The Brexit Caseby Davide Cipullo and André Reslow
2019:364
The Interaction Between Fiscal and Monetary Policies: Evidence from Swedenby Sebastian Ankargren and Hovick Shahnazarian
2019:365
Designing a Simple Loss Function for Central Banks: Does a Dual Mandate Make Sense?by Davide Debortoli, Jinill Kim and Jesper Lindé
2019:366
Gains from Wage Flexibility and the Zero Lower Boundby Roberto M. Billi and Jordi Galí
2019:367
Fixed Wage Contracts and Monetary Non-Neutralityby Maria Björklund, Mikael Carlsson and Oskar Nordström Skans
2019:368
The Consequences of Uncertainty: Climate Sensitivity and Economic Sensitivity to the Climateby John Hassler, Per Krusell and Conny Olovsson
2019:
369
Does Inflation Targeting Reduce the Dispersion of Price Setters' Inflation Expectations?by Charlotte Paulie
2019:370
Subsampling Sequential Monte Carlo for Static Bayesian Modelsby David Gunawan, Khue-Dung Dang, Matias Quiroz, Robert Kohn and Minh-Ngoc Tran
2019:371
Hamiltonian Monte Carlo with Energy Conserving Subsamplingby Khue-Dung Dang, Matias Quiroz, Robert Kohn, Minh-Ngoc Tran and Mattias Villani
2019:372
Institutional Investors and Corporate Investmentby Cristina Cella
2019:373
The Impact of Local Taxes and Public Services on Property Valuesby Anna Grodecka and Isaiah Hull
2019:374
Directed technical change as a response to natural-resource scarcityby John Hassler, Per Krusell and Conny Olovsson
2019:375
A Tale of Two Countries: Cash Demand in Canada and Swedenby Walter Engert, Ben Fung and Björn Segendorf
2019:376
Tax and spending shocks in the open economy: are the deficits twins?by Mathias Klein and Ludger Linnemann
2019:377
Mind the gap! Stylized dynamic facts and structural modelsby Fabio Canova and Filippo Ferroni
2019:378
Financial Buffers, Unemployment Duration and Replacement Labor Incomeby Mats Levander
2019:379
Inefficient Use of Competitors' Forecasts?by André Reslow
2019:380
How Much Information Do Monetary Policy Committees Disclose? Evidence from the FOMC's Minutesand Transcriptsby Mikael Apel, Marianna Blix Grimaldi and Isaiah Hull
2019:381
Risk endogeneity at the lender/investor-of-last-resortby Diego Caballero, André Lucas, Bernd Schwaab and Xin Zhang
2019:382
Heterogeneity in Households' Expectations of Housing Prices - Evidence from Micro Databy Erik Hjalmarsson and Pär Österholm
2019:383
Big Broad Banks: How Does Cross-Selling A Affect Lending?by Yingjie Qi
2020:384
Unemployment Fluctuations and Nominal GDP Targetingby Roberto Billi
2020:385
FAQ: How do I extract the output gap?by Fabio Canova
2020:386
| Drivers of consumer prices and exchange rates in small open economiesby Vesna Corbo and Paola Di Casola | 2020:387 |
| --- | --- |
| TFP news, stock market booms and the business cycle: Revisiting the evidence with VEC modelsby Paola Di Casola and Spyridon Sichlimiris | 2020:388 |
| The costs of macroprudential deleveraging in a liquidity trapby Jiaqian Chen, Daria Finocchiaro, Jesper Lindé and Karl Walentin | 2020:389 |
| The Role of Money in Monetary Policy at the Lower Boundby Roberto M. Billi, Ulf Söderström and Carl E. Walsh | 2020:390 |
| MAJA: A two-region DSGE model for Sweden and its main trading partnersby Vesna Corbo and Ingvar Strid | 2020:391 |
| The interaction between macroprudential and monetary policies: The cases of Norway and Swedenby Jin Cao, Valeriya Dinger, Anna Grodecka-Messi, Ragnar Juelsrud and Xin Zhang | 2020:392 |
| Withering Cash: Is Sweden ahead of the curve or just special?by Hanna Armelius, Carl Andreas Claussen and André Reslow | 2020:393 |
| Labor shortages and wage growthby Erik Frohm | 2020:394 |
| Macro Uncertainty and Unemployment Riskby Joonseok Oh and Anna Rogantini Picco | 2020:395 |
| Monetary Policy Surprises, Central Bank Information Shocks, and Economic Activity in a Small OpenEconomyby Stefan Laséen | 2020:396 |
| Econometric issues with Laubach and Williams' estimates of the natural rate of interestby Daniel Buncic | 2020:397 |
| Quantum Technology for Economistsby Isaiah Hull, Or Sattath, Eleni Diamanti and Göran Wendin | 2020:398 |
| Modeling extreme events: time-varying extreme tail shapeby Bernd Schwaab, Xin Zhang and André Lucas | 2020:399 |
| The Effects of Government Spending in the Eurozoneby Ricardo Duque Gabriel, Mathias Klein and Ana Sofia Pessoa | 2020:400 |
| Narrative Fragmentation and the Business Cycleby Christoph Bertsch, Isaiah Hull and Xin Zhang | 2021:401 |
| The Liquidity of the Government Bond Market - What Impact Does Quantitative Easing Have? Evidencefrom Swedenby Marianna Blix Grimaldi, Alberto Crosta and Dong Zhang | 2021:402 |
| Five Facts about the Distributional Income Effects of Monetary Policyby Niklas Amberg, Thomas Jansson, Mathias Klein and Anna Rogantini Picco | 2021:403 |

Drivers of consumer prices and exchange rates in small open economiesby Vesna Corbo and Paola Di Casola
2020:387
TFP news, stock market booms and the business cycle: Revisiting the evidence with VEC modelsby Paola Di Casola and Spyridon Sichlimiris
2020:388
The costs of macroprudential deleveraging in a liquidity trapby Jiaqian Chen, Daria Finocchiaro, Jesper Lindé and Karl Walentin
2020:389
The Role of Money in Monetary Policy at the Lower Boundby Roberto M. Billi, Ulf Söderström and Carl E. Walsh
2020:390
MAJA: A two-region DSGE model for Sweden and its main trading partnersby Vesna Corbo and Ingvar Strid
2020:391
The interaction between macroprudential and monetary policies: The cases of Norway and Swedenby Jin Cao, Valeriya Dinger, Anna Grodecka-Messi, Ragnar Juelsrud and Xin Zhang
2020:392
Withering Cash: Is Sweden ahead of the curve or just special?by Hanna Armelius, Carl Andreas Claussen and André Reslow
2020:393
Labor shortages and wage growthby Erik Frohm
2020:394
Macro Uncertainty and Unemployment Riskby Joonseok Oh and Anna Rogantini Picco
2020:395
Monetary Policy Surprises, Central Bank Information Shocks, and Economic Activity in a Small OpenEconomyby Stefan Laséen
2020:396
Econometric issues with Laubach and Williams' estimates of the natural rate of interestby Daniel Buncic
2020:397
Quantum Technology for Economistsby Isaiah Hull, Or Sattath, Eleni Diamanti and Göran Wendin
2020:398
Modeling extreme events: time-varying extreme tail shapeby Bernd Schwaab, Xin Zhang and André Lucas
2020:399
The Effects of Government Spending in the Eurozoneby Ricardo Duque Gabriel, Mathias Klein and Ana Sofia Pessoa
2020:400
Narrative Fragmentation and the Business Cycleby Christoph Bertsch, Isaiah Hull and Xin Zhang
2021:401
The Liquidity of the Government Bond Market - What Impact Does Quantitative Easing Have? Evidencefrom Swedenby Marianna Blix Grimaldi, Alberto Crosta and Dong Zhang
2021:402
Five Facts about the Distributional Income Effects of Monetary Policyby Niklas Amberg, Thomas Jansson, Mathias Klein and Anna Rogantini Picco
2021:403
SVERIGES
RIKSBANK
Sveriges Riksbank
Visiting address: Brunkebergs torg 11
Mail address: se-103 37 Stockholm
Website: www.riksbank.se
Telephone: +46 8 787 00 00, Fax: +46 8 21 05 31E-mail: registratorn@riksbank.se