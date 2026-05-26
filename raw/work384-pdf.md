
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQGw6S-vNSRR_t52MGP_Exj60MjBYzzOB-6tiLbJy6p9A3YUfxX5F6om1XurxOYu5RCZJyDwmGVxPZCwHVpve0xlc6RA3mdOzlidtQWihHaTKGVmu3akAqfw3A15KBGwQYU0FHtP=w1280-h163-v0?authuser=1)

![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQHmTkW_XfwMoD-ZQJpRuWBepsPcJrW8khoaw96el3wsVSa83H-j4nMpMvVBmlVDZCQjd6sx3kENQGF7CapOM2siKqv_2PWHB_So3YhERXAWeg5MY3Eah8vA6cTZa3DkfrayYi_Mrw=w1280-h639-v0?authuser=1)

![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQGHTJlobyE_dqYB5-hwGNh9nVs_zQfQKzi8IoLEIRdtNSXwgP-asmm8bJ2Op-Kuz-RpXz07LEmlw1BXoZlsxKlil_ziMzXWOjUS7EyAq6q6j34c4mSTV4WjsgPGMQ3nllGqjfJcuQ=w1280-h639-v0?authuser=1)
BIS Working Papers
### No 384
### The Effectiveness of Unconventional Monetary Policy at the Zero Lower Bound: A Cross-Country Analysis
by Leonardo Gambacorta, Boris Hofmann and Gert Peersman
Monetary and Economic Department
August 2012
JEL classification: C32, E30, E44, E51, E52  Keywords: unconventional monetary policy, zero lower bound, panel VARs
BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in them are those of their authors and not necessarily the views of the BIS.
This publication is available on the BIS website (www.bis.org).
*© Bank for International Settlements 2012. All rights reserved. Brief excerpts may be reproduced or translated provided the source is stated.*
ISSN 1020-0959 (print)
ISSN 1682-7678 (online)
### The E¤ectiveness of Unconventional Monetary Policy at the
### Zero Lower Bound: A Cross-Country Analysis
Leonardo Gambacorta
Bank for International Settlements
leonardo.gambacorta@bis.org
Boris Hofmann
Bank for International Settlements
boris.hofmann@bis.org
Gert Peersman
Ghent University
gert.peersman@ugent.be
August 2012
Abstract
This paper assesses the macroeconomic e¤ects of unconventional monetary policies
by estimating a panel VAR with monthly data from eight advanced economies over
a sample spanning the period since the onset of the global nancial crisis. It nds
that an exogenous increase in central bank balance sheets at the zero lower bound
leads to a temporary rise in economic activity and consumer prices. The estimated
output e¤ects turn out to be qualitatively similar to the ones found in the literature
on the e¤ects of conventional monetary policy, while the impact on the price level is
weaker and less persistent. Individual country results suggest that there are no major
di¤erences in the macroeconomic e¤ects of unconventional monetary policies across
countries, despite the heterogeneity of the measures that were taken.
JEL classication: C32, E30, E44, E51, E52
Keywords: unconventional monetary policy, zero lower bound, panel VARs
We would like to thank Claudio Borio, Selien De Schryder, Dan Thornton, Fabrizio Zampolli and participants at the Bank of England conference "Learning the lessons from QE and other unconventional monetary policies", the EC2 conference "Econometrics for policy analysis - after the crisis and beyond" and BIS seminar for helpful comments. Bilyana Bogdanova provided excellent research assistance. The opinions expressed in this paper are those of the authors and do not necessarily reect the views of the BIS.
1
1 Introduction
In the wake of the global nancial crisis, many central banks in advanced economies
embarked on unconventional monetary policy measures in order to counter the risks to
economic and nancial stability. As policy rates approached and ultimately got stuck at
their e¤ective lower bounds, central bank balance sheets basically replaced interest rates
as the main policy instrument.1 As a consequence, the models that were estimated over
the pre-crisis period with a short-term interest rate as the monetary policy instrument
are not suitable for studying the e¤ectiveness of monetary policy in the aftermath of the
crisis. The challenge is to gure out a suitable econometric approach for analyzing the
macroeconomic impact of central banks balance sheet policies in a crisis period when
interest rates reach the zero lower bound.2
The evidence available so far has mainly focused on the nancial market impact of
unconventional monetary policy measures using high-frequency nancial data.3 A few
papers go one step further and try to assess the macroeconomic e¤ects of such policies
(e.g. Chung et al. 2011, Lenza et al. 2011, Peersman 2011, Joyce, Tong and Woods
2011). A potential caveat concerning these studies is that they rely on models estimated
over sample periods covering also the pre-crisis period, which may not be adequate for
assessing macroeconomic dynamics and monetary transmission in a liquidity trap. In
addition, central bank balance sheet policies before the crisis were usually not aimed at
inuencing macroeconomic conditions. On the other hand, there are a number of papers
exploring the e¤ectiveness of the Bank of Japans quantitative easing at the zero lower
bound between 2001 and 2006 (e.g. Ugai 2007, Schenkelberg and Watzka 2011), but
1For an overview and taxonomy of the various unconventional monetary policy measures taken by central banks during the crisis, see e.g. Borio and Disyatat (2010) and Stone et al. (2011).
2Throughout the paper, we will refer to central bank balance sheet policy and unconventional monetary policy interchangeably.
3Specically, there are numerous studies on the e¤ects of central banksliquidity measures on money markets and FX and cross-currency swap markets in the rst stage of the crisis (e.g. Hördahl and King 2008, Baba et al. 2008, Christensen et al. 2009, Taylor and Williams 2009, Thornton 2010) and on the e¤ects of subsequent large-scale asset purchases on long-term interest rates and other asset prices (e.g. DAmico and King 2010, Hamilton and Wu 2010, Neely 2010, Gagnon et al. 2011, Joyce, Lasaosa, Stevens and Tong 2011). For a survey and comparison of the estimated e¤ects of recent large-scale asset purchases on ten-year yields, see Williams (2011). Cecioni et al. (2011) provide a survey of the evidence on the e¤ectiveness of the various unconventional monetary policy measures adopted by the Federal Reserve and the Eurosystem. Overall, these studies nd that such policies were e¤ective in reducing nancial market risk spreads or yields.
2
it is not clear whether the experience of the Bank of Japan during that period can be
generalized to a worldwide nancial crisis.
In this paper, we propose an alternative way to assess the e¤ects of unconventional
monetary policies on the macroeconomy during the global nancial crisis. We focus ex-
clusively on the period since the onset of the crisis, but enhance the e¢ ciency and power
of the empirical analysis by also exploiting its cross-country dimension. In particular,
the crisis has been an important common factor in the business cycles, nancial market
dynamics and monetary policy conduct of several advanced economies. This high degree
of commonality allows for the adoption of panel estimation techniques in order to improve
the accuracy of the analysis.4
More precisely, we estimate a panel structural vector autoregressive (SVAR) model
with monthly data over a sample period where central bank balance sheets e¤ectively be-
came the main policy instrument in many advanced economies. The economies included
in the panel analysis are Canada, the euro area, Japan, Norway, Sweden, Switzerland, the
United Kingdom and the United States. The time series sample is January 2008 until
June 2011. We use a mean group estimator in the spirit of Pesaran and Smith (1995)
to accommodate potential cross-country heterogeneity in macroeconomic dynamics, the
monetary transmission mechanism and the adopted unconventional monetary policy mea-
sures. In order to keep the analysis tractable, the model set-up is parsimonious but aims
to incorporate the main common features of the crisis: (i) the macroeconomic dimension
of the crisis captured by the dynamics of aggregate output and prices, (ii) the aggressive
use of balance sheet policies by central banks while policy rates got stuck at the zero lower
bound and (iii) the recurrent bouts of uncertainty and risk aversion in nancial markets.
The e¤ectiveness of unconventional monetary policy is assessed by estimating the e¤ects of
exogenous innovations to central bank assets, conditioning on the state of the macroecon-
omy and, importantly, on nancial turmoil and macroeconomic risks which we proxy by
implied stock market volatility. The latter is key to disentangling the endogenous reaction
4Almunia et al. (2010) have used a similar approach to analyze the impact of monetary and scal policy in the Great Depression. Gavin and Theodorou (2005) show that adopting a panel approach in a macro framework helps to uncover common dynamic relationships which might otherwise be obscured by idio-syncratic e¤ects at the individual country level. See also Goodhart and Hofmann (2008) or Assenmacher-Wesche and Gerlach (2008) for a discussion of these issues and applications of panel VAR analysis to the link between monetary policy and asset prices in OECD countries.
3
of central bank balance sheets to the global nancial crisis and exogenous monetary policy
shifts, similar to the importance of conditioning on commodity prices as an indicator of
nascent ination when identifying conventional monetary policy shocks (Sims 1992).
We nd that an expansionary unconventional monetary policy shock leads to a signi-
cant but temporary rise in output and prices, a result that turns out to be robust to various
perturbations of the model specication. The output e¤ects are qualitatively similar to
the ones typically found in the literature on the e¤ects of conventional monetary policy
(e.g. Christiano et al. 1999, Peersman and Smets 2003). The impact on the price level,
on the other hand, seems to be less persistent and weaker. Furthermore, the individual
country results indicate that the panel estimates do not obscure signicant cross-country
heterogeneity. Specically, we nd no major cross-country di¤erences in the macroeco-
nomic e¤ects of shocks to central bank balance sheets, despite the di¤erent measures that
were taken in response to the crisis.
The remainder of the paper is organized as follows: The next section discusses some
stylized facts on the macroeconomy and unconventional monetary policy in the economies
we consider. After a description of the panel VAR model and the data in Section 3, Section
4 presents the main results. Some robustness checks are performed in Section 5, whereas
cross-country di¤erences are discussed in Section 6. Finally, Section 7 concludes.
2 Central bank balance sheets and the crisis: some facts
The global nancial crisis has been a major common economic factor in several advanced
economies. Figure 1 shows the evolution of key macroeconomic variables, nancial market
volatility and indicators of the monetary policy stance over the period January 2007 until
June 2011 for eight economies: Canada, the euro area, Japan, Norway, Switzerland, Swe-
den, the United Kingdom and the United States. The charts reveal the close correlation of
aggregate output and price dynamics over this period. All economies were confronted with
a signicant fall in economic activity after the collapse of Lehman Brothers in September
2008, and an accompanying decline of ination rates, in many cases to temporarily nega-
tive levels, shortly afterwards. By mid-2011, many economies did still not fully recover to
4
their pre-crisis level of economic activity.
Figure 1 reveals that there was also a very close correlation across economies of the
evolution in nancial market risk aversion, measured by the implied volatility index (VIX)
for the major stock market index.5 The VIX is considered to be a prime gauge for -
nancial market risk aversion and a general proxy for nancial turmoil, economic risk and
uncertainty. Indeed, the charts show that the implied volatility indices started to creep
up with the onset of the crisis in mid-2007 and shot up dramatically with the collapse of
Lehman Brothers. After receding subsequently, they increased again during 2010 when
concerns about the economic recovery mounted, and in early 2011 with the onset of euro
area sovereign debt crisis.
There has also been a strong cross-country commonality in the conduct of monetary
policy over this period. After the intensication of the crisis, policy rates were rapidly
lowered towards their e¤ective lower bounds in early 2009. In parallel, the assets on
central bank balance sheets have in many economies grown to an unprecedented size
reecting unconventional monetary policy measures taken to provide liquidity to ailing
nancial sectors and to support faltering economies through lower long-term interest rates
and nancial market risk premia. The size of the balance sheets of the Federal Reserve
and the Bank of England tripled, while that of the Eurosystem doubled. The Bank of
Japans assets, in contrast, increased only mildly over the crisis period. Most of the
increase occurred in March 2011 when the Bank of Japan injected liquidity in response to
the Tōhoku earthquake and tsunami. Among the smaller economiescentral banks, the
Swedish Riksbank, the Swiss National Bank and, to a lesser extent, the Bank of Canada,
expanded the size of their balance sheets sharply, while the Norges Banks nancial assets
increased only temporarily after the Lehman collapse.6
Also the monetary base expanded considerably in most economies. However, the last
two charts of Figure 1 show that the expansion was often not proportional to the increase
5 Implied stock market volatility indices are forward looking measures of stock index volatility computed based on option prices and measure market expectations of stock market volatility in the next 30 days. For a more detailed discussion of the VIX and its interpretation, see Whaley (2009).
6For Norges Bank, we use total nancial assets instead of total assets (ie. we exlude in particular the investments of the government pension fund) in order to focus on that part of the balance sheet that reects unconventional monetary policy measures.
5
in central bank assets. In particular, many central banks sterilized in part the e¤ects of
their unconventional policies on base money so that the unconventional measures taken
were essentially not as clearly reected in the monetary base as they were in central bank
assets. Overall, therefore, central bank assets appear to be a better gauge for central
banksunconventional monetary policies than the monetary base.
Figure 2 provides the composition of the eight central banks balance sheets. The
charts reveal that, while unconventional policies typically led to an increase in balance
sheets, their design varied across economies and also within economies over time, reecting
di¤erences in nancial structure and the evolution of the crisis over time. For instance, the
expansion of the Federal Reserves and the Bank of Englands balance sheet was initially
driven by lending to the nancial sector and subsequently by large-scale purchases of both
private sector and government securities. The Eurosystems unconventional monetary
policy primarily focused on lending to nancial institutions. In the wake of the euro area
sovereign debt crisis and the subsequent introduction of the Securities Market Programme,
security purchases however became a more important factor. The expansion of the Swiss
National Banks balance sheet was in turn mainly driven by purchases of foreign exchange.
Thus, while there was a high degree of commonality in central banksresponse to the
crisis, there was also a considerable degree of heterogeneity in the design of central bank
balance sheet policies that needs to be taken into account and the relevance of which
should be assessed to the extent possible in the empirical analysis.
3 A panel VAR model to analyze the nancial crisis
Structural VAR techniques have been extensively used as a tool to analyze the macroeco-
nomic e¤ects of conventional monetary policy innovations. Examples include Bernanke
and Blinder (1992), Strongin (1995), Bernanke and Mihov (1998) and Christiano et al.
(1999) for the United States or Peersman and Smets (2003) for the euro area. In this
paper, we adopt a panel VAR approach to explore the dynamic e¤ects of unconventional
monetary policy shocks. The use of panel techniques allows us to obtain more e¢ cient
estimates relative to country-by-country estimations by also exploiting the cross-sectional
6
dimension. On the one hand, we take into account the correlation amongst the residuals
across countries to capture (unobserved) factors that are common to all economies while
unconventional monetary policy shocks are simultaneously identied. On the other hand,
we use a mean group estimator in the spirit of Pesaran and Smith (1995). In contrast
to the standard xed e¤ects panel estimator, the mean group estimator allows for cross-
country heterogeneity and does not require that the economic structures and dynamics of
the economies in the VAR are the same.7 This allows us to take into account di¤erences
across countries in design and transmission of unconventional monetary policy measures.
3.1 Benchmark specication
The panel VAR model that we consider has the following representation:
Yi;t=$i +A(L)iYi;t1 +Bi"i;t $(1)
whereYi;tis a vector of endogenous variables,$i $a vector of constants,A(L)ia ma-
trix polynomial in the lag operatorL,andBithe contemporaneous impact matrix of
the mutually uncorrelated disturbances"ifor economiesi=1;:::;N. In the benchmark
specication, the vector of endogenous variablesYi;tcomprises four variables: the log of
seasonally adjusted real GDP,8 the log seasonally adjusted consumer price index, the log
level of seasonally adjusted central bank assets,9 and the level of implied stock market
volatility (VIX) of the national stock market index.10
This specication, while highly parsimonious for the sake of analytical tractability
under the constraint of a rather short sample period, aims to grasp the main features of
7Fixed e¤ects estimators are inconsistent in dynamic panels if the coe¢ cients on the endogenous vari-ables di¤er across countries. In particular, restricting the coe¢ cients to be the same across groups induces serial correlation in the residuals when the regressors are autocorrelated (Holtz-Eakin et al. 1988). This serial correlation does not vanish with instrumental variables. In contrast, a mean group estimator provides a consistent estimate of the mean e¤ects by averaging across countries. See also Assenmacher-Wesche and Gerlach (2010) for a discussion of this approach within panel VARs.
8A monthly measure of real GDP was obtained based on a Chow-Lin interpolation procedure using industrial production and retail sales as reference series.
9Total nancial assets in the case of Norges Bank. 10The specication of the VAR in levels allows for implicit cointegrating relationships in the data (Sims
et al. 1990). A more explicit analysis of the long-run behavior of the various variables is however limited by the relatively short sample available.
7
the crisis. First, the dynamics of aggregate output and prices are supposed to capture the
macroeconomic dimension of the crisis.
Second, central bank assets represent the (unconventional) monetary policy instrument
while policy rates are not included in the benchmark model. This reects the notion
that, with the reaching of the lower bound of policy rates and the widespread adoption
of unconventional monetary policies, interest rate rules have implicitly been replaced by
quantitative reaction functions in the spirit of McCallum (1988), where the main policy
instrument is a quantitative aggregate.11 In the benchmark VAR specication, we include
central bank assets instead of the monetary base as the quantitative policy instrument since
the analysis in Section 2 suggested that the former is a better gauge of unconventional
monetary policies during the crisis than the latter.12
The use of central bank assets as the (aggregate) unconventional monetary policy in-
strument obviously fails to take into account possible composition e¤ects, ie. di¤erences
in the e¤ectiveness of di¤erent types of unconventional monetary policies (large-scale and
long-term lending to banks, FX interventions, purchases of public or private securities).
However, if such di¤erences are important, this should be reected in the individual coun-
try results on which the mean group estimator will be based and which are reported in
Section 6. Also, the stock of central bank assets does of course not grasp announcement
e¤ects of unconventional monetary policies. It is however not clear in general how such
e¤ects could be captured in a VAR set-up. The approach taken in this paper instead fo-
cuses on the e¤ects of central banksunconventional monetary policy actions as reected
in the size of the central bank balance sheet. It could hence be seen as an assessment of
the overall "stock e¤ect" of central bank balance sheet policies on the macroeconomy.13
Finally, the benchmark VAR model also contains the implied stock market volatility
11However, the results are robust to including policy rates in an extended specication of the panel VAR (see Section 5). 12Moreover, Borio and Disyatat (2010) suggest that, because of the close substitutability of bank reserves
and other short-term central bank paper, the e¤ectiveness of balance sheet policies does not hinge on an accompanying change in the monetary base. Notice, however, that the results are robust to using base money as the policy instrument as well as adding policy rates to the benchmark VAR model (see Section 5). 13The importance of the stock e¤ect of bond purchases, i.e. the negative impact on bond yields of
higher public bond holdings, has been emphasised and demonstrated in a number of recent papers (e.g. DAmico and King 2010, Meaning and Zhu 2011). Here, the concept of stock e¤ect is applied more broadly pertaining to total assets held by the central bank.
8
index (VIX) for each economy as a general proxy for nancial turmoil and economic risk
over the sample period. The VIX, which is commonly referred to as a "fear index" (Whaley
2000) reecting its capacity as an indicator for nancial market risk aversion, should also
capture uncertainty shocks that have probably been an important driver of macronancial
dynamics during the crisis (see e.g. Bloom 2009, Bacchetta and van Wincoop 2010, Bruno
and Shin 2012).
Conditioning on such an indicator is also of key importance to disentangle exogenous
innovations to central bank balance sheets from endogenous responses to nancial market
risk perceptions and uncertainty, as unconventional monetary policies were launched and
balance sheets increased in direct reaction to nancial and macroeconomic jitters. As was
shown in Section 2, central bank assets increased dramatically with the intensication of
the crisis when stock market volatility exploded. In fact, both variables spiked at exactly
the same time, namely in October 2008. Failing to take into account the endogenous
reaction of central bank balance sheets to nancial turbulence and economic uncertainty
could seriously bias the estimation results. For instance, the econometric model could
potentially attribute the fall in output and prices that followed the collapse of Lehman
Brothers to the increase in central bank assets although it was driven by the rise in risk
aversion and nancial market instability. The importance of the inclusion of the VIX
as a proxy for nancial turmoil and uncertainty in a VAR in order to properly identify
an unconventional monetary policy shock during the crisis can be seen as analogous to
the importance of including indicators for future ination, such as commodity prices, in
conventional monetary policy VARs to identify a conventional monetary policy shock (see
e.g. Sims 1992, Christiano et al. 1999).
3.2 Identication
An unconventional monetary policy shock is identied as an exogenous innovation to the
central bank balance sheet. Isolating exogenous balance sheet shocks involves making
identifying assumptions to estimate the parameters of the feedback rules which relate
central bank actions to the state of the economy, i.e. the variables policymakers look at
when setting their operating instruments (Christiano et al. 1999). To do so, we impose a
9
mixture of zero and sign restrictions on the contemporaneous impact matrixBof equation
(1). First, we assume that there is only a lagged impact of shocks to the central bank
balance sheet on output and consumer prices. In other words, the contemporaneous impact
on both variables is restricted to be zero. On the other hand, innovations to output and
consumer prices are allowed to have an immediate e¤ect on the balance sheet (and stock
market volatility). This assumption, which is common in monetary transmission studies,
disentangles monetary policy shocks from real economy disturbances such as aggregate
supply and demand shocks.
Second, we assume that an expansionary unconventional monetary policy shock does
not increase stock market volatility. This restriction is needed in order to disentangle ex-
ogenous innovations to the central bank balance sheet from their endogenous response to
nancial turmoil, and from nancial market disturbances. It follows as a complementary
restriction from the assumption that central bank assets increase in response to innova-
tions to the VIX, reecting the above consideration that central banks responded often
immediately through unconventional policies to mounting nancial market uncertainty. A
recursive structure with central bank assets ordered after stock market volatility is inad-
equate and potentially biasing since monetary policy interventions should be allowed to
immediately inuence nancial market sentiment.14 At the same time, the sign restric-
tion reects the notion that unconventional monetary policies had the e¤ect of mitigating
concerns about nancial and economic instability captured by stock market volatility.15
Indeed, there is widespread agreement that in particular central banksunconventional
monetary policy actions were crucial to mitigate the tail risks of a nancial meltdown
(BIS 2012).
The identifying assumptions are summarized in the table below. The sign restrictions
14The need to allow for contemporaneous interaction between monetary policy and nancial market variables in the context of the analysis of the transmission of conventional monetary policy shocks has been emphasised by Bjørnland and Leitemo (2009) and Eickmeier and Hofmann (2012). 15Put di¤erently, non-standard monetary policy measures which did lead to increased volatility are
not identied but captured by the remaining innovation in the VAR. Notice that the sign restriction is also consistent with the negative link between nancial market liquidity and volatility established by Brunnermeier and Pedersen (2009) and evidence on the interaction between the VIX and conventional monetary policy presented in Bekaert et al. (2010).
10
are imposed on impact and the rst month after the shock.
Identication of an (unconventional) central bank balance sheet shock
Output Prices VIX Central bank assets
0 0 6 0>0
3.3 Estimation
The panel VAR is estimated over the sample period January 2008 June 2011 and includes
eight industrial economies: Canada, the euro area, Japan, Norway, Switzerland, Sweden,
the United Kingdom and the United States. Data were taken from the BIS database,
Datastream and national sources. Based on the usual lag-length selection criteria, the
estimations include two lags of the endogenous variables.16
The mean group panel analysis is based on the following procedure. First, each equa-
tion of the reduced form VAR is estimated at the individual country level taking into
account the correlation amongst the residuals of the same endogenous variable across
economies (i.e. the correlation between all output residuals, between all price residuals,
between all VIX residuals, and between all balance sheet residuals). This can accurately be
done using the Zellner (1962) Feasible Generalized Least Squares (FGLS) estimator given
the fact that we only have eight economies in our panel. Accordingly, (unobserved) factors
that are common to all economies such as oil shocks or nancial market disturbances which
are not captured by the VIX are taken into account in the estimations. Estimating the
equations separately by OLS, which is usually done for individual country VARs, would
waste such information. The greater the correlation of the residuals across economies, the
greater the e¢ ciency gain of applying FGLS. Second, we draw a random decomposition
Bof the variance-covariance matrix at the individual country level with the restriction
that the candidate decompositions for all economies are from the same structural model
in order to have a mean decomposition which is also from the same model.17 Third, the
16The results proved robust to di¤erent specications of the lag length. 17Practically, this means that the rotation matrix to generate a possible decomposition of the variance-
covariance matrix has to be the same across countries. See Peersman (2005) for the derivation of such possible decompositions, and Fry and Pagan (2007) for issues related to mixing multiple models when using sign restrictions.
11
random decompositions are used to construct impulse response functions for each indi-
vidual economy. If the impulse response functions satisfy the imposed restrictions for all
economies simultaneously, the draw is kept. Otherwise the draw is rejected. Finally, we
average the impulse response functions from the individual economies to get a mean group
impulse response function. We repeat this procedure by means of bootstrapping until we
have 5,000 mean group impulse response functions.18 In the gures, we report the 16th
and 84th percentiles of this exercise.
4 Benchmark panel VAR results
Figure 3 shows the impulse responses for an unconventional monetary policy shock ob-
tained from the panel VAR. The impulse responses indicate that the shock is characterized
by an increase in the central bank balance sheet of about 3% which fades out after about
six months.19 In line with the imposed sign restrictions, implied stock market volatility
falls on impact by about 1 percentage point, but the response remains negative for almost
one year.
The responses of output and prices indicate that unconventional monetary policy mea-
sures are e¤ective in supporting the macroeconomy. Both output and prices display a
signicant increase. Output is found to rise with a peak e¤ect after about six months and
to gradually return to baseline after about 18 months. Compared to the existing evidence
on the transmission of conventional monetary policy shocks that are associated with a
change in the short-term interest rate, the response pattern of output is qualitatively very
similar. The impact on prices is, however, di¤erent. We nd a temporary signicant e¤ect
with a peak coinciding with that of the output response, while the impact of interest rate
shocks on the price level is found to be very sluggish with a peak only after about two
years or even later.20
18On average, about 23 draws are needed to have a succesful decomposition for all individual countries. 19The nding that central bank assets return to baseline is consistent with the response pattern of short-
term interest rates after a conventional monetary policy shock. It reects the feedback e¤ects of lower stock market volatility and improved macroeconomic conditions through the estimated implicit reaction function for central bank assets. 20At this stage, it is not possible to pin down whether this di¤erence is the result of the relatively short
sample period of our analysis compared to the longer datasets that are used in the existing literature on conventional monetary policy.
12
When we compare the magnitudes of the e¤ects, it appears that unconventional mone-
tary policy shocks have relatively larger output and smaller price e¤ects than conventional
monetary policy shocks. More precisely, the peak e¤ect of an unconventional monetary
policy shock on output is estimated to be about three times larger than the peak e¤ect on
prices. In contrast, studies on the transmission of interest rate shocks (e.g. Christiano et
al. 1999, Peersman and Smets 2003, Eickmeier and Hofmann 2012) usually nd the e¤ect
of a monetary policy shock on output to be only about 1.5 times larger than the impact
on the price level. A similar relatively subdued e¤ect on prices has also been obtained for
the Bank of Japans quantitative easing between 2001 and 2006 (e.g. Schenkelberg and
Watzka 2011). One potential explanation for this weaker price level response could be that
the unconventional monetary policy shocks were estimated over a recession or economic
stagnation period where the aggregate supply function is potentially convex because of
downward rigidity in nominal wages and prices (see e.g. Ball and Mankiw 1994). In such
a situation, changes in aggregate demand, also those driven by monetary policy, would
have a stronger e¤ect on output and a weaker e¤ect on prices. This explanation is also
commonly put forward to explain why monetary policy shocks have a larger e¤ect on out-
put and a smaller e¤ect on the price level in recessions (e.g. Peersman and Smets 2002,
Weise 1999).
Across the eight economies covered by our panel analysis, the average increase of the
size of central banks assets over the sample period was about 100%. When we take the
panel evidence on the e¤ects of interest rate shocks by Assenmacher-Wesche and Gerlach
(2010) as a base for comparison, a back of the envelope calculation suggests that this
doubling of balance sheets has an impact on output which is approximately equivalent to
a 300 basis points cut in policy rates. While these numbers are also very similar to those
obtained by studies assessing the impact of unconventional monetary policy measures
implemented by major central banks in response to the crisis,21 it is important to note
that the massive expansion of central bank balance sheets in the wake of the crisis did not
21For the United States, Chung et al. (2011) estimate that the Federal Reserves programmes (LSAP1 and LSAP2) will raise the level of real GDP almost 3% by the second half of 2012, a stimulus that would have required cutting the federal fund rates by approximately 3 percentage points relative to baseline from early 2009 to 2012. For the United Kingdom, a recent Bank of England study (Joyce, Tong and Woods 2011) concludes that the bond purchases increased the level of GDP by 0.52% at the peak suggesting that the e¤ect of quantitative easing was equivalent to a 150300 basis point cut in the Bank Rate.
13
represent an exogenous unconventional monetary policy shock. This becomes clear when
we consider the variance decomposition of the mean group panel VAR reported in Figure
4.22 The decompositions indicate that exogenous balance sheet shocks account for only a
small fraction of output and price variability. They are even not the main contributor to
the forecast error variance of central bank balance sheets. Central bank assets uctuations
are instead mainly driven by real economy shocks and innovations to the VIX. The latter
disturbances explain approximately 40% of the forecast error variance. The endogenous
reaction to shocks to aggregate uncertainty was therefore an important factor behind the
evolution of central bank balance sheets during the crisis.23 The decomposition analysis
further shows that volatility shocks also explain a considerable part of the forecast error
variance of output and prices (between 30% and 40%), supporting the notion that risk
shocks were important drivers of macroeconomic dynamics during crises.
5 Robustness analysis
5.1 Variations to the benchmark model
In order to assess the robustness of our results to alternative modelling choices, we consider
three variations to the benchmark VAR. Specically, we replicate the analysis of the pre-
vious section using respectively a di¤erent econometric estimator, a di¤erent quantitative
policy instrument, and a di¤erent output measure. Figure 5 shows the impulse response
bands obtained when (i) the VAR is estimated using the Fixed E¤ects (FE) estimator in-
stead of the Mean Group estimator, (ii) the VAR is estimated using the monetary base as
the quantitative policy instrument instead of central bank assets and (iii) when industrial
production replaces real GDP as the measure of aggregate output.
The rst column of Figure 5 shows that our ndings are qualitatively robust with 22The variance decomposition is performed based on the median target method of Fry and Pagan (2007).
The shock labelled as "VIX shock" is implicitly identied as a by-product of our identifying restrictions for the unconventional monetary policy shock. It is a shock that increases the VIX and the central bank balance sheet and does not a¤ect output and prices on impact. The impulse responses to this shock, which we do not report, show that it is associated with a short-lived sharp increase in the VIX and the central bank balance sheet and a temporary strong and highly signicant decline in output and prices. 23Historical decompositions at the individual country level, which we do not report for the sake of brevity,
further reveal that in particular the sharp increase in central bank balance sheets after the collapse of Lehman Brothers was almost entirely driven by innovations to the VIX variable.
14
regard to the type of panel estimator used. The e¤ects based on the FE estimator are
somewhat more persistent and quantitatively somewhat larger. This nding is consistent
with di¤erences between mean group and xed e¤ects estimation results identied by
previous studies (e.g. Assenmacher-Wesche and Gerlach 2008) and reects the problems
associated with the Fixed E¤ects estimator in dynamic panels outlined in more detail in
Section 3. The benchmark results also turn out to be robust to the use of the monetary
base as the quantitative policy instrument (see second column of Figure 5). The e¤ects of a
shock to the monetary base on output and prices are both qualitatively and quantitatively
very similar. Finally, when industrial production is used as the measure of output instead
of real GDP (third column of Figure 5), the results are essentially una¤ected. The only
di¤erence is that the reaction of output is somewhat larger. This nding is consistent with
a higher responsiveness of industrial production to monetary shocks that is also found in
the literature on the transmission of interest rate shocks.
5.2 Model extensions
We also assess the robustness of the benchmark results to the inclusion of additional
variables that might have a bearing on the analysis. Specically, we consider two extensions
of the benchmark model: (i) a version including the policy rate and (ii) a version including
the outstanding debt of the central government.
While policy rates have been at their e¤ective lower bounds most of the time in the
sample period, the analysis still includes the policy rate cuts that occurred during 2008 and
early 2009 and a few rate hikes later on. There is hence the risk that the unconventional
monetary policy shocks capture in part the e¤ects of these policy rate cuts. In order to
assess the relevance of this potential caveat, we add the policy rate to the benchmark VAR
and identify the central bank balance sheet shock with the additional restriction that it
does not a¤ect the policy rate on impact. This is done to avoid that the unconventional
monetary policy shock is associated with a change in the policy rate. Figure 6 shows the
impulse responses for the balance sheet shock obtained from this extended model together
with the impulse responses from the benchmark model. The charts show that there is
virtually no signicant di¤erence. The bands are very similar in shape and overlap for all
15
variables. The central bank balance sheet shocks identied in the benchmark model thus
do not appear to be materially contaminated by the e¤ects of policy rate changes.
In a second model extension, we consider potential overlaps of central bank and gov-
ernment balance sheet policies. Fiscal authorities in many of the economies covered by
our analysis responded to the nancial crisis by adopting a number of support measures
for the nancial sector and stimulus packages for the economy. Some of these measures
(of course not those that took the form of guarantees) can also be interpreted as bal-
ance sheet policies as they were associated with an increase in the public debt that was
similarly dramatic as the increase in central bank balance sheets.24 These expansions of
government debt could contaminate the unconventional monetary policy shock we identify
in the benchmark model if shocks to public debt would have the same short-term e¤ects
as central bank balance sheet shocks, i.e. if they would also be associated with an increase
in central bank assets and a fall in stock market volatility, whilst having a delayed impact
on output and prices.
In order to address this potential caveat, we estimate an extended model including
the outstanding debt of the central government in the model.25 For the identication, we
assume in addition to the benchmark identifying restrictions that the public debt does not
react on impact to the central bank balance sheet shock. We further assume that inno-
vations to public debt can have a contemporaneous impact on output and prices. These
restrictions are consistent with the recursive identication schemes commonly adopted in
studies on the macroeconomic e¤ects of scal policy shocks. The impulse responses to a
central bank balance sheet shock in this extended model, which are shown in Figure 7,
are very similar to those from the benchmark model. The only notable di¤erence is that
the price response is now insignicant, but the response bands of the two models overlap.
Public debt is found to fall signicantly in response to the central bank balance sheet
shock. This probably reects positive feedback e¤ects of the shock-induced increase in
output on public nances.
24Just like changes in the stock of central bank assets do not capture announcement e¤ects of unconven-tional monetary policy, the stock of public debt does not capture the announcement e¤ect of scal policy measures. 25Monthly data on outstanding central government debt are available for all countries except for Switzer-
land where quarterly data were interpolated using a Cubic spline. The data were obtained from national central banks and national debt management agencies.
16
6 Individual country estimates
Since the panel analysis is based on a mean group estimator, it also yields individual
country estimates. We can thus directly assess the degree of cross-county heterogeneity in
the dynamic e¤ects of central bank balance sheet shocks. The individual country results
could also shed some light on the di¤erences in the e¤ectiveness of di¤erent types of
unconventional monetary policies. If certain types of unconventional monetary policies,
e.g. large-scale bond purchases, would have stronger macroeconomic e¤ects, then this
should also be reected in the estimated impulse responses for those countries that heavily
relied on this specic measure.
The individual country results are reported in Figure 8. Specically, the dotted (red)
lines represent the estimated impulse response bands for each individual economy, whereas
the shaded areas those of the panel VAR. The dynamic e¤ects of a shock to central bank
assets turn out to be qualitatively similar across countries and comparable to the panel
results. In particular, the panel VAR and the individual-country impulse responses overlap
most of the times. For most economies, we nd a signicant positive temporary impact on
economic activity and also the magnitude of the e¤ect appears to be fairly similar. The
e¤ect on the price level is, however, somewhat more dispersed across countries. In only
half of the countries the impact on prices seems to be signicant.
Inspecting the impulse responses in more detail, the dynamic e¤ect of an unconven-
tional monetary policy shock are very similar in the U.S., the euro area, Canada, and the
UK, except for the insignicant price level response in the latter country. Interestingly, the
euro area results are very similar both qualitatively and quantitatively to those obtained
by Peersman (2011) using a di¤erent shock identication scheme and a sample that also
covers the pre-crisis period. For Switzerland and Sweden, the output e¤ects are somewhat
more persistent than in the other economies, which is probably the result of the higher
persistence of the shock in these economies as reected in the more persistent increase
in central bank assets. On the other hand, the output responses are hardly statistically
di¤erent from zero in Japan and Norway. This nding may be due to the relatively small
changes in central bank assets in these economies over the sample period (see Section
2), which probably makes it more di¢ cult to pin down the e¤ects of an unconventional
17
monetary policy shock.
Overall, the qualitatively similar results at the country level suggests that the panel
analysis does not seem to obscure considerable cross-country heterogeneity. This nding
could also be interpreted as indicating that, despite the heterogeneity in the design and
calibration of central bank balance sheet policies, their e¤ectiveness was qualitatively
quite similar across countries, possibly because central banks designed these policies to
the specic needs of their respective nancial sectors and economies.
7 Conclusions
This paper has examined the macroeconomic e¤ectiveness of unconventional monetary
policies adopted in the wake of the nancial crisis by exploring the dynamic e¤ects of a
shock to the central bank balance sheet on output and the price level with a panel VAR
estimated on monthly data from eight advanced economies over the crisis period. We nd
that an exogenous increase in central bank balance sheets at the zero lower bound leads to
a temporary rise in economic activity and the price level. The qualitative response pattern
of output is very similar to that obtained by previous studies on the e¤ects of interest rate
shocks, while the reaction of the price level is weaker and less persistent. The estimations
also suggest that the panel results do not obscure considerable cross-country heterogeneity
in the macroeconomic consequences, despite the di¤erences in design and calibration,
possibly reecting the fact that central banks implemented these policies according to the
specic needs of their respective nancial sectors and economies.
These results suggest that the unconventional monetary policy measures adopted by
central banks in the wake of the global nancial crisis provided temporary support to
their economies. However, this does not imply that an expansion of central bank balance
sheets will in general have positive macroeconomic e¤ects. The set-up of the analysis is
specically tailored to the crisis period, when unconventional monetary policy measures
were actively used to counter nancial and economic tail risk. The results therefore do not
in general pertain to the possible e¤ects of central bank balance sheet policy in non-crisis
18
periods.26
Finally, there are a number of caveats related to our analysis that need to be borne
in mind. First, for the sake of tractability, the analysis does not explicitly assess the ef-
fectiveness of di¤erent types of unconventional monetary policies. The individual country
results do not indicate that such composition e¤ects are a major distorting factor, but a
more careful analysis could be done in future research. Second, the analysis does not cap-
ture the announcement e¤ects of unconventional monetary policies. Just like traditional
VAR studies that estimate the e¤ects of conventional monetary policy, the approach taken
in this paper focuses instead on identifying the e¤ects of central banksunconventional
monetary policy actions, which could be seen as an assessment of the overall "stock e¤ect"
of central bank balance sheet policy on the macroeconomy.
References
[1] Almunia, M, A Bénétrix, B Eichengreen, K ORourke and G. Rua (2010) "From Great
Depression to Great Credit Crisis: similarities, di¤erences and lessons," Economic
Policy, 25, 219-265.
[2] Assenmacher-Wesche, K and S Gerlach (2008), "Monetary policy, asset prices and
macroeconomic conditions: A panel VAR approach", mimeo, Goethe University
Frankfurt am Main.
[3] Assenmacher-Wesche, K and S Gerlach (2010), "Financial structure and the impact of
monetary policy on property prices", mimeo, Goethe University Frankfurt am Main.
[4] Baba, N, F Packer and T Nagano (2008), The spillover of money market turbulence
to FX swap and cross-currency swap markets, BIS Quarterly Review, March, 7386.
[5] Bacchetta, P and E van Wincoop (2010), "Explaining sudden spikes in global risk",
University of Lausanne, mimeo. 26 It is further important to note that our analysis does not capture potential negative side-e¤ects of
prolonged monetary easing brought about by expanded central bank balance sheets in conjunction with low policy rates, such as delaying private and public sector balance sheet repair in the economies hardest hit by the crisis, global monetary policy spillover e¤ects and longer-term risks for central bankscredibility and operational autonomy. See BIS (2012) for a more comprehensive discussion of these side-e¤ects.
19
[6] Ball, L and N G Mankiw (1994), Asymmetric price adjustment and economic uc-
tuations, Economic Journal, 104, 247-261.
[7] Bekaert, G, M Hoerova, M Lo Duca (2010), "Risk, uncertainty and monetary policy,"
NBER Working Papers 16397, National Bureau of Economic Research.
[8] Bernanke, B S, A S Blinder (1992), "The Federal Funds rate and the channels of
monetary transmission," American Economic Review, 82(4), 901-21.
[9] Bernanke, B S, I Mihov (1998), "Measuring monetary policy", The Quarterly Journal
of Economics, 113(3), 869-902
[10] BIS (2012), Bank for International Settlements 82nd Annual Report, Basel, Switzer-
land.
[11] Bloom, N (2009), "The impact of uncertainty shocks", Econometrica, 77(3), 623685.
[12] Bjørnland, H and K Leitemo (2009), "Identifying the interdependence between US
monetary policy and the stock market", Journal of Monetary Economics, 56, 275-282.
[13] Borio, C and P Disyatat (2010), "Unconventional monetary policies: An appraisal",
The Manchester School, 78, 5389 (also published as BIS Working Paper, 292).
[14] Brunnermeier, M and L H Pedersen (2009), "Market liquidity and funding liquidity",
Review of Financial Studies, 22(6), 2201-2238.
[15] Bruno, V and H S Shin (2012), "Capital ows and the risk-taking channel of monetary
policy", paper presented at the 11th BIS Annual Conference, Lucerne, Switzerland.
[16] Cecioni, M, G Ferrero and A Secchi (2011), "Unconventional monetary policy in
theory and in practice ", Bank of Italy Occasional Papers, 102.
[17] Christensen, J, J Lopez and G Rudebusch (2009), "Do central bank liquidity facilities
a¤ect interbank lending rates?", Federal Reserve Bank of San Francisco, Working
Paper, 2009-13.
[18] Christiano, L, M Eichenbaum and C Evans (1999), "Monetary policy shocks: What
have we learned and to what end?", in J Taylor and M Woodford (eds.), Handbook
of Macroeconomics, North-Holland, Amsterdam, 65-148.
20
[19] Chung, H, J P Laforte, D Reifschneider and J Williams (2011), "Estimating the
macroeconomic e¤ects of the Feds asset purchases", Federal Reserve Bank of San
Francisco, Economic Letter, 3.
[20] DAmico, S and T King (2010), "Flow and stock e¤ects of large-scale Treasury pur-
chases", FRB Finance and Economics Discussion Paper, 2010-52.
[21] Eickmeier, S and B Hofmann (2012), "Monetary policy, housing booms and nancial
(im)balances", Macroeconomic Dynamics, forthcoming.
[22] Fry, R and A Pagan (2007), "Some issues in using sign restrictions for identifying
structural VARs", NCER Working Paper 14.
[23] Gagnon, J, M Raskin, J Remache and B Sack (2010), "Large-scale asset purchases
by the Federal Reserve: did they work?", FRBNY Sta¤ Reports, 441.
[24] Gavin, W and A Theodorou (2005), "A common model approach to macroeconomics:
using panel data to reduce sampling error", Journal of Forecasting, 24, 203-219.
[25] Goodhart, C and B Hofmann (2008), "House Prices, Money, Credit, and the Macro-
economy", Oxford Review of Economic Policy, 24, 180-205
[26] Hamilton, J D and J Wu (2010), "The e¤ectiveness of alternative monetary policy
tools in a zero lower bound environment", University of California, San Diego, mimeo.
[27] Hördahl, P and M King (2008), "Developments in repo markets during the nancial
turmoil", BIS Quarterly Review, December 2008.
[28] Holtz-Eakin, D, W Newey and H S Rosen (1988), Estimating vector autoregressions
with panel data, Econometrica, 56, 1371-1395.
[29] Joyce, M, A Lasaosa, I Stevens and M Tong (2011), "The nancial market impact of
quantitative easing", International Journal of Central Banking, 7 (3), 11361.
[30] Joyce M, M Tong, R Woods (2011): The United Kingdoms quantitative easing
policy: design, operation and impact, Bank of England Quarterly Bulletin, 2011 Q3,
20012.
21
[31] Lenza, M, H Pill and L Reichlin (2011), "Monetary policy in exceptional times",
Economic Policy, 25, 295339.
[32] McCallum, B T (1988), "Robustness properties of a rule for monetary policy",
Carnegie-Rochester Conference Series on Public Policy, 29, Autumn, 173-203.
[33] Meaning, J and F Zhu (2011), "The impact of recent central bank asset purchase
programmes, BIS Quarterly Review, December 2011, 73-83.
[34] Neeley, C J (2010), "The large-scale asset purchases had large international e¤ects",
FRBSL Working Papers, 2010-018.
[35] Peersman, G. (2005), "What caused the early millennium slowdown? Evidence based
on vector autoregressions", Journal of Applied Econometrics, 20, 185-207.
[36] Peersman, G (2011), "Macroeconomic e¤ects of unconventional monetary policy in
the euro area", CEPR Working Paper, 8348.
[37] Peersman, G and F Smets (2002), "Are the e¤ects of monetary policy in the euro area
greater in recessions than in booms?" In L Mahadeva and P Sinclair (eds), Monetary
transmission in diverse economies, Cambridge University Press, 2002, p 28-48.
[38] Peersman, G and F Smets (2003), "The monetary transmission mechanism in the
euro area: evidence from VAR analysis", in Angeloni I, A Kashyap and B Mojon
(eds.), Monetary policy transmission in the euro area, Cambridge University Press,
56-74.
[39] Pesaran, M H and R Smith (1995), "Estimating long-run relationships from dynamic
heterogeneous panels", Journal of Econometrics, 68, 79-113.
[40] Schenkelberg, H and S Watzka (2011), "Real e¤ects of quantitative easing at the zero
lower bound: Structural VAR-based evidence from Japan", Cesifo Working Paper,
3486.
[41] Sims, C (1992), "Interpreting the macroeconomic time series facts: the e¤ects of
monetary policy, European Economic Review, 36 (5), 9751000.
22
[42] Sims, C, J Stock, and M Watson (1990), Inference in linear time series models with
some unit roots,Econometrica, 58, 113144.
[43] Stone M, K Fujita and K Ishi (2011), "Should unconventional balance sheet policies
be added to the Central Bank toolkit? A Review of the Experience So Far", IMF
Working Paper, 11/145.
[44] Strongin, S (1995) The identication of monetary policy disturbances: Explaining
the liquidity puzzle, Journal of Monetary Economics, 35, 463-497.
[45] Taylor, J B and J CWilliams (2009), "A black swan in the money market", American.
Economic Journal: Macroeconomics, 1(1), 5883.
[46] Thornton, D L (2010), "The e¤ectiveness of unconventional monetary policy: The
Term Auction Facility", Federal Reserve Bank of St. Louis Working Paper, 44.
[47] Ugai, H (2007), "E¤ects of the quantitative easing policy: a survey of empirical
analyses", Bank of Japan Monetary and Economic Studies, 25, 147.
[48] Weise, C (1999), "The asymmetric e¤ects of monetary policy: A nonlinear vector
autoregression approach", Journal of Money Credit and Banking, 31, 85-108.
[49] Whaley, R (2000), "The Investor Fear Gauge", Journal of Portfolio Management, 26,
12-17.
[50] Whaley, R (2009), "Understanding the VIX", Journal of Portfolio Management, 35,
98-105.
[51] Williams, J C (2011), "Unconventional monetary policy: Lessons from the past three
years", FRBSF Economic Letters, 31.
[52] Zellner, A (1962), "An e¢ cient method of estimating seemingly unrelated regressions
and test of aggregation bias", Journal of the American Statistical Association, 57,
500-509.
23
Figure 1 - Macroeconomic dynamics, financial market volatility and monetary policy
1 Monthly GDP series derived based on Chow-Lin interpolation procedure using industrial production and retail sales as reference series.  2 Total assets. For Norges Bank total financial assets. 3 Sum of currency in circulation and banks' deposits with the central bank. For the Eurosystem, including the deposit facility; for the Riksbank, including the deposit facility and Riskbank certificates.
Sources: Datastream; national data.
EA = Euro area, US = United States, UK = United Kingdom, JP = Japan, CA = Canada, CH = Switzerland, SE = Sweden, NO = Norway
Index of real GDP, the CPI, central bank total assets and the monetary base normalized to 100 in 2007M1.
Monetary base3Central bank assets2
Real GDP1 Consumer prices
Implied stock market volatility Monetary policy rate
90
92
94
96
98
100
102
104
106
108
110
2007 2008 2009 2010 2011
EA
US
UK
JP
CH
SE
NO
CA
90
95
100
105
110
115
120
2007 2008 2009 2010 2011
0
100
200
300
400
2007 2008 2009 2010 2011
0
100
200
300
400
500
2007 2008 2009 2010 2011
0
10
20
30
40
50
60
70
80
2007 2008 2009 2010 2011
0
1
2
3
4
5
6
7
2007 2008 2009 2010 2011
Figure 2 - Central bank assets and liabilities (trillions of respective currency units)
(1) Total assets/liabilities. For Norges Bank total financial assets/liabilities. (2) Securities held outright. (3) For the Fed: Repurchase agreements, term auction credit, other loans and Commercial Paper Funding Facility. (4) Defined as the sum of currency in circulation and banks' deposits with the central bank. For the Eurosystem, including the deposit facility; for the Riksbank, including the deposit facility and Riskbank certificates. (5) Including US dollar liquidity auctions. (6) Securities issued by euro area residents, in euros. (7) Bonds and other securities acquired via market transactions and securities holdings of Bank of England Asset Purchase Facility Fund. The accounts of the Fund are not consolidated with those of the Bank. The Fund is financed by loans from the Bank which appear on the Bank’s balance sheet as an asset. (8) Outstanding amount of US dollar liquidity auctions. (9) Defined as JGS and corporate bonds.
Sources: Datastream; national data.
Bank of Canada Swiss National Bank
Swedish Riksbank Norges Bank
Federal Reserve Eurosystem
Bank of England Bank of Japan
-4
-3
-2
-1
0
1
2
3
4
2007 2008 2009 2010
Securities (2) Lending (3) FX swap Monetary base (4) Assets/ liabilities (1) -4
-3
-2
-1
0
1
2
3
4
2007 2008 2009 2010
Securities (6) Foreign currency assets (5)
-0.4
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0.4
2007 2008 2009 2010
Securities (7) FX swap (8) -200
-150
-100
-50
0
50
100
150
200
2007 2008 2009 2010
Securities (9) Foreign assets (5)
-0.1
-0.05
0
0.05
0.1
2007 2008 2009 2010
-0.4
-0.2
0
0.2
0.4
2007 2008 2009 2010
FX currency investments EUR/CHF swap
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
0.8
2007 2008 2009 2010
Foreign currency assets
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
0.8
2007 2008 2009 2010 2011
Other financial assets Foreign financial assets
Figure 3 - Impulse responses to a central bank balance sheet shock: mean group panel VAR estimation
16th and 84th bootstrap percentiles, monthly horizon
Figure 4 - Forecast error variance decompositions
Based on the median target method (Fry and Pagan 2007), monthly horizon
Output Prices
VIX Central bank assets
Output Prices
VIX Central bank assets
-0.02
0.00
0.02
0.04
0.06
0.08
0.10
0 6 12 18 24
-0.01
0.00
0.01
0.02
0.03
0.04
0.05
0 6 12 18 24
-1.6
-1.2
-0.8
-0.4
0.0
0.4
0 6 12 18 24
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
0 6 12 18 24
0.0
0.2
0.4
0.6
0.8
1.0
0 6 12 18 24
other shocks VIX shocks CB Balance sheet shocks
0.0
0.2
0.4
0.6
0.8
1.0
0 6 12 18 24
other shocks VIX shocks CB Balance sheet shocks
0.0
0.2
0.4
0.6
0.8
1.0
0 6 12 18 24
other shocks VIX shocks CB Balance sheet shocks
0.0
0.2
0.4
0.6
0.8
1.0
0 6 12 18 24
other shocks VIX shocks CB Balance sheet shocks
Figure 5 - Robustness checks: Variations to the benchmark model
16th and 84th bootstrap percentiles, monthly horizon.
Fixed effects panel VAR estimation Monetary base as policy instrument
Output
Prices
Industrial production as output measure
Central bank assetsCentral bank assets Monetary base
Output Output
VIX
Prices Prices
VIX VIX
-0.05
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0 6 12 18 24
-0.05
0.00
0.05
0.10
0.15
0.20
0.25
0 6 12 18 24
-4.5
-4.0
-3.5
-3.0
-2.5
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
0 6 12 18 24
-0.02
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16
0 6 12 18 24
-0.01
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0 6 12 18 24
-2.0
-1.6
-1.2
-0.8
-0.4
0.0
0.4
0 6 12 18 24
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-0.10
-0.05
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0 6 12 18 24
-0.02
-0.01
0.00
0.01
0.02
0.03
0.04
0.05
0 6 12 18 24
-2.0
-1.6
-1.2
-0.8
-0.4
0.0
0.4
0 6 12 18 24
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
0 6 12 18 24
Figure 6 - VAR model with the monetary policy rate
Benchmark VAR      Extended VAR with policy rate
16th and 84th bootstrap percentiles, monthly horizon.
Figure 7 - VAR model with public debt
Benchmark VAR      Extended VAR with public debt
16th and 84th bootstrap percentiles, monthly horizon.
Policy rate
Public debt
VIX Central bank assets
Output Prices
VIX Central bank assets
Output Prices
-0.02
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0 6 12 18 24
-0.02
-0.01
0.00
0.01
0.02
0.03
0.04
0.05
0 6 12 18 24
-2.0
-1.6
-1.2
-0.8
-0.4
0.0
0.4
0 6 12 18 24
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
0 6 12 18 24
-0.02
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0 6 12 18 24
-0.03
-0.02
-0.01
0.00
0.01
0.02
0.03
0.04
0.05
0 6 12 18 24
-2.0
-1.6
-1.2
-0.8
-0.4
0.0
0.4
0 6 12 18 24
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
0 6 12 18 24
-0.02
0.00
0.02
0.04
0 6 12 18 24
-0.25
-0.20
-0.15
-0.10
-0.05
0.00
0.05
0.10
0.15
0 6 12 18 24
Mean group panel VAR estimation
Individual country estimation
16th and 84th bootstrap percentiles, monthly horizon.
Output
United States Euro area
Canada Switzerland
Japan
Norway
United Kingdom
Sweden
Figure 8 - Impulse responses to central bank balance sheet shock: individual country results
Japan
Norway
Prices
United States Euro area United Kingdom
Canada Switzerland Sweden
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.25
-0.15
-0.05
0.05
0.15
0.25
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
-0.12
-0.08
-0.04
0.00
0.04
0.08
0.12
0 6 12 18 24
Mean group panel VAR estimation
Individual country estimation
16th and 84th bootstrap percentiles, monthly horizon.
VIX
United States Euro area United Kingdom Japan
Canada Switzerland Sweden Norway
Figure 8 (continued) - Impulse responses to central bank balance sheet shock: individual country results
United Kingdom Japan
Canada Switzerland Sweden Norway
United States Euro area
Central bank assets
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-2.0
-1.5
-1.0
-0.5
0.0
0.5
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24
-3.0
-2.0
-1.0
0.0
1.0
2.0
3.0
4.0
5.0
0 6 12 18 24