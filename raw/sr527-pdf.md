
### Federal Reserve Bank of New York Staff Reports
This paper presents preliminary fi ndings and is being distributed to economists and other interested readers solely to stimulate discussion and elicit comments. The views expressed in this paper are those of the authors and are not necessar-ily refl ective of views at the Federal Reserve Bank of New York or the Federal Reserve System. Any errors or omissions are the responsibility of the authors.
Staff Report no. 527 December 2011
Han Chen Vasco Cúrdia
Andrea Ferrero
### The Macroeconomic Effects of Large-Scale Asset Purchase Programs
Chen: University of Pennsylvania. Cúrdia, Ferrero: Federal Reserve Bank of New York (e-mail: vasco. curdia@ny.frb.org, andrea.ferrero@ny.frb.org). This paper was prepared for the conference “Learning the Lessons from QE and Other Unconventional Monetary Policies,” held at the Bank of England November 17-18, 2011. Special thanks to Richard Harrison for his discussion and to the conference participants for their comments. The authors have also benefi ted from comments by Hal Cole, Frank Diebold, Stefano Eusepi, John Fernald, Keith Kuester, James Nason, Ed Nelson, Ricardo Reis, Glenn Rudebusch, Frank Schorfheide, Eric Swanson, Michael Woodford, and participants in seminars at the University of Pennsylvania, the Federal Reserve Banks of New York, Philadelphia, and San Francisco, the University of California at Santa Cruz, and the 2011 European Economic Association meetings in Oslo. The views expressed in this paper are those of the authors and do not necessarily refl ect the
Abstract
The effects of asset purchase programs on macroeconomic variables are likely to be moderate. We reach this conclusion after simulating the impact of the Federal Reserve’s second large-scale asset purchase program (LSAP II) in a DSGE model enriched with a preferred habitat framework and estimated on U.S. data. Our simulations suggest that such a program increases GDP growth by less than half a percentage point, although the effect on the level of GDP is very persistent. The program’s marginal contribution to infl ation is very small. One key reason for our fi ndings is that we estimate a small degree of fi nancial market segmentation. If we enrich the set of observables with a measure of long-term debt, the semi-elasticity of the risk premium to the amount of debt in private-sector hands is substantially smaller than that reported in the recent empirical literature. In this case, our baseline estimates of the effects of LSAP II on the macroeconomy de-crease by at least a factor of two. Throughout the analysis, a commitment to an extended period at the zero lower bound for nominal interest rates increases the effects of asset purchase programs on GDP growth and infl ation.
Key words: quantitative easing, zero lower bound, unconventional monetary policy
The Macroeconomic Effects of Large-Scale Asset Purchase Programs Han Chen, Vasco Cúrdia, and Andrea Ferrero Federal Reserve Bank of New York Staff Reports, no. 527 December 2011 JEL classifi cation: E43, E44, E52, E58
The Macroeconomic Effects of LSAP Programs
### 1 Introduction
In response to the recent financial crisis, the major central banks around the world have
engaged in multiple rounds of large scale asset purchase (LSAP) programs, typically financed
with the creation of excess reserves. The Federal Reserve purchased a total of $1.75 trillion
in agency debt, mortgage-backed securities and Treasuries starting in early 2009, followed by
a second Treasury-only program in the fall of 2010.1 Also in early 2009, the Bank of England
set up an asset purchase facility whose size is currently about £200 billion, approximately
equivalent to $315 billion. The European Central Bank initiated purchases of up to e60
billion (approximately $43.5 billion) in Euro area covered bonds in mid-2009. In October of
2010, the Bank of Japan unveiled a U5 trillion (approximately $61.5 billion) asset purchase
program.
The objective of the various LSAP programs, often referred to as “Quantitative Easing”
(or QE), is to support aggregate economic activity in periods when the traditional instrument
of monetary policy (the short-term nominal interest rate) is not available due to the zero
bound constraint. The general idea is that asset purchases operate directly on different
segments of the yield curve, reducing rates at different maturities while the short-term rate
is at zero.
Several papers find evidence that LSAP programs have indeed been effective in reducing
long-term rates. For example, Gagnon et al. (2011) estimate that the first round of asset
purchases by the Federal Reserve lowered the ten-year Treasury yield by 58 basis points
(bp).2
Yet, agreement on the effectiveness of LSAP programs to boost the economy is far from
1In September of 2011, the Fed announced an additional $400 billion program, this time as a pure swap between short-term and long-term assets not involving the creation of additional reserves.
2A selected sample of other estimates include 13 bp in Hamilton and Wu (2010), 39 bp in Doh (2010), 45 bp in D’Amico and King (2010), and 107 bp in Neely (2010). Krishnamurthy and Vissing-Jorgensen (2011) find that LSAP II reduced the ten-year yield by about 16 bp. See more details in Table 1.
The Macroeconomic Effects of LSAP Programs
universal. From a theoretical perspective, LSAP programs were criticized before their imple-
mentation, based on some version of the irrelevance result in Wallace (1983). Quantitative
easing of this type is also irrelevant in the baseline New Keynesian model of Eggertsson and
Woodford (2003). In this framework, injecting reserves in exchange for longer term securi-
ties is a neutral operation. To the extent that market participants take full advantage of
arbitrage opportunities, LSAP programs should have no effect on real economic outcomes.
Cúrdia and Woodford (2011) extend this result to a New Keynesian model with credit fric-
tions. If households perceived the assets purchased (such as short-term government bonds)
as equivalent to reserves, again LSAP programs have no effect on the macroeconomy.3 Ex-
post, the criticism has continued due to the difficulty of identifying empirically the effects of
asset purchases from other macroeconomic forces (e.g. Cochrane, 2011).
In this paper, we estimate the effects of LSAP on macroeconomic variables in a dynamic
stochastic general equilibrium (DSGE) model with segmented asset markets. General equi-
librium effects are at the heart of Wallace’s irrelevance theorem. By going beyond the effects
of asset purchases on interest rates, we can evaluate the extent of the criticisms against this
type of programs. At the same time, we want to give LSAP programs a chance. We introduce
limits to arbitrage and market segmentation in a simple form that encompasses frictionless
financial markets. Therefore, our strategy is to identify the degree of segmentation — and
ultimately the effectiveness of asset purchases on macroeconomic activity — directly from
the data, without assuming a priori that LSAP programs are bound to fail.
We augment a standard DSGE model with nominal and real rigidities, along the lines of
Christiano, Eichembaum and Evans (2005) and Smets and Wouters (2007), with segmented
3Asset purchase programs may be an effective tool to boost the economy if the government buys securities that are not equivalent to reserves, either because not all households can invest in those assets or because financial frictions impair the investment activity. Recent research along these lines, such as Cúrdia and Woodford (2011), Del Negro et al. (2011) and Gertler and Karadi (2011), has mostly focused on private credit markets. Here, instead, we study frictions that rationalize a role for government purchases of long-term bonds.
The Macroeconomic Effects of LSAP Programs
bond markets. In particular, we follow Andres, Lopez-Salido and Nelson (2004, henceforth
ALSN) and assume that investors have heterogeneous preferences for assets of different
maturities (a “preferred habitat” motive, similar to Vayanos and Vila, 2009). We do not
model the details of why assets of different maturities are imperfect substitutes. Rather, we
postulate that this type of market segmentation exists and estimate the importance of this
friction for the transmission mechanism of monetary policy.
The form of asset market segmentation that we use in this paper implies that the long-
term interest rate matters for aggregate demand distinctly from the expectation of short-
term rates. In this world, even if the short-term rate is constrained by the zero lower
bound (ZLB) for a long period of time, monetary policy can still be effective by directly
influencing current long-term rates. In addition, we assume that the risk premium that
arises in the model as a consequence of transaction costs is a positive function of the supply
of long-term Treasury securities. This assumption captures, in reduced form, the notion that
asset purchase programs are most effective in flattening the yield curve by reducing the risk
premium (Gagnon et al., 2011).
We estimate the model with standard Bayesian methods for the post-war sample, includ-
ing the recent years.4 Our main experiment is a counterfactual evaluation of what would
have happened to output, inflation and the other macroeconomic variables in the absence of
LSAP programs.
First, we calibrate the asset purchase program in the model to match a reduction in the
risk-premium by 30 annualized bp on impact. At the same time, we consider that the central
bank announces the commitment to hold the interest rate at the ZLB for four quarters.5 The
posterior median GDP growth increase is0.4(annualized), while the posterior median
4Including the data since the Fall of 2008 presents us with the key challenge of incorporating the zero bound of nominal interest rates. We deal with this problem using the techniques developed in Cúrdia and Woodford (2011).
5This assumption is consistent with the “extended period” language in the FOMC statements at the time of LSAP II and the market expectations as implied in surveys of private forecasters.
The Macroeconomic Effects of LSAP Programs
inflation increase is less than 5 bp (annualized). Importantly, the corresponding effect on
the level of GDP is estimated to be very long lasting — six years after the start of the
program the level of GDP is still 0.25% above the path that would have prevailed in the
absence of the LSAP program.
Counterfactual simulations suggest that the commitment to hold the short-term nominal
interest rate at the ZLB increases the response of real activity and inflation roughly by a
factor of two and introduces upward skewness in the uncertainty surrounding the median
estimates. Furthermore, the boost from the commitment to the ZLB is increasingly larger
with the length of such a commitment. Overall, in our model, the effects of LSAP II are
slightly smaller — and considerably more uncertain — than a 50 bp cut in the short-term
rate.
These results take as given the effects on the risk premium from the empirical literature
discussed above. When we estimate directly the elasticity of the risk premium to the supply
of bonds using data on long-term US Treasuries, we find a much smaller number than the
empirical literature suggests. Our estimates imply that an asset purchase program of $600
billion leads to a posterior median reduction in the risk premium of 13 bp (compared with
30 bp in the baseline experiment). As a consequence, the effects on GDP and inflation are
also smaller, by about a factor of two.
Our conclusion is that the effects of LSAP programs on macroeconomic variables, such as
GDP and inflation, are likely to be moderate. We also consider several robustness exercises
and find that the effects on GDP growth are unlikely to exceed half a percentage point.
The inflationary consequences of asset purchase programs are consistently very small. As
a comparison, using the FRB/US model, Chung et al. (2011) find that LSAP II induced
a reduction in the risk premium of only 20 bp but increased the level of GDP by about
0.6% and the inflation rate by 0.1%. Baumeister and Benati (2011), using a VAR with time-
varying coefficients, consider a change in the term premium of 60 bp and estimate a median
The Macroeconomic Effects of LSAP Programs
increase in GDP growth of 3% and on inflation of 1%. We thus conclude that our results are
more moderate than in the existing literature, especially compared to the VAR methodology.
Importantly, our results only touch upon the positive dimension of LSAP programs. Harrison
(2010) evaluates the macroeconomic consequences of the optimal amount of asset purchases
in a version of this model without capital. His findings are consistent with ours in the sense
that asset purchases can improve aggregate welfare, but their quantitative relevance appears
to be limited.
Our results do not depend on whether asset purchases are financed via reserves or sales
of short-term debt, to the extent that these two assets are close to perfect substitutes.
Therefore, according to our model, the effects of the Federal Reserve’s last round of asset
purchases (also known as “Operation Twist Again”) should be in line with the estimates
from LSAP II after controlling for the scale factor.
The rest of the paper proceeds as follows. The next section presents the model. Section 3
discusses the data and the priors for the estimation. The baseline results and some robustness
exercises are in Section 4. Section 5 introduces the quantity of debt in the estimation. Section
6 concludes.
### 2 Model
Two types of households, unrestricted (denoted byu)and unrestricted (denoted byr),
populate the economy and supply differentiated labor inputs. Competitive labor agencies
combine these inputs into a homogeneous composite. Competitive capital producers trans-
form the consumption good into capital. Monopolistic competitive firms hire the labor
composite and rent capital to produce intermediate goods. Competitive final goods produc-
ing firms package intermediate goods into a homogeneous consumption good. Finally, the
government sets monetary and fiscal policy.
The Macroeconomic Effects of LSAP Programs
2.1 Households
The key modification relative to a standard medium-scale DSGE model (Christiano,
Eichembaum and Evans, 2005; Smets and Wouters, 2007) is the introduction of segmentation
and transaction costs in bond markets, as in ALSN.
A continuum of measure one of households populate the economy. Householdj=u,r
enjoys consumptionCjt(relative to productivityZt,as in An and Schorfheide, 2007) and
dislikes hours workedLjt. 6 Households supply differentiated labor inputs indexed byibut
perfectly share consumption risk within each group. The life-time utility function for a
generic householdsjis
Et∞∑s=0
βsjbjt+s
 1
1−σj
(Cjt+s
Zt+s−h
Cjt+s−1
Zt+s−1
)1−σj
−ϕjt+s(L
jt+s(i))
1+ν
1 +ν
,(2.1)
whereβj∈(0,1) is the individual discount factor,bjtis a preference shock,σj>0 is the
coefficient of relative risk aversion,h∈(0,1) is the habit parameter,ν≥0 is the inverse
elasticity of labor supply andϕjtis a labor supply shock.7 The preference and labor supply
shocks both follow stationary AR(1) processes in logs.
Two types of bonds exist. Short-term bondsBtare one-period securities purchased at
timetthat pay a nominal returnRtat timet+ 1. Following Woodford (2001), long-term
bonds are perpetuities that costPL,tat timetand pay an exponentially decaying couponκs
at timet+s+1,forκ∈(0,1].8 We abstract from money and consider the limit of a cashless
economy as in Woodford (1998).
6We express utility as a function of detrended consumption to ensure the existence of a balanced growth path with constant relative risk aversion preferences. Imposing log-utility of consumption may be an exces-sively restrictive assumption in our model which is mainly concerned about asset pricing.
7We allow for heterogeneity in preference shocks, discount factors and coefficient of relative risk aversions because these factors affect the household’s consumption-saving decisions and financial market segmentation directly influences these optimality conditions. As such, this heterogeneity can potentially influence the simulation results in a substantial way.
8Ifκ= 1, this security is a consol.
The Macroeconomic Effects of LSAP Programs
The fractionωuof unrestricted households trade in both short-term and long-term gov-
ernment bonds. Unrestricted households, however, pay a transaction costζtper-unit of
long-term bond purchased. The remaining fraction of the populationωr= 1 −ωuconsists
of restricted households who only trade in long-term bonds but pay no transaction costs.9
The flow budget constraint differs depending on whether the household is unrestricted
or restricted. For an unrestricted household that can trade both short and long-term bonds,
we have
PtCut+Bu
t+(1+ζt)PL,tBL,ut≤Rt−1B
ut−1+
∞∑s=1
κs−1BL,ut−s+W
ut(i)Lut(i)+Put+Pcp,ut−Tut.(2.2)
For a restricted household who can only trade in long-term securities but does not pay
transaction costs, we have
PtCrt+PL,tB
L,rt≤
∞∑s=1
κs−1BL,rt−s+Prt+Pcp,rt+Wr
t(i)Lrt(i)−Trt.(2.3)
In equations (2.2) and (2.3),Ptis the price of the final consumption good,Wjt(i)is the wage
set by a household of typej=u,rwho supplies labor of typei,PjtandPcp,jtare profits
from ownership of intermediate goods producers and capital producers respectively, andTjt
are lump-sum taxes.
One advantage of assuming that the entire stock of long-term government bonds consists
of perpetuities is that the price in periodtof a bond issuedsperiods agoPL−s,tis a function
of the coupon and the current price
PL−s,t=κsPL,t.
9We discuss in more detail the implications of transaction costs and bond market segmentation in sections 2.6.1 and 2.6.2 below.
The Macroeconomic Effects of LSAP Programs
Using this relation, we can rewrite the household budget constraint in a more convenient
recursive formulation.10 In particular, the budget constraint of an unrestricted household
becomes
PtCut+Bu
t+(1+ζt)PL,tBL,ut≤Rt−1B
ut−1+PL,tRL,tB
L,ut−1+Wu
t(i)Lut(i)+Put+Pcp,ut−Tut,(2.4)
while for a restricted household we have
PtCrt+PL,tB
L,rt≤PL,tRL,tB
L,rt−1+Prt+Pcp,rt+Wr
t(i)Lrt(i)−Trt,(2.5)
whereRL,tis the gross yield to maturity at timeton the long-term bond11
RL,t= 1
PL,t+κ.
Householdjconsumption-saving decisions are the result of the maximization of (2.1)
subject to (2.4) ifj=uor (2.5) ifj=r.See the technical appendix for details and section
2.6 for some discussion.
2.1.1 Labor Agencies and Wage Setting Decision
Perfectly competitive labor agencies combine differentiated labor inputs into a homoge-
nous labor compositeLtaccording to the technology
Lt=
[∫1
0
Lt(i)1
1+λwdi
]1+λw,
whereλw≥0 is the steady state wage markup.
10See the technical appendix for the derivations. 11We chooseκto match the duration of this bond, given byRL,t/(RL,t−κ),to the average duration of
ten-year US Treasury Bills.
The Macroeconomic Effects of LSAP Programs
Profit maximization gives the demand for theithlabor input
Lt(i)=
[Wt(i)
Wt
]−1+λwλw
Lt.(2.6)
From the zero profit condition for labor agencies, we obtain an expression for the aggregate
wage indexWtas a function of the wage set by theithhousehold
Wt=
[∫1
0
Wt(i)− 1λwdi
]−λw.
Households are monopolistic suppliers of differentiated labor inputsLt(i)and set wages
on a staggered basis (Calvo, 1983) taking the demand as given. In each period, the prob-
ability of resetting the wage is 1 −ζw,while with the complementary probability the wage
is automatically increased by the the steady state rates of inflation(Π)and of productivity
growth(eγ),
Wjt+s(i)=(Πeγ)sW~j
t(i),(2.7)
fors>0, whereW~jt(i)is the wage chose at timetin the event of an adjustment. A household
of typejwho can reset the wage at timetchoosesW~jt(i)to maximize
Et∞∑t=0
(βjζw)s
[Ξj,pt+sW~
jt(i)Ljt+s(i)−
ϕjt+s(Ljt+s(i))
1+ν
1 +ν
],
whereΞj,ptis the marginal utility of consumption in nominal terms, subject to (2.6) and
(2.7). The technical appendix presents the first order condition for this problem.
2.2 Capital producers
Competitive capital producers make investment decisions, choose the utilization rate and
rent capital to intermediate good producing firms. By choosing the utilization rateut,capital
The Macroeconomic Effects of LSAP Programs
producers end up renting in each periodtan amount of “effective” capital equal to
Kt=utKˉt−1,
Capital producers accumulate capital according to
Kˉt= (1−δ)Kˉt−1+µt
[ 1−S
(ItIt−1
)]It,(2.8)
whereδ∈(0,1) is the depreciation rate,µtis an investment-specific technology shock that
follows a stationary AR(1) process in logs andS(⋅)is the cost of adjusting investment (with
S′(·)≥0 andS′′(·)>0).12
Capital producers discount future profits at the marginal utility of the average shareholder
Ξpt+s≡ωuβ
suΞ
u,pt+s+ωrβ
srΞ
r,pt+s.
This variable is the appropriate discount factor of future dividends because ownership of
capital producing firms is equally distributed among all households.13 Capital producers
maximize the expected discounted stream of dividends to their shareholders
Et∞∑s=0
Ξpt+s
[Rkt+sut+sKˉt+s−1−Pt+sa(ut+s)Kˉt+s−1−Pt+sIt+s
],
subject to the law of motion of capital (2.8), whereRktis the return per unit of effective
capital. Note that we assume that utilization subtracts real resources measured in terms of
the consumption good,a(ut)Kˉt−1.14
12Furthermore, we assume thatS(eγ)=S′(eγ)= 0. 13The same consideration applies below to intermediate goods producers. 14As in Christiano, Motto and Rostagno (2009), we choose an implicit functional form fora(ut)such that
u= 1 in steady state anda(1)= 0.
The Macroeconomic Effects of LSAP Programs
2.3 Final Goods Producers
Perfectly competitive final goods producers combine differentiated intermediate goods
Yt(f),supplied by a continuum of firmsfof measure 1, into a homogeneous goodYtaccording
to the technology
Yt=
[∫1
0
Yt(f)1
1+λfdf
]1+λf,
whereλf≥0 is the steady state price markup. The resulting demand for thefthintermediate
good is
Yt(f)=
[Pt(f)
Pt
]−1+λfλf
Yt.(2.9)
From the zero profit condition for intermediate goods producers, we obtain an expression
for the aggregate price indexPtas a function of the price set by thefthintermediate good
producer
Pt=
[∫1
0
Pt(f)− 1λfdf
]−λf.
2.4 Intermediate goods producers
A continuum of measure one of monopolistic competitive firms combine rented capital and
hired labor to produce intermediate goods according to a standard Cobb-Douglas technology
Yt(f)=Kt(f)α(ZtLt(f))1−α,(2.10)
whereZtis a labor-augmenting technology process which evolves according to
log
(ZtZt−1
) = (1−ρz)γ+ρzlog
(Zt−1Zt−2
) +εz,t.
The Macroeconomic Effects of LSAP Programs
Cost minimization yields an expression for the marginal cost which only depends on aggregate
variables
MC(f)t=MCt=(Rk
t)αW1−α
t
αα(1−α)1−αZ1−αt
.(2.11)
Intermediate goods producers set prices on a staggered basis (Calvo, 1983). In each
period, a firm can readjust prices with probability 1−ζpindependently of previous adjust-
ments. We depart from the basic formulation of staggered price setting in assuming that the
firms that cannot adjust in the current period index their price to the steady state inflation
rateΠ.The problem for a firm that can adjust at timetis to choose the priceP~t(f)that
maximizes
Et∞∑s=0
ζspΞpt+s
[P~t(f)Πs−λf,t+sMCt+s
]Yt+s(f),
subject to (2.9) conditional on no further adjustments aftert,whereλf,tis a goods markup
shock that follows a stationary AR(1) process in logs.
2.5 Government Policies
The central bank follows a conventional feedback interest rate rule similar to Taylor
(1993), but with interest rate smoothing and using the growth rate in output, instead of the
output gap,
Rt
R=
(Rt−1
R
)ρm[(Πt
Π
)φπ(Yt/Yt−4e4γ
)φy]1−ρmeεm,t,
whereΠt≡Pt/Pt−1is the inflation rate,ρm∈(0,1),φπ>1,φy≥0 andεm,tis an i.i.d.
innovation.
The presence of long-term bonds modifies the standard government budget constraint
Bt+PL,tBLt=Rt−1,tBt−1+ (1 +κPL,t)B
Lt−1+PtGt−Tt.(2.12)
The Macroeconomic Effects of LSAP Programs
The left-hand side of expression (2.12) is the market value, in nominal terms, of the total
amount of bonds (short-term and long-term) issued by the government at timet.The right-
hand side is the total deficit at timet,that is, the cost of servicing bonds maturing in that
period plus spendingGtnet of taxes.
We assume that the government controls the supply of long-term bonds following a simple
autoregressive rule for their detrended market value in real terms
PL,tBLt
PtZt=
(PL,t−1B
Lt−1
Pt−1Zt−1
)ρBeεB,t,(2.13)
whereρB∈(0,1) andεB,tis an i.i.d. exogenous shock. We interpret LSAP programs as
shocks to the composition of outstanding government liabilities compared to the historical
behavior of these series.
Finally, the government adjusts the real primary fiscal surplus in response to the lagged
real value of long-term debt, as in Davig and Leeper (2006) and Eusepi and Preston (2011),
TtPtZt
−Gt
Zt=Φ
(PL,t−1B
Lt−1
Pt−1Zt−1
)φTeεT,t,(2.14)
whereφT>0 andεT,tfollows a stationary AR(1) process. All fiscal variables in rule (2.14)
are cyclically adjusted (i.e. expressed relative to the level of productivity) and the constant
Φis such that in steady state the fiscal rule is just an identity.
2.6 Equilibrium and Solution Strategy
In equilibrium, households and firms maximize their objectives subject to their con-
straints and all markets clear. In particular, the resource constraint is
Yt=ωuCut+ωrC
rt+It+Gt+a(ut)Kˉt−1.
The Macroeconomic Effects of LSAP Programs
We solve the model by taking a first-order log-linear approximation about a steady state
in which quantities are normalized by the level of productivityZtand relative prices are
expressed as function ofPt.The technical appendix shows the full set of non-linear normal-
ized equilibrium relations, characterizes the steady state solution, and presents the full set
of log-linearized equations that constitute the basis for the estimation.
These conditions are standard in modern DSGE models (Christiano, Eichembaum and
Evans, 2005; Smets and Wouters, 2007) with the exception of the households’ consumption-
saving decisions. Here, we focus on these Euler equations to sharpen the intuition about the
effects of segmentation in the bond market. This discussion should also clarify the channels
through which asset purchase programs can support macroeconomic outcomes.
Since only unrestricted households trade in short-term bonds, the pricing equation for
these securities is
1 =βuEt[e−γ−zt+1
Ξut+1
Ξut
Rt
Πt+1
],(2.15)
whereΞutis the marginal utility of detrended consumption in real terms for an unrestricted
household ande−γ−zt+1is the correction factor due to productivity growth.
Both unrestricted and restricted households trade long-term bonds. For unrestricted
households, the pricing equation of these securities is
(1 +ζt)=βuEt[e−γ−zt+1
Ξut+1
Ξut
PL,t+1
PL,t
RL,t+1
Πt+1
].(2.16)
For constrained households, the pricing condition is
1 =βrEt[e−γ−zt+1
Ξrt+1
Ξrt
PL,t+1
PL,t
RL,t+1
Πt+1
].(2.17)
Restricted households have a different marginal utility of consumption and do not pay the
transaction cost.
The Macroeconomic Effects of LSAP Programs
2.6.1 Transaction Costs and the Risk Premium
The presence of transaction costs for unrestricted households in the market for long-
term bonds gives rise to a risk premium. Using equation (2.16), we defineREHL,tas the
counterfactual yield to maturity on a long-term bond at timetin the absence of transaction
costs, given the same path for the marginal utility of consumption of unrestricted households.
No arbitrage implies that this fictitious bond should have the same risk-adjusted return as
the long-term security actually traded. We measure the risk premium as the difference
between these two yields to maturity, up to a first order approximation
R^L,t−R^EHL,t=
1
DL
∞∑s=0
(DL− 1
DL
)sEtζt+s,(2.18)
whereDLis the steady state duration of the two securities.15 Expression (2.18) shows that
the risk premium in this economy equals the present discounted value of current and expected
future transaction costs.
In ALSN, the risk premium has two components, one endogenous and one exogenous. The
endogenous component arises because households face a portfolio adjustment cost, function
of the relative quantity of money relative to long-term assets. The idea is that long-term
bonds entail a loss of liquidity that households hedge by increasing the amount of money
in their portfolio. The transaction costs in the market for long-term bonds are treated as
purely exogenous.
We retain the distinction between endogenous and exogenous component of the risk
premium while abstracting from the portfolio adjustment cost component. Instead, we
directly assume that transaction costs are function of the detrended real value of long-term
15The details of the derivation are in the technical appendix. In defining the yield to maturity of a bond in the absence of transaction costs, we adjust the parameterκto guarantee that the fictitious security has the same steady state duration as the actual long-term bond.
The Macroeconomic Effects of LSAP Programs
bonds plus an error
ζt≡ζ(PL,tB
Lz,t,εζ,t
),(2.19)
whereBLz,t≡BL
t/(PtZt).We do not take a stand on the explicit functional form ofζ(.).
We only require the function and its first derivative to be positive when evaluated in steady
state (i.e.ζ(PLBLz,0)>0 andζ′(PLB
Lz,0)>0). The first assumption ensures the presence
of a positive steady state risk premium, as in the data. The second assumption guarantees
that the yield on long-term bonds drops following a reduction in their outstanding amount.
This element gives LSAP programs a chance to work through the mechanism identified in
the reduced form estimates (Gagnon et al., 2011).
Up to a log-linear approximation, our parsimonious formulation of transaction costs is
observationally equivalent to the two frictions in ALSN. The idea that transaction costs
depend directly on the aggregate stock of bonds captures the same intuition (i.e. a liquidity
cost) of the adjustment cost function in the original formulation.
2.6.2 Limits to Arbitrage
The assumption of market segmentation captures, in reduced form, the observation that
in reality some fraction of the population mostly saves through pension funds and other
types of long-term institutional investors. These financial intermediaries are specialists in
certain segments of the market and their transaction costs are likely to be small. Conversely,
households who invest in long-term bonds mostly for diversification motives may face higher
transaction costs.16 The parameterωumeasures this segmentation and is one of the key
objects of interest in our estimation results.
The key implication of bond market segmentation is that not all agents in the model can
take full advantage of arbitrage opportunities. Unrestricted households can arbitrage away,
16See Andres et al. (2004) for a more detailed discussion of this interpretation.
The Macroeconomic Effects of LSAP Programs
up to some transaction cost, differences in risk-adjusted expected returns between short
and long-term bonds (equations 2.15 and 2.16) but restricted households do not have this
possibility. Equation (2.17) fully characterizes the savings behavior of restricted households.
This friction provides a rationale for asset purchase programs to influence macroeconomic
outcomes, thus breaking the irrelevance result in Wallace (1983). In particular, in our model,
a program targeted to purchases of long-term securities reduces the risk premium (equation
2.19). Absent segmentation, this program would affect the yield to maturity of the long-term
bond (equation 2.16), but it would have no effects on the real allocation. The intuition for
this result is that this program reduces the risk premium of the long bond, changing the
expected return on the long bond. Because the unrestricted households can invest in both
bonds, they will reallocate their portfolios until the two expected returns are equated again,
implying a different yield to maturity on the long bond, so that in the end their expected
return (accounting for transaction costs) is unchanged. Because the expected returns are
unchanged, there is no need to change the stochastic discount factor, and thus nothing else
in this economy changes.
Conversely, with segmented bond markets, LSAP programs do affect the real economy.
The change in long-term yields induces a change in the expected return of the restricted
households, which are not subject to the transaction costs. Because the expected return
is different from the restricted households’ perspective, then it requires an adjustment in
their stochastic discount factor. This change in turn leads to changes in their intertemporal
profile of consumption (equation 2.17) and indirectly influences both the pricing decisions of
intermediate producing firms and the investment decisions of capital producers. Ultimately,
general equilibrium forces imply that consumption for both types of agents, investment and
production respond as well.17 The simulations in section 4 illustrate the magnitude of the
17In practice, another effect of asset purchase programs could be the incentive for households to shift their portfolios toward riskier assets, such as equity and corporate bonds. In the model, this mechanism is absent as the equity shares are non-tradable.
The Macroeconomic Effects of LSAP Programs
LSAP stimulus on aggregate demand and inflation.
### 3 Empirical Analysis
We estimate the model with Bayesian methods, as surveyed for example by An and
Schorfheide (2007). Bayesian estimation combines prior information on the parameters with
the likelihood function of the model to form the posterior distribution. We construct the
likelihood using the Kalman filter based on the state space representation of the rational
expectations solution of the model.18 In the remainder of this section, we first describe the
data used and then present parameter prior and posterior distributions.
3.1 Data
We use quarterly data for the United States from the third quarter of 1987 (1987q3) to the
third quarter of 2009 (2009q3) for the following six series: real GDP per capita, hours worked,
real wages, core personal consumption expenditures deflator, nominal effective Federal Funds
rate, and the 10-year Treasury constant maturity yield.19 All data are extracted from the
Federal Reserve Economic Data (FRED) maintained by the Federal Reserve Bank of St.
18We impose a zero posterior density for parameter values that imply indeterminacy, which is equivalent to a truncation of the joint prior distribution.
19We use an extended sample, starting in 1959q3, to initialize the Kalman filter, but the likelihood function itself is evaluated only for the period starting in 1987q3, conditional on the previous sample.
The Macroeconomic Effects of LSAP Programs
Louis. The mapping of these variables to the states is
∆Yobst=100(γ+Y^z,t−Y^z,t−1+z^t),
Lobst= 100 (L+L^t
),
∆wobst=100(γ+w^z,t−w^z,t−1+z^t),
πobst=100(π+π^t),
robst=100(r+r^t),
robsL,t=100(rL+r^L,t),
where all state variables are in deviations from their steady state values,π≡ln(Π),r≡
ln(R),andrL≡ln(RL).
We construct real GDP by dividing the nominal GDP series by population and the GDP
deflator. The observable∆Yobstcorresponds to the first difference in logs of this series,
multiplied by 100. We measure the labor input by the log of hours of all persons in the non-
farm business sector divided by population. Real wages correspond to nominal compensation
per hour in the non-farm business sector, divided by the GDP deflator. As for GDP,∆wobst
is the first difference in logs of this series, multiplied by 100. The quarterly log-difference in
the personal consumption expenditures (PCE) core price index is our measure of inflation.
We use the effective Federal Funds Rate as our measure of nominal short-term rate and the
10-year Treasury constant maturity rate as our measure of nominal long-term interest rate.
In the baseline estimation, we do not use data on the quantity of debt. The reason
is that aggregate debt at quarterly frequency may not be the most appropriate data to
capture the implications of asset purchases on financial variables. For example, Gagnon
et al. (2011) consider high frequency time series and even studies’ methods to infer these
relations. Furthermore, D’Amico et al. (2011) argue that the use of aggregate data biases
The Macroeconomic Effects of LSAP Programs
the results, weakening the effects of asset purchases on yields. Therefore, instead of trying
to estimate the elasticity for the transmission of asset purchases onto the risk premium, we
assign a prior for this parameter consistent with the results from the vast literature on high
frequency estimation (time series and event studies included) reported in Table 1.20
A comparison between the prior and the posterior distributions of the elasticity of the
risk premium to the quantity of debt confirms our conjecture that the data contains little
information value for this parameter. As a robustness check, section 5 presents our main
experiment with parameter estimates obtained using the quantity of debt in the hands of
the private sector as an observable variable.
3.2 Prior Choice
Tables 2 and 3 (columns two to five) summarize the prior distributions of each parameter.
We use a Gamma distribution for the parameters that economic theory suggests should be
positive to constrain their support on the interval[0,∞].For those parameters that span
only the unit interval, we use the Beta distribution. For the standard deviation of shock
innovations, we use the Inverse-Gamma distribution.
The steady state value for inflation is centered at 2%, in line with the mandate-consistent
level of inflation commonly assigned to the Federal Open Market Committee (FOMC). The
steady state growth rate is centered at 2.5% (annualized). The discount factor has a prior
that implies a real interest rate of about 2% (annualized). The steady state spread be-
tween the 10-year treasury yield and the federal funds rate has a prior centered at 0.75%
(annualized), similar to the average in the data.
We follow Del Negro and Schorfheide (2008) for the priors of standard parameters. The
20We could have alternatively calibrated this elasticity but the wide range of estimates in Table 1 suggests little consensus on a specific value. Since this parameter significantly impacts our simulations, we prefer to take a more agnostic approach and allow for some uncertainty that encompasses most of the estimates in the reduced form literature.
The Macroeconomic Effects of LSAP Programs
investment adjustment cost convexity parameterS′′ has prior mean of 4 and standard de-
viation of 1. The utilization cost elasticity parametera′′has prior mean 0.2 and standard
deviation 0.1, implying that in response to a 1% increase in the return to capital, utilization
rates rise by about 0.17%. We calibrate the share of capital in productionαto 0.33, and
the capital depreciation rateδto 2.5% per quarter.
The habit formation coefficient for both types of agents has prior mean of 0.6 and standard
deviation 0.1, also fairly common in the literature. The parameter controlling the labor
supply elasticityνhas a prior centered at 2. Similarly to Smets and Wouters (2007), we
estimate the intertemporal elasticity of substitution of consumption for households, except
that in our model we have two types of agents. The prior onσuandσris relatively flat
(centered at 2 with standard deviation of 1) and equal for both types, so that the data can
be informative about their value.
The fraction of unrestricted agentsωuis the crucial parameter to identify the degree of
bond market segmentation in the model. At the mean, our prior implies that 70% of the
households are unrestricted. A standard deviation of 0.2, however, makes the distribution flat
enough that the 90% prior interval is (0.32,0.96). The other key parameter is the elasticity of
the risk premium to changes in the market value of long debtζ′. The prior for this parameter
has a mean 1.5/100 and a standard deviation big enough to match the range of estimates
shown in Table 1 (see discussion above). The cash-flow parameter that controls the duration
of long-term bonds (given the yield to maturity) is calibrated to imply a duration of 30
quarters, similar to the average duration in the secondary market for 10-year US Treasury
bills. We consider short-term debt to include both government bonds with less than one
year to maturity as well as central bank liabilities in the form of reserves, vault cash and
deposits. In the US, the average for this quantity since 1974 is about 16% of annual GDP.
For long-term bonds, we consider all government bonds with maturity greater than one year,
which in the US is also about 16% of annual GDP since 1974.
The Macroeconomic Effects of LSAP Programs
Table 2 contains three non-standard parameters(Ξu/Ξr,Cu/Cr,andχwu)which refer
to steady state ratios hard to pin down directly from the data. We decided not to calibrate
these ratios to avoid biasing the estimation and the simulations in either direction. The pos-
terior distribution for these three parameters turns out to deviate negligibly from our prior.
Furthermore, the uncertainty in these ratios translates into uncertainty in the dynamics of
the model and in the effects of asset purchases on macroeconomic variables.
The priors for the wage and price rigidity parametersζwandζpare centered at values
that imply an expected frequency of price and wage changes of three quarters (Justiniano,
Primiceri and Tambalotti, 2010). The fiscal rule parameter,φTis centered at 1.5 and its
posterior does not differ too much from the prior. For the monetary policy rule, we consider
fairly standard parameter priors. The interest rate smoothing parameterρris centered at
0.7. The response to output growthφyis centered at 0.4. The prior mean for the response
to inflationφπ,centered at 1.75, is slightly higher than the usual value of 1.5 in Taylor
(1993). The 90% prior interval, however, is completely above one, consistent with the Taylor
principle.
The shocks follow AR(1) processes, with autocorrelation coefficientρicentered at 0.75,
except for the autocorrelations of productivity shocks (equal to 0.4 so that the growth rate
shock is not too persistent) and of the risk premium and debt shocks (equal to 0.8). The prior
mean of the innovations have standard deviationsσicentered at 0.5, except for the innovation
to the monetary policy shock and the risk premium shock whose standard deviation is smaller
because these variables refer to quarterly changes in interest rates.
3.3 Parameter Posterior Distribution
In order to obtain the posterior distribution, we first get the posterior mode and then
generate a sample of the posterior distribution using the Metropolis random walk Markov
The Macroeconomic Effects of LSAP Programs
Chain Monte Carlo (MCMC) simulation method.21 The last five columns of tables 2 and 3
report the posterior distribution of each parameter.
The first result that emerges from these tables is that the measure of market segmentation
is very small — the posterior 90% interval forωuis (0.713,0.992) with a median of 0.934 and
a mode of 0.987. Given our prior, the data pushes against a model with a significant degree of
market segmentation. Ceteris paribus, we should expect small macroeconomic effects of asset
purchases. In order to check the stability of the estimate of market segmentation (and, in
general, of other parameters), we reestimated the model with alternative samples. While in
our baseline estimation the sample ends in 2009q3 (just before the first US LSAP program),
we considered three alternative endings: 2007q2 (before the recent financial turbulence),
2008q3 (before the federal funds rate reached the ZLB) and 2011q2 (the most recent available
data). The parameter estimates always remain very comparable.22
The other key parameter is the elasticity of the risk premium to asset purchasesζ′.
If this elasticity were zero, asset purchases would affect neither the risk premium nor the
real economy. While we estimate this parameter, the posterior and prior distributions are
very similar, implying that the data are not very informative about this elasticity. This
finding is not very surprising, given that in the baseline estimation we observe changes
in the spread, but we do not use any observable for the quantity of long-term debt. In the
baseline simulation, this elasticity is perhaps better interpreted as summarizing the empirical
results from reduced-form estimates and event studies incorporated in the prior distribution.
In section 5, we estimate this parameter augmenting our set of observables with data on
the ratio between long-term debt and short-term debt. Conditional on these data and our
21After getting four separate chains of 100,000 draws, we compute the covariance matrix (with a 25% burn-in) and generate four new chains of 100,000 draws. We repeat this step two more times with 200,000 and 500,000 draws, respectively. At this stage, we use these last four chains to extract the parameter posterior distribution properties and to simulate the effects of asset purchases.
22One caveat is that most of our sample corresponds to a period of relative macroeconomic and financial stability in the US. Because the recent crisis may have exacerbated financial frictions, we subject our main experiment to a robustness check where we allow for an (exogenous) increase in the degree of segmentation.
The Macroeconomic Effects of LSAP Programs
model, the posterior distribution is concentrated at low levels, with a median of 0.41/100,
suggesting a fairly small impact of the quantity of debt on the risk premium and the 10-year
yield.
The sensitivity of consumption to the interest rate is estimated to be 3.2 for the unre-
stricted type and 2.2 for the restricted type at the posterior median. These numbers suggest
a specification of utility far enough from the usual log-utility assumption but also significant
heterogeneity in the sensitivity to the interest rate for the two types. Finally, the posterior
moments for the nominal rigidity parameters and policy rule coefficients are consistent with
several contributions in the DSGE literature. Importantly, price rigidities are estimated to
be quite high relative to the micro-evidence. These parameters may significantly influence
the simulations. Therefore, in the robustness analysis, we repeat our baseline experiment
withζpset at the prior mean.
### 4 Simulating LSAP II
Our baseline experiment corresponds to a simulation of the US LSAP II program. The
central bank buys long-term bonds (in exchange for short-term bonds) over the course of
four quarters, holds its balance sheet constant for the following two years and progressively
shrinks its holdings of long-terms securities over the final two years of the simulation. We
calibrate the asset purchase program in the model so that the median reduction of the risk
premium is 30 bp (annualized), which corresponds to the mid-point of the range of estimates
discussed in Section 1 and presented in Table 1.23 We choose this calibration strategy for
this part of the simulation because our focus is on the macroeconomic consequences of the
asset purchase programs. Later, we reestimate the model using data also on the quantity of
long-term Treasuries to shed some light on the elasticity of the risk premium to the quantity
23Our model formalizes the finding of Gagnon et al. (2011) that LSAP programs reduce long-term rates via their effect on the risk premium.
The Macroeconomic Effects of LSAP Programs
of debt. Figure 1 illustrates the path of the market value of long-term bonds in the hands
of the private sector following the government purchases. Based on survey evidence from
Blue Chip, we impose that the FFR is at the ZLB for the first four quarters (the “extended
period” language) after the beginning of the asset purchase program.24
We begin by showing our main simulation of LSAP II at the prior distribution and then
repeat the same experiment at the posterior. The following two subsections discuss the role
of the commitment to the zero lower bound and how LSAP compares to interest rate policy
shocks. The last subsection offers some robustness results.
4.1 Simulation at the Prior Distribution
This section illustrates how the choice of the priors constrains the macroeconomic effects
of asset purchase programs via Monte Carlo simulations. Specifically, we get 1000 random
draws for the parameter vector using the prior distribution. We then use these draws to solve
the model and extract the path of the state variables in response to the LSAP experiment
described above. Finally, we compute moments and percentiles of this sample of responses
for the variables of interest.25
Figure 2 shows the response of output growth, output level, inflation, FFR, 10-year yield
and risk premium to the simulated LSAP II experiment at the prior distribution, all in
annualized percentage rates. The level of output corresponds to percentage deviations from
trend, as opposed to a rate of change, and thus is not annualized. These plots represent the
marginal contribution of LSAP II, i.e. the deviations of each variable relative to the path
that would have prevailed absent the government intervention. The red continuous line is
the prior median response while the grey shaded area corresponds to the50th,60th,70th,
24Blue Chip has been asking the survey participants about the expected duration of the ZLB since the end of 2008. Until the recent change in the Federal Open Market Committee language that introduced a specific date for the expected liftoff, market participants had always maintained the expectation that the FFR would remain at the ZLB for the four/five quarters after the question was asked.
25The results are not sensitive to increasing the number of draws.
The Macroeconomic Effects of LSAP Programs
80thand90thprior probability intervals, from darker to lighter shading respectively.
The figure shows the width of the response of the risk premium to asset purchases (es-
sentially mapping the reduced-form/high-frequency range of estimates into our model) with
a median response at the peak of about 30 bp. As a consequence of the change in the risk
premium, output growth, the output level and inflation are higher than in the absence of
asset purchases. By construction, the asset purchase program achieves the desired effect
in the model. The key question is how big these effects are. Our prior is fairly generous,
encompassing very large effects, but also relative agnostic, as to extract as much informa-
tion as possible from the data without imposing too many ex-ante restrictions. To be more
precise, the median prior response of output growth is about 2% and the median response
of inflation is 0.5%, roughly in line with the results in Baumeister and Benati (2011). Using
a vector auto regression (VAR) model with time-varying coefficients, these authors find that
a 60 bp reduction in long-term rates increases GDP growth by 3% and the inflation rate of
the GDP deflator by 1% at the posterior median.
Our prior may be seen as too generous to the extent that we allow the effects of LSAP to
be potentially quite extreme (for example the95thpercentile is above 12% for GDP growth
and about 4% for inflation). The literature, however, does not rule out these extreme
outcomes. For example, Kapetanios et al. (2011) present VAR evidence for the effects of
similar policies on GDP growth in the United Kingdom that can be as high as 5% at mean,
depending on the estimation method. Our choice of fairly uninformative priors gives the
model a chance to generate such large effects.
In response to higher output and inflation, the central bank eventually increases the
interest rate in accordance with the policy rule, but only after the end of the commitment to
the ZLB. The evolution of the 10-year yield reflects the combined effect of the responses of
the risk premium and the expected future short-term interest rate (expectations hypothesis).
The former puts negative pressure on the long yield while the latter exerts the opposite
The Macroeconomic Effects of LSAP Programs
pressure. The outcome depends on how effective asset purchases ultimately are in boosting
the economy. If LSAP programs have a significant effect on output and inflation, the policy
rule dictates a strong response of the federal funds rate which can potentially dominate over
the negative impact on the risk premium and lead to an equilibrium increase in the 10-year
yield.
4.2 Simulation at the Posterior Distribution
In the previous subsection, we concluded that, according to this model and our choice
of the priors for the parameters, LSAP programs can boost output and inflation while the
effect on the 10-year yield is somewhat ambiguous, depending on the interplay between the
risk premium and the expectation hypothesis. In this section, we combine the prior with the
data for the past twenty years or so to form a posterior distribution of the parameters. We
then use the posterior to revisit our simulations of the effects of LSAP II. Figure 3 shows
the same variables and simulation as Figure 2, but now using parameter draws from the
posterior distribution.
On impact, GDP growth increases by 0.4% at the posterior median. The uncertainty is
skewed on the upside to almost 2%, partly due to the ZLB. After three quarters, the effect
on output growth is less than a half of its peak (which occurs on impact) and completely
vanishes after eight quarters. The effects on the level of output level are also modest. The
peak in this case occurs after 8 quarters at about 0.3% (posterior median), but now the
effects persist longer — after 24 quarters, the output level is still 0.25% higher than without
asset purchases. This modest but persistent effect on GDP level is likely to be important
from a welfare perspective — even more so if we consider that the90thprobability interval
allows for an increase in the level of modest as high as 1.5%. The effect on inflation is very
small, 3 bp (annualized) at the median. The effect on inflation is also skewed upward but
The Macroeconomic Effects of LSAP Programs
even the95thpercentile is only about 15 bp. Our results are at the lower end of the spectrum
in the existing literature. Beside the estimates in Baumeister and Benati (2011) mentioned
earlier, Chung et al. (2011), using the FRB/US model, assume that LSAP II induces a
reduction in the risk premium of only 20 bp but increases the level of GDP by about 0.6%
and inflation rate by 0.1%.
In spite of the small magnitudes, the positive boost of asset purchases to GDP growth
and inflation puts upward pressure on the interest rate. After the four quarters at the ZLB
which correspond to the commitment period, the FFR becomes positive but the median
increase is only 8 bp. Because asset purchases introduce little stimulus, the central bank
does not raise interest rates by much upon exiting the ZLB. The upward skewness in the
FFR reflects the skewness in the effects on GDP growth and inflation. Later, we disentangle
the effects of the non-linearity introduced by the ZLB from the pure estimation uncertainty.
The drop in the 10-year yield is a combination of the reduction in the risk premium,
which is the assumption behind the experiment, and the expected increase in future short-
term rates. The long-term rate decreases but less than the 30 bp drop in the risk premium,
because the private sector correctly anticipates future short-term rates to increase. Notice
that the posterior uncertainty on the term premium is skewed downward, which we will
discuss further below.
To summarize, the effects of LSAP II on GDP and inflation are moderate, especially
compared to the prior. Nevertheless, the effect on the output level is very persistent. The
main reason for the modest effects is that the estimated degree of segmentation is small. The
posterior median forωuis 0.93, that is, less than 7% of the population is excluded from the
short-term bond market. Given that in the model segmentation is crucial for asset purchases
to have an effect, not surprisingly, the boost from government purchases of long-term bonds
is small. The posterior distribution of the degree of segmentation, however, is skewed to
the left, implying that we cannot completely discard the possibility of higher segmentation.
The Macroeconomic Effects of LSAP Programs
The posterior mean is below the median by two percentage points and the5thpercentile
is 0.71 (Table 2). Together with the ZLB, this long left tail of the posterior estimates for
ωucontributes to the upward skewness of the response of GDP growth and inflation in the
baseline simulation.
The other parameter that potentially plays an important role in determining the effects
of asset purchases on the macroeconomy is the elasticityζ′ of the risk-premium to debt.
Unfortunately, this parameter is not well identified in our baseline estimation. In section
5 we repeat our estimation augmenting the set of observables with the quantity of long-
term debt to address this problem. For now, we note that our prior for the elasticity,
which essentially coincides with the posterior, also contributes to the overall skewness of the
response of macroeconomic variables documented above.
4.3 The Role of the ZLB
In this subsection, we show that the commitment of the central bank to keep the short-
term nominal interest rate at the ZLB for an “extended period” amplifies the effects of LSAP
II. According to our simulations, asset purchases boost GDP growth and increase inflation,
thus leading the central bank to increase the FFR. This endogenous interest rate response
mitigates the macroeconomic stimulus of asset purchase programs through the conventional
monetary policy channel. A commitment to keep the short-term nominal interest rate at the
ZLB for an “extended” period of time prevents the endogenous response of the monetary
authority and magnifies the contribution of asset purchases on macroeconomic outcomes.
Here, we quantify the magnitude of such a mitigation effect.
Figure 4 shows the responses in the case in which we do not impose the commitment to the
zero lower bound. For reference, the dashed blue line corresponds to the baseline simulation
with the commitment to the ZLB imposed. Quantitatively, the ZLB commitment roughly
The Macroeconomic Effects of LSAP Programs
doubles the effects of asset purchases. Absent this commitment, output growth increases by
0.2% and inflation by only 2 bp — which correspond to about half of the baseline effects.
Interestingly, while the profile for the FFR differs from the baseline, the 10-year yield is
almost identical. The cumulative effect of the increase in short rates on long rates via the
expectation-hypothesis component is the same. Without ZLB, the increase in nominal rates
occurs earlier but is smoother.
Importantly, the responses to LSAP II remain skewed upward, regardless of whether
the ZLB is imposed or not. This observation suggests that the role of the skewness in the
posterior distribution of the degree of segmentation and of the semi-elasticity of the risk
premium to the quantity of debt play a central role in explaining the upside uncertainty of
the response of macroeconomic variables.
A ZLB commitment of four quarters essentially doubles the effects of LSAP on output and
inflation. Recently, however, the Federal Reserve has extended its commitment to keep the
nominal interest rate at zero for a longer period.26 Figure 5 reproduces the main simulation
considering a commitment to keep the interest rate at zero for six quarters. In this case,
the effects on output and inflation are more than doubled, even though the commitment
period only increased by two quarters. This result shows very clearly that in this model the
ZLB commitment is very powerful in stimulating the economy, due to the strongly forward
looking behavior of the agents in the economy, and its effects increase non-linearly with the
number of quarters of the commitment.
The uncertainty bands also widen substantially. For example, the95thpercentile for
output growth increased from just under 2% to just above 8%, and the same percentile at
the peak effect on the output level increased from just above 1.5% to just under 7%. This
more pronounced skewness further confirms the non-linear effects of the ZLB commitment
in combination with the skewed distribution of the degree of segmentation and elasticity of
26At the time we are writing this paper, the commitment is for at least six quarters
The Macroeconomic Effects of LSAP Programs
risk premium to the asset purchases.
4.4 Comparison with a Standard Monetary Policy Shock
One of the motivations for central banks to engage in asset purchases is to support output
and inflation at times in which the ZLB constrains conventional interest rate setting. To give
a sense of the relative effectiveness of these two policies, this section compares the effects of
asset purchase programs discussed so far with a standard monetary policy shock, that is, an
unexpected reduction of the short-term nominal interest rate.
Figure 6 shows the response of the key macroeconomic variables to an unexpected re-
duction of 50 bp in the short-term interest rate. The median effects on GDP growth and
inflation are somewhat stronger than those implied by the baseline simulation previously dis-
cussed. Furthermore, the effects of the interest rate shock on the output level are not only
stronger but also more persistent than those of LSAP. GDP growth increases by 0.5% and
inflation by 4 bp. The implied decrease in long-term rates, however, is much smaller, only 2
bp.27 Moreover, the long-term rate quickly turns positive. This result is not surprising given
that the risk premium does not change. Therefore, the expectation hypothesis component
completely pins down the long-term interest rate in this case.
Another significant difference is the reduced uncertainty about the effects in the case of
an interest rate shock. The absence of the ZLB constraint may in part explain why the
posterior bands are more symmetric. Yet, as discussed in the previous subsection, even in
the absence of a commitment to the ZLB, uncertainty remains skewed upward, mostly due to
the skewness of the posterior estimates of the degree segmentation and of the semi-elasticity
of the term premium to the quantity of debt. Because segmentation plays a smaller role
in case of a shock to the short-term interest rate, the uncertainty in the response of GDP
27Our estimates thus imply a much smaller sensitivity of long-term rates to shocks to the short-term rate. As a point of comparison, Gurkaynak, Sack and Swanson (2005) estimate that the typical response of long rates to a cut of 100 bp in the FFR is 15 bp.
The Macroeconomic Effects of LSAP Programs
growth and inflation becomes smaller and much more symmetric.
Overall, in this model, the effects of LSAP II on output and inflation are slightly smaller
than those of a surprise reduction of the FFR by 50 bp, and much more uncertain. This
conclusion stands in contrast with Furher and Moore (1995), who find that output is four
times more sensitive to long-term than short-term rates. According to this metric, the 30
bp reduction in the risk premium should be equivalent to a reduction of the FFR of about
120 bp. Our results are thus much less generous to changes in the risk premium, confirming
our previous finding that the model simulations yield weaker effects of LSAP II on output
and inflation than what the VAR literature suggests.
4.5 Robustness
This section considers three robustness exercises. First, we ask how sensitive the model
is to the degree of market segmentation. Second, we study the role of nominal rigidities.
Third, we consider the implications of extending the duration of the LSAP program.
4.5.1 The Role of Market Segmentation
The baseline experiment suggests that the effects of LSAP II are fairly moderate on GDP
and quite small on inflation. One reason why our results may underestimate the effects of
asset purchase programs is that the degree of financial market segmentation may have re-
cently increased due to the financial crisis.28 As discussed earlier, our reduced-form friction
for market segmentation aims at capturing a combination of preferences for certain asset
classes and institutional restrictions on the type of investments certain financial intermedi-
aries undertake. By shifting the true and perceived distribution of risk, the financial crisis
28Baumeister and Benati (2010) estimate a VAR with time-varying coefficients and stochastic volatility to account for this type of effects, on top of other changes in the structural relations among macroeconomic variables potentially triggered by the financial crisis.
The Macroeconomic Effects of LSAP Programs
may have induced a fraction of investors previously active in multiple segments of financial
markets to concentrate on one particular asset class.
For this purpose, we repeat the baseline experiment in the presence of a high degree of
market segmentation. Figure 7 shows the results of the same simulated LSAP II experiment
as in the baseline case. The difference is that, in this case, we only draw from the lower half
of the posterior distribution of the parameterωu.All other parameters are drawn from the
same posterior distribution as before.
The median responses of GDP growth and inflation with the ZLB commitment are
roughly twice as large as in the baseline case, at+0.7and+0.06respectively (com-
pared to 0.4% and 0.03%). Upside posterior uncertainty is now more pronounced. The95th
percentile now nearly reaches 4% for GDP growth and0.4for inflation, compared to 2%
and0.15before. The stronger response of macroeconomic variables requires the central
bank to increase the short-term nominal interest rate by about 8 bp more. As a consequence,
given that the drop in the risk premium is the same, long-term rates decrease slightly less
(of the order of 4 bp).
The bottom line from this exercise is that allowing for a higher degree of segmentation
does increase the response of GDP growth and inflation to the stimulus of asset purchase
programs. However, unless segmentation becomes really extreme, the macroeconomic effects
of LSAP remain relatively small, especially for inflation.
4.5.2 The Role of Nominal Rigidities
One reason for the small response of inflation to LSAP II is that the estimated degree
of nominal rigidities, especially for prices, is quite high. While our priors for the probability
of holding prices and wages fixed in any given period(ζpandζw)are both centered at0.75,
the posterior medians for the two parameters are0.94and0.88,respectively.
A high degree of stickiness in prices and wages is not an uncommon finding in the DSGE
The Macroeconomic Effects of LSAP Programs
literature, especially in the absence of real rigidities like in our case. Additionally, Hall (2011)
has recently emphasized how prices have failed to fall substantially in the last recession. As
in the case of segmentation, the financial crisis may have caused a structural change in the
price setting process that the model interprets as an increase in price rigidities (the same
consideration applies to wages).29.
Nevertheless, we want to quantify the sensitivity of our results to a lower degree of
nominal rigidities, more in line with standard values from the empirical literature that uses
micro data (e.g. Nakamura and Steinsson, 2008). Figure 8 shows the results of the baseline
LSAP II experiment when we fixζpat its prior mean, equal to 0.75. All other parameters
are drawn from the same posterior distribution as before.
The figure shows that nominal rigidities play an important quantitative role in the re-
sponse of inflation to asset purchases. When prices are more flexible, the median response of
inflation to LSAP II is three times larger on impact than when we use the estimated posterior
distribution. The counterparts are a less persistent inflation process and a slightly smaller
effect on GDP growth. In equilibrium (i.e., taking into account the endogenous response
of monetary policy), the two effects roughly compensate each other. The increase in the
short-term interest rates is almost the same in the two cases. Therefore, also the behavior
of long-term rates is very similar. The increase in upside uncertainty for inflation is roughly
proportional to the changes in the median. The95thpercentile of the response in inflation
is0.5compared to just above0.15in the baseline experiment.
In sum, higher price flexibility shifts the adjustment in response to asset purchase pro-
grams from GDP growth to inflation, by making its process more front-loaded.
29Indeed, if we consider a sample that ends before the recent crisis (second quarter of 2007), the posterior median forζpis somewhat smaller
The Macroeconomic Effects of LSAP Programs
4.5.3 The Role of the Length of LSAP Programs
In our baseline simulation, the central bank accumulates assets over four quarters and
holds the balance sheet constant for the next two years, before gradually winding down
the program over two additional years. This assumption is fairly arbitrary. Depending on
economic conditions, policy makers may change the length of the programs, as the recent US
and UK experience suggests. Without undertaking an exhaustive analysis, this subsection
considers one alternative path: the central bank still accumulates assets over the first year
but then holds the balance-sheet constant for four years, instead of two, before gradually
exiting. Figure 9 shows the corresponding responses, in the same format as the previous
figures.
Not surprisingly, this change in the time profile of the asset holdings by the central bank
induces a stronger response by the risk premium, with a median peak response of -43 bp
(instead of -30 bp). As a result, output and inflation respond more strongly. However, while
the inflation response is more than twice as big relative to the baseline scenario (median
response at the peak of 0.07%, compared to 0.03%), the response of output is only modestly
stronger (median response of 0.50%, instead of 0.37%, for GDP growth). However, the boost
to the level of GDP becomes more persistent, peaking at 0.5% only after fifteen quarters
(instead of eight quarters in the baseline). Not surprisingly, the uncertainty around the
median is larger, with the95thpercentiles increasing proportionally.
In sum, if the central bank holds the purchased assets for longer, the stimulative impact
on output and inflation increases and becomes more persistent. Moreover, the additional
boost is stronger for inflation than for output. Nominal rigidities plays an important role in
this respect. Because the shock lasts longer, more firms and workers are expected to change
their prices and wages over time, which in turn leads the firms and workers who can change
their prices and wages early to do so more aggressively.
The Macroeconomic Effects of LSAP Programs
### 5 Estimating the Model with Data on Debt Quantity
In the simulations presented so far, we have calibrated our LSAP II experiment so that
the asset purchase program reduces the risk premium by 30 bp. This calibration is consistent
with the effect of the quantity of debt on long-term rates estimated in the empirical literature
(e.g. Gagnon et al., 2011). Because in the baseline estimation the semi-elasticity of rates
to the quantity of debt is not well-identified, our results completely rely on the prior for
this parameter, which is heavily informed by the reduced-form estimates available in the
literature. By introducing the quantity of debt among the set of observables, we can hope to
better identify this elasticity. In particular, the observed variable for debt in the model is the
ratio between long-term and short-term US Treasury bonds, where the threshold maturity
to distinguish between the two forms of liabilities is one year.30
For the new experiment, we maintain our baseline assumption about the evolution of
government purchases of long-term bonds illustrated in Figure 1. The difference with the
baseline simulation is that, in this case, we calibrate the size of the asset purchase program
directly on the quantity, that is, we target a $600 billion reduction of long-term debt in the
hands of the private sector.
Figure 10 displays the results. The effects of LSAP II are smaller than in the baseline case
by a factor of two for both GDP growth(+0.14and inflation(+0.015The results are
entirely driven by a smaller semi-elasticity of the risk premium to the quantity of debt. At
the posterior median, an asset purchase program of $600 billion implies a reduction of about
13 bp in the risk premium, compared to the 30 bp of our previous experiment. Contrary to
the baseline estimation, the semi-elasticity appears to be well-identified.
While uncertainty remains upward skewed, the posterior bands do not change exactly in
proportion to the median. The95thpercentile for GDP growth is+0.6compared to about
30This assumption is consistent with the announcement of LSAP II.
The Macroeconomic Effects of LSAP Programs
+2% in the baseline case. For inflation, the decline is from+0.15to+0.06Because
GDP growth and inflation move less, so does the FFR. A smaller increase of short-term
rates, coupled with a smaller decrease in the risk premium, implies that the 10-year yield
also drops less, from about0.26to about0.12
Our results for the sensitivity of risk premia to the quantity of long-term debt in the hands
of the private sector indicate that the estimates in the empirical literature may represent
an upper bound. Of course, a structural change due to the disruption of financial markets
associated with the recent crisis may explain why reduced-form estimates, especially if based
on event studies, find higher values for this elasticity. Even allowing for this possibility, asset
purchase programs of the size of LSAP II are probably unlikely to contribute for more than
half a percentage point to GDP growth and five bp for inflation.
### 6 Conclusions
The effects of recent asset purchase programs on macroeconomic variables, such as GDP
growth and inflation, are likely to be moderate but with a lasting impact on the level of GDP.
We reach this conclusion after simulating LSAP II in an estimated medium-scale DSGE
model, similar to Smets and Wouters (2007). Asset purchase programs are in principle
effective at stimulating the economy because of limits to arbitrage and market segmentation
between short-term and long-term government bonds. The data, however, provide little
support for these frictions to be pervasive.
We consider several robustness exercises and find that the effects on GDP growth are not
very likely to exceed half a percentage point. The inflationary consequences of asset purchase
programs are even smaller. Combining LSAP programs with a commitment to keep interest
rates low for some period of time allows these programs to be about twice as effective in
boosting GDP growth and inflation.
The Macroeconomic Effects of LSAP Programs
Our results do not depend on whether asset purchases are financed via reserves or sales
of short-term debt, to the extent that money and short-term bonds are close to perfect
substitutes. Therefore, according to our model, the effects of the Federal Reserve’s last
round of asset purchases (also known as “Operation Twist Again”) should be in line with
the estimates from LSAP II after controlling for the scale factor.
### 7 References
An, S., and F. Schorfheide. (2007a) “Bayesian Analysis of DSGE Models.” Econometric
Reviews, 26(2-4), 113-172.
Andrés, J., J. López-Salido and E. Nelson. (2004) “Tobin’s Imperfect Asset Substitution
in Optimizing General Equilibrium.” Journal of Money, Credit and Banking, 36(4),
665-690.
Baumeister, C. and L. Benati. (2010) “Unconventional Monetary Policy and the Great
Recession.” European Central Bank Working Paper 1258.
Bomfim, A.N., and L.H. Meyer. (2010) “Quantifying the Effects of Fed Asset Purchases on
Treasury Yields.” Monetary Policy Insights: Fixed Income Focus.
Christiano, L., M. Eichenbaum, and C. Evans. (2005) “Nominal Rigidities and the Dynamic
Effects of a Shock to Monetary Policy.” Journal of Political Economy, 113(1), 1-45.
Chung, Hess, Jean-Philippe Laforte, David Reifschneider, and John C. Williams. (2011)
“Have We Underestimated the Likelihood and Severity of Zero Lower Bound Events?”
Unpublished, Federal Reserve Board and Federal Reserve Bank of San Francisco.
Cúrdia, V., and M. Woodford. (2010) “Credit Spreads and Monetary Policy.” Journal of
Money, Credit and Banking, 42(s1), 3-35.
Cúrdia, V., and M. Woodford. (2011) “The Central-Bank Balance Sheet as an Instrument
of Monetary Policy.” Journal of Monetary Economics, 58, 54-79.
D’Amico, S., W. English, D. López-Salido, and E. Nelson. (2011)“The Federal Reserve’s
The Macroeconomic Effects of LSAP Programs
Large-Scale Asset Purchase Programs: Rationale and Effects.” Unpublished, Federal
Reserve Board.
D’Amico, S., and T. King. (2010) “Flow and Stock Effects of Large-Scale Treasury Pur-
chases.” Finance and Economics Discussion Series No. 2010-52, Federal Reserve Board.
Davig, T., and E. Leeper. (2006) “Fluctuating Macro Policies and the Fiscal Theory.” In
NBER Macroeconomics Annual, edited by D. Acemoglu, K. Rogoff, and M. Woodford.
Del Negro, M., and F. Schorfheide. (2008) “Forming Priors for DSGE Models (and How
it Affects the Assessment of Nominal Rigidities).” Journal of Monetary Economics, 55,
1191-1208.
Doh, T. (2010) “The Efficacy of Large-Scale Asset Purchases at the Zero Lower Bound.”
FRB Kansas City Economic Review, Q2, 5-34.
Eggertsson, Gauti, and Michael Woodford. (2003) “The Zero Bound On Interest Rates and
Optimal Monetary Policy.” Brookings Papers on Economic Activity, 1, 139-211.
Eusepi, Stefano and Bruce Preston. (2011) “The Maturity Structure of Debt, Monetary
Policy and Expectations Stabilization.” Unpublished, Federal Reserve Bank of New
York and Columbia University.
Furher, J. and G. Moore. (1995) “Monetary Policy Trade-offs and the Correlation between
Nominal Interest Rates and Real Output. American Economic Review, 85, 219239.
Gagnon, J., M. Raskin, J. Remache, and B. Sack. (2011) “Large-Scale Asset Purchases by
the Federal Reserve: Did They Work?” FRB New York Staff Reports No. 441.
Gurkaynak, R., B. Sack, and E. Swanson. (2005) “Do Actions Speak Louder Than Words?
The Response of Asset Prices to Monetary Policy Actions and Statements.” International
Journal of Central Banking, 2005, 5593.
Hall, R. (2011) “The Long Slump.” American Economic Review, 101(2), 431-469.
Hamilton, J., and J. Wu. (2010) “The Effectiveness of Alternative Monetary Policy Tools in
a Zero Lower Bound Environment.” Unpublished, University of California at San Diego.
Harrison, R. (2010) “Asset Purchase Policy at the Effective Lower Bound for Interest Rates.”
The Macroeconomic Effects of LSAP Programs
Unpublished, Bank of England.
Justiniano, A., Primiceri, G. and A. Tambalotti (2010) “Investment Shocks and Business
Cycles.” Journal of Monetary Economics, 57(2), 132-145.
Kapetanios, George, Haroon Mumtaz, Ibrahim Stevens, and Konstantinos Theodoris. (2011)
“Assessing the Economy-Wide Effects of Quantitative Easing.” Unpublished, Bank of
England.
Kozicki, S., E. Santor, and L. Suchanek. (2010) “Central Bank Balance Sheets and the
Long-term Forward Rates.” Unpublished, Bank of Canada.
Krishnamurthy A., and A. Vissing-Jorgensen. (2011) “The Effects of Quantitative Easing on
Interest Rates: Channels and Implications for Policy.” Forthcoming, Brookings Papers
on Economic Activity.
Neely, C. (2011) “The large-Scale Asset Purchases Had Large International Effects.” Federal
Reserve Bank of Saint Louis Working Paper.
Smets, F., and R. Wouters. (2003) “An Estimated Dynamic Stochastic General Equilibrium
Model of the Euro Area.” Journal of the European Economic Association, 1(5), 1123-
1175.
Smets, F., and R. Wouters. (2007) “Shocks and Frictions in US Business Cycles: A Bayesian
DSGE Approach.” American Economic Review, 97(3), 586-606.
Swanson, E. T. (2011) “Lets Twist Again: A High-Frequency Event-Study Analysis of Op-
eration Twist and Its Implications for QE2.” Federal Reserve Bank of San Francisco
Working Paper No. 2011-08.
Vayanos, Dimitri, and Jean-Luc Vila. (2009) “A Preferred-Habitat Model of the Term
Structure of Interest Rates.” Unpublished, London School of Economics.
Wallace, N. (1981) “A Modigliani-Miller Theorem for Open-Market Operations.” American
Economic Review, 71, 267-274.
Woodford, Michael. (1998) “Doing without Money: Controlling Inflation in a Post-Monetary
World.” Review of Economic Dynamics, 1, 173-219.
The Macroeconomic Effects of LSAP Programs
Woodford, Michael. (2001) “Fiscal Requirements for Price Stability.” Journal of Money,
Credit and Banking, 33, 669-728.
The Macroeconomic Effects of LSAP Programs
Table 1: Estimated Impact of LSAPs on the 10-Year Treasury Yield in the literature.
Papers Total Impact Impact per $100 Bil Hamilton and Wu (2010) -13 bp -3 bp Doh (2010) -39 bp -4 bp D’Amico and King (2010) -45 bp -15 bp Bomfim and Meyer (2010) -60 bp -3 bp Gagnon et al. (2011) -58 bp to-91 bp -3 bp to-5 bp Neely (2011) -107 bp -6 bp Krishnamurthy and Vissing-Jorgensen (2011) -33 bp (LSAP2) -5 bp D’Amico et al. (2011) -55 bp (LSAP2) -9 bp Swanson (2011) -15 bp (Twist)
The Macroeconomic Effects of LSAP Programs
Table 2: Parameter prior and posterior distribution: structural parameters.
Prior Posterior Dist 5% Median 95% Mode Mean 5% Median 95%
400γG 1.7382 2.4667 3.3752 2.0317 2.0157 1.5722 2.0087 2.4814400πG 1.2545 1.9585 2.8871 2.5634 2.5838 1.9292 2.5807 3.2407
400(β−1u− 1) G 0.6272 0.9792 1.4436 0.6994 0.7850 0.5190 0.7768 1.0745400ζG 0.3913 0.7224 1.2029 0.6261 0.7609 0.4040 0.7373 1.1995S′′ G 2.5090 3.9170 5.7743 4.3392 4.7148 3.2347 4.6481 6.4254a′′G 0.0683 0.1836 0.3877 0.1725 0.2096 0.0850 0.1931 0.3892hB 0.4302 0.6029 0.7597 0.7388 0.7626 0.6216 0.7702 0.8781σuG 0.6832 1.8360 3.8768 3.2522 3.3099 1.8778 3.1781 5.2041σrG 0.6832 1.8360 3.8768 1.5767 2.3182 0.9159 2.1753 4.2176
100ζ′ G 0.3067 1.2846 3.4294 0.8538 1.7312 0.3526 1.4929 3.9085ωuB 0.3214 0.7334 0.9646 0.9872 0.9051 0.7131 0.9336 0.9924
Ξu/ΞrG 0.3416 0.9180 1.9384 0.7836 1.1429 0.4337 1.0726 2.0901Cu/CrG 0.3416 0.9180 1.9384 0.7765 1.0620 0.3912 0.9920 1.9598χwuB 0.2486 0.6143 0.9024 0.6914 0.5895 0.2494 0.6031 0.8877νG 1.2545 1.9585 2.8871 1.5728 1.8523 1.1603 1.8092 2.7035ζwB 0.5701 0.7595 0.8971 0.8194 0.8751 0.7968 0.8780 0.9411ζpB 0.5701 0.7595 0.8971 0.9402 0.9436 0.9294 0.9438 0.9570φTG 0.7825 1.4448 2.4058 1.2329 1.4772 0.7755 1.4209 2.3627ρrB 0.5242 0.7068 0.8525 0.8453 0.8557 0.8190 0.8563 0.8902φπG 1.0164 1.7026 2.6453 1.7598 1.7790 1.4585 1.7711 2.1303φyG 0.1366 0.3672 0.7754 0.2943 0.3318 0.2533 0.3270 0.4269
The Macroeconomic Effects of LSAP Programs
Table 3: Parameter prior and posterior distribution: shock process parameters.
Prior Posterior Dist 5% Median 95% Mode Mean 5% Median 95%
ρzB 0.0976 0.3857 0.7514 0.1441 0.1672 0.0506 0.1617 0.3039ρµB 0.5701 0.7595 0.8971 0.8503 0.8676 0.8084 0.8691 0.9218ρbB 0.5701 0.7595 0.8971 0.9697 0.9628 0.9366 0.9665 0.9794ρφB 0.5701 0.7595 0.8971 0.5193 0.4707 0.3389 0.4714 0.5991ρBB 0.6146 0.8135 0.9389 0.8465 0.8278 0.6298 0.8459 0.9592ρζB 0.6146 0.8135 0.9389 0.9454 0.9077 0.7724 0.9264 0.9656ρgB 0.5701 0.7595 0.8971 0.7889 0.7449 0.5690 0.7514 0.8977σzIG1 0.1663 0.3433 1.2367 0.7451 0.7643 0.6737 0.7604 0.8671σλfIG1 0.1663 0.3433 1.2367 2.5283 3.1068 1.7820 2.9146 5.0335σµIG1 0.1663 0.3433 1.2367 2.6621 2.8190 2.0830 2.7858 3.6875σbIG1 0.1663 0.3433 1.2367 4.7382 6.6897 3.7437 6.2078 11.2378σφIG1 0.1663 0.3433 1.2367 1.4242 6.0173 1.1346 3.9569 18.2035σBIG1 0.1663 0.3433 1.2367 0.2352 0.5506 0.1717 0.3883 1.5258σTIG1 0.1663 0.3433 1.2367 0.2351 0.4774 0.1679 0.3452 1.3151σmIG1 0.0819 0.1700 0.6217 0.1150 0.1164 0.1022 0.1159 0.1325σζIG1 0.0819 0.1700 0.6217 0.2385 0.2642 0.1321 0.2564 0.4178σgIG1 0.1663 0.3433 1.2367 0.2446 0.4124 0.1723 0.3638 0.8140
The Macroeconomic Effects of LSAP Programs
Figure 1: Simulated path of the market value of long-term debt, in percentage deviations from trend. (Calibrated to imply a median reduction of 30bp (annualized) in the risk premium.
0 4 8 12 16 20 24 −14
−12
−10
−8
−6
−4
−2
0 Long term debt (MV)
The Macroeconomic Effects of LSAP Programs
Figure 2: Responses to simulated shock to market value of long-term debt (shown in Figure 1), accounting for a commitment to the zero lower bound for four quarters, using the prior distribution. All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the prior median response and the grey shades to different prior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading).
0 4 8 12 16 20 24 0
5
10
Output Growth
0 4 8 12 16 20 24 0
2
4
Output Level
0 4 8 12 16 20 24 0
1
2
3
4
Inflation
0 4 8 12 16 20 24 0
1
2
FFR
0 4 8 12 16 20 24
−0.4
−0.2
0
0.2
0.4
10Yr Yield
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 3: Responses to simulated shock to market value of long-term debt (shown in Figure 1), accounting for a commitment to the zero lower bound for four quarters, using the posterior distribution. All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading).
0 4 8 12 16 20 24 0
0.5
1
1.5
Output Growth
0 4 8 12 16 20 24 0
0.5
1
1.5
Output Level
0 4 8 12 16 20 24
0
0.05
0.1
0.15
Inflation
0 4 8 12 16 20 24
0
0.1
0.2
0.3
0.4
FFR
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0
10Yr Yield
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 4: Responses to simulated shock to market value of long-term debt (shown in Figure 1), in the absence of a commitment to the zero lower bound. All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24
0
0.2
0.4
0.6
0.8 Output Growth
0 4 8 12 16 20 24 0
0.2
0.4
0.6
Output Level
0 4 8 12 16 20 24
0
0.02
0.04
0.06
Inflation
0 4 8 12 16 20 24 0
0.1
0.2
0.3
FFR
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 10Yr Yield
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 5: Responses to simulated shock to market value of long-term debt (shown in Figure 1), accounting for a commitment to the zero lower bound for six quarters. All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24 0
2
4
6
8 Output Growth
0 4 8 12 16 20 24 0
2
4
6
Output Level
0 4 8 12 16 20 24 0
0.2
0.4
0.6
0.8 Inflation
0 4 8 12 16 20 24
0
0.5
1
FFR
0 4 8 12 16 20 24 −0.8
−0.6
−0.4
−0.2
0
10Yr Yield
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 6: Responses to 50bp (annualized) temporary reduction in the FFR. All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24 0
0.2
0.4
0.6
Output Growth
0 4 8 12 16 20 24 0
0.2
0.4
Output Level
0 4 8 12 16 20 24
0
0.02
0.04
Inflation
0 4 8 12 16 20 24
−0.4
−0.3
−0.2
−0.1
0
FFR
0 4 8 12 16 20 24
−0.2
−0.1
0
10Yr Yield
0 4 8 12 16 20 24 −0.3
−0.2
−0.1
0
Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 7: Responses to simulated shock to market value of long-term debt (shown in Figure 1) in the presence of a high degree of market segmentation (by considering the lower half of the distribution ofωu).All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24 0
1
2
3
Output Growth
0 4 8 12 16 20 24 0
1
2
3
Output Level
0 4 8 12 16 20 24 0
0.1
0.2
0.3
Inflation
0 4 8 12 16 20 24 0
0.2
0.4
0.6
0.8
FFR
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0
10Yr Yield
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 8: Responses to simulated shock to market value of long-term debt (shown in Figure 1) in the presence of lower price rigidities(ζp=0.75).All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24 0
0.5
1
1.5
Output Growth
0 4 8 12 16 20 24 0
0.5
1
Output Level
0 4 8 12 16 20 24 0
0.2
0.4
Inflation
0 4 8 12 16 20 24
0
0.1
0.2
0.3
FFR
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 10Yr Yield
0 4 8 12 16 20 24
−0.6
−0.4
−0.2
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 9: Responses to simulated shock to market value of long-term debt (shown in Figure 1) in the case in which the central bank keeps the purchased assets for four years (instead of two). All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24 0
1
2
Output Growth
0 4 8 12 16 20 24 0
1
2
Output Level
0 4 8 12 16 20 24 0
0.1
0.2
Inflation
0 4 8 12 16 20 24 0
0.2
0.4
0.6
FFR
0 4 8 12 16 20 24
−0.8
−0.6
−0.4
−0.2
0 10Yr Yield
0 4 8 12 16 20 24
−1
−0.5
0 Risk Premium
The Macroeconomic Effects of LSAP Programs
Figure 10: Responses to simulated shock to market value of long-term debt in the case of estimation with observed ratio between long and short debt. Path of shock is the same as in Figure 1) but the size of the shock is chosen to simulate a $600bn reduction in long-term bonds available to the public. All responses are in annualized percentage rates (except the output level, shown in percentage deviations from the path in the absence of the shock). Red line corresponds to the posterior median response and the grey shades to different posterior probability intervals (50, 60, 70, 80 and 90 percent, from darker to lighter shading). The dashed blue line is the median response of the variables in the baseline simulation, shown in 3.
0 4 8 12 16 20 24 0
0.2
0.4
0.6
Output Growth
0 4 8 12 16 20 24 0
0.2
0.4
Output Level
0 4 8 12 16 20 24
0
0.02
0.04
0.06
Inflation
0 4 8 12 16 20 24
0
0.05
0.1
0.15
FFR
0 4 8 12 16 20 24
−0.2
−0.1
0
10Yr Yield
0 4 8 12 16 20 24 −0.3
−0.2
−0.1
0
Risk Premium