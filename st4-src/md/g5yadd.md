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

## Echocardiography in congenital heart disease: transthoracic views, intraoperative TOE and residual lesions

Added 25 November 2026 from: TSRA Review of Cardiothoracic Surgery 3rd ed., ch. 88 (Overbey DM, Turek JW, Congenital cardiac physiology and evaluation), re-read in full on disk; Lai WW, Geva T, Shirali GS, et al. Guidelines and standards for performance of a pediatric echocardiogram: a report from the Task Force of the Pediatric Council of the American Society of Echocardiography. J Am Soc Echocardiogr 2006;19(12):1413–1430, doi:10.1016/j.echo.2006.09.001 (ASE open PDF, read through an extraction tool); Lopez L, Saurers DL, Barker PCA, et al. Guidelines for performing a comprehensive pediatric transthoracic echocardiogram: recommendations from the American Society of Echocardiography. J Am Soc Echocardiogr 2024;37(2):119–170, doi:10.1016/j.echo.2023.11.015 (ASE open PDF, first two thirds read through an extraction tool); Puchalski MD, Lui GK, Miller-Hance WC, et al. Guidelines for performing a comprehensive transesophageal echocardiographic examination in children and all patients with congenital heart disease: recommendations from the American Society of Echocardiography. J Am Soc Echocardiogr 2019;32(2):173 onwards (end page not shown in the extraction; text runs to at least p. 211), doi:10.1016/j.echo.2018.08.016 (ASE open PDF, whole document read through an extraction tool in three passes); ASE 2010 paediatric quantification recommendations (ASE open PDF; citation details not shown in the extraction; first 100,000 characters read). **The 2024 ASE paediatric TTE guideline replaces Lai 2006 and the 2010 quantification document**; both are given because the brief asked for Lai 2006 and the views are largely the same. The tab already covers segmental nomenclature (Congenital 8) and catheter Qp:Qs (above); this section adds the echo examination.

### Why echo, and its limits (TSRA ch. 88)

- Echo is the mainstay: transthoracic, transoesophageal and fetal. In most cases it gives enough to plan care. Adjuncts: bubble study for shunts, 3D for structure and function.
- Limits: small field of view, needs windows, operator-dependent, may need sedation.
- MRI adds extracardiac anatomy, pulmonary veins and flow (phase-contrast: forward flow in the PA = Qp, in the aorta = Qs). CT: fast, high spatial resolution, radiation and contrast. Catheterisation is now mainly for pulmonary vascular resistance and when non-invasive data are inadequate.

### The segmental approach on echo

Lai 2006 and Lopez 2024 both require the examination to describe each segment in sequence, but neither prints a step list for acquisition; Lopez 2024 does not insist on a fixed order of views. Lopez's report order (Table 18) is the sequence to recite: **situs, segmental anatomy, systemic and pulmonary veins, atria and atrial septum, AV valves, ventricles and ventricular septum, outflow tracts, great arteries (including coronaries), duct, pericardium, pleura and diaphragm.** Many laboratories start subcostally to establish situs (Lai).

### Transthoracic windows and what each shows

| Window and view | Shows (Lai 2006; Lopez 2024) |
|---|---|
| Subcostal coronal (situs) | Abdominal situs (liver, stomach; spleen if situs is abnormal), IVC and descending aorta side by side, hepatic veins to IVC to RA |
| Subcostal sagittal | IVC and abdominal aorta with Doppler: a damped upstroke or slow return to baseline in diastole suggests arch obstruction |
| Subcostal long axis (coronal sweep) | IVC to RV outflow; atrial septum at low Nyquist; coronary sinus; left coronary ostium |
| Subcostal short axis (sagittal, bicaval) | SVC and IVC, right upper pulmonary vein, ventricles base to apex, RVOT with Doppler |
| Subcostal oblique views | Right anterior oblique: RV inflow and outflow together. Left anterior oblique: atrial septum and the AV valves en face |
| Apical four-chamber | Both AV valves, ventricular septum, coronary sinus to RVOT sweep, one right pulmonary vein, RV-focused view, TAPSE |
| Apical five and three-chamber | LVOT, aortic valve, ascending aorta; Doppler of the LVOT |
| Apical two-chamber | LA, LV, mitral valve; global and regional function |
| Parasternal long axis | Sweep from tricuspid to pulmonary valve: RA, TV, coronary sinus; LA, LV, MV, AV, root (annulus, sinuses, sinotubular junction); RVOT, PV and main PA |
| Parasternal short axis | Aortic valve morphology, coronary origins (with colour), RV infundibulum, PV and branch PAs, mitral valve, LV at papillary level (M-mode) |
| High left parasternal (ductal) | Main PA, left PA, duct, distal arch and descending aorta |
| Suprasternal long axis | Arch and branches, isthmus, proximal descending aorta with pulsed and continuous wave |
| Suprasternal short axis | Arch sidedness, left innominate vein to SVC, the "crab" view of the four pulmonary veins entering the LA, left PA |
| Right parasternal | SVC and IVC, atrial septum, superior sinus venosus defect, right upper pulmonary vein to LA, right PA |

Specific targets:
- **Atrial septum:** best from subcostal and right parasternal windows (Lai). Agitated saline: contrast in the LA within 3 to 6 cycles of RA opacification suggests an interatrial shunt; after more than 6 cycles, an intrapulmonary shunt. Contrast injected into a left-sided SVC that appears in the coronary sinus then both atria suggests an unroofed coronary sinus (Lopez).
- **Ventricular septum:** colour sweeps subcostal, apical and parasternal; pulsed and continuous wave coaxial with the jet to judge direction and restriction; look for multiple defects and relate each to the AV and semilunar valves (Lopez). Lopez lists RV systolic pressure from the tricuspid jet or the VSD gradient, and PA pressure from the duct gradient.
- **Coronary origins:** parasternal short axis with 2D and colour at a low Nyquist limit; still frames alone are not enough. Retrograde flow suggests anomalous origin from the PA or ostial atresia (Lopez).
- **Arch:** suprasternal views with the neck extended; measure proximal and distal transverse arch and isthmus; suspicion signs are a long gap between left carotid and left subclavian, a posterior shelf, colour turbulence, a double envelope on continuous wave, and a damped abdominal aortic trace (Lopez).
- **Z scores:** body size predicts structure size; ±2 is the usual normal limit; use one model for serial studies; normal values do not apply to obese children (Lopez).

Pitfalls: in children outflow diameters are small and elliptical, so continuity-based volumes are not used routinely; Doppler gradients can exceed catheter peak-to-peak gradients by 20% to 40% because of pressure recovery (ASE 2010). An uncomplicated full study takes 45 to 60 minutes; sedation needs a written policy (Lai).

### Qp:Qs by echo

- The ASE documents read state the continuity principle (stroke volume = cross-sectional area x velocity-time integral, the same at each point in a closed system) and warn that outflow diameters in children vary too much for routine volume calculation. **A specific echo Qp:Qs formula was not found in the parts read**; by that principle it would be pulmonary stroke volume over systemic stroke volume, with the diameter error squared.
- In theatre, Puchalski recommends Qp:Qs "by echo or blood oxygen saturation" for a 3 to 4 mm residual VSD. The saturation method and worked examples are in "Shunts and Qp:Qs" above. MRI phase-contrast flow is the non-invasive reference (TSRA ch. 88).

### Transoesophageal echo in children and congenital disease (Puchalski 2019)

Not the sole or primary diagnostic test in children: every child having cardiac surgery should have a preoperative TTE.

| Indication group | Examples |
|---|---|
| Diagnostic | Non-diagnostic TTE; PFO with stroke; embolic source; baffles after Fontan, Senning or Mustard; acute aortic pathology; vegetation or abscess; thrombus before cardioversion or ablation |
| Intraoperative | Immediate pre-bypass definition of anatomy and function; post-bypass results and function; monitoring ventricular volume and function; intracardiac and intravascular air and adequacy of de-airing |
| Interventional guidance | Septal occluders, septostomy, stents, percutaneous valves, ablation, minimally invasive surgery, catheter assist devices |

Contraindications: absolute include unrepaired tracheo-oesophageal fistula, perforated viscus, active upper GI bleeding, an uncontrolled airway, severe respiratory depression. Relative include previous oesophageal or gastric surgery, varices or diverticulum, oesophagitis (stricture is also listed, in an unclear column), **vascular ring or arch anomaly**, severe coagulopathy, cervical spine problems; after gastrostomy or fundoplication only oesophageal windows are used.

Complications: 1% to 3% in children. Dysphagia after TOE in 18% of children having open-heart surgery (risk: age under 3, preoperative intubation, longer intubation, left-sided obstructive surgery); endoscopic findings in 64% without long-term feeding problems. Insertion is harder at 4 kg or less. Rare: oesophageal perforation, gastric laceration at sternotomy, subglottic stenosis.

Probe by weight: micro-multiplane over 2.5 kg and mini-multiplane over 3.0 to 3.5 kg (both used safely below these); adult 2D probe over 25 kg; adult 3D matrix over 30 kg.

The guideline describes **28 views** (15 mid-oesophageal, 5 transgastric, 3 deep transgastric, and upper oesophageal arch, PA and descending aortic views); the examination is structure-based, not view-based, with 2D, colour and spectral Doppler from more than one view. Views a surgeon should know: ME four-chamber (septa, AV valves, coronary sinus), ME long axis (LVOT, RVOT), ME aortic valve short axis (cusps, coronary ostia), ME RV inflow-outflow (TV, RVOT, PV, outlet septum), ME bicaval (SVC, IVC, atrial septum, sinus venosus defects), ME right and left pulmonary veins, transgastric mid-papillary short axis (LV size and function, muscular septum), deep transgastric five-chamber (MV, LVOT, aortic valve) and RVOT views, upper oesophageal arch short axis (PA, duct).

Practice: complete the pre-bypass study **before skin incision** to avoid diathermy artefact; insert the probe before draping. In theatre a second person trained in TOE or congenital anaesthesia should be present so that monitoring is not neglected. Training: at least 50 supervised examinations and 25 supervised probe insertions.

### Residual lesions after bypass: when to go back (Puchalski 2019)

| Lesion | Threshold or advice |
|---|---|
| Residual VSD | 2 mm or less usually closes; 3 mm or less usually not significant; 3 to 4 mm: measure Qp:Qs (echo or saturations); **4 mm or more, or Qp:Qs over 1.5, usually warrants another attempt**. Check more than one view; weigh AR, outflow obstruction and haemodynamics |
| Mitral stenosis (mean gradient) | Under 5 insignificant; 5 to 8 possibly significant; over 8 significant. Over 5 mmHg suggested as the cut-off for further repair or replacement |
| Mitral regurgitation (jet width) | Under 2 mm insignificant; 2 to 4 possibly; over 4 mm significant. Consider returning to bypass for more than mild MR |
| LVOT or aortic valve | Peak gradient over 40 mmHg may need reintervention. Low output just after bypass can make obstruction look smaller |
| Aortic regurgitation | Jet over 4 mm: risk of significant AR later |
| Pulmonary regurgitation | Jet 50% to 65% of the RVOT = severe |
| Tricuspid regurgitation | Re-image at several times (loading, contractility and AV synchrony change); Nyquist 50 to 60 cm/s to compare with pre-bypass; may be underestimated with low preload; a high velocity may mean residual VSD or RVOT obstruction |
| Tetralogy | Look for residual RVOT obstruction; TR velocity gives RV pressure. **Dynamic** obstruction from a hypercontractile RV is not revised |
| AVSD | TOE before repair in essentially all; residual AV valve regurgitation or outflow obstruction may prompt return (the Congenital 9 single-patch section adds: significant residual regurgitation means back on bypass) |
| Arterial switch | Both outflows, regional wall motion (coronary transfer), coronary flow in diastole at low Nyquist, neo-aortic and neo-pulmonary valves, residual shunts |
| Glenn, Fontan | Narrowing or turbulence at the cavopulmonary anastomosis; thrombus; fenestration; residual right-to-left shunt; positive pressure may impede flow |
| TAPVC | Turbulence at the confluence anastomosis suggests stenosis or torsion; quantify with spectral Doppler and discuss return. Loss of phasic pulmonary venous flow suggests stenosis |

Decisions also weigh anaesthetic depth, haemodynamics, vasoactive drugs and the risk of more bypass. The paediatric ICU section (Congenital 13) gives the saturation and pressure clues to a residual lesion once the child is on the unit.

!fig f61_residual_vsd | Original decision chart for a residual VSD on post-bypass TOE, with the guideline thresholds for other lesions after repair. Drawn for these notes from Puchalski et al., ASE 2019.

Percentages of patients who return to bypass after intraoperative TOE were not given in the guideline text read.
