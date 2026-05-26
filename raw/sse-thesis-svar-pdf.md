
STOCKHOLM SCHOOL OF ECONOMICS
Department of Economics
BE551 Degree Project in Economics
Spring 2024
Quantitative Easing's Effect on Inflation in the SwedishEconomy
Rasmus Bjersing (25393) and Arian Hanifi (25540)
The Swedish Riksbank is facing scrutiny because of billions of dollars in deficits incurred due to itsquantitative easing (QE) program during the COVID-19 pandemic. Quantitative easing programshave now been run in Sweden for 8 years (2015-2023), but its full effects are not yet fully understood.This SVAR/VECM analysis sets out to measure the short term effect of asset purchases on inflationin the Swedish economy. Due to instability in our data, the interpretation of effects were limited tothe acceleration rates of asset purchases and inflation. As the SVAR model produced inconclusiveresults, the final estimations were made using a VECM model. The acceleration rate of assetpurchases had a precisely estimated zero effect on the acceleration rate of inflation. This conclusionis limited by the potential of omitted variable bias and the challenges in performing the VAR modelswith multiple differencing. The potential policy implications are restricted by the acceleration rate ofinflation being less relevant for the central bank than the levels of inflation itself. Furthermore, ourthesis highlights that analyzing monetary policy effects using VAR models can be challenging duringtimes of financial instability.
Keywords: Monetary Policy, Quantitative Easing (QE), Vector Auto Regression (VAR), StructuralVector Auto Regression (SVAR), Vector Error Correction Model (VECM), Inflation, Central Banking
JEL: E52, E58, E31, C32
Supervisor: Sofia Hernnäs
Date Submitted: Maj 13, 2024
Date Examined: Maj 29, 2024
Discussants: Emma S. Johnson, Filip NymanExaminer Johanna Wallenius
Contents
| 1 Introduction | 3 |
| --- | --- |
| 2 Literature Review | 4 |
| 2.1 Previous studies | 4 |
| 3 | 5 |
| 4 | 7 |
| 4.1Macroeconomic framework. | 7 |
| 4.2 Methodology | 8 |
| 5 | 9 |
| 6 | 10 |
| Stationary Variables | 10 |
| 6.2 | 12 |
| 6.3 | 13 |
| Normality of errors | 14 |
| Multicollinearity | 14 |
| 6.6 | 15 |
| 6.7 | 15 |
| 6.8 | 15 |
| 6.9 | 15 |
| 6.10 | 16 |
| 6.11 | 17 |
| 6.12 | 18 |
| 6.13 | 18 |
| 6.14 | 20 |
| 7 | 21 |
| Conclusion | 23 |
| 9 | 26 |

1 Introduction
3
2 Literature Review
4
2.1 Previous studies
4
3
Transmission channels
5
4
Methodology
7
4.1Macroeconomic framework.
7
4.2 Methodology
8
5
Data
9
6
Empirical Analysis & Result
10
Stationary Variables
6.1
10
6.2
Cointegration
12
6.3
Lag Length
13
Normality of errors
6.4
14
Multicollinearity
6.5
14
6.6
SVAR model
15
6.7
VECM Model
15
6.8
Lag Length
15
6.9
Control Variables
15
6.10
Coefficients
16
6.11
Autocorrelation in Residuals.
17
6.12
Normality of Residuals
18
6.13
Bootstrapped Confidence Intervals
18
6.14
Impulse Response Functions
20
7
Discussion
21
Conclusion
8
23
9
AI-Appendix
26
2
1 Introduction
The Swedish Riksbank, the central bank in charge of Sweden's monetary policy, requested over 7 bil-lion dollars from the Swedish Parliament in October 2023 to cover losses primarily associated with itsquantitative easing (QE) programme (Rolander, 2023). The last few years has seen the reemergenceof high inflation throughout western economies. In December 2022, the Swedish annual inflation ratepeaked at 12.39% and stayed above 8% from June 2022 to July 2023. The last time the Swedishinflation rate was above 8% was in September 1991, during the bank, finance and property crisis inSweden of the early 1990s (OECD, 2024).
The combination of unprecedented use of QE by the Swedish Riksbank along with the peak in in-flation in the following years provides ample opportunity to estimate a potential relation between theuse of QE and inflation. Sweden's position as a small open economy, not part of the eurozone, is asetting in need of further study regarding the effects of QE, as is the need in general for QE. As anovel tool in the monetary policy toolbox for central banks, the full consequences of QE are yet to bediscovered, and opinions differ regarding the efficacy and the full impact of it.
Our objective with this study is to measure the magnitudes of the transmission channels throughwhich QE could affect inflation. Especially in the context of financial turmoil with regards to theCOVID-19 pandemic and a small open economy such as Sweden.
The analysis is performed through a Structural Vector Autoregression (SVAR) that evaluates thepotential relations between the variables over several time periods, limiting the estimated relations tothose constrained by previous economic knowledge. Using Impulse Response Functions (IRFs), theshocks between variables can be estimated over time and capture the dynamics of the transmissionchannels. This was the original methodology, which over the course of the analysis was performedto the extent it was possible but also complemented with a Vector Error Correction Model (VECM).Since QE was first used in 2015 in Sweden, the studied period is limited to 2015-2023, which coversall available data in Sweden.
Our analysis cannot confirm that QE has any effect on inflation in the short-term. Due to the non-stationarity of the variables of interest, the interpretation of our results is limited to the accelerationrate of asset purchases on the acceleration rate of inflation. For these accelerations rates, the resultwe received was precisely estimated zeros indicating no relationship between the acceleration rates.
Quantitative Easing (QE) is a monetary policy tool to mitigate distressed financial markets throughlarge-scale asset purchases and boost inflation. By expanding the central bank balance sheet, assetscan be purchased from financial institutions in uncertain financial markets. The overall effect on theinstitution is increased liquidity and an increased ability to meet capital reserve requirements. Thiseffect occurs both through the reduction of held assets, leading to lower capital reserve requirementsand the proceeds from the asset sale, increasing liquidity and the size of the capital reserve (Bank ofEngland, 2024). The measure has primarily been used as a next resort when adjusting nominal interestrates has been insufficient to combat deflation and when lack of liquidity threatens the functioningof financial markets. The zero lower bound is one such phenomenon, which is the limited effect oflowering nominal interest rates when they get close to zero. Due to practical constraints, financialinstitutions and lenders tend to not lend or borrow at negative interest rates and the effect on lendingof nominal interest rate cuts have a smaller effect than at a higher interest rate level (European CentralBank., 2019).
First implemented by Japan in the early 2000s, it has since been used by central banks all overthe world, primarily in the most serious financial crises of the 21st century, namely the 2008 GreatRecession and the economic downturn due to the COVID-19 pandemic. Apart from extensive usage
3
in the event of crises, it has been used at a smaller scale to reach the inflation target when inflation isbelow the target.
Such was the case for the Swedish Riksbank when it began its first quantitative easing programme in2015 to combat an inflation on the slightly negative (annual inflation rate of -0.3% in January 2015).Along with QE, the Swedish Riksbank notably lowered the nominal interest rate to -0.1%, a primeexample of QE's role in supporting expansionary monetary policy when nominal interest rates near orexceed zero. The Riksbank's asset purchases consisted of government bonds up until the COVID-19pandemic when securities such as covered bonds, municipal bonds and corporate bonds were also in-cluded (Swedish Riksbank, 2022). During the COVID-19 Pandemic the scale of purchases also reachedunprecedented levels (Flodén, 2022) which raised the question of the impact of the policy on the overalleconomy. The Swedish Riksbank purchases assets by expanding the Riksbank's balance sheet. Theassets and debts increase by the equivalent amount to the price of the purchased securities and istransferred directly to the counter part's deposits in RIX from the Swedish Riksbank. RIX is theSwedish Riksbank's system to facilitate payments between banks and the Swedish Riksbank (SwedishRiksbank, 2022). The Riksbank then either holds the securities throughout their maturity, or sells theassets, thereby performing Quantitative Tightening. Hence, the holdings will decrease over time unlessnew assets are acquired. When the Riksbank holds securities, they are subject to the same risks anyholder of the asset would be and risk making financial losses.
2 Literature Review
2.1
Previous studies
The literature on assessing the effects of QE on financial markets is vast, however the research on theeffect on inflation and GDP is much more limited, partly due to the increased difficulty. In generalthere are three ways of assessing the macroeconomic impact which can be seen as three steps on aspectrum ranging from data-centric to theory-based (Borio & Zabai, 2018). From the data-centricperspective, the changes in the balance sheet from the asset purchase programs are used to analyse theeffect on inflation and GDP. Commonly used models here are different forms of Vector Autoregressions.On the other side of the spectrum, the theory-based approaches construct an equilibrium model forhow the asset purchases are expected to work in the economy and from this the effects are identifiedin the system. These studies are more suitable for understanding the transmission mechanism thanthe absolute effect of the policies. In between these two approaches is a two-step process. The datais first transformed into variables and shocks that are commonly used in traditional economic models.The constructed variables are then used to identify the effect of QE on inflation and GDP (Borio &Zabai, 2018).
Studies on the effect of QE have returned inconclusive results. Some studies have shown positiveeffects on GDP and inflation (Di Casola & Stockhammar, 2022; Jomaa, 2022; Kim et al., 2023). Hal-dane et al. (2016) expand the work of Weale and Wieladek (2016) and estimate the effects of QE fora selection of countries. Based on the findings they identify two forms of QE with differing levels ofeffect. The asset purchases that were conducted for liquidity purposes appear to have minimal effect.In comparison the asset purchases that were part of a loosening of monetary policies had a significantimpact on activity and prices. Furthermore, the size of the impact of QE is generally hard to esti-mate. Williams (2014) suggests that the uncertainty regarding the the effects of QE is twice as highin comparison with the effect of conventional monetary policy. Analyses of large-scale asset purchaseprograms are often conducted under the order of central banks, which is a potential source of bias;Fabo et al.'s (2021) show that central bank research generally shows a greater effect of QE on the
4
economy than studies conducted by academia.
An article that is often referenced in the literature is Weale and Wieladek's (2016) study on theeffect of large-scale asset purchases in the UK and US between 2009 to 2014 using a Bayesian VAR(BVAR) model. Instead of using actual asset purchases, announcements about the purchases by thecentral banks are used as a proxy. Four identification schemes are constructed for disentangling theorthogonal and structural shocks in the residuals. They find that an asset purchase announcement of1% of nominal GDP leads to a maximum impact of 0.62% (0.25%) on real GDP and 0.58% (0.32%)on CPI in the US (UK).
The role of QE and its effect on the economy in Sweden have only been analysed in a few stud-ies. This could partly be accredited to it being a new field of study as the Riksbank's first large-scaleasset purchase program was put in effect in 2015 (Riksbank, 2024). Jomaa (2022) looked at the assetpurchase program of the Riksbank between 2015 and 2018 and estimated the effects on inflation us-ing a Structural Vector Autoregressive (SVAR) model. The result of her study showed that an assetpurchase the size of 1% of GDP had a maximum effect of 0.3923%. The study also identifies thesignalling channels as the main mediator of the effect of QE on the economy.
Di Casola and Stockhammar (2022) argue that as Sweden is a small economy it is affected by shocksin its main trading partners based on a study by Corbo and Strid (2020). Thus they analyse theeffect of large-asset purchases by both the Riksbank and the European Central Bank (ECB) on outputand inflation in Sweden from 2015 to 2018 with a Bayesian Vector Autoregressive (BVAR) model. Interms of the effect of Domestic QE,i.e. the Riksbank, on inflation, the results are not clear as the68% confidence interval includes zero. However, the simultaneous QE program of the ECB had largepositive spillover effects on both output and inflation. A share of the positive effect was mediatedthrough the response of domestic QE to the foreign QE.
A study on the Swedish QE using a small open economy two-region dynamic stochastic general equi-librium model (DSGE) suggested that the purchases increased GDP by 0.2% and inflation by 0.25percentage points on average in 2020-2023. Of the total effect, circa half could be accredited to thepurchases of municipal and covered bonds half. They also argue that the estimates are likely a lowerbound as they do not capture that the asset purchases reduced the risk of a financial crisis happening(Akkaya et al., 2023).
Kim et al. (2023) analyse the effect of the Federal Reserve's large-scale asset purchases (LSAPs)with a SVAR model. Instead of using the size of the central bank's balance sheet or the announcedasset purchases they utilise a survey-based approach to capture the expectation of the public. Theanalysis shows that a surprise \$500 billion asset purchase had a peak effect on the level of industrialproduction by about 2% and on the level of the CPI by about 0.8%, while reducing the unemploymentrate by about 0.5 percentage points. However there are uncertainties on the accuracy of the estimatesas the 68% confidence intervals of the impulse response functions, although zero-excluded, are quitewide.
3 Transmission channels
Understanding through what mechanisms large-scale asset purchases affect the economy is of greatimportance for central banks, in particular when there are multiple monetary policies in place. There isno clear answer to this from either a theoretical or practical perspective. The nature of the transmissionis still a subject of debate in the literature. However, a transmission scheme commonly referred to isthe one Haldane et al. (2016) proposes as seen in Figure 2.
5
5. Confidence
AssetPurchases
Money
5. Risk aversion/uncertainty
1. Policysignalling
2. Portfoliorebalancing:DurationLocalsupply
4. Exchangerate
Relativeasset prices
Total wealth
3. Liquidity
6. Banklending
Cost ofborrowing
Spendingand income
Inflationand growth
Figure 1: Transmission Channels Flow Chart
The main paths for the transmission can be narrowed down to:
- monetary policy signalling channel
- portfolio balance channel
exchange rate channel
The monetary policy signalling channel is based on the idea that QE can convey information abouthow the short-term interest rates might develop. The view is that the purchases signal that the centralbanks will hold the policy interest rate at its lower rate for longer (Weale & Wieladek, 2016). Sincethe asset purchases happen under a longer period, often several years, it is the announcement of themthat give rise to the signalling effect. The longer time span is also a part of why it signals how thefuture short-term rates are going to develop.
The portfolio balance channel functions through market frictions due to imperfect asset substitutabil-ity. The large-scale purchases of long-term bonds by the central bank push up the price of assetsbought and thus reduce the yield of them. Due to investors having a preferred-habitat demand, thatis to say a preference for bonds of specific maturities, they do not see bonds of different maturities asperfect substitutes. Thus some investors rebalance their allocation of different assets and money. Thisleads to an increased demand for long-term bonds which drives up the prices and in turn lowers theyields (Bernanke et al., 2004; Jomaa, 2022).
The idea behind the exchange rate channel is that QE lowers the price of domestic assets comparedto foreign assets (Di Casola & Stockhammar, 2022). The asset purchases increase the price of domes-tic bonds which in turn reduces the bond yield of the bonds making them less attractive for foreigninvestors. Lower demand for domestic bonds leads to a depreciation of the currency (Neely & Fawley,2013). A depreciation in the domestic currency makes domestic goods and services cheaper relative toforeign alternatives which increases demand and leads to an increased inflation (Glick & Leduc, 2013).
6
For each of the transmission channels to be effective they are dependent on the assumption thatthere are certain frictions in the financial market. Without these frictions the effect of asset purchaseson asset pricing would be near non-existent (Haldane et al., 2016; Wallace, 1979).
Studies on the effect of quantitative easing in Sweden have suggested that the announcements bythe Riksbank have had effects through the above mentioned channels. The announcements lead tolower long-term government, corporate, mortgage bond yields. The mediation through the exchangerate channel could be seen via the weakened exchange rate. For the signalling channel the lower interestrate expectations at different horizons indicate that it also had a role in the transmission (De Rezende,2017).
4 Methodology
4.1
Macroeconomic framework
The macroeconomic framework we use to analyse the effect of QE on inflation are Vector Autoregres-sions (VARs) as introduced by Sims (1980). A VAR is an n-equation, n-variable linear model whereeach variable is modelled by its own lagged values and the current and past values of the remainingvariables (J. H. Stock & Watson, 2001). This framework allows for a systematic approach of examin-ing the dynamic relationships that exist between variables that interact with each other and as suchare often used as a credible method for data description, forecasting, structural inference and policyanalysis (J. H. Stock & Watson, 2001). VARs can generally be found in three different forms: reduced,recursive, and structural form. We will describe the structural form, also known as Structural VectorAutoregression SVAR, as that model is used in our analysis. For readers interested in learning moreabout the other models we refer to Vector Autoregressions (J. H. Stock & Watson, 2001) and thearticle by Kotzé (n.d.).
Structural Vector Autoregressions
Structural Vector Autoregressions are a form of VAR models in which there are identifying assump-tions that allow correlations across contemporaneous variables to be interpreted casually (J. H. Stock& Watson, 2001). The assumptions should be based on theory and it is up to the researcher to choosea suitable schema for this. In comparison with a VAR the SVAR, instead of identifying the coefficientsof the variables, the identification is imposed on the errors of the system which can be interpretedas exogenous shocks (Lütkepohl & Krätzig, 2004). Framing it differently, SVAR models decomposethe effects of each variable into an expected and an unexpected part, and then impose the identifyingrestrictions on only the unexpected parts (Gottschalk, 2001). To estimate a SVAR model, a reducedform VAR model is first estimated by using OLS per equation. Thereafter, the identifying scheme isapplied to the coefficients and residuals from the equation above. This results in orthogonal residualsor error shocks as they are also referenced to as (Gottschalk, 2001). For the OLS estimators to beconsistent the following assumptions have to be fulfilled; No perfect multicollinearity, the error termhas a conditional mean of zero given all regressors and their lags, the variables follow a stationarydistribution, and large outliers are unlikely (J. Stock & Watson, 2015).
Vector Error Correction Model
When the variables are co-integrated the resulting values from a VAR model will not be precise asthere is a long-run trend that is not taken into consideration. To solve this a Vector error correctionmodel (VECM) can be used. The difference compared to a VAR model is that an error correctingterm is added which represents the long-term relationship between the variables (Ren et al., 2020).
7
4.2 Methodology
Following the approach of Jomaa (2022) and Weale and Wieladek (2016) we construct our VAR asfollows:
$Y_{t}=\alpha_{x}+\sum_{k=1}^{L}A_{k}Y_{t-k}+e_{t},$ $e_{t}\sim N(0,\Sigma)$
$Y_{t}$ is a vector containing our endogenous variables: GDP Indicator, Consumer Price Index, SwedishKrona real effective exchange rate, and the term spread between 10-year and 3-month governmentbond yields. $A_{k}$ is the vector of coefficients for the corresponding lagged variables for lag k. $e_{t}$ is thevector of residuals at time t. L is the lag length.
Determining the optimal lag can be done based on economic theory and previous studies, or differentforms of information criteria such as Akaike Information Criterion (AIC) and Bayesian InformationCriterion (BIC) (Jomaa, 2022; Lütkepohl, 1991). The number of lags affects the performance of themodel: too many lags lead to forecasting errors and omitting lags can lead to estimation bias (Jomaa,2022). For this study we evaluate several information criteria for optimal lag length selection includingthose Jomaa (2022) or Weale and Wieladek (2016) resulting in running the following tests: BayesianInformation Criterion (BIC), Akaike Information Criterion (AIC), Hannan-Quinn Criterion (HQ). Fi-nally, the HQ Criterion is selected for determining the lag length.
Identification Scheme
Table 1: Identifying restrictions for the baseline model. Cholesky Decomposition Scheme
|  | Log CPI | GDP-indicator | Asset Purchases | Term Spread | Log Exchange Rates | STIBOR |
| --- | --- | --- | --- | --- | --- | --- |
| Log CPI | 1 | 0 | 0 | 0 | 0 | 0 |
| GDP-indicator |  | 1 | 0 | 0 | 0 | 0 |
| Asset Purchases |  |  | 1 | 0 | 0 | 0 |
| Term Spread |  |  |  | 1 | 0 | 0 |
| Log Exchange Rates |  |  |  |  | 1 | 0 |
| STIBOR |  |  |  |  |  | 1 |

Log CPI
GDP-indicator
Asset Purchases
Term Spread
Log Exchange Rates
STIBOR
Log CPI
1
0
0
0
0
0
GDP-indicator
1
0
0
0
0
Asset Purchases
1
0
0
0
Term Spread
1
0
0
Log Exchange Rates
1
0
STIBOR
1
Inspired by earlier studies (Jomaa, 2022; Weale & Wieladek, 2016) the identification scheme utilisedin the analysis is based on the Cholesky Decomposition Scheme. As seen in Table 1 the scheme usesa lower-triangular scheme, with log CPI appearing first, followed by real GDP, asset purchases, andthen the remaining variables. This implies that the identifying assumptions are that real GDP andCPI react with a lag and that aside from responding to these two, asset purchases do not react to anyother variable (Weale & Wieladek, 2016). According to Weale and Wieladek's (2016), identificationschemes that are constructed using timing exclusion restrictions have been criticised because similarrestrictions are not found when employing DSGE models. Therefore, to include such restrictions therehas to be strong theoretic support. To justify the scheme, Weale and Wieladek (2016) present earlierstudies showing that an increase in asset purchases will lead to lower interest rates on long term bonds.Similarly Jomaa (2022) argues that the term spread, exchange rates and the 1-month STIBOR raterespond immediately when the announcement of asset purchases is made public. It is worth mentioningthat designing an identification scheme that can identify asset purchase announcements perfectly ischallenging as the economic theory underlying the mechanism of asset purchases is not understoodvery well currently (Weale & Wieladek, 2016).
8
5 Data
| Variable | Description | Source |
| --- | --- | --- |
| GDP Indicator | Serves as a proxy for economic activity. Usedto estimate impact on the economy. | Statistics Sweden |
| Log(ConsumerPriceIndex) | Used to estimate the impact on inflation. | Statistics Sweden |
| 1-month STIBOR Rate | Used to examine the signalling effect of QE oninterest rate expectations. | Riksbank |
| Term Spread | Difference between the 10-year and the 3-month government bond yields. Measures theportfolio balance channel | Riksbank |
| Log(Real EffectiveExchange Rate) | Measures the exchange rate transmission mech-anism. | Bank for InternationalSettlements (BIS) |
| Cumulative Asset Pur-chases | The ratio of cumulative announced purchasesby the Riksbank to the annualised nominalGDP as of December 2014 is measured. | Riksbank |

Variable
Description
Source
GDP Indicator
Serves as a proxy for economic activity. Usedto estimate impact on the economy.
Statistics Sweden
Log(ConsumerPriceIndex)
Used to estimate the impact on inflation.
Statistics Sweden
1-month STIBOR Rate
Used to examine the signalling effect of QE oninterest rate expectations.
Riksbank
Term Spread
Difference between the 10-year and the 3-month government bond yields. Measures theportfolio balance channel
Riksbank
Log(Real EffectiveExchange Rate)
Measures the exchange rate transmission mech-anism.
Bank for InternationalSettlements (BIS)
Cumulative Asset Pur-chases
The ratio of cumulative announced purchasesby the Riksbank to the annualised nominalGDP as of December 2014 is measured.
Riksbank
Table 2: Description and Source of Variables used in the Analysis of QE Effects
The data used in the model is aggregated at a monthly level for the time period ranging from 2015 upuntil and including 2023. An overview of the variables can be seen in Table 2. This period includesall asset purchase announcements by the Riksbank up until the moment of the writing of this article.
For the variable of most interest in the report, the measure of QE, we follow the approach of thearticles by Jomaa (2022), and Di Casola and Stockhammar (2022) which in turn are inspired by Wealeand Wieladek (2016). The measure is defined as the cumulative amount of announced asset purchasesdivided by the annualised nominal GDP of December 2014, the last period before the start of the QE
ogram. This is done to eliminate endogeneity effects coming from effects of QE on contemporaneousGDP levels (Di Casola & Stockhammar, 2022; Jomaa, 2022). We use announcements as a proxy sinceour model assumes that changes in the macroeconomic variables are responses to the announcementsrather than actual asset purchases. As Laséen (2023) mentions, analysing the assets purchases ofcentral banks rather than the announcements is a complex task due to the built in endogenous natureof central bank purchase operation.
The term spread variable is the difference between the 10-year and 3-month government bond yields.Previous studies argue that the existence of the portfolio balance channel can be seen from a reducedor negative term spread. The rationale is that the portfolio rebalancing leads to a large impact on thelong-term bonds and reduces the term premia (Jomaa, 2022; Weale & Wieladek, 2016). The data isacquired from the Riksbank.
The real effective exchange rate is acquired from the Bank for International Settlements (BIS) and iscalculated with regard to a basket of 27 countries. The weights for calculating the effective exchangerate come from the manufacturing trade flows amongst the countries (Bank for International Settle-ments, 2023). This variable is used to capture the exchange rate transmission channel. As mentionedin the description of the transmission mechanism the hypothesis is that if QE is mediated through thischannel then the domestic currency should depreciate and the exchange rate decrease.
9
The 1-month STIBOR rate is included to examine the portfolio signalling effect. The role of swaprates for this purpose has appeared in several previous studies (Weale & Wieladek, 2016). ΕΟΝΙΑswap rates and the London Interbank Offered Rate, LIBOR, have been used when analysing the assetpurchases of the European Central bank and the United Kingdom central bank respectively (Haldaneet al., 2016). As the corresponding instrument in Sweden is the Stockholm Interbank Offered Rate,STIBOR, we select it as the proxy for the signalling effect (Jomaa, 2022). The role of the variable isto capture how the expectations of economic agents shift after an asset purchase announcement. SinceQE informs that the policy rates will remain low in the short-term this should be reflected in changesin the rate of the STIBOR instrument.
The GDP-indicator is used as a proxy for economic activity and inflation is the change in CPI. Bothvariables are acquired from the Statistical Database which is maintained by Statistics Sweden.
6 Empirical Analysis & Result
6.1
Stationary Variables
When performing a Vector Auto Regression model, the included variables need to be stationary forthe model's assumption to hold. A stationary variable is one for which the mean, variance and co-variance are constant over time. If the sample variable is not shown to be stationary through anAugmented Dickey-Fuller (ADF) test, it needs to be differenced, i.e. each data point is obtained bysubtracting one years observation with the previous year's. A variable's integration order is determinedas the number of differencings needed to be performed for the resulting variable to become stationary.Note that for each differencing one degree of freedom is lost and it is generally recommended not todifference to higher than the second order, to prevent losing to much information in the variable fromthe differencing.
Table 3: ADF Test
| Variable | Integration Order | p-value |
| --- | --- | --- |
| GDP | 1 | 0.4406 |
| Log (Consumer |  |  |
| Price Index | 3 | 0.9478 |
| (Log(CPI)) |  |  |
| 1-month | 1 | 0.7578 |
| Term Spread | 1 | 0.9883 |
| Log (Real Effective | 1 | 0.3385 |
| Cumulative Asset Purchases Ratio | 3 | 0.8617 |

Variable
Integration Order
p-value
GDP
1
0.4406
Log (Consumer
Price Index
3
0.9478
(Log(CPI))
1-month
STIBOR Rate
1
0.7578
Term Spread
1
0.9883
Log (Real Effective
Exchange Rate)
1
0.3385
Cumulative Asset Purchases Ratio
3
0.8617
Notes:
Table 3 shows the integration order of each variable and p-values for the original variable, obtained from the ADF-test.A p-value lower than 5% means we can reject the null hypothesis of non-stationarity at a 95% confidence level.
10
20
10
Cumulative Asset Purchases relative to GDP 2015
0
2015
2016
2017
2018
2019
2020Log(Consumer Price Index)
2021
2022
2023
2024
Year
6.0
5.9
5.8
0.02
0.01
0.00
-0.01
2015
2016
2017
2018
2019
2020
2021
3 times differenced Cumulative Asset Purchases relative to GDP 2015
2022
2023
2024
Year
иммунпримиримирири
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
3 times differenced Log(Consumer Price Index)
Year
8
6
4-
2
0
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024 Year
Figure 2: An overview of the variables in need of 3 levels of differencing
We observe that none of the variables are stationary (Table 3), and that the logarithmically trans-formed CPI variable and the Asset Purchases variable are integrated at order 3 which poses the riskof information being lost in the differencing. We can see from Figure 2 that there is a steady rise inthe $Log(CPI)$ variable, accelerating in 2022 and a sharp rise in the Cumulative Asset Purchases Ratiobetween 2020 and 2021, underlining the non-stationarity of those variables. The rest of the variablesare integrated at order 1.
11
Table 4: Result from ADF test on time-range used in Jomaa (2022)
| Variable | Integration Order |
| --- | --- |
| GDP | 1 |
| Log (Consumer |  |
| Price Index | 1 |
| 1-month |  |
| STIBOR Rate | 1 |
| Term Spread | 0 |
| Log (Real Effective | 1 |
| Cumulative Asset Purchases Ratio | 0 |

Variable
Integration Order
GDP
1
Log (Consumer
Price Index
(Log(CPI))
1
1-month
STIBOR Rate
1
Term Spread
0
Log (Real Effective
Exchange Rate)
1
Cumulative Asset Purchases Ratio
0
Notes:
Table 4 shows the integration order of each variable for the time period 2015-2018 studied by Nora Jomaa
From the results in Table 4 we can observe that the integration order of the variable is no problem forthe period studied by Jomaa (2022), spanning from 2015 to 2018, which indicates that the selectedperiod to study may have influenced the appropriateness of the SVAR model.
6.2 Cointegration
We performed an Engle-Granger Cointegration Test for each pair of variables with the same integrationorder. Here the non-differenced variables are used. co-integrated variables have a linear combination ofthem which is stationary, which implies they have a long-term relationship with each other. Performingthe cointegration tests for variables of different integration order would complicate interpretation andis not in line with the assumptions of Engle-Granger Cointegration Test nor standard practice, henceonly those variables of the same integration order are tested. If the model does not take account ofthat relationship, the short-term statistical inference is weakened as the long-term effect can influencethe short-term effects estimated by the model. This long-term effect can be accounted for with anerror-correction term which would extend the VAR-model into a Vector Error Correction (VECM)model.
Table 5: Engle-Granger Test
|  | GDP | 1-monthSTIBOR Rate | Term Spread | Log (RealEffective |
| --- | --- | --- | --- | --- |
| GDP |  | 0.1652 | 0.4957 | 0.1033 |
| 1-monthSTIBOR Rate | 0.1652 |  | 0.3173 | 0.3890 |
| Term spread | 0.4957 | 0.3173 |  | 0.6735 |
| Log (Real EffectiveExchange Rate) | 0.1033 | 0.3890 | 0.6735 |  |

GDP
1-monthSTIBOR Rate
Term Spread
Log (RealEffective
Exchange Rate)
GDP
0.1652
0.4957
0.1033
1-monthSTIBOR Rate
0.1652
0.3173
0.3890
Term spread
0.4957
0.3173
0.6735
Log (Real EffectiveExchange Rate)
0.1033
0.3890
0.6735
Notes:
Table 5 displays the calculated p-values for the Engle-Granger Test for the variables of integration order 1. A p-valuelower than 0.05 leads to a rejection of the null-hypothesis of two variables not being co-integrated. Each value in thetable corresponds to this p-value between the variables given by the cell's row and column indexes.
12
For the variables integrated at order 1, the p-values are larger than 0.05 and no significant valuescan be found (Table 5). Hence the null hypothesis of no co-integration can not be rejected and noco-integration is presumed.
Table 6: Engle-Granger TestNotes:
| p-value | Log (CPI) |
| --- | --- |
| Cumulative Asset Purchases Ratio | 0.0163 |

p-value
Log (CPI)
Cumulative Asset Purchases Ratio
0.0163
Table 6 displays the calculated p-values for the Engle-Granger Test for the variables of integration order 3. A p-valuelower than 0.05 leads to a rejection of the null-hypothesis of two variables not being co-integrated. Each value in thetable corresponds to this p-value between the variables given by the cell's row and column indexes.
The p-value of the ADF-test on the residuals of the regression of the variables (calculated in the Engle-Granger Test, is lower than 0.05. Hence at a 95% confidence we can conclude that log(CPI) and AssetPurchases are co-integrated at integration order 0.
6.3 Lag Length
For the lag length, a variety of optimisation criteria were attempted. The selection of lag length isa crucial step in performing a SVAR since the lag length is the amount of past observations used topredict current values. Higher lag length increases the risk of overfitting and reducing the degrees offreedom. On the other hand, a too short length may lead to missing significant important relationships.These tradeoffs are handled differently in different criteria that seek to balance these tradeoffs. In thisanalysis Bayesian Information Criterion (BIC), Akaike Information Criterion (AIC), Hannan-QuinnCriterion (HQ) and Final Prediction Error Criterion (FPE) are tested. Their main differences are theseverity of the penalty imposed by increasing the length where their severity from conservative to lessconservative (in terms of penalising higher lag length more) is BIC, HQ, AIC. In essence, BIC tends toprefer a shorter length than AIC. BIC and HQ vary with regards to sample size where large samplesize leads to more conservative lag length selection, AIC and FPE are less variable with regards to thesample size. FPE is explicitly focused on prediction accuracy, whereas BIC, HQ and AIC are based onlikelihood principles. These criteria were applied to a VAR model without the structural componentin order to find the optimal lag length for the SVAR model.
Table 7: Different Criteria for Optimal Lag Length
| Criteria | Optimal Lag Length |
| --- | --- |
| Bayesian Information Criterion(BIC) | 0 |
| Akaike Information Criterion (AIC) | * |
| Hannan-Quinn Criterion (HQ) | * |
| Final Prediction Error Criterion(FPE) | * |

Criteria
Optimal Lag Length
Bayesian Information Criterion(BIC)
0
Akaike Information Criterion (AIC)
*
Hannan-Quinn Criterion (HQ)
*
Final Prediction Error Criterion(FPE)
*
For the BIC the optimal lag length was 0 and for the other criteria the optimal length was 14, wherenotably 14 was the highest lag length that could be attempted without the model malfunctioning. Theprocess was repeated for different ranges of potential values where the other criteria were consistentlythe maximum value in the range. We have therefore chosen to report these lag lengths as non-conclusive, indicated with $a^{*}$ in Table 7. This presents an obstacle to the use of the VAR model sincea lag length of 0 would mean no lags, making the VAR model obsolete. With this in consideration, we
13
proceeded to perform the SVAR model for all lag lengths between 0 and 14 to analyse the differencesin results.
6.4 Normality of errors
To ensure that the residuals are normally distributed we performed a Jarque-Bera test for each variablein the VAR model without the structural component, used above for finding the optimal lag length.
Table 8: Jarque-Bera Test
| Variable | p-value |
| --- | --- |
| AGDP | 0.3157 |
| A³Log (CPI) | 0.6777 |
| A1-Month STIBOR Rate | 0.0621 |
| ATerm Spread | 0.8791 |
| $\Delta Log$ (Real Effective Exchange Rate) | 0.5243 |
| A3 Cumulative Asset Purchases Ratio | 0.0057 |

Variable
p-value
AGDP
0.3157
A³Log (CPI)
0.6777
A1-Month STIBOR Rate
0.0621
ATerm Spread
0.8791
$\Delta Log$ (Real Effective Exchange Rate)
0.5243
A3 Cumulative Asset Purchases Ratio
0.0057
Notes:
Table 8 displays the p-values for each variable with the null hypothesis that the errors are normally distributed.
As seen in Table 8 $\Delta^{3}C$ Asset Purchases Ratio has a p-value of 0.0057, which is significant ata 1% significance level. Moreover, the 1-month STIBOR Rate is significant at the 10% level, meaningwe can reject the null hypothesis of the residuals being normally distributed at a 90% confidence level.For the other variables, normality of residuals can be presumed.
6.5 Multicollinearity
Another assumption for VAR models is that there is no multicollinearity between the variables. Forthis reason a Variance Inflation Factor (VIF) Test is performed.
Table 9: VIF Test
| Variable | Value |
| --- | --- |
| Intercept | 1.4342 |
| AGDP | 1.015775 |
| A³Log (CPI) | 1.066763 |
| A1-Month STIBOR Rate | 1.1167 |
| ATerm Spread | 1.0964 |
| ALog (Real Effective Exchange Rate) | 1.0751 |
| Cumulative Asset Purchases Ratio | 1.1168 |
| Notes: |  |

Variable
Value
Intercept
1.4342
AGDP
1.015775
A³Log (CPI)
1.066763
A1-Month STIBOR Rate
1.1167
ATerm Spread
1.0964
ALog (Real Effective Exchange Rate)
1.0751
Cumulative Asset Purchases Ratio
1.1168
Notes:
Table 9 displays the Variance Inflation Factors for each differenced variable
Table 9 shows the Variance Inflation Factor for each variable. A value of 1 indicates no correlationwith other variables, and a value between 1 and 4 indicates moderate correlation. A value higher than4 suggest a predictor has high correlation with the other variables and warrants further investigation(The Pennsylvania State University, 2018).
From the multicollinearity test we can see that the Variance Inflation Factor (VIF) is low, close to 1 foreach variable and quite close to 1, 1.4342 for the Intercept Term. This indicates that multicollinearityissues are not present to a large extent in our model.
14
6.6 SVAR model
Running the SVAR model, a lag length of all potential values between 0 and 14 were attempted,all rendering a warning of non-Convergence. The exact warning we received was "Convergence notachieved after 100 iterations. Convergence Value 1". The actual program was run with vars packagein R but similar programs were attempted in the python statsmodels package where similar warningswere obtained. This means that the model is not finding a way to represent the data given the modeldesign. The non-convergence means that the likelihood function being maximised by the regressionmodel is not finding a stable global maximum that best estimates the parameters, using a scoringalgorithm (R package Documentation, 2023). The resulting estimated contemporaneous relationshipsproduced by the model cannot be trusted to reflect the actual relationships. For that reason, theestimated relationships have been excluded from this analysis.
6.7 VECM Model
Following the unsuccessful estimation of the SVAR model, a VECM model was estimated. We testeda simplified model in order to provide a rough estimate of the contemporaneous relationships betweenQuantitative Easing and inflation. It can be observed from the previous analysis that the variablesof interest: Asset purchases and $log(CPI)$, are both integrated at order 3 and co-integrated at order0, indicating that there exists a long-term equilibrium relationship among them and that a linearcombination of the variables can be created of integration order 0. This type of relationship could becaptured by a Vector Error Correction Model where an error correction term is introduced to ensurethat deviations from the long-term stability are corrected over time, allowing for interpretation ofshocks at the short-term.
6.8 Lag Length
For the VECM model, the same criteria as used for the SVAR is employed.
Table 10: Different Criteria for Optimal Lag Length (VECM)
| Criteria | Optimal Lag Length |
| --- | --- |
| Bayesian Information Criterion(BIC) | 0 |
| Akaike Information Criterion (AIC) | * |
| Hannan-Quinn Criterion (HQ) | 5 |
| Final Prediction Error Criterion(FPE) | * |

Criteria
Optimal Lag Length
Bayesian Information Criterion(BIC)
0
Akaike Information Criterion (AIC)
*
Hannan-Quinn Criterion (HQ)
5
Final Prediction Error Criterion(FPE)
*
The important differing result from the previous attempt is that HQ is now 5 instead of non-conclusive,whereas the other results are the same as for the SVAR model (Table 10). For this reason 5 is chosenas the optimal lag length.
6.9
Control Variables
To determine whether control variables from the available dataset should be included, the HQ criterionwas used to evaluate the model.
15
Table 11: HQ-values for different combinations of Control Variables
| Control Variables | HQ Value |
| --- | --- |
| None | -0.25527 |
| AGDP | 1.34210 |
| ATerm Spread | 0.16765 |
| ALog (Real Effective Exchange Rate) | -0.00137 |
| A1-month STIBOR Rate | 0.09657 |
| AGDP, ATerm Spread | 2.08532 |
| AGDP, ALog (Real Effective Exchange Rate) | 1.96554 |
| AGDP, A1-month STIBOR Rate | 2.06036 |
| ATerm Spread, ALog (Real Effective Exchange Rate) | 0.74966 |
| ATerm Spread, A1-month STIBOR Rate | 0.87931 |
| ALog (Real Effective Exchange Rate), A1-month STIBOR Rate | 0.66704 |
| AGDP, ATerm Spread, ALog (Real Effective Exchange Rate) | 3.02981 |
| AGDP, ATerm Spread, A1-month STIBOR Rate | 3.29036 |
| AGDP, ALog (Real Effective Exchange Rate), A1-month STIBOR Rate | 3.02860 |
| ATerm Spread, Log (Real Effective Exchange Rate), A1-month STIBOR Rate | 1.74336 |
| All 4 | 4.52802 |

Control Variables
HQ Value
None
-0.25527
AGDP
1.34210
ATerm Spread
0.16765
ALog (Real Effective Exchange Rate)
-0.00137
A1-month STIBOR Rate
0.09657
AGDP, ATerm Spread
2.08532
AGDP, ALog (Real Effective Exchange Rate)
1.96554
AGDP, A1-month STIBOR Rate
2.06036
ATerm Spread, ALog (Real Effective Exchange Rate)
0.74966
ATerm Spread, A1-month STIBOR Rate
0.87931
ALog (Real Effective Exchange Rate), A1-month STIBOR Rate
0.66704
AGDP, ATerm Spread, ALog (Real Effective Exchange Rate)
3.02981
AGDP, ATerm Spread, A1-month STIBOR Rate
3.29036
AGDP, ALog (Real Effective Exchange Rate), A1-month STIBOR Rate
3.02860
ATerm Spread, Log (Real Effective Exchange Rate), A1-month STIBOR Rate
1.74336
All 4
4.52802
Upon testing all possible combinations of control variables, including the case of no control variablesand control variables, the lowest HQ-value was obtained as the model with no control variables (Table11). The simple model without adding the lags of other variables, was based on the HQ-criterionbalancing goodness of fit with model simplicity in the best way. There is a general risk of overfittingwith this approach, but given that the optimal set of variables obtained was the one containing thefewest variables, the risk of overfitting is mitigated.
6.10
Coefficients
Table 12: Lagged Endogenous Parameters for $\Delta^{3}Log(CPI)$
| Variable |  | Coefficient | Std. Error | z-Value | P-value | 95% Conf. Interval |
| --- | --- | --- | --- | --- | --- | --- |
| $\Delta^{3}Log(CPI)_{lag=1}$ |  | -1.2161 | 0.100 | -12.183 | 0.000 | [-1.412, -1.020] |
| A3Cumulative Asset | Purchases Ratiotag=1 | 0.0002 | 0.001 | 0.222 | 0.825 | [-0.001, 0.002] |
| $\Delta_{a}^{3}Log(CPI)_{lag=2}$ |  | -1.0152 | 0.156 | -6.497 | 0.000 | [-1.321, -0.709] |
| A3 Cumulative Asset | Purchases Ratiolag=2 | 0.0002 | 0.001 | 0.214 | 0.830 | [-0.001, 0.002] |
| $\Delta^{3}Log(CPI)_{lag=3}$ |  | -0.4801 | 0.180 | -2.673 | 0.008 | [-0.832, -0.128] |
| A3 Cumulative Asset | Purchases Ratiolag=3 | 0.0003 | 0.001 | 0.421 | 0.674 | [-0.001, 0.002] |
| $\Delta^{3}Log(CPI)_{lag=4}$ |  | -0.2191 | 0.157 | -1.400 | 0.161 | [-0.526, 0.088] |
| A3 Cumulative Asset | Purchases Ratiolag=4 | 3.823e-05 | 0.001 | 0.059 | 0.953 | [-0.001, 0.001] |
| $\Delta^{3}Log(CPI)_{lag=5}$ |  | -0.1240 | 0.097 | -1.283 | 0.200 | [-0.314, 0.065] |
| A3 Cumulative Asset | Purchases Ratiolag=5 | 0.0001 | 0.000 | 0.207 | 0.836 | [-0.001, 0.001] |

Variable
Coefficient
Std. Error
z-Value
P-value
95% Conf. Interval
$\Delta^{3}Log(CPI)_{lag=1}$
-1.2161
0.100
-12.183
0.000
[-1.412, -1.020]
A3Cumulative Asset
Purchases Ratiotag=1
0.0002
0.001
0.222
0.825
[-0.001, 0.002]
$\Delta_{a}^{3}Log(CPI)_{lag=2}$
-1.0152
0.156
-6.497
0.000
[-1.321, -0.709]
A3 Cumulative Asset
Purchases Ratiolag=2
0.0002
0.001
0.214
0.830
[-0.001, 0.002]
$\Delta^{3}Log(CPI)_{lag=3}$
-0.4801
0.180
-2.673
0.008
[-0.832, -0.128]
A3 Cumulative Asset
Purchases Ratiolag=3
0.0003
0.001
0.421
0.674
[-0.001, 0.002]
$\Delta^{3}Log(CPI)_{lag=4}$
-0.2191
0.157
-1.400
0.161
[-0.526, 0.088]
A3 Cumulative Asset
Purchases Ratiolag=4
3.823e-05
0.001
0.059
0.953
[-0.001, 0.001]
$\Delta^{3}Log(CPI)_{lag=5}$
-0.1240
0.097
-1.283
0.200
[-0.314, 0.065]
A3 Cumulative Asset
Purchases Ratiolag=5
0.0001
0.000
0.207
0.836
[-0.001, 0.001]
Notes:
$Log(CPI)$ variable and $\Delta^{3}$
$\Delta^{3}Log(CPI)$ corresponds to the three times differenced
Asset Purchases Ratio
corresponds to the three times differenced variable for Cumulative Asset Purchases Ratio
Table 12 presents the coefficients for the lags of the variables where $\Delta^{3}Log(CPI)$ is the dependentvariable. We can observe that the P-value is greater than 0.05 for all lags of Asset Purchases (Table12). Because of the transformation and differencing of the variables, the interpretation of coefficients isnontrivial. The coefficients represents the change in (the change in (the change in the logarithmicallytransformed CPI)) across 4 data points as a consequence of the change in (the change in (the increaseof Announced Asset Purchases))). Since inflation rate, thechange in $log(CPI)$ can be interpreted as the inflation rate.
$log(CPI_{t})-log(CPI_{t-1})\approx\frac{CPI_{t}-CPI_{t-1}}{CPI_{t-1}}=$
16
The interpretation of $\Delta^{3}Log(CPI)$ can hence be simplified into the the change in (the change in infla-tion) across 4 data points. This translates into the acceleration rate of inflation. For $\Delta^{3}C$
Asset Purchases Ratio, the change in the increase of announced Cumulative Asset Purchases Ratio isthe announced Asset Purchases Ratio for a specific period, hence the change in (the change in (theincrease of announced Cumulative Asset Purchases Ratio)) can be reformulated as the the change in(the change in the announced Asset Purchases). Similarly to the interpretation of $\Delta^{3}Log(CPI)$, it canbe interpreted as the acceleration rate of Asset Purchases.
It can be observed for all the lags of $\Delta^{3}C$ Cumulative Asset Purchases Ratio that the coefficients areprecisely estimated zeros for the effect of $\Delta^{3}C$ Asset Purchases Ratio on $\Delta^{3}Log(CPI)$. Thisindicates that we cannot reject our null hypothesis of no short-term effect of the acceleration rate ofAsset Purchases relative to GDP on the acceleration rate of inflation. Instead it indicates that theacceleration rate of Asset Purchases does not have an impact on the acceleration rate of inflation. Notethat the Asset purchases is rescaled by the constant of GDP in the first period meaning the coefficientsmore precisely represents the acceleration rate of Asset Purchases relative to the initial GDP on theacceleration rate of inflation.
Additionally, the acceleration rate of inflation seems to be associated with a lower future accelera-tion rate of inflation, since the coefficients are negative and statistically significant at the 5% level, forthe first three lags.
Table 13: Lagged Endogenous Parameters for $\Delta^{3}C$
Asset Purchases Ratio
| Variable | Coefficient | Std. Error | z-Value | P-value | 95% Conf. Interval |
| --- | --- | --- | --- | --- | --- |
| $\Delta^{3}Log(CPI)_{lag=1}$ | -0.8128 | 19.312 | -0.042 | 0.966 | [-38.664, 37.038] |
| Cumulative Asset | -0.5898 | 0.165 | -3.570 | 0.000 | [-0.914, -0.266] |
| $\Delta^{3}Log(CPI)_{lag=2}$ | -35.9448 | 30.230 | -1.189 | 0.234 | [-95.195, 23.306] |
| A3Cumulative Asset Purchases | -0.6240 | 0.158 | -3.951 | 0.000 | [-0.934, -0.314] |
| $\Delta^{3}Log(CPI)_{lag=3}$ | -72.3645 | 34.746 | -2.083 | 0.037 | [-140.466, -4.263] |
| A3Cumulative Asset | -0.3155 | 0.152 | -2.077 | 0.038 | [-0.613, -0.018] |
| $\Delta_{g}^{s}Log(CPI)_{lag=4}$ | -70.7157 | 30.280 | -2.335 | 0.020 | [-130.063, -11.368] |
| Cumulative Asset Purchases $Ratio_{lag=4}$ | -0.3317 | 0.125 | -2.656 | 0.008 | [-0.576, -0.087] |
| $\Delta^{3}Log(CPI)_{lag=5}$ | -52.4084 | 18.707 | -2.802 | 0.005 | [-89.073, -15.744 |
| A3 Cumulative Asset Purchases Ratiolag=5 | 0.1333 | 0.096 | 1.393 | 0.164 | [-0.054, 0.321] |

Variable
Coefficient
Std. Error
z-Value
P-value
95% Conf. Interval
$\Delta^{3}Log(CPI)_{lag=1}$
-0.8128
19.312
-0.042
0.966
[-38.664, 37.038]
Cumulative Asset
Purchases Ratiolag=1
-0.5898
0.165
-3.570
0.000
[-0.914, -0.266]
$\Delta^{3}Log(CPI)_{lag=2}$
-35.9448
30.230
-1.189
0.234
[-95.195, 23.306]
A3Cumulative Asset Purchases
$Ratio_{lag=2}$
-0.6240
0.158
-3.951
0.000
[-0.934, -0.314]
$\Delta^{3}Log(CPI)_{lag=3}$
-72.3645
34.746
-2.083
0.037
[-140.466, -4.263]
A3Cumulative Asset
Purchases $Ratio_{lag=3}$
-0.3155
0.152
-2.077
0.038
[-0.613, -0.018]
$\Delta_{g}^{s}Log(CPI)_{lag=4}$
-70.7157
30.280
-2.335
0.020
[-130.063, -11.368]
Cumulative Asset Purchases $Ratio_{lag=4}$
-0.3317
0.125
-2.656
0.008
[-0.576, -0.087]
$\Delta^{3}Log(CPI)_{lag=5}$
-52.4084
18.707
-2.802
0.005
[-89.073, -15.744
]
A3 Cumulative Asset Purchases Ratiolag=5
0.1333
0.096
1.393
0.164
[-0.054, 0.321]
Notes:
$\Delta^{3}Log(CPI)$ corresponds to the three times differenced $Log(CPI)$ variable and $\Delta^{3_{1}}$
Asset Purchases Ratio
corresponds to the three times differenced variable for Cumulative Asset Purchases Ratio
Table 13 presents the coefficients for the equation in the system where $\Delta^{3}C$ Asset PurchasesRatio is the dependent variable. Looking at the effect of the lags of in the acceleration rate of inflationon the acceleration rate of asset purchases in Table 13, the P-value for $\Delta^{3}Log(CPI)$ as the endogenousparameter is lower than 0.05 for the lags 3-5 periods back in time, namely 0.037, 0.020 and 0.005respectively. It is a reasonable finding that changes in the inflation rate can affect monetary policydecisions, since the central bank explicitly has an inflation target and adjusts its monetary policy toreach it. To interpret the exact magnitude and sign of these coefficients is a complicated task that isbeyond the scope of this study
6.11 Autocorrelation in Residuals
An important assumption in any linear regression is that the residuals are independent and identicallydistributed. If residuals are autocorrelated they are not independent and this assumption would beviolated. For that reason, a Durbin-Watson test is performed
17
|  | Table | -Watson |  |
| --- | --- | --- | --- |
| Variable | $\Delta^{3}Log(CPI)$ | $\Delta^{3}C$ | Purchases Ratio |
| DW Statistic Value | 2.0536 | 1.9547 |  |

Table
14
:
Durbin
-Watson
Test
Variable
$\Delta^{3}Log(CPI)$
$\Delta^{3}C$
Asset
Purchases Ratio
DW Statistic Value
2.0536
1.9547
Notes:
Table 14 contains the DW Statistic Value for two variables: the $\Delta^{3}Log(CPI)$ and $\Delta^{3}c$
Asset Purchases
Ratio. A DW Statistic Value between 0 and 2 suggests positive autocorrelation, a value of 2 suggests noautocorrelation, and a value between 2 and 4 suggests negative autocorrelation.
The DW Statistic values fall within the range of 1.95-2.06, close to 2, indicating no or low autocor-relation (Table 14). Hence the issues with autocorrelation for the model performance appear to below.
6.12 Normality of Residuals
A Jarque-Bera test is performed to test the normality of the residuals to interpret the confidenceintervals for the estimated parameters. The normality assumption is crucial in the calculation andinterpretation of statistics such as p-values and CI's. If the residuals are not normally distributed, it isappropriate to bootstrap the confidence intervals and interpret those, rather than the non-bootstrappedones.
| Variable | p-value |
| --- | --- |
| $\Delta^{3}Log(CPI)$ | 0.0063 |
| Asset Purchases Ratio$\Delta^{3}($ | 0.0000, $(3.6\cdot10^{-276})$ |

Variable
p-value
$\Delta^{3}Log(CPI)$
0.0063
Asset Purchases Ratio$\Delta^{3}($
0.0000, $(3.6\cdot10^{-276})$
Table 15: Jarque-Bera Test
The residuals are not normally distributed since the null hypothesis of normally distributed residualsis rejected at an at least 99% confidence for both of the variables (Table 15). Consequently, theconfidence intervals should be bootstrapped.
6.13 Bootstrapped Confidence Intervals
Table 16: 95% Confidence Intervals for Lagged Endogenous Parameters $(\Delta^{3}Log(CPI))$
| Variable | Lower Bound | Upper Bound |
| --- | --- | --- |
| $\Delta^{3}Log(CPI)_{lag=1}$ | -0.21597 | 0.22575 |
| Cumulative Asset Purchases Ratiolag=1 | -0.00141 | 0.00123 |
| $\Delta^{3}Log(CPI)_{lag=2}$ | -0.23000 | 0.19780 |
| A³Cumulative Asset Purchases Ratiolag=2 | -0.00130 | 0.00123 |
| $\Delta^{3}Log(CPI)_{lag=3}$ | -0.20725 | 0.21780 |
| Cumulative Asset Purchases $Ratio_{lag=3}$ | -0.00125 | 0.00129 |
| $\Delta^{3}Log(CPI)_{lag=4}$ | -0.21299 | 0.20893 |
| Cumulative Asset Purchases $Ratio_{lag=4}$ | -0.00114 | 0.00124 |
| $\Delta^{3}Log(CPI)_{lag=5}$ | -0.20202 | 0.22121 |
| Cumulative Asset Purchases Ratiolag=5 | -0.00124 | 0.00142 |

Variable
Lower Bound
Upper Bound
$\Delta^{3}Log(CPI)_{lag=1}$
-0.21597
0.22575
Cumulative Asset Purchases Ratiolag=1
-0.00141
0.00123
$\Delta^{3}Log(CPI)_{lag=2}$
-0.23000
0.19780
A³Cumulative Asset Purchases Ratiolag=2
-0.00130
0.00123
$\Delta^{3}Log(CPI)_{lag=3}$
-0.20725
0.21780
Cumulative Asset Purchases $Ratio_{lag=3}$
-0.00125
0.00129
$\Delta^{3}Log(CPI)_{lag=4}$
-0.21299
0.20893
Cumulative Asset Purchases $Ratio_{lag=4}$
-0.00114
0.00124
$\Delta^{3}Log(CPI)_{lag=5}$
-0.20202
0.22121
Cumulative Asset Purchases Ratiolag=5
-0.00124
0.00142
18
Table 17: 95% Confidence Intervals for Lagged Endog. Param. ( $\Delta^{3}C$
Asset Purchases Ratio)
| Variable | Lower Bound | Upper Bound |
| --- | --- | --- |
| $\Delta^{3}Log(CPI)_{lag=1}$ | -0.21129 | 0.25474 |
| A³Cumulative Asset Purchases Ratiotag=1 | -44.5254 | 43.7032 |
| $\Delta^{3}Log(CPI)_{lag=2}$ | -0.19019 | 0.24058 |
| Cumulative Asset Purchases $Ratio_{lag=2}$ | -41.5222 | 43.9989 |
| $\Delta^{3}Log(CPI)_{lag=3}$ | -0.18922 | 0.25943 |
| Cumulative Asset Purchases $Ratio_{lag=3}$ | -46.0562 | 44.4125 |
| $\Delta^{3}Log(CPI)_{lag=4}$ | -0.19635 | 0.22434 |
| Cumulative Asset Purchases $Ratio_{lag=4}$ | -41.6504 | 40.5216 |
| $\Delta^{3}Log(CPI)_{lag=5}$ | -0.17483 | 0.23498 |
| A³Cumulative Asset Purchases Ratiolag=5 | -0.15837 | 0.02709 |

Variable
Lower Bound
Upper Bound
$\Delta^{3}Log(CPI)_{lag=1}$
-0.21129
0.25474
A³Cumulative Asset Purchases Ratiotag=1
-44.5254
43.7032
$\Delta^{3}Log(CPI)_{lag=2}$
-0.19019
0.24058
Cumulative Asset Purchases $Ratio_{lag=2}$
-41.5222
43.9989
$\Delta^{3}Log(CPI)_{lag=3}$
-0.18922
0.25943
Cumulative Asset Purchases $Ratio_{lag=3}$
-46.0562
44.4125
$\Delta^{3}Log(CPI)_{lag=4}$
-0.19635
0.22434
Cumulative Asset Purchases $Ratio_{lag=4}$
-41.6504
40.5216
$\Delta^{3}Log(CPI)_{lag=5}$
-0.17483
0.23498
A³Cumulative Asset Purchases Ratiolag=5
-0.15837
0.02709
To interpret the Bootstrapped Confidence Intervals of the lagged parameters in Table 17, we observethat the lags of $\Delta^{3}$ Asset Purchases on $\Delta^{3}Log(CPI)$ are still narrow and quite similar to the onesobserved in the non-bootstrapped confidence intervals. The lower bound is no lower than -0.00141 andno higher than 0.00142 for any of the lags. This strengthens the belief that the acceleration rate ofAsset Purchases does not have an impact on the acceleration rate of inflation.
19
6.14 Impulse Response Functions
Impulse responses
3-Differenced log(CPI) on 3-Differenced log(CPI)
3-Differenced Asset Purchases on 3-Differenced log(CPI)
1.0
1.0
0.8
0.6
0.4
0.2
0.0
-0.2
0.8-
0.6-
0.4-
0.2-
0.0
-0.2-
-0.4
-0.4
Periods
3-Differenced log(CPI) on 3-Differenced Asset Purchases
60
60-
40
20
0
-20
-40
-60
--
<--
40-
20
0
-20
-40
-60-
Periods
3-Differenced Asset Purchases on 3-Differenced Asset Purchases
-80
-80
0
10
20
30
40
50Periods
0
10
20
30
40
50Periods
Figure 3: Impulse Response Function for the VECM
Over 48 periods, i.e. 4 years, it can be observed that the shocks in $\Delta^{3}Log(CPI)$ caused by shocks in$\Delta^{3}C$ Asset Purchases Ratio, if any, have a very small magnitude compared to that of for ex-ample $\Delta^{3}Log(CPI)$ on itself (Figure 3). This indicates that shocks in the change of the acceleration rateof Asset Purchases do not generate shocks in the acceleration rate of inflation. The confidence interval,the estimated shocks and the zero-line are indistinguishable on the scale used for $\Delta^{3}Log(CPI)$ on itself.
By analysing the IRF's we observe that the shocks in the acceleration rate of inflation are smallif any and close to zero for all periods.
20
7
Discussion
In the following section, we will discuss potential reasons for which our attempt to estimate the SVARmodel were unsuccessful.
First, we discuss the integration order and cointegration of our variables of interest. Thereafter,we discuss the COVID-19 pandemic and its multi-faceted impact on the economy. Thirdly, we dis-cuss whether asset purchase announcements is the correct variable of interest, Moreover, we discusswhether Sweden's position as a small open economy and the Riksbank's other policies contributed tothe difficulties in our estimation strategy. Finally, we discuss how and if we can compare our resultsto previous studies.
Our variable representing Cumulative Asset Purchases was calculated cumulatively and relative toGDP in the first period. The purpose of this is rescaling the variable, capture the full effect of theasset purchases with regards to how they are aggregately affecting inflation and that spikes in a yearmay not be indicative of the total effect QE has had over several periods. Upon performing the ADF-test, Cumulative Asset Purchases was shown to be non-stationary up to a third level of differencing.The same integration order of 3 was found for the the logarithmically transformed Consumer PriceIndex variable. The Swedish inflation rate during the studied period also saw clear outliers comparedto the previous years. Additionally, the usage of QE shifted more towards minimising financial turmoilduring the pandemic and the range of securities was expanded, further complicating the dynamics ofAsset Purchases and inflation captured by the data.
An integration order of three presents significant challenges for a VAR-model, an integration orderover 2 can be seen as problematic since each level of differencing leads to a potential loss of informa-tion when constant terms are removed. The Engle-Granger Test identified a cointegrating relationshipbetween the Cumulative Asset Purchase Ration and inflation, which indicates a significant long termrelationship between our Cumulative Asset Purchases Ratio and inflation. This contravenes the VARmodel assumption that variables differenced at the same order are not co-integrated. Additionally,the integration order of our Cumulative Asset Purchases Ratio and inflation is three, compared toone, for our other variables used to analyse the transmission channels. The combination of havingsome variables of integration order 3, co-integrated at order 0 and variables of integration order 1, notco-integrated makes a structural VECM complicated to perform. Such an analysis would be beyondthe scope of our thesis and due to time constraints and lack of experience dealing with such specialcases, the full SVECM is not attempted.
The unprecedented usage of QE during the COVID-19 pandemic and the high levels of inflation be-tween 2021 and 2023 are potential reasons for the problematic features of the variables. This presentsa dilemma since the usage of QE during the COVID-19 pandemic and the subsequent inflation wastwo events that we hoped could inform the short-term relationships between Asset Purchases and in-flation. In essence, the outliers in the data contained valuable information that we did not want to lose.
During the two quantitative easing programs in Sweden there were many different shocks than just theasset purchases. The COVID-19 pandemic had a huge effect on the economy which was then followedby the Ukraine Russia war and disruptions in global supply chains. As the nature and interplay of eco-nomic entities change when the macroeconomic environment shifts the effect of QE might change. Forexample, an article from the UN suggests that QE might have been less effective during the COVID-19pandemic since QE mainly relaxes financial constraints at the bank level rather than at the firm level(Rashid & Pitterle, 2022). All of which might have contributed to difficulties in assessing the casualimpact of QE.
21
Using announcements as a proxy for the expectations of asset purchases might not give a correctestimate of the thoughts of the economic agents. Kim et al. (2023) argue that announcements failto capture that all following announcements will be expected to some extent and thus the shock inpractice will not be as large as the size of the announcement. An alternative approach would have beento follow the approach of Kim et al. (2023) and gauge the expectations by analysing survey answers.
To attempt to estimate the contemporaneous relationships, despite the limitations to the interpre-tation of highly differenced variables and the violation of the existence of cointegrating relationshipsbetween variables of the same order, a VAR model is fitted to apply different criteria to identify theoptimal lag length for the SVAR model. Our findings are another sign of non-perfect model specifica-tion since the BIC suggests 0 lags and the other information criteria suggest the maximal amount oflags without the model crashing. We proceed with the non-conclusive lag length and decide to test allpossible values without the model crashing which for all specified lag lengths lead to the same problemof non-convergence for the model. This can occur when the model specification is not appropriately inalignment with the actual structure of the data, which we have received several indications of already.We therefore label the entire SVAR model as inconclusive.
Furthermore, as Corbo and Strid (2020) present, Sweden is a small open economy that is affectedby shocks in its main trading partners. This includes Quantitative Easing programs conducted byother central banks which have been shown to have an effect on the Swedish economy. Di Casola andStockhammar (2022) found that the quantitative easing conducted by the European Central Bank,ECB, had positive spillover effects mediated partly through the response of the Swedish asset purchaseprogramme to the actions of the ECB. Since we do not include the ECB asset purchases in our modelwe cannot exclude the fact that our results are biased.
Swedish monetary policy did not only consist of asset purchasing during the period. Aside fromother conventional monetary policies, there were other unconventional tools used simultaneously. TheRiksbank was one of the first central banks to introduce a negative exchange rate in 2015 and the firstto abandon it in 2019 (Andersson & Jonung, 2020). Although some studies have tried to account forthis such as Jomaa (2022) who included an additional variable for controlling for the monetary policyrate, we believe that a simple approach like this won't be able to capture the complex effect it has onthe economy.
The key finding of the analysis is the precisely estimated zeros for the lags of $\Delta^{3}C$ Cumulative As-set Purchases Ratio on $\Delta^{3}Log(CPI)$. The interpretation of the differenced variables was approximatedto the acceleration rate of Asset Purchases on the acceleration rate of inflation. The preciseness of thezeros was supported by a closer examination of the confidence intervals of the parameter estimates.We observed from the Jarque-Bera test of the variables in our reduced VECM model that the variablesare not normally distributed at a 1% significance level, and the bootstrapped confidence intervals weresimilar to the non-bootstrapped CI's with a range smaller than 0.003 around 0 for all lags. This couldbe seen as that the changes of the rate at which the announcements of QE are changed, how fast theSwedish Riksbank changes the amount of QE that is announced, appears to have no effect on howfast inflation changes. The shocks in $\Delta^{3}Log(CPI)$ from the shocks in $\Delta^{3}C$Asset PurchasesRatio are indistinguishable from zero in the IRF's which strengthens the belief that the accelerationrate of Asset Purchases does not affect the acceleration rate of inflation.
Due to the limitations mentioned above it is difficult to compare our results with previous studies.Focusing on the studies on QE in Sweden there is no study that spans over the second QE program,ranging from 2020 and onwards. This is of interest as the problems with non-stationarity at higherintegration order starts in 2019. When performing the stationarity test for the data spanning from2015-2018 we get a maximum integration order of 1 for certain variables similar to the numbers inJomaa's (2022) study. Di Casola and Stockhammar (2022) also note that some variables may contain
22
unit roots. They include the variables in levels instead of differentiating, They refer to Hamilton (1994)who suggests to run the VAR in levels as running it in first difference would take away the trends. Intheir study they do not present what integration order the different variables have which would havebeen interesting to see. Since the integration orders for our data ranged between 0 to 3 and the generalassumptions of the SVAR models and the presence of cointegration relationships, we did not followthat approach. Instead we choose to use a VECM model, with the variables of integration order 3differentiated three times.
The plan of the study was to also examine through which channels the effect of QE is transmit-ted. However, due to the aforementioned change of model to a VECM with a third-order differentiatedversion of the asset announcement variable any impulse response function derived from the modelwould have limited implications. Specially since the variables representing the different transmissionchannels would have been differentiated to different levels. This in combination with the the resultfrom the HC criterion test for model selection lead to the exclusion of those variables.
8 Conclusion
This thesis sets out to investigate the short-term effects of Asset Purchases on inflation in Sweden.The results of the SVAR-model were inconclusive, the model did not converge. One potential expla-nations for this was the cointegration relationship we identified between variables differenced multipletimes. We obtained another indication of the model specification being non-ideal, in the optimal laglength calculation the results were unreasonable on both the low and high end, 0 and the maximumvalue. Based on these findings we decided not to pursue the SVAR model further and interpret theIRF's and coefficients. Since the variables in the focus of the study, asset purchases and inflation,were non-stationary at such high levels of differencing, we had no choice but to abandon our originalhypothesis of asset purchases having a short term-effect on inflation.
In the light of these findings, we performed a VECM where only the variables of interest were in-cluded. A comparison using the HQ-criterion was used to inform the selection of control variables.The coefficients of our VECM, analysed with bootstrapped confidence intervals showcased preciselyestimated zeros for the effect of the acceleration rate of Asset Purchases on the acceleration rate ofinflation. Similar findings were obtained when analysing the IRF plots, the confidence intervals andestimated shocks were indistinguishable from zero.
Our reduced VECM model lacks the robustness provided by the Cholesky-Decomposition schemefor the SVAR-model, incorporating previous findings in to the model. There is a risk of omitting im-portant variables, especially as Sweden's role as an open economy in the EU means domestic economicconditions are affected by monetary policy decisions by the European Central Bank or any entity ittrades significantly with. This reduces the weight that can be put to these precisely estimated zeros.
Additionally, the interpretation of the acceleration rates in the concerned variable is hard to translateinto a practical implication for the monetary policy decision makers. What the analysis would suggestis that, since the effect between the acceleration rates appear to be near zero, the decision makersshould perhaps not be concerned with acceleration rates of inflation and Asset Purchases and focusmore on the actual effect between the variables. This was the original intention of the study. It alsosuggests that SVAR models can become difficult to use for analysis of the effects of a monetary policydecision if the study period contains substantial financial turmoil.
23
References
Akkaya, Y., Belfrage, C.-J., Casola, P. D., & Strid, I. (2023). Staff memo: The macroeconomic effectsof Riksbank asset purchases during the pandemic simulations using a DSGE model (tech. rep.).Riksbanken.
Andersson, F. N. G., & Jonung, L. (2020). Lessons from the swedish experience with negative central
bank rates. Cato Journal, (2020:15).
Bank for International Settlements. (2023). Real effective exchange rates [Access to data on nomi-nal and real effective exchange rates for 64 economies, providing measures of internationalcompetitiveness and the impact of external shocks. Updated monthly and daily, reflectingtime-varying trade-based weights.]. https://data.bis.org/topics/EER
Bank of England. (2024). Quantitative easing. Retrieved April 2, 2024, from https://www.bankofengland.co.uk/monetary-policy/quantitative-easingBernanke, B. S., Reinhart, V. R., & Sack, B. P. (2004). Monetary policy alternatives at the zero bound:An empirical assessment (tech. rep. No. 2). Brookings Institution Press. http://www.jstor.org/stable/3805105
Borio, C., & Zabai, A. (2018, May). Unconventional monetary policies: A re-appraisal. In P. Conti-Brown & R. M. Lastra (Eds.), Research Handbook on Central Banking. Edward Elgar Pub-lishing. https://doi.org/10.4337/9781784719227.00026
Corbo, V., & Strid, I. (2020). Maja: A two-region dsge model for sweden and its main trading partners(Sveriges Riksbank Working Paper Series No. 391). Sveriges Riksbank.
De Rezende, R. B. (2017). The interest rate effects of government bond purchases away from the lower
bound. Journal of International Money and Finance, 74, 165-186.
Di Casola, P., & Stockhammar, P. (2022). When Domestic and Foreign QE Overlap: Evidence from
Sweden (tech. rep.). https://doi.org/10.2139/ssrn.4156196
European Central Bank. (2019). Is there a zero lower bound?: The effects of negative policy rates onbanks and firms. Publications Office. Retrieved April 2, 2024, from https://data.europa.eu/doi/10.2866/23378
Fabo, B., Jančoková, M., Kempf, E., & Pástor, L. (2021). Fifty shades of QE: Comparing find-ings of central bankers and academics [Publisher: Elsevier]. Journal of Monetary Economics,120(100), 1-20. Retrieved April 1, 2024, from https://ideas.repec.org//a/eee/moneco/v120y2021icp1-20.html
Flodén, M. (2022, December 14). Mina tankar kring riksbankens tillgångsköp. Retrieved April 29, 2024,from https://www.riksbank.se/globalassets/media/tal/svenska/floden/2022/floden-bilder-mina-tankar-kring-riksbankens-tillgangskop.pdf
Glick, R., & Leduc, S. (2013). The effects of unconventional and conventional u.s. monetary policy onthe dollar (Working Paper No. 11). Federal Reserve Bank of San Francisco.Gottschalk, J. (2001). An introduction into the svar methodology: Identification, interpretation and lim-itations of svar models (Kiel Working Papers No. 1072). Kiel Institute for the World Economy(IfW Kiel).
Haldane, A., Roberts-Sklar, M., Young, C., & Wieladek, T. (2016). QE: The Story so Far. SSRNElectronic Journal. https://doi.org/10.2139/ssrn.2858204
Hamilton, J. D. (1994). Time series analysis. Princeton University Press.
Jomaa, N. (2022). The Effects of Quantitative Easing on Swedish Inflation: An empirical study of theswedish riksbank's quantitative easing programme between 2015-2019 [Master's thesis, LundUniversity].
Kim, K., Laubach, T., & Wei, M. (2023). Macroeconomic Effects of Large-Scale Asset Purchases: NewEvidence. Finance and Economics Discussion Series, (2020-047r1), 1-89. https://doi.org/10.17016/feds.2020.047r1
Kotzé, b. K. (n.d.). Vector autoregression models. Retrieved April 28, 2024, from https://kevinkotze.github.io/ts-7-var/
24
Laséen, S. (2023). Central bank asset purchases: Insights from quantitative easing auctions of govern-ment bonds (Sveriges Riksbank Working Paper Series No. 419). Sveriges Riksbank.Lütkepohl, H. (1991). Introduction to multiple time series analysis (1st ed.). Springer. https://link.
springer.com/book/10.1007/978-3-662-02691-5
Lütkepohl, H., & Krätzig, M. (Eds.). (2004). Applied time series econometrics. Cambridge UniversityPress.
Neely, C., & Fawley, B. (2013). Four stories of quantitative easing. Federal Reserve Bank of St. Louis
Review, 95, 51-88. https://doi.org/10.20955/r.95.51-88
OECD. (2024). Consumer price indices oecd data explorer. Retrieved March 30, 2024, from https://data-explorer.oecd.org/?fs[0]=Topic%2C1%7CEconomy%23ECO%23%7CPrices%23ECO_PRI%23&pg=0&fc=Topic&bp=true&snb=30
R package Documentation. (2023). SVAR: Estimation of a SVAR in vars: VAR Modelling. RetrievedApril 29, 2024, from https://rdrr.io/cran/vars/man/SVAR.html
Rashid, H., & Pitterle, I. (2022, February). UN DESA policy brief no. 129: The monetary policy re-sponse to covid-19: The role of asset purchase programmes. https://www.un.org/development/desa/dpad/publication/un-desa-policy-brief-no-129-the-monetary-policy-response-to-covid-19-the-role-of-asset-purchase-programmes/
Ren, X., Shao, Q., & Zhong, R. (2020). Nexus between green finance, non-fossil energy use, and carbonintensity: Empirical evidence from China based on a vector error correction model. Journal ofCleaner Production, 277, 122844. https://doi.org/10.1016/j.jclepro.2020.122844
Riksbank, S. (2024, May 2). Government bonds. Retrieved May 5, 2024, from https://www.riksbank.se/en-gb/markets/the-riksbanks-securities-holdings/government-bonds/Rolander, N. (2023, October 24). Sweden Riksbank Needs More Than \$7 Billion to Cover LossesBloomberg. Retrieved April 1, 2024, from https://www.bloomberg.com/news/articles/2023-10-24/riksbank-says-it-will-need-more-than-7-billion-to-cover-losses
Sims, C. A. (1980). Macroeconomics and reality. Econometrica, 48(1), 1-48. http://www.jstor.org/stable/1912017
Stock, J. H., & Watson, M. W. (2001). Vector Autoregressions. Journal of Economic Perspectives,15(4), 101-115. https://doi.org/10.1257/jep.15.4.101
Stock, J., & Watson, M. (2015). Introduction to Econometrics. Pearson.Swedish Riksbank. (2022). Riksbankens balansräkning har vuxit. Retrieved March 30, 2024, from
https://www.riksbank.se/sv/press-och-publicerat/publikationer/ekonomiska-kommentarer/riksbankens-finansiella-resultat-och-kapital-paverkas-av-hogre-rantor/riksbankens-balansrakning-har-vuxit/
The Pennsylvania State University. (2018). 10.7 Detecting Multicollinearity Using Variance InflationFactors STAT 462. Retrieved April 28, 2024, from https://online.stat.psu.edu/stat462/node/180/
Wallace, N. (1979). A Modigliani-Miller Theorem for Open-Market Operations [Publisher: FederalReserve Bank of Minneapolis], (131). https://jstor.org/stable/community.28111527
Weale, M., & Wieladek, T. (2016). What are the macroeconomic effects of asset purchases? Journalof Monetary Economics, 79, 81-93. https://doi.org/10.1016/j.jmoneco.2016.03.010Williams, J. C. (2014). Monetary policy at the zero lower bound: Putting theory into practice (tech.rep.).
25
9 AI-Appendix
Purpose and Usage
A Generative AI tool, ChatGPT, has been used for the following purposes:
- Understand warnings and errors in code
- Receive suggestions on how to improve specific paragraphs in the text.Specifically, the warning messages of non-convergence produced by the SVAR model was sent to Chat-GPT for investigation along with a few errors in running the code, obtained when conducting theanalysis. To improve the text, after a paragraph was written, it was in some cases sent in to Chat-GPT with an instruction to provide suggestions on how to improve logical flow, enhance grammaticalstructure and point out needed clarifications. Rather than replacing text with the models suggestedversion, this was used to get insight into what improvements could be made and modifications weremade based on the authors personal taste.
Impact
By explaining the cause of a few errors in the code, the causes of the problems were identified morequickly and thereby increased the speed at which the code could be written. The analysis of thewarning message was informative although it didn't lead to any fundamental insight. With regards toimproving paragraphs, it was helpful to get another perspective on the content and did lead to clearerformulations and structure of paragraphs in some cases.
Mitigation of Risks
Understanding errors and warnings was overall quite fruitful and is an example of a low risk usage.If the code is not working, an incorrect pinpoint of cause of the error will not break the code buta successful identification of the cause will considerably help the development. The main potentialrisk in this regard would be to rely on the model for implementing fixes of the code since the modelmight remove the error but change the functionality of the code. To mitigate this, the model was usedexclusively to identify causes of errors.
Since the paragraphs of the text were interconnected in terms of the content, it was difficult forthe model to accurately get the full context of the paragraph. Moreover, ChatGPT and GenerativeAI models in general are known to be uncertain in their outputs, to hallucinate. Based on these twofactors, considerable precaution was taken on not relying on the model's recommendation withoutcritical analysis.
Insights
ChatGPT and Generative AI models can be useful to understand errors in code and obtain suggestionson how to improve text. A lot of times, the outputs are helpful, but reliability is not ensured and afair dose of caution should be taken to the outputs and critical analysis is warranted when making useof the generated suggestions.
26