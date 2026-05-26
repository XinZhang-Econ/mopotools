# Effects of QE on Bond Yields

**Summary**: Quantitative easing has been shown to reduce long-term government bond yields by 40-150 basis points per program, primarily through the portfolio balance channel. Effects are strongest during periods of financial stress.

**Research classification**: Empirical

**Sources**: bernanke20120831a-pdf.md, ijcb-v9n2-unconventional-monetary-policy-and-great-recession-estimating-macroeconomic-effects-spread.md, dell-ariccia-et-al-2018-unconventional-monetary-policies-in-the-euro-area-japan-and-the-united-kingd.md, ecbwp1956-pdf.md

**Last updated**: 2026-04-21

---

## Overview

The most directly measurable effect of [[quantitative-easing]] is on government bond yields. Central bank purchases of long-term bonds should raise prices and lower yields. This is the first step in the [[transmission-channels]] that ultimately affect the real economy.

## Theoretical Mechanism

Bond yields can be decomposed into:

**Yield = Expected future short rates + Term premium**

QE affects both components:

1. **Expected future short rates**: Signaling channel - QE indicates rates will stay low
2. **Term premium**: Portfolio balance channel - removing duration risk reduces the compensation investors demand for holding long-term bonds

Most evidence suggests the **term premium** channel dominates for QE. (source: dell-ariccia-et-al-2018)

## United States

### Event Study Evidence

| Study | Program | 10-Year Yield Impact |
|-------|---------|---------------------|
| Gagnon et al. (2011) | QE1 ($1.7T) | -38 to -82 bps |
| D'Amico & King (2012) | QE1 | -50 bps (10-15yr segment) |
| Krishnamurthy & Vissing-Jorgensen (2011) | QE1 | -107 bps |
| Hamilton & Wu (2012) | QE1 | -13 bps |
| Bernanke (2012) | QE1 | -40 to -110 bps |
| Bernanke (2012) | QE2 ($600B) | -15 to -45 bps |

The wide range reflects methodological differences. See [[research-debates]]. (source: bernanke20120831a-pdf.md)

### Key Findings

- Effects concentrated in longer maturities (consistent with duration risk removal)
- MBS yields fell more than Treasuries during QE1 (direct purchase effect)
- Corporate bond yields also fell through rebalancing

## United Kingdom

| Study | Program | 10-Year Yield Impact |
|-------|---------|---------------------|
| Joyce et al. (2011) | QE1 £200bn | -100 bps |
| Christensen & Rudebusch (2012) | QE1/QE2 | -47 bps |
| Bridges & Thomas (2012) | QE1 | -150 bps |

### Decomposition

UK studies found portfolio balance effects dominated:
- Expected future short rates declined only modestly
- Term premium compression explained most of yield decline
- This suggests QE works through asset scarcity, not just signaling

(source: dell-ariccia-et-al-2018)

## Euro Area

| Study | Program | Yield Impact |
|-------|---------|--------------|
| Andrade et al. (2016) | APP | -45 bps (average) |
| Koijen et al. (2016) | APP | -2 to -60 bps (varies by country) |
| Altavilla et al. (2014) | OMT | -199 bps (Italy 2y), -234 bps (Spain 2y) |
| Krishnamurthy et al. (2018) | OMT/SMP | -200 to -1000 bps (peripheral 2y) |
| De Pooter et al. (2015) | SMP | -32 to -40 bps (liquidity premium) |

### Peripheral vs. Core

Effects varied dramatically across member states:
- Germany and France: Modest declines (already low yields)
- Italy, Spain: Large declines (high initial spreads)
- Greece, Portugal, Ireland: Very large declines (crisis-level spreads)

The ECB programs were particularly effective at addressing **redenomination risk** and **liquidity premia** in peripheral countries. (source: dell-ariccia-et-al-2018)

## Japan

| Study | Program | 10-Year Yield Impact |
|-------|---------|---------------------|
| Lam (2011) | Oct 2010 announcement | -10 bps |
| Arai (2017) | QQE1 | -14 bps |
| Hausman & Wieland (2014) | QQE1 | -11 bps |

### Why Smaller Effects?

Japanese yields were already very low before QE, leaving less room for compression:
- 10-year JGBs yielded ~0.5% before QQE1
- Compare to US 10-year at ~4% before QE1

When yields are already near zero, the portfolio balance channel has less room to operate. (source: dell-ariccia-et-al-2018)

## Sweden

Pass-through from policy rate to market rates during the Riksbank's QE and negative rate period (2015-2019):

| Rate | Pass-through Coefficient |
|------|-------------------------|
| Interbank rate (STIBOR) | ~1.0 |
| 3-month mortgage rate | ~1.0 |
| Corporate loan rate | ~1.0 |
| Deposit rate | Substantial |
| 10-year government bond | ~0.1 |

Interest rate spreads over the policy rate remained relatively stable during unconventional policies, consistent with effective transmission. The lower pass-through to 10-year bonds reflects the greater role of global factors in long-term rates for a small, open economy. (source: riksbank-evaluation-12012026-pdf.md)

See [[qe-sweden]] for details.

## Cross-Country Comparison

### Factors Affecting Yield Impact

1. **Initial yield level**: Higher starting yields allow larger declines
2. **Financial stress**: Effects larger when markets are distressed
3. **Program size**: Larger programs have larger effects (but not necessarily proportional)
4. **Asset type**: Purchasing specific sectors (MBS, corporate bonds) affects those yields more
5. **Communication**: Clear commitment amplifies effects

### Persistence

Most studies find yield effects are **persistent**, not just temporary announcement effects:
- Ghysels et al. (2016): Euro area effects persisted for months
- Joyce et al. (2011): UK effects remained elevated throughout QE period

## Beyond Government Bonds

QE affects yields across asset classes through portfolio rebalancing:

### Corporate Bonds

- US: Investment-grade corporate yields fell alongside Treasuries
- UK: Corporate yields declined, especially for bonds similar to purchased gilts
- Euro area: CSPP directly targeted corporate bonds

### Mortgage Rates

- US: Fed's MBS purchases directly reduced mortgage rates
- Key channel for housing market and consumer spending

### Emerging Market Bonds

QE spillovers affected EM yields:
- "Search for yield" pushed investors into EM debt
- EM yields fell, currencies appreciated
- Spillover effects were controversial (concerns about "currency wars")

## Caveats and Limitations

### Identification Challenges

Event studies face issues:
- Other news may coincide with announcements
- Only capture "surprise" component
- May miss gradual effects

VAR approaches face issues:
- Small samples during QE period
- Parameter instability
- Difficult to isolate QE shocks

### Stock vs. Flow

Debate continues whether:
- **Stock matters**: Total holdings drive yields (preferred habitat)
- **Flow matters**: Monthly purchase pace matters
- **Both matter**: Evidence supports both mechanisms

## Related Pages

- [[quantitative-easing]]
- [[transmission-channels]]
- [[effects-on-gdp]]
- [[effects-on-inflation]]
- [[research-debates]]
- [[qe-united-states]]
- [[qe-united-kingdom]]
- [[qe-euro-area]]
- [[qe-japan]]
- [[qe-sweden]]
