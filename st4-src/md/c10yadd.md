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
