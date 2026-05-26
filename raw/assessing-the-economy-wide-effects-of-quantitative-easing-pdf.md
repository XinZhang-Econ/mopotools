
# Working Paper No. 443 Assessing the economy-wide effects of quantitative easing
## George Kapetanios, Haroon Mumtaz, Ibrahim Stevens and
## Konstantinos Theodoridis
### January 2012Working Paper No. 443 Assessing the economy-wide effects of quantitative easing
### George Kapetanios,(1) Haroon Mumtaz,(2) Ibrahim Stevens(3) and
### Konstantinos Theodoridis(4)
Abstract
This paper examines the macroeconomic impact of the first round of quantitative easing (QE) by the
Bank of England which started in March 2009.  Although Bank Rate, the UK policy rate, was reduced
to ½%, effectively its lower bound, the Bank’s Monetary Policy Committee felt that additional measures
were necessary to meet the inflation target in the medium term.  The policy of QE entailed buying
private and mainly public assets in large quantities using central bank money, with the aim of injecting
money into the economy and boosting nominal spending, in order to help achieve the Bank’s inflation
target.  Over the period from March 2009 to January 2010, the Bank of England purchased £200 billion
of assets, mainly consisting of government securities.  We attempt to quantify the effects of these
purchases by focusing on the impact of lower long-term interest rates on the wider economy.  This is
motivated by empirical evidence indicating that QE purchases reduced long-term UK government bond
yields by about 100 basis points.  Other transmission channels are also possible, but are not considered
in this paper.  We use three different models to conduct counterfactual simulations to estimate the
impact of QE on output and inflation:  a large Bayesian VAR;  a change-point structural VAR;  and a
time-varying parameter VAR.  Our preferred average estimates from the three models suggest that QE
may have had a peak effect on the level of real GDP of around 1½% and a peak effect on annual
CPI inflation of about 1¼ percentage points.  These estimates are shown to vary considerably across the
different model specifications, and with the precise assumptions made to generate the counterfactual
simulations, and are therefore subject to considerable uncertainty.
Key words: Bayesian methods, large-scale asset purchases, quantitative easing, vector autoregressions.
JEL classification: C11, C32, E52, E58.
(1)  Queen Mary, University of London.  Email:  g.kapetanios@qmul.ac.uk
(2)  Bank of England.  Email:  haroon.mumtaz@bankofengland.co.uk
(3)  Bank of England.  Email:  ibrahim.stevens@bankofengland.co.uk
(4)  Bank of England.  Email:  konstantinos.theodoridis@bankofengland.co.uk
The views expressed in this paper are those of the authors, and not necessarily those of the Bank of England.  The authors wish
to thank Mark Astley, Ryan Banerjee, Jagjit Chadha, Spencer Dale, Stefania D’Amico, Rodrigo Guimaraes, Mike Joyce,
Michele Lenza, Lea Paterson, Hashem Pesaran, Simon Price, Ron Smith, Ryland Thomas, Matthew Tong, Robert Woods,
Tony Yates and Chris Yeates for useful comments on a previous draft.  We also thank Ahila Karan and Lydia Silver for research
assistance.  This paper was finalised on 5 January 2012.
The Bank of England’s working paper series is externally refereed.
Information on the Bank’s working paper series can be found at
www.bankofengland.co.uk/publications/workingpapers/index.htm
Publications Group, Bank of England, Threadneedle Street, London, EC2R 8AH
Telephone +44 (0)20 7601 4030  Fax +44 (0)20 7601 3298  email mapublications@bankofengland.co.uk
© Bank of England 2012
ISSN 1749-9135 (on-line)
Contents
Summary 3
1 Introduction 5
2 Quantitative easing in the United Kingdom 7
3 Related literature 9
4 Econometric framework 12
4.1 Bayesian VAR (BVAR) 12
4.2 Change-point SVAR (MS-SVAR) 14
4.3 Time-varying parameter SVAR (TVP-SVAR) 16
5 Data 18
6 Counterfactual assumptions 19
7 Empirical results 20
7.1 Results from BVAR model 20
7.2 Results from MS-SVAR model 23
7.3 Results from TVP-SVAR model 25
8 Summary of empirical results 26
9 Conclusion 27
Appendix A: Estimation of large BVAR model 28
A.1 Prior tightness 29
Appendix B: Estimation of MS-SVAR model and selection of the number of change points 31
Appendix C: Estimation of TVP-SVAR model 32
Appendix D: Data appendix for large BVAR model 33
Appendix E: Charts 34
References 41
Working Paper No. 443 January 2012 2
Summary
This working paper describes research undertaken at the Bank to assess the macroeconomic
impact of the Monetary Policy Committee’s (MPC’s) quantitative easing (QE) policy undertaken
during March 2009 to January 2010. This, along with other work, fed into the article on ‘The
United Kingdom’s quantitative easing policy: design, operation and impact’, which was
published in the Bank of England Quarterly Bulletin, 2011 Q3.
The sharp deterioration of the global financial crisis in late 2008 led to the increased risk of a
severe downturn on a scale not seen since the Great Depression of the 1930s. In many countries,
the fiscal and monetary authorities responded with variety of conventional and less conventional
measures aimed at mitigating the effects on financial stability and the real economy. Actions
taken by central banks mainly consisted of liquidity support and large-scale asset purchases,
commonly described as quantitative easing.
The MPC of the Bank of England reduced Bank Rate, the official UK policy rate, to1/2on 5
March 2009. But despite reducing interest rates to their effective lower bound, the MPC felt that
additional measures were necessary to achieve the 2% CPI inflation target in the medium term.
The Committee therefore also announced that it would begin a large programme of asset
purchases financed by central bank money, mainly consisting of UK government bonds (gilts).
The aim of the programme of asset purchases was to inject a large monetary stimulus into the
economy, in order to boost nominal expenditure and thereby increase domestic inflation
sufficiently to meet the inflation target. Between March 2009 and the end of January 2010 the
Bank purchased a total of £200 billion assets, an amount equivalent to about 14% of UK GDP.
Asset purchases were expected to affect the real economy in a number of ways, but a key one
was through the so-called portfolio balance channel. Through this channel, asset purchases push
up the price of the assets being purchased, as well as the price of other assets that are closer
substitutes for the purchased asset than money. This in turn stimulates demand through lower
borrowing costs and increased wealth. Previous Bank work that examined the financial market
impact of large-scale asset purchases suggested that it had had a significant effect on medium and
long-term government bond (or gilt) yields. The main objective of this working paper is to gauge
Working Paper No. 443 January 2012 3
how the wider economy responded to the stimulus from QE by estimating the effects on output
and inflation. However, analysing these effects is not an easy task. It calls for a counterfactual
analysis of what would have happened to real GDP and CPI inflation if the QE policy had not
been implemented. In order to construct our no policy counterfactual, we assume that the
macroeconomic effects of QE come through the impact on government bond yields. This
counterfactual is then compared with a baseline prediction which includes QE. The difference
between the two scenarios is taken as a measure of the macroeconomic impact.
We construct conditional forecasts (for real GDP and CPI inflation) from three different
empirical models, which are all variants of models known as vector autoregressions, or VARs. In
general, VARs are systems of equations that each include lagged values of all the variables
examined, which allows them to account for the complicated interrelationships in the data. The
first model is a large Bayesian vector autoregression (BVAR), which is estimated over a rolling
sample period, to allow for structural change. The BVAR incorporates a large amount of data but
imposes minimum economic structure. The other two models are smaller models with more
underlying economic structure. One is a Markov-switching or change-point structural VAR
(MS-SVAR), where the parameters are allowed to change at a particular time, and the other is a
time-varying parameter structural VAR (TVP-SVAR), where parameters can change gradually
over time. The word ‘structural’ here means that we attempt to identify the economic causes, or
‘shocks’, that have buffeted the system. This is done using restrictions from economic theory,
which tell us about the sign or absence of effects following particular types of shock. We conduct
counterfactual analysis using all three models, examining both the macroeconomic impact of QE
and the persistence of the effects.
Our empirical results suggest that without the QE programme real GDP would have fallen even
more during 2009 and inflation would have reached low or even negative levels. Taking the more
conservative average estimates across the three models suggests that QE had a peak effect on the
level of real GDP of around11/2and a peak effect on annual CPI inflation of about11/4
percentage points. However, the magnitude of these effects varies considerably across the
different model specifications, and with the assumptions made to generate the counterfactual
simulations, so these estimates are subject to considerable uncertainty.
Working Paper No. 443 January 2012 4
1 Introduction
The sharp deterioration of the global financial crisis in late 2008 led to the increased risk of a
severe downturn on a scale not seen since the Great Depression of the 1930s. In many countries
the fiscal and monetary authorities responded with variety of conventional and less conventional
measures aimed at mitigating the effects on financial stability and the real economy. In the
United Kingdom, the Bank of England introduced a number of innovative policy measures. As
Bean (2011) describes, these measures included enhanced liquidity support, actions to deal with
dysfunctional financial markets and large-scale asset purchases. In this paper, we focus on
assessing the macroeconomic effects of the Bank’s programme of large-scale asset purchases
(LSAPs), commonly referred to as quantitative easing (QE).
The Monetary Policy Committee (MPC) of the Bank of England first officially announced that it
would begin a large programme of asset purchases, mainly of UK government bonds or gilts, on
5 March 2009, at the same time as it reduced Bank Rate, the official UK policy rate, to0.5
Despite lowering policy rates to their effective zero lower bound (ZLB), the MPC felt that
additional measures were necessary to achieve the 2% CPI inflation target in the medium term.
The aim of the programme of asset purchases financed by the issuance of central bank money
was to inject a large monetary stimulus into the economy, in order to boost nominal expenditure
and thereby increase domestic inflation sufficiently to meet the inflation target. Between March
2009 and the end of January 2010 the Bank purchased a total of £200 billion assets, representing
about 14% of UK GDP.
Most of the previous work on this topic has focused on the effects of QE on financial markets
(see Joyce, Lasaosa, Stevens and Tong (2011)). Our work by contrast focuses on measuring the
wider economic effects of the Bank’s asset purchases on output and inflation. Understanding the
effects of QE on the wider economy is of course necessary in order to appreciate the
effectiveness of QE as a policy option during times of financial crisis. It is also useful for
understanding the transmission mechanism of unconventional monetary policy.
The approach we take involves conducting counterfactual analysis, to assess what would have
happened had QE not been undertaken, which we then compare with a baseline prediction which
includes QE. Our analysis is based on three models. We use a large BVAR, estimated over rolling
Working Paper No. 443 January 2012 5
windows, to allow for structural change; an MS-SVAR, where parameters are allowed to change
at a particular time in order to capture regime changes; and a TVP-SVAR, which allows us to
assess general time variation in parameters. The BVAR places more weight on past patterns in
the data, by incorporating a large data set and the minimum amount of economic structure. Such
models have been found to be useful because they allow the analysis of complex
interrelationships between a large set of economic data, which in our case involves the
interconnections between interest rate spreads and the real economy. The MS-SVAR and the
TVP-SVAR employ a small data set but they allow us to incorporate a more sophisticated
treatment of structural change. The underlying economic or structural shocks in these models are
identified through restrictions on the impulse responses (see, for example, Baumeister and Benati
(2010)).
We use each of the models to conduct counterfactual analysis of the effects of QE. This exercise
relies on the empirical evidence in Joyce et al (2011), which suggests that QE reduced medium to
long-term government bond yields by about 100 basis points. To produce counterfactual
forecasts, we therefore assume that without QE gilt yields would have been 100 basis points
higher, ceteris paribus. For the purpose of the counterfactual, we also assume that the effects of
QE come solely through lower long-term government bond yield spreads. We implement this
effect on yields by adjusting the spread between the relevant long-maturity gilt yield in each
model and the three-month Treasury bill rate (henceforth the government bond spread). The link
between government bond spreads and macroeconomic variables is given a structural
interpretation in, for example, Estrella (2005). One caveat here is that our models do not allow us
to discriminate between the effects of movements in bond spreads that come through term premia
and those that come through expected future policy rates. So to the extent that QE effects on
spreads come mainly through term premia (as much of the literature suggests - see Section 3),
and this has different macroeconomic effects to spread movements caused by future policy rate
expectations, this will not be captured in our analysis.
Our multiple models strategy is similar in spirit to the approach adopted by Chung, Laforte,
Reifschneider and Williams (2011) in their analysis of the incidence of the ZLB interest rate
policy environment (though their paper only uses one model in its analysis of the Federal
Reserve’s LSAP programmes). Bridges and Thomas (2012) also use a number of monetary
models to estimate the effect of the Bank of England asset purchases on the level of GDP and
Working Paper No. 443 January 2012 6
CPI inflation. The use of different models that vary in their emphasis on data versus economic
structure increases our faith in the likely robustness of our conclusions. Our analysis
encompasses existing time-series models in the literature on the effects of unconventional
monetary policy (see for example, Joyce et al (2011), Lenza, Pill and Reichlin (2010) and
Baumeister and Benati (2010)) and extends this literature by including models that account for
structural change.
Results from the counterfactual analysis of the effects of QE using the large BVAR model
suggests that without QE there would have been larger declines in real GDP during 2009 and CPI
inflation would have been low or even negative. The QE policy was therefore effective in helping
the UK economy avoid a deeper recession and deflation. The MS-SVAR and TVP-SVAR models
provide similar evidence, if anything suggesting that QE had even larger effects on output and
inflation.
The rest of the paper is structured as follows. Section 2 discusses the United Kingdom’s
experience with QE and Section 3 reviews some of the related literature on the effects of QE and
other large-scale asset purchases on financial and macro variables. Our econometric framework
is described in Section 4, the data are described in Section 5 and the counterfactual assumptions
we use in our analysis are discussed in Section 6. Section 7 presents empirical results for each of
the models. Section 8 provides a summary of the key results and Section 9 concludes.
2 Quantitative easing in the United Kingdom
Large-scale asset purchases in the United Kingdom were a culmination of a package of measures
designed to address the consequences of the financial crisis.1 These measures included the
provision of enhanced liquidity support, measures to enhance market functioning and QE or
large-scale asset purchases (see Bean (2011)). The provision of liquidity support was centred on
the £185 billion Special Liquidity Scheme introduced in April 2008, which allowed banks to
swap mortgage-backed securities and other illiquid assets for Treasury bills. A Discount Window
Facility was also introduced to meet the short-term liquidity needs of financial institutions
requiring assistance. In addition, there was the assurance that the Bank of England was ready to
1Aı̈t-Sahalia, Andritzky, Jobst, Nowak and Tamirisa (2009) and Lenza et al (2010), amongst others, provide a review of the various measures used by major central banks in response to the great financial crisis.
Working Paper No. 443 January 2012 7
offer emergency liquidity support at a penalty rate and against a broader range of collateral to
otherwise solvent financial institutions that were experiencing liquidity problems. To address
market functioning, an Asset Purchase Facility was created to allow the Bank of England to
purchase high-quality commercial paper and sterling investment-grade corporate bonds. Before
the QE policy was introduced, these purchases were financed by the issuance of Treasury bills
and the cash management operations of the Debt Management Office. Like the offer of
emergency liquidity support, the knowledge that the central bank was now in the market for these
assets may have improved overall market functioning.
The QE policy was first announced in March 2009 and it involved the Bank of England buying
assets, mainly UK government bonds (gilts), financed by the issuance of central bank money.
The effect of these purchases was to reduce gilt yields and to stimulate demand through a number
of channels. In normal times, reducing Bank Rate would be the policy chosen to address demand
shocks. However with Bank Rate at its effective lower bound, the Bank of England’s MPC felt
that it had to use unconventional methods to ease monetary conditions further. The initial MPC
decision was for the Bank to make £75 billion of asset purchases. This was extended
subsequently to £125 billion in May 2009, to £175 billion in August 2009 and to £200 billion in
November 2009, with the purchases completed at the end of January 2010. This represented
about 14% of annual UK GDP.
Although there are a number of possible channels through which QE may affect the wider
economy (see discussion in eg Benford, Berry, Nikolov and Young (2009)), most analysis has
emphasised the so-called portfolio balance channel. This mechanism operates through QE
purchases bidding up the prices of gilts and other assets that are more substitutable for gilts than
money and this in turn stimulates demand through lower borrowing costs and wealth effects.
Portfolio balance models as described by Tobin (1969), among others, were used by Joyce et al
(2011) to determine the financial market impact of QE. They find that the predictions of these
models are broadly consistent with the event study evidence for the United Kingdom. We discuss
this and other empirical evidence in the next section.
Working Paper No. 443 January 2012 8
3 Related literature
Most of the literature on the effects of QE and the use of other unconventional monetary
instruments has focused on financial market variables, as opposed to the effects on real activity or
inflation. This is primarily due to the difficulty of identifying the appropriate counterfactual. In
this section, we summarise the literature on the effects of QE or LSAPs on financial and real
variables, both in the United Kingdom and in other countries.
The assessment of the effects of non-standard monetary policies on financial variables has
mainly relied on event study methods. Bernanke, Reinhart and Sack (2004), for example, provide
a comprehensive analysis of financial market reactions to various non-standard Fed policy
announcements that altered the relative supply of US Treasury securities. They conclude that
both changes in relative asset quantities and the expectation of such changes have had an impact
on yields or asset returns. These results are supported by VAR-based term structure models.
Bernanke et al (2004) also provide some evidence that QE as implemented by the Bank of Japan
(providing excess reserves to maintain the interest rate at zero and open market purchases of
government bonds) may have generated lower yields over the QE period, although there is
weaker support from event studies compared with those for the United States.2
Gagnon, Raskin, Remache and Sack (2011) provide an assessment of the first round of LSAPs
conducted by the Fed in the wake of the great financial crisis (commonly referred to as LSAP1).
On the basis of event studies of LSAP announcements, they suggest there was a contraction in
Treasury yields and yields on mortgage-backed securities (MBS) of about 90 and 110 basis
points respectively. They suggest that the decline in long-term interest rates largely reflected the
fall in risk premia generated by these purchases, mainly through the reduction of duration risk.
They also use a time-series econometric model of asset quantities estimated on the basis of
pre-crisis data to determine the impact of LSAPs, which suggests slightly smaller effects. Using
a different approach based on panel data analysis of individual bonds, D’Amico and King (2010)
find that LSAP1 had an effect on longer-term Treasury yields of about 30 basis points for the
5-year to 15-year sector. Krishnamurthy and Vissing-Jorgensen (2011) examine both LSAP1 and
the second round of Fed purchases (LSAP2) using an event study approach. They find evidence
of a large decline in interest rates in the first episode, but not the second (though this may reflect
2A comprehensive review of the financial and macroeconomic effects of QE in Japan is provided by Ugai (2007).
Working Paper No. 443 January 2012 9
the fact that the markets had already priced in much of the expected impact before the second
programme was announced). They identify a number of different channels through which QE
may work, such as duration, liquidity and the long-term safety channel. Swanson (2011) revisits
the Operation Twist experiment of the 1960s using event study techniques and argues that it was
broadly comparable in scale to LSAP2. He finds that both policies reduced longer-term Treasury
yields by around 15 basis points.3
The United Kingdom’s experience with QE in the recent financial crisis has been documented in
a number of studies. Meier (2009), Dale (2010), Joyce et al (2011) and Bean, Paustian, Penalver
and Taylor (2010), among others, have discussed the operational details of large-scale asset
purchases by the Bank of England and analysed various aspects of the impact of these
unconventional monetary measures. Meier (2009) used an event studies approach to assess the
impact of QE announcements and suggests long-term government bond yields declined between
40 and 100 basis points following the initial QE announcement by the Bank of England in March
2009. Joyce et al (2011) provide a more comprehensive assessment using event studies and
portfolio balance models. In this framework, it is assumed that gilts and money are imperfectly
substitutable assets and a multiplier calculated from a Markowitz-Tobin portfolio choice-type
model (see for example, Markowitz (1952)) determines the effects of changes in the quantity of
gilts on excess asset returns in a portfolio with money, equities, corporate bonds and gilts.4 They
suggest that QE lowered long-term gilt yields by about 100 basis points and that most of the
decline was generated by portfolio balance effects.
There are far fewer studies that try to estimate the macroeconomic effects of unconventional
monetary policy measures. One of the first in the current crisis was by Lenza et al (2010), who
conduct a comprehensive review of the European Central Bank’s use of non-standard monetary
instruments in response to the crisis. The ECB embarked on an ‘enhanced credit support’
programme (see, for example, Trichet (2009)), focused on market liquidity, from mid-2009 to
mid-2010 in addition to a multitude of other measures intended to enhance market functioning
introduced at the onset of the crisis. Lenza et al (2010) provide evidence, based on a
counterfactual analysis using a large BVAR model, that these measures were successful in
3Other supportive evidence on the effects of the Fed’s LSAPs programme is provided by Hamilton and Wu (2011) and Doh (2010). 4Others have also used portfolio balance models to estimate the impact of LSAPs. See, for example, Kimura and Small (2006) who suggested that QE in Japan had some positive portfolio balance effects and reduced risk premia on some assets. Neely (2010) used a portfolio balance model to examine the international effects of US LSAPs.
Working Paper No. 443 January 2012 10
reducing financial market dysfunction given the noticeable contraction in money market spreads.
They also find that these measures had a positive effect on output and inflation but with a lag.
Another VAR-based study by Baumeister and Benati (2010) provides evidence of a significant
macroeconomic impact in the United States, United Kingdom and the euro area due to the
observed decrease in long-term bond spreads following asset purchases, though the magnitudes
of the effects output seem extremely large.
The impact of the Fed’s LSAPs on the US macroeconomy is also covered in Chung et al (2011),
who find that the first LSAPs were successful. In particular, simulations from the Fed’s FRB/US
macroeconomic model suggest that asset purchases prevented deflation in the United States and
reduced the rate of unemployment. The authors suggest that the boost to the level of real GDP
was about 3%, inflation was 1% higher and that the unemployment rate was reduced by1.5
percentage points compared with what it would otherwise have been.
The theoretical underpinnings for expecting changes in asset quantities to affect yields are
provided in Vayanos and Vila (2009), who develop a model based on investors with
preferred-habitats (Greenwood and Vayanos (2008) offer empirical evidence in support of the
model’s predictions).5 But in most conventional New Keynesian models QE has no wider
economic effects, unless it changes agents’ expectations about the future path of interest rates
through the signalling channel. Eggertsson and Woodford (2003) argue that there are no portfolio
balance effects in these models because the reduction in private sector portfolio risks resulting
from central bank asset purchases is offset by a corresponding increase in the riskiness of public
sector portfolio due to the inherent uncertainty of future taxes and spending, making QE
purchases irrelevant through this channel. But the literature incorporating the use of
unconventional monetary policies into theoretical macroeconomic models is steadily evolving. In
more recent work, Curdia and Woodford (2009) suggest that there can be some role for credit
easing, which involves changing the composition of assets on a central bank’s balance sheet but
not for QE, which would still be ineffective at the ZLB.6 But, when financial frictions or
incomplete markets are coupled with imperfect asset substitutability, changing the maturity
5Analysis of the effects of altering the maturity structure of government debt is not new. Informal analysis of the preferred-habitat theory and empirical evidence on debt maturity structure are available in, for example, Modigliani and Sutch (1966, 1967). 6Christiano and Ikeda (2011) also consider the role of credit easing using theoretical models with financial frictions. ‘Credit easing’ in the United States is described as the Fed’s purchases of mortgage-backed securities, which changed the composition of assets on the Fed’s balance sheet.
Working Paper No. 443 January 2012 11
structure of assets can also affect asset prices. A useful starting point is the inclusion of Tobin’s
idea of imperfect asset substitutability in standard New Keynesian models. For example, Andrés,
López-Salido and Nelson (2004) and Harrison (2012) develop microfoundations for
preferred-habitats and portfolio balance effects which is supportive of a role for QE within a
dynamic stochastic general equilibrium (DSGE) framework. In general, to explain the
macroeconomic effects of QE and other unconventional monetary policies fully, the (modified)
DSGE model must capture the frictions that generate interest rate spreads and linkages between
interest rate spreads and the real economy. An insightful overview of related issues in this
emerging literature is found in, for example, Christiano (2011).
4 Econometric framework
In this section we describe the econometric models used in the paper.
4.1 Bayesian VAR (BVAR)
The seminal work by Sims (1980) introduced the use of vector autoregressions (VAR) into
macroeconometric modelling and VAR models continue to occupy centre stage. In this paper we
use Bayesian methods to estimate them. Specifically, we estimate a large BVAR model similar to
the model employed by Lenza et al (2010). As our analysis involves a large data set, BVAR
models are useful to overcome parametrisation problems which would otherwise be encountered
when a standard VAR is estimated in large dimensions. The BVAR model allows us to use a
priori information to restrict the parameter space. Our approach of applying prior information to
a standard VAR model can be motivated from both a Bayesian and a classical perspective. We
view the use of Bayesian technology as desirable mainly on pragmatic rather than philosophical
grounds.
4.1.1 Notation and preliminaries
The model belongs to the general class of BVAR models for large data sets.7 Assuming that all
the variables in the large data set are in the vector Yt , we can write the model as:
Yt =Θ0+Θ1Yt−1+ · ·⋅+ΘpYt−p+ et (1)
7See, for example, Banbura, Giannone and Reichlin (2010).
Working Paper No. 443 January 2012 12
where et is a vector white-noise error term,Θ0is a vector of constants andΘ1toΘpare
parameter matrices.
4.1.2 A normal-inverted Wishart AR(1) prior
As will be discussed later, our large data set comprises macroeconomic and financial market
variables. A good prior for BVAR models of the macroeconomy is a simple random walk
forecast; see, for example, Litterman (1986). Many macroeconomic and financial market
variables are characterised by persistent processes. In general, simple autoregressive (AR) or
random walk (RW ) models are known to produce reasonable forecasts for macroeconomic and
financial variables (over short horizons). We therefore choose a univariate AR(1) process with
high persistence as our prior for each of the variables in the BVAR model. With this prior, the
‘own’ first lag is considered to be the most important in every equation in the BVAR.
Specifically, the expected value of the matrixΘ1isE[Θ1]=0.99×I. We assume thatΘ1is
conditionally (onΣ)normal, with first and second moments given by:
E[Θ(ij) 1 ] =
0.99if i = j
0 if i 6= j,Var[Θ(ij)
1 ] =φσ2 i/σ
2 j,(2)
whereΘ(i j) 1 denotes the element in position(i,j) in the matrixΘ1,and where the covariances
among the coefficients inΘ1are zero. The shrinkage parameterφdetermines the tightness of the
prior or the extent to which the data influences the estimates. With a tight prior the data has little
or no influence on the estimates asφ→0. For a loose prior, whereφ→∞there is an increasing
role for the data and the estimates then converge to the standard OLS estimates. To complete the
specification of our BVAR prior, we assume that the constant,Θ0,has a diffuse normal prior and
the matrix of disturbances have an inverted Wishart prior,Σ∼iW(v0,S0).v0 and S0 are the prior
scale and shape parameters with the expectation ofΣequal to a fixed diagonal residual variance
E[Σ]=diag(σ21,...,σ
2 N) . This is a conjugate prior with a normal-inverted Wishart posterior
distribution. The BVAR model is estimated using rolling windows to account for structural
change. Additional technical information on model estimation and prior tightness is provided in
Appendix A.
Working Paper No. 443 January 2012 13
4.2 Change-point SVAR (MS-SVAR)
Our consideration of regime changes is motivated by the fact that since the early 1970s the UK
monetary policy regime has changed a number of times. Since how agents form their
expectations will have changed under different monetary policy reaction functions,
macroeconomic dynamics over this period cannot be easily described by deep parameters of a
single structural model. Since the collapse of the Bretton Woods system in the early 1970s, we
might loosely identify four successive monetary policy regimes in the United Kingdom. These
are monetary targeting (not explicitly introduced until 1979 but monetary aggregates were
monitored from the mid-1970s), an exchange rate targeting regime in the mid-1980s, inflation
targeting after 1992 and more recently the use of unconventional monetary policy instruments
and inflation targeting in a ZLB environment.8 The use of four different structural models might
help us to understand agents’ actions inside these regimes, but it would not be able to capture
agents’ expectations that the policy regime might change in the future.
The following MS-SVAR model allows us to model (in a reduced-form manner) changes in the
policymaker’s reaction function and to study how aggregate dynamics have been affected.
Yt = cS + K
### ∑
j=1
Bj,SYt−j+A0,Sεt(3)
where the data vector Yt contains monthly data on the 3-month Treasury bill (Rt), the 10-year
government bond yield spread (St) (defined as the 10-year government bond yield minus the
3-month Treasury bill rate), annual GDP growth (yt), annual CPI inflation(πt),annual M4
growth (Mt), and the annual change in stock prices (SPt); Bj,SandA0,Sare regime dependent
autoregressive coefficients and structural shock loading matrices respectively.
As explained in Chib (1998), the dates of (say, M) regime breaks in the model are unknown and
they are modelled via the latent state variable S, which is assumed to follow an (M-state)
8The Bank of England was given operational independence for monetary policy in 1997. However, the United Kingdom has had an inflation target since late 1992 and the Bank held joint meetings with the Treasury ahead of policy decisions by the Chancellor of the Exchequer.
Working Paper No. 443 January 2012 14
Markov-chain process with restricted transition probabilities pi j = p(St = j|St−1 = i) given by
pi j>0 if i = j (4)
pi j>0 if j = i+1
pMM = 1
pi j = 0 otherwise.
For example, if M = 4 the transition matrix is defined as
P̃ =
 p11 0 0 0
1− p11 p22 0 0
0 1− p22 p33 0
0 0 1− p33 1

Equations (3) and (4) define a Markov-switching VAR with non-recurrent states where
transitions are allowed in a sequential manner. For example, to move from Regime 1 to Regime
3, the process has to visit Regime 2. Similarly, transitions to past regimes are not allowed. This
imposed structure (which is not necessarily more restrictive than a standard Markov-switching
model) implies that any new regimes are given a new label (rather than being explicitly linked to
past states as in a standard Markov-switching model) and this allows us to isolate periods of
interest (such as the current period) and tailor our shock identification scheme accordingly.
4.2.1 Identification of structural shocks
In this model we identify four structural shocks: a monetary policy shock, a demand shock, a
supply shock and a shock to the yield spread. Following Baumeister and Benati (2010), these
shocks are identified using a combination of sign and zero type restrictions; see Table A.
We impose standard sign restrictions for the monetary policy, demand and supply shocks. A
positive monetary policy shock, which increases the short-term rate, will lead to a compression in
the yield spread, lower GDP growth rate and lower inflation. A positive demand shock will lead
to higher inflation and output, short-term interest rates, money growth and stock prices; while a
negative supply shock will lead to higher inflation and lower output growth. On the other hand, a
Working Paper No. 443 January 2012 15
Table A: Sign restrictions in the MS-SVAR model
Shocks \ Variables Rt St YtπtMt SPt
Monetary policy≥≤≤≤? ? Spread 0≥≤≤? ? Demand≥?≥≥≥≥Supply ? ?≤≥? ?
Note: For variable definitions see discussion of equation (3).
negative shock to the yield spread is assumed to have zero contemporaneous impact on the
short-term interest rate, but leads to lower inflation and output growth.
The MS-SVAR not only accounts for different policy regimes but we are also able to examine the
effects of the policymaker’s inability to change the interest rates in order to stimulate demand, as
under the ZLB. We only do this in the most recent regime by imposing the prior assumption that
the policy rate does not depend on other lagged endogenous variables. We show below that our
benchmark model estimate of Regime 4 roughly coincides with the 2007-09 financial crisis
(Chart 1).
4.3 Time-varying parameter SVAR (TVP-SVAR)
Another model that captures policy regime changes is the following TVP-SVAR:
Yt = ct + L
### ∑
l=1
φl,tYt−l+ vt (5)
where Yt contains quarterly data on the 3-month Treasury bill (Rt), the 10-year government bond
yield spread (St) (defined as the 10-year government bond yield minus the 3-month Treasury bill
rate), annual GDP growth (yt) and annual CPI inflation(πt).
The law of motion for the coefficients is given by:
φ~​l,t=φ~​l,t−1+ηt. (6)
whereφ~​l,t= {ct$,φl,t}. $As in Cogley and Sargent (2005), the covariance matrix of the innovations
vt is factored as
E(vtv′t)≡Ωt= A−1 t Ht(A−1
t )′. (7)
Working Paper No. 443 January 2012 16
The time-varying matrices Ht and At are defined as:
Ht≡
h1,t0 0 0
0h2,t0 0
0 0h3,t0
0 0 0h4,t
 At≡
 1 0 0 0
α21,t1 0 0
α31,tα32,t1 0
α41,tα42,tα43,t1
 (8)
with thehi,tevolving as geometric random walks,
lnhi,t=lnhi,t−1+ν~t.
Following Primiceri (2005), we postulate the non-zero and non-one elements of the matrix At to
evolve as driftless random walks,
αt=αt−1+τt, (9)
We assume the vector [v′t,η′t,τ′t,ν~′ t ] ′ to be distributed as
vt
ηt
τt
ν~t
∼N(0,V) , with V =
 Ωt 0 0 0
0 Q 0 0
0 0 S 0
0 0 0 G
 and G =
σ2
1 0 0 0
0σ22 0 0
0 0σ23 0
0 0 0σ24
 . (10)
The TVP-SVAR model can be written compactly as
Yt = x′tB̃t+A0,tεt(11)
where xt =I⊗[1,Yt−1,Yt−2,...], B̃t = vec ( [ct,φ1,t,φ2,t...]
) , E(εtε
′ t) =I,A0,t= A−1
tH1/2t P, where P
is an othonormal matrix (PP′ = I) that satisfies the zero-sign restrictions shown in Table B.
This model is substantially more flexible than the one discussed in the previous section. It is not
only consistent with variation in the policy rule, but also with deviations from the rational
expectations hypothesis. In this framework agents do not know the structural parameters and
they use simple forecasting models to form their projections about future variables and,
consequently, learn about the structure of the economy. This model seems very plausible during
crisis periods where agents have no idea how shocks have changed the structure of the economy
and they use simple ‘rules of thumb’ to learn about the new state. During the financial crisis
policymakers had to employ non-standard policy tools and, arguably, it makes sense for agents to
Working Paper No. 443 January 2012 17
‘abandon’ the rational expectation hypothesis and use simple forecasting rules to learn about the
structure of the economy; at least for a short period. If agents behave this way we need to allow
the parameters to vary over time as in the TVP-SVAR model to assess the effects of QE.
4.3.1 Identification of structural shocks
The shock identification scheme used for this model is identical to the one discussed in Section
4.2.1. The only difference is that two sets of restrictions have been dropped (those associated
with the M4 and Stock Prices series) because the dimension of the VAR in this case has been
reduced from six to four variables for reasons of tractability. Table B reports these restrictions.
Table B: Sign restrictions in the TVP-SVAR model
Shocks \ Variables Rt St Ytπt
Monetary policy shock≥≤≤≤Spread shock 0≥≤≤Demand shock≥?≥≥Supply shock ? ?≤≥
Note: For variable definitions see discussion of equation (5).
5 Data
Our data set for the large BVAR comprises 43 variables, with monthly observations covering
April 1993 to September 2010. UK variables include those capturing real activity, prices, money,
the yield curve and financial markets.9 Given that QE is expected to affect monetary aggregates
and interest rates directly, the bulk of the domestic variables are interest rates, interest rate
spreads and monetary aggregates. To incorporate potential international financial and economic
linkages, we also include data for real activity, prices and the policy rates for the United States
and the euro area. We use log-levels for the variables except those which are already in growth
rates. The list of variables are provided in Appendix D.
The SVAR models were estimated using monthly and quarterly data on a smaller set of variables
covering a longer period, from 1963 to 2011. The MS-SVAR uses monthly data, from February
9We obtain monthly GDP estimates from the National Institute of Economic and Social Research. These estimates are obtained from statistical projection and involve a fair amount of interpolation. Mitchell, Smith, Weale, Wright and Salazar (2005) discuss the methodology in detail.
Working Paper No. 443 January 2012 18
1963 to March 2011, for the 3-month Treasury bill rate, the 10-year government bond yield
spread (defined as the 10-year government bond yield minus the 3-month Treasury bill),
annualised GDP growth, annualised CPI inflation, annualised M4 growth, and the annual change
in the FTSE All-Share index (stock prices). For the TVP-SVAR model we use quarterly data,
from 1968 Q1 to 2011 Q1,10 for the 3-month Treasury bill rate, the 10-year government bond
yield spread (defined as the 10-year government bond yield minus the 3-month Treasury bill
rate), annualised GDP growth and annualised CPI inflation.
6 Counterfactual assumptions
Our counterfactual analysis is based on the empirical findings in Joyce et al (2011) which
suggest that QE may have depressed medium to long-term government bond yields (average
5-year to 25-year spot rates) by about 100 basis points. We implement this impact on yields by
changing the government bond spread, the spread between the relevant long-maturity bond yield
in each model and the three-month Treasury bill rate. The resulting counterfactual simulations
are conditional forecasts for real GDP and CPI inflation. We examine two scenarios: a policy
scenario and a no policy scenario.
Under the policy scenario, which we describe as our baseline model prediction, we produce a
counterfactual forecast taking the actual levels of long-term government bond spreads and Bank
Rate that were observed from March 2009 to the end of our forecast horizon as our conditioning
assumptions. We do not take the outturns for real GDP and CPI inflation as our baseline because
the changes in these variables may also be due to changes in other factors that are not captured in
the model. This means that we are only identifying the assumed impact of QE on the growth and
inflation profiles, and disregarding all the other forces pushing up on demand. Consequently, the
actual recovery may be higher than our model prediction, which does not capture these shocks.
For the no policy scenario, we assume that long-term government bond spreads would have been
100 basis points higher over the period from March 2009 onwards had QE not been
implemented.11 We also consider an alternative no policy scenario, where we adjust government
10These data actually start from 1958 Q1, but we have used the first 10 years as a training sample to calibrate the priors. 11This type of conditioning assumption is similar to the ‘hard conditions’ discussed in Waggoner and Zha (1999).
Working Paper No. 443 January 2012 19
bond spreads by 100 basis points and fix Bank Rate at0.5We describe the two no policy
scenarios as Bank Rate endogenous and Bank Rate exogenous.
To approximate the macroeconomic impact of QE, we compare the conditional forecasts for real
GDP and CPI inflation under the policy scenario with those for the no policy scenario and take
the difference between the two as our estimate. We are therefore using the change in the slope of
the yield curve as our sole metric to determine the effects of QE on the macroeconomy. Lenza
et al (2010) and Baumeister and Benati (2010) use a similar approach to examine the effects of
unconventional monetary policy on the macroeconomy. We do not examine the effects of other
QE transmission channels. Implicit in our approach is the assumption that QE operates through
expectations and that markets price in the total amount of asset purchases expected by the MPC.
As noted, £75 billion of asset purchases were announced in March 2009, and this was extended
to £125 billion in May 2009, to £175 billion in August 2009 and to £200 billion in November
2009. But evidence from event study analysis suggests that by far the largest reaction in gilt
yields occured around March 2009 (see Joyce et al (2011)).
In the BVAR model, we focus on the 5-year and 10-year government bond yield spreads to assess
the potential macroeconomic effects of QE, so the adjustments for the no QE counterfactual are
applied to these spreads. For the smaller SVAR models, we apply the spread adjustment to the
10-year government bond spread.
7 Empirical results
7.1 Results from BVAR model
We set the lag order for our large BVAR model equal to one. For a model of this size, standard
information criteria are difficult to use, so we rely on serial correlation tests on the residuals to
arrive at the lag order. The residuals seemed to be well behaved, with little evidence of residual
serial correlation. We set the tightness parameter following the approach used in Lenza et al
(2010). So the tightness parameter for the reported results ensures that the standard deviation of
the residuals of the Bank Rate equation in the large BVAR is equivalent to those for the Bank
Rate equation in a ‘small’ VAR. We choose 12 variables for the ‘small’ VAR, including both UK
variables and foreign variables, to mimic the dynamics of a central bank monetary policy rule.
Working Paper No. 443 January 2012 20
The ‘small VAR’ is therefore used to pin down the prior for the BVAR.
We estimate the model using a rolling estimation approach and only use data from August 2007
to September 2010 to conduct our counterfactual analysis. For these simulations, we assume that
under the two no policy scenarios the 100 basis point increase in long-term government bond
yields (which is implemented through a rise in the 5 and 10-year gilt yield spread to the 3-month
Treasury bill rate) occurs in the initial period and yields remain at 100 basis points higher over
the forecast horizon. We also conduct some sensitivity analysis by looking at the effects of a 80
basis point and a 120 basis point increase in spreads under the no policy scenario. We also vary
the persistence of the QE shock by allowing the size of the adjustment on government bond
spreads to vary over the forecast horizon.
Chart 2 illustrates the estimated effects of QE on real GDP and inflation using the Bank Rate
endogenous scenario (first column) and the Bank Rate exogenous scenario (second column). As
with any VAR model, the forecasts become less informative as the forecast horizon lengthens,
since our focus is on the effects of QE, the counterfactual forecasts for GDP and CPI inflation are
shown for the period that they lie below the baseline forecast which is typically around a year.
From the results it appears that the decrease in long-term government bond spreads supported the
level of real GDP during 2009 and prevented CPI inflation from becoming very low or negative.
From Chart 2 (first column), the Bank Rate endogenous scenario, leads to a maximum decrease
of real GDP of about0.7in September 2009. In the Bank Rate exogenous scenario (Chart 2,
second column), we observe a maximum fall of about0.3in the level real GDP in November
2009. The effects of QE on output are therefore more pronounced in the Bank Rate endogenous
scenario compared to the Bank Rate exogenous scenario. This result is somewhat puzzling, as we
would expect to see a larger effect in the case where the Bank Rate is fixed. This is perhaps a
consequence of the fact that BVAR imposes little economic structure on the data. The effects on
inflation are very similar across the two scenarios, however, with QE having a maximum effect of
about 1 percentage point on CPI inflation. The peak impact occurs in March 2010 for both
scenarios. So our evidence for the effects of QE on real GDP would suggest that the maximum
effect occurs after about 6 to 9 months, while the maximum effect on inflation occurs after about
a year.
Working Paper No. 443 January 2012 21
These are the maximum effects of QE. As noted previously, these are estimated by comparing the
no policy scenario with the policy scenario which is a forecast conditional on the actual paths of
the relevant interest rate spreads and the actual path for Bank Rate over the forecast horizon. The
effects would be larger if the counterfactual were defined as the no policy scenario relative to the
actual data, as the model underpredicts output and inflation over the period.
We also considered a number of other adjustments for the no policy scenario, as shown in Table
C. This included examining the effects of larger and smaller changes in spreads, but since the
shock is linear in the spreads the effects are simply proportional to the 100 basis point
adjustment. To assess the persistence of the shock we considered an alternative adjustment
profile for sensitivity analysis, which we call less persistence in Chart 2. In this case, instead of
assuming the effects on the government bond spread are constant, we assume that without QE
there would have been a 60 basis point increase in spreads in the first three months, a 100 basis
point increase for the next seven months and then a gradual decline of about 11 basis points each
month over the rest of the horizon.12 Unsurprisingly this resulted in slightly smaller effects. But,
overall, the results under these various alternative spread adjustment profiles were broadly
similar to our central case.13
Table C: Maximum effects of QE: large BVAR
CPI Inflation Real GDP Level Adjustment \ Estimate BR endogenous BR exogenous BR endogenous BR exogenous 80bp 0.82pp 0.85pp 0.61% 0.23% 100bp 1.03pp 1.07pp 0.72% 0.28% 120bp 1.24pp 1.28pp 0.83% 0.34% Less persistence 0.96pp 0.94pp 0.65% 0.26%
Note: BR is abbreviation for Bank Rate. The BR endogenous scenario is the forecast conditional on only the adjusted government bond spreads. The BR exogenous scenario is the forecast conditional on the adjusted government bond spreads and Bank Rate.
12In subsequent months after the seven months increase of 100 basis points, the increase in spreads will be equivalent to a decline of about 6% in the previous month’s increase in spreads. For example, the increase in spreads in the 11th month is equivalent to 100 basis points minus 100*1/9. These types of conditioning assumptions are similar to the ‘soft conditions’ described in Waggoner and Zha (1999). 13In addition, we also tried combining changes in yields with shocks to the money stock, with the aim of combining quantity and asset price effects. This is consistent with a standard portfolio balance approach, see Joyce et al (2011). These results proved very sensitive to which monetary aggregate we assumed was affected by QE and they are not reported here. Further analysis of the effects of QE using a monetary approach are provided in another Bank of England Working Paper by Bridges and Thomas (2012).
Working Paper No. 443 January 2012 22
7.2 Results from MS-SVAR model
For this model, the number of the regimes is decided before the model is estimated. This
selection can be based on data-driven techniques - such as the marginal likelihood criterion (see
Chib (1998)) - or, as in this case, by prior knowledge. As noted previously, Chart 1 shows the
estimated regime pattern. We listed four monetary policy regimes in the post-Bretton Woods era
in Section 4.2. The first regime identified by the model ended in the early 1980s, which, although
covering a period when different regimes may have operated, roughly coincides with the end of
monetary targeting in the United Kingdom. The second regime ended in the early 1990s, a period
when the United Kingdom left the Exchange Rate Mechanism and started inflation targeting. The
end of the third regime is around the outset of the recent financial crisis.
7.2.1 Counterfactual scenario by imposing alternative spread paths
This exercise is identical to the exercise in Section 7.1. Chart 3 plots the results from this
experiment, where we focus on the effects of QE over the period until the no policy conditional
forecasts return to the baseline. Similarly, the outcomes are grouped into two categories: Bank
Rate endogenous and Bank Rate exogenous. The Bank Rate endogenous estimate (first column
of Chart 3) is the forecast for output growth and CPI inflation conditional on the adjusted
government bond spread, under the no policy scenario. For the Bank Rate exogenous estimate,
the forecast is conditional on the adjusted government bond spread and 3-month Treasury bill
rate (the proxy for Bank Rate in this model) fixed at0.5over the entire forecast period (second
column).
Table D reports the peak effects on GDP growth and CPI inflation from these simulations. For a
100 basis point contraction in spreads, the maximum impact on inflation and GDP growth occurs
in April 2009 using the Bank Rate endogenous estimate and in March 2010 for the Bank Rate
exogenous estimate. The large initial impact of the stimulus, using the Bank Rate endogenous
estimate, occurs because in subsequent periods the unconstrained policy rate declines in response
to lower inflation and output. The results for the less persistent case suggest that a staggered
impact on spreads produces smaller effects compared with the standard case, where we assume
there is a 100 basis point increase in every period over the forecast horizon, especially for the
case where Bank Rate is treated as endogenous. The MS-SVAR suggests that if we assumed the
Working Paper No. 443 January 2012 23
effects of QE on spreads were less persistent, the impact on output growth and CPI inflation
would be smaller. These effects are more marked than in the case of the BVAR.
Table D: Maximum effects of QE: MS-SVAR
CPI Inflation GDP growth Adjustment \ Estimate BR endogenous BR exogenous BR endogenous BR exogenous 80bp 1.03pp 3.01pp 2.14pp 3.68pp 100bp 1.31pp 3.38pp 2.72pp 4.08pp 120bp 1.59pp 3.79pp 3.29pp 4.45pp Less persistence 0.75pp 3.11pp 1.57pp 3.96pp
Note: BR is abbreviation for Bank Rate. The BR endogenous scenario is the forecast conditional on only the adjusted government bond spreads. The BR exogenous scenario is the forecast conditional on the adjusted government bond spreads and Bank Rate.
In the scenario where Bank Rate is exogenous, the effects on output and inflation are larger and
inflation would have gone into negative territory. This means that without an additional policy
instrument to affect expectations about demand, the economy would suffer from deflation and
positive real interest rates which would depress demand even further (people expect inflation to
fall, meaning consumption and investment goods are going to be cheaper in the future and,
therefore, they postpone consumption and investment into the future). Uncertainty about states of
the world is another mechanism that can squeeze demand. For instance, in periods of major
financial crises, agents are particularly uncertain about the future and, in order to offset high
consumption variations (due to, say, the possibility of being unemployed) or/and to avoid big
capital losses (from firms going bust), they increase their precautionary saving, which squeezes
current demand.
7.2.2 Impulse responses from MS-SVAR model
The structural identification scheme allows us to examine the evolution of the variables in the
different regimes following a particular shock. Focusing on the responses after a shock to
government bond spreads (the ‘spread’ shock), Chart 4 shows that this shock has significantly
larger effects in the recent regime. For example, the effect of the shock (a 100 basis point
decrease in spreads) on GDP growth increases from about0.6in Regime 3 to about 2% in
Regime 4.14
14The responses have been normalised to make them comparable across different regimes.
Working Paper No. 443 January 2012 24
7.3 Results from TVP-SVAR model
7.3.1 Counterfactual scenario by imposing alternative spread paths
Chart 5 and Table E show the results from the TVP-SVAR model. We focus on the effects of QE
over the period until the no policy conditional forecasts return to the baseline. For a 100 basis
point contraction in spreads, the maximum effects on inflation and output growth occur in 2009
Q4 for the Bank Rate endogenous scenario and in 2010 Q1 for the Bank Rate exogenous
scenario, ie three to four quarters after the start of QE. However, the model prediction is hugely
pessimistic relative to the data outturns. The poor forecasting power of the TVP-SVAR may be
due to how agents learn about the evolution or structure of the economy. For example, if we
consider the TVP-SVAR as the reduced-form version of a structural model where agents use
simple forecasting rules to learn about the structure of the economy, then the results from these
conditional forecasts would suggest that the agents in this model learn very slowly.15 Since the
initial point of the forecast is in a downturn, agents seem to remain pessimistic for a long period
despite the stimulus from QE.
Table E: Maximum effects of QE: TVP-SVAR
CPI Inflation GDP growth Adjustment \ Estimate BR endogenous BR exogenous BR endogenous BR exogenous 80bp 0.87pp 3.20pp 0.56pp 2.64pp 100bp 1.30pp 3.63pp 0.86pp 2.98pp 120bp 1.71pp 4.09pp 1.15pp 3.29pp Less persistence 0.87pp 3.42pp 0.56pp 2.82pp
Note: BR is abbreviation for Bank Rate. The BR endogenous scenario is the forecast conditional on only the adjusted government bond spreads. The BR exogenous scenario is the forecast conditional on the adjusted government bond spreads and Bank Rate.
The forecast performance not withstanding, we can still evaluate the effects of QE using the
TVP-SVAR model. Using the Bank Rate endogenous scenario the effects of QE are large and
persistent reflecting agents’ pessimism about the economic outlook. For the Bank Rate
exogenous scenario, the effects of QE are much larger. This is similar to the MS-SVAR and may
be due to the fact that when the policy rate is exogenised recovery can only be achieved by
lowering spreads. In the case with less persistence of the QE shock, the TVP-SVAR suggests that
15This is a standard feature of structural models with adaptive learning see, for example, Evans and Honkapohja (2001).
Working Paper No. 443 January 2012 25
the effects on output and CPI inflation would be commensurately smaller, broadly in line with
findings for the MS-SVAR.
8 Summary of empirical results
Table F provides a summary of the key results from all three models employed in this paper,
showing the peak effects of a 100 basis point QE shock from the counterfactual simulations.
However, these effects occur at different times across the three models. Although the models are
strictly not directly comparable due to their different dynamic structures and their informational
content,16 they jointly illustrate the range of potential macroeconomic impacts of QE.
Table F: Summary table: maximum effect of QE (100 basis point contraction in spreads)
CPI Inflation GDP Level Adjustment \ Estimate BR endogenous BR exogenous BR endogenous BR exogenous BVAR 1.03pp 1.07pp 0.72% 0.28% MS-SVAR 1.31pp 3.38pp 2.75% 5.13% TVP-SVAR 1.30pp 3.63pp 0.86% 5.36% Model Average∗ 1.21pp 2.60pp 1.42% 3.59%
Note(∗): Model averaging done with an equally weighted probability. BR is abbreviation for Bank Rate. The BR endogenous scenario is the forecast conditional on only the adjusted government bond spreads. The BR exogenous scenario is the forecast conditional on the adjusted
government bond spreads and Bank Rate.
The final row of the table illustrates the effects implied by averaging across the models on the
basis of an equally weighted probability for inflation and GDP.17 The average model prediction
indicates that, without the 100 basis point contraction in government bond spreads following the
implementation of QE, output would have been between1.4and3.6lower while CPI
inflation would have been reduced by between1.2to2.6percentage points relative to the
baseline model prediction.
The range of these estimates reflects the different assumptions made about the policy rate in the
two counterfactual simulations. Making Bank Rate exogenous produces a much larger range of
results across the models. We put more emphasis on the more conservative model average
results; the Bank Rate endogenous scenario. Our preferred average estimates from the three
16Although from Proposition 1 in Waggoner and Zha (1999) it is clear that the structural identification scheme plays no role in the conditional forecast, in this instance we could only loosely compare these models due to the different manner in which the reduced-form dynamics are modelled. 17To enable model comparison, we convert the GDP growth effects obtained from the smaller models to an equivalent GDP level effect.
Working Paper No. 443 January 2012 26
models therefore suggest that QE may have had a peak effect on the level of real GDP of around
11/2and a peak effect on annual CPI inflation of about11/4percentage points. Clearly, there is
considerable uncertainty around all of the estimates, which increase as the forecast horizon
lengthens. These results should be viewed as an attempt to quantify the macroeconomic effects
of a 100 basis point reduction in long-term interest rates. Of course, as noted earlier QE may
have affected the real economy in a variety of other ways and not just through its effect on long
rates (for example through confidence effects), but we have not investigated the impact of these
other possible transmission channels in this paper.
9 Conclusion
In this paper we provide new results on the potential macroeconomic effects of the Bank of
England’s QE programme during March 2009 to January 2010. We employ a multiple models
approach, using three different time-series models. Results from a large BVAR model suggest
that without QE real GDP would have fallen by even more during 2009 and inflation would have
reached low or even negative levels. Results obtained from analysis using an MS-SVAR model
and a TVP-SVAR model broadly support those obtained from the BVAR, if anything suggesting
that the impact might have been even larger. Overall, our analysis would suggest that QE was an
effective policy option during the financial crisis. However, the magnitude of its effects varies
considerably across the different model specifications, and with the precise assumptions made to
generate the counterfactual simulations, so these estimates are subject to considerable
uncertainty.
Our analysis also needs to be qualified by a number of caveats. First, it is clear that any form of
counterfactual exercise is very uncertain, particularly so in this case given the relative uniqueness
of QE. Second, we have chosen a set of models that, while different, are nevertheless related and,
therefore, may provide similar answers. Third, we have exclusively focused on the link between
government bond spreads and macroeconomic variables, ignoring other possible transmission
channels. Despite these caveats, our multiple times-series approach provide a useful benchmark
for assessing the macroeconomic impact of QE.
Working Paper No. 443 January 2012 27
Appendix A: Estimation of large BVAR model
In what follows we briefly discuss the estimation of the large BVAR described in (1). We can
compactly rewrite the VAR as:
Y =XhΨh+E,(A-1)
where Y =[yh+1,..,yT] ′ is a T ×N matrix containing all the data points in yt , Xh = [1 Y−h] is a
T ×M matrix containing a vector of ones (1) in the first columns and the h-th lag of Y in the
remaining columns,Ψh=[Φ0,hΦ1,h]′ is a M× N matrix, and E =[εh+1,..,εT]
′ is a T ×N matrix
of disturbances. As only one lag is considered we have M = N +1. The prior distribution can
then be written as:
Ψh∣Σ∼N(Ψ0,Σ⊗Ω0),Σ∼IW(v0,S0).(A-2)
Note thatΨh∣Σis a matric-variate normal distribution where the prior expectationE[Ψh]=Ψ0
and prior varianceVar[Ψh]=Σ⊗Ω0are set according to equation (2). The prior variance matrix
has a Kroneker structureVar[Ψh]=Σ⊗Ω0whereΣis the variance matrix of the disturbances
and the elements of Ω0 are given byVar[Φ(ij)1,h] in (2). Since the normal-inverted Wishart prior is
conjugate, the conditional posterior distribution of this model is also normal-inverted Wishart
(Zellner (1973)):
Ψh∣Σ,Y∼N(Ψˉ,Σ⊗Ωˉ),Σ∣Y∼ IW(vˉ,Sˉ),(A-3)
where the bar denotes that the parameters are those of the posterior distribution. DefiningΨ^and
Ê as the OLS estimates, we have thatΨˉ= (Ω−1 0 +X ′X)−1(Ω−1
0Ψ0+X ′Y ),
Ω̄ = (Ω−1 0 +X ′X)−1, v̄ = v0 +T , and S̄ =Ψ^′X′XΨ^+Ψ′0Ω
−1 0Ψ0+Ψ0+ Ê ′Ê−Ψ^′Ωˉ−1Ψ^.
In order to perform inference and forecasting one needs the full joint posterior distribution and
the marginal distributions of the parametersΨˉandΣ.One could use the conditional posteriors in
(A-3) as a basis of a Gibbs sampling algorithm that drawing in turn from the conditionalsΨh∣Σ,Y
andΣ∣Ywould eventually produce a sequence of draws from the joint posteriorΨhΣ∣Yand the
marginal posteriorsΨh∣Y,Σ∣Y, as well as the posterior distribution of any function of these
coefficients (for example, multi-step forecasts or impulse responses).
Still, if one is interested only in the posterior distribution ofΨh(rather than in any non-linear
function of it) there is an alternative to simulation: by integrating outΣfrom (A-3). Zellner
Working Paper No. 443 January 2012 28
(1973)) has shown that the marginal posterior distribution ofΨhis a matric-variate t:
Ψh∣Y∼MT(Ψˉ,Ωˉ−1,Sˉ,vˉ).(A-4)
The expected value for this distribution is given by:
Ψˉ= (Ω−1 0 +X ′X)−1(Ω−1
0Ψ0+X ′Y),(A-5)
which is obviously extremely fast to compute. Recalling thatΨ^is the OLS estimator, and using
the normal equations (X′X)−1Ψ^= X ′Y we can rewrite this as:
Ψˉ= (Ω−1 0 +X ′X)−1(Ω−1
0Ψ0+X′XΨ^),(A-6)
which shows that the posterior mean ofΨhis a weighted average of the OLS estimator and of the
prior meanΨ0,with weights proportional to the inverse of their respective variances. In the
presence of a tight prior (ie, whenθ→0) the posterior estimate will collapse toΨˉ=Ψ0,while
with a diffuse prior (ie, whenθ→∞)the posterior estimate will collapse to the unrestricted OLS
estimate.
Given the posterior meanΨˉ=[Φˉ0,hΦˉ1,h]′, it is straightforward to produce forecasts up to h steps
ahead simply by setting:
ŷt+h =Φˉ0,h+Φˉ1,hyt,(A-7)
As shown by Banbura et al (2010) it is also possible to implement the prior described above
using a set of dummy observations. Consider adding Td dummy observations Yd and Xd such that
their moments coincide with the prior moments:Ψ0= (X ′dXd) −1X ′dYd , Ω0 = (X ′dXd)
−1, v0 =
Td−M−N−1,S0 =(Yd−XdΨ0)′(Yd−XdΨ0).Augmenting the system in (A-1) with the
dummy observations gives:
Y+ = X+ hΨh+E+,(A-8)
where Y+ = (Y ′ Y ′d) ′ and E+ = (E ′ E ′d)
′ are (T +Td)×N matrices and X+ = (X ′ X ′d) ′ is a
(T +Td)×M matrix. Then it is possible to show that the OLS estimator of the augmented system
(given by the usual formula (X+′ h X+
h )−1X+′ h Y+) is numerically equivalent to the posterior meanΨˉ.
A.1 Prior tightness
To make the prior operational, one needs to choose the value of the hyperparameterφ.We
discuss a number of methods for addressing this issue. The marginal data density of the model
Working Paper No. 443 January 2012 29
can be obtained by integrating out all the coefficients, ie, definingΘas the set of all the
coefficients of the model, the marginal data density is:
p(Y ) =∫
p(Y∣Θ)p(Θ)dΘ.(A-9)
Under our normal-inverted Wishart prior the density p(Y ) can be computed in closed form (see
Bauwens, Lubrano and Richard (1999)). At each point in timeφcould be chosen by maximising:
φ∗ t = argmax
φ
ln p(Y ) (A-10)
This method has been used by Carriero, Kapetanios and Marcellino (2010). However, as
discussed there, such a method may have a tendency to choose low values for the tightness
parameter implying a large weight on the prior. It is important for our purposes to give
considerable weight on the data. We therefore adopt an alternative approach whereby the
tightness parameter is chosen by matching the fit of particular equations in the large VAR to
those from smaller VAR models. Lenza et al (2010) use a similar approach to set tightness. We
find this approach produces a reasonable balance between the effects of priors and data that is
appropriate for our analysis.
Working Paper No. 443 January 2012 30
Appendix B: Estimation of MS-SVAR model and selection of the number of change points
We follow Chib (1998) and adopt a Bayesian Gibbs sampling approach to the estimation of the
MS-SVAR models. Here we briefly describe the main steps of the algorithm. The Gibbs
sampling algorithm proceeds in the following steps:
1. Sampling St:
Following Kim and Nelson (1999) we use the Multi-Move Gibbs sampling algorithm to draw
St from the joint conditional density f ( St |Zt,cS,B1,S,...,BK,S,ΩS,P̃
) . We impose the
restriction that each regime must have at least N× (K +1)+2 observations, where N denotes
the number of endogenous variables in the VAR, to ensure sufficient degrees of freedom for
each regime.
2. SamplingcS,B1,S,...,BK,S,ΩS:
Conditional on a draw for St , the model is simply a sequence of Bayesian VAR models. The
regime specific VAR coefficients are sampled from a normal distribution and the covariances
are drawn from an inverted Wishart distribution. For the first M regimes, we use a normal
inverse Wishart prior (see Kadiyala and Karlsson (1997)). However, as described in detail
below, we employ a (normal diffuse) prior distribution for the VAR coefficients of the final
regime, which is compatible with the identification of the shock to the government bond
spread. In our sample, the recent financial crisis coincides with the final regime of the
estimated VAR model. The prior on the VAR coefficients in this regime implies that the policy
rate does not respond to lagged changes in other endogenous variables. This assumption is
compatible with restrictions used to identify the shock to the bond yield spread and reflects the
fact that policy rates have reached the ZLB.
3. Sampling P̃:
Given the state variables St , the non-zero elements of the transition probability matrix are
independent of Zt and the other parameters of the model and are drawn from a Dirichlet
posterior.
We estimate the MS-SVAR model using200,000replications of the Gibbs sampler and discard
the first 190,000 as burn-in. Chart 6 plots the 20th order autocorrelation for the key parameters of
the benchmark model. These are close to zero providing evidence in favour of convergence.
Working Paper No. 443 January 2012 31
Appendix C: Estimation of TVP-SVAR model
The TVP-SVAR model is estimated using the Bayesian methods described in Kim and Nelson
(1999). In particular, we employ a Gibbs sampling algorithm that approximates the posterior
distribution. Here we summarise the basic algorithm which involves the following steps:
1. The VAR coefficients B̃t and the off-diagonal elements of the covariance matrix At are
simulated by using the methods described in Carter and Kohn (1994). As is common practice
in this literature (see for example, Cogley and Sargent (2005)) we impose the constraint that B̃t
should be stable at each point in time.
2. The volatilities of the reduced-form shocks Ht are drawn using the date-by-date blocking
scheme introduced in Jacquier, Polson and Rossi (2004).
3. The hyperparameters Q and S are drawn from an inverse Wishart distribution while the
elements of G are simulated from an inverse gamma distribution.
Chart 7 shows the recursive means of the retained draws appear stable, providing evidence of
convergence.
The lag length is set at two. The data sample runs from 1958 Q1 to 2011 Q1 and we use the first
ten years of data as a training sample that is used to calibrate priors.
Working Paper No. 443 January 2012 32
Appendix D: Data appendix for large BVAR model
The data set for the large BVAR model is given in Table G.
Table G: Data appendix for large BVAR model
t No. Variable Source No. Variable Source
1 US industrial production DS 23 20-year UK gilts BofE 2 US CPI DS 24 15-year UK gilts BofE 3 Euro-area industrial production DS 25 7-year UK gilts BofE 4 Euro-area HICP ECB 26 3-year UK gilts BofE 5 UK GDP NIESR 27 5-year 5-year implied inflation BofE 6 UK industrial production ONS 28 6-month Libor BG 7 Brent dollar oil price DS 29 12-month Libor BG 8 UK CPI ONS 30 FTSE All-Share index DS 9 UK-PPI ONS 31 FTSE All-Share dividend yield DS 10 UK-UEMP ONS 32 FTSE All-Share price-earnings ratio DS 11 UK house price index HF 33 UK exchange rate index BofE 12 10-year gilt - T-bill spread BofE 34 US dollar-sterling exchange rate BofE 13 UK consumer confidence EC 35 Euro-sterling exchange rate BofE 14 M4 BofE 36 T-bill - Bank Rate spread BofE 15 M3 BofE 37 3-month Libor - T-bill spread BofE 16 Retail deposit and cash in M4 BofE 38 3-month Libor-Bank Rate spread BofE/BG 17 Secured lending to individuals BofE 39 2-year gilt - T-bill spread BofE 18 M4 net lending to private sector BofE 40 5-year gilt - T-bill spread BofE 19 M4 lending BofE 41 Bank Rate BofE 20 Household M4 BofE 42 US federal funds rate Fed 21 PNFC M4 BofE 43 Euro-MRO interest rate BD/BG 22 OFC-M4 BofE
Data Sources: Bank of England (BofE), Board of Governors of the Federal Reserve System (Fed), Bundesbank (BD), European Central Bank (ECB), European Commission (EC), National Institute of Economic and Social Research (NIESR), Datastream (DS), Bloomberg (BG), Office for National Statistics (ONS) and Halifax (HF). Data transformation: We use log-levels for the variables except those which are already in growth rates.
Working Paper No. 443 January 2012 33
Appendix E: Charts
Chart 1: Regime estimation for the MS-SVAR model
1970 1980 1990 2000 2010 0
0.5
1 Probability of Regime 1
Pr ob
ab ilit
y
1970 1980 1990 2000 2010 0
0.5
1 Probability of Regime 2
Pr ob
ab ilit
y
1970 1980 1990 2000 2010 0
0.5
1 Probability of Regime 3
Pr ob
ab ilit
y
1970 1980 1990 2000 2010 0
0.5
1 Probability of Regime 4
Pr ob
ab ilit
y
0 0
0 0
Probability 3−month T−Bill Bond yield spread GDP growth CPI inflation M4 growth Stock price growth
Working Paper No. 443 January 2012 34
Chart 2: BVAR counterfactual analysis
No policy counterfactual simulations for the level of
real GDP (Bank Rate endogenous)
No policy counterfactual simulations for the level of
real GDP (Bank Rate exogenous)
No policy Counterfactual simulations for inflation
(Bank Rate endogenous)
No policy counterfactual simulations for inflation
(Bank Rate exogenous)
92
94
96
98
100
102
104
Sep-08 Dec-08 Mar-09 Jun-09 Sep-09 Dec-09
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
Real GDP
2006=100
92
94
96
98
100
102
104
Sep-08 Jan-09 May-09 Sep-09 Jan-10 May-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistance)
Model Prediction
Real GDP
2006=100
-1
0
1
2
3
4
5
6
Sep-08 Feb-09 Jul-09 Dec-09 May-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
Inflation
Per cent
-1
0
1
2
3
4
5
6
Sep-08 Feb-09 Jul-09 Dec-09 May-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistance)
Model Prediction
Inflation
Per cent
Working Paper No. 443 January 2012 35
Chart 3: Conditional forecasts, MS-SVAR: GDP growth and inflation
No policy counterfactual simulations for GDP growth
(Bank Rate endogenous)
No policy counterfactual simulations for GDP growth
(Bank Rate exogenous)
No policy counterfactual simulations for inflation
(Bank Rate endogenous)
No policy counterfactual simulations for inflation
(Bank Rate exogenous)
-12
-10
-8
-6
-4
-2
0
2
4
Sep-08 Dec-08 Mar-09 Jun-09 Sep-09 Dec-09
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
GDP Growth
Per cent
-12
-10
-8
-6
-4
-2
0
2
4
Sep-08 Jan-09 May-09 Sep-09
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
GDP Growth
Per cent
-4
-2
0
2
4
6
Sep-08 Dec-08 Mar-09 Jun-09 Sep-09 Dec-09
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
Inflation
Per cent
-4
-2
0
2
4
6
Sep-08 Feb-09 Jul-09 Dec-09 May-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
Inflation
Per cent
Working Paper No. 443 January 2012 36
Chart 4: Responses after a spread shock in MS-SVAR
20 40
0
0.05
0.1 S (spread)
20 40 −0.3
−0.2
−0.1
0
Y (spread)
20 40
−0.1
−0.05
0
π(spread)
20 40 0
0.1 0.2 0.3
M (spread)
20 40 −5 −4 −3 −2 −1
SP (spread)
20 40
0
0.05
0.1 S (spread)
20 40
−0.15 −0.1
−0.05 0
Y (spread)
20 40 −0.1
−0.05
0
π(spread)
20 40
0.1
0.2
0.3
M (spread)
20 40 −6
−4
−2
0 SP (spread)
20 40
0.05
0.1 S (spread)
20 40 −0.15
−0.1
−0.05
0 Y (spread)
20 40
−0.08 −0.06 −0.04 −0.02
π(spread)
20 40
0 0.1 0.2 0.3
M (spread)
20 40
−6 −4 −2
0 SP (spread)
20 40 0
0.05
0.1 S (spread)
20 40
−0.6
−0.4
−0.2
0 Y (spread)
20 40
−0.3
−0.2
−0.1
π(spread)
20 40 0.2 0.4 0.6 0.8
1 1.2 1.4
M (spread)
20 40 −20
−10
0 SP (spread)
Working Paper No. 443 January 2012 37
Chart 5: Conditional forecasts, TVP-SVAR: GDP growth and inflation
No policy counterfactual simulations for GDP  growth
(Bank Rate endogenous)
No policy counterfactual simulations for GDP growth
(Bank Rate exogenous)
No policy counterfactual simulations for inflation
(Bank Rate endogenous)
No policy counterfactual simulations for inflation
(Bank Rate exogenous)
-10
-8
-6
-4
-2
0
2
4
Sep-08 Feb-09 Jul-09 Dec-09 May-10 Oct-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
GDP Growth
Per cent
-10
-8
-6
-4
-2
0
2
4
Sep-08 Jan-09 May-09 Sep-09 Jan-10 May-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
GDP Growth
Per cent
-3
-2
-1
0
1
2
3
4
5
6
Sep-08 Feb-09 Jul-09 Dec-09 May-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
Inflation
Per cent
-3
-2
-1
0
1
2
3
4
5
6
Sep-08 Mar-09 Sep-09 Mar-10 Sep-10
No QE counterfactual (+100bps)
No QE counterfactual (+80bps)
No QE counterfactual (+120bps)
No QE counterfactual (persistence)
Model Prediction
Inflation
Per cent
Working Paper No. 443 January 2012 38
Chart 6: Convergence diagnostic statistics: MS-SVAR
100 200 300 400
−0.04
−0.02
0
0.02
0.04
MS−SVAR Coefficients
A ut
oc or
re la
tio n
Number of Parameters 20 40 60 80 100 120 140
0
0.1
0.2
0.3
0.4
MS−SVAR Covariance Matrices
A ut
oc or
re la
tio n
Number of Parameters
1 2 3 4 5 6 −4
−2
0
2
4
6
x 10 −3 Transition Probabilities
A ut
oc or
re la
tio n
Number of Parameters
Working Paper No. 443 January 2012 39
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQED_Stb4jpbPIYvunmfkgNpipw3GnZb4ebRovwN6WLKHbkZgU-cQEPZIsO5zSPEPp9y6HTCV4ei0yiP7xJU-MInxE52BWFX-LohFiUZypZCqRCGuHvVTnE8eHqHZ-FgfTBuVngz=w1062-h812-v0?authuser=1)

Chart 7: Convergence diagnostic statistics: TVP-SVAR
Working Paper No. 443 January 2012 40
References
Aı̈t-Sahalia, Y, Andritzky, J R, Jobst, A, Nowak, S B and Tamirisa, N T (2009), ‘How to stop a herd of running bears? Market response to policy initiatives during the global financial crisis’, International Monetary Fund, IMF Working Paper No. 09/204.
Andrés, J, López-Salido, J D and Nelson, E (2004), ‘Tobin’s imperfect asset substitution in optimizing general equilibrium’, Journal of Money, Credit and Banking, Vol. 36, No. 4, pages 665–90.
Banbura, M, Giannone, D and Reichlin, L (2010), ‘Large Bayesian vector auto regressions’, Journal of Applied Econometrics, Vol. 25, No. 1, pages 71–92.
Baumeister, C and Benati, L (2010), ‘Unconventional monetary policy and the great recession -estimating the impact of a compression in the yield spread at the zero lower bound’, European Central Bank, Working Paper Series No. 1258, Oct.
Bauwens, L, Lubrano, M and Richard, J-F (1999), Bayesian inference in dynamic econometric models, Oxford University Press.
Bean, C (2011), ‘Lessons on unconventional monetary policy from the United Kingdom’, speech given at the US Monetary Policy Forum, New York on 25 February 2011. Available at: www.bankofengland.co.uk/publications/speeches/2011/speech478.pdf.
Bean, C, Paustian, M, Penalver, A and Taylor, T (2010), ‘Monetary policy after the fall’, Federal Reserve Bank of Kansas City Annual Conference.
Benford, J, Berry, S, Nikolov, K and Young, C (2009), ‘Quantitative easing’, Bank of England Quarterly Bulletin, Vol. 49, No. 2, pages 90–100.
Bernanke, B S, Reinhart, V R and Sack, B P (2004), ‘Monetary policy alternatives at the zero bound: an empirical assessment’, Brookings Papers on Economic Activity, Vol. 35, No. 2, pages 1–100.
Bridges, J and Thomas, R (2012), ‘The impact of QE on the UK economy - some supportive monetarist arithmetic’, Bank of England Working Paper No. 442.
Carriero, A, Kapetanios, G and Marcellino, M (2010), ‘Forecasting government bond yields with large Bayesian VARs’, Queen Mary, University of London, School of Economics and Finance, Working Paper No. 662.
Carter, C K and Kohn, R (1994), ‘On Gibbs sampling for state space models’, Biometrika, Vol. 81, No. 3, pages 541–53.
Chib, S (1998), ‘Estimation and comparison of multiple change-point models’, Journal of Econometrics, Vol. 86, No. 2, June, pages 221–41.
Working Paper No. 443 January 2012 41
Christiano, L (2011), ‘Commentary: remarks on unconventional monetary policy’, International Journal of Central Banking, Vol. 7, No. 1, pages 121–30.
Christiano, L and Ikeda, D (2011), ‘Government policy, credit markets and economic activity’, National Bureau of Economic Research, Working Paper No. 17142.
Chung, H, Laforte, J-P, Reifschneider, D and Williams, J C (2011), ‘Have we underestimated the likelihood and severity of zero lower bound events?’, Federal Reserve Bank of San Francisco, Working Paper Series No. 2011-01.
Cogley, T and Sargent, T J (2005), ‘Drift and volatilities: monetary policies and outcomes in the post WWII US’, Review of Economic Dynamics, Vol. 8, No. 2, April, pages 262–302.
Curdia, V and Woodford, M (2009), ‘Conventional and unconventional monetary policy’, CEPR, CEPR Discussion Paper No. 7514, Oct.
Dale, S (2010), ‘QE – one year on’, remarks at the CIMF and MMF Conference.
D’Amico, S and King, T B (2010), ‘Flow and stock effects of large-scale Treasury purchases’, Federal Reserve Board, Working Paper No. 2010-52.
Doh, T (2010), ‘The efficacy of large-scale asset purchases at the zero lower bound’, Economic Review, Vol. 95, No. 2, pages 5–34.
Eggertsson, G B and Woodford, M (2003), ‘The zero bound on interest rates and optimal monetary policy’, Brookings Papers on Economic Activity, Vol. 34, No. 1, pages 139–235.
Estrella, A (2005), ‘Why does the yield curve predict output and inflation?’, Economic Journal, Vol. 115, No. 505, 07, pages 722–44.
Evans, G W and Honkapohja, S (2001), Learning and expectations in macroeconomics, Princeton University Press.
Gagnon, J, Raskin, M, Remache, J and Sack, B (2011), ‘The financial market effects of the Federal Reserve’s large-scale asset purchases’, International Journal of Central Banking, Vol. 7, No. 1, March, pages 3–43.
Greenwood, R and Vayanos, D (2008), ‘Bond supply and excess bond returns’, National Bureau of Economic Research, Inc, NBER Working Paper No. 13806, Feb.
Hamilton, J D and Wu, J C (2011), ‘The effectiveness of alternative monetary policy tools in a zero lower bound environment’, National Bureau of Economic Research, Inc, NBER Working Paper No. 16956, Apr.
Harrison, R (2012), ‘Asset purchase policy at the effective lower bound for interest rates’, Bank of England Working Paper No. 444.
Jacquier, E, Polson, N and Rossi, P (2004), ‘Bayesian analysis of stochastic volatility models’, Journal of Business and Economic Statistics, Vol. 12, pages 371–418.
Working Paper No. 443 January 2012 42
Joyce, M, Lasaosa, A, Stevens, I and Tong, M (2011), ‘The financial market impact of quantitative easing’, International Journal of Central Banking, Vol. 7, No. 3, pages 113–61.
Kadiyala, K R and Karlsson, S (1997), ‘Numerical methods for estimation and inference in Bayesian VAR-models’, Journal of Applied Econometrics, Vol. 12, No. 2, pages 99–132.
Kim, C-J and Nelson, C R (1999), State-space models with regime switching, Cambridge, Massachusetts: MIT Press.
Kimura, T and Small, D H (2006), ‘Quantitative monetary easing and risk in financial asset markets’, The BE Journal of Macroeconomics, Vol. 6, No. 1, pages 1–54.
Krishnamurthy, A and Vissing-Jorgensen, A (2011), ‘The effects of quantitative easing on interest rates: channels and implications for policy’, NBER Working Paper No. 17555, Oct.
Lenza, M, Pill, H and Reichlin, L (2010), ‘Monetary policy in exceptional times’, Economic Policy, Vol. 25, No. 62, pages 295–339.
Litterman, R (1986), ‘Forecasting with Bayesian vector autoregressions - five years of experience’, Journal of Business and Economic Statistics, Vol. 4, pages 25–38.
Markowitz, H (1952), ‘Portfolio selection’, The Journal of Finance, Vol. 7, pages 77–91.
Meier, A (2009), ‘Panacea, curse, or nonevent? Unconventional monetary policy in the United Kingdom’, International Monetary Fund, IMF Working Paper No. 09/163, Aug.
Mitchell, J, Smith, R J, Weale, M R, Wright, S and Salazar, E L (2005), ‘An indicator of monthly GDP and an early estimate of quarterly GDP growth’, Economic Journal, Vol. 115, No. 501, pages F108–F129.
Modigliani, F and Sutch, R (1966), ‘Innovations in interest rate policy’, The American Economic Review, Vol. 56, No. 1/2.
Modigliani, F and Sutch, R (1967), ‘Debt management and the term structure of interest rates: an empirical analysis of recent experience’, Journal of Political Economy, Vol. 75, page 569.
Neely, C J (2010), ‘The large scale asset purchases had large international effects’, Federal Reserve Bank of St. Louis, Working Paper No. 2010-018.
Primiceri, G E (2005), ‘Time varying structural vector autoregressions and monetary policy’, Review of Economic Studies, Vol. 72, No. 3, July, pages 821–52.
Sims, C (1980), ‘Macroeconomics and reality’, Econometrica, Vol. 48, pages 1–48.
Swanson, E T (2011), ‘Let’s twist again: a high-frequency event-study analysis of operation twist and its implications for QE2’, Federal Reserve Bank of San Francisco, Working Paper Series No. 2011-08.
Working Paper No. 443 January 2012 43
Tobin, J (1969), ‘A general equilibrium approach to monetary theory’, Journal of Money, Credit and Banking, Vol. 1, No. 1, pages 15–29.
Trichet, J-C (2009), ‘The ECB’s enhanced credit support’, keynote address at the University of Munich, 13 July 2009. Available at: www.ecb.int/press/key/date/2009/html/sp090713.en.html.
Ugai, H (2007), ‘Effects of the quantitative easing policy: a survey of empirical analyses’, Monetary and Economic Studies, Vol. 25, No. 1, pages 1–48.
Vayanos, D and Vila, J-L (2009), ‘A preferred-habitat model of the term structure of interest rates’, National Bureau of Economic Research, Inc, NBER Working Paper No. 15487, Nov.
Waggoner, D F and Zha, T (1999), ‘Conditional forecasts in dynamic multivariate models’, The Review of Economics and Statistics, Vol. 81, No. 4, November, pages 639–51.
Zellner, A (1973), An introduction to Bayesian inference in econometrics, Wiley.
Working Paper No. 443 January 2012 44