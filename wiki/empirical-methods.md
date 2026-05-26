# Empirical Methods for Studying QE

**Summary**: Researchers use three main empirical approaches to study QE effectiveness: event studies for immediate market reactions, vector autoregressions (VARs) for dynamic macro effects, and DSGE models for structural analysis. Each method has strengths and limitations, contributing to the wide range of estimates in the literature.

**Research classification**: Both (methodological review with empirical applications)

**Sources**: fifty-shades-of-qe-pdf.md, ijcb-v9n2-unconventional-monetary-policy-and-great-recession-estimating-macroeconomic-effects-spread.md, dell-ariccia-et-al-2018-unconventional-monetary-policies-in-the-euro-area-japan-and-the-united-kingd.md, riksbank-evaluation-12012026-pdf.md

**Last updated**: 2026-04-21

---

## Overview

Measuring the effects of [[quantitative-easing]] is challenging because QE programs were deployed during extraordinary circumstances, making counterfactuals difficult to construct. Researchers have developed several empirical strategies, each with distinct advantages and limitations.

## Event Studies

### Approach

Event studies examine asset price movements in narrow windows (minutes to days) around QE announcements.

**Steps**:
1. Identify announcement dates and times
2. Measure yield/price changes in tight window around announcement
3. Attribute changes to the policy "surprise"

### Strengths

- **Clean identification**: Market movements in narrow windows can be attributed to the announcement
- **High-frequency data**: Intraday data available for many markets
- **Model-free**: Doesn't require structural assumptions about the economy

### Limitations

- **Captures only surprises**: If markets anticipated the announcement, measured effect is understated
- **Persistence unclear**: Announcement effects may not persist
- **Confounding news**: Other information may arrive on announcement days
- **Extrapolation difficult**: Hard to translate yield changes into GDP/inflation effects

### Key Studies Using Event Studies

| Study | Finding |
|-------|---------|
| Gagnon et al. (2011) | Fed QE1 reduced 10-year yields 38-82 bps |
| Krishnamurthy & Vissing-Jorgensen (2011) | Fed QE1 reduced 10-year yields 107 bps |
| Joyce et al. (2011) | BoE QE1 reduced 10-year yields 100 bps |

(source: dell-ariccia-et-al-2018)

## Vector Autoregressions (VARs)

### Approach

VARs estimate dynamic relationships between QE shocks and macroeconomic variables over time.

**Steps**:
1. Specify a system of equations relating policy variables to macro outcomes
2. Identify QE "shocks" through timing restrictions, sign restrictions, or external instruments
3. Trace impulse responses of GDP, inflation, yields to shocks

### Strengths

- **Dynamic effects**: Captures how effects build and fade over time
- **Macro outcomes**: Can estimate GDP and inflation effects directly
- **Relatively model-free**: Fewer structural assumptions than DSGE

### Limitations

- **Identification challenges**: Isolating QE shocks from other factors is difficult
- **Small samples**: Limited observations during QE period
- **Specification sensitivity**: Results depend on variable selection, lag length
- **Time variation**: Fixed-coefficient VARs may miss changing relationships

### Time-Varying Parameter VARs (TVP-VARs)

Baumeister and Benati (2013) argued that economic relationships shifted during the crisis, making fixed-coefficient VARs inappropriate. Their TVP-VAR approach found larger effects:

- Without Fed QE: GDP would have contracted 10% (annualized) in 2009Q1
- Without BoE QE: Output growth would have dropped 12% at annual rates

This suggests standard VAR methods may underestimate QE effects during crisis periods. (source: ijcb-v9n2-unconventional-monetary-policy-and-great-recession-estimating-macroeconomic-effects-spread.md)

### Key VAR Studies

| Study | Method | Key Finding |
|-------|--------|-------------|
| Baumeister & Benati (2013) | TVP-VAR | QE prevented Great Depression-level collapse |
| Weale & Wieladek (2016) | Bayesian VAR | +0.25% GDP per 1% of GDP in purchases |
| Kapetanios et al. (2012) | VAR | UK QE raised GDP 1.5%, inflation 1.25 pp |

(source: dell-ariccia-et-al-2018)

## DSGE Models

### Approach

Dynamic Stochastic General Equilibrium models simulate QE effects within structural macroeconomic frameworks.

**Steps**:
1. Specify a model with optimizing households, firms, and central bank
2. Add QE mechanisms (portfolio balance, financial frictions)
3. Calibrate or estimate parameters
4. Simulate counterfactuals with/without QE

### Strengths

- **Theory-consistent**: Results grounded in economic theory
- **General equilibrium**: Accounts for feedback effects across the economy
- **Counterfactual analysis**: Can evaluate hypothetical scenarios
- **Policy analysis**: Can inform optimal QE design

### Limitations

- **Model dependence**: Results depend on structural assumptions
- **QE as add-on**: Standard models don't naturally include QE mechanisms
- **Calibration uncertainty**: Parameters often difficult to pin down
- **Linearity**: Most models assume linear dynamics, may miss nonlinearities

### Key DSGE Approaches

**Gertler-Karadi (2011, 2013)**: Added financial intermediaries with leverage constraints. When central bank purchases reduce private-sector risk exposure, intermediaries can expand lending.

**Preferred Habitat (Vayanos-Vila 2009)**: Investors have preferences for specific maturities. Central bank purchases of long-term bonds reduce term premia.

**Chen-Cúrdia-Ferrero (2012)**: Combined portfolio balance with credit frictions to model Fed QE2.

(source: dell-ariccia-et-al-2018)

### The Swedish MAJA Model

Sweden's Riksbank uses the MAJA DSGE model for forecasting and policy analysis:

**Strengths**:
- Two-region framework (Sweden + trading partners)
- Sophisticated modeling of Swedish economy features
- Includes labor union wage-setting, exchange rate dynamics

**Limitations**:
- Fixed frequency of price changes (Calvo framework)
- Linear responses to shocks
- Underperformed during Covid inflation surge

(source: riksbank-evaluation-12012026-pdf.md)

## High-Frequency Identification

### Approach

Uses intraday data to identify monetary policy shocks in very narrow windows around announcements.

**Steps**:
1. Measure changes in interest rate futures in 30-minute windows around announcements
2. Use these as "external instruments" for policy shocks
3. Trace effects through the economy

### Application to Sweden

Almerud et al. (2024) applied high-frequency identification to Swedish data:
- Found forward guidance shocks are close substitutes for actual rate changes
- Estimated 1 pp policy rate increase reduces GDP by 1.5% at peak

(source: riksbank-evaluation-12012026-pdf.md)

## Narrative Approaches

### Approach

Identify monetary policy shocks by examining historical records and central bank communications to find "exogenous" policy changes.

### Application: Swedish 2010-11 Episode

Coglianese et al. (2025) used the Riksbank's 2010-11 rate increases as a natural experiment:
- Riksbank raised rates primarily for financial stability (household debt) concerns
- Inflation was below target, suggesting rates would otherwise have been lower
- Found very large effects: 1 pp rate increase reduced GDP by ~5%

This narrative approach suggests conventional methods may underestimate monetary policy effects. (source: riksbank-evaluation-12012026-pdf.md)

## Comparing Methods

### Why Estimates Vary

| Factor | Effect on Estimates |
|--------|---------------------|
| Method choice | Event studies vs VARs vs DSGE yield different results |
| Sample period | Crisis vs. normal times matter |
| Identification | Different shock identification strategies |
| Model specification | Variable selection, lags, restrictions |

### The "Fifty Shades of QE" Problem

Fabo et al. (2021) documented that central bank researchers systematically report larger QE effects than academic researchers:

- Gap persists after controlling for methodology
- May reflect institutional incentives, selection effects, or data access
- Raises concerns about research credibility

(source: fifty-shades-of-qe-pdf.md)

### Cross-Method Comparison (Sweden)

| Study | Method | GDP Effect (1 pp rate rise) |
|-------|--------|----------------------------|
| Berggren et al. (2024) | Bayesian VAR | -0.7% to -0.8% |
| Almerud et al. (2024) | High-frequency | -1.5% |
| Coglianese et al. (2025) | Narrative | -5% |

Even for the same country over similar periods, methods yield substantially different estimates. (source: riksbank-evaluation-12012026-pdf.md)

## Best Practices

Based on the literature, robust QE analysis should:

1. **Use multiple methods**: Triangulate with event studies, VARs, and models
2. **Report uncertainty**: Confidence intervals, not just point estimates
3. **Consider time variation**: Relationships may differ in crisis vs. normal times
4. **Be transparent about identification**: Clearly state assumptions
5. **Pre-register designs**: Reduce publication bias concerns

## Related Pages

- [[research-debates]]
- [[quantitative-easing]]
- [[effects-on-yields]]
- [[effects-on-gdp]]
- [[effects-on-inflation]]
- [[transmission-channels]]
