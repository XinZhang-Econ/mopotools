
### Unconventional Monetary Policy and the Great Recession: Estimating the Macroeconomic
### Effects of a Spread Compression at the Zero Lower*Bound∗*
Christiane Baumeistera and Luca Benatib aBank of Canada
bUniversity of Bern
We explore the macroeconomic effects of a compression in the long-term bond yield spread within the context of the Great Recession of 2007–09 via a time-varying parame-ter structural VAR model. We identify a “pure” spread shock defined as a shock that leaves the policy rate unchanged, which allows us to characterize the macroeconomic consequences of a decline in the yield spread induced by central banks’ asset purchases within an environment in which the policy rate is constrained by the effective zero lower bound. Two key findings stand out. First, compressions in the long-term yield spread exert a powerful effect on both output growth and inflation. Second, conditional on available estimates of the impact of the Federal Reserve’s and the Bank of England’s asset pur-chase programs on long-term yield spreads, our counterfactual
*∗We*wish to thank Pierpaolo Benigno, Jeffrey Campbell, Marcelle Chauvet, James Hamilton, Lutz Kilian, Mathias Trabandt, John Williams, and our dis-cussants Tino Berger, Gabriel Bruneau, Márcio Garcia, and Domenico Giannone as well as seminar participants at the Bank of England, Bundesbank, Carleton University, ECB, IMF, Norges Bank, Universidade do Minho, Universiteit van Pretoria, and University of California at San Diego for useful comments and sug-gestions. The opinions expressed herein are those of the authors and do not neces-sarily reflect the views of the Bank of Canada. Part of this paper was written while Christiane Baumeister was visiting the European Central Bank, which she thanks for its kind hospitality. Author contact: Baumeister: International Economic Analysis Department, Bank of Canada, 234 Wellington Street, Ottawa, Ontario, K1A 0G9, Canada. E-mail: cbaumeister@bankofcanada.ca. Benati: Department of Economics, University of Bern, Schanzeneckstrasse 1, CH-3001 Bern, Switzer-land. E-mail: luca.benati@vwi.unibe.ch.
165
166 International Journal of Central Banking June 2013
simulations suggest that U.S. and U.K. unconventional mone-tary policy actions have averted significant risks both of defla-tion and of output collapses comparable to those that took place during the Great Depression.
JEL Codes: C11, C32, E52, E58.
“The decisive policy easing by the Fed and the ECB during the crisis, and the adoption of unconventional measures by the two central banks, was crucial in countering the threat of deflation in the current episode.”
—Athanasios Orphanides1
**1. Introduction**
In response to the 2007–09 financial crisis, all major central banks aggressively lowered their policy rate. Once the effective zero lower bound on the short-term nominal interest rate was reached, policy-makers resorted to unconventional tools to provide further stimulus in light of the significant deterioration of economic conditions and the perceived risks of deflation. Among these non-standard monetary policy operations, the large-scale asset purchases conducted by the Federal Reserve and the Bank of England from early 2009 onwards attracted considerable attention. These operations entailed with-drawing large quantities of longer-term Treasury securities from the private sector through purchases in the secondary market, thereby changing the relative supplies of short-term and long-term bonds and other assets available to the public. The primary objective of these quantitative easing policies, as they are commonly referred to, was to put downward pressure on long-term interest rates in order to support private borrowing of households and businesses, thus spurring aggregate demand and real economic activity. This paper addresses two questions. First, we investigate how effective central banks’ unconventional monetary policy actions in the form of government-bond purchases were in countering the recessionary
1Keynote speech by Athanasios Orphanides, Governor, Central Bank of Cyprus, at the International Research Forum on Monetary Policy, Federal Reserve Board, March 27, 2010.
Vol. 9 No. 2 Unconventional Monetary Policy 167
shocks associated with the 2007–09 financial crisis. The underlying thought experiment is a counterfactual simulation of how output, inflation, and unemployment would have evolved had the asset pur-chase programs never existed. Second, we evaluate more generally how powerful central bank interventions are at the zero lower bound, when the traditional instruments for conducting monetary policy are no longer available.
In order to quantify the macroeconomic implications of these policies, it is necessary to establish first how effective large-scale asset purchases are at compressing the government-bond yield spread once the zero lower bound becomes binding. The latter question has been addressed by a number of recent papers, including Doh (2010), Gagnon et al. (2011), Krishnamurthy and Vissing-Jorgensen (2011), D’Amico and King (2012), and Hamilton and Wu (2012) for the United States, and Meier (2009) and Joyce et al. (2011) for the United Kingdom. These studies employ a variety of time-series and event-study approaches, and all reach the conclusion that the asset purchase programs were successful at flattening the yield curve. In fact, they find a substantial reduction in longer-term yields as a result of balance sheet policies.
Assessing the financial market effects of asset purchases is only a first step in gauging the effectiveness of unconventional monetary policy actions, however, because the ultimate goal of the central bank is to counteract deflationary pressures and to foster economic growth and employment. Our paper focuses on this latter question. Specifically, we take the estimates of the effects of government-bond purchases on the spread as given and ask what the macro-economic consequences of a compression in the yield spread are when short-term interest rates are constrained by the zero lower bound.
Chung et al. (2012) recently addressed this question within the Federal Reserve Board’s large-scale macroeconomic model. Their counterfactual simulations indicate that the expansion of the Federal Reserve’s balance sheet has kept the unemployment rate from rising to levels that would have prevailed in the absence of asset purchases and has likely averted a deflationary spiral for the U.S. economy. Similar conclusions are reached by Del Negro et al. (2011) and Chen, Cúrdia, and Ferrero (2012) based on medium-sized dynamic sto-chastic general equilibrium (DSGE) models with an explicit role for the zero bound on nominal interest rates. Lenza, Pill, and Reichlin
168 International Journal of Central Banking June 2013
(2010) also assess the macroeconomic effects of a decline in interest rate spreads for a given level of the policy rate for the euro area. They focus on the likely impact of the ECB’s non-standard policy actions on the short end of the yield curve by contrasting macroeco-nomic outcomes resulting from a policy versus a no-policy scenario which differ only in the evolution of short-term interest rates. Put differently, in order to gauge the effectiveness of policy interven-tion in warding off disastrous macroeconomic consequences, they conduct a forecasting exercise of key variables conditional upon a counterfactual path and an observed path of money-market rates based on a reduced-form large Bayesian VAR model estimated over the pre-crisis period. While they show that the narrowing of spreads induces economic stimulus, these beneficial effects take hold only with a considerable delay.
A common feature of all these analyses is that they build on the premise that the historically observed relationships uncovered in the data have not been affected by the most recent episode of financial turmoil. There is reason to doubt that the underlying behavioral relationships have remained unaltered given the severe economic dis-locations in the aftermath of the financial crisis. We instead propose to explore the macroeconomic effects of a compression in the long-term bond yield spread within the context of the Great Recession of 2007–09 by estimating a time-varying parameter structural VAR (TVP-VAR) model for the U.S. and the U.K. economies. Within this framework, we define a “pure” spread shock as a disturbance that leaves the short-term policy rate unchanged, which allows us to characterize the responses of macroeconomic aggregates to a decline in long-term yield spreads induced by central banks’ bond purchase programs under circumstances where the short rate cannot move, which is exactly the situation encountered at the zero lower bound. This shock is identified by means of a combination of sign restrictions and a*single*zero restriction.
Our empirical analysis yields several intriguing results. First, we show that a compression in the long-term yield spread exerts a powerful positive effect on both output growth and inflation when monetary policy is constrained by the effective zero lower bound. Second, our evidence clearly highlights the importance of allowing for time variation in the transmission of a spread compression to the macroeconomy. For example, the effect on U.S. inflation was
Vol. 9 No. 2 Unconventional Monetary Policy 169
particularly large during the Great Inflation of the 1970s, the reces-sion of the early 1990s, and the most recent past, whereas the 1990s were characterized by significantly weaker responses. By the same token, in the United Kingdom the impact on both inflation and out-put growth appears to have become stronger in recent years. This implies, for the present purposes, that the use of fixed-coefficient models estimated over (say) the last two decades would underesti-mate the macroeconomic impact resulting from yield spread com-pressions engineered by central banks via asset purchase programs in offsetting the adverse shocks associated with the 2007–09 finan-cial crisis. Third, conditional on Gagnon et al.’s (2011) estimates of the impact of the Federal Reserve’s bond purchases on the ten-year government-bond yield spread, our counterfactual simulations indi-cate that U.S. unconventional monetary policy actions have averted significant risks both of deflation and of severe output collapses com-parable to those that took place during the Great Depression. We show that without the large-scale asset purchase program, the U.S. economy would have been in deflation for two quarters with annual-ized inflation being as low as –1 percent in 2009:Q2, annualized real GDP growth would have contracted by 10 percent in the first quarter of 2009, and the unemployment rate would have been consistently above its actual value throughout 2009, reaching 10.6 percent at the end of 2009. A similar picture emerges for the United Kingdom conditional on Charlie Bean’s (2009) broad estimate of the impact of the Bank of England’s gilt purchases on long-term yield spreads, without which inflation would have fallen to –4 percent and output growth would have dropped by 12 percent at annual rates.
The remainder of the paper is structured as follows. The next section outlines the key features of the time-varying parameter VAR model, discusses the reasons for this modeling choice, and describes and motivates the identification strategy. Section 3 presents the empirical evidence. Section 4 concludes.
**2. Empirical Methodology**
The use of a time-varying parameter specification is of particular importance in the present context since it allows us to capture the macroeconomic structure in place during the Great Recession of 2007–09 when tracing the effects of a compression in the bond yield
170 International Journal of Central Banking June 2013
spread induced by central banks’ unconventional monetary policies. In this respect, the use of fixed-coefficient models would be unad-visable for at least two reasons. First, the notion that key structural macroeconomic relationships have remained unchanged in the face of the dramatic economic contraction associated with the financial crisis is entirely open to question. Second, at a very general level, there is widespread evidence of instabilities in macroeconomic time series (see, e.g., Stock and Watson 1996) and of changing volatility in the U.S. and the U.K. economies (see, e.g., McConnell and Pérez-Quirós 2000; Benati 2008). In fact, previous empirical studies of the transmission of*conventional*monetary policy provide evidence in support of models that feature smoothly evolving coefficients and heteroskedastic shocks (e.g., Primiceri 2005; Canova and Gambetti 2009; Koop, Leon-Gonzalez, and Strachan 2009; Baumeister, Liu, and Mumtaz 2013).
While many models may potentially be able to account for some time variation in the parameters, a TVP-VAR structure is the most flexible and encompassing model specification since it does not impose strong restrictions on the evolution of the economic rela-tionships. Although many periods over the sample are likely to be characterized by slow-moving but continuous structural changes, it cannot be excluded that the financial crisis led to a rupture in the economic structure due to its severity. However, as noted by Benati and Mumtaz (2007) and more formally demonstrated in Baumeis-ter and Peersman (2012, 2013) by means of a Monte Carlo study, drifting-coefficient models in practice are able to capture such dis-crete breaks if they occur.
*2.1 A Time-Varying Parameter VAR with Stochastic Volatility*
We model the joint behavior of the short-term nominal interest rate, the spread between the ten-year Treasury-bond yield and the pol-icy rate, GDP deflator inflation, and real GDP growth as aVAR(p)model with time-varying parameters and stochastic volatility as in Cogley and Sargent (2005), Primiceri (2005), and Cogley, Primiceri, and Sargent (2010):
Yt=B0,t+B1,tYt−1+*· · ·*+Bp,tYt−p+ut≡X*′*
tθt+ut,(1)
Vol. 9 No. 2 Unconventional Monetary Policy 171
whereYt≡[rt,st,πt,yt]′is anN×1vector of endogenous variables.2
The time-varying interceptsB0,tand the matrices of time-varying coefficientsB1,t...p,tare collected in the vectorθt,andXtis a matrix including lags ofYtand a constant to obtain the state-space rep-resentation of the model. Theutin the observation equation is anN*×*1 vector of unconditionally heteroskedastic disturbance terms. The data frequency is quarterly. Consistent with the vast majority of papers in the literature, and for reasons of computational fea-sibility, the lag order is set top= 2. Following, e.g., Cogley and Sargent (2002, 2005), and Primiceri (2005), the VAR’s time-varying parametersθtare postulated to evolve according to
p(θt∣θt−1,Qt)=I(θt)f(θt∣θt−1,Qt)(2)
withI(θt)being an indicator function that rejects unstable draws, thereby enforcing a stationarity constraint on the VAR,3 and withf(θt*|*θt−1,Qt)given by
θt=θt−1+ηt(3)
withηt≡[η1,t,η2,t,...,ηN⋅(1+Np),t]′,whereηt*∼*N(0,Qt).In the spirit of Cogley, Primiceri, and Sargent (2010), we introduce a stochastic volatility specification for the evolution of the covari-ance matrix of the innovations in the law of motion of the VAR coefficients,Qt.Specifically, we assume thatQtis given by
Qt≡
⎡⎢⎢⎣
q1,t0 . . . 0 0q2,t. . . 0
. . . . . . . . . . . . 0 0 . . .qN⋅(1+Np),t
⎤⎥⎥⎦(4)
with theqi,t’s,i=1,...,N*·*(1 +Np),evolving as geometric ran-dom walks: lnqi,t= lnqi,t−1+ωi,t.This specification allows for
2The GDP deflator and real GDP were transformed to annualized quarter-on-quarter rates of growth, while the short-term rate and the yield spread are included in levels. For a description of the data sources for the United States and the United Kingdom, see appendix 1.
3It is important to be clear about the meaning of such a stationarity con-straint. Although inflation contains a stochastic trend due to the time-varying parameter specification (1), the constraint (2) implies that its fluctuations*around*such a trend cannot be explosive.
172 International Journal of Central Banking June 2013
a time-varying drift, which is a desirable feature since key macro-economic variables have been remarkably volatile during the Great Inflation of the 1970s, extremely stable during the Great Modera-tion period, and, in the case of output growth and interest rates, once again very volatile during the Great Recession. The tradi-tional, “first-generation” time-varying parameter models (see, e.g., Cogley and Sargent 2005; Primiceri 2005) have a hard time fitting such a pattern of time variation successfully, as they postulate that the extent of random-walk drift is constant over the sample. As a result, they tend to “underdrift” (that is, drift too little) during the Great Inflation and “overdrift” (that is, drift too much) during the Great Moderation, thus automatically distorting inference. Instead, a model that features a*time-specific*extent of random-walk time variation in the VAR’s coefficients is more appropriate to capture such changes over time in the macroeconomic structure. Specifically, it allows the dynamics of the time-varying coefficients “to lie dor-mant” in stable periods and to pick up speed in volatile periods in a data-driven way, depending on the information contained in the sample.4
The VAR’s reduced-form innovations in (1) are postulated to be zero-mean normally distributed with time-varying covariance matrixVar(ut)≡Ωtwhich, following established practice, we factor as
Ωt=A−1tHt(A−1
t*)′*. (5)
Htis a diagonal matrix that contains the stochastic volatilities that capture changes in the magnitude of structural shocks, andAtis a lower triangular matrix that models the contemporaneous interac-tions among the endogenous variables, which are defined as
4Note that this specification is somewhat simpler than the one suggested by Cogley, Primiceri, and Sargent (2010), who factor the covariance matrix of the innovations to the state equation for the time-varying parameters asQt=(B−1
s)′Hs,tB*−1*s, whereHs,thas exactly the same specification which we
postulated forQt,andBsis a lower triangular matrix with ones along the main diagonal and static covariance parameters. Thus, our specification is obtained from Cogley, Primiceri, and Sargent’s by settingBsequal to the identity matrix. Figure 7A in the online appendix (available at http://www.bankofcanada.ca/wp-content/uploads/2012/11/BB appendix.pdf) shows that our model accurately tracks the trends in inflation for the United States (panel A) and the United Kingdom (panel B), suggesting that this specification works well in our setting.
Vol. 9 No. 2 Unconventional Monetary Policy 173
Ht≡
⎡⎢⎢⎣
h1,t0 0 0 0h2,t0 0 0 0h3,t0 0 0 0h4,t
⎤⎥⎥⎦At≡
⎡⎢⎢⎣
1 0 0 0α21,t1 0 0α31,tα32,t1 0α41,tα42,tα43,t1
⎤⎥⎥⎦(6)
with thehi,t’sevolving as geometric random walks,
lnhi,t=lnhi,t−1+νi,t. (7)
As in Primiceri (2005), we postulate that the non-zero and non-unity elements of the matrixAt—whichwe collect in the vectorαt≡[α21,t,. . . ,α43,t]′—evolveas driftless random walks,
αt=αt−1+τt,(8)
and we assume the vector[ε′t,τ*′*
t,ν′t,ω′
t]*′,*withεtderived from the
relationshiput≡A−1tH
1 2tεt,to be distributed asN(0,V), with
V=
⎡⎢⎢⎣
I40 0 0 0S0 0 0 0Zν0 0 0 0Zω
⎤⎥⎥⎦,Zν=
⎡⎢⎢⎣
σ2ν,10 0 0 0σ2
ν,20 0 0 0σ2
ν,30 0 0 0σ2
ν,4
⎤⎥⎥⎦,and
Zω=
⎡⎢⎢⎣
σ2ω,10 . . . 0 0σ2
ω,2. . . 0 . . . . . . . . . . . . 0 0 . . .σ2
ω,N⋅(1+Np)
⎤⎥⎥⎦.(9)
Finally, following Primiceri (2005), we adopt the additional simpli-fying assumption of a block-diagonal structure forSof the following form:
S≡Var(τt)=
⎡⎣S1*01×2 01×3*
*02×1*S2*01×3 03×1 03×2*S3
⎤⎦(10)
withS1≡Var(τ21,t),S2≡Var([τ31,t,τ32,t]′),andS3≡Var([τ41,t,τ42,t,τ43,t]′),which implies that the non-zero and
174 International Journal of Central Banking June 2013
non-unity elements ofAtbelonging to different rows evolve indepen-dently. As discussed in Primiceri (2005, appendix A.2), this assump-tion drastically simplifies inference and increases the efficiency of the estimation algorithm in an already highly parameterized model since it allows us to do Gibbs sampling on the non-zero and non-unity elements ofAtequation by equation.
We estimate (1)–(10) via standard Bayesian methods described in Kim and Nelson (1999). Appendix 2 discusses our choices for the priors, describes the Markov chain Monte Carlo algorithm we use to simulate the joint posterior distribution of the hyperparameters and the states conditional on the data, and provides evidence of convergence to the ergodic distribution.
*2.2 Identification of a “Pure” Spread Shock*
A key insight that motivated the unconventional policy interven-tions in the Treasury market was that a narrowing of the long-short spread of government bonds spurs real economic activity and stems the decline in inflation by removing duration risk from portfolios of market participants and by reducing the borrowing costs for the private sector (see Bernanke 2006, 2010). Empirical evidence for a negative relationship between the term premium and future real eco-nomic activity has been provided by Rudebusch, Sack, and Swanson (2007), who show that a decline in the term premium of ten-year Treasury yields tends to boost GDP growth. Gilchrist, Yankov, and Zakraǰsek (2009), who study the transmission of credit spread shocks to the broader economy within a structural framework, demonstrate that an unexpected widening of credit spreads leads to a significant contraction of economic activity and a fall in prices. Eickmeier and Hofmann (2012) also show that a contractionary term spread shock that raises the yield spread lowers output and prices.
The sign restrictions we propose to recover the “pure” spread shock are in line with these stated policy objectives and previous empirical evidence that a compression in the spread should lead to higher levels of economic activity and exert upward pressure on inflation. However, the very nature of the question we are trying to answer—“What are the macroeconomic effects of a spread compres-sion in a situation in which the central bank leaves the policy rate unchanged?”—commands that the spread shock cannot possibly be
Vol. 9 No. 2 Unconventional Monetary Policy 175
recovered via sign restrictions alone, but requires a zero restriction on the impact response of the short-term interest rate. To extract the structural shock to the yield spread, we propose a novel identi-fication strategy that combines sign restrictions with a single zero restriction on impact. A key point to stress is that, for the present purpose, the identification of a “pure” spread shock—pure in the sense that it does not trigger a policy response—is of crucial impor-tance, since it allows us to explore the impact of a compression of the yield spread within an environment in which the policy rate is bound to stay unchanged for an extended period. During normal times, the pure spread shock can be thought of as any unexpected disturbance in financial markets to which the central bank does not feel com-pelled to respond on impact. Examples of this type of shock include shifts in liquidity preferences, in long-term inflation expectations, and in investors’ risk appetite and flight-to-quality considerations.
In addition, we identify three “traditional” shocks—monetary policy, demand non-policy, and supply—via a standard set of sign restrictions (see, e.g., Benati 2008; Benati and Goodhart 2010).5
Even though we are not genuinely interested in these three shocks given that our focus is on the pure spread shock, Canova and Paustian (2011) and Kilian and Murphy (2012) make the case that in order to pin down the shock of interest, all theoretically plausible restrictions ought to be imposed. While the responses of the spread after the supply and demand non-policy shocks are left unrestricted, postulating a flattening of the yield curve after a contractionary monetary policy shock can be motivated by imperfect pass-through along the term structure of interest rates given that short-term interest rates are only temporarily higher.
The contemporaneous restrictions on the responses of the short-term interest rate, the yield spread, inflation, and output growth characterizing each structural shock are summarized in table 1. It can be shown that this set of restrictions is sufficient to separate the various shocks from one another, thus achieving identification.
5See also Faust (1998), Canova and De Nicolò (2002), and Uhlig (2005). A key advantage of sign restrictions is that they are, in principle, fully compatible with general equilibrium models, while this is not necessarily the case for alternative identification schemes based on, e.g., exclusion restrictions (see Canova and Pina 2005).
176 International Journal of Central Banking June 2013
**Table 1. Identification Restrictions**
**Shock**
**Variable**εMPtεSpread
tεDemandtεSupply
t
Short Rate + O + ? Spread – – ? ? Inflation – + + – Output Growth – + + +
**Note:**? = left unconstrained.
We compute the time-varying structural impact matrix,A0,t,by combining the procedure proposed by Rubio-Ramı́rez, Waggoner, and Zha (2010) for imposing sign restrictions with the imposi-tion of a single zero restriction via a deterministic rotation matrix. Specifically, letΩt=PtDtP
*′*tbe the eigenvalue-eigenvector decom-
position of the VAR’s time-varying covariance matrixΩt,and letA~0,t≡PtD
1 2t. We draw anN*×*Nmatrix,K,from theN(0,1) dis-
tribution, we take theQRdecomposition ofK—thatis, we compute matricesQandRsuch thatK=Q*·*R,and we compute the time-varying structural impact matrix asAˉ0,t=A~0,t⋅Q′.We then impose a zero in the(1,2) position ofAˉ0,tvia an appropriate rotation ofAˉ0,t—specifically,by defining a rotation matrixRˉas
Rˉ=
⎡⎣cos(ϕ)−sin(ϕ)
sin(ϕ)cos(ϕ)02
02I2
⎤⎦(11)
withRˉ*·*Rˉ′=I4,whereI4is a 4*×*4 identity matrix. The rotation angleϕis defined asϕ=tan−1(Aˉ1,2
0,t/Aˉ1,10,t), where tan stands for
tangens andAˉi,j0,tdenotes the(i,j)element of the candidate impact
matrixAˉ0,tat timet,such that we obtain a new impact matrixA0,t=Aˉ0,t*·*Rˉthat has a zero in the(1,2) position. IfA0,tsatisfies the sign restrictions, we keep it; otherwise, we discard it. We repeat this procedure until we obtain an impact matrix that fulfills both the sign restrictions and the zero restriction at the same time.
Vol. 9 No. 2 Unconventional Monetary Policy 177
**3. Evidence on the Impact of a Compression in the Yield Spread**
In this section, we provide empirical evidence for the two questions posed in the introduction. First, conditional on available estimates of the impact of central banks’ asset purchase programs on long-term government-bond yield spreads, what role did unconventional mon-etary policy actions play within the context of the 2007–09 Great Recession? In particular, did the large-scale asset purchase programs instituted by the Federal Reserve and the Bank of England avert substantial risks of deflation and of output contractions, on a scale comparable to those which took place during the Great Depression? Second, how large is the impact of a compression in the long-term yield spread on inflation and output growth within an environment in which the short-term policy rate does not move, and has that impact changed over time?6 Before addressing these issues in turn, we assess the plausibility of our baseline model by looking at the dynamic effects of a conventional monetary policy tightening over time.
*3.1 Responses to a Conventional Monetary Policy Shock*
Since the reliability of our results ultimately depends upon the abil-ity of the empirical model to accurately capture the underlying structural relationships, it is instructive to get an idea about how well our model performs along a dimension that has been studied extensively in the literature. Therefore, a useful starting point for the analysis of the effects of unconventional monetary policy is a review of the responses to a traditional innovation in the monetary policy rule. This exercise helps ensure consistency with similar time-varying VAR models that have investigated changes in the monetary transmission mechanism.7
Figure 1, panels A and B, displays the time profile of the pos-terior median responses of inflation and of real output growth to
6In Baumeister and Benati (2010) we also provide evidence on this question for Japan and the euro area.
7Note that this comparison is useful also because we added the stochastic volatility component in the law of motion of the VAR coefficients which was absent in previous structural TVP studies about the transmission mechanism.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQH0aix9wIcvCQO2WEe-0uq1rrHMPbo-tW7SMz4Rk4ck1BxOntf1qVCq_JQdc7AgJl1p0bTQy4QrnrueJ2sO8LNisFAWp6SWL5iT9AI3BMJyOlrSvO_ZkhwADwhzJoZARoJQkal6kw=w1280-h1172-v0?authuser=1)

178 International Journal of Central Banking June 2013
**Figure 1. Time-Varying Median Responses of Inflation and Output Growth to a Contractionary Monetary Policy**
**Shock of 25 Basis Points**
an exogenous increase in the policy rate of 25 basis points for the United States and the United Kingdom, respectively, for a period of ten quarters after the contractionary monetary policy shock. We observe that the negative effect of a monetary tightening of equal size on inflation and on output growth becomes gradually stronger over the sample period in both economies. In particular, discretionary monetary policy in the United States induces a greater decline in real economic activity over time, while in the United Kingdom infla-tion falls by more since the introduction of the inflation-targeting regime. Both variables exhibit the largest responses during the past
Vol. 9 No. 2 Unconventional Monetary Policy 179
couple of years. These results are in line with previous evidence presented in Benati and Mumtaz (2007) and Canova and Gambetti (2009) for the United States and in Benati (2008) for the United Kingdom. The finding of a substantial drop in inflation and in out-put growth in response to a monetary policy contraction since the onset of the crisis cautions against recommending raising interest rates to stir inflation expectations as a strategy to exit the liquidity trap as advocated by, e.g., Schmitt-Grohé and Uŕıbe (2010) since such a policy is likely to exacerbate current economic conditions.
*3.2 Did Unconventional Monetary Policies Avert Catastrophic Outcomes?*
*3.2.1 The United States*
It would seem that unconventional central bank interventions in the Treasury market during 2009 should be readily reflected in the sequence of estimated structural shocks to the government-bond yield spread. Figure 2 plots the historical series of pure spread shocks, where the vertical line marks the first announcement of the large-scale asset purchase program by the Federal Reserve. As can be seen from the graph, spread shocks were mainly*positive*during the first round of asset purchases. This observation can be explained by the fact that spread shocks during 2009 were not just the result of central bank interventions but were also determined by crisis-related factors that were pushing up the spread. Specifically, the key moti-vation for conducting non-standard monetary policy operations was precisely that there were countervailing forces such as the drying up of liquidity, panic and strains on financial markets, etc., which were exerting upward pressures on the yield spread. This implies that sim-ply looking at the sequence of pure spread shocks is uninformative about what the spread would have been in the absence of central banks’ asset purchases and, hence, suppressing those shocks does not constitute a valid counterfactual to gauge the macroeconomic implications of unconventional policy measures.
One way to quantify whether unconventional monetary policy actions have reduced the threat of deflation and counteracted even larger output contractions is to generate a hypothetical sequence of spread shocks that undo the impact of balance sheet policies on
180 International Journal of Central Banking June 2013
**Figure 2. Historical Sequence of Structural Shocks to the Yield Spread for the United States, 1965:Q4 to 2011:Q4**
1970 1975 1980 1985 1990 1995 2000 2005 2010 -2.5
-2
-1.5
-1
-0.5
0
0.5
1
1.5
2
2.5 Pure spread shocks
**Note:**The vertical line indicates the announcement of the large-scale asset pur-chase program.
the term spread to obtain a counterfactual path for inflation and real GDP growth had the asset purchases not taken place.8 In their extensive empirical analysis of the effect of the Federal Reserve’s asset purchase programs on U.S. long-term yield spreads, Gagnon et al. (2011) conclude that
these purchases caused economically meaningful and long-lasting reductions in longer-term interest rates on a range of securities, including securities that were not included in the purchase programs. . . . Our results [based on time-series meth-ods] suggest that the $1.725 trillion in announced purchases reduced the 10-year term premium by between 38 and 82 basis points. This range of point forecasts overlaps considerably with
8See, e.g., Sims and Zha (2006) for a similar counterfactual analysis in relation to changes in the conduct of conventional monetary policy.
Vol. 9 No. 2 Unconventional Monetary Policy 181
that obtained in our event study, which is impressive given that entirely separate data and methodologies were used to obtain the results.
D’Amico and King (2012) find that the program as a whole resulted in a downward shift of the yield curve of about 50 basis points in the ten- to fifteen-year maturity segment. Chung et al. (2012) derive a long-run trajectory for the evolution of the effects of asset purchases on the yield spread that die out only gradually over the years based on a portfolio-balance model. While appealing, we adopt the simplifying assumption that the central bank intervenes in such a way as to maintain the initial effects over the lifetime of the program. This is consistent with evidence provided by D’Amico and King (2012). Furthermore, given the long horizons considered by Chung et al. (2012), the steady decline in term premium effects amounts only to a couple of basis points difference in the short run.
In what follows, we take Gagnon et al.’s (2011) time-series estimates as our benchmark measure of the impact of the Fed-eral Reserve’s asset purchases on U.S. long-term yield spreads— specifically, for illustrative purposes, we will consider the average between their lower and upper estimates of the impact on the ten-year government-bond yield spread, which is 60 basis points9—and we will tackle the question of what would have happened if the Fed-eral Reserve had not engineered such a yield spread compression via asset purchases. Specifically, we ask whether the U.S. economy would have fallen into prolonged deflation like Japan in the 1990s and whether the output collapse would have been as severe as during the Great Depression.
The graphs in the top panel of figure 3 report the results from the following counterfactual simulation. Starting in 2009:Q1, we rerun history
(i) conditional on the time-varying VAR’s estimated coefficients, (ii) keeping all the structural shocks except the one to the spread
unchanged at their estimated historical values, and
9Bomfim and Meyer (2010) also estimate the total impact of the asset pur-chases on the ten-year Treasury yield to amount to 60 basis points.
182 International Journal of Central Banking June 2013
**Figure 3. Counterfactual Simulations for U.S. Inflation, Output Growth, and Unemployment Rate for 2009**
**Eliminating the Impact on the Spread of the Federal Reserve’s Asset Purchases**
**2008Q2 Q4 2009Q2 Q4**
**-20**
**-15**
**-10**
**-5**
**0**
**5**
**2008Q2 Q4 2009Q2 Q4**
**-4**
**-3**
**-2**
**-1**
**0**
**1**
**2**
**3**
**2008Q2 Q4 2009Q2 Q4 0**
**0.1**
**0.2**
**0.3**
**0.4**
**0.5**
**0.6**
**0.7**
**0.8**
**0.9**
**1**
Actual inflation
16th percentile
84th percentileActual real GDP growth
Median
Inflation, actual and     counterfactual
Real GDP growth, actual       and counterfactual
Fractions of draws for which counterfactual     inflation is negative
**2008Q2 Q4 2009Q2 Q4**
**-12**
**-10**
**-8**
**-6**
**-4**
**-2**
**0**
**2**
**4**
**2008Q2 Q4 2009Q2 Q4**
**-1.5**
**-1**
**-0.5**
**0**
**0.5**
**1**
**1.5**
**2**
**2.5**
**3**
**3.5**
**2008Q2 Q4 2009Q2 Q4**
**6**
**7**
**8**
**9**
**10**
**11**
**12**
Inflation, actual and counterfactual corridor
Real GPD growth, actual and       counterfactual corridor
Unemployment rate, actual          and counterfactual
Vol. 9 No. 2 Unconventional Monetary Policy 183
(iii) recomputing the shocks to the spread such that the counter-factual path for the spread is, for the whole of 2009, 60 basis points higher than the actual historical path.10
The first and last columns of the figure report the medians and the 16th and 84th percentiles of the distributions of the counterfac-tual paths for inflation and real GDP growth, together with actual inflation and real GDP growth, respectively, whereas the middle column shows the fraction of draws from the posterior distribution for which the economy is in deflation. The figure portrays a sober-ing picture of what might have happened had the Federal Reserve not engineered yield spread compressions via its asset purchase pro-gram. Specifically, based on the median estimates, macroeconomic performance would clearly have been worse, with inflation slipping 1 percentage point below zero and output growth reaching a trough of –10 percent in the first quarter of 2009. These findings are in line with the results obtained by Chung et al. (2012), who also pro-vide evidence of substantial beneficial effects on inflation and real economic activity as a result of diminished long-term bond yields.
What is especially noteworthy in the top panel of figure 3, how-ever, are not the median projections, but rather the*risks*associated with such projections as measured by the probability of falling into the tails of the posterior distribution (see Kilian and Manganelli 2007). In particular, with regard to inflation, the fraction of draws for which counterfactual inflation would have been negative peaks at about 90 percent in 2009:Q2 and stays consistently around 80 percent over the next quarter before falling slightly below 20 per-cent. As for output growth, results are even more ominous, with the lower percentile reaching*–20 percent.*Although these figures may appear wildly implausible, it is important to keep in mind that in the fourth quarter of 1929, U.S. real GNP contracted, on a quarter-on-quarter annualized basis, by a remarkable*17.5 percent,*whereas over the three subsequent years (from 1930:Q1 to 1932:Q4) the aver-age quarter-on-quarter annualized rate of growth was equal to*–10.4*
10An important point to stress about this counterfactual simulation is that, since we are only manipulating structural shocks while leaving all other elements of the estimated SVAR unchanged, such a counterfactual is*not*vulnerable to Sargent’s (1979) criticism of SVAR-based policy counterfactuals.
184 International Journal of Central Banking June 2013
*percent.11*So, although the results portrayed in the top panel of figure 3 are outside the bounds of advanced countries’ post-WWII experience, they are definitely*not*outside the bounds of histori-cal experience; to the contrary, they are*exactly*in line with the experience of the U.S. Great Depression.
It is even possible to make a case that such counterfactual sim-ulations paint an excessively optimistic picture of policy inactive-ness. Consider the case of demand non-policy shocks. The estimated sequence of these shocks for 2009 is conditional on the Federal Reserve having announced and implemented its asset purchase pro-gram, which, among other things, contributed to “calm nerves” and steady markets. Had the Federal Reserve instead stood idle in the face of the crisis, business and consumer confidence would have dete-riorated further and would have collapsed eventually, which in turn would most likely have led to a “worse” sequence of demand non-policy shocks and, consequently, to worse macroeconomic perfor-mance across the board. This point has also been stressed by Chung et al. (2012), who suggest that simulation results may underestimate the beneficial effects of the program if the very existence of the pro-gram contributed to reduce concerns about extremely adverse tail events, thereby boosting household and business confidence in a way not captured in the model. We therefore conjecture that, rather than being unrealistically dire, our counterfactual scenario might in fact be*too rosy*and that economic conditions might have turned even worse.
Given the considerable amount of uncertainty surrounding the estimates of financial market effects of the first round of asset pur-chases, it is instructive to assess the range of macroeconomic implica-tions for the weakest and the strongest impact of policy interventions on yield spreads reported in the literature. Based on a term struc-ture model, Hamilton and Wu (2012) find that the Federal Reserve’s non-standard open-market operations reduced the ten-year Treas-ury yield by 13 basis points, which represents the lowest end of spectrum, while Neely (2010), using an event-study methodology, arrives at an estimated effect of large-scale asset purchases on the ten-year government-bond yield of –107 basis points. The first two
11These figures are based on the real GNP data found in Balke and Gordon (1986), appendix B, table 2.
Vol. 9 No. 2 Unconventional Monetary Policy 185
columns of the bottom panel of figure 3 display a counterfactual “corridor” for inflation and real GDP growth based on the median of the counterfactual paths obtained with the smallest and largest estimates for spread compressions.
There has been a lot of discussion about the deterioration of labor market conditions in the aftermath of the financial crisis. Therefore, we replace real GDP growth with the unemployment rate as an indi-cator of economic activity and evaluate how the unemployment rate would have evolved in the absence of the large-scale asset purchases. The last column of the bottom panel of figure 3 depicts the median counterfactual path for the unemployment rate together with the 16th and 84th percentiles of the posterior distribution, as well as the actual unemployment rate. It clearly emerges that the labor market performance would have been much worse for an extended period had the Federal Reserve not intervened, since the counterfac-tual path for unemployment is consistently above its observed value. This evidence is consistent with Chung et al. (2012), who report that the unemployment rate is 0.75 percentage points lower as a result of the implementation of the program.
Thus, while not being able to lift up the economy on the same growth path that prevailed in the pre-crisis period, our results indi-cate that large-scale purchases of Treasury securities worked as an engine for economic recovery and helped guard against prolonged deflation.
*3.2.2 The United Kingdom*
Even though we already established for the case of the United States that the sequence of historical spread shocks cannot be deemed a reliable guide to assess the effectiveness of unconventional monetary policy operations, for completeness, figure 4 displays the series of pure spread shocks for the United Kingdom, where the vertical line indicates the announcement of quantitative easing by the Bank of England (BoE). Interestingly, the shocks during the period of the policy intervention are rather small by historical standards, which would suggest that quantitative easing measures and countervailing forces were more balanced.
Nevertheless, as before, we proceed by conditioning our coun-terfactual simulations of the macroeconomic effects on previous
186 International Journal of Central Banking June 2013
**Figure 4. Historical Sequence of Structural Shocks to the Yield Spread for the United Kingdom, 1975:Q2 to 2011:Q4**
1980 1985 1990 1995 2000 2005 2010
-2
-1
0
1
2
3
Pure spread shocks
**Note:**The vertical line indicates the announcement of quantitative easing.
estimates of the compression in the spread as a result of quantitative easing. In a speech delivered in May 2009, the Bank of England’s Deputy Governor, Charlie Bean, thus spoke of the impact of the Bank’s asset purchase program on long-term yield spreads:
There are signs that these measures are having a beneficial impact. . . . Spreads on commercial paper eligible for purchase have fallen by around 1
2 percentage point and the size of the market has increased by around 10%. Similarly, average spreads on sterling investment grade corporate bonds for industrial com-panies have declined by some 60 basis points and gross issuance of bonds by UK companies has been strong. These developments may reflect a range of influences, but feedback from market participants suggests that our purchases have indeed played a helpful role.
His assessment is supported by empirical evidence presented in Meier (2009), who purports that the BoE’s purchases of U.K. gov-ernment bonds have reduced gilt yields by a range of at least 35–60
Vol. 9 No. 2 Unconventional Monetary Policy 187
**Figure 5. Counterfactual Simulations for U.K. Inflation and Output Growth for 2009 Eiminating the Impact on the Spread of the BoE’s Quantitative Easing Measures**
**2008Q2 Q4 2009Q2 Q4**
**-18**
**-16**
**-14**
**-12**
**-10**
**-8**
**-6**
**-4**
**-2**
**0**
**2**
**2008Q2 Q4 2009Q2 Q4 -10**
**-8**
**-6**
**-4**
**-2**
**0**
**2**
**4**
**6**
**2008Q2 Q4 2009Q2 Q4 0**
**0.1**
**0.2**
**0.3**
**0.4**
**0.5**
**0.6**
**0.7**
**0.8**
**0.9**
**1**
Fractions of draws for which counterfactual
inflation is negative Real GDP growth, actual
and counterfactual Inflation, actual and
counterfactual
Actual inflation
Actual real GDP growth
84th percentile
Median
16th percentile
**2008Q2 Q4 2009Q2 Q4 -16**
**-14**
**-12**
**-10**
**-8**
**-6**
**-4**
**-2**
**0**
**2**
**2008Q2 Q4 2009Q2 Q4 -8**
**-6**
**-4**
**-2**
**0**
**2**
**4**
**6**
Inflation, actual and counterfactual corridor
Real GDP growth, actual and counterfactual corridor
basis points and by Joyce et al. (2011), who arrive at estimates for the financial market effects of up to 100 basis points.
The graphs in the top panel of figure 5 show the results for the United Kingdom from the same counterfactual exercise we discussed
188 International Journal of Central Banking June 2013
earlier, in which we rerun the U.K. Great Recession based on the estimated SVAR but recompute the spread shocks for 2009 in such a way that the counterfactual path for the spread is 50 basis points higher than it has been historically. Unsurprisingly, the results are in line with those for the United States, with strong deflation of around 4 percent based on median estimates and a severe recession with real GDP growth reaching about –18 percent in the first quar-ter of 2009. The graphs in the bottom panel of figure 5 display the lower and upper bounds for the median estimates of the counterfac-tual paths for inflation and output growth conditional on the lowest (35 basis points) and highest (100 basis points) estimated decline in gilt yields as a result of quantitative easing. Once again, it is possible to make a convincing argument that these projections are actually optimistic in that they might understate the adverse macroeconomic outcomes absent policy interventions, for the same reason previously highlighted for the United States. We conclude that asset purchases were successful at counteracting the further weakening of real eco-nomic activity and at deflecting the threat of deflation also in the United Kingdom.
*3.3 How Powerful Is a Compression in the Yield Spread at the Zero Lower Bound?*
In what follows, we study the propagation of pure spread shocks under the assumption that the zero lower bound is binding for eight quarters after the spread compression. Given that for identifi-cation purposes a zero restriction on the nominal short-term rate is imposed only contemporaneously, we will constrain the policy rate to remain unchanged for eight quarters after the impact of the spread shock when computing the impulse responses. Postu-lating no response of the short-term interest rate despite higher output growth and inflation appears appropriate at the zero lower bound since the macroeconomic effects of policy-induced move-ments in the long-short spread should not be undermined by an increase in the policy rate. Otherwise, the central bank would defeat the purpose of its own unconventional monetary policy operations.
We employ two methodologies to take the zero-lower-bound con-straint into account. The first approach shuts down the systematic
Vol. 9 No. 2 Unconventional Monetary Policy 189
response of the central bank by “zeroing out” the coefficients in the structural interest rate rule, while the second approach computes a sequence of hypothetical monetary policy shocks that exactly off-sets the interest rate increase triggered by the expansionary spread shock.
*3.3.1 “Zeroing Out” the Structural Interest Rate Rule*
To examine the transmission of pure spread shocks in a constant-interest-rate environment, we subject the long-term yield spread to a one-time shock equal to –1 percent, but do not allow the short-term rate to react on impact—which is implied by the very way we extract such “pure” spread shocks—or over the subsequent eight quarters. We implement this additional restriction on the short-term interest rate by setting to zero all the coefficients in the structural VAR’s monetary policy rule, with the exception of the one on the short rate itself. To fix ideas, let the structural time-varying parameter VAR (henceforth, TVP-SVAR) representation be given by
A−10,tYt=A−1
0,tB1,tYt−1+*· · ·*+A−10,tBp,tYt−p+εt,(12)
whereYt≡[Rt,X*′*t]
*′*is anN*×1*vector of endogenous variables, withRtbeing the nominal short-term rate andXtbeing an(N*−*1)*×*1 vector of variables other thanRt,including the spread, inflation, and real output growth;A0,tbeing the impact matrix of the structural shocks at timet;B1,t,...,Bp,tbeing the time-varying autoregres-sive matrices of the VAR; andεt=A−1
0,tutbeing a vector collecting the VAR’s structural innovations, whereutis theN*×*1 vector con-taining the VAR’s reduced-form shocks. The vectorεtis defined asεt≡[εR,t,ε′
˜R,t]*′,*whereεR,tis the conventional monetary policy
shock andε˜R,tis a vector collecting all the structural shocks other thanεR,t.DefineB~0,t≡A−1
0,t,B~1,t≡A−10,tB1,t,...,B~p,t≡A−1
0,tBp,t,and partitionB~0,t,B~1,t,...,B~p,tas
B~0,t=
[B~R
0,t
B~˜R0,t
] ,B~1,t=
[B~R
1,t
B~˜R1,t
] , . . . ,B~p,t=
[B~R
p,t
B~˜Rp,t
] . (13)
190 International Journal of Central Banking June 2013
Leaving the short-term rate unchanged after the impact period is achieved by “zeroing out” the relevant elements of the matricesB~0,t,B~1,t,...,B~p,tin (13) as follows:
B~∗0,t=
[B~R
0,t,1101×(N−1)
B~˜R0,t
] ,B~∗
1,t=
[01×N
B~˜R1,t
] , . . . ,B~∗
p,t=
[01×N
B~˜Rp,t
],
(14)
whereB~R0,t,11is the (1,1) element ofB~0at timet.The dynamics of
the system after the initial impact is then described by the reduced-form VAR implied byB~∗
0,t,B~∗1,t,...,B~
*∗*p,t.From the ninth quarter
after the impact onwards, we allow the TVP-SVAR’s monetary rule to “kick in,” and hence use the original matricesB1,t,...,Bp,trather than those implied byB~∗
0,t,B~∗1,t,...,B~
*∗*p,t.
Figures 6 and 7 show, for the United States and the United King-dom, the median time-varying impulse response functions (hence-forth, IRFs) of the policy rate, the yield spread, GDP deflator infla-tion, and real GDP growth, to an unexpected decrease in the spread of 100 basis points for the entire sample period.12 Several findings are readily apparent from these figures. First, the IRFs of the spread to a –1 percent shock exhibit little time variation. Second, evidence of time variation is, in general, quite substantial for both inflation and real GDP growth, providing both a strong justification for the use of time-varying estimation method and an important caveat to results obtained with fixed-coefficient models. This is especially apparent for the responses of U.S. inflation and real GDP growth, which since the end of the 1960s have exhibited three peaks around the time of the Great Inflation of the 1970s, of the recession of the early 1990s, and in the most recent past. These results clearly suggest that a fixed-coefficient model estimated over (say) the last two decades will understate the impact on inflation and output growth of a compres-sion in the yield spread during the financial crisis, as this sample period mixes two sub-samples which, in this respect, are quite dif-ferent. Evidence of gradual variation in the responses of inflation and
12Figures 1A and 2A in the online appendix show, for the United States and the United Kingdom, respectively, the median IRFs of inflation and output growth to a 1 percent negative shock to the yield spread, together with the 16th and 84th percentiles of the posterior distribution for selected quarters.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQH12b-YNIlFDzE3AZTTAKHio2nDUDu-xeYNFDrM5-U_kHaSZq1pXEhupG8FylukYFxv5cpJ2_f3CbwgDfhl3AwgArfb0lHkm0i4HKKwqVMU5EZeY2N7KmGENrBjieOEJeRtzaQufg=w1280-h965-v0?authuser=1)

Vol. 9 No. 2 Unconventional Monetary Policy 191
**Figure 6. Median IRFs to a 1 Percent Negative Shock to the Long-Term Bond Yield Spread for the United States,**
**1965:Q4 to 2011:Q4**
**Note:**The above was computed by setting the coefficients in the SVAR’s interest rate equation to zero for eight quarters.
output growth is even more apparent for the United Kingdom. The impact of a compression in the yield spread appears to have increased in recent years. Finally—and crucially, for the present purposes—the stimulative power of a reduction in the spread for both inflation and output growth appears to be substantial in the post-crisis period. For the United States in 2009:Q4, for example, real GDP growth increases (based on median estimates) by 1.2 percent in the quar-ter of impact, peaks at 2.2 percent three quarters after the impact, and then rapidly fades away over subsequent quarters. The impact on inflation starts at 0.4 percent on impact, peaks at 1.7 percent after three quarters, and then declines gradually. The results for the United Kingdom are quantitatively slightly different but overall of the same order of magnitude.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEisGhEODnX68AOjLLyeRsOpu_8X9805da5MMgEf_roKO_VUVLjwd8u1fMYIeHFtLrh_6gmfjinM5_Z2u9E9YcvW_44mUAADNo6oJwqW4kmK26rOGe6Bwfr2I_hPKZN0EkM6OjaYA=w1280-h985-v0?authuser=1)

192 International Journal of Central Banking June 2013
**Figure 7. Median IRFs to a 1 Percent Negative Shock to the Long-Term Bond Yield Spread for the United**
**Kingdom, 1975:Q2 to 2011:Q4**
**Note:**The above was computed by setting the coefficients in the SVAR’s interest rate equation to zero for eight quarters.
It is important to be mindful of the fact that constructing any counterfactual simulation is subject to the Lucas critique since it is based on the notion of taking an estimated SVAR and chang-ing (some of) the parameters in its structural monetary policy rule, which in the present context amounts to setting them to zero (see Sargent 1979). Even though Benati and Surico (2009) and Benati (2010) have shown based on estimated DSGE models that results produced by such counterfactuals may turn out to be misleading, the extent to which the Lucas critique matters is an empirical ques-tion and has to be judged on a case-by-case basis. Therefore, in the next section, we perform the exercise under consideration by induc-ing offsetting monetary policy shocks rather than shutting down the
Vol. 9 No. 2 Unconventional Monetary Policy 193
coefficients in the SVAR’s interest rate equation. We show that the results obtained with both approaches are qualitatively and quan-titatively similar, which is supportive of the fact that the Lucas critique is of lesser concern in this application.
*3.3.2 “Constant-Interest-Rate” Projection Methodology*
An alternative way of obtaining IRFs to a spread shock when the zero lower bound is binding for eight quarters after impact is to con-struct a hypothetical path of monetary policy shocks that exactly neutralizes all endogenous dynamics in the federal funds rate.13
Since the systematic component of monetary policy requires raising the short-term rate in response to higher inflation and real output growth triggered by the spread compression, the imposition of a suitable sequence of negative monetary policy surprises ensures that the short-term rate is kept constant over this period. This method is routinely used in central banks in order to compute “constant-interest-rate” (CIR) projections. From the ninth quarter onwards, we again allow the short rate to move according to what is implied by the SVAR’s monetary policy rule.
Figure 8 displays for the U.S. economy (panel A) and for the U.K. economy (panel B) the time-varying median IRFs of inflation and real GDP growth one year after the spread shock obtained with this methodology at each point in time. For comparison, we also report the median responses together with the 16th and 84th percentiles of the posterior distribution for the case where the coefficients in the policy rule are set to zero. The results for the United Kingdom are remarkably similar to those produced with the earlier approach throughout the sample. The responses of U.S. inflation and out-put growth are more pronounced for several quarters, in particular towards the end of the sample. Compared with the results obtained by “zeroing out” the coefficients of the SVAR’s interest rate rule, the IRFs derived with the CIR methodology exhibit greater volatility, which can be attributed to the workings of the following “feedback loop”: On impact, a compression of the spread stimulates output
13This approach has been widely used in the literature for counterfactual analyses (see, e.g., Hamilton and Herrera 2004; Kilian and Lewis 2011).
194 International Journal of Central Banking June 2013
**Figure 8. Time-Varying Median Impulse Responses of Inflation and Real GDP Growth One Year after a 1**
**Percent Negative Shock to the Long-Term Yield Spread**
A. United States, 1965:Q4 to 2011:Q4
1970 1980 1990 2000 2010 0
1
2
3
4
U.S. inflation
1970 1980 1990 2000 2010 -1
0
1
2
3
4
5 U.S. real GDP growth
68% credible set median with zero coefficients in policy rule median with CIR
B. United Kingdom, 1975:Q2 to 2011:Q4
1980 1990 2000 2010 0
1
2
3
4 U.K. inflation
1980 1990 2000 2010
0
1
2
3
4 U.K. real GDP growth
68% credible set median with zero coefficients in policy rule median with CIR
**Note:**The above was obtained by setting the coefficients in the SVAR’s inter-est rate equation to zero for eight quarters (solid line) and by applying the “constant-interest-rate” projection methodology (dotted line).
growth and inflation. As a consequence, starting from the first quar-ter after the impact, the SVAR’s monetary rule would call for an increase in the policy rate in order to temper such expansionary effects. The negative monetary policy shock that we inject to offset
Vol. 9 No. 2 Unconventional Monetary Policy 195
such a rise of the short rate exerts a*further*expansionary effect on inflation and real GDP growth, thereby compounding the ini-tial impact of the spread shock. Over the response horizon, this effect cumulates since a series of negative monetary policy shocks is needed to keep the short-term rate from rising, which results in stronger responses at later horizons.14 The strength of this feedback loop thus depends on (i) how large the impact of a spread shock is on inflation and on output growth, and (ii) how strongly monetary pol-icy responds to higher inflation and output growth. In the limiting case in which the policy rate does not react to inflation and output growth, the feedback loop would not even “kick in.” This implies that this phenomenon is not a general one, but rather may or may not be there, depending on the specific structure of the economy at each point in time.
Even though this way of implementing constant policy rates in a zero-lower-bound environment is not vulnerable to the Lucas cri-tique in the strict sense since we are only using monetary policy shocks and not changing the coefficients of the structural interest rate equation, there are other implications for agents’ expectations. First, since the structural monetary policy rule which is encoded in the estimated SVAR implies that the short-term rate always reacts to the state of the economy, this exercise ignores the direct effect on expectations formed by the public in response to the central bank’s announcement that it will keep the interest rate unchanged for an “extended period.”15 This expectational channel has the potential of amplifying the macroeconomic consequences of a compression in the yield spread. However, the extent to which agents will adjust their expectations in response to the change in policy crucially depends on the credibility of the announcement. Swanson and Williams (2012) show that during the first round of asset purchases, the Blue Chip consensus expectation of the length of time until the first increase in the federal funds rate fluctuated between three and five quarters,
14This feature is apparent in figure 3A in the online appendix, where the median responses for the United States are shown in three-dimensional graphs for all four variables based on the CIR methodology. Figure 4A shows the corresponding results for the U.K. economy.
15We say “for an extended period” since leaving the interest rate unchanged forever, and announcing that to the public, leads to global indeterminacy.
196 International Journal of Central Banking June 2013
indicating that the private sector was not convinced that the zero bound would constrain monetary policy for an extended period.16
Second, our thought experiment assumes that the public will not revise the model it uses to forecast the future path of the nominal interest rate despite the fact that the policy rate is repeatedly devi-ating in the same direction from the path that would be implied by the systematic component of monetary policy. Specifically, the downward adjustment of the policy rate needed to countervail its endogenous rise so that it stays at zero results in a sequence of inter-est rate “surprises”*all of the same—negative—sign.*If agents were to notice that policy shocks are no longer drawn from a zero-mean, symmetric distribution, but from a distribution with an upper bound at zero, they could use this information to improve their interest rate forecasts. Whether the public will or will not detect such a regularity eventually depends on how persistent these shock sequences are. In the present case, it is not evidently unreasonable to presume that the public will not readily uncover such a systematic pattern given that the unanticipated changes in the policy rate last for a comparatively short period of time.
*3.3.3 On the Sources of Time Variation*
As previously discussed, based on both methodologies we detect sig-nificant time variation in the economy’s response to a compression in the yield spread. Although identifying the*sources*of such time variation is clearly beyond the scope of this paper, one possible cause deserves to be at least briefly mentioned.17 Historically, changes in the yield spread for a given short rate have had a multiplicity of causes: shifts in long-term inflation expectations, changes in the liquidity premium, etc. Since it is at least possible to entertain the hypothesis that different underlying causes of changes in the yield spread may lead to a different pattern of responses of the economy— that is, to different impulse response functions to a compression of the yield spread of a given magnitude—one obvious possibility for the identified changes over time in the pattern of IRFs is that such
16Announcements are more likely to be credible since the Federal Reserve started using a more explicit form of forward guidance in August 2011, tying its intentions for the future path of the federal funds rate to a specific timeline.
17We wish to thank a referee for pointing this out.
Vol. 9 No. 2 Unconventional Monetary Policy 197
changes may simply result from a change in the “mixture” of the underlying shocks leading to changes in the yield spread. We consider this an interesting avenue for future research.
*3.3.4 Normal Times versus Zero-Lower-Bound Episode*
In sections 3.3.1 and 3.3.2, we postulated that the zero lower bound was binding throughout the sample period. We now examine the macroeconomic effects of a spread compression when the policy rate is free to adjust to macroeconomic conditions as would be relevant for the pre-crisis period.
Figure 9 compares, for the United States (panel A) and the United Kingdom (panel B), the time profile of the constrained and unconstrained responses of prices and real GDP one year after the unanticipated reduction in the yield spread by 1 percent.18 We observe that, in several historical episodes, both U.S. output and prices react more strongly to a spread compression when the policy rate is held fixed. The reason for the smaller effects in the uncon-strained case is that in those periods the central bank responds to the decline in the long-short spread by raising interest rates consid-erably (not reported), which contains inflation and output growth. Starting in 2000, the gap between the responses with and without the zero bound in place widens for both macroeconomic variables and becomes largest during the period of large-scale asset purchases, which lends support to the idea that the constraint on the policy rate magnifies the effects of a spread shock on the macroeconomy.
What is striking is that in the United Kingdom over the pre-crisis sample, the transmission of spread shocks to the macroeconomy does not seem to be affected much by imposing the zero-lower-bound constraint. Whether the policy rate is allowed to react to a spread shock after impact or whether it is constrained to remain at zero for eight consecutive quarters has virtually no effect on output and makes only a little difference for the price response before the start of quantitative easing. In contrast, the macroeconomic consequences are greatly amplified from early 2009 onwards, when the zero bound was effectively binding.
18The results are not markedly different for shorter or longer horizons.
198 International Journal of Central Banking June 2013
**Figure 9. Time-Varying Median Responses of Prices and Real GDP One Year after a 1 Percent Negative Shock to**
**the Long-Term Yield Spread with and without the Zero-Lower-Bound Constraint Imposed on the Policy Rate**
A. United States, 1965:Q4 to 2011:Q4
1970 1980 1990 2000 2010 2
4
6
8
10
12 U.S. prices
1970 1980 1990 2000 2010 0
5
10
15
20 U.S. real GDP
without ZLB constraint with ZLB constraint
B. United Kingdom, 1975:Q2 to 2011:Q4
1980 1990 2000 2010
2
4
6
8 U.K. prices
1980 1990 2000 2010 0
2
4
6
8
10 U.K. real GDP
without ZLB constraint with ZLB constraint
**Note:**The vertical line indicates the start of large-scale asset purchases.
Vol. 9 No. 2 Unconventional Monetary Policy 199
**4. Conclusions**
In this paper, we explored the macroeconomic effects of a com-pression in the long-term bond yield spread within the context of the Great Recession of 2007–09 via a multivariate structural VAR with time-varying parameters and stochastic volatility to account for changes in the economic structure in the aftermath of the finan-cial crisis. We identified a “pure” spread shock as a disturbance that leaves the policy rate unchanged on impact, which allowed us to characterize the macroeconomic consequences of a compression in the yield spread induced by central banks’ asset purchases within an environment in which the short-term rate cannot move because it is constrained by the zero lower bound.
Two main findings emerged from our empirical analysis. First, a compression in the long-term yield spread exerts a powerful effect on both output growth and inflation in the United States and in the United Kingdom when the zero lower bound is binding. Sec-ond, conditional on consensus estimates of the impact of the Federal Reserve’s and the Bank of England’s asset purchase programs on long-term government-bond yield spreads, our counterfactual sim-ulations have indicated that both in the United States and in the United Kingdom, unconventional monetary policy actions have been successful at mitigating significant risks both of deflation and of fur-ther output collapses comparable to those that took place during the Great Depression. Our model simulations suggest that in the absence of policy interventions, the U.S. economy would have been in deflation until 2009:Q3 with annualized inflation rates as low as –1 percent. Real GDP would have been 0.9 percent lower, and unem-ployment would have been 0.75 percentage points higher, reaching a level of about 10.6 percent in 2009:Q4. Similarly, in the United Kingdom, without quantitative easing, annualized inflation would have fallen to –4 percent and output growth would have reached a trough of –12 percent at an annual rate in the first quarter of 2009 based on the median of our counterfactual estimates. Based on these results, we conclude that large-scale purchases of Treasury securities constitute a viable policy option to provide additional monetary pol-icy accommodation in a zero-lower-bound environment that enables central banks to achieve their mandate of promoting price stability and, in the case of the Federal Reserve, fostering full employment
200 International Journal of Central Banking June 2013
and should therefore be added to the toolkit of monetary authorities.
It cannot be excluded, however, that there were additional forces at play that are not captured in our empirical model, which have the potential to reinforce the macroeconomic stimulus induced by the large open-market purchases of domestic government debt. First, unconventional fiscal policy operations in the wake of the crisis complement monetary policy efforts when the economy is stuck at the zero lower bound (see, e.g., Auerbach and Obstfeld 2005). Sec-ond, the announcement and implementation of non-standard policy measures should also have stabilizing effects on agents’ expectations and contribute to a rebound of confidence that enhance the effec-tiveness of policy interventions. Carvalho et al. (2011), based on cross-country experiences during the crisis, present evidence that both unconventional monetary and fiscal actions positively affected the evolution of inflation and growth expectations. Exploring these and other additional channels of non-standard policy interventions is an important task for future research to provide a comprehensive assessment of the beneficial macroeconomic effects of such policies.
**Appendix 1. Data Appendix**
*United States*
A monthly seasonally unadjusted series for the federal funds rate (FEDFUNDS) available for the period July 1954–December 2011, and a monthly series for the ten-year Treasury constant-maturity rate (GS10) available for April 1953–December 2011, are from the Federal Reserve Bank of St. Louis’s FRED database. We converted them to quarterly frequency by taking averages within the quarter. Quarterly seasonally adjusted series for real GDP (GDPC96) and the GDP deflator (GDPDEF), available for the period 1947:Q1– 2011:Q4, are from the same database.
*United Kingdom*
Quarterly seasonally adjusted series for real GDP and the GDP deflator are from the Office for National Statistics and are avail-able since the first quarter of 1955. The Treasury-bill rate and the
Vol. 9 No. 2 Unconventional Monetary Policy 201
long-term government-bond yield for the period 1964:Q1 to 2011:Q4 are from the International Monetary Fund’s International Financial Statistics database.
**Appendix 2. Details of the Markov Chain Monte Carlo Procedure**
We estimate the model described by equations (1)–(10) via Bayesian methods. The next two sub-sections describe our choices for the priors and the Markov chain Monte Carlo (MCMC) algorithm we use to simulate the posterior distribution of the hyperparameters and the states conditional on the data. Section 3 provides evidence for the convergence of the Markov chain to the ergodic distribu-tion, and section 4 provides an informal assessment of our modeling assumptions.
*Prior Distributions and Initial Values*
For the sake of simplicity, the prior distributions of thestates—θ0,α0,h0,andq0—whichwe postulate all to be normal, are assumed to be independent both from one another and from the distribution of the hyperparameters. In order to calibrate the prior distributions forθ0,α0,h0,andq0and to obtain initial values, we estimate a time-invariant version of (1) based on the first ten years of data and we set
θ0*∼*N[θ^OLS,4*·*V^(θ^OLS)].(15)
As forα0andh0,we proceed as follows. LetΣ^OLSbe the estimated covariance matrix ofεtfrom the time-invariant VAR, and letCbe the lower-triangular Choleski factor ofΣ^OLS—i.e.,CC*′*=Σ^OLS.We set
lnh0*∼*N(lnμ0,10*×*I4),(16)
whereμ0is a vector collecting the squared elements on the diagonal ofC.We then divide each column ofCby the corresponding element on the diagonal—let’s call the matrix we thus obtainC~—andwe set
α0*∼*N[α~0,V~(α~0)],(17)
202 International Journal of Central Banking June 2013
whereα~0—which,for future reference, we define asα~0≡[α~0,11,α~0,21,...,α~0,61]′—isa vector collecting all the non-zero and non-unity elements ofC~−1(i.e., the elements below the diagonal), and its covariance matrix,V~(α~0),is postulated to be diagonal, with each individual*(j,j*) element equal to ten times the absolute value of the corresponding*j*-th element ofα~0.Such a choice for the covari-ance matrix ofα0is clearly arbitrary but is motivated by our goal to scale the variance of each individual element ofα0in such a way as to take into account the element’s magnitude.
As forq0,we proceed as follows. LetQ0be the prior matrix for the extent of random-walk drift of the VAR’s parametersθtthat we would use if we were working with a traditional Bayesian time-varying parameters VAR with a*constant*extent of random-walk drift over the sample. We setQ0=γ*×*Σ^OLS,withγ=1.0*× 10−4,*the same value used in Primiceri (2005), and a relatively “conserva-tive” prior for the extent of drift compared (e.g.) with the*3.5×10−4*
used by Cogley and Sargent (2002). We set
lnq0*∼*N(10−2*×*lnqˉ​0,10*×*IN⋅(1+Np)),(18)
whereqˉ​0is a vector collecting the elements on the diagonal ofQ0.Turning to the hyperparameters, we postulate independence
between the parameters corresponding to the matricesSandZ—anassumption we adopt uniquely for reasons of convenience—and we make the following, standard assumptions. The three blocks ofSare assumed to follow inverted Wishart distributions, with prior degrees of freedom set, again, equal to the minimum allowed, respectively, 2, 3, and 4:
S1*∼*IW(Sˉ−1
1,2 )
(19)
S2*∼*IW(Sˉ−1
2,3 )
(20)
S3*∼*IW(Sˉ−1
3,4 ).(21)
As forSˉ1,Sˉ2,andSˉ3,we calibrate them based onα~0in (17) as
Sˉ1=*10−3 ×*∣α~0,11∣,Sˉ2=*10−3 ×*diag([∣α~0,21∣,∣α~0,31∣]′)and
Sˉ3=*10−3 ×*diag([∣α~0,41∣,∣α~0,51∣,∣α~0,61∣]′).
Vol. 9 No. 2 Unconventional Monetary Policy 203
Such a calibration is consistent with the one we adopted forQ,as it is equivalent to settingSˉ1,Sˉ2,andSˉ3equal to*10−4*times the relevant diagonal block ofV~(α~0)in (17). As for the variances of the innovations to the stochastic volatilities for the VAR’s reduced-form shocks, we follow Cogley and Sargent (2002, 2005) and we postulate an inverse-Gamma distribution for the elements ofZν,
σ2ν,i*∼*IG
(*10−4*
2,1 2
).(22)
Finally, as for the variances of the innovations to the stochastic volatilities for the VAR’s random-walk parameters’ innovations, we postulate an inverse-Gamma distribution for the elements ofZω,
σ2ω,i*∼*IG
(*10−4*
2,10 2
).(23)
(23) implies that the prior forσ2ω,ihas the same mean as in Cogley,
Primiceri, and Sargent (2010), but it has a smaller variance.
*Simulating the Posterior Distribution*
We simulate the posterior distribution of the hyperparameters and the states conditional on the data via the following MCMC algo-rithm, combining elements of Cogley and Sargent (2002, 2005) and Primiceri (2005). In what follows,xtdenotes the entire history of the vectorxup to timet—i.e.,xt≡[x′
1,x′2, . . . ,x′
t]*′—while*Tis the
sample length.
(i) Drawing the elements ofθt:Conditional onYT,αT, andHT, the observation equation (1) is linear, with Gaussian inno-vations and a known covariance matrix. Following Carter and Kohn (1994), the densityp(θT∣YT,αT,HT,V) can be factored as
p(θT∣YT,αT,HT,V)
=p(θT∣YT,αT,HT,V)T−1∏t=1
p(θt∣θt+1,YT,αT,HT,V).(24)
204 International Journal of Central Banking June 2013
Conditional onαT,HT, andV, the standard Kalman filter recursions nail down the first element on the right-hand side of (24),p(θT∣YT,αT,HT,V) =N(θT,PT), withPTbeing the precision matrix ofθTproduced by the Kalman filter. The remaining elements in the factorization can then be computed via the backward recursion algorithm found, e.g., in Kim and Nelson (1999) or Cogley and Sargent (2005, appendix B.2.1). Given the conditional normality ofθt,we have
θt∣t+1=θt∣t+Pt∣tP*−1*t+1∣t(θt+1*−*θt)(25)
Pt∣t+1=Pt∣t*−*Pt∣tP*−1*t+1∣tPt∣t,(26)
which provides, for eachtfromT–1to 1, the remaining ele-ments in (1),p(θt∣θt+1,YT,αT,HT,V) =N(θt∣t+1,Pt∣t+1).Specifically, the backward recursion starts with a draw fromN(θT,PT); call itθ~T. Conditional onθ~T, (25)–(26) give usθT−1∣TandPT−1∣T, thus allowing us to drawθ~T−1fromN(θT−1∣T,PT−1∣T); and so on untilt= 1.
(ii) Drawing the elements ofαt:Conditional onYT,θT, andHT, following Primiceri (2005), we draw the elements ofαt
as follows. Equation (1) can be rewritten asAtY~t≡At(Yt−X
*′*
tθt)=Atεt≡ut,withVar(ut)=Ht,namely
Y~2,t=−α21,tY~1,t+u2,t(27)
Y~3,t=−α31,tY~1,t*−*α32,tY~2,t+u3,t(28)
Y~4,t=−α41,tY~1,t*−*α42,tY~2,t*−*α43,tY~3,t+u4,t,(29)
plus the identityY~1,t=u1,t,where[Y~1,t,Y~2,t,Y~3,t,Y~4,t]′≡Y~t.Based on the observation equations (27)–(29) and the tran-sition equation (8), the elements ofαtcan then be drawn by applying the same algorithm we described in the previ-ous paragraph separately to (27)–(29). The assumption thatShas the block-diagonal structure (10) is in this respect cru-cial, although, as stressed by Primiceri (2005, appendix D), it could in principle be relaxed.
(iii) Drawing the elements ofHt:Conditional onYT,θT, andαT, the orthogonalized innovationsut≡At(Yt−X
*′*
tθt),withVar(ut)=Ht,are observable. Following Cogley and Sargent
Vol. 9 No. 2 Unconventional Monetary Policy 205
(2002), we then sample thehi,t’sby applying the univariate algorithm of Jacquier, Polson, and Rossi (1994) element by element.19
(iv) Drawing the elements ofQt:Conditional onθT, the innova-tionsηt=θt*−*θt−1,withVar(ηt)=Qt,are observable, and, along the lines of point (iii), we therefore sample theqj,t’sby applying the univariate algorithm of Jacquier, Polson, and Rossi (1994) element by element.
(v) Drawing the hyperparameters: Finally, conditional onYT,θT,HT, andαT, the innovations toθt,αt,thehi,t’sand theqi,t’sare observable, which allows us to draw the hyperparameters—the elements ofS1,S2,S3,and theσ2
ν,i
and theσ2ω,i—fromtheir respective distributions.
Summing up, the MCMC algorithm simulates the posterior dis-tribution of the states and the hyperparameters, conditional on the data, by iterating on (i)–(v). In what follows, we use a burn-in period of 50,000 iterations to converge to the ergodic distribution, and after that we run 10,000 more iterations, sampling every tenth draw in order to reduce the autocorrelation across draws.
*Assessing the Convergence of the Markov Chain to the Ergodic Distribution*
Following Primiceri (2005), we assess the convergence of the Markov chain by inspecting the autocorrelation properties of the draws from the ergodic distribution. Specifically, in what follows, we consider the draws’ inefficiency factors (IFs), defined as the inverse of the relative numerical efficiency measure of Geweke (1992),
RNE=(2π)−11S(0)
∫π
−π
S(ω)dω,(30)
whereS(ω)is the spectral density of the sequence of draws from the Gibbs sampler for the quantity of interest at the frequencyω.We estimate the spectral densities by smoothing the periodograms in the frequency domain by means of a Bartlett spectral window.
19For details, see Cogley and Sargent (2005, appendix B.2.5).
206 International Journal of Central Banking June 2013
Following Berkowitz and Diebold (1998), we select the bandwidth parameter automatically via the procedure introduced by Beltrão and Bloomfield (1987).
Figures 5A and 6A in the online appendix show, for the United States and the United Kingdom, the draws’ IFs for the models’ hyperparameters, i.e., the free elements of the matricesZν,Zω,S1,S2,andS3,and for the states, i.e., the time-varying coefficients of the VAR (theθt’s),the volatilities of the innovations to the VAR’s random-walk parameters (theqi,t’s),the volatilities of the VAR’s reduced-form innovations (thehi,t’s),and the non-zero and non-one elements of the matrixAt.As can be seen from the figures, for both countries the autocorrelation of the draws is uniformly very low, being in the vast majority of cases around or below 3, which suggests that the Markov chains have indeed converged.20
*An Informal Assessment*
An informal check to assess how well our time-varying parameter VARs track the data is to look at the inflation trends produced by the model. For the United States, in particular, there is a vast consensus—stemming, first and foremost, from the work of Cogley and Sargent—that trend inflation peaked, during the 1970s, between 7 and 8 percent, and significantly declined since then. The estimated time-varying VAR for the United States should generate comparable results if our model specification performs well.
Figure 7A in the online appendix plots, for the United States (panel A) and the United Kingdom (panel B), actual GDP defla-tor inflation together with the time-varying trends generated by the model. Several things are apparent from the figures. First, concern-ing the United States, the median inflation trend peaks at about 7 percent during the second half of the 1970s, exactly in line with the previous evidence. Second, the estimated inflation trends mani-festly appear to capture the slow-moving, low-frequency component of inflation.
20As stressed by Primiceri (2005, appendix B), values of the IFs below or around 20 are generally regarded as satisfactory.
Vol. 9 No. 2 Unconventional Monetary Policy 207
**Appendix 3. Computing Time-Varying Impulse Response Functions**
Here we describe the Monte Carlo integration procedure we use in section 3.3 to compute non-linear IRFs to a pure spread shock along the lines of Koop, Pesaran, and Potter (1996) and Kilian and Vigfusson (2011).
Randomly draw the current state of the economy at timetfrom the output of the Gibbs sampler. Given the current state of the economy, repeat the following procedure 100 times. Draw four inde-pendentN(0,1) variates—the four structural shocks—and based on the relationshipεt=A0,tet,withet≡[eMP
t,eSPt,eD
t,eSt*]′,*where
eMPt,eSP
t,eDt, andeS
tare the monetary policy, pure spread, demand non-policy, and supply structural shocks, respectively, compute the reduced-form shocksεtat timet.Simulate both the VAR’s time-varying parameters and the covariance matrix of its reduced-form innovations,Ωt,twenty quarters into the future. Based on the sim-ulatedΩt,randomly draw reduced-form shocks fromt+ 1 tot+ 20. Based on the simulatedθt,and on the sequence of reduced-form shocks fromttot+20,compute simulated paths for the four endoge-nous variables. Call these simulated pathsX^j
t,t+20,j=1,...,100. Repeat the same procedure 100 times based on exactly the same simulated paths for the VAR’s time-varying parameters, theθt;the same reduced-form shocks at timest+ 1 tot+ 20; and the same structural shockseMP
t,eDt, andeS
tat timet,but settingeSPtto
1. Call these simulated pathsX~jt,t+20.For each of the 100 itera-
tions defineirfjt,t+20≡X^j
t,t+20*−*X~jt,t+20.Finally, compute each
of the 1,000 generalized IRFs as the mean of the distribution ofirfj
t,t+20.
**References**
Auerbach, A. J., and M. Obstfeld. 2005. “The Case for Open-Market Purchases in a Liquidity Trap.”*American Economic Review*95 (1): 110–37.
Balke, N., and R. J. Gordon. 1986. “Appendix B: Historical Data.” In*The American Business Cycle: Continuity and Changes,*ed. R. J. Gordon. Chicago: University of Chicago Press.
208 International Journal of Central Banking June 2013
Baumeister, C., and L. Benati. 2010. “Unconventional Monetary Policy and the Great Recession—Estimating the Impact of a Compression in the Yield Spread at the Zero Lower Bound.” ECB Working Paper No. 1258.
Baumeister, C., P. Liu, and H. Mumtaz. 2013. “Changes in the Effects of Monetary Policy on Disaggregate Price Dynam-ics.”*Journal of Economic Dynamics & Control*37 (3): 543– 60.
Baumeister, C., and G. Peersman. 2012. “The Role of Time-Varying Price Elasticities in Accounting for Volatility Changes in the Crude Oil Market.” Forthcoming in*Journal of Applied Econo-metrics.*
———. 2013. “Time-Varying Effects of Oil Supply Shocks on the U.S. Economy.” Forthcoming in*American Economic Journal: Macroeconomics.*
Bean, C. 2009. Untitled speech given at the Bank of England, at Cutlers’ Feast, Cutlers’ Hall, Sheffield, May 21.
Beltrão, K. I., and P. Bloomfield. 1987. “Determining the Band-width of a Kernel Spectrum Estimate.”*Journal of Time Series Analysis*8 (1): 21–38.
Benati, L. 2008. “The Great Moderation in the United Kingdom.”*Journal of Money, Credit and Banking*39 (1): 121–47.
———. 2010. “Are Policy Counterfactuals Based on Structural VARs Reliable?” ECB Working Paper No. 1188.
Benati, L., and C. Goodhart. 2010. “Monetary Policy Regimes and Economic Performance: The Historical Record, 1979–2008.” In*Handbook of Monetary Economics,*Vol. 1D, ed. B. Friedman and M. Woodford. North Holland.
Benati, L., and H. Mumtaz. 2007. “U.S. Evolving Macroeconomic Dynamics: A Structural Investigation.” ECB Working Paper No. 746.
Benati, L., and P. Surico. 2009. “VAR Analysis and the Great Mod-eration.”*American Economic Review*99 (4): 1636–52.
Berkowitz, J., and F. X. Diebold. 1998. “Bootstrapping Multivari-ate Spectra.”*Review of Economics and Statistics*80 (4): 664– 66.
Bernanke, B. S. 2006. “Reflections on the Yield Curve and Monetary Policy.” Speech presented at the Economic Club of New York, March 20.
Vol. 9 No. 2 Unconventional Monetary Policy 209
———. 2010. “The Economic Outlook and Monetary Policy.” Remarks at the Federal Reserve Bank of Kansas City Economic Symposium, Jackson Hole, Wyoming, August 27.
Bomfim, A. N., and L. H. Meyer. 2010. “Quantifying the Effects of Fed Asset Purchases on Treasury Yields.”*Monetary Policy Insights: Fixed Income Focus*(June 17).
Canova, F., and G. De Nicolò. 2002. “Monetary Disturbances Mat-ter for Business Fluctuations in the G-7.”*Journal of Monetary Economics*49 (6): 1131–59.
Canova, F., and L. Gambetti. 2009. “Structural Changes in the US Economy: Is There a Role for Monetary Policy?”*Journal of Economic Dynamics & Control*33 (2): 477–90.
Canova, F., and M. Paustian. 2011. “Business Cycle Measurement with Some Theory.”*Journal of Monetary Economics*58 (4): 345–61.
Canova, F., and J. Pina. 2005. “What VAR Tell Us About DSGE Models.” In*New Trends in Macroeconomics,*ed. C. Diebolt and C. Kyrtsou. Springer Verlag.
Carter, C. K., and R. Kohn. 1994. “On Gibbs Sampling for State Space Models.”*Biometrika*81 (3): 541–53.
Carvalho, C., V. Cúrdia, S. Eusepi, and C. Grisse. 2011. “An Assess-ment of the Effects of Unconventional Policies using Cross-Country Experiences.” Mimeo, Federal Reserve Bank of New York.
Chen, H., V. Cúrdia, and A. Ferrero. 2012. “The Macroeconomic Effects of Large-Scale Asset Purchase Programmes.”*Economic Journal*122 (564): F289–F315.
Chung, H., J.-P. Laforte, D. Reifschneider, and J. C. Williams. 2012. “Have We Underestimated the Likelihood and Severity of Zero Lower Bound Events?”*Journal of Money, Credit and Banking*44 (1, Suppl.): 47–82.
Cogley, T., G. E. Primiceri, and T. J. Sargent. 2010. “Inflation-Gap Persistence in the US.”*American Economic Journal: Macroeco-nomics*2 (1): 43–69.
Cogley, T., and T. J. Sargent. 2002. “Evolving Post-World War II U.S. Inflation Dynamics.” In*NBER Macroeconomics Annual 2001,*eds. B. S. Bernanke and K. Rogoff, 331–73. Cambridge, MA: MIT Press.
210 International Journal of Central Banking June 2013
———. 2005. “Drifts and Volatilities: Monetary Policies and Out-comes in the Post WWII US.”*Review of Economic Dynamics*8 (2): 262–302.
D’Amico, S., and T. B. King. 2012. “Flow and Stock Effects of Large-Scale Treasury Purchases: Evidence on the Importance of Local Supply.” Forthcoming in*Journal of Financial Economics.*
Del Negro, M., G. Eggertsson, A. Ferrero, and N. Kiyotaki. 2011. “The Great Escape? A Quantitative Evaluation of the Fed’s Liquidity Facilities.” Federal Reserve Bank of New York Staff Report No. 520 (October).
Doh, T. 2010. “The Efficacy of Large-Scale Asset Purchases at the Zero Lower Bound.”*Economic Review*(Federal Reserve Bank of Kansas City) (2nd Quarter): 5–34.
Eickmeier, S., and B. Hofmann. 2012. “Monetary Policy, Housing Booms, and Financial (Im)Balances.” Forthcoming in*Macroeco-nomic Dynamics.*
Faust, J. 1998. “The Robustness of Identified VAR Conclusions about Money.”*Carnegie-Rochester Conference Series on Public Policy*49 (1): 207–44.
Gagnon, J., M. Raskin, J. Remache, and B. P. Sack. 2011. “The Financial Market Effects of the Federal Reserve’s Large-Scale Asset Purchases.”*International Journal of Central Banking*7 (1): 3–43.
Geweke, J. 1992. “Evaluating the Accuracy of Sampling-Based Approaches to the Calculation of Posterior Moments.” In*Bayesian Statistics,*eds. J. M. Bernardo, J. O. Berger, A. P. Dawid, and A. F. M. Smith, 169–93. Oxford: Oxford University Press.
Gilchrist, S., V. Yankov, and E. Zakraǰsek. 2009. “Credit Market Shocks and Economic Fluctuations: Evidence from Corporate Bond and Stock Markets.”*Journal of Monetary Economics*56 (4): 471–93.
Hamilton, J. D., and A. M. Herrera. 2004. “Comment: Oil Shocks and Aggregate Macroeconomic Behavior: The Role of Monetary Policy.”*Journal of Money, Credit and Banking*36 (2): 265–86.
Hamilton, J. D., and J. C. Wu. 2012. “The Effectiveness of Alter-native Monetary Policy Tools in a Zero Lower Bound Environ-ment.”*Journal of Money, Credit and Banking*44 (1, Suppl.): 3–46.
Vol. 9 No. 2 Unconventional Monetary Policy 211
Jacquier, E., N. G. Polson, and P. E. Rossi. 1994. “Bayesian Analy-sis of Stochastic Volatility Models.”*Journal of Business and Economic Statistics*12 (4): 371–418.
Joyce, M., A. Lasaosa, I. Stevens, and M. Tong. 2011. “The Financial Market Impact of Quantitative Easing.”*International Journal of Central Banking*7 (3): 113–61.
Kilian, L., and L. T. Lewis. 2011. “Does the Fed Respond to Oil Price Shocks?”*Economic Journal*121 (555): 1047–72.
Kilian, L., and S. Manganelli. 2007. “Quantifying the Risk of Deflation.”*Journal of Money, Credit and Banking*39 (2–3): 561–90.
Kilian, L., and D. P. Murphy. 2012. “Why Agnostic Sign Restrictions Are Not Enough: Understanding the Dynamics of Oil Market VAR Models.”*Journal of the European Economic Association*10 (5): 1166–88.
Kilian, L., and R. J. Vigfusson. 2011. “Are the Responses of the U.S. Economy Asymmetric in Energy Price Increases and Decreases?”*Quantitative Economics*2 (3): 419–53.
Kim, C.-J., and C. R. Nelson. 1999.*State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Appli-cations.*Cambridge, MA: MIT Press.
Koop, G., R. Leon-Gonzalez, and R. W. Strachan. 2009. “On the Evolution of the Monetary Policy Transmission Mechanism.”*Journal of Economic Dynamics & Control*33 (4): 997–1017.
Koop, G., M. H. Pesaran, and S. M. Potter. 1996. “Impulse Response Analysis in Nonlinear Multivariate Models.”*Journal of Econo-metrics*74 (1): 119–47.
Krishnamurthy, A., and A. Vissing-Jorgensen. 2011. “The Effects of Quantitative Easing on Interest Rates: Channels and Policy Implications.”*Brookings Papers on Economic Activity*2 (Fall): 215–65.
Lenza, M., H. Pill, and L. Reichlin. 2010. “Monetary Policy in Excep-tional Times.”*Economic Policy*25 (62): 295–339.
McConnell, M., and G. Pérez-Quirós. 2000. “Output Fluctuations in the United States: What Has Changed Since the Early 1980’s?”*American Economic Review*90 (5): 1464–76.
Meier, A. 2009. “Panacea, Curse, or Nonevent? Unconventional Monetary Policy in the United Kingdom.” IMF Working Paper No. 09/163.
212 International Journal of Central Banking June 2013
Neely, C. 2010. “The Large-Scale Asset Purchases Had Large Inter-national Effects.” Federal Reserve Bank of St. Louis Working Paper No. 18.
Primiceri, G. E. 2005. “Time Varying Structural Vector Autoregres-sions and Monetary Policy.”*Review of Economic Studies*72 (3): 821–52.
Rubio-Ramı́rez, J., D. F. Waggoner, and T. Zha. 2010. “Structural Vector Autoregressions: Theory of Identification and Algorithms for Inference.”*Review of Economic Studies*77 (2): 665–96.
Rudebusch, G. D., B. P. Sack, and E. T. Swanson. 2007. “Macroeco-nomic Implications of Changes in the Term Premium.”*Review*(Federal Reserve Bank of St. Louis) 89 (4, July/August): 241–69.
Sargent, T. J. 1979. “Estimating Vector Autoregressions Using Methods Not Based on Explicit Economic Theories.”*Quarterly Review*(Federal Reserve Bank of Minneapolis) 3 (Summer): 8– 15.
Schmitt-Grohé, S., and M. Uŕıbe. 2010. “Liquidity Traps: An Interest-Rate-Based Exit Strategy.” NBER Working Paper No. 16514.
Sims, C. A., and T. Zha. 2006. “Were there Regime Switches in U.S. Monetary Policy?”*American Economic Review*96 (1): 54–81.
Stock, J. H., and M. W. Watson. 1996. “Evidence of Structural Instability in Macroeconomic Time Series Relations.”*Journal of Business and Economic Statistics*14 (1): 11–30.
Swanson, E. T., and J. C. Williams. 2012. “Measuring the Effect of the Zero Lower Bound on Medium- and Longer-Term Interest Rates.” Federal Reserve Bank of San Francisco Working Paper No. 2012-02.
Uhlig, H. 2005. “What Are the Effects of Monetary Policy on Out-put? Results from an Agnostic Identification Procedure.”*Journal of Monetary Economics*52 (2): 381–419.