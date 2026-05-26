
# Staff Working Paper No. 542 Unconventional monetary policies and the macroeconomy:  the impact of the United Kingdom’s QE2 and Funding for Lending Scheme
## Rohan Churm, Michael Joyce, George Kapetanios and Konstantinos Theodoridis
### August 2015
Staff Working Papers describe research in progress by the author(s) and are published to elicit comments and to further debate.  Any views expressed are solely those of the author(s) and so cannot be taken to represent those of the Bank of England or to state Bank of England policy.  This paper should therefore not be reported as representing the views of the Bank of England or members of the Monetary Policy Committee, Financial Policy Committee or Prudential Regulation Authority Board.Staff Working Paper No. 542 Unconventional monetary policies and the macroeconomy:  the impact of the United Kingdom’s QE2 and Funding for Lending Scheme
### Rohan Churm,(1) Michael Joyce,(2) George Kapetanios(3) and Konstantinos Theodoridis(4)
**Abstract**
In this paper we assess the macroeconomic effects of two of the flagship unconventional monetary policies used by the Bank of England during the later stages of the global economic crisis:  additional quantitative easing (QE) and the introduction of the Funding for Lending Scheme (FLS).  We argue that these policies can be seen as complements, as QE effectively bypasses the banks by attempting to reduce risk-free yields directly in order to have a wider effect on asset prices, while FLS operates directly through banks by reducing their funding costs and increasing incentives to lend.  We attempt to quantify the effects of these policies by estimating their impact on long-term interest rates and bank funding costs, respectively, and then tracing out their wider effects on the macroeconomy using simulations from a large Bayesian vector autoregression (VAR), which are cross-checked with a simpler auto-regressive distributed lag (ARDL) approach.  We find that the second round of the Bank’s QE purchases during 2011–12 and the initial phase of the FLS each boosted GDP in the United Kingdom by around 0.5%–0.8%.  Their effect on inflation was also broadly positive reaching around 0.6 percentage points, at its peak.
**Key words:**Bayesian methods, large-scale asset purchases, quantitative easing, Funding for Lending Scheme, vector autoregressions, auto-regressive distributed lag.
**JEL classification:**C11, C32, E52, E58.
(1)  Bank of England:  Email:  rohan.churm@bankofengland.co.uk. (2)  Bank of England:  Email: mike.joyce@bankofengland.co.uk (3)  Queen Mary, University of London:  Email:  g.kapetanios@qmul.ac.uk (4)  Bank of England:  Email:  konstantinos.theodoridis@bankofengland.co.uk
The views expressed in this paper are those of the authors, and not necessarily those of the Bank of England.
Information on the Bank’s working paper series can be found at www.bankofengland.co.uk/research/Pages/workingpapers/default.aspx
Publications Team, Bank of England, Threadneedle Street, London, EC2R 8AH Telephone +44 (0)20 7601 4030  Fax +44 (0)20 7601 3298  email publications@bankofengland.co.uk
**© Bank of England 2015**ISSN 1749-9135 (on-line)
1 Introduction
The pronounced global financial crisis in late 2008 led to a severe economic downturn on a scale not
seen since the Great Depression of the 1930s. The fiscal and monetary authorities of many countries
responded with a variety of conventional and less conventional measures aimed at mitigating the effects
on financial stability and the real economy. In the aftermath of the crisis, the Bank of England (BoE),
like many other central banks, introduced a number of innovative policy measures to loosen monetary
conditions, as the scope for conventional policy rate reductions became increasingly constrained by
the fact that interest rates were already close to their lower bound. These measures included enhanced
liquidity support, actions to deal with dysfunctional financial markets and large-scale asset purchases,
as discussed in Bean (2011).
The aim and contribution of this paper is to assess the macroeconomic impact of two of these
so-called unconventional monetary policy measures: Quantitative Easing (QE) and the Funding for
Lending Scheme (FLS).
The first of these policies, QE, was initially announced in March 2009 at the height of the global
crisis, with the first round of £200 billion of purchases, predominantly of UK government securities
(gilts), concluding in January 2010. Our focus in this paper, however, is on the second round of
purchases between October 2011 and June 2012, when the Bank of England purchased £175 billion
of gilts, about 11% of nominal GDP, in response to concerns that the euro area sovereign crisis would
lead to UK CPI inflation undershooting its 2% target.
The second policy measure, FLS, was first announced by the Chancellor of the Exchequer and the
Governor of the Bank of England on 14 June 2012, with the aim of boosting lending to firms and
households, which had been broadly flat for over three years, despite the large monetary loosening
brought about by lower policy rates and QE. Under the scheme, banks and building societies were
offered cheap funding linked to additional lending to the real economy. Outstanding drawings at the
end of the first phase of the scheme, in January 2014, were £41.9bn. In total 46 groups participated
(in the first phase of the scheme), of whom 41 made at least one drawing. With its focus on reducing
bank funding costs in order to increase bank lending, the FLS can be viewed as complementary to
the policy of QE, which aimed to bypass banks through boosting asset prices and reducing borrowing
costs.
A large and growing literature has developed over recent years that tries to evaluate the impact
of the unconventional monetary policies adopted by central banks during the global financial crisis.1
Most of this literature has focused on the Fed’s various policy measures, and particularly its large-
scale asset purchase programmes, and their impact on financial markets (see eg Gagnon et al. (2011),
Krishnamurthy and Vissing-Jorgensen (2011), D’Amico et al. (2012) and D’Amico and King (2013))
and the macroeconomy (see eg Chen et al. (2012) and Baumeister and Benati (2013)). A large
literature has also grown up around the ECB’s non-standard measures (see eg Lenza et al. (2010),
Giannone et al. (2012) and Eser and Schwaab (2013)). In relative terms, much less has been written
on the BoE’s unconventional monetary policies, with most of the published studies to date focusing
on the financial market impact of the first phase of QE during March 2009 to January 2010 (see eg
Joyce et al. (2011a), Breedon et al. (2012), Joyce and Tong (2012)). Exceptions to this are Bridges
and Thomas (2012) and Kapetanios et al. (2012) who look at the macroeconomic effects of QE1.2
1For a review of some of the early literature, see Joyce et al. (2012b). 2Baumeister and Benati (2013) also look at the impact of QE in the UK, as well as the effects of unconventional
measures in the United States, euro area and Japan.
Of those papers covering the more recent period, McLaren et al. (2014) and Butt et al. (2012) both
focus more narrowly on the effects on the gilt market and broad money respectively, and there are no
studies of the macro effects of the FLS to our knowledge. By examining the macroeconomic impact
of the later round of purchases by the Bank during October 2011 to December 2012 (QE2), and the
FLS, this paper therefore attempts to fill an important gap in our knowledge of the effectiveness of
unconventional policies.
Our paper is most closely related to Kapetanios et al. (2012), who examine the macro economic
impact of QE1 during March 2009 to January 2010 using several time-varying VAR models of the
economy to construct counterfactual simulations, assuming that the impact of QE came through a
reduction in longer-term interest rates. We follow their broad approach by assessing the impact of
QE through a large-scale Bayesian VAR that is an adapted to include bank funding costs, in order
to allow us to investigate the impact of the FLS.3 To check for robustness, we also estimate a much
simpler ARDL model in line with the conclusions of Pesaran and Smith (2014). Both methods rely on
us being able to identify the shock to the yield curve and to bank funding costs arising through QE
and FLS. Kapetanios et al. (2012) relied on event study evidence on QE announcements to estimate
the latter but a problem of using this form of analysis in later rounds of QE is that the market was
better able to predict the MPC’s decisions (see eg Joyce et al. (2012a)). We therefore draw on a
number of additional approaches, including regression-based methods, in order to generate a plausible
estimate of the impact of QE2. Quantifying the impact of FLS faces similar challenges, as a range of
other factors, and in particular, developments in the euro area will have impacted on the funding costs
facing UK banks. In order to estimate the impact of FLS, we explicitly model the effects of euro area
developments on UK bank funding costs using a regression approach that uses principal components
to summarise the information in euro area bank and sovereign CDS and unsecured bank debt. Our
estimates of the impact of FLS on bank funding costs are an additional contribution of the paper.
The rest of the paper is structured as follows. In Section 2 we provide a short summary of the
Bank of England’s use of unconventional monetary policy during the financial crisis and in particular
how and why QE and the FLS were implemented. Section 3 turns to the modelling techniques we
use in the paper to quantify the macro-effects of the two policies. Sections 4 and 5 describe how we
estimate the impact of QE and FLS on financial market prices and macroeconomic variables. Section
6 sets out our conclusions.
2 The Bank of England’s use of unconventional monetary policies
This paper focuses on the macroeconomic impact of the BoE’s QE and FLS policies during the
financial crisis and therefore does not attempt to assess the full raft of policies introduced, by the
UK authorities, after 2007, including the recapitalisations of the banks, the Special Liquidity Scheme,
the Credit Guarantee Scheme, and the Asset Protection Scheme and Forward Guidance. With the
exception of Forward Guidance, these other policies are less obviously described as monetary policy
measures, though this boundary line is perhaps less clear when policy rates approach their lower
bound. In contrast, Forward Guidance is clearly a form of unconventional monetary policy using our
definition below, but our modelling approach - focussing on movements in observed contemporaneous
variables - is not well suited to analysing it. This section starts by explaining what we mean by
3The use of macro VAR model techniques to investigate the impact of unconventional policies has been used in other studies, such as Baumeister and Benati (2013) and Giannone et al. (2012).
term unconventional monetary policy and why we consider both QE and FLS to be unconventional
monetary policies. We then turn to the use of QE and FLS during the crisis by setting out the context
in which both policies have been used. The third section briefly discusses the transmission channels
through which both policies may affect the real economy, which can be viewed as complementary.
2.1 Conventional and unconventional monetary policies
Conventional monetary policy typically involves setting the value of the current policy rate. Bernanke
and Reinhart (2004) group alternative monetary policies into three classes: (1) using communications
policies to shape public expectations about the future course of interest rates; (2) increasing the size
of the central bank’s balance sheet; and (3) changing the composition of the central bank’s balance
sheet. All such policies are considered unconventional, and naturally come into play when greater
monetary stimulus is required than can be achieved by cutting the policy rate to its effective lower
bound. Such policies are likely to be complementary. Consistent with this, there can also be a role for
unconventional policy even when the policy rate is above its lower bound.4 This might occur when the
transmission mechanism is impaired, for example when interest rates in the economy become unusually
elevated relative to the policy rate. King (2009) distinguishes between ‘conventional unconventional’
and ‘unconventional unconventional’ measures. QE is in the former camp, involving the purchase of
liquid assets with the intention of expanding the central bank balance sheet and boosting the supply of
money. FLS is very much an unconventional unconventional measure. It was a direct response to the
threat to the UK economy caused by elevated bank funding spreads. It works primarily by changing
the composition of the central bank balance sheet, rather than through expansion. We discuss the
likely transmission mechanisms of these policies in more detail below, but for now can conclude that
they are both types of unconventional monetary policy.
One possible question regarding our categorisation of FLS is that the scheme is not voted on by
the MPC and instead overseen by a joint Bank of England/HM Treasury Oversight Board, potentially
implying that there is an element of fiscal policy. But the Scheme is fully operated by the Bank and is
operationally similar to other monetary policy operations such as the ECB’s Longer-Term Refinancing
Operations (LTRO) and targeted LTROs (TLTROs). We therefore interpret this form of governance
as simply reflecting a desire for joined up policy making given the exceptional challenges facing the
UK economy at the time, and the desire of the Bank to seek and receive assurance that the objectives
of the Scheme lay within its remit.5 The operation of the scheme could also potentially impact on the
Financial Stability objectives of the FPC and therefore both the MPC and the FPC were involved
ahead of the decision to modify the scheme in November 2013.6
2.2 Implementation
Table 1 provides a brief chronology of the main QE and FLS events. As discussed in the introduction,
QE was originally introduced in March 2009. This was in response to fears that without further
monetary easing measures the reduction of policy rates to 0.5% would be insufficient to avoid inflation
substantially undershooting the 2% inflation target in the medium term. The first phase of the Bank’s
4This has been emphasised by the ECB in particular. See Bini Smaghi (2009) or Trichet (2013). 5See FLS explanatory note http://www.bankofengland.co.uk/markets/Documents/explanatory notefls120713.pdf. 6For more information see http://www.bankofengland.co.uk/publications/Pages/news/2013/177.aspx
asset purchases ended in January 2010, by which time the Bank had made £200 billion of purchases,
which were overwhelmingly of UK government bonds. A second phase of purchases, sometimes referred
as QE2, was announced in October 2011, when a deterioration in the economic outlook associated with
the euro sovereign debt crisis again led to an increase in the risk of undershooting the inflation target
in the medium term. The MPC initially voted to increase its asset purchases by a further £75 billion,
with further extensions to the programme of £50 and £25 billion subsequently announced following
the February 2012 and July 2012 MPC meetings. After the conclusion of this phase of purchases, at
the beginning of November 2012, the Bank had purchased an additional £175 billion of gilts.
In June 2012, the Chancellor and the Governor of the Bank of England announced that the Bank
and Treasury had plans to launch a ‘funding for lending’ scheme to tackle the high level of bank
funding costs and give banks incentives to sustain or expand their lending to the UK households and
companies. The details of this scheme, the FLS, were subsequently announced the following month
on 13 July. The Scheme was designed to reduce funding costs for banks and building societies, so that
they can make loans cheaper and more easily available. Access to the Scheme was directly linked to
how much each bank and building society lends to the real economy. Those that increased lending
were able to borrow more under the Scheme, and do so at a much lower cost than those that scaled
back their loans.
In particular, over the eighteen months to the end of January 2014 – the ‘drawdown period’ – the
Bank of England offered to lend UK Treasury Bills to banks and building societies. These were lent
for a period of up to four years, for a fee. As security against that lending, banks provided collateral
– in the form of loans to businesses and households and other assets – to the Bank of England. Each
participating bank was able to borrow an amount up to 5% of its stock of existing loans to the UK
non-financial sector – ‘the real economy’ – as at end-June 2012, plus any expansion of its lending
during a ‘reference period’ from that date to the end of 2013.7 The price of each bank’s borrowing in
the Scheme was dependent on its net lending between 30 June 2012 and the end of 2013. For banks
maintaining or expanding their lending over that period, the fee was 0.25% per year on the amount
borrowed. For banks whose lending declined, the fee schedule increased linearly, adding 0.25% for each
1% fall in lending, up to a maximum fee of 1.5% of the amount borrowed for banks that contracted
their stock of lending by 5% or more.
2.3 Transmission channels
QE was primarily expected to affect GDP and inflation by reducing gilt yields and boosting other
asset prices, thereby reducing the costs of borrowing, and boosting expenditure through wealth effects.
This would occur mainly through a portfolio balance channel. Agents in the non-bank private sector
would prefer to reinvest the newly created bank deposits into riskier assets such as corporate bonds
and equities, absent a change in the price of those assets. This would lead to portfolio re-balancing
and asset price changes, due to the imperfect substitutability of money and securities, as originally
set out in Tobin (1963) and Brunner and Meltzer (1973).8 Asset prices might also be boosted through
7Any expansion of lending was calculated on a ‘net’ basis – new lending into the real economy minus repayments. Eligible lending was in sterling to UK resident households or private non-financial corporations and in the form of drawn loans. Banks’ holdings of securities did not count; neither did undrawn facilities. Purchases or sales of loans do not affect this measure, because they leave unchanged the total amount of credit to households and companies in the economy. Write-offs are also excluded from the measure of net lending used under the Scheme.
8For a discussion of the portfolio balance channel, see eg Andres et al. (2004).
T ab
le 1:
Q E
an d
F L
S C
h ro
n ol
og y
of K
ey A
n n
ou n
ce m
en ts
D at
e Q
E F
L S
5 M
ar ch
20 09
M P
C st
at em
en t
an n
ou n
ce s
B an
k w
il l
p u
rc h
as e
£ 75
b il
li on
of a ss
et s,
p ri
m ar
il y
co n ve
n ti
on al
gi lt
s, ov
er 3
m on
th s
fi n
an ce
d b y
th e
is su
e of
ce n tr
al b
an k
m on
ey .
P u
rc h
as es
ar e
to b
e sp
li t
b et
w ee
n tw
o m
at u
ri ty
se ct
o rs
fo r
gi lt
s w
it h
re m
a in
in g
m at
u ri
ti es
of :
5-10
ye ar
s an
d 10
-2 5
ye ar
s. [B
an k
R a te
al so
re d
u ce
d to
0. 5%
.] S
u b
se q u
en t
ex te
n si
o n
s to
th e
p ro
gr am
m e
an n
ou n
ce d
in M
ay 20
09 ,
A u
gu st
2 00
9 a n d
N ov
em b
er 20
09 .
O ve
ra ll £
20 0
b il
li on
o f
p u
rc h
as es
m ad
e b
et w
ee n
M ar
ch 20
09 an
d J an
u ar
y 20
10 .
6 O
ct o b
er 20
11 M
P C
st at
em en
t an
n ou
n ce
s th
at Q
E p
u rc
h as
es w
il l
b e
ex te
n d
ed b y
£ 75
b il
li on
to £
27 5
b il
li o n
. (T
h e
st ar
t of
Q E
2) 9
F eb
ru a ry
20 12
M P
C st
at em
en t
an n
ou n
ce s
th at
Q E
p u
rc h
as es
w il
l b
e ex
te n
d ed
b y
£ 50
b il
li on
to £
32 5
b il
li o n
. P
u rc
h as
es to
b e
sp li
t b
et w
ee n
th re
e se
ct or
s fo
r gi
lt s
w it
h re
m ai
n in
g m
at u
ri ti
es of
: 3-
7 ye
ar s,
7-15
y ea
rs an
d 15
ye a rs
a n
d gr
ea te
r. 14
J u
n e
20 12
G ov
er n
or an
d C
h an
ce ll
or an
n ou
n ce
B an
k an
d T
re as
u ry
w or
k in
g on
”f u
n d
in g
fo r
le n
d in
g” sc
h em
e. 5
J u
ly 20
12 M
P C
st at
em en
t an
n ou
n ce
s Q
E p
u rc
h as
es w
il l
b e
ex te
n d
ed b y
£ 50
b il
li on
to £
37 5
b il
li o n
. 13
J u
ly 20
12 T
h e
B an
k an
d T
re as
u ry
la u
n ch
th e
F u
n d
in g
fo r
L en
d in
g S
ch em
e (F
L S
). 1
A u
gu st
20 12
T h
e F
u n
d in
g fo
r L
en d
in g
sc h
em e
d ra
w d
ow n
w in
d ow
o p
en s.
a signalling channel that policy rates would remain lower for longer and also through improvements
in market liquidity. Other secondary channels were conceived as possible, including a bank lending
channel,9 although the MPC always downplayed the likely importance of the latter given that banks
were in the process of de-leveraging (see Joyce et al. (2011b) for further discussion).10
In contrast, the operation of the FLS was expected to affect GDP by reducing banks’ funding
costs, leading to easier credit conditions for real economy borrowers. The FLS offered banks a lump
sum of funding, which they could use for any purpose but which had a fee that was increasing if
they shrank their lending to the real economy. The FLS also offered banks a cheap source of further
funding, which they could access directly only if they expanded their lending to the real economy. And
the availability of FLS funding could bring about a fall in the cost of other sources of bank funding
by reducing the need for participating banks to issue debt in public markets or compete as hard for
term deposits. Together, lower overall bank funding costs would allow banks to reduce the cost of
loans or ease other, non-price terms. The increased supply of credit would then boost consumption
and investment spending.11
In general, QE was intended to work by circumventing the banking sector. QE would in the first
instance benefit the owners of assets, and businesses who could issue debt or equity in capital markets.
In contrast, FLS aimed to reduce borrowing costs by going directly through the banking sector. For
this reason the immediate beneficiaries were likely to be those who were reliant on banks as a source of
finance. Because the transmission mechanisms of the two policies were different they can be regarded
as complements. More importantly for this paper, it means that it is possible for us to identify them
separately.
3 Models
3.1 Bayesian VAR (BVAR)
The seminal work by Sims (1980) introduced the use of vector autoregressions (VAR) into macroe-
conometric modelling and VAR models continue to play a central role. More recently, the studies of
Lenza et al. (2010) and Koop (2011) illustrate how this modelling approach can be extended to large
information sets with remarkable good forecasting properties. Bayesian estimation techniques turn
out to be particularly useful in this large information setup to overcome parametrisation problems
which would otherwise be encountered when a standard VAR is estimated in large dimensions.
3.1.1 Notation and preliminaries
The model we use belongs to the general class of BVAR models for large data sets.12 Assuming that
all the variables in the large data set are in the vector Yt, we can write the model as:
Yt=Θ0+Θ1Yt−1+ · · ·+ΘpYt−p+et(1)
9Butt et al. (2014) evaluate whether QE provided a boost to bank lending in the UK. They find no evidence that QE gave rise to a bank lending channel, possibly because QE operating through a portfolio rebalancing channel gave rise to flighty deposits, mitigating any bank lending channel.
10For more on the intended transmission mechanism of QE, see Benford et al. (2009). 11For more on the intended transmission mechanism of FLS, see Churm et al. (2012). 12See, for example, Bandbura et al. (2010).
where et is a vector white-noise error term,Θ0is a vector of constants andΘ1toΘpare parameter
matrices. In our study Yt consists of 44 series meaning thatΘj(wherej=1,...,p)is a function of
1936 parameters, which leaves us no other choice but to restrict the number lag order of our empirical
model to one
Yt=Θ0+Θ1Yt−1+et(2)
3.1.2 A Normal-inverted Wishart prior
As will be discussed later, our large data set comprises both macroeconomic and financial market
variables. A good prior for BVAR models of the macroeconomy is a simple random walk forecast; see,
for example, Litterman (1986). Many macroeconomic and financial market variables are characterised
by persistent processes. In general, simple autoregressive(AR)or random walk(RW) models are
known to produce reasonable forecasts for macroeconomic and financial variables over short horizons.
We therefore choose a univariateAR(1)process as our prior for each of the stationary variables in the
BVAR model, while our prior for each nonstationary series is aRWprocess. With these priors, the
‘own’ first lag is considered to be the most important in every equation in the BVAR and the first two
moments of the VAR coefficient vector are given by:
E[Θ(ij)1 ] =
{ρifi=j
0 otherwise,Var[Θ
(ij)1 ] =φσ2i/σ
2j,(3)
whereρis set equal to one for nonstationary variables and estimated for stationary series (Mumtaz
and Zanetti (2012)),Θ(ij)1 denotes the element in position(i,j)in the matrixΘ1,and the covariances
among the coefficients inΘ1are zero. The shrinkage parameterφdetermines the tightness of the
prior or the extent to which the data influences the estimates. With a tight prior the data has little or
no influence on the estimates asφ→0. For a loose prior, whereφ→∞there is an increasing role for
the data and the estimates then converge to the standardOLSestimates. In our exerciseφhas been
set equal to one implying loose priors. To complete the specification of our BVAR prior, we assume
that the constant,Θ0,has a diffuse zero mean normal prior and the matrix of disturbances have an
inverted Wishart prior,Σ∼iW(v0,S0),wherev0andS0are the prior scale and shape parameters
with the expectation ofΣequal to a fixed diagonal residual varianceE[Σ]=diag(σ21,...,σ2N) . This is a
conjugate prior with a normal-inverted Wishart posterior distribution. The BVAR model is estimated
using rolling windows to account for structural change. Additional technical information on model
estimation and prior tightness is provided in Appendix A.
3.2 Autoregressive distributed lag model (ARDL)
Our approach to assess the real economy effects of unconventional policies relies on counterfactual
analysis. Pesaran and Smith (2014) argue that if the policy intervention affects the reduced-form pol-
icy parameters in the empirical model then one would not be in a position to carry out counterfactual
analysis correctly unless a full model of all endogenous variables is entertained and estimated. Our
BVAR model is such a model so our work can be considered as immune to their critique. However,
Pesaran and Smith (2014) also suggest an alternative approach. They argue that a general autore-
gressive distributed lag model is robust to the problem they pose, and can be used to assess policy
effects. The model takes the form
yt=ρ(L)yt+ψ(L)xt+φ(L)ut+εt(4)
whereytis the variable of interest (GDP and CPI Inflation in our case),xtis the policy variable such
as, e.g, spreads, in our case, andutdenotes exogenous series that might affectyt.ρ(L),ψ(L)and
φ(L)are lag polynomials needed to account for the dynamics of the overall data generation process.
All other endogenous variables are bypassed by the use of sufficiently long lag structures enabling the
use of this rather parsimonious ARDL model. In our case, we do not consider any exogenous variables
and end up with a model of the form
yt=ρ(L)yt+ψ(L)xt+εt(5)
Although we argue that policy interventions did not change the reduced-form empirical parameters
(as change would be consistent with the idea that unconventional policies had a permanent effect on
the economy), we feel that applying Pesaran and Smith’s suggested model provides a useful robustness
check to our benchmark BVAR model.
3.3 Data
Our data set comprises 44 variables, with monthly observations covering January 1991 to February
2013. UK variables include those capturing real activity, prices, money, the yield curve and financial
markets.13 To incorporate potential international financial and economic linkages, we also include data
for real activity, prices and the policy rates for the United States and the euro area. We use log-levels
for the variables except those expressed in percentage terms. The list of variables are provided in
Appendix B.
3.4 Counterfactual analysis
Similar to Kapetanios et al. (2012), the analysis is carried out in two steps. In the first step, we
identify the effects of the unconventional policy on the variable of interestut,that is banks’ funding
costs for FLS and 5-year and 10-year maturity government bond yields for QE. By doing so we can
identify what the path ofutwould be without the policy intervention. This path is denoted byu~t.We
provide a detailed discussion below of howu~tis obtained but here only offer a ‘high-level’ description
of our methodology.
In the second step we useuT+Handu~T+Hto derive two sets of conditional forecasts denoted by
E(YT+H∣uT+H)andE(YT+H∣u~T+H),respectively. Finally, the effect of unconventional policies is
assessed by taking the difference between the two sets of forecasts
D(T+H∣uT+H,YT+H∣u~T+H)=E(YT+H∣uT+H)−E(YT+H∣u~T+H)(6)
The conditional forecasts are produced using the methodology developed by Waggoner and Zha (1999,
‘hard conditions’). In all counterfactual exercises we do not allow changes in the domestic economy
to have an effect on the foreign economy (small open economy assumptions). Furthermore, when we
measure the economic impact of FLS we control for QE effects and vice versa.
13We obtain monthly GDP estimates from the National Institute of Economic and Social Research. Mitchell et al. (2005) discuss the methodology in detail.
4 The effects of the Funding for Lending Scheme
This section explains how we assess the macroeconomic effects of FLS and also discusses our empirical
results.
4.1 Estimating the impact of FLS on funding costs
In the spirit of Kapetanios et al. (2012), we need a way of estimating the impact of FLS on banks’
marginal funding costs. But this is not simple, for at least three important reasons. First, even without
FLS there is no single perfect measure of the marginal funding cost for a bank. Banks have a variety
of different funding options, with different headline interest rates, but also different indirect costs
such as fees, costs of collateral usage, and associated liquidity requirements. Assuming that banks
arbitrage between different funding sources such that their ultimate cost is similar, it is common to
look at the implied cost over time of issuing a new senior unsecured bond.14 Because there are low
indirect costs to such issuance the total funding cost can be proxied by the headline yield or spread
over a benchmark reference rate. The two most common proxies are the spreads on debt trading in the
secondary market and the Credit Default Swaps (CDS) referenced to such debt. Secondary market
debt is attractive because it is closest to the instrument that would be issued. But CDS are attractive
when a consistent constant horizon time series is available, as tends to be the case for larger banks.
For this reason practitioners often prefer secondary market bonds, whereas academic papers often use
CDS. We avoid taking a strong view by producing estimates based on both in what follows.
A second issue is the more familiar one of identification. The timing over which FLS should impact
on market funding costs is not clear a priori, so while there was an immediate response following the
announcement of FLS, it is not at all obvious that we will capture all of the impact through a one or
two day event study window, particularly when the details of the scheme were not known. But when
looking over a longer period moves in funding costs are likely to be contaminated by other influences.
Most notably, UK bank funding spreads were highly correlated with those of euro area banks over
this period, possibly because of concerns regarding the impact on their solvency of euro area breakup.
Less than three months after the announcement of FLS in June 2012 - and less than a month after the
FLS opened for drawings - Mario Draghi, the ECB president, gave his now famous ‘whatever it takes’
remarks, which led to a rally in European financial markets. For this reason we cannot rely on timing
alone but need to identify and abstract from any improvement in UK bank funding costs stemming
from an improvement in the outlook for the euro area. Our method for doing so is discussed below.
A third important issue is that, in addition to any impact on banks’ funding costs in the market,
the FLS delivers incentives to lend through the funding offered directly to participants. An exposition
of how the price and quantity incentives within FLS would affect a profit maximising bank is contained
in Churm et al. (2012). But because banks change loan prices for numerous unobservable reasons,
we have no good way to accurately identify these effects and test whether FLS participants changed
their behaviour as a result. We therefore do not include any ’direct effects’ of the FLS in this exercise.
We do know that banks drew around £42bn from the first phase of FLS however, consistent with it
lowering their funding costs. Further, we know from the Bank of England’s market contacts, Credit
Conditions Survey responses, and specific product announcements that access to FLS drawings played
a role in reducing the cost of loans. So for this reason the estimates we produce are biased downwards
and the beneficial impact of FLS overall is more likely to be larger.
14See also the discussion in Button et al. (2010).
Before explaining our method of identification it makes sense to summarise developments in UK
bank funding costs and those for euro area banks and sovereigns, over this period. UK Libor-OIS
spreads had risen in the second half of 2011 and remained elevated in 2012 (Figure 1). Libor rates
and spreads fell sharply on 15 June 2012, the morning after the Mansion House speeches where the
principle of the Funding for Lending Scheme was announced (see King (2012a)). In a speech Weale
(2013) shows that the next day fall in Libor futures was statistically significant at the 1% level. But
Libor-OIS spreads continued to fall during the rest of summer and autumn 2012, before flattening
out. From close of business (cob) 14 June 2012, to 31 December 2012, the sterling 3-month Libor OIS
spread fell from 55bps to 11bps (Table 2).
Figure 1: Libor-OIS spreads
0 20 40 60 80 100 120 140 160 180
Jan-11 Jul-11 Jan-12 Jul-12 Jan-13 Jul-13 Jan-14
bpsLibor-OIS spread (3 months)
Libor-OIS spread (12 months)
Intial FLS announcement
Table 2: Bank Spreads
FLS Draghi announcement ‘whatever it
takes’ speech
Instrument 31/12/11 14/06/12 25/07/12 30/09/12 31/12/12 24/02/2014
UK bank B6 average CDS 254.25 262.90 250.46 196.39 138.32 92.28
UK bank B6 average
Senior Unsecured 296.17 183.52 156.55 88.17 65.51 59.28
CDS + 3m Libor 362.26 361.90 326.36 256.08 189.82 144.46
3m Libor-OIS spread 58.76 55.25 36.15 21.44 10.75 144.46
There were also significant falls in spreads on UK banks’ senior unsecured debt - quoted over Libor
swap rates, so as to avoid any double counting with the Libor spreads discussed above - and CDS
premia (Figure 2). And following those with a lag, spreads on term retail deposits - an alternative
source of stable uncollateralised term funding also fell. A simple average of CDS for the largest 6 UK
banks fell from 263bps as of cob 14 June 2012, to 138bps at the end of the year (Table 2). And over
the same period senior unsecured bond spreads for the same six banks showed a fall from 184bps to
66bps.
The full details of FLS were announced when it was subsequently launched on 13 July 2012,
Figure 2: Indicative long-term bank funding spreads. Covered and senior unsecured bond spreads taken over swap rates.
-50
0
50
100
150
200
250
300
350
400
Jan 10 Jul 10 Jan 11 Jul 11 Jan 12 Jul 12 Jan 13 Jul 13 Jan 14
bpsFixed rate retail bond (average of 2 & 3yr spreads) 5yr CDS c.5yr covered bond c.5yr senior unsecured
Initial FLS announcement
with the scheme opening for drawdowns on 1 August, and the first drawdowns actually occurring in
September. For this reason it seems plausible that the impact of FLS on funding costs was not limited
to the immediate aftermath of 14 June. And the data are suggestive of a positive dynamic starting
at that point but continuing for a period. Importantly, there was a material fall in UK bank funding
spreads before Draghi’s ’whatever it takes’ speech on 26 August 2012, during which time euro area
bank spreads had on average changed little. But of course such a speech could have been anticipated
and conversely FLS could have had further impacts after 25 August; for example, if market yields fell
further in response to lower bank debt supply as specific issues matured and were not replaced.
One plausible method for identifying the impact of FLS was set out in a speech by King (2012b).
In this speech he simply noted that funding spreads on bank unsecured debt in the UK had fallen by
more than those in the US or in ’core’ European economies. Such an approach makes relatively strict
implicit assumptions, some of which we can relax. Notably, comparing levels of spreads implicitly
assumes that UK banks’ funding spreads should respond by an equal amount in basis points to euro
area news. Such assumptions, when carrying out this type of exercise, cannot be varied according
to the set of euro area countries considered ’core’ and implicitly comparable to the UK, or according
to the sample of banks chosen for each country. So while we find those early results plausible, we
consider an alternative method that might be more robust.
The philosophy behind our method is to predict how much UK banks’ funding costs ’should’ have
moved using regression analysis and the pre-FLS co-movement of UK bank spreads with developments
in the euro area. And we do this using data for as many related euro area funding costs as possible,
without making an a priori judgement about which country or banks UK bank spreads should be most
related to. More specifically, our method is as follows:
cipal component is a quantitative metric of the primary shock driving euro area spreads.
this on the metric of the euro area shock (first principal component) up to 14 June 2012.
residuals are an estimate of the change in UK banks’ CDS that is unexplained by the shock
driving euro area spreads. We produce forecasts out as far as the end of 2012.
The final stage is to assume that, because FLS was the major UK specific development over this
period, the change in funding spreads unexplained by the euro area shock is a reasonable estimate
of its impact. If other UK specific developments were thought to have played an important role in
increasing or decreasing UK bank’s funding costs over the period then our estimate will be biased,
but we feel that given the identification challenges ours is a reasonable starting point.
The results for the CDS-based measure are shown in Figures 3 and 4. The regression fits well over
the May 2010 to June 2012 period, suggesting that UK bank funding costs were largely driven by the
same shock driving euro area CDS during this period.16 Following the introduction of the FLS, in
July, a residual opens up, suggesting that something else reduced UK banks’ funding costs over that
period (blue line on Figure 4). We are aware that results based on a regression starting in May 2010,
while justified by our priors, would not be convincing if choosing other start dates resulted in very
different results. The swathe around our ‘preferred estimate’ on Figure 4 shows the resulting estimates
derived by choosing different start dates for the regression ranging from 1 January 2009 right up to
including only data in June 2012. The result that the euro area does not explain all of the falls in UK
banks’ CDS is, therefore, robust to different estimation periods.
Figure 3: B6 banks’ CDS and fitted value (bps)
### 135
### 185
### 235
### 285
### 335
### Actual Data Fitted Data
As we discussed earlier, senior unsecured bond spreads fell by more than CDS following the intro-
duction of FLS. We can apply the same methodology as above but this time using senior unsecured
15The major UK lenders are Banco Santander, Barclays, HSBC, Lloyds Banking Group, Nationwide and Royal Bank of Scotland and together they accounted for around 70% of the stock of lending to businesses, 45% of the stock of consumer credit, and 75% of the stock of mortgage lending at the end of December 2011. See Trends in Lending, July 2012 Bank of England (2012)
16The R-squared of the regression is 75% over this period. A natural interpretation is that this shock emanated in the euro area, and was related to the likelihood of very bad outcomes, but the method here simply demonstrates co-movement.
Figure 4: Estimate of the FLS effect on UK bank CDS
### -155
### -135
### -115
### -95
### -75
### -55
### -35
### -15
### 5
### 25
### 07/12 08/12 09/12 10/12 11/12 12/12 01/13 02/13 03/13
### Preferred Estimate Median
spreads as the proxy of UK banks’ funding costs. We might expect the impact on cash bonds to be
larger if there is imperfect arbitrage and the scheme affects liquidity or other premia specific to them.
The estimated effect on senior unsecured bonds is larger (75bps). However, the regression fit over the
preceding period is less good (Figure 5), suggesting bond specific factors were playing an important
role before the FLS, and these are not explained by movements in euro area CDS.
Figure 5: B6 banks’ senior unsecured bond spreads and fitted value (bps)
### 115
### 165
### 215
### 265
### 315
### Actual Data Fitted Data
4.2 The Impact of lower market funding costs on GDP and inflation
From the last exercise we have an estimate of the level of UK banks’ wholesale funding spreads
without the policy intervention and this is our counterfactual scenario. Our next step is to estimate
the large BVAR model over the period between01/2008and06/2012(FLS announcement month). The
estimated model is then used to forecast (from07/2012to02/2013)how the state of the economy would
have evolved without the policy stimulus (conditional on counterfactual spreads) and to derive agents’
projections about the future evolution of the economy once they are informed about the policy actions
(conditional on actual spreads). We then proceed to forecast further (03/2013-03/2014), without
conditioning on spreads but letting the model dynamics fully determine the forecast of all variables in
Figure 6: Estimate of the FLS effect on UK bank senior unsecured bond spreads
### -125
### -105
### -85
### -65
### -45
### -25
### -5
### 07/12 08/12 09/12 10/12 11/12 12/12 01/13 02/13 03/13
### Preferred Estimate Median
the model. The difference between the two forecasts offers a metric to assess the effectiveness of FLS.
Figure 7 illustrates the FLS effect on GDP and annual CPI inflation, using the CDS+3-month Libor
measure. The blue solid line denotes the pointwise posterior median while the 16%-84% posterior
percentiles are captured by the red dashed-dotted lines.
Figure 7: Estimate of the impact of FLS on the level of GDP and CPI inflation, based on its estimated impact on CDS
07/2012 03/2013 10/2013 03/2014
0
0.2
0.4
0.6
0.8
1
1.2
1.4
GDP−Level
Conditional Forecast Unconditional Forecast
07/2012 03/2013 10/2013 03/2014
−0.2
0
0.2
0.4
0.6
0.8
1
Annual−CPI−Inflation
Conditional Forecast Unconditional Forecast
Starting from Figure 7 we see the FLS impact on GDP is significant both in statistical and
economic terms. The effect is persistent and it takes more than a year to reach a peak of0.8As
banks’ funding costs fall, that lowers the effective interest rate for households and firms and boosts
consumption and investment. The lower cost of capital also implies higher profits for firms and this
increases asset prices, which further pushes up on GDP. These effects become even stronger if we
believe that households and firms are subject to collateral credit constraints.
Figure 8: Estimate of the impact of FLS on the level of GDP and CPI inflation, based on its estimated impact on senior unsecured bond spreads
07/2012 03/2013 10/2013 03/2014
0
1
2
3
4
5 GDP−Level
Conditional Forecast Unconditional Forecast
07/2012 03/2013 10/2013 03/2014
−0.5
0
0.5
1
1.5
2
2.5
3
Annual−CPI−Inflation
Conditional Forecast Unconditional Forecast
Inflation also increases as result of the FLS intervention. The increase reaches a peak of about 0.6
pp more than a year after the policy started. To understand what drives this results let us consider
a New Keynesian Philips Curve (see Christiano et al. (2005) and Smets and Wouters (2007) among
others) where inflation is function of the current and expected real marginal cost and the latter is a
weighted average of real wages and the return on capital. The introduction of FLS lowers the cost
of capital and puts downward pressure on marginal cost and inflation. However, as demand expands,
the demand for labour rises too putting upward pressure on real wages and inflation. Since real wages
are the largest component of marginal costs, the reduction of the cost of capital should eventually be
offset by the increase in wages.
As expected and can be seen from Figure 8, the effects are larger when the secondary market bond
spread proxy is used, given the larger estimate of the size of the shock. There is also a slight difference
because the model estimate of the impact of funding costs is slightly different, but the results are not
statistically different to scaling up the results from the CDS-based exercise for the larger estimated
shock.
4.3 ARDL robustness exercise
As has been discussed earlier, Pesaran and Smith (2014) argue that if the reduced form policy param-
eters are different after the policy intervention then our counterfactual exercise is not valid. To check
the robustness of our results, we apply their methodology, using the univariate model described by
equation (4).
The first task is to decide about the dynamic order of the univariate model, for which we use
the Hannan Quinn Information Criterion (HQIC, see Lutkepohl (2007)). For the GDP series, the
information criterion selects the model with four endogenous and two exogenous variable lags as the
best, while it chooses a significantly more parsimonious model for CPI (one lag for both endogenous
and exogenous variables). Both models are estimated using OLS for the same estimation period and
are used to produce conditional forecasts again for the same period.
Figure 9: Effects of FLS on GDP and CPI inflation based on its estimated impact on CDS and using ARDL model
07/2012 03/2013 10/2013 03/2014
0
0.2
0.4
0.6
0.8
1
GDP−Level
Conditional Forecast Unconditional Forecast
07/2012 03/2013 10/2013 03/2014 −0.1
0
0.1
0.2
0.3
Annual−CPI−Inflation
Conditional Forecast Unconditional Forecast
From Figure 9, it appears that the ARDL analysis supports the BVAR results reported earlier.
As predicted by the BVAR analysis, FLS has a positive effect on demand and prices. Although it can
be argued that the effects obtained using the ARDL appear to be somewhat smaller they are equally
persistent.
5 The effects of Quantitative Easing 2
5.1 The impact of QE2 on yield spreads
In order to estimate the impact of QE2 on the macroeconomy, our analysis again broadly follows
the approach used by Kapetanios et al. (2012), where the counterfactual simulations presented are
derived on the assumption that the main impact from QE comes from its effects on government bond
spreads.17 In order to quantify this initial yield impact, Kapetanios et al. (2012) use the event study
evidence reported in Joyce et al. (2011a), which suggested the impact on 5-25 year gilt yields from
the Bank’s first round of asset purchases summed to about 100 basis points during March 2009 to
January 2010.
Table 3 repeats a similar exercise for 5 and 10-year gilt yields showing the announcement reactions
over both 1 and 2 day windows and also extending the dataset to include the policy announcements
associated with QE2. Summing over the QE1 events using the longer 2-day window preferred by Joyce
et al. (2011a) suggests that overall 5-year yields fell by around 55 basis points and 10-year yields fell
by 80 basis points. The reactions to the QE2 announcements are much smaller, however, particularly
17Given the reduced form nature of the models used, the study does not attempt to identify the precise transmission channels involved, though the main transmission channels were assumed to be through portfolio balancing and signalling.
T ab
le 3:
R ea
ct io
n of
gi lt
y ie
ld s
to Q
E 1
an d
Q E
2 an
n o u
n ce
m en
ts
E ve
n t
D at
e 5-
ye a r
y ie
ld 1 0 -y
ea r
y ie
ld
1-d
ay ch
an g e
2 -d
ay ch
a n
g e
1 -d
ay ch
a n
g e
2 -d
ay ch
a n
g e
1. F
eb ru
ar y
20 09
In fl
at io
n R
ep or
t an
d as
so ci
at ed
p re
ss co
n fe
re n
ce in
d i-
ca te
s Q
E li
ke ly
11 .2
.2 00
9 -1
1 -2
6 -1
3 -2
7
2. M
P C
an n
ou n
ce s £
75 b
il li
on of
as se
t p
u rc
h as
es 5.
3. 20
09 -1
8 -3
4 -3
2 -6
8 3.
M P
C an
n ou
n ce
s £
50 b
il li
on ex
te n
si on
of p
ro gr
am m
e 7.
5. 20
09 5
9 6
1 0
4. M
P C
an n
ou n
ce s
fu rt
h er
ex te
n si
on of
£ 50
b il
li on
, as
w el
l as
ex te
n si
on of
b u
y in
g ra
n ge
6. 8.
20 09
-1 1
-4 -7
-3
5. G
D P
re le
as e
fo r
20 09
Q 3
su gg
es ts
m or
e Q
E li
ke ly
23 .1
0. 20
09 -5
-3 -4
-1 6.
M P
C an
n ou
n ce
s fu
rt h
er £
25 b
il li
on of
p u
rc h
as es
5. 11
.2 00
9 4
4 7
1 0
7. M
P C
d ec
is io
n to
re su
m e
p u
rc h
as es
, w
it h
ad d
it io
n al
£ 75
b il
li on
6. 10
.2 01
1 3
7 4
1 2
8. M
P C
an n
ou n
ce s
fu rt
h er
£ 50
b il
li on
of p
u rc
h as
es 9.
2. 20
12 -1
-1 3
5 -5
9. M
P C
an n
ou n
ce s
fu rt
h er
£ 50
b il
li on
of p
u rc
h as
es 5.
7. 20
12 -1
0 -1
5 -6
-1 1
Q E
1 ev
en ts
(1 )-
(6 )
-3 6
-5 4
-4 4
-8 0
Q E
2 ev
en ts
(7 )-
(9 )
-8 -2
1 4
-4 T
ot al
al l
ev en
ts -4
3 -7
5 -4
0 -8
4
N ot
es :
P ar
t of
th e
fa ll
in y ie
ld s
fo ll
ow in
g th
e F
eb ru
a ry
20 09
an n
ou n ce
m en
t m
ay h
av e
re fl
ec te
d th
e m
ar ke
t’ s
gr ea
te r
ce rt
ai n ty
th at
th er
e w
ou ld
b e
a B
a n
k R
a te
cu t
in M
ar ch
20 09
. T
h e
fi gu
re s
re p
or te
d in
p ar
en th
es es
a re
ad ju
st ed
to ta
ke ac
co u
n t
of th
is eff
ec t:
sp ot
ra te
s fo
r 12
F eb
ru ar
y w
er e
re ca
lc u
la te
d w
it h
25 b
as is
p o in
ts su
b tr
a ct
ed fr
om th
e u
n d er
ly in
g in
st an
ta n
eo u
s fo
rw ar
d ra
te s
b et
w ee
n ze
ro an
d fi
v e
ye ar
s on
a sl
id in
g sc
al e,
as in
J oy
ce et
al .
(2 01
1a ).
for longer maturities. In considering the impact of later purchases and particularly QE2, there are
reasons for thinking that event study methods might be less useful, as financial markets may have
become more familiar with the use of QE (i.e. the Bank’s reaction function) and therefore been better
able to anticipate its use (as discussed in Joyce et al. (2012a)). At the same time there are reasons why
it may not be appropriate to quantify QE2 on the basis of QE1 event studies, as the importance of
some of the channels through which QE works may have been weaker in QE2 relative to QE1 (eg any
impact through signalling might plausibly have been greater when the new policy was first announced
than when it was extended). We therefore examine several methods, in order to derive a plausible
estimate for the yield curve impact.
Figures 10 and 11 illustrate the 2-day reactions of 5-year and 10-year gilt yields (estimated zero
coupon spot rates) to the news about total QE purchases following various QE announcements and
the 2009 Q3 GDP release, where news is calculated using the Reuters survey of economists.18 For
both 5 and 10-year yields, the responses to the QE1 announcements all fall fairly close to the solid
regression line which represents the line of best fit through them, although they are dominated by
the initial impact of QE (which is represented by the dot in the bottom right of each chart, which
combines the yield reaction of February and March 2009 (see Joyce et al. (2011a))). For two of the QE2
announcements, the size of the implied news is quite small, but the gilt yield reaction is slightly larger,
particularly for 5-year yields. The first QE2 announcement in October 2011 stands out, however, in
implying a fairly large change in QE news accompanied a rise rather than a fall in yields.19 There are
reasons for not taking this announcement reaction at face value, as there was a change to the survey
question used to calculate QE news in this month and there was a significant amount of international
news at the same time. Joyce et al. (2012a) report that gilt yields rose by less than international
yields on the same day. Nevertheless, overall the yield reaction to news about QE2 does seem weaker
for the later purchases.
To the extent that a weaker impact might be the consequence of additional QE being anticipated
by the markets, it may be more relevant to examine the market reaction to macro news that might have
signalled the likely use of the policy. Goodhart and Ashworth (2012) find that 5-25 year yields actually
rose in aggregate over the seven MPC announcements they examine during the QE2 period, and even
when they include the yield reaction following the Purchasing Manager’s Index (PMI) manufacturing
and services at the beginning of September they find a modest negative impact of about 20 basis
points. However, their analysis excludes the impact of the August 2011 Inflation Report, which they
argue caused yields to fall for reasons unrelated to QE, and the £50 billion extension of QE that was
announced in July 2012, which occurred after their paper was written. In Table 4, we tabulate the
1-day and 2-day reactions of 5-year and 10-year gilt yields to all these events. Like Goodhart and
Ashworth (2012), we find that the seven monetary policy events they focus on accompanied a small
rise in yields overall, but including the other events leads to a larger and negative impact up to 55
basis points. Even so, the estimated impact is still rather less than proportionate to the impact of QE1
and, of course, the choice of these events can be questioned. A couple of other studies have attempted
to look at these issues in different ways. Butt et al. (2012) look at the comparative effects of QE2
18The details on the construction of this chart are explained in Joyce et al. (2011a) and Joyce et al. (2012a). The difference from these papers is that we show the reaction of 5 year and 10-year gilt yields, rather than the 5-25 year yield. We use the 5 and 10-year yields, as these are the yields that feed into the spreads used in the BVAR model we report later.
19An article by Chris Giles in the Financial Times on the day following the announcement (‘QE2: Old Lady delivers shock and awe’, 7 October 2011) has the byline “Few anticipated the scale of the Bank of England’s decisive move to tackle weak growth”.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQGMnZrJPe85gFYM06PTSVYMhbu0MEVE1IxecbiXpzw0hDk7_Pg0GD7kk4uwtwYYZmwOgLrSfjU5rgKgJAC1KUoB1F2MLPZiwwMTuAPtfGqRivYaNrm5ur-RIwtJoxeFEc6qaxOVHg=w1280-h768-v0?authuser=1)

![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQGCQmNjKCN0IfmBAYExqtABMgxo-nARL1ivVIFpRNuRKRKjmuxL8v9ZV-uTPS304_kLPagyTyDFjMZwXGwrgUB_GiZAif7VuMN5vOKGjxvGUG7igixiTPt9et7PdbXgcvX-3we2KA=w1280-h815-v0?authuser=1)

Figure 10: The 2-day reaction of 5-year gilt yields to QE news. Least squares regression line based on QE1 observations
Figure 11: The 2-day reaction of 10-year gilt yields to QE news. Least squares regression line based on QE1 observations
Table 4: Reaction of gilt yields to wider set of QE 2 policy and macro announcements
Event Date 5-year yield 10-year yield
1-day change 2-day change 1-day change 2-day change
1. Aug 2011 Inflation Report 10.8.2011 -22 -20 -21 -21 2. PMI manufacturing survey for August 2011
1.9.2011 -8 -15 -8 -17
3. PMI services survey for August 2011
5.9.2011 -13 -11 -15 -16
4. MPC minutes 21.9.2011 1 0 2 -7 5. MPC decision, £75bn 6.10.2011 3 7 4 12 6. BoE inflation report 16.11.2011 2 10 2 9
7. MPC decision £50bn 9.2.2012 -1 -12 5 -5
8. MPC minutes 21.3.2012 -2 -5 -6 -11
9. MPC minutes 18.4.2012 6 9 4 6
10. MPC decision 10.5.2012 7 3 8 7 11. MPC decision, £50bn 5.7.2012 -10 -15 -6 -11
Total (4)-(10) 16 12 20 11 Total (2)-(10) -4 -14 -3 -22
Total all QE2 events -36 -49 -30 -54
Notes: The events (4)-(10) correspond to the 7 policy announcements reported in Table 10 of Goodhart and Ashworth (2012). The events (2)-(10) include the reactions to the PMI surveys they also cite, but exclude reaction to the August 2011 Inflation Report.
and QE1 on broad money and find the effects have been broadly proportionate, although the precise
transmission channels seem to have been different. McLaren et al. (2014) look instead at the reaction
of gilt yields to shocks to the distribution of QE purchases across the term structure associated with
various operational changes in the QE programme spanning across QE1 and QE2. They find the
impact of local supply surprises had a similar impact across the events they examine, suggesting that
the strength of this channel (part of the portfolio balance effect) has not changed significantly over
time, but they also find it only accounts for only about half the estimated effect of QE on gilt yields.
As an alternative approach, and mirroring the earlier analysis of banks’ CDS discussed in the
section on the FLS, we can also compare the behaviour of UK yields over the QE2 period with
what might have been expected given their normal relationship with international yields. In order to
construct this counterfactual, we first carried out a principal component analysis using daily data on
5-year and 10-year benchmark yields for 11 and 13 different countries respectively over the period from
April 1999 to March 2013.20 The first two principal components explain over 90% of the variation
in the 5 and 10 year yield data, with the first principal component alone accounting for more than
80% of the variance of yields in each case. We then regressed UK 5-year and 10-year spot yields on
the first two principal components over a sample preceding the start of the global financial crisis (up
to the end of March 2008). There is clearly a large amount of comovement between UK yields and
international yields, with this simple regression having an adjusted R-squared of more than 75% for
both 5 and 10 year maturities. Finally, we used this historical relationship between UK yields and
international yields to forecast the behaviour of UK yields over the global crisis period. The results
from this exercise are shown in Figures 12 and 13, where the shaded areas show the QE1 and QE2
periods, where the start of each period is defined by the first official MPC QE announcement and
20The 13 countries included in the 10-year yield analysis were Australia, Belgium, Canada, Finland, France, Germany, Japan, Netherlands, New Zealand, Norway, Sweden, Switzerland, United States. Dropping the United States from the set of countries had little effect on the results. For the 5-year yield, we dropped Denmark and Finland because of lack of available data over parts of the sample period.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQFa6TllR3bgx9onwLfaraER34UPtBkl3gsRUN32tyswSAfHXVv8zkKFZVpNRs8lyAz30O5KdJrNiArjc176QYEYu4oas0vXQSJjVwukMcua9yP8nXLzykpj2VwP8IicftWkUN2Zaw=w1280-h768-v0?authuser=1)

Figure 12: 5-year gilt yields vs predicted values based on international yield correlations (%)
the end of each period coincides with the day of the last reverse gilt auction. Although the principal
components regressions explain the past behaviour of UK yields well, they overpredict them during
the crisis period. During the QE2 period, the underprediction of 5-year and 10-year yields increases
by 10 basis points and more than 30 basis points respectively from the day before the first QE2
announcement to the day of the third announcement on 5 July 2012 (if it is assumed that QE2 was
anticipated and we take a longer window back to the 1 September the increase is of the order of 12 basis
points and 55 basis points respectively). Of course, there were other factors driving UK yields over
this period, including safe-haven flows into gilts associated with the euro area sovereign debt crisis, but
it is nonetheless striking that UK yields were depressed by a significant order of magnitude relative to
the counterfactual based on the behaviour of international yields. Nevertheless, the estimated effects
are still considerably smaller than the event study based ones for QE1.
These various approaches to calibrating the impact of QE2 are summarised in Table 5 alongside
their caveats. Overall the balance of the estimates suggests that QE2 had a smaller impact than the
previously estimated impact of QE1. Given the uncertainties surrounding the individual estimates,
for the purposes of the simulations we assumed that the impact on 5 and 10 year yields of QE2 was
45 basis points. This figure is broadly in line with the reactions of gilt yields reported in Table 4.
5.2 Macroeconomic effects of QE2
The steps taken to infer the real economy effects of QE2 are similar to those discussed in Section 4.2.
To be precise, the BVAR model is estimated over the period between01/2008and01/2012and used
to forecast (from02/2012to02/2013)how the state of the economy would have evolved with and
without the stimulus. We model the stimulus by assuming that spreads were 45 basis points lower
under QE during October 2011 to October 2012.
Figure 14 illustrates the effects of QE2 on GDP and annual inflation under the scenario that the
yield spread was reduced by 45bps. The exercises suggest QE2 had a significant effect on demand.
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEcf9-MOx1wJGYBzibuDMfZkExl9yq9HZEEUuJzvPWvS-pa4pkhjgz77KfMJ7do-hKJr1b2f_Dzgav4Pz-Q-hhOA81Y4zE5fazYlhsK8CoGceFj2uDvMUeL-LL9Amw9c8SlOib1=w1280-h768-v0?authuser=1)

Figure 13: 10-year gilt yields vs predicted values based on international yield correlations (%)
GDP rises 0.6 % by the end of the period under consideration. The inflation response has an inverted
U shape, and is initially increasingly positive and significant, peaking at 0.6 pp. Then, it declines to
about 0.25pp. These estimates can be contrasted with the findings of Kapetanios et al. (2012), where
QE1 was found to have had a positive impact on GDP of about 1.5% and to inflation of about 1.25pp.
Given our finding that QE2 had a smaller effect on spreads compared to QE1, these differences appear
intuitive.
We also carry out an ARDL analysis whose results are reported in figure 15. This analysis delivers
qualitatively similar estimates, thereby suggesting that the counterfactual analysis undertaken in this
section is not subject to the problems discussed in Pesaran and Smith (2014).
6 Conclusion
In this paper we provide new results on the potential macroeconomic effects of two key unconventional
monetary policies pursued by the Bank of England after the 2008 financial crisis. Our analysis is
structured in two steps. Firstly, we use both existing and new approaches to determine the effect of
the unconventional policies on relevant financial variables, such as spreads and bank funding costs.
Secondly, we use two econometric models to map out the effect changes in these financial variables
had on the macroeconomy. The use of BVAR and ARDL models provides a useful cross-check for our
empirical analysis, especially since the two models have different characteristics and motivations and
use different data.
Starting with FLS we have documented the scheme’s effect on bank wholesale funding spreads and
considered the effect this drop in spreads had on GDP growth and inflation. In particular, we find a
positive peak effect of 0.8 % on GDP and 0.6 pp on inflation more than a year after the start of the
policy. For QE2 we find a significant positive effect for GDP growth of about 0.6 % and a significant
positive effect on inflation that has an inverted U shape.
Figure 14: Effects of QE2 on GDP and CPI Inflation using BVAR model
10/11 01/12 04/12 07/12 10/12 01/13 04/13 07/13 10/13 0
0.2
0.4
0.6
0.8
1 GDP−Level
Conditional Forecast Unconditional Forecast
10/11 01/12 04/12 07/12 10/12 01/13 04/13 07/13 10/13
−0.2
0
0.2
0.4
0.6
0.8
1
Annual−CPI−Inflation
Conditional Forecast Unconditional Forecast
Finally, it is appropriate to qualify our analysis and results by noting several caveats. First, the
relative uniqueness of the two policy interventions and the economic environment in which they took
place means that our efforts to model their impact are obviously uncertain. This is compounded by the
fact that we have estimated our models using relatively small samples, in order to account for potential
parameter time-variation associated with structural change. Second, we have focused exclusively on
what we consider the main channels from the unconventional policies to the macroeconomic variables of
interest, ignoring other possible transmission channels that can be less well approximated through our
models. Despite these caveats, we believe our modelling approach represents a reasonable compromise,
given the inevitable constraints of any such counterfactual analysis, and that it provides a useful
estimate of the overall macroeconomic impact of QE2 and the FLS.
Figure 15: Effects of QE2 on GDP and CPI Inflation using ARDL model
02/2012 10/2012 05/2013 10/2013 −0.2
0
0.2
0.4
0.6
0.8
GDP−Level
Conditional Forecast Unconditional Forecast
02/2012 10/2012 05/2013 10/2013 −0.2
0
0.2
0.4
0.6
Annual−CPI−Inflation
Conditional Forecast Unconditional Forecast
T ab
le 5:
Im p
ac t
of Q
E 2
on 10
-y ea
r gi
lt y ie
ld s
M et
h o d
S ou
rc e
Im p
a ct
C av
ea ts
E x tr
ap ol
at io
n fr
om Q
E 1
ev en
t st
u d
ie s
J oy
ce et
al .
(2 01
1a )
J oy
ce an
d T
on g
(2 01
2)
O n
5-y ea
r y ie
ld s:
-5 0
b p
O n
10 -y
ea r
y ie
ld s:
-7 0
b p
R el
ie s
o n
Q E
1 ev
id en
ce (2
-d ay
w in
-d
ow )
o n
ly
E ve
n t
st u
d y
an al
y si
s of
Q E
2 G
o o d
h ar
t an
d A
sh w
or th
(2 01
2) ex
te n
d ed
to ot
h er
ev en
ts
O n
5-y ea
r y ie
ld s:
-2 9
to -4
9 b
p O
n 10
-y ea
r y ie
ld s:
-3 3
to -5
4 b
p (l
ow er
es ti
m at
e ex
cl u
d es
im p
a ct
o f
A u
gu st
20 11
IR )
S el
ec ti
o n
o f
ev en
ts is
sl ig
h tl
y a rb
i-tr
a ry
Im p
ac t
on m
on et
ar y
ag gr
eg at
es B
u tt
et al
. (2
01 2)
S im
il ar
p ro
p or
ti o n
a te
ly to
Q E
1 A
ss u
m es
a st
ra ig
h tf
o rw
a rd
eq u
iv -
a le
n ce
b et
w ee
n th
e m
o n
et a ry
a n
d y ie
ld cu
rv e
im p
a ct
s
A n
al y si
s b
as ed
on ch
an ge
s in
p u
r-ch
as es
ra n
ge s
d u
ri n
g Q
E 1
an d
Q E
2 M
cL ar
en et
al .
(2 01
4) S
tr en
gt h
of lo
ca l su
p p
ly eff
ec ts
si m
i-la
r, 40
-6 0%
of to
ta l im
p a ct
o n
y ie
ld s
F o cu
se s
o n
ly o n
lo ca
l su
p p
ly ch
a n
-n
el so
m ay
u n
d er
es ti
m a te
th e
to ta
l eff
ec ts
E v id
en ce
fr om
p ri
n ci
p al
co m
p on
en t
m o d
el of
in te
rn at
io n
al y ie
ld s
T h
is p
ap er
O n
5-y ea
r y ie
ld s:
-1 0
to -1
2 b
p O
n 10
-y ea
r y ie
ld s:
-3 0
to -5
5 b
p M
o d
el ig
n o re
s o th
er fa
ct o rs
th a n
in -
te rn
a ti
o n
a l
y ie
ld s
References
Andres, J., J. D. Lopez-Salido, and E. Nelson (2004): “Tobin’s imperfect asset substitution in
optimizing general equilibrium,” Journal of Money, Credit, and Banking, 36, 665–90.
Bandbura, M., D. Giannone, and L. Reichlin (2010): “Large Bayesian vector auto regressions,”
Journal of Applied Econometrics, 25, 71–92.
Bank of England (2012): “Trends in Lending,” Bank of England.
Baumeister, C. and L. Benati (2013): “Unconventional Monetary Policy and the Great Reces-
sion: Estimating the Macroeconomic Effects of a Spread Compression at the Zero Lower Bound,”
International Journal of Central Banking, 9, 165–212.
Bauwens, L., M. Lubrano, and J. F. Richard (1999): Bayesian Inference in Dynamic Econo-
metric Models, Oxford: Oxford University Press.
Bean, C. (2011): “Lessons on Unconventional Monetary Policy from the United Kingdom,” Speech
by Charles Bean given at the US Monetary Policy Forum, New York, 25 February.
Benford, J., S. Berry, K. Nikolov, M. Robson, and C. Young (2009): “Quantitative Easing,”
Bank of England Quarterly Bulletin.
Bernanke, B. S. and V. R. Reinhart (2004): “Conducting Monetary Policy at Very Low Short-
Term Interest Rates,” American Economic Review, 94, 85–90.
Bini Smaghi, L. (2009): “Conventional and unconventional monetary policy,” Keynote lecture by
Mr Lorenzo Bini Smaghi, Member of the Executive Board of the European Central Bank, at the
International Center for Monetary and Banking Studies (ICMB), Geneva, 28 April 2009.
Breedon, F., J. S. Chadha, and A. Waters (2012): “The financial market impact of UK quan-
titative easing,” Oxford Review of Economic Policy, 28, 702–728.
Bridges, J. and R. Thomas (2012): “The impact of QE on the UK economy some supportive
monetarist arithmetic,” Bank of England working papers 442, Bank of England.
Brunner, K. and A. Meltzer (1973): “Mr. Hicks and the ‘Monetarists’,” Economica, 40, 44–59.
Butt, N., R. Churm, M. McMahon, A. Morotz, and J. Schanz (2014): “QE and the bank
lending channel in the United Kingdom,” Bank of England Working Paper.
Butt, N., S. Domit, M. McLeay, R. Thomas, and L. Kirkham (2012): “What can the money
data tell us about the impact of QE?” Bank of England Quarterly Bulletin, 52, 321–331.
Button, R., S. Pezzini, and N. Rossiter (2010): “Understanding the price of new lending to
households,” Bank of England Quarterly Bulletin, 50.
Carriero, A., G. Kapetanios, and M. Marcellino (2011): “Forecasting large datasets with
Bayesian reduced rank multivariate models,” Journal of Applied Econometrics, 26, 735–761.
Chen, H., V. Curdia, and A. Ferrero (2012): “The Macroeconomic Effects of Large-scale Asset
Purchase Programmes,” Economic Journal, 122, F289–F315.
Christiano, L., M. Eichenbaum, and C. Evans (2005): “Nominal Rigidities and the Dynamic
Effects of a shock to Monetary Policy,” Journal of Political Economy, 113, 1–45.
Churm, R., A. Radia, J. Leake, S. Srinivasan, and R. Whisker (2012): “The Funding for
Lending Scheme,” Bank of England Quarterly Bulletin, 52, 306–320.
D’Amico, S., W. English, D. Lopez-Salido, and E. Nelson (2012): “The Federal Reserve’s
Large-scale Asset Purchase Programmes: Rationale and Effects,” Economic Journal, 122, F415–
F446.
D’Amico, S. and T. King (2013): “Flow and Stock Effects of Large-Scale Treasury Purchases:
Evidence on the Importance of Local Supply,” Journal of Financial Economics, 108, 425–448.
Eser, F. and B. Schwaab (2013): “Assessing asset purchases within the ECBs Securities Markets
Programme,” ECB Working paper.
Gagnon, J., M. Raskin, J. Remache, and B. Sack (2011): “The Financial Market Effects of the
Federal Reserve’s Large-Scale Asset Purchases,” International Journal of Central Banking, 7, 3–43.
Giannone, D., M. Lenza, H. Pill, and L. Reichlin (2012): “The ECB and the Interbank
Market,” Economic Journal, 122, F467–F486.
Goodhart, C. A. E. and J. P. Ashworth (2012): “QE: a successful start may be running into
diminishing returns,” Oxford Review of Economic Policy, 28, 640–670.
Joyce, M. A. S., A. Lasaosa, I. Stevens, and M. Tong (2011a): “The Financial Market Impact
of Quantitative Easing in the United Kingdom,” International Journal of Central Banking, 7, 113–
161.
Joyce, M. A. S., N. McLaren, and G. Young (2012a): “Quantitative easing in the United
Kingdom: evidence from financial markets on QE1 and QE2,” Oxford Review of Economic Policy,
28.
Joyce, M. A. S., D. Miles, A. Scott, and D. Vayanos (2012b): “Quantitative Easing and
Unconventional Monetary Policy an Introduction,” Economic Journal, 122, F271–F288.
Joyce, M. A. S. and M. Tong (2012): “QE and the Gilt Market: a Disaggregated Analysis,”
Economic Journal, 122, F348–F384.
Joyce, M. A. S., M. Tong, and R. Woods (2011b): “The United Kingdoms quantitative easing
policy: design, operation and impact,” Bank of England Quarterly Bulletin, 51, 200–212.
Kapetanios, G., H. Mumtaz, I. Stevens, and K. Theodoridis (2012): “Assessing the Economy-
wide Effects of Quantitative Easing,” Economic Journal, 122, F316–F347.
King, M. A. (2009): “Speech by Mervyn King,” Speech given at the CBI Dinner, Nottingham, at the
East Midlands Conference Centre, 20 January 2009.
——— (2012a): “Speech by Mervyn King,” Speech given at the Lord Mayors Banquet for Bankers
and Merchants of the City of London at the Mansion House, 14 June 2012.
——— (2012b): “Speech by Mervyn King,” Speech given at South Wales Chamber of Commerce at
The Millennium Centre, Cardiff 23 October 2012.
Koop, G. (2011): “Forecasting with Medium and Large Bayesian VARs,” Journal of Applied Econo-
metrics, 1099–1255.
Krishnamurthy, A. and A. Vissing-Jorgensen (2011): “The Effects of Quantitative Easing on
Interest Rates: Channels and Implications for Policy,” Brookings Papers on Economic Activity, 43,
215–287.
Lenza, M., H. Pill, and L. Reichlin (2010): “Monetary policy in exceptional times,” Economic
Policy, 25, 295–339.
Litterman, R. (1986): “Forecasting with Bayesian Vector Autoregressions - Five Years of Experi-
ence,” Journal of Business and Economic Statistics, 4, 25–38.
Lutkepohl, H. (2007): New introduction to multiple time series analysis, New York: Springer
Publishing Company, Incorporated.
McLaren, N., R. N. Banerjee, , and D. Latto (2014): “Using Changes in Auction Maturity
Sectors to Help Identify the Impact of QE on Gilt Yields,” The Economic Journal, 124, 453–479.
Mitchell, J., R. J. Smith, M. R. Weale, S. Wright, and E. L. Salazar (2005): “An Indicator
of Monthly GDP and an Early Estimate of Quarterly GDP Growth,” Economic Journal, 115, F108–
F129.
Mumtaz, H. and F. Zanetti (2012): “Neutral Technology Shocks And The Dynamics Of Labor
Input: Results From An Agnostic Identification,” International Economic Review, 53, 235–254.
Pesaran, H. and R. Smith (2014): “Counterfactual Analysis in Macroeconometrics: An Empirical
Investigation into the Effects of Quantitative Easing,” Working Paper in Economics and Finance
1406, Birkbeck College.
Sims, C. (1980): “Macroeconomics and Reality,” Econometrica, 48, 1–48.
Smets, F. and R. Wouters (2007): “Shocks and Frictions in US Business Cycles: a Bayesian DSGE
Approach,” American Economic Review, 97, 586–606.
Tobin, J. (1963): “Commercial Banks as Creators of Money,” in Banking and Monetary Studies, ed.
by D. Carson, Richard D. Irwin.
Trichet, J. C. (2013): “Central Banking in the Crisis - Conceptual Convergence and Open Questions
on Unconventional Monetary Policy,” 2013 Per Jacobsson Lecture.
Waggoner, D. F. and T. Zha (1999): “Conditional Forecasts In Dynamic Multivariate Models,”
The Review of Economics and Statistics, 81, 639–651.
Weale, M. (2013): “Forward Guidance and its Effects,” Speech given at National Institute of Eco-
nomic and Social Research, London Wednesday 11 December 2013.
A Estimation of BVAR model
In what follows we briefly discuss the estimation of the large BVAR described in Section 3. We can
compactly rewrite the VAR as:
Y=XhΨh+E,(7)
where Y=[yh+1,..,yT]′ is aT×Nmatrix containing all the data points inyt,Xh=[1 Y−h] is aT×Mmatrix containing a vector of ones (1) in the first columns and theh−thlag of Y in the remaining
columns,Ψh=[Φ0,hΦ1,h]′is aM×Nmatrix, andE=[εh+1,..,εT]′ is aT×Nmatrix of disturbances.
As only one lag is considered we haveM=N+ 1. The prior distribution can then be written as:
Ψh∣Σ∼N(Ψ0,Σ⊗Ω0),Σ∼IW(v0,S0).(8)
Note thatΨh∣Σis a matric-variate normal distribution where the prior expectationE[Ψh]=Ψ0and
prior varianceVar[Ψh]=Σ⊗Ω0are set according to equation (3). The prior variance matrix has a
Kronecker structureVar[Ψh]=Σ⊗Ω0whereΣis the variance matrix of the disturbances and the
elements of Ω0 are given byVar[Φ(ij)1,h] in (3). Since the normal-inverted Wishart prior is conjugate,
the conditional posterior distribution of this model is also normal-inverted Wishart
Ψh∣Σ,Y∼N(Ψˉ,Σ⊗Ωˉ),Σ∣Y∼IW(vˉ,Sˉ),(9)
where the bar denotes that the parameters are those of the posterior distribution. DefiningΨ^and
Ê as the OLS estimates, we have thatΨˉ= (Ω−10 + X′X)−1(Ω−10Ψ0+ X′Y), Ω̄ = (Ω−10 + X′X)−1, v̄
=v0+T, and S̄ =Ψ^′X′XΨ^+Ψ′0Ω−10Ψ0+Ψ0+ Ê′Ê−Ψ^′Ωˉ−1Ψ^.
In order to perform inference and forecasting one needs the full joint posterior distribution and
the marginal distributions of the parametersΨˉandΣ.One could use the conditional posteriors in
(9) as a basis of a Gibbs sampling algorithm that drawing in turn from the conditionalsΨh∣Σ,Yand
Σ∣Ywould eventually produce a sequence of draws from the joint posteriorΨhΣ∣Yand the marginal
posteriorsΨh∣Y,Σ∣Y,as well as the posterior distribution of any function of these coefficients (for
example, multi-step forecasts or impulse responses).
Still, if one is interested only in the posterior distribution ofΨh(rather than in any non-linear
function of it) there is an alternative to simulation: by integrating outΣfrom (9). It can be shown
that the marginal posterior distribution ofΨhis a matric-variatet:
Ψh∣Y∼MT(Ψˉ,Ωˉ−1,Sˉ,vˉ).(10)
The expected value for this distribution is given by:
Ψˉ= (Ω−10 + X′X)−1(Ω−10Ψ0+X′Y),(11)
which is obviously extremely fast to compute. Recalling thatΨ^is the OLS estimator, and using the
normal equations(X′X)−1Ψ^= X′Y we can rewrite this as:
Ψˉ= (Ω−10 + X′X)−1(Ω−10Ψ0+X′XΨ^),(12)
which shows that the posterior mean ofΨhis a weighted average of the OLS estimator and of the
prior meanΨ0,with weights proportional to the inverse of their respective variances. In the presence
of a tight prior (ie, whenθ→0) the posterior estimate will collapse toΨˉ=Ψ0,while with a diffuse
prior (ie, whenθ→∞)the posterior estimate will collapse to the unrestricted OLS estimate.
Given the posterior meanΨˉ=[Φˉ0,hΦˉ1,h]′,it is straightforward to produce forecasts up tohsteps
ahead simply by setting:
y^​t+h=Φˉ0,h+Φˉ1,hyt,(13)
As shown by Bandbura et al. (2010) it is also possible to implement the prior described above using
a set of dummy observations. Consider addingTddummy observations Yd and Xd such that their
moments coincide with the prior moments:Ψ0= (X′dXd)−1X′dYd, Ω0 = (X′dXd)−1, v0 =Td−M−N−1,S0 = (Yd−XdΨ0)′(Yd−XdΨ0).Augmenting the system in (7) with the dummy observations
gives:
Y+ = X+hΨh+E+,(14)
where Y+ = (Y′ Y′d)′ and E+ = (E′ E′d)′ are(T+Td)×Nmatrices and X+ = (X′ X′d)′ is a(T+
Td)×Mmatrix. Then it is possible to show that the OLS estimator of the augmented system (given
by the usual formula (X+′ h X+
h )−1X+′ h Y+) is numerically equivalent to the posterior meanΨˉ.
A.1 Prior tightness
To make the prior operational, one needs to choose the value of the hyperparameterφ.We discuss a
number of methods for addressing this issue. The marginal data density of the model can be obtained
by integrating out all the coefficients, ie, definingΘas the set of all the coefficients of the model, the
marginal data density is:
p(Y)=
∫p(Y∣Θ)p(Θ)dΘ.(15)
Under our normal-inverted Wishart prior the densityp(Y)can be computed in closed form (see
Bauwens et al. (1999)). At each point in timeφcould be chosen by maximising:
φ∗t= arg maxφ
lnp(Y)(16)
This method has been used by Carriero et al. (2011). However, as discussed there, such a method
may have a tendency to choose low values for the tightness parameter implying a large weight on the
prior. It is important for our purposes to give considerable weight on the data. We therefore adopt
an alternative approach whereby the tightness parameter is chosen by matching the fit of particular
equations in the large VAR to those from smaller VAR models. Lenza et al. (2010) use a similar
approach to set tightness. We find this approach produces a reasonable balance between the effects of
priors and data that is appropriate for our analysis.
B Data appendix for large BVAR model
The data set for the large BVAR model is given in Table 6.
Table 6: Data appendix for large BVAR model
No. Variable Source No. Variable Source
1 US industrial production DS 23 20-year UK gilts BofE 2 US CPI DS 24 15-year UK gilts BofE 3 Euro-area industrial production DS 25 7-year UK gilts BofE 4 Euro-area HICP ECB 26 3-year UK gilts BofE 5 UK GDP NIESR 27 5-year 5-year implied inflation BofE 6 UK industrial production ONS 28 6-month Libor BG 7 Brent dollar oil price DS 29 12-month Libor BG 8 UK CPI ONS 30 FTSE All-Share index DS 9 UK-PPI ONS 31 FTSE All-Share dividend yield DS 10 UK-UEMP ONS 32 FTSE All-Share price-earnings ratio DS 11 UK house price index HF 33 UK exchange rate index BofE 12 10-year gilt - T-bill spread BofE 34 US dollar-sterling exchange rate BofE 13 UK consumer confidence EC 35 Euro-sterling exchange rate BofE 14 M4 BofE 36 T-bill - Bank Rate spread BofE 15 M3 BofE 37 3-month Libor - T-bill spread BofE 16 Retail deposits and cash in M4 BofE 38 3-month Libor-Bank Rate spread BofE/BG 17 Secured lending to individuals BofE 39 2-year gilt - T-bill spread BofE 18 M4 net lending to private sector BofE 40 5-year gilt - T-bill spread BofE 19 M4 lending BofE 41 Bank Rate BofE 20 Household M4 BofE 42 US federal funds rate Fed 21 PNFC M4 BofE 43 Euro-MRO interest rate BD/BG 22 OFC-M4 BofE