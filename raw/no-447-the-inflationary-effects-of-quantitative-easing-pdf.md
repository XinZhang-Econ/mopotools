
SVERIGES RIKSBANK
WORKING PAPER SERIES
ChaMP
447
SVERIGESRIKSBANK
The Inflationary Effects of Quantitative Easing
Mathias Klein and Xin Zhang
February 2025
WORKING PAPERS ARE OBTAINABLE FROM
www.riksbank.se/en/research
Sveriges Riksbank SE-103 37 StockholmFax international: +46 8 21 05 31Telephone international: +46 8 787 00 00
The Working Paper series presents reports on matters inthe sphere of activities of the Riksbank that are considered
to be of interest to a wider public.
The papers are to be regarded as reports on ongoing studiesand the authors will be pleased to receive comments.
The opinions expressed in this article are the sole responsibility of the author(s) and should not be
interpreted as reflecting the views of Sveriges Riksbank.
The Inflationary Effects of Quantitative Easing*
Mathias Klein
Xin Zhang
Sveriges Riksbank
Sveriges Riksbank
February 24, 2025
Sveriges Riksbank Working Paper Series No. 447Abstract
We provide new evidence on the inflationary effects of Quantitative Easing (QE) usingSwedish administrative data at the bank, firm, and product level. For identification,we rely on bank-firm lending relationships and the heterogeneous participation ratesof banks in the government bond purchase program by the Swedish central bank.Our results show that the bond purchase program led to a significant and persistentincrease in producer prices. Importantly, we find that the degree of financial frictionsconsiderably influences firms' price response: low leverage firms do not change theirprices, whereas high leverage firms raise their prices significantly. This divergent pricingbehaviour can be rationalized by a significant increase in long-term borrowing andinterest rate expenses among high leverage firms. The difference in price responsesacross high and low leverage firms is less pronounced for exogenous changes in therepo rate implying that the transmission mechanism of QE differs from the one ofconventional interest rate policy.
*For valuable comments and suggestions, we thank Niklas Amberg, Christoph Bertsch, Olivier Coibion, Jens Christensen (discussant), LucaDedola, Michael Ehrmann, Martin Ellison, Zeno Enders, Francesco Furlanetto, Georgios Georgiadis, Boris Hofmann, Peter Karadi, Ryan Kim(discussant), Gisle Natvik, Mathieu Pedemonte (discussant), Vincenzo Quadrini, Federico Ravenna, Anna Rogantini Picco, Timo Reinelt, RaphaelSchoenle, Daniel Streitz, Felix Strobel (discussant), Yannick Timmer, Tomasz Wieladek, Roland Winkler, Jing Cynthia Wu and Francesco Zanetti aswell as conference and seminar participants at the ChaMP Research Network Workshop, the 23rd IWH-CIREQ-GW Macroeconometric Workshop,4th European Midwest Micro/Macro Conference, PRISMA/ESCB Workshop on Firm-level price setting and inflation dynamics, the Federal ReserveDay Ahead Conference on Financial Markets and Institutions, the Innsbruck Workshop in Empirical Macroeconomics, and the Bank of Canadaand the University of Toronto's Inflation Workshop. The views expressed in this paper are those of the author and they do not necessarily reflectthe views of Sveriges Riksbank.
Keywords: Quantitative easing, price dynamics, financial frictions.
JEL Classification: E31, E51, E58.
1 Introduction
As many central banks across the globe have reached the zero lower bound (ZLB) onnominal interest rates, unconventional monetary policies like large-scale asset purchaseshave become a popular tool to stimulate private demand and raise prices. Thesepolicies were implemented by many central banks around the world, however, theireffects and transmission mechanisms are still unsettled questions. While some papersprovide evidence in favor of significant positive effects of unconventional monetarypolicies (Lewis, 2019; Gambacorta et al., 2014; Boeckx et al., 2020), others find onlysmall or even negative effects (Lenza et al., 2010; Carlstrom et al., 2017). Most of thesestudies use aggregate data to trace out the dynamic impact of unconventional monetarypolicies. However, relying on aggregate time series faces the challenges of first, limitedtime variation given the relatively short period during which unconventional monetarypolicies were implemented and, second, the lack of proper identification as economiesare hit by different aggregate shocks at the same time.
This paper provides new estimates on the inflationary effects of quantitative easing(QE) using detailed micro level data on the Swedish economy. In particular, we mergeofficial data underlying the aggregate producer price index (PPI) with administrativebank and firm level data. We construct a linked database of granular bank-firm-product-price information. For identification, we use the different exposure of banks tothe government bond purchase program by the Swedish central bank (Sveriges Riks-bank) and construct an individual firm treatment measure based on bank-firm rela-tionships in the spirit of Acharya et al. (2019). The measure relies on the typicalbank lending channel of monetary policy and is constructed such that firms havinga relationship with banks more active in the QE program are more exposed to theunconventional monetary policy intervention compared to firms having a relationship1
with less active banks.
Our analysis at the very granular level has several important advantages comparedto studies at the aggregate level. First, the large cross sectional variation can be usedfor identification and should thus result in more precise estimates. As our proposed QEexposure measure varies across time and between firms, the impact of unconventionalmonetary policy can be studied at the micro level. Secondly, using the comprehensiveinformation on firm characteristics, potential heterogeneities can be investigated in astraight forward way. Indeed, we show that the degree of firms' financial frictions iscrucial for understanding the price response to QE.
Our main results show that large scale asset purchases are an effective tool toincrease prices in the economy. We find that the government bond purchase programby the Riksbank led to a significant increase in producer price inflation that lasts formore than a year. A 1 billion SEK QE exposure leads to a one year increase in producerprices by more than 1%. Thus, QE might indeed serve as an adequate tool to produceinflationary pressure when the ZLB restricts conventional interest rate policy.
Importantly, we detect strong heterogeneities in the price setting behaviour acrossfirms. First, much in line with D'Acunto et al. (2018); Gilchrist et al. (2017); Renkinand Zuellig (2023), we show that financial frictions are a central determinant of afirms' pricing behaviour unconditional on the bond purchase innovation. High leveragefirms have a larger price changing frequency than low leverage ones implying moreflexible prices for financially constrained firms. Secondly, we show that the degree offinancial frictions significantly influences how firms adjust their prices following thecentral banks' bond purchases. Low leverage firms do not change their prices by asignificant amount. In stark contrast, high leverage firms raise their prices significantly.The increase in prices among high leverage firms is driven by a rise in both price-settingmargins: a higher price change frequency and a larger price change magnitude. Lowleverage firms reduce both price-setting margins. Thus, the inflationary effects of QEare mainly driven by financially constrained firms.
To better understand the underlying driver of this leverage-dependent price re-2
sponse to unconventional monetary policy interventions, we make use of our granularmatched dataset and run additional regressions at the firm level on real and financialvariables. We find that high leverage firms significantly increase their long-term debtposition and face higher interest rate expenses following the QE intervention. Thus,borrowing costs of high leverage firms rise, which puts upward pressure on their pric-ing decision. The additional borrowing is mainly used to finance investments in fixedassets. Because such assets can typically be used a collateral for debt, increasing fixedassets could be explained by an incentive among high leverage firms to loosen bor-rowing constraints in the future. Moreover, high leverage firms do not gain from anypositive aggregate demand effects which results in higher inventories and no significantchange in revenues for these firms. In contrast, investment in R&D, machines, andequipment by low leverage firms increases which mitigates any positive price pressurefor these firms. In addition, low leverage firms experience an increase in profits andrevenues and thus are able to raise their market share.
Notably, we also show that the difference in price responses across high and lowleverage firms is less pronounced for conventional monetary policy interventions. Anexogenous fall in the repo rate leads to price increases among both low and high lever-age firms. This suggests that the transmission mechanism of QE to inflation is differentto the one of conventional interest rate policy. Our estimates imply that a governmentbond purchase program of 1.3% of GDP induces a similar-sized price increase thanan exogenous fall in the repo rate by 25 basis points. Overall, our findings intend toinform theoretical analyses on the impact of QE and on the importance of financialfrictions for understanding how unconventional monetary policy shapes the economy.
Related literature. A number of papers investigate the impact of QE on inflationin Japan, the Euro Area, U.K. and U.S.. Fabo et al. (2021) provide a survey of 54studies on how QE impacts output and inflation. They find that the average (median)effect on the price level consists in an increase by 1.42% (0.93%). Standardizing theQE intervention to 1% of GDP, the average (median) effect on the price level is 0.19%
3
(0.11%). What's more, they find that the inflationary effect of QE is strongest in theU.S..¹ The surveyed papers employ either DSGE models or VAR models to estimatethe impact of quantitative easing. In our paper, we are among the first to evaluate theimpact of QE on inflation exploring very detailed micro data on producer prices andlinking them with firm characteristics and bank lending relationships.
There are a few well established transmission channels of QE to financial marketsand to the real economy. Our paper is related to the classical bank lending channel ofmonetary policy transmission, as first introduced by Bernanke et al. (1988).2 Under thebank lending channel, bank deposits are negatively affected when central banks tightenthe policy rate, leading to a reduction of bank credit in the economy. A few recent worksfocus on unconventional monetary policy and the bank lending channels, includingJoyce and Spaltro (2014), Buttz et al. (2015) and Bowman et al. (2015). These paperspresent evidence of stimulatory effects of QE but with various degrees of significance. Itis thus important to relate the QE program to the economic condition and the financialmarket structure. In our study, we show that unconventional monetary policy transmitsthrough the bank-firm credit relationship in Sweden, which contributes to the increasein producer prices and the heterogeneous price responses across financially constrainedand unconstrained firms.
A few papers in the literature document the heterogeneous impacts of QE on banks(Rodnyansky and Darmouni, 2017; Sims and Wu, 2021), households (Cui and Sterk,2021), and firms R&D decisions (Grimm et al., 2021). To the best of our knowledge, weare the first to document firms' heterogeneous price responses to QE. Our work is alsorelated to Sims and Wu (2021). They present a model in which financial intermediaries,as in Gertler and Karadi (2018), can hold long-term bonds issued by firms or thegovernment, and interest-bearing reserves. Within the model, the QE program leads
to a change of portfolio holdings of banks and eases its balance sheet constraints, which
¹It is worth mentioning that the authors find substantial differences in the results among different countriesand different researchers.
2Morais et al. (2019) show that there exists an international bank lending channel. As a result, Quanti-tative Easing programs in the U.K., U.S. and Euro Area generate significant spillovers to emerging marketeconomies.
4
enables financial institutions to buy more privately issued bonds.
Our paper is broadly related to the literature on how firm heterogeneity shapes themonetary policy transmission mechanism. Ehrmann and Fratzscher (2004), Gorod-nichenko and Weber (2016) and Ippolito et al. (2018) show that firms with differentcharacteristics have heterogeneous sensitivities to monetary policy shocks and mone-tary policy communications. We contribute to this strand of the literature by focusingon the inflationary effects of unconventional monetary policy, which is an importantpolicy tool when conventional monetary policy is constrained by the ZLB. We furtherhighlight the differences of price responses across constrained and unconstrained firmsand rationalize our findings by divergent adjustments of long term debt positions andinterest rate expenses. When the floating-rate channel of Ippolito et al. (2018) is notactive at the ZLB, we find that long-term debt can serve as an important transmissionchannel of unconventional monetary policy.
Finally, our paper relates to recent studies which investigate the relationship be-tween price-setting behaviour and firms' financial conditions (Gilchrist et al., 2017;D'Acunto et al., 2018; Renkin and Zuellig, 2023; Kim, 2021). We contribute to thisliterature by showing that firms' financial position is key to understand how uncon-ventional monetary policy interventions transmit to inflation.
Institutional background. The Riksbank started the QE program after an extendperiod of low inflation in Sweden. In response to the low inflation environment after theGreat Financial Crisis and the European Debt Crisis, Sveriges Riksbank lowered thepolicy rate to zero and implemented negative interest rates later on. In February 2015,the Riksbank introduced the QE program to purchase Swedish government bonds. ByApril 2020, it owned more than half of the outstanding nominal bonds and aroundone-fourth of the inflation-linked ones. In April 2022, the Riksbank held Swedish gov-ernment bonds of SEK 401 billion. According to the evaluation of the Riksbank, thesepurchases successfully lowered interest rates which, in turn, led to a boost in aggregatedemand and stimulated the economy. During the Corona pandemic, the Riksbank fur-ther extended the purchase to include covered bonds, municipality bonds, and qualified
5
corporate bonds, to support market liquidity and market functions.3 The Riksbank
has conducted more than 450 auctions of nominal and real Swedish government bondsin the period between February 2015 and June 2021. The QE purchase transactionshappen at a higher frequency than the auctions. In the paper, we utilize a proprietarydataset of Riksbank bond purchase allocations among participating banks to investi-gate the inflationary effects of the QE program through bank-firm credit relationships.
Structure of the paper. The paper proceeds as follows. Section 2 presents ourmain dataset and the identification strategy. Section 3 describes our econometric ap-proach and Section 4 discusses the main empirical results on the firms' pricing responsesto the Riksbank QE program, the underlying transmission mechanism, and comparesthe main findings to the ones in response to conventional monetary policy interven-tions. Section 5 presents the results of several robustness checks. Finally, Section 6concludes.
2
Data
In this section, we describe the main data used in our empirical exercise. In particular,we merge several different Swedish databases: the micro price data underlying theofficial Producer Price Index, the banks' participation in the Riksbank QE program,banks' balance sheet information, all firms' financial and accounting variables, and thebank-firm exposure in banks' loan portfolios. As far as we know, it is the first attempt inthe literature to create a linked database of such granular bank-firm-price information.While our main identification relies on the detailed bank-firm relationships, the mainoutcome variable consists in the firms' pricing decision. In addition, we include severalmacroeconomic control variables in the regressions.
3In our study, we do not investigate the Coronavirus pandemic QE program.
6
2.1 Price data
We use administrative product-level data from Statistics Sweden (SCB), comprisingall products underlying the Swedish producer and import price index (PPI). The PPIis calculated as a weighted average of observed monthly prices on individual prod-uct offerings by product group level according to the Swedish Standard of IndustryClassification (SPIN), and may then be aggregated to final indices within each market(domestic, import and export) as well as for all Swedish-made products. Thus, bothproduct-specific and product group-specific weights are used in the construction of theofficial PPI. The data covers the period January 1992 to December 2017 and includesroughly 1.44 million price observations in total.
We filter out observations with negative prices as well as duplicated products, andexclude a SPIN group for the entire year whenever the group has missing observationswithin that specific year. Moreover, we restrict the analysis to manufactured productssold at the Swedish domestic market. After these cleaning steps, we are left with morethan 51,000 price observations which amounts to roughly 80% of the raw data availablefor our baseline sample of the QE program which covers the period 2015M2-2017M12.
2.2 Bank and firm data
We obtain the bond purchase auction and sales history in the Riksbank QuantitativeEasing program that started in 2015. Several banks participated in the bond auction.We observe the bidding amount, price information from each bank in each round ofthe QE program, and we have information on the final bond sales allocation and thecorresponding price. We sum up bank b's QE sales at month t as its QE participation$QE_{b,t}$ Figure 1 provides a time series plot of randomly selected banks' QE partici-pation. It shows that the bank participation is highly volatile over time and differentin the cross-section which helps our identification strategy that combines variation inbanks' QE participation with bank-firm credit relationships. For example, we can seethat Bank B is not involved in the QE sales for more than half of the sample period,7
Figure 1: Banks' QE activities
Bank ABank C
Bank BBank D
6-
4-
3-
2
1
2015
2016
2017
2018
2019
whereas Bank C is very active in the first half of the sample and show less activity inthe later periods.
Banks can either sell QE eligible government bonds from their own bond holdings,or sell bonds for their customers. The different nature of the bond sales could affectbanks' balance sheet differently. If the bank is selling bonds in their own portfolio,it will strengthen the liquidity position, and free up capital for other risk-taking busi-nesses, such as expanding corporate lending. If the bank is helping its customers to sellbonds in the QE program, it is very likely that bank deposits increase. The bank canthus increase lending to firms or other financial institutions. SCB provides a detaileddatabase of banks' balance sheet at the monthly frequency covering our sample period.Therefore, we can link banks' QE activities to changes of treasury (government bond)holdings and the deposits from other non-monetary financial institutions (Non-MFIs).
For the corporate sector, we have a large comprehensive database covering the wholeuniverse of Swedish firms, provided by the credit registry UC, for the period 1990-2019. We observe all firm balance sheet items, including financial, accounting, andreal variables at the annual frequency. The database covers all registered firms in8
Sweden, so it doesn't suffer from any bias in coverage across firm size or age. Below,we will use a number of firm level variables to investigate heterogeneous responses offirms to QE. Because the PPI microdata include a unique firm identifier, we can matchthe UC data with the price data. For our period of interest (2015M2-2017M12), thematch covers around 1,100 firms. Table 2 provides the summary statistics of the mainfirm variables used in the paper.
The final dataset is a hand-collected bank credit portfolio with detailed contract-level information. Here we observe the bank-firm lending relationship from the begin-ning of 2007 to the end of 2015. Unfortunately, the data collection process stopped atthe beginning of 2016. However, it seems reasonable to assume that bank relationshipsare relatively sticky. In our main regression specification, we will use the bank-firmlink variable just before the implementation of QE, to ease the concern that the QEparticipation is endogenous to the bank lending decision.
2.3 Measure firms' exposure to QE
We define firm i's exposure to QE at month t through bank b, through its creditrelationship exposure from bank b. The credit relationship variable $\omega_{i,b,t}$ is the fractionof credit from bank b over the total credit firm i borrows at month t.
Given bank b's bond sales amount in the QE program at tas $QE_{b,t}$, we can calculatea measure of firm QE exposure as
$Expo_{i,t}=\sum_{b}\omega_{i,b,t}\cdot QE_{b,t}$
(1)
The underlying assumption is that banks will channel more credit to its relationshipfirms after acquiring additional deposits from sales of government bonds through theQE program. Put differently, firms that have a relationship with banks more active inthe QE program are more exposed to the unconventional monetary policy interventionthan firms that have a relationship with less active banks. Thus, we rely on the wellknow bank-lending channel of QE very much in line with the approach suggested by
9
Table 1: Bank-firm credit relationship weights between 2008 and 2015
| Correlation | $\omega_{i,b,t}$ | $\omega_{i,b,t-12}$ | $\omega_{i,b,t-24}$ | $\omega_{i,b,t-36}$ | $\omega_{i,b,t-48}$ | $\omega_{i,b,t-60}$ | $\omega_{i,b,t-72}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\omega_{i,b,t}$ | 1.000 |  |  |  |  |  |  |
| $\omega_{i,b,t-12}$ | 0.929 | 1.000 |  |  |  |  |  |
| $\omega_{i,b,t-24}$ | 0.869 | 0.920 | 1.000 |  |  |  |  |
| $\omega_{i,b,t-36}$ | 0.806 | 0.850 | 0.908 | 1.000 |  |  |  |
| $\omega_{i,b,t-48}$ | 0.754 | 0.793 | 0.841 | 0.907 | 1.000 |  |  |
| $\omega_{i,b,t-60}$ | 0.703 | 0.735 | 0.775 | 0.830 | 0.893 | 1.000 |  |
| $\omega_{i,b,t-72}$ | 0.635 | 0.659 | 0.682 | 0.723 | 0.775 | 0.845 | 1.000 |

Correlation
$\omega_{i,b,t}$
$\omega_{i,b,t-12}$
$\omega_{i,b,t-24}$
$\omega_{i,b,t-36}$
$\omega_{i,b,t-48}$
$\omega_{i,b,t-60}$
$\omega_{i,b,t-72}$
$\omega_{i,b,t}$
1.000
$\omega_{i,b,t-12}$
0.929
1.000
$\omega_{i,b,t-24}$
0.869
0.920
1.000
$\omega_{i,b,t-36}$
0.806
0.850
0.908
1.000
$\omega_{i,b,t-48}$
0.754
0.793
0.841
0.907
1.000
$\omega_{i,b,t-60}$
0.703
0.735
0.775
0.830
0.893
1.000
$\omega_{i,b,t-72}$
0.635
0.659
0.682
0.723
0.775
0.845
1.000
Acharya et al. (2019). We fix the weight $\omega_{i,b,t}$ at $t=t_{0}$ as the credit relationship ratioin January 2015, right before the Riksbanks' QE program started.
There are a few reasons to weight the firm exposure with a predetermined sharethrough banks' QE sales. First of all, the bank lending relationship in Sweden isquite stable, especially for large firms. Obviously, it takes time to establish a creditrelationship between banks and firms. We elaborate on the point by examining thebank-firm credit relationships in our sample 2008-2015 using quarterly snapshots of therelationship mapping. Table 1 shows that the bank firm relationship, measured by$\omega_{i,b,t}$as the fraction of firm i's total loans coming from bank bat t, is highly correlated over
the 12-month, 24-month, and 36-month window. The correlation coefficient betweenthe contemporaneous weight, $\omega_{i,b,t}$, and the weight three years ago, $\omega_{i,b,t-36}$ is 0.806and highly statistically significant. If we only look at the main bank, which is definedas the bank that firm i borrows most credit from, none of the firms switched theirmain bank after 6 years. It is thus reasonable to assume that the share of loans fromvarious banks turn out to be constant over time. Thus, the time variation in the firms'exposure measure is coming from the bank's decision regarding their activity in theQE program only. This decision should be exogenous to the firms given their limitedpower in influencing the banks' participation in the bond purchases which supportsour identification strategy.
Secondly, we want to rule out that the weights are affected by the endogenousadjustments of banks' credit issuance. If banks follow the strategy to adjust the creditportfolio to favor certain firms, for instance riskier firms as in the risk taking channel ofmonetary policy, it is possible that banks' QE and credit decisions are decided jointly.
10
This would lead to possible endogeneity issues regarding firms' pricing decisions andcredit availability. In our analysis, we fix the credit allocation weights in the monthprior to the QE program, January 2015. Thus, we can rule out the possible endogenousresponse of credit re-allocation due to the QE program.
Table 2: Summary statistics
|  | count | mean | sd | p25 | p50 | p75 |
| --- | --- | --- | --- | --- | --- | --- |
| Cash flow/Total liabilities | 9864 | 0.252 | 0.295 | 0.057 | 0.180 | 0.383 |
| Labour cost / revenue | 9094 | 0.134 | 0.079 | 0.072 | 0.124 | 0.188 |
| Working capital / revenue | 9827 | 0.176 | 0.202 | 0.045 | 0.137 | 0.261 |
| Inventory / revenue | 9825 | 0.123 | 0.092 | 0.051 | 0.109 | 0.179 |
| Current liabilities / revenue | 9825 | 0.266 | 0.162 | 0.157 | 0.218 | 0.319 |
| Total DebtLong-term Debt | 9994 | 6.550 | 7.927 | 0.000 | 0.000 | 15.719 |
| Short-term Debt | 9994 | 5.269 | 7.240 | 0.000 | 0.000 | 14.108 |
| External interest expense | 10037 | 11.393 | 3.863 | 10.309 | 12.301 | 13.769 |
| Long-term leverage ratio | 9992 | 0.039 | 0.078 | 0.000 | 0.000 | 0.028 |
| R&D expenses | 2894 | 5.393 | 7.976 | 0.000 | 0.000 | 15.375 |
| Total sales | 9992 | 19.188 | 1.419 | 18.243 | 19.086 | 20.097 |
| $\omega_{i,b,t_{0}}$ | 9524 | 0.250 | 0.423 | 0.000 | 0.000 | 0.493 |
| $Expo_{i,t}$ | 121431 | 0.845 | 1.089 | 0.000 | 0.491 | 1.272 |

count
mean
sd
p25
p50
p75
Cash flow/Total liabilities
9864
0.252
0.295
0.057
0.180
0.383
Labour cost / revenue
9094
0.134
0.079
0.072
0.124
0.188
Working capital / revenue
9827
0.176
0.202
0.045
0.137
0.261
Inventory / revenue
9825
0.123
0.092
0.051
0.109
0.179
Current liabilities / revenue
9825
0.266
0.162
0.157
0.218
0.319
Total DebtLong-term Debt
9994
9996
6.550
4.698
7.927
7.204
0.000
0.000
0.000
0.000
15.719
14.323
Short-term Debt
9994
5.269
7.240
0.000
0.000
14.108
External interest expense
10037
11.393
3.863
10.309
12.301
13.769
Long-term leverage ratio
9992
0.039
0.078
0.000
0.000
0.028
R&D expenses
2894
5.393
7.976
0.000
0.000
15.375
Total sales
9992
19.188
1.419
18.243
19.086
20.097
$\omega_{i,b,t_{0}}$
9524
0.250
0.423
0.000
0.000
0.493
$Expo_{i,t}$
121431
0.845
1.089
0.000
0.491
1.272
3 Empirical specification
To evaluate the effects of quantitative easing on producer prices, we use panel localprojections (Jordà, 2005) at the individual product level and estimate for each horizon$h=0,...,12$, the following equation:
log(Yi,j,t+h) - log(Yi,j,t-1) =  j,h + am,h + ẞhExpoi,t + YhXi,t + Ui,j,t+h, (2)
where $y_{i,j,t}$ is the price of firm i for product j at month t. $\alpha_{j,h}$ are product groupfixed effects to filter out any unobserved heterogeneity across product groups. $\alpha_{m,h}$are monthly fixed effects to control for seasonal price movements. $X_{i,t}$ is a vectorof additional control variables and $u_{i,j,t+h}$ is the standard error term. $Expo_{i,t}$ is thequantitative easing exposure measure as already described earlier which varies betweenfirms and over time. Our focus lies on the coefficient $\beta_{h}$ which directly yields, for eachhorizon h, the firms' price response to the quantitative easing exposure measure. The
11
coefficient measures the relative price responses of QE exposed firms to those of firmsnot exposed. In the baseline model, $X_{i,t}$ includes 12 lags of the exposure measure, theaggregate unemployment rate, and the logarithm of the aggregate industrial produc-tion index to control for common movements in aggregate demand. Thus, the overallaggregate effect of quantitative easing is partly accounted for. As additional firm con-trols we also include one-year lags of the leverage ratio, defined as the ratio between thesum of short and long-term debt to total assets, the liquidity ratio, and the logarithmsof total assets and total sales. Throughout, we use Driscoll and Kraay (1998) standarderrors, which take into account the potential residual correlation across firms, as wellas serial correlation and heteroskedasticity among the residuals over time.
To investigate whether the price response depends on the financial conditions of afirm, we extend the linear specification (2) by an interaction term $I_{i,t}$
$log(y_{i,j,t+h})-log(y_{i,j,t-1})=I_{i,t-1}[\beta_{h}^{A}Expo_{i,t}+\gamma_{h}^{A}X_{i,t}]$
$+(1-I_{i,t-1})[\beta_{h}^{B}Expo_{i,t}+\gamma_{h}^{B}X_{i,t}]$ (3)
$+\alpha_{j,h}+\alpha_{m,h}+u_{i,j,t+h}$
$I_{i,t}$ is a dummy variable that takes a value of one if firm i has a high leverage ratioand zero otherwise. We will describe the particular leverage definition and thresholdvalues for $I_{i,t}$ below. We include a one-period lag of $I_{i,t}$ in the estimation to minimizethe contemporaneous correlation between the exposure measure and changes in theindicator variable. By interacting the exposure measure with the leverage dummy,$\beta_{h}^{A}$ provides the price response of high leverage firms following the unconventionalmonetary policy intervention, whereas $\beta_{h}^{B}$ gives the price response of low leveragefirms.
12
-.01
20
Figure 2: Producer prices and QE exposure
PPI Price Level
0
2
4
6Month
T8
10
T12
4 Empirical results
4.1 Producer price inflation
Figure 2 presents our main results from estimating equation (2). The solid line showsthe point estimate $\beta_{h}$ over a horizon of 12 months. The shaded areas are 90% Driscolland Kraay (1998) adjusted confidence bands.
For the first two months after the bond purchase, prices decline, although theresponse is insignificant. Afterwards, the price response turns positive and becomessignificant after around four months. One year after the unconventional monetarypolicy intervention, prices are around 1.2% above their pre-shock level. Thus a 1%GDP bond purchase in the QE program leads to a one year increase in producer prices4around 0.8%. Overall, we find that quantitative easing leads to a significant andpersistent price increase. Further, producer prices relatively quickly respond to theQE intervention leading to considerable price pressure within the year of the policy${}^{4}On$ average, the QE allocation ratio per bank is 0.070, and the average of $\omega_{i,b,t_{0}}$ is 0.250. Thus, 1% GDPpurchase around 40 billion SEK leads to 0.8% increase of the producer price.
13
.42
.44
.46Frequency of Price Change
.48
Figure 3: Price changing frequency and firm leverage
Yearly Averages (Lagged)
Low Leverage (Long)
High Leverage (Long)
change. Thus, bond purchases might serve as an effective tool to raise inflation whenthe ZLB restricts conventional interest rate policy. Our micro price analysis supportsrelated studies at the aggregate level which show that unconventional monetary policyhas expansionary effects by boosting economic activity and pushing up prices (Lewis,2019; Gambacorta et al., 2014; Boeckx et al., 2020).
An important advantage of our detailed micro data compared to studies at the ag-gregate level is the large cross-sectional variation that allows for investigating whetherthe transmission of unconventional monetary policy significantly differs across firmcharacteristics. While Figure 2 shows the inflationary effects of quantitative easing byassuming a common price response across all firms, it might well be argued that theway firms change their prices following a monetary policy intervention is influenced byspecific factors. In the following, we therefore test for important heterogeneous priceresponses across firms.
An obvious candidate that could affect a firms' pricing behavior is the degree offinancial frictions. Indeed, there is evidence that more financially constrained firms
Below, we further elaborate on this issue by comparing the inflationary effects of the QE interventionto an exogenous change in the repo rate.
14
20
20
.02
.04
Figure 4: Producer prices, QE exposure, and firm leveragePPI Price Level
0
2
4
6Month
8
10
T12
Low Leverage
High Leverage
change their prices more often and by a larger magnitude (D'Acunto et al., 2018;Gilchrist et al., 2017; Renkin and Zuellig, 2023). To investigate whether financialfrictions also influence the price response to our quantitative easing exposure measure,we first calculate for each firm the leverage ratio (defined as the sum of short term andlong term debt to total assets) and then define a low (high) leverage firm, dependingon whether an individual firms' leverage ratio is below (above) the mean leverage ratioacross all firm in the previous year. We also calculate the frequency of price adjustmentat the good level following the approach suggested by (D'Acunto et al., 2018). Inparticular, the price changing frequency is defined as the ratio of price changes to thenumber of sample months. For example, if an observed price path is SEK40 for twomonths and then changes to SEK50 for another three months, one price change occursduring five months, and the frequency of price adjustment is $1/5.$ As presented inFigure 3, our data show that high leverage firms have a larger price changing frequencycompared to low leverage firms which is very much in line with earlier literature. Putdifferently, prices of high leverage firms are more flexible than prices of low leverage
15
2+
2
Figure 5: Decomposing price changes among high and low leverage firms
0
6Month
10
12
Low
High
(a) Frequency price increase
2
0
2
6Month
8
10
12
Low
High
(b) Frequency price decrease
ones which suggests that the degree of financial frictions significantly influences firms'
price setting behavior.
Next, we estimate equation (3) allowing for a different price reaction coefficient tothe QE exposure measure for low and high leverage firms. The estimates are presentedin Figure 4. The results clearly demonstrate that the degree of financial frictionssignificantly influences how firms adjust their prices following the central banks' bondpurchase. In particular, low leverage firms do not change their prices by a significantamount in the short run and even show a slight tendency to decrease prices at longerhorizons. In stark contrast, high leverage firms raise their prices significantly leadingto a price increase after 12 months of around 4%. Thus, the inflationary effects ofquantitative easing documented in Figure 2 seem to be mainly driven by financiallyconstrained firms whereas firms with solid financial positions do not raise prices inresponse to the unconventional monetary policy intervention.
As shown by Klenow and Kryvtsov (2008), prices changes can be expressed asthe product of the frequency of price change, the extensive margin, and the averagesize of those price changes, the intensive margin. In addition, the frequency of pricechange can be further decomposed into terms due to price increases and price decreases.Similarly, the average size of price changes can be decomposed into terms due toprice increases and price decreases. Figure 5 shows the responses of the price changefrequency and the average size of price changes separately for price increases and price16
-.05
0
6Month
Low
High
10
12
05
0
6Month
Low
High
10
12
(a) Size price increase
(b) Size price decrease
decreases between high and low leverage firms. In response to the QE intervention,high leverage firms adjust both price-setting margins: they significantly increase theprice change frequency and raise the average size of price changes. Thus, followingthe bond purchase by the Riksbank, high leverage firms adjust prices more often andadjust actual prices by a larger magnitude. These effects are particularly strong forprice increases which explains the strong increase in prices as shown in Figure 4. Incontrast, low leverage firms significantly reduce the price change frequency and theaverage size of price changes. We do not find strong differences between price increasesand price declines which rationalizes the rather flat price response of low leverage firmspresented in Figure 4.
Our result of a leverage-dependent price response could be driven by the fact thathigh and low leverage firms are differently affected by the QE exposure measure. Forexample, if high leverage firms are much more exposed to QE than low leverage ones,our results might be biased because of different treatment intensities across firms.However, Figure 6 shows that this hypothesis is not supported by the data. The figurepresents the distribution of our QE exposure measure for high and low leverage firms,respectively. It is evident that both distributions are relatively similar, thus ruling outthat our results might be driven by significantly different treatment effects.
While we use unweighted price observations in our baseline regressions, our datasetalso includes the actual weights used to construct the official aggregate producer priceindex. To rule out that our main findings are driven by large price swings of products17
Figure 6: QE exposure distribution for high and low leverage firms
Density
10
15
20
20
5
Graphs by LevRat_ind
High Leverage
Low Leverage
0
.2
.4
.6 0QEAmount
2
.4
.6
with small weights, we re-estimate our local projections but weight product prices withtheir actual weights. Figure 7 presents the results, whereas the left panel shows theaverage price response across firms and the right panel presents the responses for highand low leverage firms, respectively. Solid lines correspond to the baseline (unweighted)regressions and dashed lines to the regressions using weighted observations. Moreover,shaded areas correspond to the confidence intervals of our baseline estimates. Theshapes of the weighted responses are very similar to our baseline estimates. In par-ticular, QE leads to an increase in average producer prices independent whether weweight price observations or not. However, the price increase is somewhat smaller forthe weighted regressions especially in the early periods of the forecast horizon. Mostimportantly, there is a strong divergent price response between high and low leveragefirms also when using weighted price observations. Prices of high leverage firms in-crease following the QE intervention whereas low leverage firms do not change theirprices significantly. Thus, our main findings are robust to using weighted (instead ofunweighted) price information in the local projections.
18
01
어
20
Figure 7: Baseline versus weighted price observations8-
0
2
4
6Month
8
10
12
Unweighted
Weighted
-.02
20
0
2
4
6Month
8
10
12
Low
High
WeightedWeighted
4.2 Comparison to conventional monetary policy shocksNext, we investigate whether the leverage-dependent price response detected for theQE exposure measure also prevails when studying the effects to conventional monetarypolicy. In doing so, we re-estimate equation (2) but replace the QE exposure measureby an aggregate Swedish monetary policy shock series. The monetary policy shockseries is taken from Amberg et al. (2021) who construct a monetary policy surpriseseries following a high-frequency identification strategy similar to those used in therecent literature on monetary non-neutrality (Gertler and Karadi, 2015; Jarocińskiand Karadi, 2020).
Figure 8 shows the estimates for the local projection not conditioning on firmleverage and Figure 9 presents the different price responses for low and high leveragefirms, respectively. In both figures the shock is normalized such that the repo rate fallsby 25 basis points in the impact period.
An exogenous expansionary monetary policy shock has a delayed effect on producerprice inflation which becomes significant after around 1 year. Two years after the shockmaterialized, inflation is more than 2% above its pre-shock level. Thus, similar to thebond purchase program, expansionary conventional monetary policy also pushes upproducer prices. Importantly, as shown in Figure 9, the price responses of low andhigh leverage firms are rather similar. Both, low and high leverage firms significantly
19
-.02
20
8- +
Figure 8: Producer prices and monetary policy shocks
PPI Price Level
0
3
6
9
12Month
15
18
21
24
increase their prices following an expansionary monetary policy shock. Although, highleverage firms raises their prices by a larger amount, the respective confidence bandsclearly overlap. Thus, the documented heterogeneous price reaction to the QE shockis unique in the sense that it is not observed for conventional monetary policy. Putdifferently, the transmission mechanism of QE to inflation is different to the one ofconventional interest rate policy.
We can further use these estimates to compare the inflationary effects of QE toconventional monetary policy. If we do a simple back-of-the envelope calculation,our estimates imply that in order to replicate the similar-sized price response at the12 month horizon of a exogenous reduction in the repo rate by 25 basis points, theRiksbank would need to implement a government bond purchases program of 1.3% ofGDP.
4.3
Understanding leverage-dependent price responses
What might explain the leverage-dependent price responses? In this section, we provideevidence that firms' borrowing and investment decisions following QE can rationalize20
-.02
Figure 9: Producer prices, monetary policy shock, and firms leverage
PPI Price Level
8-
20
0
3
6
9
12Month
15
18
21
T24
Low Leverage
High Leverage
the divergent price reaction of firms with high and low leverage. In doing so, we runthe following panel regression on the individual firm data:
$y_{i,yr}=\alpha_{i}+\alpha_{ind,yr}+\delta\sum_{yr}Expo_{i,t}+\gamma X_{i,yr-1}+\epsilon_{i,yr}$
(4)
The dependent variable $y_{i,yr}$ for firm i in year yr measures a particular variable ofinterest like debt holdings, debt interest rate expenses or investment expenditures. Weinclude firm fixed effects, $\alpha_{i}$, industry-year fixed effects, $\alpha_{ind,yr}$, and a few firm levelcontrol variables with a one period lag, including total asset, cash flow over total liabil-ity, labour cost over total revenue, working capital over total revenue, inventory overtotal revenue, and current liability normalized by revenue. Because the firm balancesheet data are only available at the annual frequency, we accumulate the monthly QEexposure measure to the annual aggregate value.
The firms debt and interest rate expense responses might be important for un-derstanding the firms' price response to the QE exposure because an higher (lower)outstanding debt raises (reduces) borrowing costs and thus firms' marginal financial
21
costs which increases (lowers) price pressure. In a similar vein, an increase (decrease)
in investment and in particular R&D investment, should be associated with higher(lower) productivity in the future which reduces (raises) marginal costs and thus prod-uct prices.
We report the regression results on total debt, long-term and short-term debt inTable 3. In order to show that the results are robust to different empirical specifications,we include firm fixed effects together with, either industry fixed effects and time fixedeffects or industry-time fixed effects. Columns (1) and (2) show that all firms' totaldebt increases following QE, although the level of significance varies a bit. Importantly,Columns (3) and (4) show that firms' long-term debt increases significantly. Theestimated coefficient from Column (4) implies that a 1 billion SEK QE exposure leadsto a 2.3% increase in firm's long-term debt (roughly 530 thousand SEK). Thus, theQE impact on long-term debt is both economically and statistically significant. Incontrast, Columns (5) and (6) indicate that short-term is not significantly affected bythe QE intervention. Therefore, the increase in total debt across firms is mainly drivenby a strong raise in long-term liabilities.
We further explore the heterogeneous responses across firms, by re-estimating re-gression (4) but splitting the sample between high and low leverage firms. In particular,we are interested in the response of their debt structure and business activities. We useas dependent variables the logarithm of long-term bank debt (LT Debt), short-termbank debt (ST Debt), external interest expenses, inventories, revenues, investment inR&D (R&D inv), and machines and equipment (M&E), and fixed-asset investment(FA Inv). We also run separate regressions with the contemporaneous QE exposurevariable and the 1 year lagged exposure variable, to capture the effects on slow-movingvariables. For instance, interest expenses may adjust slowly due to a change in thematurity structure.
The regression results are summarized in Table 4. Columns (1) and (2) report the
${}^{6}Our$ sample covers only those firms also covered in the micro price data between the years 2015 and2019. However, the results can be generalized to a larger sample of firms.
22
|  | (1) | (2) | (3) | (4)LT Debt | (5)ST Debt | (6)ST Debt |
| --- | --- | --- | --- | --- | --- | --- |
| Expoint | 0.0150* | 0.0158 | 0.0191** | 0.0226** | 0.0116 | 0.0080 |
|  | (0.0082) | (0.0104) | (0.0089) | (0.0105) | (0.0093) | (0.0106) |
| Cash flow / Total liab. | 0.0015 | 0.0034 | -0.0178 | -0.0131 | 0.0037 | 0.0032 |
|  | (0.0238) | (0.0232) | (0.0157) | (0.0112) | (0.0239) | (0.0230) |
| Labour cost / revenue | 0.1196 | 1.3216 | 0.0509 | 0.3490 | 0.0957 | 1.1274 |
|  | (0.0848) | (1.1414) | (0.0611) | (0.9408) | (0.0705) | (0.9088) |
| Working capital / revenue | -0.0021 | -0.0049* | -0.0009 | -0.0018 | -0.0013 | -0.0032* |
|  | (0.0014) | (0.0026) | (0.0010) | (0.0022) | (0.0009) | (0.0017) |
| Inventory / revenue | 0.0239 | 0.0431* | 0.0137 | 0.0177 | 0.0181 | 0.0402* |
|  | (0.0196) | (0.0242) | (0.0125) | (0.0186) | (0.0152) | (0.0212) |
| Current liab. / revenue | -0.0007 | -0.0033 | -0.0003 | -0.0010 | -0.0005 | -0.0025 |
|  | (0.0005) | (0.0023) | (0.0003) | (0.0020) | (0.0003) | (0.0018) |
| No of obs | 9013 | 8239 | 9015 | 8241 | 9013 | 8239 |
| Adj. R2 | 0.774 | 0.783 | 0.771 | 0.771 | 0.738 | 0.748 |
| Control | YES | YES | YES | YES | YES | YES |
| Firm FE | YES | YES | YES | YES | YES | YES |
| Ind. FE | YES | NO | YES | NO | YES | NO |
| Time FE | YES | NO | YES | NO | YES | NO |
| Ind-Time FE | NO | YES | NO | YES | NO | YES |
| Cluster SE | IND | FIRM | IND | FIRM | IND | FIRM |

(1)
Tot Debt
(2)
Tot Debt
(3)
LT Debt
(4)LT Debt
(5)ST Debt
(6)ST Debt
Expoint
0.0150*
0.0158
0.0191**
0.0226**
0.0116
0.0080
(0.0082)
(0.0104)
(0.0089)
(0.0105)
(0.0093)
(0.0106)
Cash flow / Total liab.
0.0015
0.0034
-0.0178
-0.0131
0.0037
0.0032
(0.0238)
(0.0232)
(0.0157)
(0.0112)
(0.0239)
(0.0230)
Labour cost / revenue
0.1196
1.3216
0.0509
0.3490
0.0957
1.1274
(0.0848)
(1.1414)
(0.0611)
(0.9408)
(0.0705)
(0.9088)
Working capital / revenue
-0.0021
-0.0049*
-0.0009
-0.0018
-0.0013
-0.0032*
(0.0014)
(0.0026)
(0.0010)
(0.0022)
(0.0009)
(0.0017)
Inventory / revenue
0.0239
0.0431*
0.0137
0.0177
0.0181
0.0402*
(0.0196)
(0.0242)
(0.0125)
(0.0186)
(0.0152)
(0.0212)
Current liab. / revenue
-0.0007
-0.0033
-0.0003
-0.0010
-0.0005
-0.0025
(0.0005)
(0.0023)
(0.0003)
(0.0020)
(0.0003)
(0.0018)
No of obs
9013
8239
9015
8241
9013
8239
Adj. R2
0.774
0.783
0.771
0.771
0.738
0.748
Control
YES
YES
YES
YES
YES
YES
Firm FE
YES
YES
YES
YES
YES
YES
Ind. FE
YES
NO
YES
NO
YES
NO
Time FE
YES
NO
YES
NO
YES
NO
Ind-Time FE
NO
YES
NO
YES
NO
YES
Cluster SE
IND
FIRM
IND
FIRM
IND
FIRM
Table 3: Firm debts and QE exposures
Notes: This table reports the results of regression 4 in the paper, with dependent variables as logarithmvalue of total bank debt (Tot Debt), short-term bank debt (ST Debt), and long-term bank debt (LT Debt).We include a few commonly used firm level control variables in the regression, with one period lag, includ-ing cash flow over total liability and labour cost/working capital/inventory/current liability normalized byrevenue. Note that the results are robust to removing the additional controls and with/without standarderror clustering. Industry-level (IND) or Firm-level clustered standard errors are reported in parentheses.***, and *** indicate statistical significance at the 10%, 5%, and 1% level, respectively.
results on the firms' debt structure. We find that the increase in long term debt isprimarily driven by an increase in long-term debt for firms with a high leverage ratio,while the increase for low leverage firms is not statistically significant. The magnitudeof the long-term debt increase is more than 3 times higher for high leverage firmscompared to low leverage ones. The changes in short-term debt are not statisticallysignificant across both firm groups. As a result of the strong increase in long termdebt, high leverage firms also experience a significant delayed rise in their interest rateexpenses (see Column (3)). In contrast, interest rate expenses of low leverage firmsdo not respond significantly. Thus, the QE intervention induces an rise in borrowingcosts among constrained firms which, in isolation, puts upward pressure on these firms'pricing decisions.
If we investigate the response of inventories and revenues for the two firm groups, asshown in Columns (4)-(5), we also find quite opposite results for high and low leveragefirms. In particular, inventories (revenues) significantly increase (decline) for high23
| (1) | (2) | (3) | (4) | (5)Revenue | (6)R&D Inv | (7)M&E | (8) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Panel A: All firms |  |  |  |  |  |  |  |
| 0.0226** | 0.0080 | 0.0022 | 0.0231** | 0.0061 | -0.0007 | 0.0312** | 0.0092* |
| (0.0105) | (0.0106) | (0.0032) | (0.0097) | (0.0068) | (0.0010) | (0.0138) | (0.0052) |
| 0.0559 | -0.0315 | -0.0018 | -0.0021 | 0.0106 | -0.0013 | 0.0016 | 0.0079 |
| (0.0411) | (0.0350) | (0.0051) | (0.0163) | (0.0151) | (0.0011) | (0.0229) | (0.0088) |
| Panel B: High-Lev firms |  |  |  |  |  |  |  |
| 0.0626* | 0.0504 | -0.0013 | 0.0242* | -0.0088 | -0.0031* | 0.0080 | 0.0239* |
| (0.0348) | (0.0326) | (0.0015) | (0.0136) | (0.0079) | (0.0018) | (0.0188) | (0.0141) |
| 0.0276 | -0.0007 | 0.0022* | 0.0042 | -0.0096* | -0.0001* | -0.0603* | 0.0044 |
| (0.0684) | (0.0581) | (0.0012) | (0.0136) | (0.0053) | (0.0001) | (0.0327) | (0.0087) |
| Panel C: Low-Lev firms |  |  |  |  |  |  |  |
| $Expo_{i,t}$ | -0.0182 | -0.0033 | 0.0162 | 0.0193* | 0.0013 | 0.0344* | 0.0143* |
| (0.0235) | (0.0285) | (0.0107) | (0.0106) | (0.0106) | (0.0013) | (0.0193) | (0.0082) |
| $Expo_{i,t-1}$ | -0.0404 | 0.0127 | 0.0052 | 0.0240 | -0.0008 | 0.0286 | 0.0129 |
| (0.0597) | (0.0460) | (0.0193) | (0.0089) | (0.0170) | (0.0020) | (0.0369) | (0.0131) |
| YES | YES | YES | YES | YES | YES | YES | YES |
| YES | YES | YES | YES | YES | YES | YES | YES |
| Ind-Time FE | YES | YES | YES | YES | YES | YES | YES |
| FIRM | FIRM | FIRM | FIRM | FIRM | FIRM | FIRM | FIRM |

(1)
LT Debt
(2)
ST Debt
(3)
Int. Exp.
(4)
Inventory
(5)Revenue
(6)R&D Inv
(7)M&E
(8)
FA Inv
Panel A: All firms
0.0226**
$Expo_{i,t}$
0.0080
0.0022
0.0231**
0.0061
-0.0007
0.0312**
0.0092*
(0.0105)
(0.0106)
(0.0032)
(0.0097)
(0.0068)
(0.0010)
(0.0138)
(0.0052)
0.0559
$Expo_{i,t-1}$
-0.0315
-0.0018
-0.0021
0.0106
-0.0013
0.0016
0.0079
(0.0411)
(0.0350)
(0.0051)
(0.0163)
(0.0151)
(0.0011)
(0.0229)
(0.0088)
Panel B: High-Lev firms
0.0626*
$Expo_{i,t}$
0.0504
-0.0013
0.0242*
-0.0088
-0.0031*
0.0080
0.0239*
(0.0348)
(0.0326)
(0.0015)
(0.0136)
(0.0079)
(0.0018)
(0.0188)
(0.0141)
0.0276
$Expo_{i,t-1}$
-0.0007
0.0022*
0.0042
-0.0096*
-0.0001*
-0.0603*
0.0044
(0.0684)
(0.0581)
(0.0012)
(0.0136)
(0.0053)
(0.0001)
(0.0327)
(0.0087)
Panel C: Low-Lev firms
$Expo_{i,t}$
0.0103
-0.0182
-0.0033
0.0162
0.0193*
0.0013
0.0344*
0.0143*
(0.0235)
(0.0285)
(0.0107)
(0.0106)
(0.0106)
(0.0013)
(0.0193)
(0.0082)
$Expo_{i,t-1}$
0.0343
-0.0404
0.0127
0.0052
0.0240
-0.0008
0.0286
0.0129
(0.0597)
(0.0460)
(0.0193)
(0.0089)
(0.0170)
(0.0020)
(0.0369)
(0.0131)
YES
Control
YES
YES
YES
YES
YES
YES
YES
YES
Firm FE
YES
YES
YES
YES
YES
YES
YES
Ind-Time FE
YES
YES
YES
YES
YES
YES
YES
YES
FIRM
Cluster FE
FIRM
FIRM
FIRM
FIRM
FIRM
FIRM
FIRM
Table 4: Firm decisions and QE exposures
Notes: This table reports the results of regression 4 in the paper, with dependent variables as logarithm valueof long-term bank debt (LT Debt), short-term bank debt (ST Debt), Interest expense over total bank debt(Int. Exp.), inventory, revenue, R&D investment (R&D inv), Machine and Equipment (M&E) and Fixed-asset investment (FA Inv). We include a few commonly used firm level control variables in the regression,with one period lag, including total asset (in log term), cash flow over total liability and labour cost/workingcapital/inventory/current liability normalized by revenue. Note that the results are robust to removing theadditional controls and with/without standard error clustering. Industry-time fixed effects and firm fixedeffects are included. Firm-level clustered standard errors are reported in parentheses. *,**, and *** indicatestatistical significance at the 10%, 5%, and 1% level, respectively.
24
leverage firms, which can be interpreted as a consequence of lower demand for productsof high leverage firms after the increase in product prices. On the other hand, lowleverage firms experience an increase in their revenues suggesting that unconstrainedfirms raise their market share based on a relative decrease in their product pricescompared to high leverage competitors. These results are confirmed by the change incosts of sold goods reported in Column (6).
In addition, we examine the investment decisions of high and low leverage firms.We aim to understand whether firms adjust their investment horizon and the type ofinvestment expenditures. As a start, we treat expenditures on Research and Devel-opment (R&D) investment as a proxy for long-term investment. R&D activities havea very long duration of investment horizon, and might lead to higher productivity.We find that high leverage firms significantly decrease their R&D expenditures whichshould lower their productivity path. Such a fall in productive investment can be in-terpreted as a negative supply shock, which according to standard theory, implies anincrease in prices. In contrast, R&D investment expenditures of low leverage firms raisealthough the estimated coefficient is not significantly different form zero. At the sametime, low leverage firms invest more in their machines and equipment, most likely toexpand their production. Low leverage firms also start to invest more in fixed assets.In addition, high leverage firms expand their fixed asset investment expenditures morethan low leverage firms. Because such assets can typically used a collateral for debt,increasing fixed assets investments among high leverage firms could be explained bythe incentive to stock up the available collateral and loosen borrowing constraints inthe future.
Through the additional firm level regressions, we find that high leverage firms sig-nificantly increase their long-term debt position following the QE intervention. In iso-lation this raises their marginal borrowing costs which is well in line with the observedsignificant increase in interest rate expenses among high leverage firms. Moreover, highleverage firms experience higher inventories and no significant change in revenues. Theadditional borrowing in long term debt is mainly used to increase fixed assets invest-25
ment, most likely to raise the collateral value of the firm. In contrast, investment inR&D, machines, and equipment by low leverage firms increases which helps them toincrease productivity. In addition, it enables low leverage firms to gain higher profitsand revenues while increasing their market share. Thus, the leverage-dependent priceresponse might be rationalized by QE raising marginal costs for high leverage firmswhile lowering marginal costs for low leverage firms.
We have explored several dimensions of firm heterogeneity, for instance size, age,and total debt. However, none of the other heterogeneities generate a distinct responsepattern as observed along the leverage ratio dimension. These findings suggest thatfirms' dependence on long term debt is an important factor in shaping the transmissionof QE shocks.7
Detailed results of these additional analyses are available from the authors upon request.
26
5 Robustness checks
In this section, we demonstrate that our main results are robust to different robustnesschecks. First, we show that placebo tests do not reproduce our baseline estimatesimplying that our insights can not be attributed to a random exposure treatment.Second, we show that the main findings remain when utilizing a IV strategy commonlyapplied in the literature.
5.1 Placebo test
The results provided in the previous sections show that firms' pricing decisions andother real outcomes are affected by their exposure to the QE program through therelationship banks. One potential concern is that the results we find are driven by othercharacteristics of the bank or the firm. In this section, we present evidence against thishypothesis placebo tests. For the placebo tests, we compute two alternative measuresof QE exposures utilizing different simulations. The first measure is computed byassigning a vector of weights to each firm for their bank relationship. The weights aredrawn randomly and sum up to 1. We use the true bond sales allocation of banks inthe QE program. The second measure is computed by keeping the actual bank-firmrelationship weights but with simulated banks' QE bond sales. We draw the banks'QE bond sales amount randomly, and make sure that the total amount sums up tothe actual bond sales each month. Note that we will not change banks' participationdecision, so banks not selling bonds in a month will stay as inactive in the simulation.The estimation results when using these two alternative exposure measures are showin Figure 10.
Figure 10 shows that producer prices do not significantly respond to the randomlygenerated QE exposure measures. In particular, we do not see different price responsesfor high and low leverage firms. It is an insightful exercise because we used the truebank QE bond sales or the true bank-firm link information to simulate the firm's QEexposure. It provides another piece of evidence that the price dynamics responding to27
firms' QE exposure is not a byproduct of an unobserved aggregate trend or omittedfirm characteristics. We need both the true bank QE sales and the bank-firm link datato generate meaningful QE price responses. It holds for both the cross-sectional groupresults and the aggregate producer price pattern.
5.2 Banks' deposits and QE exposures
Past studies indicate that banks are not the main holders of outstanding governmentbonds. To participate in the QE program, banks can sell the bonds from their owngovernment bond holdings, or they sell the bonds to the central bank on behalf oftheir clients. The latter case is very common, because banks use government bondsas collateral and are usually not flexible in adjusting the holding positions. On theother hand, non-bank financial institutions such as pension funds and insurance com-panies can sell bonds to the central bank and search for higher yields elsewhere. Buttzet al. (2015) argue that the deposits created by QE transactions are an exogenoussource of variation to banks' deposits from non-bank financial institutions. To furtherdemonstrate the robustness of our results, we follow that argument and instrument thebanks' QE participation in each month with the change of deposits from other financialcompanies.
The two-stage instrumental variable regressions are
$QE_{b,t}=\alpha_{t}+\alpha_{b}+\beta\Delta Dep_{b,t}+\epsilon_{b,t}.$$\begin{matrix}y_{i,yr}&=&\alpha_{i}+\alpha_{ind,yr}+\delta\sum_{yr}E\hat{xpo_{i,t}+\gamma X_{i,yr-1}+\epsilon_{i,yr}&$ •
(5)
(6)
where $\hat{Expo_{i,t}=\sum_{b}\omega_{i,b,t_{0}}\cdot\hat{QE_{b,t}$ is the weighted QE participation amounts fitted usingthe monthly changes of other financial institutions' deposits $\Delta Dep_{b.t}$. The instrumentalvariable regression provides evidence on the bank lending channel under the assumptionthat the sales of government bonds by other financial institutions will create newdeposits in the banking sector. However, we hold the view that these deposits willnot leave banks immediately, because the Swedish financial institutions with a strong28
-.04
-.02
0
.02PPI Inflation
04
언
Figure 10: placebo tests: firm price responses to simulated QE exposures
We plot the firms' price responses to two simulated QE exposure measures. Panels on the left shows theresults for QE measures with simulated bank-firm link weights and real bank QE purchases. Panels on theright present the results for QE measures with simulated banks' QE sales amounts and the real bank-firmrelationship. The first row shows the aggregate price responses, and the second row shows the separateprice reactions for firms with high / low leverage ratio.
+
QEExpo_Amount_Rand
0
2
6
8
10
12
Month
QEExpo_Amount_Rand
-.006
-.004
-.002
PPI Inflation
-.01
-.005
0
.005
01
0
.002
.004
0
2
QEExpo_Amount_Bank
6Month
8
10
12
QEExpo Amount Bank
0
2
4
8
10
12
0
2
4
Month
6Month
8
10
12
Low Leverage (Long)
High Leverage (Long)
Low Leverage (Long)
High Leverage (Long)
29
home bias could re-invest in domestic financial assets through the same relationship
bank. The deposits change, as a proxy, measures how much the banks could benefitfrom the additional deposits.
Table 5: Bank QE and other financial institutions' deposits
|  | (1) | (2) | (3) | (4) |
| --- | --- | --- | --- | --- |
|  |  |  | $QE_{b,t}$ |  |
| $\Delta Dep_{b,t}$ | 19.3324 | 26.8157* | 26.3202* | 21.8071* |
|  | (21.0176) | (15.4104) | (15.3994) | (12.3934) |
| Treasury Holding |  | -0.0234 |  |  |
|  |  | (2.5327) |  |  |
| No of obs | 235 | 235 | 235 | 235 |
| Adj. R2 | -0.002 | 0.534 | 0.537 | 0.658 |
| F-stat. | 0.846 | 5.413 | 5.529 | 11.359 |
| Bank FE | NO | YES | YES | NO |
|  | NO | YES | YES | YES |
| Time FEBank-Year FE | NO | NO | NO | YES |
| Standard Errors | ROBUST | ROBUST | ROBUSTROBUST |  |

(1)
(2)
(3)
(4)
$QE_{b,t}$
$\Delta Dep_{b,t}$
19.3324
26.8157*
26.3202*
21.8071*
(21.0176)
(15.4104)
(15.3994)
(12.3934)
Treasury Holding
-0.0234
(2.5327)
No of obs
235
235
235
235
Adj. R2
-0.002
0.534
0.537
0.658
F-stat.
0.846
5.413
5.529
11.359
Bank FE
NO
YES
YES
NO
NO
YES
YES
YES
Time FEBank-Year FE
NO
NO
NO
YES
Standard Errors
ROBUST
ROBUST
ROBUSTROBUST
Notes: This table reports the results of regression 5 in the paper, with dependent variables as monthly QEallocated amount for each bank. We include a few fixed effects, and the key independent variable changesof other financial companies' deposits. Robust standard errors are reported in parentheses. ***, and ***indicate statistical significance at the 10%, 5%, and 1% level, respectively.
We show the first stage regression results in Table 5. The changes of other finan-cial institutions' deposits are positively correlated with the banks' QE activities, aspresented in columns (2)-(4). It suggests that banks' deposits from other financialinstitutions increase after the QE sales. We also tried to include the changes of banks'own treasury holdings as an additional control variable. The banks' bond holding po-sitions coefficient is not statistically significant. It supports the common view thatbanks are acting as the intermediary for their customers to get engaged in the centralbank government bond purchase program. We take the fitted QE amount for eachbank from the first stage regressions and use them to compute the measure of firms'QE exposure through their relation banks. The results of the corresponding secondstate regressions are presented in Table 6. We find that the main results of the IVregressions are similar to the OLS results of our baseline specification. The estimatedcoefficients on firms' QE exposure are smaller, but still statistically significant.
We further demonstrate the robustness of the firms' price responses to QE if we
30
Table 6: Firm debts and QE exposures: two-stage regressions
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| --- | --- | --- | --- | --- | --- | --- |
|  | Tot Debt | Tot Debt | LT Debt | LT Debt | ST Debt | ST Debt |
| $Expo_{i,t}$ | $0.0163^{**}$ | 0.0137 | $0.0140^{**}$ | $0.0183^{**}$ | 0.0095 | 0.0069 |
|  | (0.0076) | (0.0095) | (0.0070) | (0.0090) | (0.0081) | (0.0097) |
| Cash flow/ Total liab. | 0.0011 | 0.0030 | -0.0186 | -0.0136 | 0.0033 | 0.0030 |
|  | (0.0238) | (0.0232) | (0.0157) | (0.0109) | (0.0240) | (0.0230) |
| Labour cost / revenue | 0.1184 | 1.3090 | 0.0482 | 0.3279 | 0.0943 | 1.1209 |
|  | (0.0844) | (1.1435) | (0.0609) | (0.9448) | (0.0699) | (0.9093) |
| Working capital / revenue | -0.0021 | -0.0049* | -0.0009 | -0.0017 | -0.0013 | -0.0031* |
|  | (0.0014) | (0.0026) | (0.0010) | (0.0022) | (0.0009) | (0.0017) |
| Inventory / revenue | 0.0252 | 0.0436* | 0.0149 | 0.0183 | 0.0189 | 0.0404* |
|  | (0.0196) | (0.0243) | (0.0124) | (0.0188) | (0.0151) | (0.0212) |
| Current liab. / revenue | -0.0007 | -0.0033 | -0.0003 | -0.0010 | -0.0005 | -0.0025 |
|  | (0.0005) | (0.0023) | (0.0003) | (0.0020) | (0.0003) | (0.0018) |
| No of obs | 9013 | 8239 | 9015 | 8241 | 9013 | 8239 |
| Adj. R2 | 0.774 | 0.783 | 0.771 | 0.771 | 0.738 | 0.748 |
| Control | YES | YES | YES | YES | YES | YES |
| Firm FE | YES | YES | YES | YES | YES | YES |
| Ind. FE | YES | NO | YES | NO | YES | NO |
| Time FE | YES | NO | YES | NO | YES | NO |
| Ind-Time FE | NO | YES | NO | YES | NO | YES |
| Cluster SE | IND | FIRM | IND | FIRM | IND | FIRM |

(1)
(2)
(3)
(4)
(5)
(6)
Tot Debt
Tot Debt
LT Debt
LT Debt
ST Debt
ST Debt
$Expo_{i,t}$
$0.0163^{**}$
0.0137
$0.0140^{**}$
$0.0183^{**}$
0.0095
0.0069
(0.0076)
(0.0095)
(0.0070)
(0.0090)
(0.0081)
(0.0097)
Cash flow/ Total liab.
0.0011
0.0030
-0.0186
-0.0136
0.0033
0.0030
(0.0238)
(0.0232)
(0.0157)
(0.0109)
(0.0240)
(0.0230)
Labour cost / revenue
0.1184
1.3090
0.0482
0.3279
0.0943
1.1209
(0.0844)
(1.1435)
(0.0609)
(0.9448)
(0.0699)
(0.9093)
Working capital / revenue
-0.0021
-0.0049*
-0.0009
-0.0017
-0.0013
-0.0031*
(0.0014)
(0.0026)
(0.0010)
(0.0022)
(0.0009)
(0.0017)
Inventory / revenue
0.0252
0.0436*
0.0149
0.0183
0.0189
0.0404*
(0.0196)
(0.0243)
(0.0124)
(0.0188)
(0.0151)
(0.0212)
Current liab. / revenue
-0.0007
-0.0033
-0.0003
-0.0010
-0.0005
-0.0025
(0.0005)
(0.0023)
(0.0003)
(0.0020)
(0.0003)
(0.0018)
No of obs
9013
8239
9015
8241
9013
8239
Adj. R2
0.774
0.783
0.771
0.771
0.738
0.748
Control
YES
YES
YES
YES
YES
YES
Firm FE
YES
YES
YES
YES
YES
YES
Ind. FE
YES
NO
YES
NO
YES
NO
Time FE
YES
NO
YES
NO
YES
NO
Ind-Time FE
NO
YES
NO
YES
NO
YES
Cluster SE
IND
FIRM
IND
FIRM
IND
FIRM
Notes: This table reports the results of regression 4 in the paper, with dependent variables as logarithmvalue of total bank debt (Tot Debt), short-term bank debt (ST Debt), and long-term bank debt (LT Debt).We include a few commonly used firm level control variables in the regression, with one period lag. Notethat the results are robust to removing the additional controls and with/without standard error clustering.Industry-level (IND) or Firm-level clustered standard errors are reported in parentheses. ***, and ***indicate statistical significance at the 10%, 5%, and 1% level, respectively.
31
어
20
PPI Price Level
Figure 11: Producer prices and fitted QE exposure
0
2
4
6Month
8
10
12
-.05
05
PPI Price Level
0
2
4
6Month
8
10
12
Low Leverage
High Leverage
use the fitted QE amount from the instrumental variable regressions. We take theweighted QE participation amounts, fitted in the regression (5), and run the samelocal projection as in (2). We can see from Figure 11 that the price responses aresimilar to the main results as shown in Section 4.1. Producer prices increase as aresponse to higher exposure to QE through firms' relationship banks. There is strongheterogeneity in the price response for firms with high and low leverage. As shown inthe right panel of Figure 11, we can see that the instrumental variable regression fittedQE exposures generate clear differences in firms' pricing responses with high leveragefirms significantly increasing their prices whereas low leverage firms do not significantlychange prices.
It is important to note that we cannot conclude that the bank lending channelunderlies these results. There are other potential explanations which are in line withour empirical findings as well. For instance, if other financial institutions' depositsmove out of the financial intermediaries, the investors might purchase other longerterm bonds issued by the corporate sector, as they are searching for yields or theyare looking for exposure to certain duration risk. If we assume that the banks act asthe intermediary for the corporate bond issuance and purchase, we capture the effectof portfolio rebalancing of the large financial institutions. Given the importance ofrelationship banking and modern full-service banking, it is plausible that the bank'scustomers are likely to use other services provided by their relationship banks.
32
6 Conclusion
We have presented new empirical evidence on the inflationary effect of QE using admin-istrative Swedish data. Our results indicate that QE has led to a significant increasein producer prices. However, we detect strong heterogeneities across firms' pricing de-cisions following the unconventional monetary policy intervention. In particular, highleverage firms significantly increase prices whereas low leverage firms do not show atendency to significantly change their prices. Further, firm level regressions confirmthat high leverage firms borrow more long-term credit from banks and thus face asignificant increase in interest rate expenses following the QE intervention. Thus, theyexperience higher borrowing costs which might explain their price increase. Investmentin R&D, machines, and equipment by low leverage firms increases which helps them toincrease productivity. In addition, it enables low leverage firms to gain higher profitsand revenues while increasing their market share.
Our study contributes to the literature by investigating firms' product price adjust-ments responding to QE, with a micro database that links bank-firm-product price dataand proprietary QE program auction information. The granularity of the data allow usto document, for the first time, that firms' price setting decisions are influenced by theirQE program exposure through their relationship banks. The main channel tends tocome from the bank lending expansion in longer-term debt. The significant differencein price responses across high and low leverage firms is less pronounced when lookingat conventional interest rate policy interventions. Future research can be extended toexamine the employer-employee links and the consequential household welfare reactionto QE activities.
33
References
Acharya, V. V., T. Eisert, C. Eufinger, and C. Hirsch (2019). Whatever it takes:The real effects of unconventional monetary policy. Review of Financial Studies 32,3366-3411.
Amberg, N., T. Jansson, M. Klein, and A. R. Picco (2021). Five facts about thedistributional income effects of monetary policy shocks. American Economic Review:Insights, forthcoming.
Bernanke, B. S., A. S. Blinder, et al. (1988). Credit, money, and aggregate demand.American Economic Review 78(2), 435-439.
Boeckx, J., M. de Sola Perea, and G. Peersman (2020). The transmission mechanismof credit support policies in the euro area. European Economic Review 124, 103403.
Bowman, D., F. Cai, S. Davies, and S. Kamin (2015). Quantitative easing and banklending: Evidence from japan. Journal of International Money and Finance 57,15-30.
Buttz, N., R. Churmz, M. McMahon, A. Morotzz, and J. Schanz (2015). QE and theBank Lending Channel in the United Kingdom. Economic Research Papers 270021,University of Warwick.
Carlstrom, C. T., T. S. Fuerst, and M. Paustian (2017). Targeting long rates in amodel with segmented markets. American Economic Journal: Macroeconomics 9,205-42.
Cui, W. and V. Sterk (2021). Quantitative easing with heterogeneous agents. Journalof Monetary Economics 123, 68-90.
Driscoll, J. C. and A. C. Kraay (1998). Consistent Covariance Matrix Estimation WithSpatially Dependent Panel Data. The Review of Economics and Statistics 80(4),549-560.
34
D'Acunto, F., R. Liu, C. Pflueger, and M. Weber (2018). Flexible prices and leverage.Journal of Financial Economics 129, 46-68.
Ehrmann, M. and M. Fratzscher (2004). Taking stock: Monetary policy transmissionto equity markets. Journal of Money, Credit and Banking, 719-737.
Fabo, B., M. Jančoková, E. Kempf, and Luboš Pástor (2021, 5). Fifty shades ofqe: Comparing findings of central bankers and academics. Journal of MonetaryEconomics 120, 1-20.
Gambacorta, L., B. Hofmann, and G. Peersman (2014). The effectiveness of unconven-tional monetary policy at the zero lower bound: A cross-country analysis. Journalof Money, Credit and Banking $46(4)$, 615-642.
Gertler, M. and P. Karadi (2015). Monetary policy surprises, credit costs, and economicactivity. American Economic Journal: Macroeconomics 7, 44-76.
Gertler, M. and P. Karadi (2018). Qe 1 vs. 2 vs. 3...: A framework for analyzinglarge-scale asset purchases as a monetary policy tool. 29th issue (January 2013) ofthe International Journal of Central Banking.
Gilchrist, S., R. Schoenle, J. Sim, and E. Zakrajšek (2017). Inflation dynamics duringthe financial crisis. American Economic Review 107, 785-823.
Gorodnichenko, Y. and M. Weber (2016). Are sticky prices costly? evidence from thestock market. American Economic Review 106(1), 165-99.
Grimm, N., L. Laeven, and A. A. Popov (2021). Quantitative easing and corporateinnovation.
Ippolito, F., A. K. Ozdagli, and A. Perez-Orive (2018). The transmission of mone-tary policy through bank lending: The floating rate channel. Journal of MonetaryEconomics 95, 49-71.
35
Jarociński, M. and P. Karadi (2020). Deconstructing monetary policy surprises the
role of information shocks. American Economic Journal: Macroeconomics 12, 1-43.
Jordà, O. (2005). Estimation and inference of impulse responses by local projections.American Economic Review 95(1), 161-182.
Joyce, M. and M. Spaltro (2014). Quantitative easing and bank lending: a panel dataapproach.
Kim, R. (2021). The effect of the credit crunch on output price dynamics: The cor-porate inventory and liquidity management channel. The Quarterly Journal of Eco-nomics 136(1), 563-619.
Klenow, P. J. and O. Kryvtsov (2008). State-Dependent or Time-Dependent Pricing:Does it Matter for Recent U.S. Inflation?*. The Quarterly Journal of Economics 123,863-904.
Lenza, M., H. Pill, L. Reichlin, and M. Ravn (2010). Monetary policy in exceptionaltimes [with discussion]. Economic Policy 25, 295-339.
Lewis, D. J. (2019). Announcement-specific decompositions of unconventional mone-tary policy shocks and their macroeconomic effects. Staff Report 891.
Morais, B., J.-L. Peydró, J. Roldán-Peña, and C. Ruiz-Ortega (2019). The internationalbank lending channel of monetary policy rates and qe: Credit supply, reach-for-yield,and real effects. The Journal of Finance 74 (1), 55-90.
Renkin, T. and G. Zuellig (2023). Credit supply shocks and prices: Evidence fromdanish firms. American Economic Journal: Macroeconomics, forthcoming.
Rodnyansky, A. and O. M. Darmouni (2017). The effects of quantitative easing onbank lending behavior. The Review of Financial Studies 30 (11), 3858-3887.
Sims, E. and J. C. Wu (2021). Evaluating central banks' tool kit: Past, present, andfuture. Journal of Monetary Economics 118, 135-160.
36
Recent Working Papers:
For a complete list of Working Papers published by Sveriges Riksbank, see www.riksbank.se
| The Macroeconomic Effects of Trade Tariffs: Revisiting the Lerner Symmetry Resultby Jesper Lindé and Andrea Pescatori | 2019:363 |
| --- | --- |
| Biased Forecasts to Affect Voting Decisions? The Brexit Caseby Davide Cipullo and André Reslow | 2019:364 |
| The Interaction Between Fiscal and Monetary Policies: Evidence from Swedenby Sebastian Ankargren and Hovick Shahnazarian | 2019:365 |
| Designing a Simple Loss Function for Central Banks: Does a Dual Mandate Make Sense?by Davide Debortoli, Jinill Kim and Jesper Lindé | 2019:366 |
| Gains from Wage Flexibility and the Zero Lower Boundby Roberto M. Billi and Jordi Galí | 2019:367 |
| Fixed Wage Contracts and Monetary Non-Neutralityby Maria Björklund, Mikael Carlsson and Oskar Nordström Skans | 2019:368 |
| The Consequences of Uncertainty: Climate Sensitivity and Economic Sensitivity to the Climateby John Hassler, Per Krusell and Conny Olovsson | 2019:369 |
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
2019:369
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
| When domestic and foreign QE overlap: evidence from Swedenby Paola Di Casola and Pär Stockhammar | 2021:404 |
| Dynamic Macroeconomic Implications of Immigrationby Conny Olovsson, Karl Walentin, and Andreas Westermark | 2021:405 |
| Revisiting the Properties of Moneyby Isaiah Hull and Or Sattath | 2021:406 |
| The cost of disinflation in a small open economy vis-à-vis a closed economyby Oleksandr Faryna, Magnus Jonsson and Nadiia Shapovalenko | 2021:407 |
| The low-carbon transition, climate commitments and firm credit riskby Sante Carbone, Margherita Giuzio, Sujit Kapadia, Johannes Sebastian Krämer, Ken Nyholm andKatia Vozian | 2022:409 |
| Seemingly Irresponsible but Welfare Improving Fiscal Policy at the Lower Boundby Roberto M. Billi and Carl E. Walsh | 2022:410 |
| Pension Reform and Wealth Inequality: Evidence from Denmarkby Torben M. Andersen, Joydeep Bhattacharya, Anna Grodecka-Messi and Katja Mann | 2022:411 |

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
When domestic and foreign QE overlap: evidence from Swedenby Paola Di Casola and Pär Stockhammar
2021:404
Dynamic Macroeconomic Implications of Immigrationby Conny Olovsson, Karl Walentin, and Andreas Westermark
2021:405
Revisiting the Properties of Moneyby Isaiah Hull and Or Sattath
2021:406
The cost of disinflation in a small open economy vis-à-vis a closed economyby Oleksandr Faryna, Magnus Jonsson and Nadiia Shapovalenko
On the Performance of Cryptocurrency Fundsby Daniele Bianchi and Mykola Babiak
2021:407
2021:408
The low-carbon transition, climate commitments and firm credit riskby Sante Carbone, Margherita Giuzio, Sujit Kapadia, Johannes Sebastian Krämer, Ken Nyholm andKatia Vozian
2022:409
Seemingly Irresponsible but Welfare Improving Fiscal Policy at the Lower Boundby Roberto M. Billi and Carl E. Walsh
2022:410
Pension Reform and Wealth Inequality: Evidence from Denmarkby Torben M. Andersen, Joydeep Bhattacharya, Anna Grodecka-Messi and Katja Mann
2022:411
| Inflation Targeting or Fiscal Activism?by Roberto M. Billi | 2022:412 |
| --- | --- |
| Trading volume and liquidity provision in cryptocurrency marketsby Daniele Bianchi, Mykola Babiak and Alexander Dickerson | 2022:413 |
| DISPERSION OVER THE BUSINESS CYCLE: PASSTHROUGH, PRODUCTIVITY, AND DEMANDby Mikael Carlsson, Alex Clymo and Knut-Eric Joslin | 2022:414 |
| Electoral Cycles in Macroeconomic Forecastsby Davide Cipullo and André Reslow | 2022:415 |
| The Curious Incidence of Monetary Policy Across the Income Distributionby Tobias Broer, John Kramer and Kurt Mitman | 2022:416 |
| Central Bank Mandates and Monetary Policy Stances: through the Lens of Federal Reserve Speechesby Christoph Bertsch, Isaiah Hull, Robin L. Lumsdaine, and Xin Zhang | 2022:417 |
| The Political Costs of Austerityby Ricardo Duque Gabriel, Mathias Klein and Ana Sofia Pessoa | 2022:418 |
| Central bank asset purchases: Insights from quantitative easing auctions of government bondsby Stefan Laséen | 2023:419 |
| Greenflation?by Conny Olovsson and David Vestin | 2023: |
| Effects of foreign and domestic central bank government bond purchases in a small open economyDSGE model: Evidence from Sweden before and during the coronavirus pandemicby Yildiz Akkaya, Carl-Johan Belfrage, Paola Di Casola and Ingvar Strid | 2023:421 |
| Dynamic Credit Constraints: Theory and Evidence from Credit Lines*by Niklas Amberg, Tor Jacobson, Vincenzo Quadrini and Anna Rogantini Picco | 2023:422 |
| CBDC: Lesson from a Historical Experienceby Anna Grodecka-Messi and Xin Zhang | 2023:424 |
| Do Credit Lines Provide Reliable Liquidity Insurance? Evidence from Commercial-Paper Backup Linesby Niklas Amberg | 2023:425 |
| Price Pass-Through Along the Supply Chain: Evidence from PPI and CPI Microdataby Edvin Ahlander, Mikael Carlsson and Mathias Klein | 2023:426 |
| Cash for Transactions or Store-of-Value? A comparative study on Sweden and peer countriesby Carl Andreas Claussen, Björn Segendorf and Franz Seitz | 2023:427 |
| Fed QE and bank lending behaviour: a heterogeneity analysis of asset purchasesby Marianna Blix Grimaldi and Supriya Kapoor | 2023:428 |
| Monetary policy in Sweden after the end of Bretton Woodsby Emma Bylund, Jens Iversen and Anders Vredin | 2023:429 |
| Banking Without Branchesby Niklas Amberg and Bo Becker | 2024:430 |
| Climate impact assessment of retail payment servicesby Niklas Arvidsson, Fumi Harahap, Frauke Urban and Anissa NurdiawatiFour Facts about International Central Bank Communicationby Christoph Bertsch, Isaiah Hull, Robin L. Lumsdaine, and Xin Zhang | 2024:431 |
| Optimal Monetary Policy with r* < 0by Roberto Billi, Jordi Galí, and Anton Nakov | 2024:433 |
| Quantitative Easing, Bond Risk Premia and the Exchange Rate in a Small Open Economyby Jens H. E. Christensen and Xin Zhang | 2024:434 |
| Supply-Chain Finance: An Empirical Evaluation of Supplier Outcomesby Niklas Amberg, Tor Jacobson and Yingjie Qi | 2024:435 |
| Optimal Contracts and Inflation Targets Revisitedby Torsten Persson and Guido Tabellini | 2024:436 |
| Potential Climate Impact of Retail CBDC Modelsby Niklas Arvidsson, Fumi Harahap, Frauke Urban and Anissa Nurdiawati | 2024:437 |
| Do we need firm data to understand macroeconomic dynamics?by Michele Lenza and Ettore Savoia | 2024:438 |

Inflation Targeting or Fiscal Activism?by Roberto M. Billi
2022:412
Trading volume and liquidity provision in cryptocurrency marketsby Daniele Bianchi, Mykola Babiak and Alexander Dickerson
2022:413
DISPERSION OVER THE BUSINESS CYCLE: PASSTHROUGH, PRODUCTIVITY, AND DEMANDby Mikael Carlsson, Alex Clymo and Knut-Eric Joslin
2022:414
Electoral Cycles in Macroeconomic Forecastsby Davide Cipullo and André Reslow
2022:415
The Curious Incidence of Monetary Policy Across the Income Distributionby Tobias Broer, John Kramer and Kurt Mitman
2022:416
Central Bank Mandates and Monetary Policy Stances: through the Lens of Federal Reserve Speechesby Christoph Bertsch, Isaiah Hull, Robin L. Lumsdaine, and Xin Zhang
2022:417
The Political Costs of Austerityby Ricardo Duque Gabriel, Mathias Klein and Ana Sofia Pessoa
2022:418
Central bank asset purchases: Insights from quantitative easing auctions of government bondsby Stefan Laséen
2023:419
Greenflation?by Conny Olovsson and David Vestin
2023:
420
Effects of foreign and domestic central bank government bond purchases in a small open economyDSGE model: Evidence from Sweden before and during the coronavirus pandemicby Yildiz Akkaya, Carl-Johan Belfrage, Paola Di Casola and Ingvar Strid
2023:421
Dynamic Credit Constraints: Theory and Evidence from Credit Lines*by Niklas Amberg, Tor Jacobson, Vincenzo Quadrini and Anna Rogantini Picco
Stablecoins: Adoption and Fragilityby Christoph Bertsch
2023:422
2023:423
CBDC: Lesson from a Historical Experienceby Anna Grodecka-Messi and Xin Zhang
2023:424
Do Credit Lines Provide Reliable Liquidity Insurance? Evidence from Commercial-Paper Backup Linesby Niklas Amberg
2023:425
Price Pass-Through Along the Supply Chain: Evidence from PPI and CPI Microdataby Edvin Ahlander, Mikael Carlsson and Mathias Klein
2023:426
Cash for Transactions or Store-of-Value? A comparative study on Sweden and peer countriesby Carl Andreas Claussen, Björn Segendorf and Franz Seitz
2023:427
Fed QE and bank lending behaviour: a heterogeneity analysis of asset purchasesby Marianna Blix Grimaldi and Supriya Kapoor
2023:428
Monetary policy in Sweden after the end of Bretton Woodsby Emma Bylund, Jens Iversen and Anders Vredin
2023:429
Banking Without Branchesby Niklas Amberg and Bo Becker
2024:430
Climate impact assessment of retail payment servicesby Niklas Arvidsson, Fumi Harahap, Frauke Urban and Anissa NurdiawatiFour Facts about International Central Bank Communicationby Christoph Bertsch, Isaiah Hull, Robin L. Lumsdaine, and Xin Zhang
2024:431
2024:432
Optimal Monetary Policy with r* < 0by Roberto Billi, Jordi Galí, and Anton Nakov
2024:433
Quantitative Easing, Bond Risk Premia and the Exchange Rate in a Small Open Economyby Jens H. E. Christensen and Xin Zhang
2024:434
Supply-Chain Finance: An Empirical Evaluation of Supplier Outcomesby Niklas Amberg, Tor Jacobson and Yingjie Qi
2024:435
Optimal Contracts and Inflation Targets Revisitedby Torsten Persson and Guido Tabellini
2024:436
Potential Climate Impact of Retail CBDC Modelsby Niklas Arvidsson, Fumi Harahap, Frauke Urban and Anissa Nurdiawati
2024:437
Do we need firm data to understand macroeconomic dynamics?by Michele Lenza and Ettore Savoia
2024:438
| Inflation-Dependent Exchange Rate Pass-Through in Sweden: Insights from a Logistic SmoothTransition VAR Model | 2024:439 |
| --- | --- |
| by Gabriella Linderoth and Malte Meuller |  |
| Quantitative Easing and the Supply of Safe Assets: Evidence from International Bond Safety Premiaby Jens H. E. Christensen, Nikola N. Mirkov and Xin Zhang | 2024:440 |
| Bank fragility and the incentives to manage riskby Toni Ahnert, Christoph Bertsch, Agnese Leonello and Robert Marquez | 2024:441 |
| A Traffic-Jam Theory of Growthby Daria Finocchiaro and Philippe Weil | 2024:442 |
| Intertemporal MPC and Shock Sizeby Tullio Jappelli, Ettore Savoia and Alessandro Sciacchetano | 2024:443 |
| Plundered or profitably pumped-up? The effects of private equity takeoverby Anders Kärnä and Samantha Myers | 2024:444 |
| Measuring Riksbank Monetary Policy: Shocks and Macroeconomic Transmissionby Jakob Almerud, Dominika Krygier, Henrik Lundvall and Mambuna Njie | 2024:445 |
| Joint extreme Value-at-Risk and Expected Shortfall dynamics with a single integrated tail shapeparameterby Enzo D'Innocenzo, André Lucas, Bernd Schwaab and Xin Zhang | 2025:446 |

Inflation-Dependent Exchange Rate Pass-Through in Sweden: Insights from a Logistic SmoothTransition VAR Model
2024:439
by Gabriella Linderoth and Malte Meuller
Quantitative Easing and the Supply of Safe Assets: Evidence from International Bond Safety Premiaby Jens H. E. Christensen, Nikola N. Mirkov and Xin Zhang
2024:440
Bank fragility and the incentives to manage riskby Toni Ahnert, Christoph Bertsch, Agnese Leonello and Robert Marquez
2024:441
A Traffic-Jam Theory of Growthby Daria Finocchiaro and Philippe Weil
2024:442
Intertemporal MPC and Shock Sizeby Tullio Jappelli, Ettore Savoia and Alessandro Sciacchetano
2024:443
Plundered or profitably pumped-up? The effects of private equity takeoverby Anders Kärnä and Samantha Myers
2024:444
Measuring Riksbank Monetary Policy: Shocks and Macroeconomic Transmissionby Jakob Almerud, Dominika Krygier, Henrik Lundvall and Mambuna Njie
2024:445
Joint extreme Value-at-Risk and Expected Shortfall dynamics with a single integrated tail shapeparameterby Enzo D'Innocenzo, André Lucas, Bernd Schwaab and Xin Zhang
2025:446
SVERIGES
RIKSBANK
Sveriges Riksbank
Visiting address: Brunkebergs torg 11
Mail address: se-103 37 Stockholm
Website: www.riksbank.se
Telephone: +46 8 787 00 00, Fax: +46 8 21 05 31E-mail: registratorn@riksbank.se