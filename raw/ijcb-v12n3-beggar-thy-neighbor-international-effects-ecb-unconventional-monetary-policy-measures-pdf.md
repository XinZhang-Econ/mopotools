
### Beggar-Thy-Neighbor? The International Effects of ECB Unconventional Monetary
### Policy*Measures∗*
Kristina Bluwsteina and Fabio Canovab
aEuropean University Institute bBI Norwegian Business School, CAMP, and CEPR
This paper examines the effects of unconventional mon-etary policy measures by the European Central Bank on nine European countries not adopting the euro with a novel Bayesian mixed-frequency structural vector autoregressive technique. Unconventional monetary policy disturbances gen-erate important domestic fluctuations. The wealth, the risk, and the portfolio rebalancing channels matter for international propagation; the credit channel does not. The responses of foreign output and inflation are independent of the exchange rate regime. International spillovers are larger in countries with more advanced financial systems and a larger share of domes-tic banks. A comparison with conventional monetary policy disturbances and with announcement surprises is provided.
JEL Codes: E52, F42, C11, C32, G15.
*∗We*are grateful to Klaus Adam, Jordi Gali, Ajeandro Justiniano, Giorgio Primiceri, Anders Vredin, Knut Are Aaastvert, Aleksei Netsunajev, Sweder van Wijnbergen, Marco Lo Duca, Andrea Nobili, and participants of seminars at the European Central Bank, Norges Bank, Riksbank, the European University Insti-tute, the University of Amsterdam, Bank of Italy, BIS, Federal Reserve Bank of Chicago, Federal Reserve Bank of Richmond, the International Journal of Central Banking Conference “Challenges to Achieving Price Stability,” the ECB confer-ence “Non-standard Policy Measures,” and the Empirical Monetary Economics Workshop at Sciences Po, for comments and suggestions. Canova acknowledges the financial support from the Spanish Ministerio do Economia y Competitividad through the grant ECO2012-33247. Corresponding author (Bluwstein): Depart-ment of Economics, European University Institute, Via della Piazzuola 43, 50133 Firenze, Italy; e-mail: kristina.bluwstein@eui.eu.
69
70 International Journal of Central Banking September 2016
**1. Introduction**
In recent years there has been an unprecedented use of uncon-ventional monetary policy (UMP) measures by central banks of advanced economies. These measures have attracted increasing crit-icism from leaders of developing and peripheral countries. For exam-ple, India’s Central Bank Governor Raghuram Rajan, in a 2014 Brookings speech, stated:
When monetary policy in large countries is extremely and unconventionally accommodative, capital flows into recipient countries tend to increase local leverage; this is not just due to the direct effect of cross-border banking flows but also the indirect effect, as the appreciating exchange rate and rising asset prices, especially of real estate, make it seem that bor-rowers have more equity than they really have. . . . But when source countries move to exit unconventional policies, some recipient countries are leveraged, imbalanced, and vulnerable to capital outflows. Given that investment managers anticipate the consequences of the future policy path, even a measured pace of exit may cause severe market turbulence and collateral damage.
In addition, concerns have been voiced that UMP measures could lead to “beggar-thy-neighbor” effects. Brazilian President Rouss-eff remarked in 2012: “Quantitative easing policies . . . have trig-gered . . . a monetary tsunami, have led to a currency war and have introduced new and perverse forms of protectionism in the world.”
For Europe, where non-euro members are linked to the euro area either through membership in the European Union or signif-icant trade and financial ties, concerns that recent quantitative eas-ing (QE) measures could lead to large appreciation pressures, to increased financial volatility, and to perverse real effects are wide-spread. For example, Riksbank Deputy Governor Per Jansson states that “ECB measures . . . create challenges. . . . The plan is to make extensive purchases of financial assets, equivalent to three times Swedish GDP over a period of just one year . . . In the event of a more tangible and rapid appreciation of the krona, it will be even
Vol. 12 No. 3 Beggar-Thy-Neighbor? 71
more difficult for the Riksbank to attain an inflation rate in line with the target.”1
The economic implications of international spillovers are expected to be severe, as demonstrated by the recent example of Switzerland, who abandoned its floor to the euro in January 2015 in anticipation of QE measures and lost about 50 billion Swiss francs in foreign exchange holdings over the first half of the year. Thus, for both academic and policy purposes, it is crucial to understand if these international spillovers exist, to measure the repercussions in foreign economies, and to design policies that can contain their negative consequences.
This paper sheds light on these issues using an empirical model, which combines slow-moving monthly macroeconomic variables, weekly monetary policy variables, and fast-moving daily financial variables. To handle the frequency mismatch, we employ a Bayesian mixed-frequency vector autoregressive model. The setup accounts for macroeconomic–financial linkages without the time-aggregation biases that are present when lower-frequency data are used, and enables us to give a structural interpretation to the international spillovers. Such an interpretation is not possible when only high-frequency data is used.
We focus on three questions. First, do European Central Bank (ECB) UMP measures generate important financial and real spillovers in European countries not adopting the euro? If so, does the exchange rate regime play a role? Second, does the degree of financial and banking integration matter? Third, which channel of international transmission is operative? What is the relative impor-tance of exchange rate and financial links?
Many papers have analyzed the domestic effects of UMP meas-ures (see Cecioni, Ferrero, and Secchi 2011 for a review). For the euro area, there is evidence that they had positive regional output effects (Lenza, Pill, and Reichlin 2010; Gambacorta, Hofmann, and Peers-man 2012; Darracq Paries and De Santis 2013, Lewis and Roth 2015) but that real responses were slower and less significant than those induced by conventional monetary policy measures (Peersman 2012). The inflation effects instead seem to be muted (Lewis and Roth
1Minutes of the Monetary Policy Committee meeting of February 11, 2015.
72 International Journal of Central Banking September 2016
2015). In addition, high-frequency event studies find a reduction in market spreads (Abbassi and Linzert 2011; Angelini, Neri, and Panetta 2011; Beirne et al. 2011) and a fall in the term premia and government bond yields following a UMP announcement, especially when intraday data are used (see Ghysels et al. 2013).
A number of studies have also begun investigating the inter-national consequences of the Federal Reserve’s UMP measures for emerging markets and found that QE caused the U.S. dollar to depreciate, foreign stock prices to rise, and credit default swap (CDS) spreads to decrease (see, e.g., Neely 2010; Chen et al. 2012; Chinn 2013; Fratzscher, Lo Duca, and Straub 2013). Moessner (2014) observes that international effects for advanced and emerg-ing countries are similar, Chen et al. (2012) claim that the impact in emerging countries is stronger (see also Aizenman, Binici, and Hutchison 2014), and Bhattarai, Chattarjee, and Park (2015) find that the “fragile five” emerging economies are affected most. Lim (2014) claims that at least 5 percent of financial inflows to developing countries between 2000 and 2013 were due to the Federal Reserve’s UMP. Passari and Rey (2015) find that financial flows to developed countries may also have been large.
For euro-area UMP measures, Boeckx, Dossche, and Peersman (2014) show that, after a liquidity increase, the countries with less capitalized banks have smaller bank lending and output effects, while Lo Duca, Fratzscher, and Straub (2014) find that confidence and asset prices improve. Since the effects on yields are small, they con-clude that UMP policies have limited international impact. Chen et al. (2012) note that the international effects of euro UMP meas-ures are weaker than those of the United States. In this paper, we measure the effects of ECB UMP measures in a structural frame-work that considers both financial and macroeconomic variables. We examine the pairwise transmission between the euro area and nine European countries not adopting the euro and attempt to disentan-gle channels of transmission of UMP disturbances.
We find that UMP shocks generate important financial mar-ket responses in the euro area, sizable macroeconomic fluctuations, and some differences in terms of timing or persistence relative to conventional monetary policy shocks. Interestingly, while UMP disturbances induce significant inflation, conventional monetary policy disturbances primarily affect output. Thus, a combination
Vol. 12 No. 3 Beggar-Thy-Neighbor? 73
of conventional and unconventional measures may help to better control output and inflation dynamics. Announcement surprises produce financial market responses that are similar to those of con-ventional policy shocks, but the domestic macroeconomic effects are weak.
International spillovers exist but there is considerable cross-country heterogeneity. The exchange rate regime is not the reason for this heterogeneity. Advanced economies, which tend to be more financially integrated with the euro area and have a larger share of domestic banks, have stronger output and inflation dynamics than those in the euro area. The macroeconomic effects for financially less developed countries, which have a larger share of foreign banks, are varied, but the magnitude of output and inflation responses are the opposite of those of advanced economies. International trans-mission occurs via both the exchange rate channel and financial links (wealth, risk, and portfolio rebalancing channels). However, the exchange rate does not seem to shape the responses of foreign macroeconomic variables to euro-area UMP shocks. This is in con-trast to the international transmission of conventional policy shocks, where the exchange rate is crucial to understand foreign dynamics.
Our investigation has important policy implications. Letting exchange rate float will not prevent non-euro-area countries from importing ECB unconventional monetary policy decisions (see also Rey 2013). Since the dynamics of financial flows are crucial and the presence of global banks in the area is important in determining domestic outcomes (see also Cetorelli and Goldberg 2012; Bruno and Shin 2015a), measures indirectly restricting financial flows and bank leverage could be more effective in insulating small open economies from undesired output and inflation fluctuations. Bruno and Shin (2015b) and Devereux, Young, and Yu (2015) provide the theoretical justification for using such measures.
The paper is structured as follows: Section 2 gives an overview of the channels through which UMP measures may induce domes-tic and international adjustments. Section 3 describes the estima-tion methodology, the identification strategy, and the data. Section 4 presents domestic responses. Section 5 discusses international spillovers. Section 6 investigates why international macrofinancial linkages are heterogeneous. Section 7 examines the robustness of the results. Conclusions are in section 8. The appendices present
74 International Journal of Central Banking September 2016
an overview of the UMP actions by the ECB, the details of the mixed-frequency algorithm, and additional results.
**2. Channels of International Transmission**
There is quite a lot of literature analyzing the mechanics of domestic monetary policy transmission (see, e.g., Krishnamurthy and Vissing-Jorgensen 2011). As far as conventional monetary policy is con-cerned, the expectation, the exchange rate, and the interest rate channels have been emphasized (e.g., Russell 1992). Basic to the idea that monetary policy affects the economy is the notion that central bank decisions influence (i) price-level expectations and thus the domestic aggregate supply via price and wage settings; and (ii) expectations of future short-term interest rates, which feed into long-term interest rates. As long-term interest rates matter for investment and consumption, the domestic aggregate demand is also altered.
Both aggregate demand and aggregate supply effects could be reinforced when monetary policy alters the value of the domestic currency. Exchange rate variations influence the quantity and the price of imports and exports and thus both the aggregate supply and aggregate demand. Monetary policy may also tilt the term structure of interest rates and thus consumption and investment decisions. The interest rate channel is considered the main transmission mechanism for conventional monetary policy in Europe before the introduction of the euro (Angeloni 2012).
When discussing UMP, two other channels become potentially relevant. UMP measures may alter asset prices if they change the user cost of capital*(wealth channel),*and they may reduce uncer-tainty and financial risk perceptions*(confidence channel).*The latter stabilization purpose has been heavily emphasized during the recent financial crisis.
Figure 1 shows the channels of international transmission rele-vant for unconventional policies. UMP measures may alter the bilat-eral nominal (real) exchange rate, which affects net trade and import prices for the partner country*(exchange rate channel).*In turn, these variations affect foreign prices, production, and consumption. The relative magnitude of the changes in foreign inflation and output depends on substitution and income effects (Mishkin 2001).
Vol. 12 No. 3 Beggar-Thy-Neighbor? 75
**Figure 1. Channels of International Unconventional Monetary Policy Transmission**
**Notes:**The gray arrow indicates an indirect effect. The white arrows indicate contemporaneous effects.
There has been an increased interest in the financial channels of international transmission since the onset of the financial crisis. The*credit channel*comprises the bank lending and the balance sheet sub-channels. The*bank lending channel*refers to the effect that UMP measures have on bank reserves when the amount of market liquid-ity changes (recall that banks are the main financial institutions in the euro area). The*balance sheet channel*refers to variations in the net worth of banks (and firms) due to changes in the value of cash flows and collateral. These two sub-channels alter credit conditions by affecting both the quantity and quality of loans. In economies that are financially integrated, global credit conditions may also be affected.
UMP measures may change the relative cost of capital. This may have an effect on the relative price of stocks, bonds, houses, and land, which in turn may lead to international capital flows*(wealth channel).*Both the wealth and the credit channels feed
76 International Journal of Central Banking September 2016
into financial risk, investment, and consumption decisions. While these channels are also present when conventional monetary policy actions are undertaken, unconventional policy—hence an expansion or change in the composition of the balance sheet of the central banks—activates the*portfolio rebalancing channel*(Krishnamurthy and Vissing-Jorgensen 2011). It has been argued that balance sheet policies may reduce private portfolios’ duration risk (e.g., Bernanke 2010; Gagnon et al. 2011). Thus, yields on long-term securities should decline with long-term borrowing increasing. As a conse-quence, aggregate demand and financial risk should be altered. Besides a duration (temporal) effect, the*portfolio rebalancing chan-nel*could lead to an international (spatial) rebalancing between UMP and non-UMP countries, as investors seek higher yields or lower risk (see Passari and Rey 2015). This rebalancing effect may also affect nominal exchange rates (see Bruno and Shin 2015b). Finally, the*confidence channel*influences perceptions of uncertainty and risk. Changes in liquidity and asset prices may also have an indirect effect on risk, as they influence the confidence of investors, and thus investment and consumption decisions.2
Table 1 lists the programs and the timing of ECB unconventional measures during the sample we consider. A detailed explanation of what each measure involves is in appendix 1. “Unorthodox” poli-cies fell into two broad categories: liquidity policies and sovereign debt policies. The former were introduced as a reaction to the finan-cial crisis to ease tensions and make the interbank market function properly. The presumption was that the additional liquidity would be channeled to private borrowers and that real activity would then pick up. If the additional liquidity would become available in global markets and if foreign banks were willing to use it to finance domestic projects, foreign real activity could have also received a boost. The second type of policies were introduced during the sovereign debt crisis to restore confidence in the euro, to lower long-term yields for troubled economies, and to restart normal lending practices.
Thus, while ECB unconventional policies could have had a direct effect on credit and confidence, they may have only indirectly affected the exchange rate and the portfolio of agents, if they induced
2While figure 1 does not mention the*signaling channel,*we account for sig-naling effects in the empirical analysis.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 77
**Table 1. Timeline of ECB Unconventional Monetary Measures**
**Total Size in**€**Billions**
**Date Tool (Outstanding)**
Dec. 2007–Ongoing Reciprocal Currency Agreement
271.6
Mar. 2008–May 2010 6-month long-term refinancing operations
66
May–Dec. 2009 12-month long-term refinancing operations
614
Jun. 2009–Jun. 2010 Covered Bond Purchase Program
45
May 2010–Aug. 2012 Securities Markets Programme
195
Aug. 2011 12-month long-term refinancing operations
49.8
Oct. 2011 13-month long-term refinancing operations
57
Nov. 2011–Oct. 2012 Covered Bond Purchase Program 2
15
Dec. 2011 36-month long-term refinancing operations
489
Feb. 2012 36-month long-term refinancing operations
530
Jul. 2012 Draghi’s “whatever it takes” speech
Aug. 2012–Ongoing Outright Monetary Transactions
Jul. 2013 Forward guidance
**Sources:**ECB weekly financial statements; ECB Statistical Warehouse; Cecioni, Ferrero, and Secchi (2011).
capital flows. In addition, they could have produced global wealth effects if, in response to the additional liquidity, the banking system changed the composition of its portfolio of assets toward more risky activities.
78 International Journal of Central Banking September 2016
**3. The Mixed-Frequency Methodology**
Due to the high-frequency nature of financial variables and the slow reporting of macroeconomic data, applied economists typi-cally face a frequency mismatch when trying to jointly examine macrofinancial linkages in response to shocks. The most common solution is to aggregate high-frequency data into lower-frequency data, but valuable information is lost in the process and conclusions may be affected (see Ghysels et al. 2013 and Rogers, Scotti, and Wright 2014). Alternatively, one may discard low-frequency data and focus on event studies that look at financial variables’ move-ments around policy announcement dates (see Krishnamurthy and Vissing-Jorgensen 2011). This approach is also sub-optimal since it ignores macroeconomic effects. In addition, because high-frequency data is volatile, noise may drive the conclusions.
In this paper, we provide a mixed-frequency compromise (see Foroni and Marcellino 2013 for a survey of mixed-frequency meth-ods): key macro variables are converted from monthly to weekly frequency using an augmented Gibbs sampler technique; financial variables are aggregated from daily to weekly frequency by tak-ing averages. Because ECB unconventional policy data is reported weekly, a weekly frequency balances the desire to smooth some of the noise without discarding too much information. The empirical model we consider is
yt=Ayt−1+Bωt+εt,εt*∼*N(0,Σ),(1)
whereωt=[1,ω∗**t**] is a vector of control variables, andyt=(zt,xt)is
a vector of endogenous variables containing the low-frequency data,zt,and the high-frequency data,xt.zthas missing observations, since we only observe a mid-month average or end-of-the-month value,zi
t.
*3.1 Mixed Frequency with Irregular Spacings*
Researchers trying to combine weekly with monthly data face a problem, fairly neglected in the literature. Because of the irregu-lar nature of weeks (some months contain four weeks, others five weeks), the standard Gibbs sampler cannot be used mechanically to predict missing values and needs to be modified to take into account the possibility of irregularly spaced observations.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 79
The approach we employ is similar to Chiu et al. (2011) and Qian (2013), uses a Bayesian setting, and differs from the usual Kalman-filter approach (Carter and Kohn 1994) employed in the literature because missing data is sampled directly from a constrained multi-variate normal distribution. Furthermore, unlike Kalman-filter tech-niques, the approach works sequentially, and this increases the com-putational speed. There are two main drawbacks of the approach: the dependence of the Gibbs draws increases. We avoid this problem by appropriately thinning the chains. The number of nodes at which the distribution needs to be evaluated increases and this affects the tightness of the standard errors.
Apart from having to deal with irregularly spaced weeks, we also need to solve a time-aggregation problem. Because monthly data is generally reported as a midpoint average, we need to take this into account when drawing missing data. Unlike with end-of-the-period sampling, where one draws the latent variables from an unconstrained multivariate normal distribution, we need to draw all missing variables simultaneously from a constrained multivariate normal distribution, so that the draws satisfy the monthly average. The algorithm employed to estimate the parameters is described in detail in appendix 2.
To avoid imposing too much a priori information which is unjus-tified, given our ignorance about the properties of UMP shocks, we will use flat priors on all the coefficients of the model.
*3.2 Identification of UMP Shocks*
Since the countries we consider are relatively small open economies, they are likely to have little influence on the euro area, while the latter has presumably a larger impact on them. Hence, there is a nat-ural block exogeneity in the system with the euro-area block coming first. The block exogeneity assumption has been used quite a lot in the empirical international literature (e.g., Cushman and Zha 1997; Mackowiak 2007; Dungey and Pagan 2009). It is stronger than the one employed by Kim and Roubini (2000), where block exogeneity is only imposed on the contemporaneous matrix. The estimates we compute are equivalent to those obtained with the two-step approach of Canova (2005).
80 International Journal of Central Banking September 2016
For each country pair, the structural system is
A0,11y1t=A1,11(L)y1t−1+B1ωt+ε1t,ε1t*∼*N(0,Σ1)(2)
A0,21y1t+A0,22y2t=A1,21(L)y1t−1+A1,22(L)y2t−1
+B2ωt+ε2t,ε2t*∼*N(0,Σ2).(3)
The endogenous variables of the small open economy arey2t=*[IP*t,πt,et,spt,lt,riskt]′;those of the euro area arey1t=*[IP∗*
t,π*∗*t,UMP∗
t,sp∗
t,l*∗*t,risk∗
t*]′.*The control variables areωt=[Newst,it−1,i*∗*t−1,
*PC*t].*IP*t(IP∗t) is a real activity measure,πt(π∗
t) is inflation,*UMP∗*t
is the unconventional monetary policy variable,etis the nominal exchange rate,spt(sp∗
t) is stock prices,lt(l∗t) is a measure of liquid-ity, andriskt(risk∗
t) is a measure of risk.Newstis a dummy variable capturing UMP announcements; the conventional monetary policy tool (the interest rate) is denoted byit−1(i∗t−1).Finally,*PC*tis the first principal component of a number of control variables and is described in more detail in the next subsection. It is important to have both the conventional monetary policy tool and the UMP announcements as controls to avoid confounding their effects with those of the shocks of interest.
The variables included are chosen so as to be able to examine the transmission channels discussed in section 2. The exchange rate channel is operative if UMP shocks generate significant exchange rate movements; significant responses of the liquidity variable, on the other hand, would indicate that credit channel is important; a strong and significant response of stock prices would suggest the presence of a wealth channel; and finally, a strong and significant response of the risk variable would indicate that the confidence channel matters.
Because theory is silent regarding the features of UMP shocks, we identify them in an agnostic way. We assume that output and inflation matter for UMP decisions within a week, but that the UMP variable reacts to financial variables only with a week delay. Note that these restrictions have to hold only for a week and are therefore weaker than similar restrictions imposed on a monthly or a quarterly VAR.
The assumption that unconventional monetary policy reacts to financial factors with a delay of at least a week is satisfied for the long-term refinancing operation (LTRO) programs that make up the
Vol. 12 No. 3 Beggar-Thy-Neighbor? 81
largest proportion of UMP measures in our sample. However, for the Securities Markets Programme (SMP), it may be less appropriate, since Lo Duca, Fratzscher, and Straub (2014) pointed out that some of the decisions were made at a daily frequency. The ordering of the variables within the financial block is arbitrary. We have stock prices before the liquidity spread, since we assume they react more slowly to monetary policy than liquidity in the interbank market due to transaction costs. The risk variables appear last, since risk percep-tions react fast and take all available information into account. In section 7 we examine the robustness of the conclusions when different identification and ordering assumptions are employed.
*3.3 Data*
All data comes from Datastream and the ECB. The sample spans from December 18, 2008 until May 10, 2014. The starting and ending dates have been chosen in order to (i) avoid major structural breaks, (ii) avoid the high-volatility period following the Lehman crisis, (iii) have a time period where UMPs were frequently used, and (iv) skip the era of negative interest rates, applied on bank deposits by the ECB in June 2014. Excluding the first six months of the sample does not change the essence of the results we present.
We focus on nine European countries; some are EU members and some are not. Since they have the largest trade and financial linkages with the euro area, they are the most likely candidates to be influ-enced by the ECB’s policies. The majority of countries have float-ing currency regimes (Czech Republic, Hungary, Norway, Poland, Romania, and Sweden). Denmark and Bulgaria are instead pegged to the euro, while Switzerland is a hybrid case, since it switched from a floating regime to an exchange rate floor in September 2011. Rey (2013) has argued that when cross-border flows and leverage of global institutions matter, monetary policy is transmitted globally even under floating exchange rate. Our sample allows us to examine how important the exchange rate regime is for international trans-mission of unconventional monetary policies and to analyze whether policies targeted to affect liquidity and sovereign risk have a different impact than conventional measures.
In the baseline exercises, the monthly Industrial Production (IP) Index is used as a real activity measure and the monthly consumer
82 International Journal of Central Banking September 2016
price index is used to compute inflation. The policy variable is calcu-lated summing up LTRO, SMP, and covered bond purchase (CBP) programs I and II. The daily financial variables are the bilateral nominal exchange rate; the liquidity spread, measured by the differ-ence between the three-month and overnight interbank rates (e.g., EURIBOR-EONIA for the euro area); stock market indices; and CDS spreads. The CDS for the euro area are computed weight-ing individual euro members’ CDS using Eurostat weights. The announcement dummy,Newst,sums up the event dummies for LTROs, collateral changes, SMP, and CBP I and II. Implicit in this setup is the assumption that only surprises orthogonal to the mon-etary information present att*−*1 and to the announcement news attare considered. Changing the timing of the conditioning vari-ables (announcement surprises att+ 1 and interest rates att)does not change the conclusions we obtain. Thus, the possibility that UMP measures were taken as a substitute or as a complement to conventional surprises is statistically weak.3
Apart from the nominal interest rate and the announcement dummy of euro-area UMP measures, we use a principal compo-nent (PC) indicator as control variable. This PC is computed using U.S. and UK (conventional and unconventional) policy variables, global real economy indicators, oil prices, Eastern European and EU (excluding euro-area) financial indicators, global trade price, and global equity indicators. Its inclusion enables us to filter out dynam-ics that could be spuriously attributed to UMP measures but are in fact due to, e.g., oil price shocks, global business-cycle variations, or monetary policy decisions made outside the euro area.
Since VAR data is used as a conditioning set to draw the latent variables, it is essential that all variables (and in particular the higher-frequency ones) exhibit an approximate normal distribution. IP, prices, UMP variables, asset prices, and CDS enter the VAR in log-growth rates. We use first differences for the liquidity spread,
3When we examine the role of conventional monetary policy shocks, we switch the role of interest rates and of the balance sheet variable. When we examine announcement surprises, we keep the nominal interest rates as predetermined and use the balance sheet variable att*−*1 as a control variable. While it would make more sense to treat all monetary variables jointly as endogenous, the mixed-frequency approach would become intractable with the larger-sized VAR.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 83
and interest rates remain in level. The financial data transformed this way shows less skewness and almost no kurtosis. Note that, while long-run relationships will be lost, our transformation helps to have the data on a similar scale, making the Gibbs sampler more efficient and economic interpretation easier.
We have some latitude in choosing the unconventional monetary variable and the risk measure. Thus, we have conducted a num-ber of robustness experiments. In particular, we examined euro-area responses when an excess liquidity variable is used instead of a bal-ance sheet UMP variable. This series is computed using the differ-ence between the current account and reserve requirements, net of the deposit and marginal lending facilities, and purifies the balance sheet variable from the demand effects due to the fixed-rate full-allotment provision (see also Lewis and Roth 2015). We furthermore split the balance sheet variable into liquidity measures and sover-eign measures. We also checked what happens when we substituted the VIX index for CDS risk, when possible. The next section com-ments on the results, and appendix 3 plots the responses we obtain in alternative systems.
**4. Domestic Transmission**
We first present the dynamics produced by UMP shocks in the euro area; see the first column of figure 2. We plot euro-area responses to compare our results with those present in the literature, and to provide a benchmark to understand international dynamics. Figure 2 also reports the responses obtained following an expansionary conventional monetary policy shock (second column) and a UMP announcement surprise (third column).
A few features of the dynamics are noteworthy. First, following a UMP shock, inflation significantly and persistently increases, while real activity responses are negative on impact and then insignificant. This latter pattern is in contrast to what researchers have found for the United States and the United Kingdom. However, while cen-tral banks in these countries engaged in large-scale asset purchase programs to drive up yields and aggregate demand, euro-area UMP measures were aimed mainly at providing liquidity for the interbank market. In order for output effects to materialize, additional liquid-ity is needed to reach the real economy via bank lending, and there
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEy9g_FsOjdnu0BRkYDFZjLqiYUHgnC5X0QnTH7o0_1bak39zty6G7IRO7toLGd8KDUzzTN-b3g7OcGefhT1uv7lLq96nZfMS6dHMAOt-MV7yEU6LLRfe6KV5AFcOVyS_13e_dMbQ=w1198-h682-v0?authuser=1)

84 International Journal of Central Banking September 2016
**Figure 2. Responses of Euro-Area Variables to Shocks**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread, the interest rate (for conventional monetary policy), and the announcement dummy.
is little evidence that this has happened (Borstel, Eickmeier, and Krippner 2015). In addition, since euro-area members differ sub-stantially in their bank lending responses, failure to observe positive aggregate real activity responses may be due to regional hetero-geneities (Santis and Surico 2013; Altavilla, Canova, and Ciccarelli 2015).
To understand whether the lack of positive real activity responses depends on particular features of the empirical model, we have rerun the analysis (i) with aggregated monthly variables, (ii) with excess liquidity as an indicator of unconventional monetary policy; and (iii) splitting liquidity from sovereign bond unconventional policies (see appendix 3). Real activity responses are still insignificant at all horizons in the monthly VAR, while disturbances to excess liquid-ity variable produce the same pattern of real activity and inflation responses as in the baseline case. This lets us conclude that the use of mixed-frequency data and of the balance sheet variable as a measure of UMP is not responsible for our conclusions. Aggre-gating liquidity and sovereign debt programs may not be ideal if the task is to measure the real effectiveness of UMP measures,
Vol. 12 No. 3 Beggar-Thy-Neighbor? 85
since they are likely to work through different channels. In fact, while liquidity disturbances lead to the same pattern of output and inflation responses as in the baseline case, sovereign debt distur-bances produce small medium-term positive real activity responses and negative but insignificant inflation responses.
Second, financial variable responses are in line with expecta-tions. Stock prices initially fall and then persistently increase and the responses are generally significant; liquidity spread responses are positive but insignificant on impact and turn significantly neg-ative in the medium run; risk responses are generally negative but insignificant. Thus, while the liquidity and the wealth channels seem operative, at least in the medium run, the confidence channel is weak.
Third, as in Peersman (2012), we find that real activity responses are stickier and less significant than those obtained after conven-tional monetary policy disturbances. Conventional monetary pol-icy shocks have a persistently positive effect on output—the peak response occurs after eight to ten weeks—but an insignificant effect on inflation. Hence, jointly using conventional and unconventional monetary tools may help to better control output and inflation dynamics in the area.
Fourth, risk perceptions persistently decrease following a conven-tional monetary policy disturbance, and stock prices increase for up to eight weeks, while the liquidity spread is not significantly affected. The dynamics of these three financial variables are both quantita-tively and qualitatively in line with what is known in the euro area (see, e.g., Christoffel, Coenen, and Warne 2008). The weak response of inflation and the strong decrease in risk are a feature of our sam-ple period, which only starts in 2008 and includes both the financial and the European sovereign debt crises.
Finally, a UMP announcement surprise does not have measurable effects on output or inflation. The responses of financial variables, although less significant, resemble those produced by a conventional policy disturbance (see also Szczerbowicz 2015). Altavilla, Giannone, and Lenza (2014) have shown that OMT announcements have sig-nificant effects on output of Mediterranean countries. Our results are not necessarily in contrast with theirs. First, while they find that output positively reacts in Spain and Italy, no effect is found in France and Germany. Hence, the aggregate effects they find may
86 International Journal of Central Banking September 2016
**Figure 3. Responses to a Euro-Area UMP Shock, Foreign Countries**
2 4 6 8 10 12 14 16
-0.2 0
0.2 0.4
**Advanced**
**Output**
2 4 6 8 10 12 14 16
-0.1 0
0.1 0.2 0.3
**Inflation**
2 4 6 8 10 12 14 16
-0.1 -0.05
0**Exchange Rate**
2 4 6 8 10 12 14 16
-0.2
0
0.2
**Stock Prices**
2 4 6 8 10 12 14 16
0 0.1 0.2 0.3
**Liquidity**
2 4 6 8 10 12 14 16 -0.5
0 0.5
1 1.5
**Risk (CDS)**
SE NO SW DK
2 4 6 8 10 12 14 16
-0.2 0
0.2 0.4
**CEE**
2 4 6 8 10 12 14 16 -0.2 -0.1
0 0.1
2 4 6 8 10 12 14 16
-0.15 -0.1
-0.05 0
2 4 6 8 10 12 14 16
-0.2 -0.1
0 0.1
2 4 6 8 10 12 14 16
-0.03 -0.02 -0.01
0 0.01
2 4 6 8 10 12 14 16
-2
-1
0
CZ PO
2 4 6 8 10 12 14 16
-0.3 -0.2 -0.1
0
**SEE**
2 4 6 8 10 12 14 16
-0.1 0
0.1 0.2
2 4 6 8 10 12 14 16
-0.2
-0.1
0
2 4 6 8 10 12 14 16 -0.2
0
0.2
2 4 6 8 10 12 14 16 -0.05
0 0.05
0.1
2 4 6 8 10 12 14 16 -1
-0.5 0
0.5
HU RO BG
**Notes:**The lines report the point-wise posterior median responses in deviations from euro-area responses. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is 10 percent of UMP.
be insignificant. Second, they consider only the announcement of one program, while we examine the effects of announcements of all UMP programs. Third, their methodology is different: while they use the persistent financial responses that announcements induce as a measure for announcement effects in the VAR, we use a dummy approach. Finally, as Ghysels et al. (2013) and Rogers, Scotti, and Wright (2014) argued, to measure the effects of announcements, higher-frequency data, ideally intradaily, should be used. Hence, our announcements effects could be underestimated.
**5. International Transmission**
Figure 3 shows the median posterior responses of the variables of the nine foreign economies to a euro-area UMP shock, in deviations from the responses obtained in the euro area (except for the exchange rate, which is plotted in level). For instance, positive and signifi-cant responses of real activity would indicate that a UMP shock generates foreign output responses that are significantly larger than
Vol. 12 No. 3 Beggar-Thy-Neighbor? 87
those obtained in the euro area. For presentation purposes, responses are grouped into different country groups: (i) advanced countries— Sweden, Norway, Denmark, and Switzerland, (ii) Central Eastern European countries (CEE)—Poland and the Czech Republic, and (iii) Southeastern European countries (SEE)—Hungary, Romania, and Bulgaria. Figure 6 in appendix 3 reports group average responses with the posterior credible sets.
Output responses to euro-area UMP shocks are quite heteroge-neous. While in advanced countries responses are persistently posi-tive and significantly larger than in the euro area after two weeks, those in the CEE countries are insignificant, and those in SEE countries are persistently negative and significantly smaller than in the euro area after about two weeks. Inflation responses are also heterogeneous: they are positive for CEE and SEE countries, gen-erally after about two or three weeks, and negative for advanced economies.
Why are macroeconomic responses so different across countries? One possibility is that certain countries are insulated from for-eign shocks while others are not because of different exchange rate regimes. Such an explanation does not seem to hold up since, e.g., both peggers and floaters are part of the advanced-countries group. As is pointed out by Rey (2013), having floating exchange rates does not necessarily insulate a country from importing foreign monetary policy decisions. A related explanation could be that different real exchange rate dynamics lead to different trade gains across country groups. Again, this explanation seems incapable of accounting for the heterogeneities we find: real exchange rate responses are all negative (the local currency appreciate versus the euro). Fratzscher, Lo Duca, and Straub (2013) and Lo Duca, Fratzscher, and Straub (2014) also find a (nominal) appreciation using an event-study approach and much higher-frequency data. Therefore, while the exchange rate channel is activated following UMP shocks, differential exchange rate dynamics do not explain the pattern of macroeconomic responses we obtain.
Gopinath (2015) suggests that similar currency appreciations do not necessarily lead to similar dynamics of exports and imports, if firms engage in non-competitive pricing and alter markups following a nominal appreciation. Therefore, if countries have different levels of non-competitiveness, similar appreciations of the currency may lead
88 International Journal of Central Banking September 2016
to different inflation responses across countries. While the inflation dynamics we present could be consistent with this explanation, it is hard to see how differential non-competitive behavior may lead to the variety of output responses that we obtain.
Another reason why output and inflation responses could be different is that euro-area UMP shocks occur at the same time as, e.g., oil shocks, and hence our responses are potentially spu-rious. Again, this explanation does not seem to be relevant for two reasons: we have conditioned on oil prices (via PCs) in the VAR, and (ii) the only oil-producing country of our sample (Nor-way) displays large output responses but also negative stock price responses, which are hard to rationalize if UMP shocks proxied for oil shocks.
Cross-country heterogeneities of output and inflation responses could be generated if euro-area UMP disturbances hit countries at different stages of the business and the financial cycles. As figures 12 and 13 in appendix 3 show, both types of cycles in the nine countries are closely synchronized.
Another possibility one can consider to account for the inter-national macroeconomic heterogeneities is that some countries con-ducted their own UMP measures when the ECB engaged in non-conventional policies, while others did not. While lack of detailed information prevents us from directly linking monetary decisions to existing heterogeneities, we have one country—Sweden—where liquidity policies were conducted from October 2008 until December 2010, but not thereafter. Thus, comparing the responses in the two subsamples, we can check whether the presence of domestic UMP measures makes a difference. Figures 10 and 11 in appendix 3 report the responses following a UMP shock in the euro area. When liquid-ity measures were in place, relative output responses were positive and relative inflation responses were insignificant; when they were not, relative output responses were insignificant and relative infla-tion responses were positive. However, since the second subsample roughly corresponds to the period when the ECB implemented sover-eign debt policies, it is difficult to reliably attribute these differences to the presence of domestic UMP measures. We discuss our favorite explanation in section 6.
Stock price responses are significantly different from those obtained in the euro area. They initially increase for all countries
Vol. 12 No. 3 Beggar-Thy-Neighbor? 89
but Norway and then fall for up to eight weeks, with Denmark as the exception. Note that the responses in CEE and SEE countries are slightly more persistent than in advanced countries. Positive international stock price responses have also been found in event studies such as Fratzscher, Lo Duca, and Straub (2013) and Lo Duca, Fratzscher, and Straub (2014) and are consistent with the presence of both wealth and portfolio rebalancing channels: at least on impact stock prices increase significantly more than in the euro area. In the medium run, stock prices of all countries either increase by less than in the euro area or fall.
There is considerable heterogeneity in the response of the risk spread: consistent with the finding of Fratzscher, Lo Duca, and Straub (2013), it declines relative to the euro area for CEE and SEE countries (with the exception of Hungary), while it increases for advanced countries. Risk responses are large in absolute value, even though we are using CDS spreads to infer risk. Given that country risk usually serves as a floor for domestic financial risk, the true effects may be even larger.
The credit channel, on the other hand, is weak. Except for Roma-nia and perhaps Poland, the liquidity spread is not responding sig-nificantly to euro-area UMP disturbances. This is in line with Taylor and Williams (2008), who find that the LIBOR-OIS spread did not react to the Federal Reserve’s QE1.
In sum, the financial market responses we obtain are in line with those found in high-frequency event studies. Hence, aggregating daily financial data does not entail a significant loss of information regarding the international transmission of UMP measures. Inter-estingly, our analysis shows that macroeconomic responses to UMP disturbances are very much country specific, even when financial market responses are similar.
*5.1 A Counterfactual*
To quantify the relative importance of the financial versus the exchange rate channels in transmitting UMP disturbances, we per-form a counterfactual exercise: we trace out the dynamics of the foreign variables to a euro-area UMP shock holding either stock prices, liquidity and risk spreads, or the exchange rate constant. Thus, in the former case, international links are generated via the
90 International Journal of Central Banking September 2016
**Figure 4. Counterfactual Responses to a Euro Area UMP Shock, Foreign Countries**
2 4 6 8 10 12 14 16
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
**Full Transmission**
**Output**
2 4 6 8 10 12 14 16
-0.2
-0.1
0
0.1
0.2
0.3
0.4
**Inflation**
2 4 6 8 10 12 14 16
-0.4
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0.4**No Exchange Rate Transmission**
2 4 6 8 10 12 14 16
-0.2
-0.15
-0.1
-0.05
0
0.05
0.1
0.15
0.2
0.25
2 4 6 8 10 12 14 16
-2
-1.5
-1
-0.5
0
0.5
1
**No Financial Transmission**
2 4 6 8 10 12 14 16
-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
0.1
0.2
SE NO SW CZ PO HU RO BG DK
**Notes:**The lines report the point-wise posterior median impulse responses in deviations from the euro-area responses. The horizontal axis reports weeks; the vertical axis reports monthly growth rates.
exchange rate; in the latter case, only financial transmission takes place. Figure 4 presents the results. In the first column, we report the benchmark output and inflation responses we had in figure 3; in the second, the responses obtained switching off the exchange rate channel; and in the third, the responses obtained switching off the financial channels.
Eliminating the exchange rate channel slightly alters the mag-nitude but does not change the shape of the responses. Overall, exchange rate movements seem to slightly reduce output responses and slightly amplify inflation responses. In contrast, shutting off financial channels has major effects on foreign output and infla-tion responses: output responses are now insignificant except on impact and display no persistence, and inflation now drops on impact, because the currency generally appreciates and imported inflation falls. Note also that output and inflation responses are now more homogenous. Hence, cross-country differences in financial– macro linkages are likely to be the reason for the cross-country heterogeneity of the output and inflation responses.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 91
*5.2 International Effects of Conventional Monetary Policy and Announcement Surprises*
In appendix 3 we present the international responses obtained when conventional monetary policy shocks and announcement surprises are considered.
Conventional monetary policy shocks also induce heterogeneous international dynamics. For advanced countries, the exchange rate temporarily appreciates relative to the euro, but there is little dif-ference with the euro area as far as output and inflation responses are concerned, and this occurs despite the fact that both the liquid-ity and the risk spreads are quite heterogeneous across countries. For CEE countries, the exchange rate depreciates relative to the euro, but output falls and stock prices increase, while the risk spread eventually decreases. Finally, for SEE countries, the local currency generally depreciates and output temporarily increases, while stock prices fall and the risk spreads increase.
Announcement surprises produce macroeconomic responses, which are similar to those obtained in the euro area for many advanced and SEE countries. The exchange rate and the financial responses resemble those obtained with a conventional monetary pol-icy shock, with Denmark being the exception. However, exchange rate responses are far less persistent. Also, the SEE countries seem to be the countries whose financial markets benefit most from ECB measures: stock prices increase while the liquidity and the risk spread decrease.
In sum, the evidence suggests that the exchange rate, wealth, risk, and portfolio rebalancing channels spill euro-area UMP shocks to foreign countries. Advanced economies tend to have output and inflation dynamics that resemble those of the euro area, even though output effects are larger and inflation effects smaller. For the remain-ing countries, the macroeconomic consequences differ. The exchange rate channel does not seem to shape the responses of foreign macro-economic variables, but the financial channels are important for the international transmission. This is in sharp contrast to the international transmission of conventional monetary policy shocks, where exchange rate movements drive foreign output and inflation dynamics.
92 International Journal of Central Banking September 2016
**6. Why Are Foreign Macroeconomic Responses Heterogeneous?**
As we have seen, positive financial spillovers from UMP disturbances do not necessarily translate into positive real transmission. In addi-tion, even in countries where financial market responses are some-what similar, real responses are heterogeneous. In this section, we examine the reasons behind this heterogeneity.
The International Monetary Fund (2013) states that between 70 and 90 percent of assets in CEE and SEE countries is held by foreign banks and claims that these assets amount to at least 50 percent of domestic GDP. Since foreign banks in the countries under consider-ation are mostly from the euro area, they have access to the cheap ECB liquidity, and they may invest into foreign financial markets what they borrow from the ECB rather than lend it to domestic agents. This would positively affect foreign asset prices and reduce foreign risk but would not lead to positive real spillovers, as foreign loans would not be affected. Hence, if countries are heterogeneous in the composition of their banking sector, similar financial market responses may lead to different real effects. In particular, in countries featuring a large share of foreign banks, global liquidity increases should have the large effects on stock prices and small pass-through to the real economy.
Figure 5 reports the average responses for countries with a low foreign bank share (at least two-thirds of banks are domestic) and high foreign ownership. Confirming our intuition, we find no signif-icant difference in the dynamics of the liquidity spread in the two groups, but we observe a stark difference in the response of stock prices and risk. Countries with a high share of foreign bank owner-ship experience an increase in stock prices and a reduction in risk relative to the euro area; countries with a lower share of foreign banks feature declining stock prices and increasing risk. In addition, while the former display falling relative real output growth, the lat-ter show a significant relative output increase a few weeks after the euro-area UMP shock.
To provide further evidence that the structure of domestic finan-cial markets is crucial to understand the international transmission of UMP disturbances, we group countries according to the level of financial development (as provided by the World Economic Forum
Vol. 12 No. 3 Beggar-Thy-Neighbor? 93
**Figure 5. Comparative Impulse Responses to a UMP Shock**
0 2 4 6 8 10 12 14 16 -1
-0.5
0
0.5
1**Industrial Production**
0 2 4 6 8 10 12 14 16 -0.4
-0.2
0
0.2
0.4**Inflation**
0 2 4 6 8 10 12 14 16 -0.15
-0.1
-0.05
0
0.05
0.1**Real Exchange Rate**
0 2 4 6 8 10 12 14 16 -0.2
-0.1
0
0.1
0.2**Stock Prices**
0 2 4 6 8 10 12 14 16 -0.04
-0.02
0
0.02
0.04**Liquidity Spread**
0 2 4 6 8 10 12 14 16 -0.6
-0.4
-0.2
0
0.2
0.4
0.6**Risk (CDS)**
low Foreign Bank Share high Foreign Bank Share
**Notes:**The lines report the point-wise average posterior median responses in deviations from the euro-area responses. The dotted line represents the 68 per-cent point-wise credible sets. Countries with a low foreign bank share are Sweden (52 percent), Norway (58 percent), Poland (63 percent), and Denmark (61 per-cent); countries with a high foreign bank share are Switzerland (72 percent), Czech Republic (92 percent), Hungary (100 percent), Romania (72 percent), and Bulgaria (81 percent). Data on foreign bank shares come from the Bank for International Settlements and are for 2012.
2012) and the credit-to-GDP ratio. With these two alternative classifications, the groups remains unchanged except for Poland and Switzerland, which switch groups. The financially advanced, high credit-to-GDP ratio countries (Sweden, Norway, Denmark) behave like the countries that have a low foreign bank share, while the less financially advanced, low credit-to-GDP economies (CEE and SEE) show the same responses as the countries that have a high foreign bank share. These results agree with Aizenman, Chinn, and
94 International Journal of Central Banking September 2016
Ito (2015), who claim that higher levels of financial development can mitigate the negative effects of a foreign UMP shock and that finan-cially more open but potentially less developed small economies are more sensitive to foreign UMP shocks. They also agree with Dedola, Rivolta, and Stracca (2015), who show that spillovers of U.S. mone-tary shocks are largest for emerging economies whose level of finan-cial development is generally low, and with Ongena, Schindele, and Vonnak (2015), who point out that local lending in foreign curren-cies, which is common among countries that have a high foreign bank share, leads to a stronger international bank lending channel.
**7. Robustness**
The results presented so far are derived under the identification assumption that a UMP shock has no weekly effect on output and inflation and that the UMP variable does not respond within a week to financial variables. While the first assumption is hard to dispute, the second could be debatable. Furthermore, the ordering of vari-ables within the financial block is arbitrary. In this section we dis-cuss what happens when we alter identification assumptions. The responses for these cases are in appendix 3.
*7.1 Changing the Ordering of Euro-Area Financial Variables*
We considered three alternative orderings of the variables of the euro-area block: two where financial variables are permuted (R1: output, inflation, UMP, liquidity, stock prices, and risk; R2: output, inflation, UMP, risk, stock prices, and liquidity), and one where the policy variable reacts within a week to macro and financial variables, meaning that the ECB monitored financial markets on a weekly basis when deciding UMP which, as mentioned, seem to have occurred with the Securities Markets Programme—roughly 10 percent of the UMP in our sample (R3: output, inflation, stock prices, liquidity, risk, and UMP).
No major differences are noticeable between the baseline and the R1 and R2 schemes except for the kink in the liquidity spread responses for Romania. Thus, the order of the variables within the financial block is inconsequential for the transmission of UMP shocks.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 95
Some changes appear when the R3 scheme is used. The responses for euro-area variables are qualitatively similar, even though stock prices and risk responses are less significant. Internationally, the most notable change is in the dynamics of pegger countries: the responses of inflation and of the liquidity spread are now stronger; those of stock prices and of risk are weaker. Thus, the relative impor-tance of the wealth and portfolio channels may depend on whether we allow the UMP variable to react to financial variables.
*7.2 Identification of UMP via Sign and Zero Restrictions*
While the identification scheme that we have used for euro-area UMP shocks imposes relatively weak restrictions, we also exam-ined the dynamics with an identification scheme that mixes sign and zero restrictions. In particular, we still assume that output and inflation do not react to UMP shocks within a week, but impose that a positive UMP shock increases the UMP variable and makes the liquidity spread non-positive for one period. Restrictions of this type have been used by Gambacorta, Hofmann, and Peersman (2012) and Carrera, Forero, and Ramirez-Rondan (2015) and seem reason-able since several UMP measures aim at increasing the liquidity of financial markets.
Since this scheme identifies a set rather than a point in the space of contemporaneous matrices, responses are generally more uncer-tain. Qualitatively speaking, the responses for the exchange rate, the liquidity spread, and risk are as in the baseline, while the response of stock prices is, on average, more negative. Interestingly, the dynamic responses of output and inflation are similar to those of the R3 scheme for most countries.
*7.3 Identification via Heteroskedasticity*
The use of higher-frequency data makes us less sensitive to the issue of policy endogeneity but still imposes some restrictions on financial variables. As a further check on the robustness of our conclusions, we use volatility changes to identify UMP shocks as in Rigobon (2003). The method requires that there are at least two regimes with differ-ent volatilities (e.g., low and high), assumes that shocks are uncor-related, and assumes that the contemporaneous impact matrix and
96 International Journal of Central Banking September 2016
the parameters of the VAR are stable. While the restrictions such an identification scheme imposes are weak, one should also remember that regimes are often arbitrarily chosen and that shocks identified this way have very little economic interpretation (Kilian 2011).
We check for the presence of different regimes/structural breaks in the reduced-form VAR residuals informally. There is a decrease in volatility in a number of the equations roughly corresponding to Mario Draghi’s famous “whatever it takes” speech on July 26, 2012. This decrease is marked in the liquidity and UMP equations for the euro area, and in the exchange rate, liquidity, and risk equations for some countries.
To estimate the system, we condition the Gibbs sampler on the variances for the two regimes as in Kulikov and Netsunajev (2013). We divide the sample into pre-Draghi speech state,s1,and post-Draghi speech state,s2,and assume that the variance of the struc-tural errors is state dependent:
εt(sj)∣st*∼*Normal(0,D(st)).
The diagonal matrix,D(s2),determines the short-run matrix,**A0,**once posterior variances are computed usingΣ−1(1)=**A′**
0A0,Σ−1(2)=**A′ 0D(s2)−1A0,**whereD(s1)=I.
Since not all countries display volatility changes around the cho-sen breakpoint, general conclusions are difficult to draw. While responses are not very significant, the basic conclusions we have obtained are unchanged: output responses vary across countries, with advanced countries displaying strong positive responses while responses in CEE and SEE countries are negative; the real exchange rate appreciates for most countries; and the credit channel is weak.
**8. Conclusion**
This paper examined the international transmission of euro-area UMP disturbances. We contributed to the literature in three ways. From a methodological point of view, we provide a way to combine low-frequency macroeconomic data with high-frequency financial data, minimizing time-aggregation and policy endogeneity biases. From an economic point of view, we shed light on the effect of uncon-ventional ECB measures using a framework where macrofinancial
Vol. 12 No. 3 Beggar-Thy-Neighbor? 97
linkages are properly accounted for and an international perspec-tive is adopted. From a policy perspective, we provide new evidence on the role of exchange rate regime in internationally transmitting monetary policy decisions in a world where cross-border flows and leverage matter.
We focused the analysis on three questions. First, do ECB UMP measures generate important macroeconomic effects domestically and in European countries not adopting the euro? We document that UMP shocks generate important euro-area financial market responses, sizable macroeconomic fluctuations. Interestingly, while UMP disturbances induce significant inflation, conventional mone-tary policy disturbances primarily affect output. This means that a combination of conventional and unconventional measures may help to better control output and inflation dynamics. Announcement sur-prises produce financial market responses, which are similar to those of conventional policy shocks, but output and inflation effects are weak. International spillovers exist, but there is considerable cross-country heterogeneity. The exchange rate regime is not the reason for this heterogeneity.
Second, does the degree of financial integration matter for inter-national transmission? Is it true that larger financial market inte-gration led to more significant international real co-movements in response to UMP disturbances? Advanced economies, which are more financially integrated with the euro area and have a larger share of domestic banks, tend to have output and inflation dynamics that are qualitatively similar but generally stronger than those in the euro area. The macroeconomic effects for financially less developed countries, which have a larger share of foreign banks, are varied, but output and inflation responses are the opposite of those of advanced economies.
Third, which channel of international transmission is operative? What is the relative importance of exchange rate and financial spillovers in propagating UMP shocks? International transmission occurs both through the exchange rate channel and the financial (wealth, risk, and portfolio rebalancing) channels. However, the exchange rate does not seem to shape the responses of foreign macro-economic variables to euro-area UMP shocks. This is in contrast to the international transmission of conventional policy shocks, where the exchange rate is crucial to understanding foreign dynamics.
98 International Journal of Central Banking September 2016
Our results have important policy implications. In our sample of countries, the exchange rate regime is unimportant to explain cross-country differences in the dynamics of real activity and infla-tion. Exchange rate movements are closely watched by policymakers and, as the quotes from the introduction suggest, are considered crucial for the international propagation of UMP decisions. How-ever, when financial channels are dominant and capital flows impor-tant, controlling exchange rate movements will not prevent non-euro-area countries from importing the unconventional monetary policy decisions of the ECB (see also Rey 2013). Since the dynamics of financial flows are crucial and the presence of global banks in the area is important in determining domestic outcomes (Cetorelli and Goldberg 2012), policies that indirectly restrict financial flows and bank leverage could be more effective in insulating the small open economies from undesired output and inflation fluctuations. Bruno and Shin (2015b) and Devereux, Young, and Yu (2015) provide the theoretical justification for using such measures.
The current work can be extended in various ways. One could study announcement effects in more detail. While we controlled for them in the estimation, we did not consider any potential anticipa-tory effect that announcements can generate. Taking expectations into account might increase the significance of the credit channel. We could include the recent QE measures in the analysis. Finally, we have assumed that structural parameters are stable. Ciccarelli, Maddaloni, and Peydro (2013) suggested that time variations could play a role in international policy transmission. Investigations of this type can improve our understanding of how UMP measures are transmitted and give policymakers a more solid foundation when deciding which policy to implement.
**Appendix 1. ECB Unconventional Measures**
The ECB’s unconventional toolbox included five liquidity policy measures to aid the interbank market. The first of these tools was introduced in October 2008—the new fixed-rate full-allotment ten-der procedure—and was designed to ensure that the high demand for liquidity, which reached a peak of 95 billion euros during the crisis, could be met. The policy allows credit institutions to acquire an unlimited amount of euros in an auction at a fixed rate. The
Vol. 12 No. 3 Beggar-Thy-Neighbor? 99
second tool, also introduced in October 2008, expanded the list of assets that were accepted as collateral. These two tools together ensured an almost unlimited refinancing to the 2,200 credit insti-tutions that had access. The third tool allowed lengthening of the maturities of the longer-term refinancing operations (LTROs) from three months to up to three years. In March and July 2008, the first six-month full allotments were announced, and twelve-month LTROs were introduced in June 2009. In December 2011 and then again in February 2012, LTROs with a maturity of three years were introduced to provide more long-term liquidity and to ease interbank market tensions. The fourth tool ensured enough liquidity of foreign currency, particularly of the U.S. dollar. This was conducted through a direct swap line with the Federal Reserve. The final measure, cov-ered bond purchases (CBPs), introduced in 2009, allowed the ECB to purchase debt securities issued by banks. This allowed banks to have even longer-term funding than through refinancing operations following the complete shutdown of the covered bond market dur-ing the financial crisis.4 In November 2011, a second round of CBPs was introduced. These five tools make up what we term (in-) direct liquidity policy.
As far as sovereign debt policy is concerned, a measure was introduced in May 2010 that allowed the ECB to purchase pub-lic and private debt securities—the Securities Markets Programme (SMP). The official objective of the SMP is to provide more liquid-ity to “dysfunctional” market segments to ensure that transmission channels for monetary policy are properly operating. The ECB con-ducted sterilizing operations to reabsorb the excess liquidity. The composition of the SMP consisted of 47 percent Italian debt, 22 percent Spanish, 16 percent Greek, and the remaining percent in Irish and Portuguese debt. The final measure—Outright Monetary
4CBPs are different from asset-backed securities. The risk associated with covered bonds stays with the originator, so that the ECB was not necessarily subjected to more risk and the issuing institution still had an incentive to con-stantly evaluate credit risk. This is in contrast to the United States and the United Kingdom, where the Federal Reserve started buying asset-backed securi-ties, commercial paper, and direct obligation of mortgage-backed securities and the Bank of England introduced an asset purchase facility, to ease the non-bank credit market. Since banks are the biggest holders of covered bonds in Europe, such a measure was designed to improve interbank market conditions.
100 International Journal of Central Banking September 2016
Transactions (OMT)—was announced in August 2012, when the SMP was aborted. Similarly to the SMP, the OMT is the steril-ized purchase, conditional on certain domestic economic conditions, of one- to three-year maturing government debt.
**Appendix 2. Mixed-Frequency VAR Algorithm**
This appendix describes the algorithm used to draw sequences for the posterior distribution of the missing variables and of the parameters—see also Qian (2013).
Let$zt $be the vector of all missing observations and let(z,x)rep-resent all recorded observations. The algorithm works as follows:
1. Define a matrix of dataY(missing observations are indicated by NaN).
2. Analyze the aggregation structure (if data comes as sum, average, end-of-period) and define a matrix,M, indicating which observations are missing. For example, if we have two variables—one monthly average which we observe once in the final week, and one weekly which we observe four times— we construct
−→M, vectorizingM
kxTcolumn by column, so that
−→M=[0,0,0,1,1,1,1,*1]′.*
3. Transform the averaged data into summed data, where the average isza,b≡1
b−a+1
$∑b−a t=0 ẑt+a $and the sumzb=
(b*−*a+1)za,b.
4. Specify a normal prior for the coefficients,A,B,and an inverted-Wishart prior for the varianceΣ.
5. Draw initial values for the coefficients,A,B,and for the vari-anceΣ.
6. Specify initial values for the latent data by substituting miss-ing values with sums computed from step 3.
7. Construct the matrixTTk×Tk
that will account for time aggre-
gation. In our caseT= 262 andk= 12. Initially,T*3144×3144*
is
Vol. 12 No. 3 Beggar-Thy-Neighbor? 101
an identity matrix. Using the matrixM, we scan each row,i,and column,j,for missing values,m.In the previous example, we havem=1,2,3 ini= 1 right beforej= 4. We add one for every missing variable to the transformation matrix in row(j−1)k+iand column(j−1)k+i−mk.The transformation matrix is then
T*8×8*
=
⎛⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 1
⎞⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
.
8. Transform the data using−→MY, so that we have both a latent
disaggregated block and an observed block.
9. Start the Gibbs sampler: (a) Estimate the VAR coefficients and draw parameter esti-
mates fromf(Ai,Bi∣Y^i,Σi−1).
(b) Estimate the variances of the VAR and draw the variance estimates fromf(Σi−1∣Y^i,Ai,Bi).
(c) Compute the covariance matrix of the VAR using draws for the coefficients,A^,B^,and the varianceΣ^.
(d) Constrain the multivariate normal (MVN) distribution using the transformation matrixA,so thatyt*∼ MVN*(Aη,AΩA′)=*MVN*(μ,Σ).The distribution for the latent variables is
$zt|z, x $*∼ MVN*(μ0+Σ01Σ−111((z,x)′*−*μ1),
Σ00*−*Σ01Σ−111Σ10),
whereΣ01is a submatrix ofΣrepresenting the covari-ances between the missing and the observed observations.Σ00is the variance of the missing observations andΣ11is the variance of the observed data.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQH4qoy6WR4AMlncAJ8O7a7x2bUuMep129O2-CEwMmjcCsoFuYVKbT3bWDMj8IDfjMDIhXFrufj0yzvxo8ZiN9qla-hfmQCGvYLkRO1HPH2s2DgCX2-ij0NoMkdScCxnFI_57Dz4=w1280-h932-v0?authuser=1)

102 International Journal of Central Banking September 2016
(e) Sample missing data from the conditional constrained MVN described in step 9(d) (in blocks). That is, for allt=1,...,T, we draw missing data fromf(z^i
$t|x, ẑi−1 t , Ai, Bi, Σi). $
(f) Repeat steps (a) through (e).
10. Examine convergence using, e.g., CUSUM statistics.
The results we present are based on 12,500 draws: we discard the first 2,500 as burn-in and retain every 20th draw to reduce serial correlation. Inference is based on 500 saved draws.
**Appendix 3. Additional Results**
**Figure 6. Euro-Area Responses to UMP Shocks: Monthly VAR**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEBmd6hff2Lwr_W7qkUwyWOKypcazWMc9RkitF2sKzpdTvZwtSDWOUbBJmm7Ro-MSqFtZE-iZb9yl8oGZSczTrWY9VEvbjquwX8aH92i0EQqqRHinumdUAVJn3PyDDvvJY02Cga=w1280-h904-v0?authuser=1)

Vol. 12 No. 3 Beggar-Thy-Neighbor? 103
**Figure 7. Euro-Area Responses to UMP Shocks: Excess Liquidity as a Measure of UMP**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread and excess liquidity.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQGQMXyY3kb2Y8XFtcfTw7BdUv21uuwcm9yqMZncK7N63khnT9b9-a3g2Ccs1HxDQ3XseOzom06mwDNtBpo6Kgl-zKou4qT6nWh_hwQe_NSyA61sHhtBLGBLghlQsYL213_sxvpttA=w1280-h906-v0?authuser=1)

104 International Journal of Central Banking September 2016
**Figure 8. Euro-Area Responses to UMP Shocks: Shocks to UMP Liquidity Variable**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEkec1ypadsw74IWTqudRlBqi76p8QlY27HSWMHp6-jy7f9DJnfJHjOj4wMUjGOqiMMZG-qJzi1wmVleZ3-RmNd-q-HqRYRXvSoWH5KjQWQ5arKFOLT2arxSH79JE913XegT83cRw=w1280-h896-v0?authuser=1)

Vol. 12 No. 3 Beggar-Thy-Neighbor? 105
**Figure 9. Euro-Area Responses UMP Shocks: Shocks to UMP Sovereign Bond Variable**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQGja-hzKFXfC5OwtA1aiQuZkc7ykqvp5DPXijtyoO9tGAAZyJWhsVHxn8KJICQzZNpqIo5raM7f9PCaY6P7vyuih2Gyx2ksfEuuv5-MVI8JFqgIsQOHj4YAwmyIutEa029Ea_on=w1280-h960-v0?authuser=1)

106 International Journal of Central Banking September 2016
**Figure 10. Swedish Responses to UMP Shocks: Sample with Sweden UMP Measures**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread in absolute terms.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEIF2rb-nMAnf7XBiHg9-D5OkTH-chi9nUdfeGdwOrLzbvlw0JI7lkIJhjK_Jz9WSeNuwAM04ei-7hkNXSYnoSokv5dv6yd-UFMTCfmH12Af9uvplihYkhHLWkcatxg7FtsmTBD5w=w1280-h952-v0?authuser=1)

Vol. 12 No. 3 Beggar-Thy-Neighbor? 107
**Figure 11. Swedish Responses to UMP Shocks: Sample without Sweden UMP Measures**
**Notes:**The shaded regions report point-wise 68 percent credible intervals. The horizontal axis reports weeks; the vertical axis reports monthly growth rates for all variables but the liquidity spread in absolute terms.
108 International Journal of Central Banking September 2016
**Figure 12. Real Activity Dynamics in the Nine Countries**
2009 2009.5 2010 2010.5 2011 2011.5 2012 2012.5 2013 2013.5 2014 93
94
95
96
97
98
99
100
101
102
103
**Notes:**The horizontal axis reports time; the vertical axis reports the level of the IP index.
**Figure 13. Financial Dynamics in the Nine Countries**
2009 2009.5 2010 2010.5 2011 2011.5 2012 2012.5 2013 2013.5 2014 -150
-100
-50
0
50
100
150
200
CZ DK HU NO PO SE
**Notes:**The figure reports the dynamics of the first principal component of stock prices, liquidity, and risk spreads. The horizontal axis reports time; the vertical axis reports monthly growth rates.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 109
**Figure 14. Group Responses to Euro-Area UMP Shocks**
0 2 4 6 8 10 12 14 16 -1
-0.5
0
0.5
1**Industrial Production**
0 2 4 6 8 10 12 14 16 -0.4
-0.2
0
0.2
0.4**Inflation**
0 2 4 6 8 10 12 14 16 -0.3
-0.2
-0.1
0
0.1**Real Exchange Rate**
0 2 4 6 8 10 12 14 16 -0.2
-0.1
0
0.1
0.2
0.3**Stock Prices**
0 2 4 6 8 10 12 14 16 -0.06
-0.04
-0.02
0
0.02
0.04**Liquidity Spread**
0 2 4 6 8 10 12 14 16 -2
-1
0
1
2**Risk (CDS)**
Advanced CEE SEE
**Notes:**The solid lines report point-wise average posterior median responses in deviations from euro-area responses. The dotted lines report point-wise 68 percent credible intervals. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread.
110 International Journal of Central Banking September 2016
**Figure 15. Foreign Responses to Conventional Euro-Area Interest Rate Shocks**
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock corresponds to 10 monthly basis points.
**Figure 16. Foreign Responses to Euro-Area Announcement Shocks**
2 4 6 8 10 12 14 16
-3
-2
-1
0
**Advanced**
**Output**
2 4 6 8 10 12 14 16
0
0.5
1
**Inflation**
2 4 6 8 10 12 14 16
-1
-0.5
0
**Exchange Rate**
2 4 6 8 10 12 14 16
-0.4
-0.2
0
0.2
0.4
**Stock Prices**
2 4 6 8 10 12 14 16 0
0.2
0.4
**Liquidity**
2 4 6 8 10 12 14 16
-3 -2 -1 0 1
**Risk (CDS)**
SE NO SW DK
2 4 6 8 10 12 14 16 0
0.2
0.4
0.6
0.8**CEE**
2 4 6 8 10 12 14 16
-0.1
0
0.1
2 4 6 8 10 12 14 16 0
0.2
0.4
0.6
2 4 6 8 10 12 14 16
-0.6
-0.4
-0.2
0
2 4 6 8 10 12 14 16
-0.01
0
0.01
0.02
2 4 6 8 10 12 14 16
-1
0
1
CZ PO
2 4 6 8 10 12 14 16
-0.6 -0.4 -0.2
0 0.2
**SEE**
2 4 6 8 10 12 14 16 -0.2
-0.1
0
0.1
2 4 6 8 10 12 14 16
-0.1
0
0.1
0.2
0.3
2 4 6 8 10 12 14 16
-0.5
0
0.5
1
2 4 6 8 10 12 14 16
-0.8 -0.6 -0.4 -0.2
0
2 4 6 8 10 12 14 16
-4
-2
0
HU RO BG
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is one policy announcement.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 111
**Figure 17. Foreign Responses to Euro-Area UMP Shocks: Identification R1**
0 2 4 6 8 10 12 14 16 -0.6
-0.4
-0.2
0
0.2
0.4
0.6**Industrial Production**
0 2 4 6 8 10 12 14 16 -0.2
0
0.2
0.4
0.6**Inflation**
0 2 4 6 8 10 12 14 16 -0.3
-0.2
-0.1
0
0.1**Real Exchange Rate**
0 2 4 6 8 10 12 14 16 -0.08
-0.06
-0.04
-0.02
0
0.02**Stock Prices**
0 2 4 6 8 10 12 14 16 -0.4
-0.2
0
0.2
0.4
0.6**Liquidity Spread**
0 2 4 6 8 10 12 14 16 -3
-2
-1
0
1
2**Risk (CDS)**
SE NO SW CZ PO HU RO BG DK
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is one stan-dard deviation of UMP growth (a 10 percent monthly increase in the quantity of UMP).
112 International Journal of Central Banking September 2016
**Figure 18. Foreign Responses to Euro-Area UMP Shocks: Identification R2**
0 2 4 6 8 10 12 14 16 -0.6
-0.4
-0.2
0
0.2
0.4
0.6**Industrial Production**
0 2 4 6 8 10 12 14 16 -0.4
-0.2
0
0.2
0.4
0.6**Inflation**
0 2 4 6 8 10 12 14 16 -0.3
-0.2
-0.1
0
0.1**Real Exchange Rate**
0 2 4 6 8 10 12 14 16 -3
-2
-1
0
1
2**Stock Prices**
0 2 4 6 8 10 12 14 16 -0.4
-0.2
0
0.2
0.4**Liquidity Spread**
0 2 4 6 8 10 12 14 16 -0.08
-0.06
-0.04
-0.02
0
0.02**Risk (CDS)**
SE NO SW CZ PO HU RO BG DK
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is one stan-dard deviation of UMP growth (a 10 percent monthly increase in the quantity of UMP).
Vol. 12 No. 3 Beggar-Thy-Neighbor? 113
**Figure 19. Foreign Responses to Euro-Area UMP Shocks: Identification R3**
0 2 4 6 8 10 12 14 16 -0.5
0
0.5
1**Industrial Production**
0 2 4 6 8 10 12 14 16 -0.4
-0.2
0
0.2
0.4
0.6**Inflation**
0 2 4 6 8 10 12 14 16 -0.4
-0.3
-0.2
-0.1
0
0.1**Real Exchange Rate**
0 2 4 6 8 10 12 14 16 -0.3
-0.2
-0.1
0
0.1
0.2
0.3**Stock Prices**
0 2 4 6 8 10 12 14 16 -1
-0.5
0
0.5**Liquidity Spread**
0 2 4 6 8 10 12 14 16 -3
-2
-1
0
1
2**Risk (CDS)**
SE NO SW CZ PO HU RO BG DK
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is one stan-dard deviation of UMP growth (a 10 percent monthly increase in the quantity of UMP).
114 International Journal of Central Banking September 2016
**Figure 20. Foreign Responses to Euro-Area UMP Shocks: Identification via Zero and Sign Restrictions**
0 2 4 6 8 10 12 14 16 -0.5
0
0.5
1**Industrial Production**
0 2 4 6 8 10 12 14 16 -0.1
-0.05
0
0.05
0.1
0.15**Inflation**
0 2 4 6 8 10 12 14 16 -0.15
-0.1
-0.05
0
0.05
0.1**Real Exchange Rate**
0 2 4 6 8 10 12 14 16 -0.3
-0.2
-0.1
0
0.1
0.2**Stock Prices**
0 2 4 6 8 10 12 14 16 -0.2
-0.1
0
0.1
0.2
0.3**Liquidity Spread**
0 2 4 6 8 10 12 14 16 -1
0
1
2
3**Risk (CDS)**
SE NO SW CZ PO HU RO BG DK
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is one stan-dard deviation of UMP growth (a 10 percent monthly increase in the quantity of UMP).
Vol. 12 No. 3 Beggar-Thy-Neighbor? 115
**Figure 21. Foreign Responses to Euro-Area UMP Shocks: Identification via Heteroskedasticity**
**Notes:**The lines report point-wise posterior median responses in deviations from euro-area responses. The x-axis reports weeks; the y-axis reports monthly growth rates for all variables but the liquidity spread. The size of the shock is one stan-dard deviation of UMP growth (a 10 percent monthly increase in the quantity of UMP).
**References**
Abbassi, P., and T. Linzert. 2011. “The Effectiveness of Monetary Policy in Steering Money Market Rates during the Recent Finan-cial Crisis.” ECB Working Paper No. 1328.
Aizenman, J., M. Binici, and M. M. Hutchison. 2014. “The Trans-mission of Federal Reserve Tapering News to Emerging Financial Markets.” NBER Working Paper No. 19980.
Aizenman, J., M. D. Chinn, and H. Ito. 2015. “Monetary Pol-icy Spillovers and the Trilemma in the New Normal: Periphery
116 International Journal of Central Banking September 2016
Country Sensitivity to Core Country Conditions.” NBER Work-ing Paper No. 21128.
Altavilla, C., F. Canova, and M. Ciccarelli. 2015. “Monetary Pol-icy Pass-Through and Heterogeneous Bank Lending.” Technical Report.
Altavilla, C., D. Giannone, and M. Lenza. 2014. “The Financial and Macroeconomic Effects of the OMT Announcements.” Working Paper No. 352, Centre for Studies in Economics and Finance.
Angelini, P., S. Neri, and F. Panetta. 2011. “Monetary and Macro-prudential Policies.” Temi di discussione (Working Paper) No. 801, Bank of Italy, Economic Research and International Rela-tions Area.
Angeloni, I. 2012.*Monetary Policy Transmission in the Euro Area: A Study by the Eurosystem Monetary Transmission Network.*Cambridge: Cambridge University Press.
Beirne, J., L. Dalitz, J. Ejsing, M. Grothe, S. Manganelli, F. Monar, B. Sahel, M. Susec, J. Tapking, and T. Vong. 2011. “The Impact of the Eurosystem’s Covered Bond Purchase Programme on the Primary and Secondary Markets.” ECB Occasional Paper No. 122.
Bernanke, B. S. 2010. “Opening Remarks: The Economic Out-look and Monetary Policy.” In*Macroeconomic Challenges: The Decade Ahead,*1–16. Proceedings of the Annual Economic Pol-icy Symposium sponsored by the Federal Reserve Bank of Kansas City, Jackson Hole, Wyoming, August 26–28.
Bhattarai, S., A. Chattarjee, and W. Y. Park. 2015. “The Effects of U.S. Quantitative Easing on Emerging Markets.” Technical Report, University of Illinois.
Boeckx, J., M. Dossche, and G. Peersman. 2014. “Effectiveness and Transmission of the ECB’s Balance Sheet Policies.” CESifo Working Paper No. 4907.
Borstel, J., S. Eickmeier, and L. Krippner. 2015. “The Interest Rate Pass-Through in the Euro Area during the Sovereign Debt Cri-sis.” Discussion Paper No. 10/2015, Deutsche Bundesbank.
Bruno, V., and H. S. Shin. 2015a. “Capital Flows and the Risk-Taking Channel of Monetary Policy.”*Journal of Monetary Eco-nomics*71: 119–32.
———. 2015b. “Cross-Border Banking and Global Liquidity.”*Review of Economic Studies*82 (2): 534–64.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 117
Canova, F. 2005. “The Transmission of US Shocks to Latin Amer-ica.”*Journal of Applied Econometrics*20 (2): 229–51.
Carrera, C., F. P. Forero, and N. Ramirez-Rondan. 2015. “Effects of U.S. Quantitative Easing on Latin American Economies.” Work-ing Paper No. 2015-35, Peruvian Economic Association.
Carter, C. K., and R. Kohn. 1994. “On Gibbs Sampling for State Space Models.”*Biometrika*81 (3): 541–53.
Cecioni, M., G. Ferrero, and A. Secchi. 2011. “Unconventional Mon-etary Policy in Theory and in Practice.” Questioni di Economia e Finanza (Occasional Paper) No. 102, Bank of Italy, Economic Research and International Relations Area.
Cetorelli, N., and L. S. Goldberg. 2012. “Banking Globalization and Monetary Transmission.”*Journal of Finance*67 (5): 1811–43.
Chen, Q., A. J. Filardo, D. He, and F. Zhu. 2012. “International Spillovers of Central Bank Balance Sheet Policies.” SSRN Schol-arly Paper No. 2185394.
Chinn, M. D. 2013. “Global Spillovers and Domestic Monetary Pol-icy.” BIS Working Paper No. 436.
Chiu, C. W. J., B. Eraker, A. T. Foerster, T. B. Kim, and H. D. Seoane. 2011. “Estimating VARs Sampled at Mixed or Irregular Spaced Frequencies: A Bayesian Approach.” Technical Report.
Christoffel, K., G. Coenen, and A. Warne. 2008. “The New Area-Wide Model of the Euro Area: A Micro-founded Open-Economy Model for Forecasting and Policy Analysis.” ECB Working Paper No. 944.
Ciccarelli, M., A. Maddaloni, and J.-L. Peydro. 2013. “Heteroge-neous Transmission Mechanism: Monetary Policy and Financial Fragility in the Euro Area.”*Economic Policy*28 (75): 459–512.
Cushman, D. O., and T. Zha. 1997. “Identifying Monetary Policy in a Small Open Economy under Flexible Exchange Rates.”*Journal of Monetary Economics*39 (3): 433–48.
Darracq Paries, M., and R. A. De Santis. 2013. “A Non-standard Monetary Policy Shock: The ECB’s 3-Year LTROs and the Shift in Credit Supply.” ECB Working Paper No. 1508.
Dedola, L., G. Rivolta, and L. Stracca. 2015. “If the Fed Sneezes, Who Gets a Cold?” Mimeo.
Devereux, M., E. Young, and C. Yu. 2015. “A New Dilemma: Cap-ital Controls and Monetary Policy in Sudden Stop Economies.” NBER Working Paper No. 21791.
118 International Journal of Central Banking September 2016
Dungey, M., and A. Pagan. 2009. “Extending a SVAR Model of the Australian Economy.”*The Economic Record*85 (268): 1–20.
Foroni, C., and M. Marcellino. 2013. “Mixed Frequency Structural Models Identification, Estimation, and Policy Analysis.” Work-ing Paper No. 2013/06, Norges Bank.
Fratzscher, M., M. Lo Duca, and R. Straub. 2013. “On the Interna-tional Spillovers of US Quantitative Easing.” Discussion Paper No. 1304, DIW Berlin.
Gagnon, J., M. Raskin, J. Remache, and B. Sack. 2011. “Large-scale Asset Purchases by the Federal Reserve: Did They Work?”*Eco-nomic Policy Review*(Federal Reserve Bank of New York) 17 (1, May): 41–59.
Gambacorta, L., B. Hofmann, and G. Peersman. 2012. “The Effectiveness of Unconventional Monetary Policy at the Zero Lower Bound: A Cross-Country Analysis.” BIS Working Paper No. 384.
Ghysels, E., J. Idier, S. Manganelli, and O. Vergote. 2013. “A High Frequency Assessment of the ECB Securities Markets Pro-gramme.” SSRN Scholarly Paper No. 2365833.
Gopinath, G. 2015. “The International Price System.” Technical Report, Harvard University.
International Monetary Fund. 2013. “Central, Eastern and South-eastern Europe—Financing Future Growth: The Evolving Role of Banking Systems in CESEE.” Central Eastern and Southeast-ern Europe: Regional Economic Issues Series.
Kilian, L. 2011. “Structural Vector Autoregressions.” CEPR Discus-sion Paper No. 8515.
Kim, S., and N. Roubini. 2000. “Exchange Rate Anomalies in the Industrial Countries: A Solution with a Structural VAR Approach.”*Journal of Monetary Economics*45 (3): 561–86.
Krishnamurthy, A., and A. Vissing-Jorgensen. 2011. “The Effects of Quantitative Easing on Interest Rates: Channels and Implica-tions for Policy.”*Brookings Papers on Economic Activity*43 (2, Fall): 215–87.
Kulikov, D., and A. Netsunajev. 2013. “Identifying Monetary Policy Shocks via Heteroskedasticity: A Bayesian Approach.” Working Paper No. 2013-9, Bank of Estonia.
Lenza, M., H. Pill, and L. Reichlin. 2010. “Monetary Policy in Excep-tional Times.”*Economic Policy*25 (62): 295–339.
Vol. 12 No. 3 Beggar-Thy-Neighbor? 119
Lewis, V., and M. Roth. 2015. “The Financial Market Effects of the ECB’s Balance Sheet Policies.” Technical Report, Deutsche Bundesbank.
Lim, J. J. 2014. “Tinker, Taper, QE, Bye? The Effect of Quantitative Easing on Financial Flows to Developing Countries.”
Lo Duca, M., M. Fratzscher, and R. Straub. 2014. “ECB Unconven-tional Monetary Policy Actions: Market Impact, International Spillovers and Transmission Channels.” Policy Research Working Paper No. 6820, World Bank.
Mackowiak, B. 2007. “External Shocks, U.S. Monetary Policy and Macroeconomic Fluctuations in Emerging Markets.”*Journal of Monetary Economics*54 (8): 2512–20.
Mishkin, F. S. 2001. “The Transmission Mechanism and the Role of Asset Prices in Monetary Policy.” NBER Working Paper No. 8617.
Moessner, R. 2014. “International Spillovers from US Forward Guid-ance to Equity Markets.” DNB Working Paper No. 427.
Neely, C. J. 2010. “The Large Scale Asset Purchases Had Large International Effects.” Working Paper No. 2010-018, Federal Reserve Bank of St. Louis.
Ongena, S., I. Schindele, and D. Vonnak. 2015. “In Lands of Foreign Currency Credit, Bank Lending Channels Run Through?” SSRN Scholarly Paper ID 2507688.
Passari, E., and H. Rey. 2015. “Financial Flows and the International Monetary System.” NBER Working Paper No. 21172.
Peersman, G. 2012. “Effectiveness of Unconventional Monetary Pol-icy at the Zero Lower Bound.” 2012 Meeting Paper No. 400, Society for Economic Dynamics.
Qian, H. 2013. “Vector Autoregression with Mixed Frequency Data.” MPRA Paper No. 47856.
Rajan, R. 2014. “Competitive Monetary Easing: Is It Yesterday Once More?” Remarks at the Brookings Institution, Washington, DC, April 10.
Rey, H. 2013. “Dilemma not Trilemma: The Global Financial Cycles and Monetary Policy Independence.” Technical Report, London Business School.
Rigobon, R. 2003. “Identification Through Heteroskedasticity.”*Review of Economics and Statistics*85 (4): 777–92.
120 International Journal of Central Banking September 2016
Rogers, J. H., C. Scotti, and J. H. Wright. 2014. “Evaluating Asset-Market Effects of Unconventional Monetary Policy: A Cross-Country Comparison.”
Russell, S. 1992. “Understanding the Term Structure of Interest Rates: The Expectations Theory.”*Review*(Federal Reserve Bank of St. Louis) 74 (4): 36–50.
Santis, R. A., and P. Surico. 2013. “Bank Lending and Monetary Transmission in the Euro Area.”*Economic Policy*28 (75): 423– 57.
Szczerbowicz, U. 2015. “The ECB Unconventional Monetary Poli-cies: Have They Lowered Market Borrowing Costs for Banks and Governments?”*International Journal of Central Banking*11 (4, December): 91–127.
Taylor, J. B., and J. C. Williams. 2008. “A Black Swan in the Money Market.” NBER Working Paper No. 13943.
World Economic Forum. 2012. “The Financial Development Report 2012.” Insight Report.