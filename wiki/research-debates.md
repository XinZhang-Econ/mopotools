# Research Debates on QE Effectiveness

**Summary**: Empirical research on QE effectiveness shows wide variation in estimates. A notable finding is that central bank researchers tend to report larger effects than academic researchers, raising questions about methodology and potential conflicts of interest.

**Research classification**: Empirical (meta-analysis and methodology review)

**Sources**: fifty-shades-of-qe-pdf.md, dell-ariccia-et-al-2018-unconventional-monetary-policies-in-the-euro-area-japan-and-the-united-kingd.md

**Last updated**: 2026-04-21

---

## The Central Question

How effective is [[quantitative-easing]]? Despite over a decade of research, estimates vary enormously:

- **Yield effects**: 13 to 150 basis points per program
- **GDP effects**: 0.25% to 4%
- **Inflation effects**: 0.3% to 2%

Why such wide ranges?

## "Fifty Shades of QE"

Fabo, Jančoková, Kempf, and Pástor (2021) conducted a meta-analysis of QE research and found a striking pattern: **central bank researchers report significantly larger QE effects than academic researchers**. (source: fifty-shades-of-qe-pdf.md)

### Key Findings

1. Papers authored by central bank staff find statistically significantly larger effects
2. The gap persists after controlling for methodology, sample, and other factors
3. The difference is economically meaningful - not just statistical artifact

### Potential Explanations

**Institutional incentives**: Central bankers may face pressure (explicit or implicit) to justify policies their employers have pursued.

**Selection effects**: Central banks may be more likely to publish research finding positive effects.

**Different priors**: Central bank researchers may have different theoretical frameworks or beliefs about policy effectiveness.

**Data advantages**: Central banks have access to proprietary data that may reveal effects invisible to academics.

The authors do not definitively resolve which explanation dominates, but note the pattern is "disconcerting from the perspective of research credibility." (source: fifty-shades-of-qe-pdf.md)

## Methodological Issues

### Event Studies

**Approach**: Examine asset price movements in narrow windows around QE announcements

**Strengths**:
- Clean identification (market moves attributed to announcement)
- High-frequency data available

**Weaknesses**:
- Captures only "surprise" component
- Doesn't measure persistence of effects
- Assumes no confounding news on announcement days
- Difficult to extrapolate to macro effects

### Vector Autoregressions (VARs)

**Approach**: Estimate dynamic relationships between QE shocks and macro variables

**Strengths**:
- Can estimate GDP and inflation effects
- Captures dynamic transmission
- Model-free (doesn't impose structural assumptions)

**Weaknesses**:
- Identification is challenging
- Results sensitive to specification choices
- Limited sample sizes for QE period
- Time-varying parameters may be important

### DSGE Models

**Approach**: Simulate effects in structural macroeconomic models with explicit QE mechanisms

**Strengths**:
- Theory-consistent
- Can evaluate counterfactuals
- Accounts for general equilibrium effects

**Weaknesses**:
- Results depend on model structure
- QE mechanisms are add-ons to standard models
- Calibration/estimation uncertainty

### Time-Varying Parameter VARs

Baumeister and Benati (2013) argued that fixed-coefficient VARs are inappropriate because economic relationships shifted during the crisis. Their TVP-VAR approach found larger effects, suggesting standard methods underestimate QE impact. (source: ijcb-v9n2-unconventional-monetary-policy-and-great-recession-estimating-macroeconomic-effects-spread.md)

## Identification Challenges

The fundamental problem: QE was implemented during extraordinary circumstances, making it hard to construct a counterfactual.

### Confounding Factors

- Other policy interventions (fiscal stimulus, bank bailouts)
- Evolving economic conditions
- Global spillovers
- Expectations of future QE

### The Endogeneity Problem

QE was deployed *because* conditions were bad. Naively comparing periods with/without QE conflates the policy effect with the underlying economic deterioration.

## Cross-Country Comparisons

Comparing across countries faces challenges:

- Different program designs
- Different economic structures
- Different starting conditions
- Different credibility levels

Japan's underwhelming results don't necessarily mean QE doesn't work - it may mean QE is less effective when:
- Yields are already near zero
- Deflationary expectations are entrenched
- Central bank credibility is low

(source: dell-ariccia-et-al-2018)

## Areas of Relative Consensus

Despite uncertainty, most researchers agree:

1. **QE reduced long-term yields** - event study evidence is fairly robust
2. **QE had positive effects on GDP and inflation** - direction is clear even if magnitude is disputed
3. **Effects were larger during financial stress** - consistent with theory
4. **Transmission channels operate** - portfolio balance, signaling, liquidity effects all documented
5. **No runaway inflation** - fears of hyperinflation proved unfounded

## Areas of Ongoing Debate

1. **Magnitude of effects** - varies by factor of 3-10x across studies
2. **Stock vs. flow effects** - do purchases matter or just the accumulated holdings?
3. **Diminishing returns** - is QE3 less effective than QE1?
4. **Financial stability risks** - long-term consequences still unclear
5. **Optimal exit strategy** - how to unwind without disruption?
6. **Balance sheet costs** - how to weigh fiscal costs of QE against benefits?

## The Sweden Case: A Comprehensive Evaluation

The 2026 Ravn-Wilkins evaluation of Sweden's Riksbank provides a unique opportunity to assess QE effectiveness with hindsight:

### Mixed Evidence on QE Effectiveness

| Period | GDP Effect | Inflation Effect | Assessment |
|--------|-----------|-----------------|------------|
| 2015-2019 | ~1% | +20-50 bps | Modest but positive |
| 2020-2022 | ~0.2% | +0.25 pp | Weaker than pre-Covid |

Key finding: Covid-era QE had much weaker effects than pre-Covid QE, attributed to:
- Asset composition (more covered bonds with weaker transmission)
- Market stress had already subsided when some programs implemented
- Smaller purchases relative to economy

(source: riksbank-evaluation-12012026-pdf.md)

### Balance Sheet Consequences

Sweden provides a cautionary tale on QE costs:
- Peak balance sheet: 27.5% of GDP (early 2022)
- Large mark-to-market losses when rates rose in 2022
- Required SEK 25 billion capital injection from government (0.39% of GDP)

The Ravn-Wilkins evaluation notes that "the Riksbank did not have a sufficiently developed framework for assessing the evolving risks of unconventional policies." (source: riksbank-evaluation-12012026-pdf.md)

### Methodological Diversity in Swedish Research

Three recent studies of Swedish monetary policy use different identification strategies:

| Study | Method | Findings |
|-------|--------|----------|
| Berggren et al (2024) | Bayesian VAR with timing restrictions | Moderate GDP effects (-0.7% to -0.8% per 1pp rate rise) |
| Almerud et al (2024) | High-frequency identification | Larger GDP effects (-1.5% peak) |
| Coglianese et al (2025) | Narrative quasi-experiment (2010-11) | Very large effects (-5% GDP) |

This illustrates the methodological uncertainty discussed above - even for the same country, different approaches yield substantially different estimates. (source: riksbank-evaluation-12012026-pdf.md)

### Key Lessons from Sweden

1. **Exchange rate channel is crucial** for small, open economies
2. **Balance sheet risks** should be assessed more systematically ex-ante
3. **Market-functioning vs. stimulus** QE should be distinguished
4. **Exit strategies** should be predefined
5. **Coordination** between monetary and fiscal authorities matters

See [[qe-sweden]] for full details.

## Implications

The uncertainty in QE research suggests:

1. **Humility is warranted** in claiming precise estimates
2. **Robust communication** by central banks requires acknowledging uncertainty
3. **Pre-registration** of research designs could reduce publication bias concerns
4. **Institutional diversity** in research (not just central banks) is valuable
5. **Historical perspective** will take decades to develop

## Related Pages

- [[quantitative-easing]]
- [[transmission-channels]]
- [[effects-on-yields]]
- [[effects-on-gdp]]
- [[effects-on-inflation]]
- [[qe-sweden]]
