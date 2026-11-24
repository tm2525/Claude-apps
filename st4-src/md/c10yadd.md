## Risk models and outcome monitoring: calibration, discrimination, funnel plots and VLAD

Added 21 November 2026 from: NICOR, National Adult Cardiac Surgery Audit (NACSA) report, data 2021/22 to 2023/24 (National Cardiac Audit Programme; nicor.org.uk document 3663; publication date not stated in the document), methodology slides read from the online text. NICOR. NACSA Domain Report 2021 (HQIP), read from the online PDF. Bridgewater B, Grant S, Hickey G, Fazal N. NACSA Annual Report 2010-2011 (SCTS, NICOR, HQIP), read from the online PDF. Cosgriff R, Hickey G, Grant S, Bridgewater B. UK Heart Surgery: what patients can expect from their surgeons. NICOR 2013, read from the online PDF. Ohri SK, Benedetto U, Luthra S, et al. Coronary artery bypass surgery in the UK, trends in activity and outcomes from a 15-year complete national series. Eur J Cardiothorac Surg 2022;61:449-56, doi:10.1093/ejcts/ezab391, read from the online full text. HCAI. The California Report on Coronary Artery Bypass Graft Surgery, 2024: Technical Note (October 2026), methods read from the online PDF. New York State Department of Health, Adult Cardiac Surgery 2018-2021, methods and appendix tables read from the online PDF. NHS England (London). St George's University Hospitals cardiac surgery Independent Oversight Panel report (2020), read from the online PDF. NLCA State of the Nation 2026 Methodology Supplement (NATCAN, February 2026), read from the online PDF. HQIP National Clinical Audit Benchmarking (NCAB), Adult Cardiac Surgery (NACSA) context page (updated 3 January 2024), read online. The VLAD chart and funnel plot use invented data worked for these notes. The original EuroSCORE II derivation paper (Nashef et al., Eur J Cardiothorac Surg 2012;41) and the Thoracoscore and STS 2018 model papers could not be opened in this session, so their derivation figures are not given.

### Two properties of a risk model
| | Discrimination | Calibration |
|---|---|---|
| Question | Does the model rank patients correctly, giving those who die a higher predicted risk? | Do predicted risks match observed rates, overall and across the risk range? |
| Measure | **C-statistic** = area under the ROC curve = the proportion of (died, survived) pairs in which the patient who died had the higher predicted risk. Runs from **0.5 (chance) to 1** | **Hosmer-Lemeshow test** compares observed and predicted outcomes across deciles of risk; a non-significant P means no detectable miscalibration. Observed against expected deaths by risk group; observed-to-expected (O/E) ratio |
| Worked values | California CABG mortality model 2024: **C = 0.836** (other US states 0.777 to 0.830; the US national CMS 30-day CABG model 0.74). New York 2018-21: isolated CABG C = 0.784, valve 0.804, TAVR 0.730 | California 2024: Hosmer-Lemeshow **P = 0.217**; in all ten risk groups the observed deaths lay within the 95% CI of predicted (highest-risk group 142 observed against 146.6 predicted) |
| What spoils it | Patients unlike those the model was built on (emergency and salvage cases for EuroSCORE; acute type A dissection for EuroSCORE II and STS) | **Calibration drift**: outcomes improve over time, so an old model over-predicts |

Discrimination and calibration are separate: the original EuroSCORE over-predicted UK mortality, yet NICOR (2013) still used it to show relative trends over time.

### EuroSCORE in the UK: drift and recalibration
- Additive EuroSCORE (Nashef 1999) and logistic EuroSCORE (Roques 2003) were built on 1995 data. As UK mortality fell and predicted risk rose, logistic EuroSCORE **over-predicted**. Ohri et al. (15-year UK CABG series, 347,626 operations) applied dynamic modelling to correct for this systematic calibration drift. They report that EuroSCORE II superseded it after 2012.
- NACSA 2010-11: EACTS found isolated CABG mortality 36% lower than predicted, so UK benchmarking **multiplied the original EuroSCORE by 0.73**. Emergency and salvage cases were excluded from risk-adjusted comparison because EuroSCORE predicted them poorly; only crude mortality was reported for them.
- **Current NACSA method** (report on 2021/22 to 2023/24): predicted survival comes from "an annually recalibrated version of EuroSCORE logistic". Uncorrected, actual UK mortality is "very approximately a third" of the logistic EuroSCORE prediction. EuroSCORE II is used only to group isolated AVR patients by risk: low under 4%, medium 4 to 8%, high 8% or more.
- EuroSCORE II and STS scores are not calibrated for acute type A dissection, and EuroSCORE II included few thoracic aortic operations (already in this tab). Thoracoscore is the thoracic equivalent (Thoracic 2); its variables were not checked in this session.

### Risk-adjusted mortality
- **Risk-adjusted mortality = (observed ÷ expected) × national (or state) rate.** Expected = the sum of each patient's predicted risk. This is indirect standardisation: the unit's rate if it had the average case mix. Used by New York, and by the NLCA ("observed number of events divided by the expected number, multiplied by the overall national average").
- Outliers: New York and California flag a provider whose **95% CI lies wholly above (or below) the state rate**.

### Funnel plots and control limits
!fig f19_funnel_plot | Institutional funnel plot: risk-adjusted mortality against volume, with a national rate of 2.5% and 2 SD (about 95%, alert) and 3 SD (99.8%, alarm) limits that narrow as volume rises. A small unit at 4.1% is inside the limits; a large unit at 4.1% is an alarm. Invented units; limits computed from the binomial standard error; drawn for these notes.

- The x-axis is volume and the y-axis the risk-adjusted rate, with the national average as the reference line; the limits narrow as volume rises. A unit above the limit may reflect case mix or data quality as well as care, and surgeons work in teams (NICOR 2013).
- **UK thresholds**: HQIP alert = more than 2 SD and alarm = more than 3 SD (already in the FRCS tab). The NCAB summary of NACSA describes **99.8% (alarm) limits** on the funnel plot, with alarm-level negative outliers given priority and asked to review preventable deaths by case-note review. The **NLCA 2026** uses inner limits at 2 SD and outer limits at 3 SD around the national average, with risk adjustment by logistic regression (age, sex, Charlson index, cancer type, stage, performance status) and multiple imputation for missing data.
- **Over-dispersion** is a named limitation of simple funnel plots; the St George's oversight report notes that "many of these problems can be addressed by random effects modelling". The current NACSA report infers outlier status "using a random effects model", shown as a **forest plot** of hospitals, not a funnel. All UK hospitals were "as expected" for 2021/22 to 2023/24.

### VLAD and CUSUM
!fig f19_vlad | Variable life-adjusted display (VLAD) for 120 invented operations: the line rises by the predicted risk with each survivor and falls by (1 − predicted risk) with each death; a cluster of deaths between cases 81 and 103 turns a positive run negative. Worked for these notes.

- **VLAD**: plot the running total of (predicted risk − outcome), where outcome = 1 for death, 0 for survival. The y-axis is net lives saved against the model. A survivor at 3% predicted risk adds 0.03; a death at 3% subtracts 0.97. A rising line means better than predicted; a sustained fall is a signal to review.
- **CUSUM**: a cumulative sum that signals when it crosses a preset boundary. The **observed-minus-expected** CUSUM is the VLAD inverted. Formal risk-adjusted CUSUM methods were not read in a primary source in this session.
- Both give **real-time** monitoring between the annual national reports. Funnel plots compare units over a fixed period.

### Case study: St George's, London (Independent Oversight Panel, 2020)
- A **NICOR alert** is issued when an outcome is more than 2 SD from the mean. St George's had **two consecutive alerts**, for April 2013 to March 2016 and April 2014 to March 2017. GIRFT (2017) had also found the unit a significant outlier on several outcomes.
- Unit mortality 2015/16 to 2017/18: **3.4%** against a UK average of 2.7% (2017/18). It fell to **1.7%** from December 2018 to July 2019.
- **A unit can be an outlier when no individual surgeon is**: surgeons' denominators had been "boosted by high-volume low risk cases undertaken externally". This is why unit-level as well as surgeon-level monitoring matters.
- The response included structured judgement review of every death over 5 years by an external mortality panel, a networked audit system, minuted morbidity and mortality meetings, and protocols for managing outlying performance. The panel noted the risk of relying on a single cardiac surgery data manager.

### Surgeon against unit reporting
- NACSA is "increasingly moving away from purely reporting surgeon level mortality statistics" towards unit-level outcomes (NACSA 2021). For **dual consultant operating**, with prior documented MDT agreement, high-risk cases can be removed from a surgeon's own figures but stay in the hospital's audit.
- GIRFT (2018) likewise recommended that outcomes for complex and very high-risk cases be attributed to units, not individuals (next section).

## UK national audit 2025 to 2026: NACSA, the National Lung Cancer Audit and GIRFT

Added 21 November 2026 from: NICOR, NACSA report on data 2021/22 to 2023/24 (National Cardiac Audit Programme; nicor.org.uk document 3663; publication date not stated), "Report at a glance" and results read from the online text. NICOR, NACSA 2023 Summary Report (data 2019/20 to 2021/22, published 8 June 2023), read from the online PDF, for comparison. National Cancer Audit Collaborating Centre (RCS England). National Lung Cancer Audit State of the Nation Report 2026 (February 2026; patients diagnosed in 2024 in England and Wales), read from the NATCAN report web page; the full PDF was not opened. GIRFT. Cardiothoracic surgery: GIRFT programme national specialty report (Richens D, March 2018), from the GIRFT summary page of 12 April 2018 (14 of the 20 recommendations listed there) and the Patient Safety Learning hub summary (activity figures); the full report PDF was not opened.

### NACSA (England, Wales and Northern Ireland; data to 2023/24)
| Measure | 2023/24 (or 2021/22 to 2023/24) |
|---|---|
| Operations | **26,529**: 10% fewer than 2019/20 and about a fifth fewer than ten years earlier |
| Isolated CABG | 11,694; elective CABG 23% lower than 2019/20, urgent 2% higher |
| Isolated AVR | 3,589. **TAVI nearly three times isolated AVR**; more than 15,000 aortic valve procedures in all |
| Isolated mitral | 1,759; mitral operations 24% fewer than 2019/20 |
| Crude in-hospital mortality, all cases | **2.6%**, back to pre-pandemic levels (2.9% in 2021/22) |
| Risk-adjusted survival, UK, 3 years | **98.2%**; every hospital "as expected" |
| Isolated CABG mortality | 1.2% overall; **elective 0.49%**, urgent 1.4% |
| Isolated AVR (non-emergency) | 1.2%; AVR with CABG 2.5%. By EuroSCORE II group: **0.7% (low), 2.5% (medium), 9.4% (high)** |
| Elective CABG wait | Target 84 days from angiography; mean **130 days**; five NHS hospitals met it |
| Urgent inpatient CABG | Target: within 7 days, for 75% of patients. Met within 7 days in 23% (England), 16% (Wales) and 2% (Northern Ireland). Mean wait 14 days (best hospital 8). **No hospital met the 75% target** (best 42%, average 22%) |
| Consultant caseload | Median **96** a year (140 in 2013/14) |

**Recommendations**: (1) consultants should aim for **at least 150 cardiac operations a year**; (2) offer day-of-surgery admission to more patients, in line with GIRFT; (3) units with long postoperative stays should investigate them; (4) reduce bleeding (reoperation) where rates are higher; (5) reduce deep sternal wound infection where rates are higher; (6) submit complete data, especially complications, transfusion and MDT discussion.

For comparison, the 2023 report (data to 2021/22) recorded: reopening for bleeding after CABG 2.2% (range 0.5% to 7% by centre); transfusion after CABG about 46% (9% to 100%, with 44% of data missing); MDT discussion before valve surgery recorded in only about a third; a mitral repair rate of 60% (26% to 86% by hospital); day-of-surgery admission 11% in England (one hospital reached the 50% target); and trainees operating in about 23% of English cases.

### National Lung Cancer Audit: State of the Nation 2026 (diagnoses in 2024)
!fig f19_nlca2026 | NLCA State of the Nation 2026, England, people diagnosed in 2024: performance against audit standards (in brackets). Drawn for these notes from the NATCAN report page.

| England, 2024 | Result | Standard or comparison |
|---|---|---|
| Diagnoses | 39,409 | 36,557 in 2023 |
| Stage 1 to 2 at diagnosis | **40.2%** | 35.5% in 2023; the rise is linked to lung cancer screening |
| Stage 4 (of those staged) | 41% | 44% in 2023 |
| Diagnosed after emergency admission | 30.2% | 31.9% in 2023 |
| Pathological diagnosis (PS 0 to 1) | 81.7% | 90% |
| NSCLC resection rate | **21.8%** (7,878 operations) | 19.6% in 2023; target 17% |
| Referral to surgery, stage 1 to 2 NSCLC | Median **81 days**; about 88% waited longer than the 49-day pathway target | National Optimal Lung Cancer Pathway |
| Curative treatment, stage 1 to 2, PS 0 to 2 | 78.9% | 80% |
| Curative treatment, stage 3A, PS 0 to 2 | 59.1% | no standard given |
| Systemic therapy, advanced NSCLC, PS 0 to 1 | about 63% | 70% |
| Systemic therapy, small-cell | 71.2% | 70% |
| **90-day survival after surgery** (England and Wales; risk adjusted) | **98.4%** | outlier reporting not applied to this indicator |
| One-year survival (diagnosed January to June 2024) | 50.7%; median 372 days (stage 4: 95 days) | |

Wales (different data source; not directly comparable): resection rate 17.1%, median referral-to-surgery 91 days, stage 1 to 2 curative treatment 77.8%.

**Recommendations for surgeons and units**: review MDT decisions in stage 3A to remove barriers to curative treatment (NICE NG122); **increase thoracic surgery capacity** to meet growing demand from patients suitable for curative surgery; remove delays to systemic therapy, especially in small-cell; and advise aerobic and resistance exercise for stage 1 to 3 disease, including **before surgery** (ASCO 2022).

### GIRFT cardiothoracic surgery (Richens, March 2018)
Scope: 31 cardiothoracic units in England (about 28,000 cardiac and 69,000 thoracic operations a year); 20 recommendations; up to **£52 million** potential savings (including procurement transparency and litigation). Endorsed by the SCTS.

| Theme | Recommendation |
|---|---|
| Flow | **Day-of-surgery admission** as routine; ring-fence ICU and ward beds for cardiothoracic patients; pool non-elective cases to the next available theatre and suitable surgeon |
| Sub-specialisation | Specialist surgeons for aortovascular surgery (including rupture) and mitral surgery; **VATS** for lung resection |
| Outcomes | Outcomes a collective responsibility; complex and very high-risk cases attributed to the **unit**, not the individual; a national policy for very high-risk cases |
| Lung cancer | Fewer, centralised lung cancer MDTs; a **thoracic surgeon at every lung cancer MDT** |
| Infection | A microbiologist-led MDT review of every deep sternal wound infection |
| Data | Coders at MDT and M&M meetings; work with NICOR on data quality (theatre returns, sternal infection, stroke, renal replacement) |
| Other | Consultant review of all patients before and after surgery 7 days a week; thoracic as well as cardiac surgeons on major trauma rotas; the GIRFT five-point plan to cut litigation costs |

## Frailty before cardiac surgery and TAVI: EACTS/EAPC 2023 consensus

Added 21 November 2026 from Sündermann SH, Bäck C, Bischoff-Ferrari HA, Dehbi H-M, Szekely A, Völler H, Niebauer J. Preinterventional frailty assessment in patients scheduled for cardiac surgery or transcatheter aortic valve implantation: a consensus statement of the European Association for Cardio-Thoracic Surgery (EACTS) and the European Association of Preventive Cardiology (EAPC) of the European Society of Cardiology (ESC). Eur J Cardiothorac Surg 2023;64(4):ezad181, doi:10.1093/ejcts/ezad181 (also Eur J Prev Cardiol 31(2):146, doi:10.1093/eurjpc/zwad304). **Full text not accessible**: the abstract was read on CTSNet and the cut-offs come from a news report of the paper (Deutsches Ärzteblatt, 27 October 2023). Check them against the paper itself before relying on them in a viva. This tab already lists frailty as a gap in EuroSCORE II and STS-PROM, and the Fried index and Hospital Frailty Risk Score.

### Why and where
- Frailty assessment is now a standard part of Heart Team discussion before cardiac surgery and transcatheter procedures, but there was **no agreed method** for using it to predict outcome. EuroSCORE II and STS do not capture age-related physiological decline adequately (Ärzteblatt report).
- Written by a working group from cardiac surgery, cardiology, anaesthesia, geriatrics and biostatistics after a literature review. It covers surgery and **TAVI**. The authors propose the same approach for other transcatheter procedures, such as mitral edge-to-edge repair, because those patients resemble TAVI cohorts (abstract).
- It addresses frailty's ability to predict quality of life, complications and death, and measures before the procedure that may improve the patient's condition (prehabilitation).
- Frailty should be assessed, interpreted and acted on by a multidisciplinary team: geriatrician, anaesthetist, cardiologist and surgeon.

### Measures and cut-offs (as reported; not checked against the paper)
!fig f19_frailty | Frailty cut-offs named in the EACTS/EAPC 2023 consensus, as reported by Deutsches Ärzteblatt (27 October 2023); full text not checked. Drawn for these notes.

| Measure | Frail if |
|---|---|
| 5-metre gait speed | **below 0.8 m/s** |
| Clinical Frailty Scale | **4 or more** |
| Short Physical Performance Battery | **below 10** |
| Fried (Cardiovascular Health Study) phenotype | **3 or more** criteria |
| CT psoas muscle area, where CT is available | **below 8.5 cm²/m² (men)** or **6.5 cm²/m² (women)** |
| Nutrition and cognitive or mental state | assess before the procedure; no numeric cut-off reported |

Viva use: quote a risk score together with a frailty measure, never alone. The consensus pairs assessment with measures to improve the patient's condition before the procedure.

## ICVTS best evidence topics: perioperative drugs, AF prophylaxis and wound infection

Added 24 November 2026 from six best evidence topics in Interactive CardioVascular and Thoracic Surgery (ICVTS), cited in their rows. Read from the journal's online full text (academic.oup.com). "Full" means the whole page including the clinical bottom line was read; "Part" means the abstract, question, search and evidence table were read but the page was cut off before the bottom line section, so the conclusion is the abstract's.

### Tranexamic acid dose

| Three-part question | Papers (found, best) | Bottom line and numbers | Citation, how read |
|---|---|---|---|
| In adults having cardiac surgery, what dose of tranexamic acid is most effective and safe? | 586, 12 | High dose (over 80 mg/kg in total) bleeds less than low dose (under 50 mg/kg). Sigaut 2014 trial (569 patients), low v high: blood loss on day 1 820 v 590 ml, blood product units 4.1 v 2.5, re-operation for bleeding 6.2% v 2.5%; transfusion rate, death and seizures did not differ. The benefit was largest in patients at high bleeding risk; trials that excluded them found no difference. Seizures rise with dose in observational data: Sharma 2014 (11,529 patients) 0.3% after a 50 mg/kg bolus v 2.6% with over 80 mg/kg, odds ratio 14.3; Kalavrouziotis 2012: over 100 mg/kg predicted seizure within 24 hours (odds ratio 2.6), and about 30% of those patients had an old brain lesion on imaging. Causation is unproven. Recommended: high bleeding risk 30 mg/kg bolus, 16 mg/kg/h infusion and 2 mg/kg in the prime; low risk 10 mg/kg bolus, 1 mg/kg/h and 1 mg/kg in the prime. | Hodgson S, Larvin JT, Dearman C. ICVTS 2015;21(3):384-388. doi:10.1093/icvts/ivv134. Full (two fetches) |

!fig f43_txa_dose | Bleeding and seizure figures for low and high-dose tranexamic acid as reported in Hodgson, Larvin and Dearman, ICVTS 2015 (my chart; the seizure pair is observational)

The current guideline line already in this tab (total dose no more than 100 mg/kg) matches the dose above which Kalavrouziotis 2012, in this BET, found seizures more likely.

### Preventing postoperative atrial fibrillation

| Three-part question | Papers (found, best) | Bottom line and numbers | Citation, how read |
|---|---|---|---|
| In cardiac surgery, are prophylactic beta-blockers of benefit in reducing postoperative AF? | 113, 8 (5 meta-analyses) | Yes: number needed to treat about 7. Crystal 2002 (27 trials, 3,840 patients): AF 33% to 19%. Andrews 1991: 34% to 8.7%. Sotalol reduced AF more than other beta-blockers. No reduction in stroke. Best agent and benefit with a poor ventricle unclear. | Omorphos S, Hanif M, Dunning J. ICVTS 2004;3(4):641-646. doi:10.1016/j.icvts.2004.07.014. Full |
| In cardiac surgery, does preoperative statin therapy prevent postoperative AF? | 445, 12 | Yes in 10 of 12 studies, with less stroke and shorter stay; best dose, drug and duration (3 days to 2 months) unknown. Kuhn 2014 (91,491 patients): odds ratio 0.71 (0.61 to 0.82). ARMYDA-3 (atorvastatin 40 mg for 7 days, 200 patients): 35% v 57%. Chen 2010 meta-analysis of trials: relative risk 0.57, number needed to treat 8. Two large studies found no effect (Yin 2010, Virani 2008). | Goh SL, Yap KH, Chua KC, Chao VTT. ICVTS 2015;20(3):422-428. doi:10.1093/icvts/ivu402. Full |
| In CABG, does posterior pericardiotomy reduce postoperative AF? | 12, 7 | Yes: number needed to treat 6. Biancari 2010 meta-analysis of trials (763 patients): AF 10.8% v 28.1%, odds ratio 0.33 (0.16 to 0.69). Two of the six trials were neutral (Asimakopoulos 1997, Arbatli 2003). | Kaleda VI, McCormack DJ, Shipolini AR. ICVTS 2012;14(4):384-389. doi:10.1093/icvts/ivr099. Part |

!fig f43_poaf_prevention | Postoperative AF with and without beta-blockers, posterior pericardiotomy and preoperative atorvastatin, from the pooled or trial results quoted in three ICVTS best evidence topics (my chart)

The statin BET (2015) predates the guideline line already in this tab: the 2024 EACTS perioperative medication guideline says do not start a statin shortly before surgery because of kidney injury (class III) but continue an existing one (IIa). Mention the change.

### Other drugs and wound infection

| Three-part question | Papers (found, best) | Bottom line and numbers | Citation, how read |
|---|---|---|---|
| Before cardiac surgery, should ACE inhibitors or angiotensin II receptor blockers be omitted to avoid postoperative vasodilation? | 421, 11 (3 randomised) | Omitting them is rational, as preoperative use lowers systemic vascular resistance and predicts vasoplegia, but the evidence is weak. Tuman 1995 (4,301): two or more vasoconstrictor infusions in 7.7% v 4.0%. Mekontso-Dessap 2001: ACE inhibitor an independent predictor of vasoplegia after bypass (relative risk 2.26). Webb 1998 trial: no difference in resistance on bypass. | Raja SG, Fida N. ICVTS 2008;7(3):470-475. doi:10.1510/icvts.2007.174698. Part |
| In cardiac surgery, does routine topical antimicrobial use prevent sternal wound infection? | 238, 11 | Topical antibiotics reduce both superficial and deep infection, but agents, doses and definitions vary too much for a general recommendation. Kowalewski 2017 meta-analysis of topical vancomycin (20,039 patients): any sternal infection relative risk 0.24. Kowalewski 2015 meta-analysis of gentamicin-collagen sponges (23,102 patients, 4 trials): relative risk 0.62, mediastinitis 0.64. | Magro PL, Sousa Uva M. ICVTS 2021;32(3):452-456. doi:10.1093/icvts/ivaa292. Part |

### Using these in a viva

- Note the contrast in the drug questions: the BETs of 2004 to 2015 support beta-blockers (still class I to continue), but the statin and ACE inhibitor advice has since been rewritten by the 2024 EACTS perioperative medication guideline in this tab (continue, rather than start or stop).
- Tranexamic acid: give the two regimens and the reason for the cap. Seizure risk is the cost of high doses; in Koster 2013 (in the BET's table) the link with seizures held for open-heart surgery but not for CABG.

## SCTS 2025 to 2026: position statements, guidance and audit news

Added 24 November 2026 from: SCTS position statements page (scts.org/about_scts/position_statements.aspx), read through a summarising extract; SCTS statement on patient safety, complex case management, consultant collaboration and teamwork (27 November 2025, scts.org/news/780), read through a summarising extract; SCTS Statement on the Retraining and Reskilling of Consultants in Cardiothoracic Surgery (January 2026, scts.org PDF), read through a summarising extract; SCTS Executive combined meeting report, June 2026, and its audit sub-committee report (June 2026) and adult cardiac sub-committee report (May 2026), read through summarising extracts. NICOR NCAP 2025 annual report: only a news summary (Arden and GEM CSU) was read, which gave no figures. The notes already hold the NACSA report on data to 2023/24, the NLCA 2026 and GIRFT (UK national audit 2025 to 2026, above); no newer NACSA report or SCTS "blue book" was found.

### Position statements

| Statement | Date | Content |
|---|---|---|
| Patient safety, complex case management, consultant collaboration and teamwork | 27 November 2025 (after the September 2025 unit representatives meeting) | Seven principles: (1) safety above all; (2) risk **reduction**, not risk **avoidance**, so complex patients are not denied surgery; (3) safety nets: checklists, MDT decisions, peer review, transparent M&M, escalation protocols; (4) **dual or multiple consultant operating and anaesthesia** for high-risk or complex cases, with mentoring and proctoring essential when new procedures are introduced; (5) collaborative culture; (6) continuous data collection and open sharing of outcomes, complications and near misses, including with patients for consent; (7) managers must fund realistic job plans for dual operating, resilient rotas and protected time for audit and peer review. No numerical thresholds |
| Retraining and reskilling of consultants | January 2026 | For a consultant returning after restriction, suspension, investigation or absence (not for new procedures). Prompt, fair investigation (delay erodes skills); PPAS may give expert assessment and programme advice. A written **learning agreement** mapped to the ISCP curriculum, with roles, duration, review and sign-off criteria. **Two named consultant supervisors** with paid time; an independent educational supervisor; an external senior mentor. Monthly progress reviews, formal review at least every 3 months, MCR and MSF; WBAs, logbook and reflection. No on-call at first; fixed-term contract; target **3 to 12 months**. Competence for paediatric, transplant, aortic, mitral and robotic surgery at least at senior fellowship level. The **trust** funds, delivers and signs off; the SCTS advises only when invited |
| UK transplant services | April 2026 | Cardiothoracic transplant services are not meeting international standards and are under strain; investment is not reaching surgical teams, critical care and perioperative pathways; surgeons and patients have not been consulted enough. An SCTS working group is building a framework for UK and Ireland heart and lung transplant services. The transplant committee (re-formed 2025) has run three Delphi rounds and proposes renaming itself the Mechanical Circulatory Support and Cardiothoracic Transplant Committee |
| Aprotinin | Submitted to the Executive 16 January 2026 | Drafted at the MHRA's request after review of off-label use. Context: licence suspended 2007, restricted indication 2013 with a registry condition (NAPaR). In NAPaR, **52.2%** of patients given aprotinin across nine European countries were in the UK; of UK patients, **20%** had isolated CABG and **80%** high-risk surgery (aortic, valve, endocarditis). The statement text was not found |
| SDCEP antibiotic prophylaxis against infective endocarditis | 2025 to 2026 | SCTS endorsed the revised SDCEP implementation advice supporting NICE CG64, UK-wide |

Other guidance in progress (June 2026): RIB-GUIDE on rib fractures (being finalised); "Managing Risk" guidance (published; not read); a congenital "Framework for Good Practice in Congenital Heart Surgery in the UK and Ireland" (completed).

### Audit and data

| Item | Detail (SCTS reports, May to June 2026) |
|---|---|
| NICOR adult cardiac | Data deadline 31 May 2026, outlier analysis to follow. New deputy adult cardiac audit lead (S Budhia); an SCTS dashboard project chasing unit submissions |
| Congenital | S Stoica is NICOR national congenital (NCHDA) clinical lead, the first surgeon in that role; a congenital data bank has stalled over cost and burden |
| **Thoracic returns 2025/26** | **37 of 38 centres; more than 11,000 procedures, 21% more than the previous year; mortality after minimally invasive lobectomy about 0.5%** |
| National Thoracic Database | Built with Epic, hosted on the cardiac model through the University of Bristol; a part-time database manager funded |
| National Ambulatory Chest Drain Audit | Starts August 2026 (retrospective data from thoracic centres) |
| Thoracic State of the Nation | The SCTS is preparing a Thoracic Surgery State of the Nation report; NHS England's National Diagnostic Standards of Care and Optimal Pathways for Thoracic Oncology are due |
| NCAP 2025 annual report | "Very low" mortality and complication rates for adult and congenital surgery; most TAVI under conscious sedation, percutaneous transfemoral. No figures in the summary read |

### National work touching cardiac surgery

- NICE: SCTS expert advice on IP2042 (microaxial flow pump for cardiogenic shock). NICE published HTG774 and HTG775 on these pumps in March 2026 (see the NICE HealthTech section below); which of them IP2042 became was not confirmed.
- Health Technology Wales: SCTS review of TAVI reassessment at intermediate risk and a new low-risk topic.
- NHS England type B aortic dissection toolkit (combined societies), to extend to post-surgical surveillance and incidental aortic dilatation.
- Proposed NCEPOD study of non-traumatic aortic emergencies (ruptured AAA and acute dissection), supported by the SCTS.
- National rollout of minimally invasive cardiac surgery with ERACS will need perfusion training; cannula supply depends mostly on one US manufacturer.
- RAMP (military casualty reception) planning, led by the SCTS for cardiothoracic surgery.

### Viva points

- Dual consultant operating is now the SCTS position for high-risk cases, with job planning to fund it: a useful answer to "how would you manage a very high-risk case?" alongside GIRFT's unit attribution of high-risk outcomes.
- Retraining: trust-led, learning agreement, two supervisors plus mentor, 3 to 12 months, no on-call initially.
- Minimally invasive lobectomy mortality in the UK is about 0.5% (SCTS 2025/26 returns).


## NICE HealthTech guidance 2025 to 2026 for cardiac surgery: TAVI valves, TAVI for aortic regurgitation and microaxial flow pumps

Added 24 November 2026 from: NICE HTG757, Transcatheter heart valves for transcatheter aortic valve implantation to treat aortic stenosis: late-stage assessment (21 August 2025, minor update December 2025; replaces HTE31); NICE HTG752, TAVI for native aortic valve regurgitation (24 June 2025 as IPG805; migrated to HTG752 in January 2026 with no change); NICE HTG775, Percutaneous insertion of a catheter-based left ventricular microaxial flow pump for cardiogenic shock (25 March 2026); NICE HTG774 overview page (surgical insertion of the same pump; last reviewed 25 March 2026). HTG757, HTG752 and HTG775 read from the guidance PDFs through summarising extracts; HTG774 from its overview page only (recommendations not shown). None of these was in the notes. Former interventional procedures and early value assessment documents now carry HealthTech (HTG) numbers: IPG805 became HTG752, and HTE31 was replaced by HTG757.

### TAVI valves: HTG757 (August 2025)

| Recommendation | Content |
|---|---|
| 1.1 | Not enough evidence to say whether price differences between transcatheter valves are justified |
| 1.2 | Trusts should offer a **range** of valves so a clinically suitable one is available for everyone |
| 1.3 | If more than one valve is suitable, use the **least expensive** |
| 1.4 | Enter everyone into the **UK TAVI registry** (NICOR) |

Reasoning: over half of patients do not need a particular valve; anatomy and calcium distribution predict outcome. The registry (7,409 procedures with identifiable device; 3,917 with complete linked data; follow-up to 31 months) showed some in-hospital differences between valves in stroke, aortic regurgitation and pacemaker rate, none after discharge, and could not separate valve from patient effects. Valves covered include Evolut, Sapien 3, Navitor, Myval Octacor, Allegra, Hydra and Trilogy (ACURATE neo2 withdrawn). Equality point: women more often need small valves, and some people decline particular valves for religious or cultural reasons.

### TAVI for native aortic regurgitation: HTG752 (2025)

| Patient group | Recommendation |
|---|---|
| SAVR unsuitable or high risk | Can be used **with special arrangements** for clinical governance, consent and audit or research, while evidence is generated |
| SAVR suitable and not high risk | **Research only** |
| Everyone | Selection by an experienced MDT (interventional cardiologist, cardiac surgeon, imaging expert; cardiac anaesthetist and elderly-care physician as needed) who set risk and valve; specialised centres with cardiac and vascular surgical backup; UK TAVI registry |

Committee comments: devices not approved for regurgitation had worse safety; may not suit significant aortic root dilatation. Evidence: 10 studies, mostly small observational, short term.

### Microaxial flow pump for cardiogenic shock: HTG775 (March 2026)

- Percutaneous LV microaxial flow pump **can be used during an evidence generation period** with **enhanced informed consent** and **audit** (registry, or NICE's audit tool).
- Only **primary PCI centres with on-site intensive care expertise**, by trained clinicians, with a **bleeding management protocol**.
- Rationale: one randomised trial showed better survival than standard care in **infarct-related** cardiogenic shock, but with strict eligibility; benefit in wider shock is unknown; observational data are inconsistent; serious bleeding occurs. Uses: bridge to recovery, transplant or durable LVAD. (The NICE document does not name the trial or give its figures.)
- HTG774 covers **surgical** insertion (through a graft into an artery); its recommendations were not read.

### Viva points

- Choosing a TAVI valve: suitability first, then cost (NICE HTG757); register every case.
- Pure aortic regurgitation: SAVR remains standard; TAVI only under special arrangements in inoperable or high-risk patients.
- Impella-type support in infarct-related shock is now NICE-sanctioned in primary PCI centres, under audit and enhanced consent.


## Cardiac rehabilitation phases 1 to 4 (SIGN 57)

Added 24 November 2026 from Scottish Intercollegiate Guidelines Network. Cardiac rehabilitation: a national clinical guideline (SIGN 57). January 2002. scotphn.net PDF, read through a summarising extract of the first 100,000 of 139,000 characters (sections 1 to 6); and The Heart Manual / NHS Lothian, Cardiac Rehabilitation training resource (about 2017), read through a summarising extract. The notes (Coronary surgery tab, BACPR section) say that a definition of numbered phases was not found in a primary source; SIGN 57 gives one. SIGN 57 dates from 2002: check whether it has been replaced before quoting it as current. BACPR refers instead to the six-stage Department of Health pathway of care (see the Coronary surgery tab).

| Phase | Setting and timing | Content |
|---|---|---|
| 1 | In hospital, or after any "step change" (MI, new angina, emergency admission, **cardiac surgery**, angioplasty, new heart failure) | Medical evaluation, reassurance and education, correcting misconceptions, risk factor assessment, **mobilisation**, discharge planning; family involved |
| 2 | Early after discharge, mostly at home | Home visits, telephone contact, supervised self-help (the Heart Manual); covers the period when patients feel isolated |
| 3 | Structured exercise, historically hospital-based, increasingly community | Exercise with education, psychological support and risk factor advice; menu-based (smoking, weight, vocational rehabilitation, referral onward). **At least two exercise sessions a week for at least eight weeks** |
| 4 | Long term, community (for example a support group at a leisure centre) | Maintenance of physical activity and lifestyle change; benefit lasts only if sustained |

After surgery: comprehensive rehabilitation is recommended after coronary revascularisation, surgical or percutaneous (**grade A**); it lowered lipids and improved perceived health, while exercise-only programmes improved capacity but not lipids or weight; no trial was powered for mortality after revascularisation. Rehabilitation starts once medically stable; SIGN 57 sets no start day for exercise after sternotomy. The Heart Manual resource notes that a phase model can exclude patients never admitted.

Viva point: phase numbers are old shorthand; the BACPR standards (in the Coronary surgery tab) give the timings to quote now: referral during the admission or within 24 h of discharge, assessment within 10 working days, at least 8 weeks of programme.

## Who is high risk for low output, and the Heart Team decision on pre-emptive support: EACTS 2025 protected cardiac surgery consensus

Added 24 November 2026 from Lorusso R, Salazar L, Nersesian G, Milojevic M, Schmack B, Engelman DT, et al. EACTS Expert Consensus Document on protected cardiac surgery: pre-emptive use of temporary mechanical circulatory support in adult cardiac surgery patients at high risk for perioperative low cardiac output syndrome. Eur J Cardiothorac Surg 2026;68(3):ezaf296 (online 9 October 2025); doi:10.1093/ejcts/ezaf296. Read in full from the published PDF (sections 3 to 6 and 15, Figure 2). The document's statements carry no class or level (approval needed 75% agreement in an anonymous vote). Its statements and device tables are in Cardiac 15, "Protected cardiac surgery" parts 1 to 3.

### Size of the problem
About 10% of cardiac surgical patients develop perioperative low cardiac output syndrome (LCOS), which raises hospital mortality 12 to 24 times. Even with temporary support, survival to discharge is about 40%. The age of patients referred has risen by about 1.2 years every 4 years, with more women and more comorbidity, fewer isolated CABG and more combined and aortic operations.

### Features that predict LCOS
- Text (section 6.2): older age, female sex, previous cardiac surgery, LV dysfunction, acute endocarditis, coronary disease with previous infarction, left main disease, preoperative renal impairment; urgent or emergency surgery for acute infarction, especially if revascularisation will be incomplete.
- Figure 2 list: reduced uni- or biventricular function, previous cardiac surgery, age over 70, acute-onset cardiovascular disease, endocarditis with septic shock, previous infarction or complex coronary disease, acute renal impairment, urgent or emergency operation, refractory shock or cardiac arrest.
- Signs of hypoperfusion: cold peripheries, slow capillary refill, mottling, confusion, low urine output; metabolic acidosis, raised lactate, low SvO2, falling GFR, rising urea and liver enzymes. Thresholds (VIS, cardiac index, cardiac power, PCWP, lactate, SvO2, RV and LV echo indices) are in Cardiac 15, part 1.
- Imaging: echo for LV and RV function (LVEF a main predictor of LCOS) and structural lesions; CT for vascular access (calcification, patency, tortuosity) for both the operation and the device.

### Risk scores
- EuroSCORE II and the STS score are the usual tools. The STS score uses more cardiac variables but tends to give lower mortality than EuroSCORE; EuroSCORE II was built for elective surgery and is poorly validated in emergencies.
- In a patient on high-dose inotropes, tMCS or CPR, combine the surgical score with a shock score: the vasoactive-inotropic score (drug load), INTERMACS profile (clinical state and inotrope need) and the SCAI stage (shock-focused).

### The pathway
!fig f56_pathway | Assessment of a patient at high risk of post-cardiotomy shock for pre-emptive temporary support. Drawn for these notes from the EACTS 2025 protected cardiac surgery consensus, Figure 2 (which the authors adapted from Stein and Silvestry)

### The Heart Team (section 4)
| Member | Role in protected surgery |
|---|---|
| Cardiac surgeon | Leads the operation, chooses the tMCS strategy, coordinates theatre and postoperative care |
| Intensivist | Perioperative care, LCOS, runs the device, ICU transitions |
| Interventional and heart failure cardiologists | Clinical, echo and haemodynamic assessment; drug and catheter options; eligibility for transplant or LVAD |
| Anaesthetist | Intraoperative stability and monitoring |
| Critical care nurse | Continuous monitoring, early warning of instability |
| Perfusionist | Runs the device in theatre and ICU, shares weaning protocols |
| Clinical pharmacist | Drug therapy and interactions |
| Palliative care specialist | Futility and end-of-life discussions in line with the patient's values |

Standard handoffs: before the operation (baseline haemodynamics, plan, risks) and after it (intraoperative events, support in place, immediate goals). On deterioration the team reassesses and escalates between devices or to durable support.

### Consent and futility (section 15)
Before starting, discuss: risks and benefits for that patient; possible prolonged dependence on the device and its effect on independence and quality of life; possible escalation to transplant or LVAD; and that support may become futile. Allow time for reflection with family. The patient either consents or chooses a do-not-initiate MCS order. Involve palliative care and ethics early, to help judge futility and withdrawal, guide on ethical and legal aspects and support everyone involved.
