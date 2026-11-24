## Risk adjustment in congenital heart surgery: RACHS-1, Aristotle, STAT and PRAiS2

Added 21 November 2026 from: Jacobs ML, Jacobs JP, Thibault D, et al. Updating an empirically based tool for analyzing congenital heart surgery mortality. World J Pediatr Congenit Heart Surg 2021;12:246-81, doi:10.1177/2150135121991528 (abstract read via the Duke Scholars record); STS Congenital Heart Surgery Database, Appendix C, STAT Mortality Categories, dated 24 June 2020 (PDF read; procedure rows checked twice); O'Brien SM and colleagues, An empirically based tool for analyzing mortality associated with congenital heart surgery, J Thorac Cardiovasc Surg 2009 (PubMed 19837218; abstract only); Kansy A, Maruszewski B, Jacobs J, Maruszewski P. Application of four complexity stratification tools to evaluate early congenital heart surgery outcomes over 16 years at a single institution. Kardiochir Torakochir Pol 2013;10:115-9, doi:10.5114/kitp.2013.36129 (online full text); Rogers L, Brown KL, Franklin RC, et al. Improving risk adjustment for mortality after pediatric cardiac surgery: the UK PRAiS2 model. Ann Thorac Surg 2017;104:211-9 (full text PDF, UCL Discovery); Brown KL, Rogers L, Barron DJ, et al. Incorporating comorbidity within risk adjustment for UK pediatric cardiac surgery. Ann Thorac Surg 2017;104:220-6 (full text PDF, UCL Discovery). The Aristotle score ranges and levels were not found in a primary source I could open today and are left out.

### Why congenital surgery needs its own tools
- Case mix differs between centres and deaths are few, so crude mortality misleads. The stated purpose of STAT is to let hospitals with different case mix be compared (O'Brien 2009).
- Two families: **procedure-based categories** (RACHS-1, Aristotle Basic, STAT), which describe case mix, and **patient-level models** (PRAiS2 in the UK), which add patient factors and give each child a predicted probability.

### The four procedure-based tools compared

| Tool | How built | Structure | Notes from the sources |
|---|---|---|---|
| RACHS-1 (references 2002 and 2004) | Not described in the sources read | 6 levels of increasing mortality risk | Scored 74.4% of operations in the Kansy single-centre series |
| Aristotle Basic Complexity | Not described in the sources read (corrected 24 November 2026: expert-panel scoring, 1999 to 2003, by the Aristotle working group; now described in the Aristotle score section added 24 November) | Sum of potential for mortality, potential for morbidity and technical difficulty | Scores about 98% of coded operations; covered 89% in the Kansy series |
| STAT 2009 (STS-EACTS) | Empirical: about 77,000 operations, 2002 to 2007, Bayesian estimates for 148 procedures | Score 0.1 to 5.0; 5 categories | Procedure mortality 0.3% to 29.8%; C-index about 0.78, better than RACHS-1 and Aristotle Basic |
| STAT 2020 | Empirical: 161,351 operations, 110 centres, January 2010 to June 2017 | 235 scored operations (58% more than 2009); 5 categories | Validation 46,933 operations at 108 centres: C-statistic 0.791 (score), 0.779 (category). About half the 2009 codes changed category |

- Single-centre test (Kansy 2013, 7,493 operations in patients aged 18 or under, hospital mortality 4.38%): C-index STAT score 0.768, RACHS-1 0.765, STAT categories 0.750, Aristotle Basic 0.746. In the 6,534 operations all four could score: 0.777, 0.765, 0.772 and 0.721. The paper is internally inconsistent about which differences were significant.
- STAT rules: a combined operation takes the risk of its highest-risk component, unless the combination's own estimate differs; Bayesian modelling handles small numbers; category boundaries were chosen to minimise variation within and maximise variation between categories.

!fig f17_stat_categories | STAT 2020 mortality categories: number of procedure codes and the range of estimated in-hospital mortality in each. Drawn for these notes from Jacobs and colleagues, World J Pediatr Congenit Heart Surg 2021 (abstract).

### STAT category examples (viva list)

!fig f17_stat_examples | Example operations in each STAT category with their mortality scores. Drawn for these notes from the STS CHSD Appendix C list dated 24 June 2020; the document does not say whether these assignments are the 2009 or the 2020 calibration, so check against the current list before quoting a score.

- Points worth knowing: sinus of Valsalva aneurysm repair is category 1 (0.3); the one-and-a-half ventricle repair is category 2 (0.4); the arterial switch is category 3 (0.8) but becomes category 4 with VSD closure (1.4); a modified BT shunt (1.5) and a PA band (1.7) are category 4, riskier than a complete AVSD repair; heart transplant is category 4 (1.4); Norwood is 4.0 and truncus with interrupted arch 5.0.
- I found no row for pulmonary atresia with intact septum; its operations are scored by component (shunt, one-and-a-half ventricle repair, Glenn, Fontan).

### PRAiS2: the UK patient-level model
- **Outcome**: death within 30 days of the first operation in a 30-day surgical episode. Logistic regression.
- **Development**: NCHDA 2009 to 2014, 21,838 episodes in 18,834 patients, 539 deaths (2.5%). Cross-validated AUC median 0.83 (0.82 to 0.83). **Test set**: 4,207 episodes, 97 deaths (2.3%), AUC 0.86 (95% CI 0.82 to 0.89). A recalibrated original PRAiS gave 0.80 on the same data.
- **Variables**: specific procedure (49 procedures in 15 risk groups plus "no specific procedure"); primary diagnosis (29 categories in 11 groups); age and weight as non-linear fractional polynomials (avoids jumps in risk at age-band edges); univentricular heart; bypass or not; era (2013 onwards); four comorbidity flags.
- **Comorbidity flags** (adjusted odds ratios for 30-day death): additional cardiac risk factor, for example cardiomyopathy or raised pulmonary artery pressure, 2.20 (1.61 to 3.03); acquired comorbidity 1.99 (1.52 to 2.61); severity of illness, for example preoperative ventilation or circulatory support, 1.75 (1.40 to 2.18); congenital comorbidity 1.52 (1.18 to 1.95). Down syndrome and prematurity lost significance on multivariable analysis and were dropped. 73.7% of episodes had none of the four. Each is yes or no, so several similar codes do not inflate the risk.
- **Changes from PRAiS1**: 29 procedure categories became 49 specific procedures; 3 diagnosis categories became 29; one comorbidity flag became four; number of functioning ventricles became a univentricular indicator; parameters 38 to 36; the HLHS hybrid procedure added.
- **Known weakness**: it under-predicts risk for the hybrid HLHS procedure; the authors suggest running it with and without hybrid cases.
- Adults (16 and over) in the UK audit are risk-adjusted with the STAT score, not PRAiS2 (NCHDA 2022 report).

## Aristotle score: components, levels and the comprehensive score

Added 24 November 2026 from (1) Erek E, Yılmaz B, Kaya M, et al. Analysis of results according to the Aristotle scoring system in congenital heart surgery. Turk Gogus Kalp Dama 2014;22(3):509-16, doi:10.5606/tgkdc.dergisi.2014.9144 (open-access full text PDF, read through the extraction tool); (2) von Segesser LK. Aristotle scores in congenital heart surgery (editorial). Eur J Cardiothorac Surg 2004;25:909-10 (full text); (3) Sata S, Haun C, Weber T, et al. A morbidity score for congenital heart surgery based on observed complications. Eur J Cardiothorac Surg 2012;41:898-904, doi:10.1093/ejcts/ezr161 (full text to 100,000 of 116,000 characters); (4) Jacobs JP, Jacobs ML, Maruszewski B, et al. Initial application in the EACTS and STS Congenital Heart Surgery Databases of an empirically derived methodology of complexity adjustment. Eur J Cardiothorac Surg 2012;42:775-80, doi:10.1093/ejcts/ezs026 (full text to 100,000 of 108,000 characters). The original Lacour-Gayet 2004 paper was not opened. The risk-adjustment section above says the Aristotle components were "not described in the sources read"; this fills that gap.

### How it was built

- Developed 1999 to 2003 by the Aristotle working group led by François Lacour-Gayet: delegates from 50 centres in 23 countries (von Segesser; Erek). Built on **expert opinion** ("subjective probability"), not observed outcomes, which is the main criticism and the reason STAT was later derived empirically (Jacobs 2012).
- Used by the STS and EACTS congenital databases from 2002 (Jacobs 2012).

### Aristotle Basic Complexity (ABC) score

- A fixed score per **procedure**, range **1.5 to 15**: the sum of three components, each scored by the panel: **potential for mortality, potential for morbidity, and technical difficulty** (Erek). (Morbidity is capped at 5 points, Sata; the morbidity component is estimated indirectly from ICU stay.)
- Examples: ASD repair 3.0 to 3.4; VSD patch 6.2; arterial switch 10 to 10.7; Norwood 14.5 (Erek; Sata).

### Aristotle Comprehensive Complexity (ACC) score

- ABC plus **patient** factors, range 1.5 to **25** (Erek):
  - procedure-dependent factors, 0 to 5 points: anatomical variants and associated procedures;
  - procedure-independent factors, 0 to 5 points: general state, clinical parameters, extracardiac anomalies, preoperative ventilation, renal failure.

### Levels

| Level | Score | Applies to |
|---|---|---|
| 1 | 1.5 to 5.9 | ABC and ACC |
| 2 | 6.0 to 7.9 | ABC and ACC |
| 3 | 8.0 to 9.9 | ABC and ACC |
| 4 | 10.0 to 15.0 | ABC and ACC |
| 5 | 15.1 to 20 | ACC only |
| 6 | 20.1 to 25 | ACC only |

Mortality rose with ACC level in Erek's single-surgeon series of 167 operations (2012, overall hospital mortality 12.5%): level 1 3.7%, level 2 4.5%, level 3 13.6%, level 4 18.8%, level 5 2 of 3, level 6 1 of 1. ACC correlated with mortality, morbidity (ICU stay 7 days or more) and difficulty (bypass over 120 minutes).

### Performance

- The scores exist partly so that a unit taking harder cases is credited for it (Jacobs 2012). The original Aristotle definition of performance (complexity combined with survival) is in Lacour-Gayet 2004, which was not opened. Sata proposed: performance = Aristotle score × (1 − observed morbidity score / 5).
- Against observed complications, ABC and ACC discriminated well in Sata's series (c-statistic 0.92 and 0.94) and the Aristotle morbidity estimate correlated with observed morbidity (r = 0.75 for operations done at least five times). Sata suggested the arterial switch is over-scored and the bidirectional cavopulmonary shunt under-scored.
- The planned successor combines STAT mortality, a STAT morbidity score and technical difficulty (Jacobs 2012). In head-to-head testing STAT discriminates mortality better than ABC (section above).
