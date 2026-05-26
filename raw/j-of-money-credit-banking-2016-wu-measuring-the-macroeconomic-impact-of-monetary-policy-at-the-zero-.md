
JING CYNTHIA WU
FAN DORA XIA
Measuring the Macroeconomic Impact of Monetary
Policy at the Zero Lower Bound
This paper employs an approximation that makes a nonlinear term structure model extremely tractable for analysis of an economy operating near the zero lower bound for interest rates. We show that such a model offers an excellent description of the data compared to the benchmark model and can be used to summarize the macroeconomic effects of unconventional monetary policy. Our estimates imply that the efforts by the Federal Reserve to stimulate the economy since July 2009 succeeded in making the unemployment rate in December 2013 1% lower, which is 0.13% more compared to the historical behavior of the Fed.
*JEL*codes: E43, E44, E52, E58 Keywords: monetary policy, shadow federal funds rate, zero lower bound,
dynamic term structure model, unemployment.
HISTORICALLY THE FEDERAL RESERVE (hereafter, the “Fed”) has used the federal funds rate as the primary instrument of monetary policy, lowering the rate to provide more stimulus and raising it to slow economic activity and control inflation. But since December 2008, the federal funds rate has been near zero, so that lowering it further to produce more stimulus has not been an option. Consequently, the Fed has relied on unconventional policy tools such as large-scale asset purchases
We have benefited from extensive discussions with Jim Hamilton and Drew Creal. We also thank Jim Bullard, John Cochrane, Greg Duffee, Benjamin Friedman, Refet Gurkaynak, Kinda Hachem, Anil Kashyap, Leo Krippner, Randy Kroszner, Jun Ma, David Romer, Glenn Rudebusch, Jeff Russell, Frank Schorfheide, Matthew Shapiro, Eric Swanson, Ruey Tsay, Ken West, Johannes Wieland, John Williams, three anonymous referees, and seminar and conference participants at Chicago Booth, UCSD, NBER Sum-mer Institute Monetary Economics Workshop, St. Louis Fed Applied Time Series Econometrics Workshop, FRBSF ZLB workshop, Second BIS Research Network Meeting, Atlanta Fed, Boston Fed, Chicago Fed, Dallas Fed, and Kansas City Fed for helpful suggestions. Cynthia Wu gratefully acknowledges financial support from the IBM Faculty Research Fund at the University of Chicago Booth School of Business.
JING CYNTHIA WU*is an Associate Professor at The University of Chicago Booth School of Business and NBER (E-mail:*cynthia.wu@chicagobooth.edu). FAN DORA XIA*is a U.S. Rates Strategist at the Bank of America Merrill Lynch (E-mail:*dora.xia@baml.com).*The work was done when Xia attended University of California San Diego Economics Ph.D. program.*
Received August 6, 2014; and accepted in revised form June 30, 2015.
*Journal of Money, Credit and Banking,*Vol. 48, No. 2–3 (March–April 2016) C© 2016 The Ohio State University
254 : MONEY, CREDIT AND BANKING
(commonly known as quantitative easing [QE]) and forward guidance to try to affect long-term interest rates and influence the economy. Assessing the impact of these measures or summarizing the overall stance of monetary policy in the new environ-ment has proven to be a big challenge. Previous efforts include Gagnon et al. (2011), Hamilton and Wu (2012), Krishnamurthy and Vissing-Jorgensen (2011), D’Amico and King (2013), Wright (2012), Bauer and Rudebusch (2014), and Swanson and Williams (2014). However, these papers focused only on measuring the effects on the yield curve. In contrast, the goal of this paper is to assess the overall effects on the economy.
A related challenge has been to describe the relations between the yields on assets of different maturities in the new environment. The workhorse model in the term structure literature has been the Gaussian affine term structure model (GATSM); for surveys, see Piazzesi (2010), Duffee (2013), Gürkaynak and Wright (2012), and Diebold and Rudebusch (2013). However, because this model is linear in Gaussian factors, it potentially allows nominal interest rates to go negative and faces real difficulties in the zero lower bound (ZLB) environment. One approach that could potentially prove helpful for measuring the stance of unconventional monetary policy and describing the relations between different yields is the shadow rate term structure model (SRTSM) first proposed by Black (1995). This model posits the existence of a shadow interest rate that is linear in Gaussian factors, with the actual short-term interest rate the maximum of the shadow rate and zero. However, the fact that an analytical solution to this model is known only in the case of a one-factor model makes using it more challenging.
In this paper we propose a simple analytical representation for bond prices in the multifactor SRTSM that provides an excellent approximation and is extremely tractable for analysis and empirical implementation. It can be applied directly to discrete-time data to gain immediate insights into the nature of the SRTSM’s predictions. We demonstrate that this model offers an excellent empirical de-scription of the recent behavior of interest rates, as compared to the benchmark GATSM.
More importantly, we show using a simple factor-augmented vector autoregression (FAVAR) that the shadow federal funds rate calculated by our model exhibits similar dynamic correlations with macro variables of interest in the period since July 2009 as the federal funds rate did in data prior to the Great Recession. This result provides us with a tool to measure the effects of monetary policy at the ZLB and offers an important insight to the empirical macro literature where people use the federal funds rate in vector autoregressive (VAR) models to study the relationship between mon-etary policy and the macroeconomy. Examples of this literature include Christiano, Eichenbaum, and Evans (1999), Stock and Watson (2001), and Bernanke, Boivin, and Eliasz (2005). The evident structural break in the federal funds rate prevents researchers from extracting meaningful information out of a VAR once the data cover the ZLB period. In contrast, the continuity between our shadow federal funds rate and
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 255
the actual federal funds rate allows researchers to update their favorite VAR during and post the ZLB period.1
We show that the Fed has used unconventional policy measures to successfully lower the shadow federal funds rate, and these measures have been more stimulative than a historical version of the Taylor rule. Our estimates imply that the Fed’s efforts to stimulate the economy since July 2009 have succeeded in lowering the unemployment rate by 1% in December 2013, which is 0.13% more compared to the historical behavior of the Fed.
The SRTSM has been used to describe the recent behavior of interest rates and monetary policy by Kim and Singleton (2012) and Bauer and Rudebusch (2013), but these authors relied on simulation methods to estimate and study the model. Krippner (2013) proposed a continuous-time analog to our solution, where he added a call option feature to derive the solution. Ichiue and Ueno (2013) approximate bond prices by ignoring Jensen’s inequality. Both derivations are in continuous time, which requires numerical integration when applied to discrete-time data.
Our paper also contributes to the recent discussion on the usefulness of the shadow rate as a measure for the stance of monetary policy. Christensen and Rudebusch (2014) and Bauer and Rudebusch (2013) pointed out that the estimated shadow rate varied across different models. We confirm that different model choices do influence the level of the shadow rate. However, the common dynamics among different shadow rates point to the same economic conclusion. We also demonstrate that the shadow rate is a powerful tool to summarize useful information at the ZLB. Therefore, our evidence further supports the view expressed by Bullard (2012) and Krippner (2012), who advocated the potential of the shadow rate to describe the monetary policy stance. Recent work by Lombardi and Zhu (2014) shares the same view with a shadow rate constructed from a factor model with a large information set.
The rest of the paper proceeds as follows. Section 1 describes the SRTSM. Section 2 proposes to use the shadow rate to measure the monetary policy at the ZLB. Section 3 summarizes the implication of unconventional monetary policy on the macroeconomy using historical data from 1960 to 2013, and Section 4 zooms in on the ZLB period and analyzes forward guidance and QE. Section 5 extends the robustness of our results to different model specifications, and Section 6 concludes.
1. SHADOW RATE TERM STRUCTURE MODEL
*1.1 Shadow Rate*
Similar to Black (1995), we assume that the short-term interest rate is the maximum of the shadow rate*st*and a lower bound*r*:
*rt*=*max(r , st ).*(1)
1. Our shadow rate data with monthly update are available at the Atlanta Fed (https://www. frbatlanta.org/cqer/research/shadow_rate.aspx) or our webpage (http://faculty.chicagobooth.edu/jing.wu/ research/data/WX.html).
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
256 : MONEY, CREDIT AND BANKING
If the shadow rate*st*is greater than the lower bound, then*st*is the short rate. Note that when the lower bound is binding, the shadow rate contains more information about the current state of the economy than does the short rate itself. Since the end of 2008, the Fed has paid interest on reserves at an annual interest rate of 0.25%, proposing the choice of*r*=*0.25%.2*
*1.2 Factor Dynamics and Stochastic Discount Factor*
We assume that the shadow rate*st*is an affine function of some state variables*Xt*,
*st*=δ0+δ′1*Xt .*(2)
The state variables follow a first-order vector autoregressive process (VAR(1)) under the physical measure (P):
*Xt+1*=μ+ρ*Xt*+$εt+1, εt+1 $∼*N (0, I ).*(3)
The log stochastic discount factor is essentially affine as in Duffee (2002)
log*Mt+1*=*−rt*− 1
2λ′
tλt−λ′tεt+1,(4)
where the price of riskλtis linear in the factors
λt=λ0+λ1*Xt .*
This implies that the dynamics for the factors under the risk neutral measure (Q) are also a VAR(1):
*Xt+1*=μQ+ρQ*Xt*+$ε $Q*t+1,*ε
Q*t+1*
Q∼*N (0, I ).*(5)
The parameters under the P and Q measures are related as follows:
μ−μQ=$λ0, $
ρ−ρQ=$λ1. $
*1.3 Forward Rates*
Equation (1) introduces nonlinearity into an otherwise linear system. A closed-form pricing formula for the SRTSM described in Sections 1.1 and 1.2 is not available beyond one factor. In this section, we propose an analytical approximation for the forward rate in the SRTSM, making the otherwise complicated model extremely tractable. Our formula is simple and intuitive, and we will compare it to the solution
2. Our main results are robust if we estimate*r*as a free parameter; see Section 5 for detailed discussion.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 257
from a Gaussian model in Section 1.4. A simulation study in Section 1.6 demonstrates that the error associated with our approximation is only a few basis points.
Define*fn,n+1,t*as the forward rate at time*t*for a loan starting at*t*+*n*and maturing at*t*+*n*+ 1,
*fn,n+1,t*=*(n*+*1)yn+1,t*−*nynt ,*(6)
which is a linear function of yields on risk-free*n*and*n*+ 1 period pure discount bonds. The forward rate in the SRTSM described by equations (1) to (5) can be approximated with
*f SRTSM n,n+1,t*=*r*+σQ
*n g*
(*an*+*b′*
*n Xt*−*r*
σQ*n*
)*,*(7)
where(σQ*n*)2≡*VarQ*
*t (st+n).*The function*g(z)*≡*z(z)*+φ(z)consists of a nor-mal cumulative distribution function*(.)*and a normal probability density functionφ(.).Its nonlinearity comes from moments of the truncated normal distribution. The expressions for*an*,*bn*andσQ
*n*as well as the derivation are in Appendix A. To our knowledge, we are the first in the literature to propose an analytical ap-
proximation for the forward rate in the SRTSM that can be applied to discrete-time data directly. For example, Bauer and Rudebusch (2013) used a simulation-based method. Krippner (2013) proposed an approximation for the instantaneous forward rate in continuous time. To apply his formula to the 1-month ahead forward rate in the data, a researcher needs to numerically integrate the instantaneous forward rate over that month; see Christensen and Rudebusch (2014) for example. Conversely, our discrete-time formula can be applied directly to the data. In summary, our analytical approximation is free of any numerical error associated with simulation methods and numerical integration.
*1.4 Relation to Gaussian Affine Term Structure Models*
If we replace equation (1) with
*rt*=*st ,*
the SRTSM becomes a GATSM, the benchmark model in the term structure literature. The forward rate in the GATSM is an affine function of the factors:
*f GATSM n,n+1,t*=*an*+*b′*
*n Xt ,*(8)
where*an*and*bn*are the same as in equation (7), and the detailed expressions are in Appendix A.
The difference between (7) and (8) is the function*g(.).*We plot it in Figure 1 together with the 45-degree line. It is a nonlinear and increasing function. The function value is indistinguishable from the 45-degree line for inputs greater than 2,
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
258 : MONEY, CREDIT AND BANKING
−5 −4 −3 −2 −1 0 1 2 3 4 5 0
1
2
3
4
5
z
y
y = g(z) y = z
FIG. 1. The Function*g(.).*
NOTES: Solid dark gray curve: the function*g(z)*=*z(z)*+φ(z).Light gray dashed line: the 45-degree line.
and is practically zero for*z*less than −2. The limiting behavior demonstrates that the GATSM is a simple and close approximation for the SRTSM, when the economy is away from the ZLB.
*1.5 Estimation*
*State space representation for the SRTSM.*We write the SRTSM as a nonlinear state space model. The transition equation for the state variables is equation (3). From equation (7), the measurement equation relates the observed forward rate*f o*
*n,n+1,t*to the factors as follows:
*f o n,n+1,t*=*r*+σQ
*n g*
(*an*+*b′*
*n Xt*−*r*
σQ*n*
) +ηnt*,*(9)
where the measurement errorηntis i.i.d. normal,ηnt∼*N (0,*ω).The observation equation is not linear in the factors. We use the extended Kalman filter for estimation, which applies the Kalman filter by linearizing the nonlinear function*g(.)*around the current estimates. See Appendix B for details.
The extended Kalman filter is extremely easy to apply due to the closed-form formula in equation (7). We take the observation equation (9) directly to the data without any further numerical approximation, which is necessary for pricing formulas derived in continuous time. The likelihood surface behaves similarly to a GATSM, because the function*g(.)*is monotonically increasing. These features together make our formula appealing.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 259
1990 1992 1994 1996 1998 2000 2002 2004 2006 2008 2010 2012 2014 0
1
2
3
4
5
6
7
8
9
10 3m 6m 1y 2y 5y 7y 10y
FIG. 2. Forward Rates.
NOTES: One-month forward rates monthly from January 1990 to December 2013, measured in annualized percentage points. Maturities are 3 and 6 months, 1, 2, 5, 7, and 10 years. The gray area marks the ZLB period from January 2009 to December 2013.
*State space representation for the GATSM.*For the GATSM described in Section 1.4, equation (3) is still the transition equation. Equation (8) implies the measurement equation:
*f o n,n+1,t*=*an*+*b′*
*n Xt*+ηnt*,*(10)
withηnt∼*N (0,*ω).We apply the Kalman filter for the GATSM, because it is a linear Gaussian state space model. See Appendix B for details.
*Data.*We construct 1-month forward rates for maturities of 3 and 6 months, 1, 2, 5, 7, and 10 years from the Gürkaynak, Sack, and Wright (2007) data set, using observations at the end of the month.3 Our sample spans from January 1990 to December 2013.4 We plot the time series of these forward rates in Figure 2. In December 2008, the Federal Open Market Committee (FOMC) lowered the target range for the federal funds rate to 0 to 25 basis points. We refer to the period from January 2009 to the end of the sample as the ZLB period and highlight with shaded area. For this period, forward rates of shorter maturities are essentially stuck at zero,
3. As a robustness check, we also estimate the SRTSM and extract the shadow rate with Fama and Bliss (1987) zero coupon bond data from CRSP, and we get similar results. See Section 5 for detailed discussion.
4. Starting the sample from 1990 is standard in the GATSM literature, see Wright (2011) and Bauer, Rudebusch, and Wu (2012) for examples.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
260 : MONEY, CREDIT AND BANKING
and do not display meaningful variation. Those with longer maturities are still far away from the lower bound, and display significant variation.
*Normalization.*The consensus in the term structure literature is that three factors are sufficient to account for almost all of the cross-sectional variation in yields. Therefore, we focus our discussion on three factor models.5 The collection of parameters we estimate include(μ,μQ,ρ,ρQ,*,*δ0,δ1).For identification, we impose normalizing restrictions on the Q parameters similar to Joslin, Singleton, and Zhu (2011) and Hamilton and Wu (2014): (i)δ1=*[1, 1,*0]′, (ii)μQ= 0, (iii)ρQis in real Jordan form with eigenvalues in descending order, and (iv)**is lower triangular. Note that these restrictions are for statistical identification only, that is, they prevent the latent factors from shifting, rotating, and scaling. Imposing this or other sets of restrictions does not change economic implications of the model.
*Repeated eigenvalues.*Estimation assuming thatρQhas three distinct eigenvalues produces two smaller eigenvalues almost identical to each other, with the difference in the order of 10−3. This evidence points to repeated eigenvalues. Creal and Wu (2015) have documented a similar observation using a different data set and a different model. With repeated eigenvalues, the real Jordan form becomes
ρQ=⎡⎣ρ
Q 1 0 0 0ρ
Q 2 1
0 0ρQ 2
⎤⎦*.*
*Model comparison.*Maximum likelihood estimates, and robust standard errors (see Hamilton 1994, p. 145) are reported in Table 1. The log likelihood value is 755.46 for the GATSM, and 855.57 for the SRTSM. The superior performance of the SRTSM comes from its ability to fit the short end of the forward curve when the lower bound binds. In Figure 3, we plot average observed (red dots) and fitted (blue curves) forward curves in 2012. The left panel illustrates that the SRTSM fitted forward curve flattens at the short end, because the*g(.)*function is very close to zero when the input is sufficiently negative. This is consistent with the feature of the data. In contrast, the GATSM in the right panel has trouble fitting the short end. Instead of having a flat short end as the data suggest, the GATSM generates too much curvature. That is the only way it can approximate the yield curve at the ZLB.
As demonstrated in Section 1.4, the GATSM and the SRTSM are approximately the same when forward rates are sufficiently higher than the lower bound. We illustrate this property using the following numerical example. When both models are estimated over the period of January 1990 to December 1999, the maximum log likelihood is 475.71 for the SRTSM, and 476.69 for the GATSM. The slight difference in the likelihood comes from the linear approximation of the extended Kalman filter.
5. All of our main results relating to the macroeconomy, from Section 2 onward, are robust to two-factor models, see Section 5 for further discussion. But for the term structure models themselves, two-factor models perform worse than three-factor models in terms of fitting the data.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 261
TABLE 1
MAXIMUM LIKELIHOOD ESTIMATES WITH ROBUST STANDARD ERRORS
SRTSM GATSM
1200μ−0.3035 −0.2381 0.0253 −0.2296 −0.2069 0.0185 (0.1885) (0.1815) (0.0160) (0.1464) (0.1413) (0.0115)
ρ0.9638 −0.0026 0.3445 0.9676 −0.0043 0.4854 (0.0199) (0.0183) (0.4821) (0.0184) (0.0200) (0.5408)
−0.0226 0.9420 1.0152 −0.0231 0.9333 1.0143 (0.0202) (0.0212) (0.5111) (0.0185) (0.0227) (0.5519) 0.0033 0.0028 0.8869 0.0030 0.0028 0.8935
(0.0018) (0.0019) (0.0385) (0.0015) (0.0020) (0.0423)eig(ρ)0.9832 0.9642 0.8452 0.9870 0.9627 0.8448
ρQ0.9978 0 0 0.9967 0 0 (0.0003) (0.0003)
0 0.9502 1 0 0.9503 1 (0.0012) (0.0012)
0 0 0.9502 0 0 0.9503 (0.0012) (0.0012)
1200δ013.3750 11.6760 (1.0551) (0.5591)
*1200*0.4160 0.4744 (0.0390) (0.0497)
−0.3999 0.2445 −0.4589 0.2175 (0.0369) (0.0233) (0.0447) (0.0188)
−0.0110 0.0033 0.0390 −0.0167 0.0013 0.0359 (0.0069) (0.0034) (0.0030) (0.0062) (0.0029) (0.0026)
1200√
ω0.0893 0.0927 (0.0027) (0.0027)
Log-likelihood value 855.5743 755.4587
NOTES: Maximum likelihood estimates for the three-factor SRTSM and the three-factor GATSM with robust standard errors in parentheses. Sample: January 1990 to December 2013.
1 2 5 7 10 0
0.5
1
1.5
2
2.5
3
3.5
4 SRTSM
fitted observed
1 2 5 7 10 0
0.5
1
1.5
2
2.5
3
3.5
4 GATSM
fitted observed
FIG. 3. Observed and Fitted Forward Curves.
NOTES: Average forward curves in 2012. Gray curves: fitted forward curves, from the SRTSM in the left panel and the GATSM in the right panel. Gray dots: observed data. X-axis: maturity in years.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
262 : MONEY, CREDIT AND BANKING
*1.6 Approximation Error*
An alternative to equation (7) to compute forward rates or yields is simulation. We compare forward rates and yields implied by equation (7) and by an average of 10 million simulated paths to measure the size of the approximation error.6 The approximation errors grow with the time to maturity for forward rates and yields. We focus on the longest end to report the worst case scenario. The average absolute approximation error of the 24 Januaries between 1990 and 2013 for the 10-year ahead forward rate is 2.3 basis points, about 0.36% of the average forward rate for this period (6.37%). The number is 0.78 basis points for the 10-year yield with an average level of 5.29%, yielding a ratio of 0.14%. The approximation errors for long-term forward rates are larger than those for yields, because yields factor in the smaller approximation errors of short-term and medium-term forward rates. Regardless, the approximation errors are at most a few basis points, orders of magnitude smaller than the level of interest rates. Although these numbers contain simulation errors, with the large number of draws (10 million), the simulation error is negligible. To show that, we compare the analytical solution in equation (8) for the GATSM with simulation. The average absolute simulation errors are 0.1 basis points for the 10-year ahead forward rate and 0.04 for the 10-year yield.
2. POLICY RATE
The federal funds rate has been the primary measure for the Fed’s monetary policy stance and has provided the basis for most empirical studies of the interaction be-tween monetary policy and the economy. However, since 2009, it has been stuck at the lower bound and no longer conveys any information. How do we summarize the effects of monetary policy in this situation? Most research has focused on the ZLB subperiod. The issue with this approach is that it throws out a half century of valuable historical data. Moreover, how do we move forward after the economy exits the ZLB and the short rate regains its role as the summary for monetary policy? Is there a way economists can keep using the long historical data, with the presence of the ZLB period? The shadow rate from the SRTSM is a potential solution. Section 2.2 demon-strates that the shadow federal funds rate interacts with macro variables similarly as the federal funds rate did historically. Section 4.1 reinforces this key result.
We construct a new policy rate*so t*by splicing together the effective federal funds
rate (EFFR) before 2009 and the estimated shadow federal funds rate since 2009. This combination makes the most use out of both series. We plot the model im-plied shadow rate (in blue) and the EFFR rate (in green) in Figure 4. Before 2009, the ZLB was not binding, the model implied short rate was equal to the shadow rate. The difference between the two lines in Figure 4 reflects measurement error,
6. At time*t*, we simulate 10 million paths of*st+ j*for*j*=*1, ...,*120 with the estimated factors*Xt*and Q parameters, and compute*rt+ j*based on equation (1). Then we compute the corresponding 10 million*ynt*= − 1
*n*log(EQ
*t [exp(−rt*−*rt+1*−*...*−*rt+n−1)])*and then*fn,n+1,t*using (6). We take the average of the 10 million draws as the simulated yield or forward rate.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 263
1990 1992 1994 1996 1998 2000 2002 2004 2006 2008 2010 2012 2014
−2
0
2
4
6
8
10 shadow rate effective federal funds rater
FIG. 4. The Shadow Rate and Effective Federal Funds Rate.
NOTES: Solid gray line: the estimated shadow rate of the SRTSM from January 1990 to December 2013 in percentage points. Light gray dashed line: the EFFR in percentage points. Black dashed line: lower bound*r*. The gray area marks the ZLB period from January 2009 to December 2013.
in units of basis points. The two rates have diverged since 2009. The EFFR has been stuck at the ZLB. In contrast, the shadow rate has become negative and still displays meaningful variation. We update our shadow federal funds rate monthly at http://faculty.chicagobooth.edu/jing.wu/research/data/WX.html.
*2.1 Factor Augmented Vector Autoregression*
We use the factor augmented vector autoregression (FAVAR) model proposed by Bernanke, Boivin, and Eliasz (2005) to study the effects of monetary policy. The basic idea of the FAVAR is to compactly summarize the rich information contained in a large set of economic variables*Y m*
*t*using a low-dimensional vector of factors*xm*
*t*. This model allows us to study monetary policy’s impact on any macroeconomic variable in the data set. The factor structure also ensures that the number of parameters remains manageable.
*Model.*Following Bernanke, Boivin, and Eliasz (2005), we use three macro factors and assume that the factors*xm*
*t*and the policy rate*so t*jointly follow a VAR(13):7[
*xm t*
*so t*
] = [
μx
μs
] +ρm
[*Xm*
*t−1 So*
*t−1*
] +*m*
[εm
*t*εMP
*t*
]*,*
[εm
*t*εMP
*t*
] ∼*N (0, I ),*(11)
where we summarize the current value of*xm t*(and*so*
*t*) and its 12 lags using a capital letter to capture the state of the economy,*Xm*
*t*=*[xm′ t , xm′*
*t−1, ..., xm′ t−12]′*(and
*So t*=*[so*
*t , so t−1, ..., so*
*t−12]′).*Constantsμxandμsare the intercepts, andρmis the
7. Our results hold with different numbers of factors (3 or 5) and with different lag lengths (6, 7, 12, or 13), see Section 5 for further discussion.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
264 : MONEY, CREDIT AND BANKING
autoregressive matrix. The matrix*m*is the cholesky decomposition of the covari-ance matrix. The monetary policy shock isεMP
*t*. We identify the monetary policy shock through the recursiveness assumption as in Bernanke, Boivin, and Eliasz (2005); for details see Appendix C. Observed macroeconomic variables load on the macroeco-nomic factors and policy rate as follows:
*Y m t*=*am*+*bx xm*
*t*+*bsso t*+ηm
*t ,*ηm*t*∼*N (0,),*(12)
where*am*is the intercept, and*bx*and*bs*are factor loadings.
*Data.*Similar to Bernanke, Boivin, and Eliasz (2005),*Y m t*consists of a balanced
panel of 97 macroeconomic time series from the Global Insight Basic Economics, and our data span from January 1960 to December 2013.8 We have a total of*T*= 635 observations. We apply the same data transformations as in the original paper to ensure stationarity. Detailed data description can be found in the Online Appendix (http://faculty.chicagobooth.edu/jing.wu/).
*Estimation.*First, we extract the first three principal components of the observed macroeconomic variables over the period of January 1960 to December 2013 and take the part that is orthogonal to the policy rate as the macroeconomic factors. Then, we estimate equation (12) by ordinary least squares (OLS). See Appendix C for details. Next, we estimate equation (11) by OLS.
*Macroeconomic variables and factors.*The loadings of the 97 macro variables on the factors are plotted in Figure 5. Real activity measures load heavily on factor 1, price level indexes load more on factor 2, and factor 3 contributes primarily to employment and prices. For the contemporaneous regression in equation (12), more than one third of the variables have an*R2*above 60%, which confirms the three-factor structure. Besides the policy rate, we focus on the following five macroeconomic variables: industrial production, consumer price index, capacity utilization, unemployment rate, and housing starts. They represent the three factors and cover real activity and price levels. The*R2s*for these macroeconomic variables are 73%, 89%, 64%, 64%, and 67%, respectively.
*2.2 Measures of Monetary Policy*
The natural question is whether the shadow rate could be used in place of the federal funds rate to describe the stance and effects of monetary policy at the ZLB. We first approach this using a formal hypothesis test—can we reject the hypothesis that the parameters relating the shadow federal funds rate to macroeconomic variables of interest at the ZLB are the same as those that related the federal funds rate to those variables in normal times?
We begin this exercise by acknowledging that we do not attempt to model the Great Recession in our paper, because it was associated with some extreme financial
8. Global Insight Basic Economics does not maintain all 120 series used in Bernanke, Boivin, and Eliasz (2005). Only 97 series are available from January 1960 to December 2013. The main results from Bernanke, Boivin, and Eliasz (2005) can be replicated by using the 97 series in our paper for the same sample period.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 265
−2
0
2 Loadings on macro factor 1
−4
0
4 Loadings on macro factor 2
−3
0
3 Loadings on macro factor 3
0 10 20 30 40 50 60 70 80 90 100 −2
0
2 Loadings on policy rate
FIG. 5. Loadings on the Macroeconomic Factors and Policy Rate.
NOTES: Loadings of standardized economic variables*Y m t*on the three macroeconomic factors and the standardized
policy rate. X-axis: identification number for economic variables in the Online Appendix (http://faculty.chicagobooth. edu/jing.wu/). Vertical dashed lines separate variables by groups, and the groups are real output (1–18); employment and hours (19–42); consumption (43–46); housing starts and sales (47–53); real inventories, orders, and unfilled orders (54–58); stock prices (59–60); exchange rates (61–62); interest rates (63–73); money and credit quantity aggregates (74–79); price indexes (80–94); average hourly earnings (95–96); miscellaneous (97).
events and monetary policy responses. For example, Ng and Wright (2013) provided some empirical evidence that the Great Recession is different in nature from other postwar recessions. Instead, we are interested in the behavior of monetary policy and the economy in the period following the Great Recession, when policy returned to a new normal that ended up being implemented through the traditional 6-week FOMC calendar but using the unconventional tools of large-scale asset purchases and forward guidance. We investigate whether a summary of this new normal based on our derived shadow federal funds rate shows similar dynamic correlations as did the federal funds rate in the period prior to the Great Recession.
We rewrite the first block for*xm t*in (11)
*xm t*=μx+ρxx*Xm*
*t−1*+**1(t<December**2007)ρ*xs*1*So*
**t−1+1(December**2007≤t≤June2009)ρ*xs*2*So*
*t−1*
+**1(t>June**2009)ρ*xs*3*So*
*t−1*+$xxεm $*t .*(13)
The null hypothesis is that the matrixρxsis the same before and after the Great Recession:
*H0*:ρxs1 =ρxs
3*.*
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
266 : MONEY, CREDIT AND BANKING
TABLE 2
ROBUSTNESS CHECKS FOR STRUCTURAL BREAK TESTS
*p-value*forρxs1 =ρxs
3*p-value*forρsx1 =ρsx
3
Baseline 0.29 1.00 A1 estimate*r*0.18 1.00 A2 2-factor SRTSM 0.13 0.97 A3 Fama-Bliss 0.38 1.00 A4 5-factor FAVAR 0.70 1.00 A5 6-lag FAVAR 0.09 0.98
7-lag FAVAR 0.19 0.97 12-lag FAVAR 0.22 1.00
NOTES: This table consists of*p-values*for structural break tests with alternative model specifications.
We construct the likelihood ratio statistic as follows (see Hamilton 1994, p. 297):
*(T*−*k)*(
log$∣∣∣̂xx $
*R xx*′*R*
∣∣∣−log$∣∣∣̂xx $
*U xx*′*U*
∣∣∣),where*T*is the sample size,*k*is the number of regressors on the right-hand side
of equation (13),*̂xx U xx*′
*U*is the estimated covariance matrix, and*̂xx R xx*′
*R*is the estimated covariance matrix with the restriction imposed by the null hypothesis.
The likelihood ratio statistic has an asymptoticχ2distribution with 39 degrees of freedom. The*p*value is 0.29 for our policy rate*so*
*t*(see the first row of Table 2). We fail to reject the null hypothesis at any conventional significance level. This is consistent with the claim that our proposed policy rate impacts the macroeconomy the same way at the ZLB as before. If we use the EFFR instead, the*p*value is 0.0007, and we would reject the null hypothesis at any conventional significance level. Our results show that there is a structural break if one tries to use the conventional monetary policy rate. Using a similar procedure for the coefficients relating lagged macro factors to the policy rate, the*p*values are 1 for our policy rate and the effective federal funds rate. In summary, our policy rate exhibits similar dynamic relations to key macroeconomic variables before and after the Great Recession and captures meaningful information missing from the EFFR after the economy reached the ZLB. The immediate implication of this result is that researchers can use the shadow federal funds rate to update earlier studies that had been based on the historical federal funds rate.
3. MACROECONOMIC IMPLICATIONS
After the Great Recession the Fed implemented a sequence of unconventional monetary policy measures including large-scale asset purchases and forward guidance. The literature has thus far focused on large-scale asset purchases or QE, and its effects on the yield curve. In contrast to previous studies, here we attempt
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 267
to answer some more fundamental questions: what is the overall impact of these new unconventional policy tools on the real economy? Is the Fed able to achieve its stated goal of lowering the unemployment rate?
*3.1 Effects of Unconventional Monetary Policy*
In this section, we attempt to assess the effect of the various unconventional policy measures adopted by the Fed after the Great Recession with two counterfactual exercises. We can write each variable in equation (11) as a sum of past shocks and its initial condition. Specifically, the contribution of monetary policy shocks after the Great Recession (between*[t1*= July*2009, t2*= December 2013]) to an individual economic variable*Y m,i*
*t*can be summarized by
max(t,t2)∑τ=t1
* MP,i*t−τεMP
τ*,*(14)
where* MP,i j*is the impulse response
* MP,i j*=∂Y*m,i*
*t+ j*
∂εMP*t*
=*bx,i*
∂xm*t+ j*
∂εMP*t*
+*bs,i*
∂so*t+ j*
∂εMP*t*
*,*(15)
for variable*i*after*j*periods in response to a one unit shock inεMP*t*, and the derivatives
on the right-hand side are the impulse responses from a standard VAR. In Figure 6, we plot the observed time series for the six variables (the policy rate,
industrial production, consumer price index, capacity utilization, unemployment rate and housing starts) in blue, and counterfactual paths in red dashed lines for an alternative world where all the monetary policy shocks at the ZLB were zero. This exercise is equivalent to a historical decomposition. In the top left panel, we show the difference between the realized and counterfactual policy rates. Without any deviation from the traditional monetary policy rule, the shadow rate would have been about –1% in December 2013, whereas the actual shadow rate then was about –2%. On average, the shadow rate would have been 0.4% higher between 2011 and 2013 if the monetary policy shocks were set to zero. These results indicate that unconventional monetary policy has been actively lowering the policy rate, and the Fed has employed an expansionary monetary policy since 2011.
Next consider implications for the real economy. In the absence of expansionary monetary policy, in December 2013, the unemployment rate would be 0.13% higher at the 6.83% level rather than 6.7% in the data. The industrial production index would have been 101.0 rather than 101.8, and capacity utilization would be 0.3% lower than what we observe. Housing starts would be 11,000 lower (988,000 versus 999,000). These numbers suggest that unconventional monetary policy achieved its goal of stimulating the economy. Interestingly, the accommodative monetary policy during this period has not boosted real activity at the cost of high inflation. Instead,
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
268 : MONEY, CREDIT AND BANKING
2010 2011 2012 2013 -2.5
-2
-1.5
-1
-0.5
0
0.5 Policy rate
2010 2011 2012 2013 80
85
90
95
100
105 Industrial production index
2010 2011 2012 2013 210
215
220
225
230
235
240
245 Consumer price index
2010 2011 2012 2013 64
66
68
70
72
74
76
78 Capacity utilization
2010 2011 2012 2013 6.5
7
7.5
8
8.5
9
9.5
10
10.5 Unemployment
2010 2011 2012 2013 400
500
600
700
800
900
1000
1100
1200 Housing starts
realized counterfactural I counterfactual II
FIG. 6. Observed and Counterfactual Macroeconomic Variables.
NOTES: Gray solid lines: observed economic variables between July 2009 and December 2013. Dark gray dashed lines: what would have happened to these macroeconomic variables, if all the monetary policy shocks were shut down. Light gray dashed lines: what would have happened if the shadow rate was kept at*r*.
monetary policy shocks have contributed to decreasing the consumer price index by 1. Our result exhibits the same price puzzle that has been discussed in earlier macro studies.9
The historical decomposition exercise calculates the contribution of monetary policy shocks defined as deviations of the realized shadow federal funds rate from the policy rate implied by the historical monetary policy rule. Another question of interest is what would happen if the Fed had adopted no unconventional monetary policy at all. This question is more difficult to answer, because it is not clear what the counterfactual shadow rate would be. One possible counterfactual to consider would be what would have happened if the shadow federal funds rate had never fallen below the lower bound*r*. Specifically, we replace the realized monetary policy shock(εMP
τ) in equation (14) with the counterfactual shocks,εMP,I*I*
τ, such that these shocks would have kept the shadow rate at the lower bound. One might view the difference between the actual shadow rate and this counterfactual as an upper bound on the contribution of unconventional monetary policy measures. If instead of the realized shadow rate, monetary policy had been such that the shadow rate never fell below 0.25%, the unemployment rate would have been 1% higher than observed.
Our estimated effect of unconventional monetary policy on the unemployment rate is smaller than the ones found in Chung et al. (2012) and Baumeister and Benati
9. Examples include Sims (1992) and Eichenbaum (1992).
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQFKe09ZOmWd9eLEqOvhs20YhU-ZPqDaJ0Ya9tmqR2kq1BCqWnvrNsS2x_uL6d1xag97iNdNEvBDaFSl28gAh-3DLDS8TmbVD40xWz0J56-NzACZGcVSh64eSriMXYVfy7F-WPPthA=w1280-h672-v0?authuser=1)

JING CYNTHIA WU AND FAN DORA XIA : 269
FIG. 7. Impulse Responses with Full Sample.
NOTES: Impulse responses to a −25 basis-point shock on monetary policy. 90% confidence intervals are shaded. Sample: January 1960 to December 2013. Model: FAVAR with 3 macro factors and 13 lags. X-axis: response time in months. The policy rate is measured in annualized percentage; the industrial production index, consumer price index, and housing starts are measured in percentage deviation from the steady state; the capacity utilization and unemployment rate are measured in percentage points.
(2013). This is primarily because they assumed that unconventional monetary policy had a big impact on the yield curve. For example, Chung et al. (2012) assumed that the large-scale asset purchases reduced the long-term interest rates by 50 basis points and then translated this number into a 1.5% decrease in the unemployment rate. If we were to use Hamilton and Wu (2012)’s estimate of 13 basis-point decrease in the 10-year rate, a simple linear calculation would translate this number into a 0.39% reduction in the unemployment rate. This is comparable to our estimate.
*3.2 Impulse Responses*
What would happen to the unemployment rate 1 year later if the Fed decreases the policy rate by 25 basis points now? An impulse response function offers a way to think about questions like this by describing monetary policy’s dynamic impact on the economy.
We compute the impulse responses using equation (15) and plot them in Figure 7 for six economic variables to a loosening monetary policy shock with a size of 25 basis points$(ssεMP $
*t*= −25 bps). The 90% confidence intervals are in the shaded areas.10 With an expansionary monetary policy shock, real activity increases as expected: industrial production, capacity utilization and housing starts
10. Confidence intervals are constructed by bootstrapping.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
270 : MONEY, CREDIT AND BANKING
increase while the unemployment rate decreases. The impacts peak after about a year. Specifically, 1 year after a –25 basis-point shock to the policy rate, industrial pro-duction is 0.5% higher than its steady state level, capacity utilization increases by 0.2%, the unemployment rate decreases by 0.06%, and housing starts is 1.3% above its steady state level. After the peak, the effects die off slowly, and they are eventually gone in about 8 years.
4. MACROECONOMIC IMPACT AT THE ZLB
Our main results in Section 2 and 3 are based on a constant structure before and after the Great Recession. Despite a much smaller sample, the ZLB period provides an alternative angle, complementing the results we have so far. Section 4.1 serves as a robustness check—we compare the full sample impulse responses with those from the ZLB period, demonstrating the usefulness of the shadow rate. Section 4.2 studies forward guidance. With a sample size of 53 months at the ZLB, we replace the 13-lag FAVAR with a 1-lag FAVAR. In Section 4.3, we connect our shadow rate with the three rounds of QE and operation twist.
*4.1 New versus Conventional Policy Rates*
Consider first an attempt to estimate a first-order FAVAR for data at the ZLB period in which the effective federal funds rate is used as the policy rate. We plot impulse re-sponses to an expansionary policy shock of 25 basis points in Figure 8. The turquoise lines are median responses, and 90% confidence intervals are in the turquoise areas. For comparison, we also plot the impulse responses for the full sample with our pol-icy rate in blue. These are identical to the impulse responses presented in Figure 7. For the ZLB subsample, the impulse responses to a shock to the EFFR are as-sociated with huge uncertainty, with the confidence intervals orders of magnitude bigger than those for the full sample. This indicates that the EFFR does not carry much information at the ZLB. The reason is simple: it is bounded by the lower bound, and does not display any meaningful variation. We can also see this from Figure 4.
By contrast, Figure 9 plots the ZLB impulse response functions in turquoise with our policy rate introduced in Section 2. Again, we compare them with full sample impulse responses in blue. The subsample impulse responses are qualitatively the same as those for the full sample. Specifically, an expansionary monetary policy shock boosts real economic activity. The impulse responses for the subsample and full sample also look quantitatively similar, especially for medium and long horizons, despite some differences in the short horizon for several variables, potentially due to different model specifications. Overall, at the ZLB, the shadow federal funds rate conveys important and economically meaningful information, while the federal funds rate gets stuck around zero.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQFR4GP9XUoUUaQ9O8tLly1-ZdIMZp2ip3fpzmOz1W6_L9Q5WzYV7Q19OBuQNcOs9iVjyJ70d3KNjE8NUyCPm4WkRdiQS_GEpnWYVdld7uBOaZmBMhSkjReNhyEC1jiyqq-KcS_C=w1280-h647-v0?authuser=1)

![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQHu-wqCPGBOz45YifXwZztPt_bwvc69OOPrKIpKAVJynurZVqg__5lbBKD-RmL4Ad4zPrJP6GX6PpfgGuAkoO8k9N8Pbr71Nk6jhp-NA8qj_7-WC-G_C--Me4MgyEAl718Uw0Zn0Q=w1280-h647-v0?authuser=1)

JING CYNTHIA WU AND FAN DORA XIA : 271
FIG. 8. Impulse Responses (full sample versus ZLB with EFFR).
NOTES: Impulse responses to a −25 basis-point shock on monetary policy. 90% confidence intervals are shaded. Dark gray: full sample from January 1960 to December 2013 with the policy rate in FAVAR (13). Light gray: ZLB from July 2009 to December 2013 with the EFFR in FAVAR (1). X-axis: response time in months. The policy rate is measured in annualized percentage; the industrial production index, consumer price index, and housing starts are measured in percentage deviation from the steady state; the capacity utilization and unemployment rate are measured in percentage points.
FIG. 9. Impulse Responses (full sample versus ZLB with new policy rate).
NOTES: Impulse responses to a –25 basis-point shock on monetary policy. 90% confidence intervals are shaded. Dark gray: full sample from January 1960 to December 2013 with the policy rate in FAVAR (13). Light gray: ZLB from July 2009 to December 2013 with the policy rate in a FAVAR (1). X-axis: response time in months. The policy rate is measured in annualized percentage; the industrial production index, consumer price index, and housing starts are measured in percentage deviation from the steady state; the capacity utilization and unemployment rate are measured in percentage points.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
272 : MONEY, CREDIT AND BANKING
TABLE 3
FORWARD GUIDANCE QUOTES
Date Quotes
12/16/2008 “...anticipates that weak economic conditions are likely to warrant exceptionally low levels of the federal funds rate for some time.”
03/18/2009 “...anticipates that economic conditions are likely to warrant exceptionally low levels of the federal funds rate for an extended period.”
08/09/2011∗ “...anticipates that economic conditions—including low rates of resource utilization and a subdued outlook for inflation over the medium run—are likely to warrant exceptionally low levels for the federal funds rate at least through mid-2013.”
01/25/2012∗ “...decided today to keep the target range for the federal funds rate at 0 to 1/4% and currently anticipates that economic conditions—including low rates of resource utilization and a subdued outlook for inflation over the medium run—are likely to warrant exceptionally low levels for the federal funds rateat least through late 2014.”
09/13/2012∗ “...decided today to keep the target range for the federal funds rate at 0 to 1/4% and currently anticipates that exceptionally low levels for the federal funds rate are likely to be warranted at least through mid-2015.”
12/12/2012 “...decided to keep the target range for the federal funds rate at 0 to 1/4% and currently anticipates that this exceptionally low range for the federal funds rate will be appropriate at least as long as the unemployment rate remains above 6-1/2%, inflation between 1 and 2 years ahead is projected to be no more than a half percentage point above the Committee’s 2% longer-run goal, and longer-term inflation expectations continue to be well anchored.”
06/19/2013∗ “...14 of 19 FOMC participants indicated that they expect the first increase in the target for the federal funds rate to occur in 2015, and one expected the first increase to incur in 2016.”
12/18/2013 “...anticipates, based on its assessment of these factors, that it likely will be appropriate to maintain the current target range for the federal funds rate well past the time that the unemployment rate declines below 6-1/2% , especially if projected inflation continues to run below the Committee’s 2% longer-run goal.”
NOTES: This table summarizes a list of forward guidance quotes, when the Fed specified a different liftoff date or condition for the ZLB. All quotes except the one on 6/19/2013 are from FOMC statements. The quote on 6/19/2013 is from Chairman Bernanke’s press conference. Asterisks mark the statements with explicit liftoff dates. SOURCE: http://www.federalreserve.gov/monetarypolicy/fomccalendars.htm.
*4.2 Forward Guidance*
Since December 2008, the federal funds rate has been restricted by the ZLB. The conventional monetary policy is no longer effective, because the Fed cannot further decrease the federal funds rate below zero to boost the economy. Consequently, the central bank has resorted to a sequence of unconventional monetary policy tools. One prominent example is forward guidance, or central bank communications with the public about the future federal funds rate. In particular, forward guidance aims to lower the market’s expectation regarding the future short rate. Market expectations about future short rates feed back through the financial market to affect the current yield curve, especially at the longer end. Lower long-term interest rates in turn stimulate aggregate demand. The Fed has made considerable use of forward guidance since the federal funds rate first hit the ZLB. In Table 3, we summarize a list of forward guidance quotes, when the Fed expected a different liftoff date. Some of these dates
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 273
overlap with Woodford (2012). The wording focuses either on (i) the liftoff date or (ii) some target macroeconomic quantities. We first compare the liftoff dates prescribed by forward guidance and the market’s expectation from our model and then study the impact of forward guidance on the unemployment rate.
*Liftoff date.*One focus of forward guidance is for the Fed to implicitly or explicitly communicate with the general public about how long it intends to keep the federal funds rate near zero, as demonstrated in Table 3. In the earlier FOMC statements in late 2008 and early 2009, they used phrases such as “some time” and “an extended period.” Starting from late 2011, the Fed decided to be more transparent and specific about forward guidance. In each statement, they unambiguously revised the liftoff date or specify some economic conditions for exiting.
Our model implies a closely related concept: the ZLB duration. It measures the market’s perception of when the economy will finally escape from the ZLB. This is a random variable defined as
τt≡$inf{τt $≥0∣st+τ≥*r}.*
Thusτtrepresents how much time passes before the shadow rate first crosses the lower bound from below. At time*t*,st+τis unknown. We simulate out*N*= 10,000 paths of the future shadow rate given the information at time*t*.11 Every simulated path generates an estimate ofτt. Therefore, we have a distribution ofτt, and we take the median across*N*simulations as our measure of the market’s expected ZLB duration.
We summarize the history of the market’s expected ZLB duration in terms of the liftoff date in Figure 10. The market’s expectation of the liftoff date kept extending until early 2013, when the market believed the ZLB would continue until sometime in 2016. Then the market revised its expectation of liftoff to 2015 in mid 2013. Since then, the market’s expectations have fluctuated between 2015 and 2016. We highlight four announcements in August 2011, January 2012, September 2012, and June 2013 when the Fed explicitly spelled out the ZLB liftoff date (see Table 3). Between early 2011 and the first announcement, the market kept revising the liftoff date forward. On August 9, 2011, the Fed promised to keep the rate low “at least through mid-2013,” whereas the market anticipated the ZLB to last until early 2015. Then the market made some downward adjustment to mid 2014 in the following months. When the liftoff date was postponed to “at least through late 2014” on January 25, 2012, the market revised its expectation to early 2015. The two expectations overlap each other. On September 13, 2012, the forward guidance further extended the liftoff date to “at least through mid-2015,” when the market expected the ZLB to last until early 2016. On June 19, 2013, Chair of the Board of Governors of the Federal Reserve System Ben Bernanke expressed in a press conference the Fed’s plan to maintain accommodative monetary policy until 2015 based on the economic outlook at that time. Following
11. Note that we use the P parameters for simulation to capture real-life expectations.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
274 : MONEY, CREDIT AND BANKING
2009 2010 2011 2012 2013 2014
2010
2011
2012
2013
2014
2015
2016 market anticipation
Fed announcement
at least through mid-2013
at least through mid-2015
2015at least through late 2014
FIG. 10. The Market’s Expected versus Fed’s Announced ZLB Liftoff Dates.
NOTES: Gray dots: the market’s expected liftoff dates from January 2009 to December 2013. Four gray vertical lines mark the following months when forward guidance specified explicit liftoff dates for the ZLB: August 2011, Jan-uary 2012, September 2012, and June 2013. The corresponding liftoff dates are in diamonds. Black dashed line: the 45-degree line.
his remarks, the market’s expected liftoff date jumped to coincide with Bernanke’s statement.12
Overall, evidence suggests that when time goes on, forward guidance and the market’s expectation align better. For the later events, the two expectations overlapped each other. In the next section, we will use the expected ZLB duration as a proxy for forward guidance, and study its impact on the real economy, especially the unemployment rate.
*Impact on unemployment.*We have demonstrated that forward guidance is consistent with the market’s expectation. The ultimate question central bankers and economists care about is whether forward guidance is as successful in terms of its impact on the real economy, especially unemployment. We phrase this question in a FAVAR (1) framework with the expected ZLB duration measuring the monetary policy and use this tool to study the transmission mechanism of forward guidance. For the macroe-conomic factors, we keep them as they were. Figure 11 shows the impulse responses to a shock that extends the expected ZLB duration by 1 year. Overall, in response to an easing monetary policy, the economy starts to expand. Most interestingly, a 1-year increase in the expected ZLB duration translates into a 0.1% decrease in the unemployment rate, although the impulse response is not statistically significant at 10% level.
12. The results look very similar if we use real time duration instead, i.e., compute the ZLB duration at time*t*using only data up to*t*.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 275
0 24 48 -0.5
0
0.5
1**ZLB duration**
0 24 48 -0.5
0
0.5**Industrial production index**
0 24 48 -1
-0.5
0
0.5**Consumer price index**
0 24 48 -0.5
0
0.5
1**Capacity utilization**
0 24 48 -0.3
-0.2
-0.1
0
0.1**Unemployment**
0 24 48 -2
0
2
4
6**Housing starts**
FIG. 11. Impulse Responses (ZLB with expected duration).
NOTES: Impulse responses to a 1-year shock to expected ZLB duration. 90% confidence intervals are shaded. Sample: ZLB from July 2009 to December 2013. Model: FAVAR (1) with the ZLB duration as the monetary policy measure. X-axis: response time in months. The expected duration is measured in years; the industrial production index, consumer price index, and housing starts are measured in percentage deviation from the steady state; the capacity utilization and unemployment rate are measured in percentage points.
A simple calculation suggests that a 1-year increase in the expected ZLB duration has roughly the same effect on the macroeconomy as a 15 basis-point decrease in the policy rate. The visual comparison is in Figure 12, where the blue part is identical to Figure 11, and the turquoise portion is 15/25 times the turquoise in Figure 9. Figure 12 suggests that in response to a 1-year shock to the expected ZLB duration, or a negative 15 basis-point shock to the policy rate, capacity utilization goes up by 0.2%, unemployment rate decreases by 0.1%, and housing starts is about 2% over its steady state.
*4.3 Quantitative Easing*
In this section, we relate the Fed’s QE and operation twist (OT) to our shadow federal funds rate in an informal event study setting.
Lasting from November 2008 to March 2010, QE1 purchased about $1.7 trillion of mortgage-backed securities, agency debt as well as Treasury securities. During this period, the policy rate dropped from 97 basis points in October 2008 to negative 48 basis points in March 2010, totaling 1.45%, see Figure 13. Overall, we observe sizable downward movement in the policy rate associated with a substantial operation. QE2 was implemented from November 2010 to June 2011 with $600 billion purchases of
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
276 : MONEY, CREDIT AND BANKING
0 24 48
d u
ra tio
n (1
yr )
p o
lic y
ra te
(-1
5 b
p )
-0.5
0
0.5
1**ZLB duration**
0 24 48 -0.5
0
0.5**Industrial production index**
0 24 48 -1
-0.5
0
0.5**Consumer price index**
0 24 48 -0.5
0
0.5
1**Capacity utilization**
0 24 48 -0.3
-0.2
-0.1
0
0.1**Unemployment**
0 24 48 -2
0
2
4
6**Housing starts**
policy rate duration
FIG. 12. Impulse Responses at ZLB (policy rate versus ZLB duration).
NOTES: Light gray: impulse responses to a –15 basis-point shock on the policy rate. Dark gray: impulse responses to a 1-year shock on the ZLB duration. 90% confidence intervals are shaded. Sample: ZLB from July 2009 to December 2013. Model: FAVAR (1). X-axis: response time in months. The policy rate is measured in –15 basis points; the expected duration is measured in years; the industrial production index, consumer price index, and housing starts are measured in percentage deviation from the steady state; the capacity utilization and unemployment rate are measured in percentage points.
2008 2009 2010 2011 2012 2013 2014 2015 −3
−2.5
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
QE2
QE1
OT
QE3
FIG. 13. Policy Rate and Fed’s Asset Purchases.
NOTES: Dark gray line: the extended policy rate in percentage points from our website: http://faculty.chicagobooth. edu/jing.wu/research/data/WX.html. QE1: the first round of QE from November 2008 to March 2010. QE2: the second round of QE from November 2010 to June 2011. OT: operation twist from September 2011 to December 2012. QE3: the third round of QE from September 2012 to October 2014.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 277
longer maturity US Treasuries. In the meantime, the shadow rate moved from –1% to –1.12%, with a net change of 12 basis points. The decrease in the shadow rate was smaller due to two reasons. First, the scale of QE2 was smaller than QE1. Second, QE2 was well anticipated by the market, and much of the adjustment was already made prior to its announcement due to the forward looking nature of market participants. Operation Twist, between September 2011 and December 2012, swapped the shorter term bonds the Fed held with longer term bonds. There was no net purchase, and the nominal amount exchanged was $667 billion. There was not much action in the shadow rate, moving only 5 basis points lower. Between September 2012 and October 201413, QE3 made another round of bigger purchases with $1.7 trillion of longer-term Treasuries and mortgage-backed securities (Figure 13). In the meantime, we see the biggest drop for the shadow rate of 1.54% from –1.26% in August 2012 to –2.8% in October 2014.14 Among these events, the larger purchases of QE1 and QE3 were accompanied with bigger drops of the shadow rate, around 1.5% each time.
These numbers give a rough overall mapping between the QE and OT programs to our shadow federal funds rate. We need to interpret these numbers with a grain of salt. Although during these periods unconventional monetary policy constituted major events, the yield curve, hence the shadow rate, could still have potentially reacted to other macroeconomic news. To better single out QE’s effects on the shadow rate, we narrow down the window size below.
In Figure 14, we document responses of interest rates to two announcements, which surprised the market the most. On November 25, 2008, The Fed announced its first QE program to purchase the direct obligations of housing-related government-sponsored enterprises and mortgage-backed securities (top row of Figure 14). On May 22, 2013, Ben Bernanke mentioned to taper the Fed’s QE program, referred by the popular media as the “taper tantrum” (bottom row of Figure 14). In the first column of Figure 14, we plot the 1-day change of the yield curve corresponding to these events. In response to the accommodative announcement about QE1, we observe the longer end of the yield curve shifted down, while the shorter end remained unchanged. During the taper tantrum, a tightening event, longer yields shifted up without moving short yields. The second column describes the same movements in terms of monthly changes of the forward curve, which is a simple linear function of the yield curve, see (6). Again, long rates moved in the right directions, whereas short rates did not react to the taper tantrum due to the ZLB. The forward curve approximately captures the expected future short-term interest rate under the risk-neutral measure. Given that agents do not expect the short-term interest rate to move away from the lower bound anytime soon, we do not see any movement at the short end. To contrast this lack of movement, we plot the expected future shadow rate curves in the third column. The longer end mimicked the movements in the second column. The difference is that as the shadow rate still displays variation
13. Note, there are several months overlap between OT and QE3. 14. We use the extended shadow rate from our website: http://faculty.chicagobooth.edu/jing.wu/
research/data/WX.html.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
278 : MONEY, CREDIT AND BANKING
1  2  3  4  5  6  7  8  910
1
2
3
4
5 yield
QE1 one day prior
1  2  3  4  5  6  7  8  910 0
1
2
3 yield
Taper tantrum one day prior
1  2  3  4  5  6  7  8  910 0
5
10 forward rate
QE1 one month prior
1  2  3  4  5  6  7  8  910 0
2
4
6 forward rate
Taper tantrum one month prior
1  2  3  4  5  6  7  8  910 0
5
10 expected path of shadow rate
QE1 one month prior
1  2  3  4  5  6  7  8  910 −2
0
2
4
6 expected path of shadow rate
Taper tantrum one month prior
FIG. 14. Interest Rates’ Responses to Fed’s Announcements.
NOTES: Top row: QE1 announcement on November 25, 2008. Bottom row: taper tantrum on May 22, 2013. First column: yield curves. Second column: forward curves. Third column: expected shadow rates. Dark gray: event dates. Light gray: one day prior to event dates for yields, 1 month prior to event dates for forward rates and expected path of shadow rates. X-axis: maturity in years. Y-axis: interest rates in percentage points.
at the ZLB, we see the whole curve, including the short end, shifted in response to these events. In response to the QE1 announcement, the shadow rate dropped 42 basis points. The taper tantrum increased the shadow rate by 25 basis points.
Overall, we have illustrated that the shadow rate can adequately summarize changes in long-term interest rates (or forward rates) due to QE announcements. Some researchers have suggested that QE lowers long-term interest rates through the term premium channel. If this is the case, even at the very short end of the yield curve, our shadow federal funds rate is able to capture movements in the term premium component.
5. ROBUSTNESS
*5.1 Lower Bound*
Our benchmark SRTSM in Section 1 sets*r*=*0.25%*at the interest the Fed has paid on reserves. This parameter is potentially estimable. As a robustness, we estimate it as an additional parameter. The estimated lower bound*r̂*=*0.19%*is fairly close to the 25 basis points chosen by economic intuition.
As a result, the dynamics of the shadow rates implied by the two versions resemble each other, see Figure 15. There is some difference between the blue line (our original shadow rate) and the green line (the new shadow rate with estimated*r*) in levels,
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 279
1990 1992 1994 1996 1998 2000 2002 2004 2006 2008 2010 2012 2014
−2
0
2
4
6
8
10*r=0.25% r estimated*
FIG. 15. Shadow Rates.
NOTES: Dark gray line: the shadow rate from the benchmark model with*r*=*0.25%*in percentage points. Light gray line: the shadow rate with estimated*r̂*=*0.19%*in percentage points. The gray area marks the ZLB period from January 2009 to December 2013.
similar to what Bauer and Rudebusch (2013) found. However, the dynamics of the two series exhibit a strong comovement, with a correlation of 1.00 for the full sample and 0.93 for the ZLB subsample. The comovement rather than the difference in levels between the shadow rates is what drives the key results. For example, the liftoff dates produced by them resemble each other as well, see Figure 16.
More importantly, they produce the same economic implications. Our key result in Section 2 holds. The second row of Table 2 reports the*p*value for the test*H0*:ρxs
1 =ρxs3 on the left. Similar to the benchmark case in the first row, we cannot
reject the null hypothesis at any conventional level, again supporting the conclusion that the shadow rate is a natural extension of the federal funds rate at the ZLB. The second number illustrates that we cannot reject the null hypothesis*H0*:ρsx
1 =ρsx3
either. The impulse responses produced with the new shadow rate have an identical economic meaning as those in Figure 7.15 Overall, whether we fix the*r*at 25 basis points as in our benchmark or estimate it at 19 basis points does not alter any conclusion, especially our main macro conclusions.
*5.2 Macro Implications*
One of the key macro results is based on the structural break tests in Section 2. We demonstrated the robustness of this result against an alternative lower bound.
15. For brevity, figures are not included in the paper.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
280 : MONEY, CREDIT AND BANKING
2009 2010 2011 2012 2013 2014
2010
2011
2012
2013
2014
2015
2016
r=0.25% r estimated
FIG. 16. Liftoff Dates.
NOTES: Dark gray dots: liftoff dates from the benchmark model with*r*=*0.25%.*Light gray triangles: liftoff dates with estimated*r̂*=*0.19%.*Black dashed line: the 45-degree line.
Next, we vary some other specifications of the SRTSM to show a broader set of robustness. First, although it is well established in the GATSM literature that we need three factors to capture the cross-sectional variation of the term structure, some researchers in the SRTSM use two factors instead. Examples are Kim and Singleton (2012), Krippner (2013), and Christensen and Rudebusch (2014). Therefore, the second set of robustness (A2) uses a two-factor SRTSM instead of a three-factor model. There is also some concern about the Gürkaynak, Sack, and Wright (2007) data set due to its smoothing nature. As a third alternative (A3), we use the Fama and Bliss (1987) unsmoothed zero coupon bond yields from CRSP, with maturities of 3 months and 1 through 5 years. The results for these alternatives are in rows 3 and 4 of Table 2. Again, all the*p*values are larger than 10%, as opposed to 0.0007 for the federal funds rate, supporting our conclusion.
Another important macro result are the impulse responses in Section 3.2. The impulse responses using alternative shadow rates look economically identical to the benchmark responses in Figure 7. The literature argues that different aspects of the SRTSM—including the lower bound, number of factors, and data set—might have implications for the term structure of interest rates itself. However, our evidence suggests that for the more important economic implications, they do not play such a role.
To further extend the reliance of our key macro results, we vary the specifications for the FAVAR as well. We first change the number of macro factors from three to five in A4. Then, we also check for 6, 7, and 12 lags (A5) as opposed to 13 lags in the benchmark. These are all plausible alternatives analyzed in Bernanke, Boivin, and Eliasz (2005). Rows 5–8 of Table 2 summarize the results. We cannot reject either
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 281
of the null hypotheses at 5% level for all the specifications, with all but one*p*values greater than 0.1. Thus, our key results are not subject to the specific model choices for the FAVAR either.
Overall, neither changes in the SRTSM hence the shadow rate, nor changes in the FAVAR alter the key macroeconomic results of this paper, and our results are robust to a wide range of alternatives.
6. CONCLUSION
We have developed an analytical approximation for the forward rate in the SRTSM, making the otherwise complicated model extremely tractable, with the approximation error being only a couple of basis points. The SRTSM offers an excellent description of the data especially when the economy is at the ZLB. We used the shadow rate from the SRTSM to construct a new measure for the monetary policy stance when the EFFR is bounded below by zero and employed this measure to study unconventional monetary policy’s impact on the real economy. We have found that our shadow federal funds rate impacts the real economy since July 2009 in a similar fashion as the EFFR did before the Great Recession. An expansionary monetary policy shock boosts the real economy. More specifically, at the ZLB, in response to a −15 basis-point shock to the policy rate, the unemployment rate decreases by 0.1%. This quantity is equivalent to a 1-year extension of the expected ZLB period, prescribed by forward guidance. Our counterfactual analyses have found that the efforts by the Fed to stimulate the economy since July 2009 succeeded in lowering the unemployment rate by 1% in December 2013, or 0.13% lower than it would have been if the Fed followed the historical Taylor rule.
The continuity in our policy rate series before and post the Great Recession provides empirical researchers—who used the EFFR in a VAR to study monetary policy in the macroeconomy—a tool to update their historical analysis. It also has potential applications in other areas in macroeconomics, such as dynamic stochastic general equilibrium models.
Researchers introduced new modeling ingredients into New Keynesian models specifically for the ZLB period, Eggertsson and Woodford (2003) and Wieland (2014) are examples, although empirically Wieland (2014) found a constant relationship between economic quantities during normal times and the ZLB, which is a similar observation as ours.16 How to map the empirical evidence of ours and Wieland’s (2014) into a coherent structural model and map the shadow rate into an equilibrium quantity are still open to future work.
16. He found that the sign and size of supply shock’s impact on the economy are similar during normal times and the ZLB.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
282 : MONEY, CREDIT AND BANKING
APPENDIX A: APPROXIMATION TO FORWARD RATES
Define
*ān*≡δ0+δ′1
⎛⎝n−1∑*j=0*
(ρQ)*j*
⎞⎠μQ,
*an*≡*ān*− 1
2δ′
1
⎛⎝n−1∑*j=0*
(ρQ)*j*
$⎞⎠′ $
⎛⎝n−1∑*j=0*
(ρQ)*j*
⎞⎠′
δ1,
*b′ n*≡δ′
1
(ρQ*)n*
*.*
*A.1 Shadow Rate*
The shadow rate is affine in the state variables. Under the risk-neutral measure, it is conditionally normally distributed. The conditional mean is
EQ*t [st+n]*=*ān*+*b′*
*n Xt ,*
the conditional variance is
VarQ*t [st+n]*≡(σQ
*n*
)2 =n−1∑*j=0*
δ′1
(ρQ)*j*
*′*(ρQ′)*j*δ1,
and
1
2
⎛⎝VarQ*t*
⎡⎣n∑*j=1*
*st+ j*
⎤⎦−VarQ*t*
⎡⎣n−1∑*j=1*
*st+ j*
⎤⎦⎞⎠=*ān*−*an.*
*A.2 SRTSM*
We start the derivation of equation (7) with the following approximation:*log(E[eZ*])≈*E[Z*] + 1
2*Var[Z*] for any random variable*Z*. This approximation uses Taylor series expansions for the exponential and natural logarithm functions. For the special case of a Gaussian random variable*Z*, this approximation is exact. Then the forward rate between*t*+*n*and*t*+*n*+ 1 can be approximated as follows:
*f SRTSM n,n+1,t*=*(n*+*1)yn+1,t*−*nynt*
= −log (
*e−rt*EQ*t*
[e−∑n
*j=1 rt+ j*
]) + log
(*e−rt*EQ
*t*
[e−∑n−1
*j=1 rt+ j*
])≈EQ
*t*
⎡⎣n∑*j=1*
*rt+ j*
⎤⎦−1
2 VarQ
*t*
⎡⎣n∑*j=1*
*rt+ j*
⎤⎦−EQ*t*
⎡⎣n−1∑*j=1*
*rt+ j*
⎤⎦+1
2 VarQ
*t*
⎡⎣n−1∑*j=1*
*rt+ j*
⎤⎦= EQ
*t [rt+n]*− 1
2
⎛⎝VarQ*t*
⎡⎣n∑*j=1*
*rt+ j*
⎤⎦−VarQ*t*
⎡⎣n−1∑*j=1*
*rt+ j*
⎤⎦⎞⎠*.*(A1)
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 283
We calculate the first term EQ*t [rt+n]*analytically:
EQ*t [rt+n]*= EQ
*t [max(r , st+n)]*
= PrQ*t [st+n < r*] ×*r*+ PrQ
*t [st+n*≥*r*] × EQ*t [st+n|st+n*≥*r*]
=*r*+σQ*n*
((*ān*+*b′*
*n Xt*−*r*
σQ*n*
)**
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
) +φ
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
)) =*r*+σQ
*n g*
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
)*.*(A2)
Using the second moments for the truncated normal distribution, we have the fol-lowing approximations for the conditional variance and covariance (see details in Appendix A.4):
VarQ*t [rt+n]*≈PrQ
*t [st+n*≥*r*]VarQ*t [st+n] ,*(A3)
CovQ*t*
[*rt+n− j , rt+n*
]≈PrQ*t [st+n− j*≥*r , st+n*≥*r*]CovQ
*t [st+n− j ,*st+n],∀*j*
=*1, . . . , n*−*1.*(A4)
Next, we take the approximation
PrQ*t [st+n− j*≥*r |st+n*≥*r*]≈*1,*
using the fact that the shadow rate is very persistent. Equation (A4) becomes
CovQ*t [rt+n− j , rt+n]*≈PrQ
*t [st+n*≥*r*]CovQ*t [st+n− j , st+n].*
Then, the second term in equation (A1) is
1
2
⎛⎝VarQ*t*
⎡⎣n∑*j=1*
*rt+ j*
⎤⎦−VarQ*t*
⎡⎣n−1∑*j=1*
*rt+ j*
⎤⎦⎞⎠≈PrQ
*t (st+n*≥*r*) × 1
2
⎛⎝VarQ*t*
⎡⎣n∑*j=1*
*st+ j*
⎤⎦−VarQ*t*
⎡⎣n−1∑*j=1*
*st+ j*
⎤⎦⎞⎠=**
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
) ×*(ān*−*an).*(A5)
Plug equations (A2) and (A5) to (A1), we conclude our derivation for equation (7) with another first-order Taylor approximation:
*f SRTSM n,n+1,t*≈*r*+σQ
*n g*
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
) +**
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
) ×*(an*−*ān)*
=*r*+σQ*n g*
(*ān*+*b′*
*n Xt*−*r*
σQ*n*
) +σQ
*n*
∂g(
*ān+b′ n Xt −r*
σQ*n*
)∂*ān*
×*(an*−*ān)*
≈*r*+σQ*n g*
(*an*+*b′*
*n Xt*−*r*
σQ*n*
)*.*(A6)
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
284 : MONEY, CREDIT AND BANKING
*A.3 GATSM*
In the GATSM, the forward rate between*t*+*n*and*t*+*n*+ 1 is priced as follows:
*f G AT SM n,n+1,t*=*(n*+*1)yn+1,t*−*nynt*
= −log (
*e−st*EQ*t*
[e−∑n
*j=1 st+ j*
]) + log
(*e−st*EQ
*t*
[e−∑n−1
*j=1 st+ j*
]) = EQ
*t*
⎡⎣n∑*j=1*
*st+ j*
⎤⎦−1
2 VarQ
*t*
⎡⎣n∑*j=1*
*st+ j*
⎤⎦−EQ*t*
⎡⎣n−1∑*j=1*
*st+ j*
⎤⎦+1
2 VarQ
*t*
⎡⎣n−1∑*j=1*
*st+ j*
⎤⎦= EQ
*t [st+n]*− 1
2
⎛⎝VarQ*t*
⎡⎣n∑*j=1*
*st+ j*
⎤⎦−VarQ*t*
⎡⎣n−1∑*j=1*
*st+ j*
⎤⎦⎞⎠=*ān*+*b′*
*n Xt*+*an*−*ān*
=*an*+*b′ n Xt .*
*A.4 Approximations to Variance and Covariance*
Define
*s̃t+n*≡*st+n*− EQ*t [st+n]*
σQ*n*
andαnt≡*r*− EQ*t [st+n]*
σQ*n*
*,*
then*rt+n*=σQ*n r̃t+n*+ EQ
*t [st+n],*where*r̃t+n*≡*max(s̃t+n,*αnt).
*Variance.*Standard results for the truncated normal distribution states that if*x*∼*N (0,*1), then (i)*Pr[x*≥α]= 1 −$(α), $(ii)*Pr[x*≥α]E[x*|x*≥α]=φ(α),and*(iii)Pr[x*≥α]E[x2∣x≥α]= 1 −$(α) $+αφ(α).Because*s̃t+n*is conditionally nor-mally distributed with mean 0 and variance 1 under the Q measure,
EQ*t [r̃t+n]*= PrQ
*t [s̃t+n*≥αnt]*Et [s̃t+n|s̃t+n*≥αnt] + PrQ*t [s̃t+n <*αnt]αnt
=φ(αnt) +$αnt (αnt $)*,*(A7)
EQ*t*
[*r̃2*
*t+n*
] = PrQ*t [s̃t+n*≥αnt]*Et*
[*s̃2*
*t+n|s̃t+n*≥αnt]+ PrQ
*t [s̃t+n <*αnt]α2*nt*
= 1 −**(αnt) +αntφ(αnt) +α2*nt*(αnt)*.*
Accordingly,
VarQ*t [rt+n]*=(σQ
*n*
)2 VarQ
*t [r̃t+n]*=(σQ*n*
)2 (*Et*[*r̃2*
*t+n*
]−*(Et [r̃t+n])2)*=(σQ
*n*
)2($1−(αnt )+αntφ(αnt )+α2 $
$nt(αnt )−(φ(αnt $) +$αnt(αnt $)) 2 )*.*
(A8)
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 285
−5 −4 −3 −2 −1 0 1 2 3 4 5 −0.16
−0.12
−0.08
−0.04
0
αnt
D (.
)
FIG. A1.D(αnt).
NOTES:*D*as a function ofαnt.
Comparing the exact formula in equation (A8) with the approximation in equation (A3), or VarQ
*t (rt+n)*≈PrQ*t [st+n*≥*r*]VarQ
*t [st+n]*=(σQ*n*)2(1 −$(αnt $), the approxi-
mation error is
(σQ
*n*
)2{(*1−*(αnt)+αntφ(αnt)+α2
*nt*$(αnt )−(φ (αnt )+αnt (αnt $))*2)−(1−*(αnt))
}=−(σQ
*n*
)2*g*(αnt)*g*(−αnt)≡
(σQ
*n*
)2*D*(αnt)*.*
The first derivative ofD(αnt) isD′(αnt) =−g′(αnt)g(−αnt) +g(αnt)g′(−αnt), andD′(αnt)∣αnt=0 = 0. Therefore*D(0)*is a local maximum/minimum. From Figure A1,*D(.)*is bounded by 0 from above and achieves the global minimum atαnt= 0. There-fore, the absolute approximation error is bounded by a small number(σQ
*n*)2φ(0)2.
*Covariance.*Standard results for the multivariate truncated normal distribution states
that if
[*x1*
*x2*
] ∼*N*
([ 0 0
]*,*
[ 1ρ
ρ1
]) , then
*(i)*Pr*[x1*≥α1,*x2*≥α2]=*F*(−α1,−α2;ρ)*,*
*(i i)*Pr*[x1*≥α1,*x2*≥α2]E*[x1|x1*≥α1,*x2*≥α2]=h(α1,α2,ρ)+ρh(α2,α1,ρ),
*(i i i)*Pr*[x1*≥α1,*x2*≥α2]E*[x1x2|x1*≥α1,*x2*≥α2]
=ρ(α1h(α1,α2;ρ)+α2h(α2,α1;ρ)+F(−α1,−α2;ρ))+(1−ρ2)
*f*(α1,α2;ρ),
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
286 : MONEY, CREDIT AND BANKING
where
*f (x1, x2;*ρ)≡λ(2π)−1*exp*
{ −1
2λ2(*x2*
1 −2ρx1x2+*x2*2
)}*,*
F(α1,α2;ρ)≡∫α1
−∞
∫α2
−∞*f (x1, x2;*ρ)dx1dx2,
h(α1,α2;ρ)≡φ(α1)**(λ(ρα1−α2))*,*
λ≡(1 −ρ2)−1 2*.*
Letρmntbe the correlation between*s̃t+m*and*s̃t+n*under the Q measure, then,
EQ*t [r̃t+mr̃t+n]*= EQ
*t [s̃t+ms̃t+n*|*s̃t+m*≥αmt*, s̃t+n*≥αnt]PrQ*t (s̃t+m*≥αmt*, s̃t+n*≥αnt)
+αmtEQ*t [s̃t+n |s̃t+m <*αmt*, s̃t+n*≥αnt] PrQ
*t (s̃t+m <*αmt*, s̃t+n*≥αnt)
+αntEQ*t [s̃t+m |s̃t+m*≥αmt*, s̃t+n <*αnt] PrQ
*t (s̃t+m*≥αmt*, s̃t+n <*αnt)
+αmtαntPrQ*t (s̃t+m <*αmt*, s̃t+n <*αnt)
=ρmnt(αmt*h*(αmt*,*αnt;ρmnt)+αnt*h*(αnt*,*αmt;ρmnt*)+F*(−αmt*,*−αnt;ρmnt))
+ (1 −ρ2*mnt*
)*f*(αmt*,*αnt;ρmnt)
+αmt*(h*(αnt,−αmt;−ρmnt) −ρmnt*h*(−αmt*,*αnt*,*−ρmnt))
+αnt*(h*(αmt,−αnt;−ρmnt) −ρmnt*h*(−αnt*,*αmt;−ρmnt))
+αmtαnt*F*(αmt*,*αnt;ρmnt)*.*
With the identityh(α1,α2;ρ)=h(−α1,α2;−ρ),we simplify the expression above as follows:
EQ*t [r̃t+mr̃t+n]*=ρmnt*F*(−αmt,−αnt;ρmnt) + (1 −ρ2
*mnt*
)*f*(αmt*,*αnt;ρmnt)
+αmt*h*(αnt,−αmt;−ρmnt) +αnt*h*(αmt,−αnt;−ρmnt)
+αmtαnt*F*(αmt*,*αnt;ρmnt)*.*
From equation (A7), we have
EQ*t [r̃t+m]*EQ
*t [r̃t+n]*=(φ(αmt) +$αmt (αmt $))(φ(αnt) +$αnt (αnt $))*.*
Accordingly,
CovQ*t [rt+m, rt+n]*=σQ
*m*σQ*n*CovQ
*t [r̃t+m, r̃t+n]*
=σQ*m*σQ
*n*
( EQ
*t [r̃t+mr̃t+n]*− EQ*t [r̃t+m]*EQ
*t [r̃t+n]*)
*.*(A9)
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
![image](https://lh3.googleusercontent.com/notebooklm/AKXwDQEOwmxGsPybWxPFQea29wnRNCjXLCpldoWTPF-bGvThA45K4HfksBSIkfQ_Tf8D9vVDrSaSroNsqVpYrAgCqaeRqlczKsOsLsLBg3En3PJPmdliTFaGhVC1mVbn4qeeNeAktrWqCw=w1280-h623-v0?authuser=1)

JING CYNTHIA WU AND FAN DORA XIA : 287
FI G
.A 2.
*D*(α
*m t,*
α*nt*
;ρ*m*
*nt*).
N O
T E
S: 3D
pl ot
s of
D as
a fu
nc tio
n of
α*m*
*t*an
dα
*nt*,f
orρ
*m nt*
= −0
*.9 ,*−0
*.8 , ..*
*., 0.*
9.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
288 : MONEY, CREDIT AND BANKING
Comparing the exact formula in equation (A9) with the approximation in equation (A4), or CovQ
*t [rt+m, rt+n]*≈PrQ*t [st+m*≥*r , st+n*≥*r*]CovQ
*t [st+m, st+n]*=ρmntσ
Q*m*σQ
*n*F(−αm,−αn;ρmnt), the approximation error is
σQ*m*σQ
*n*× {(1 −ρ2*mnt*)*f*(αmt*,*αnt;ρmnt) +αmt*h*(αnt*,*−αmt;−ρmnt) +αnt*h*(αmt*,*−αnt;−ρmnt)
+αmtαnt*F*(αmt*,*αnt;ρmnt) −(φ(αmt) +$αmt (αmt $))(φ(αnt) +$αnt (αnt $))}≡σQ
*m*σQ*n D*(αmt*,*αnt;ρmnt)*.*
The first derivative ofD(αmt*,*αnt;ρmnt) with respect toαmtis
∂*D*(αmt*,*αnt;ρmnt)
∂αmt= −(αmt−ρmntαnt)*f*(αmt*,*αnt;ρmnt)
+*h*(αnt*,*−αmt;−ρmnt) +λmntαmtφ(αnt)φ(λmnt(−ρmntαnt+αmt))
−$αntαmt (αmt $)**(λmnt(−ρmntαmt+αnt))
−λmntρmntαntφ(αmt)φ(λmnt(−ρmntαmt+αnt))
+αnt*F*(αmt*,*αnt;ρmnt) +αmtαnt*h (amt ,*−αnt;−ρmnt)
−**(αmt)(φ(αnt) +$αnt (αnt $))*,*
whereλmnt= (1 −ρ2*mnt*)
− 1 2 . And∂D(αmt,αnt;ρmnt)
∂αmt∣αmt=0,αnt=0 =$φ(0)(0) $−$φ(0)(0) $
= 0. SinceD(αmt*,*αnt;ρmnt) =D(αnt*,*αmt;ρmnt), we have∂D(αmt,αnt;ρmnt)∂αnt
∣αmt=0,αnt=0
= 0 as well. Thus,*D(0,*0;ρmnt) is a local maximum/minimum. We plotD(αmt*,*αnt;ρmnt) forρmnt=*−0.9,−0.8, ..., 0.8, 0.9*in Figure A2, andD(αmt*,*αnt;ρ)is bounded by 0 from above and achieves the global minimum atαmt=*0,*αnt= 0. Therefore, the absolute approximation error is bounded by a small number,σQ
*m*σQ*n*(1 − (1 −ρ2
*mnt*) 1 2)φ2(0).
APPENDIX B: KALMAN FILTERS
*B.1 Extended Kalman Filter for the SRTSM*
The transition equation is in (3). Stack the observation equation in (9) for all seven maturities, we get the following system:
*Fo t+1*=*G (Xt+1)*+ηt+1ηt+1∼*N (0,*ωI7).
Approximate the conditional distribution of*Xt*with*Xt |Fo 1:t*∼*N (X̂t |t , Pt |t*). Update
*X̂t+1|t+1*and*Pt+1|t+1*as follows:
*X̂t+1|t+1*=*X̂t+1|t*+*Kt+1*(*Fo*
*t+1*−*F̂o t+1|t*)*,*
*Pt+1|t+1*=*(I3*−*Kt+1 H*′*t+1*
)*Pt+1|t ,*
*X̂t+1|t*=μ+ρ*X̂t |t ,*
*Pt+1|t*=ρ*Pt*∣tρ′ +*′,*
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 289
with the matrices defined as
*F̂o t+1|t*=*G(X̂t+1|t ),*
*Ht+1*= (
∂G(Xt+1)
∂*X*′*t+1*
∣∣∣∣*Xt+1=X̂t+1|t*
)′*,*
*Kt+1*=*Pt+1|t Ht+1*(*H*′
*t+1 Pt+1|t Ht+1*+ωI7)−1
*,*
where we can obtain*H*′*t+1*by stacking*( an+b′*
*n X̂t+1|t −r*
σQ*n*
) ×*b′ n*for the seven maturities.
Given the initial values*X̂0|0*and*P0|0,*we can update*{X̂t |t , Pt |t }T t=1*recursively with
the above algorithm. The log likelihood is
*L*=*−7T*
2log2π− 1
2
T∑*t=1*
*log|H*′*t Pt+1|t Ht*+ωI7∣
−1
2
T∑*t=1*
*(Fo t*−*G(X̂t |t−1)′*
(*H*′
*t Pt+1|t Ht*+ωI7)−1
*(Fo t*−*G(X̂t |t−1).*
*B.2 Kalman Filter for the GATSM*
The GATSM is a linear Gaussian state space model. The*G(.)*function stacks the linear function in equation (10). The matrix*H*′
*t+1*stacks*b′ n*for the seven maturities.
The algorithm described above collapses to a Kalman filter.
APPENDIX C: FACTOR CONSTRUCTION FOR THE FAVAR
This appendix illustrates how to construct the macro factors. First, extract the first three principal components*p̂ct*from*Y m*
*t*. Then extract first three principal components*p̂c∗*
*t*from the slow-moving variables indicated with “∗” in the data table in the Online Appendix (http://faculty.chicagobooth.edu/jing.wu/). Normalize them to unit variance. Next, run the following regression*p̂ct*=*bpc p̂c∗*
*t*+*bpc,sso t*+η
*pc t*
and construct*x̂m t*from*p̂ct*−*b̂pc,sso*
*t*. We then estimate equation (12) as follows. If*Y m,i*
*t*is among the slow-moving variables, we regress*Y m,i t*on a constant and*x̂m*
*t*
to obtain*âm,i*and*b̂x,i*and set*b̂s,i*= 0. For other variables, we regress*Y m,i t*on a
constant,*x̂m t*and*so*
*t*to get*âm,i*,*b̂x,i*and*b̂s,i*.
LITERATURE CITED
Bauer, Michael D., and Glenn D. Rudebusch. (2013) “Monetary Policy Expectations at the Zero Lower Bound.” Federal Reserve Bank of San Francisco Working Paper.
Bauer, Michael D., and Glenn D. Rudebusch. (2014) “The Signaling Channel for Federal Reserve Bond Purchases.”*International Journal of Central Banking,*10, 233–89.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
290 : MONEY, CREDIT AND BANKING
Bauer, Michael D., Glenn D. Rudebusch, and Jing Cynthia Wu. (2012) “Correcting Estimation Bias in Dynamic Term Structure Models.”*Journal of Business & Economic Statistics,*30, 454–67.
Baumeister, Christiane, and Luca Benati. (2013) “Unconventional Monetary Policy and the Great Recession: Estimating the Macroeconomic Effects of a Spread Compression at the Zero Lower Bound.”*International Journal of Central Banking,*9, 165–212.
Bernanke, Ben S., Jean Boivin, and Piotr Eliasz. (2005) “Measuring the Effects of Monetary Policy: A Factor-Augmented Vector Autoregressive (FAVAR) Approach.”*Quarterly Journal of Economics,*120, 387–422.
Black, Fischer. (1995) “Interest Rates as Options.”*Journal of Finance,*50, 1371–6.
Bullard, James. (2012) “Shadow Interest Rates and the Stance of US Monetary Policy.” Presentation at the Center for Finance and Accounting Research Annual Corporate Finance Conference, Washington University in St. Louis.
Christensen, J. H. E., and Glenn D. Rudebusch. (2014) “Estimating Shadow-Rate Term Struc-ture Models with Near-Zero Yields.”*Journal of Financial Econometrics,*13(2), 226–259.
Christiano, Lawrence J., Martin Eichenbaum, and Charles L. Evans. (1999) “Monetary Policy Shocks: What Have We Learned and to What End?” In*Handbook of Macroeconomics,*Vol. 1 Part A, edited by John B. Taylor and Michael Woodford, pp. 65–148. Amsterdam, The Netherlands: Elsevier.
Chung, Hess, Jean-Philippe Laforte, David Reifschneider, and John C. Williams. (2012) “Have We Underestimated the Likelihood and Severity of Zero Lower Bound Events?”*Journal of Money, Credit and Banking,*44, 47–82.
Creal, Drew D., and Jing Cynthia Wu. (2015) “Estimation of Affine Term Structure Models with Spanned or Unspanned Stochastic Volatility.”*Journal of Econometrics,*185, 60–81.
D’Amico, Stefania, and Thomas King. (2013) “Flow and Stock Effects of Large-Scale Treasury Purchases: Evidence on the Importance of Local Supply.”*Journal of Financial Economics,*108, 425–48.
Diebold, Francis X., and Glenn D. Rudebusch. (2013).*Yield Curve Modeling and Forecasting.*Princeton, NJ: Princeton University Press.
Duffee, Gregory R. (2002) “Term Premia and Interest Rate Forecasts in Affine Models.”*Journal of Finance,*57, 405–43.
Duffee, Gregory R. (2013) “Bond Pricing and the Macroeconomy.” In*Handbook of the Economics of Finance,*Vol. 2 Part B, edited by George M. Constantinides, Milton Harris, and Rene M. Stulz, pp. 907–67. Amsterdam, the Netherlands: Elsevier.
Eggertsson, Gauti B., and Michael Woodford. (2003) “The Zero Bound on Interest Rates and Optimal Monetary Policy.”*Brookings Papers on Economic Activity,*1, 139–233.
Eichenbaum, Martin. (1992) “Comment on Interpreting the Macroeconomic Time Series Facts: The Effects of Monetary Policy.”*European Economic Review,*36, 1001–11.
Fama, Eugene F., and Robert R. Bliss. (1987) “The Information in Long-Maturity Forward Rates.”*American Economic Review,*77, 680–92.
Gagnon, Joseph, Mattew Raskin, Julie Remache, and Brian Sack. (2011) “The Financial Market Effects of the Federal Reserve’s Large-Scale Asseet Purchase.”*International Journal of Central Banking,*7, 3–43.
Gürkaynak, Refet S., Brian Sack, and Jonathan H. Wright. (2007) “The U.S. Treasury Yield Curve: 1961 to the Present.”*Journal of Monetary Economics,*54, 2291–304.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L
JING CYNTHIA WU AND FAN DORA XIA : 291
Gürkaynak, Refet S., and Jonathan H. Wright. (2012) “Macroeconomics and the Term Struc-ture.”*Journal of Economic Literature,*50, 331–67.
Hamilton, James D. (1994).*Time Series Analysis.*Princeton, NJ: Princeton University Press.
Hamilton, James D., and Jing Cynthia Wu. (2012) “The Effectiveness of Alternative Monetary Policy Tools in a Zero Lower Bound Environment.”*Journal of Money, Credit, and Banking,*44, 3–46.
Hamilton, James D., and Jing Cynthia Wu. (2014) “Testable Implications of Affine Term Structure Models.”*Journal of Econometrics,*178, 231–42.
Ichiue, Hibiki, and Yoichi Ueno. (2013) “Estimating Term Premia at the Zero Bound: An Analysis of Japanese, US, and UK Yields.” Bank of Japan Working Paper.
Joslin, Scott, Kenneth J. Singleton, and Haoxiang Zhu. (2011) “A New Perspective On Gaussian Dynamic Term Structure Models.”*Review of Financial Studies,*27, 926–70.
Kim, Don H., and Kenneth J. Singleton. (2012) “Term Structure Models and the Zero Bound: An Empirical Investigation of Japanese Yields.”*Journal of Econometrics,*170, 32–49.
Krippner, Leo. (2012) “Modifying Gaussian Term Structure Models When Interest Rates are Near the Zero Lower Bound.” Reserve Bank of New Zealand Discussion Paper 2012/02.
Krippner, Leo. (2013) “A Tractable Framework for Zero Lower Bound Gaussian Term Struc-ture Models.” Australian National University CAMA Working Paper 49/2013.
Krishnamurthy, Arvind, and Annette Vissing-Jorgensen. (2011) “The Effects of Quantitative Easing on Interest Rates.”*Brooking Papers on Economic Activity,*43, 215–87.
Lombardi, Marco J., and Feng Zhu. (2014) “A Shadow Policy Rate to Calibrate US Monetary Policy at the Zero Lower Bound.” Working paper, BIS.
Ng, Serena, and Jonathan H. Wright. (2013) “Facts and Challenges from the Great Recession for Forecasting and Macroeconomic Modeling.”*Journal of Economic Literature,*51, 1120– 54.
Piazzesi, Monika. (2010) “Affine Term Structure Models.” In*Handbook of Financial Econo-metrics,*edited by Y. Ait-Sahalia and L. P. Hansen, pp. 691–766. New York: Elsevier.
Sims, Christopher A. (1992) “Interpreting the Macroeconomic Time Series Facts: The Effects of Monetary Policy.”*European Economic Review,*36, 975–1000.
Stock, James H., and Mark W. Watson. (2001) “Vector Autoregression.”*Journal of Economic Perspectives,*15, 101–15.
Swanson, Eric T., and John C. Williams. (2014) “Measuring the Effect of the Zero Lower Bound on Medium- and Longer-Term Interest Rates.”*American Economic Review,*104, 3154–85.
Wieland, Johannes. (2014) “Are Negative Supply Shocks Expansionary at the Zero Lower Bound?” Working paper, University of California, San Diego.
Woodford, Michael. (2012) “Methods of Policy Accommodation at the Interest-rate Lower Bound.” Jackson Hole symposium, August, Federal Reserve Bank of Kansas City.
Wright, Jonathan H. (2011) “Term Premia and Inflation Uncertainty: Empirical Evidence from an International Panel Dataset.”*American Economic Review,*101, 1514–34.
Wright, Jonathan H. (2012) “What Does Monetary Policy do to Long-term Interest Rates at the Zero Lower Bound?”*Economic Journal,*122, F447–66.
15384616, 2016, 2-3, D ow
nloaded from  https://onlinelibrary.w
iley.com /doi/10.1111/jm
cb.12300 by Statens B eredning, W
iley O nline L
ibrary on [17/04/2026]. See the T erm
s and C onditions (https://onlinelibrary.w
iley.com /term
s-and-conditions) on W iley O
nline L ibrary for rules of use; O
A  articles are governed by the applicable C
reative C om
m ons L