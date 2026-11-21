"""Drawings from the gap-fill agents, 21 November 2026."""
from figs import svg, T, box, arrow, line, bars, tiles, W, E  # noqa: F401

# ---- figs_F1.py



def f1_resp_failure():
    """Hypoxaemia after lung resection: exclude the treatable causes, then treat as ALI/ARDS."""
    b = box(170, 8, 380, 50, ['New hypoxaemia or infiltrate after lung resection', 'ABG, film, ECG, cultures, review the drain'], 'b1', 'f-h')
    b += arrow(360, 58, 360, 80)
    b += T(360, 98, 'Exclude the treatable causes first (ALI/ARDS is a diagnosis of exclusion)', 'f-h')
    spec = [
        ('Retention, collapse', ['Sputum: physiotherapy;', 'bronchoscopic toilet'], 'b0'),
        ('Pneumonia, aspiration', ['Cultures (BAL);', 'antibiotics'], 'b0'),
        ('Fistula or torsion', ['CT and bronchoscopy;', 're-explore if torsion'], 'warn'),
        ('PE, cardiac, fluid', ['CTPA, echo;', 'treat AF or ischaemia'], 'b0'),
    ]
    for i, (h, s, c) in enumerate(spec):
        x = 10 + i * 178
        b += f'<rect x="{x}" y="110" width="166" height="86" rx="9" class="f-{c}"/>'
        b += T(x + 83, 132, h, 'f-h') + T(x + 83, 156, s, 'f-s')
    b += arrow(360, 198, 360, 222)
    b += box(110, 224, 500, 52, ['None found: primary ALI/ARDS (usually days 0 to 3)', 'Secondary ALI follows a complication (days 3 to 12)'], 'warn', 'f-h')
    b += arrow(360, 276, 360, 298)
    b += box(10, 300, 340, 92, ['Lung-protective ventilation', 'Tidal volume 6 to 8 ml/kg predicted weight', 'Plateau under 30 cmH2O; PEEP', 'SpO2 88 to 95%; pH down to 7.25 accepted'], 'b0')
    b += box(370, 300, 340, 92, ['Moderate to severe ARDS', 'Prone 16 h a day, started within 12 to 24 h', 'Restrict fluid, diuretics', 'Dexamethasone (DEXA-ARDS)'], 'b0')
    b += T(360, 414, 'Mortality once ventilated: about 25 to 40% (Alam 2007; Dulu 2006); 50% after pneumonectomy', 'f-s')
    return svg(426, b)


def f1_ali_rates():
    h, b = bars([('Sublobar resection', 0.88, 'ok'), ('Lobectomy or bilobectomy', 2.96, 'b1'), ('Pneumonectomy', 7.9, 'warn')],
                '%', 10, 'ALI/ARDS needing ventilation rises with resection extent (Dulu 2006, 2,192 resections)')
    h2, b2 = bars([('Sublobar resection', 22, 'ok'), ('Lobectomy or bilobectomy', 42, 'b1'), ('Pneumonectomy', 50, 'warn')],
                  '%', 100, 'Hospital mortality of those patients (overall 40%)')
    return svg(h + h2, b + f'<g transform="translate(0 {h})">{b2}</g>')


def f1_bpf_algorithm():
    b = box(130, 8, 460, 54, ['Suspected fistula: new or large air leak, sepsis, cough with', 'pleural fluid, falling air-fluid level, surgical emphysema'], 'b1', 'f-h')
    b += arrow(360, 62, 360, 82)
    b += box(60, 84, 600, 54, ['First: operated side down, head up; drain the space; cultures and antibiotics;', 'protect the other lung; then CT and bronchoscopy to confirm and size it'], 'warn')
    b += arrow(250, 138, 180, 166) + arrow(470, 138, 540, 166)
    b += box(10, 168, 340, 40, 'Early (under 2 weeks): usually technical', 'b0', 'f-h')
    b += box(370, 168, 340, 40, 'Late: poor stump healing, infected space', 'b0', 'f-h')
    b += arrow(100, 208, 100, 230) + arrow(260, 208, 260, 230)
    b += box(10, 232, 170, 108, ['Fit, defect over', '5 mm: re-explore,', 'debride, re-close,', 'flap cover'], 'ok')
    b += box(190, 232, 160, 108, ['Under 5 mm or', 'unfit: glue, valve,', 'occluder, stent', '(many fail)'], 'b1')
    b += arrow(460, 208, 460, 230) + arrow(620, 208, 620, 230)
    b += box(370, 232, 170, 108, ['Unfit or small', 'collection: open', 'window (avoid', 'after LUL)'], 'b1')
    b += box(550, 232, 160, 108, ['Fit, large defect:', 'completion', 'pneumonectomy', '(lobectomy BPF)'], 'ok')
    b += arrow(360, 340, 360, 360)
    b += box(60, 362, 600, 44, 'When clean: obliterate the space (serratus, latissimus, omentum, thoracoplasty)', 'b0')
    return svg(416, b)


def f1_bpf_rates():
    h, b = bars([('Segmentectomy', 0.18, 'ok'), ('Lobectomy', 0.54, 'b1'), ('Bilobectomy', 2.56, 'warn'), ('Pneumonectomy', 4.19, 'warn')],
                '%', 5, 'Bronchopleural fistula rises with resection extent (series of 4,794)')
    return svg(h, b)


def f1_poaf_risk():
    return tiles([('Under 5%', ['Low risk: bronchoscopy,', 'mediastinoscopy, VATS wedge,', 'pleural procedures'], 'ok'),
                  ('5 to 15%', ['Intermediate: segmentectomy,', 'VATS sympathectomy,', 'Nissen, Zenker'], 'b1'),
                  ('Over 15%', ['High: lobectomy (VATS or open),', 'pneumonectomy, oesophagectomy,', 'LVRS, transplant'], 'warn')], 120)


def f1_poaf_pathway():
    b = T(10, 22, 'Prevent (AATS 2014 class and level; ESC 2024 where marked)', 'f-h', 'start')
    rows = [('Continue a beta-blocker already taken', 'I A', 'ok'),
            ('Amiodarone after intermediate or high-risk lung resection', 'IIa A', 'ok'),
            ('Diltiazem if LV function preserved and not on a beta-blocker', 'IIa B', 'ok'),
            ('Magnesium if low or depleted', 'IIb C', 'b1'),
            ('Digoxin for prophylaxis: do not use', 'III A', 'warn'),
            ('ESC 2024: routine beta-blocker to prevent AF in non-cardiac surgery: do not use', 'III B', 'warn')]
    y = 32
    for txt, cl, c in rows:
        b += f'<rect x="10" y="{y}" width="700" height="28" rx="7" class="f-{c}"/>'
        b += T(22, y + 19, txt, '', 'start') + T(698, y + 19, cl, 'f-n', 'end')
        y += 33
    y += 18
    b += T(10, y, 'New AF after surgery', 'f-h', 'start')
    y += 10
    b += box(10, y, 340, 58, ['Unstable or ischaemic:', 'synchronised DC cardioversion', 'now (I C)'], 'warn')
    b += box(370, y, 340, 58, ['Stable: correct triggers (I C): bleeding,', 'PE, pneumothorax, sepsis, airway,', 'fluids, electrolytes, inotropes'], 'b0')
    b += arrow(540, y + 58, 540, y + 76)
    y += 78
    b += box(370, y, 165, 72, ['Rate control (IIa)', 'IV beta-blocker or', 'diltiazem, to 110 (I B)'], 'b1')
    b += box(545, y, 165, 72, ['Rhythm control if', 'recurrent, symptomatic', 'or uncontrolled (IIa)'], 'b1')
    y += 100
    b += T(10, y, 'Anticoagulate', 'f-h', 'start')
    y += 10
    b += box(10, y, 228, 66, ['Under 48 h: decide on', 'CHA2DS2-VASc against', 'bleeding risk (I C)'], 'b0')
    b += box(246, y, 228, 66, ['Over 48 h: anticoagulate (I A);', '3 weeks before and 4 after', 'elective cardioversion (I B)'], 'b0')
    b += box(482, y, 228, 66, ['ESC 2024: long-term OAC', 'should be considered if', 'stroke risk raised (IIa B)'], 'ok')
    return svg(y + 76, b)


# ---- figs_F2.py



def f2_dnc_sequence():
    """Diagnosis of death by neurological criteria, adults (AoMRC 2025)."""
    b = box(10, 10, 700, 78, ['1. Preconditions: known cause on imaging; no further useful treatment',
                              'Observe 6 h or more (primary brain injury) or 24 h or more (hypoxic injury, or after rewarming)',
                              'Core temperature 36 °C or more · no sedative or blocker effect (nerve stimulator)'], 'b1', 'f-s')
    b += arrow(360, 88, 360, 106)
    b += box(10, 108, 700, 40, 'Sodium 125 to 160 · potassium over 2.0 · magnesium and phosphate 0.5 to 3.0 · glucose 3.0 to 20.0 (mmol/L)', 'b1', 'f-s')
    b += arrow(360, 148, 360, 166)
    b += box(10, 168, 340, 106, ['2. First set (two doctors)', 'Six brainstem reflexes: pupils,', 'corneal, vestibulo-ocular, motor to', 'supraorbital pressure, gag, cough'], 'b0', 'f-s')
    b += arrow(350, 221, 370, 221)
    b += box(372, 168, 338, 106, ['3. Apnoea test (last test of the set)', 'Off the ventilator on CPAP, FiO2 1.0', 'At least 5 minutes, then arterial gas', 'PaCO2 8.0 kPa or more, rise 2.7, pH under 7.3'], 'b0', 'f-s')
    b += arrow(541, 274, 541, 292)
    b += box(372, 294, 338, 66, ['Recruit the lungs; restore gases', 'and baseline before the second set'], 'b1', 'f-s')
    b += arrow(372, 327, 352, 327)
    b += box(10, 294, 340, 66, ['4. Second set, roles reversed', '(family may watch)'], 'b0', 'f-s')
    b += arrow(180, 360, 180, 378)
    b += box(10, 380, 340, 52, ['Time of death: end of the', 'second set'], 'ok', 'f-h')
    b += box(372, 380, 338, 52, ['Ancillary test (CT angiography) if the', 'exam is incomplete or confounders persist'], 'warn', 'f-s')
    return svg(442, b)


def f2_apnoea():
    """Apnoea test thresholds, 2025 Code against 2008 Code."""
    b = T(12, 22, 'Apnoea test: what changed in the 2025 Code', 'f-h', 'start')
    b += line(40, 150, 690, 150, 'f-grid')
    b += T(40, 170, 'Ventilated', 'f-s', 'start') + T(690, 170, 'Arterial gas', 'f-s', 'end')
    b += '<path d="M40 120 L200 120 L620 62 L690 62" class="f-l" fill="none" style="stroke-width:3px"/>'
    b += line(200, 40, 200, 150, 'f-dash') + T(206, 50, 'Disconnect: CPAP circuit, FiO2 1.0', 'f-s', 'start')
    b += line(620, 40, 620, 150, 'f-dash') + T(614, 140, '5 minutes or more', 'f-s', 'end')
    b += T(430, 76, 'PaCO2 rising', 'f-s')
    b += box(10, 190, 226, 70, ['Start PaCO2', '5.3 kPa or more', '(2008: 6.0, pH under 7.4)'], 'b0', 'f-s')
    b += box(247, 190, 226, 70, ['End PaCO2', '8.0 kPa or more, pH under 7.3', '(2008: no end value)'], 'b0', 'f-s')
    b += box(484, 190, 226, 70, ['Rise in PaCO2', '2.7 kPa or more', '(2008: 0.5 kPa)'], 'warn', 'f-s')
    b += box(10, 272, 700, 40, 'Abort for breathing effort, instability despite drugs, desaturation on FiO2 1.0 and CPAP, or unstable arrhythmia', 'b1', 'f-s')
    return svg(322, b)


def f2_donor_targets():
    """NHSBT adult DBD donor optimisation care bundle."""
    b = T(12, 20, 'NHSBT donor optimisation bundle (death by neurological criteria)', 'f-h', 'start')
    steps = [('Immediately', ['Recruitment manoeuvre', 'Tidal volume 4 to 8 ml/kg,', 'PEEP 5 to 10 cmH2O', 'Vasopressin 0.48 to 4 U/h,', 'wean noradrenaline']),
             ('Within 1 hour', ['Methylprednisolone', '15 mg/kg (max 1 g)', 'Request ECG, echo,', 'chest film']),
             ('Within 4 hours', ['ECG, echo and', 'film reported', 'Cardiac output', 'monitoring if able'])]
    for i, (h, ls) in enumerate(steps):
        x = 10 + i * 236
        b += f'<rect x="{x}" y="32" width="226" height="130" rx="10" class="f-b0"/><rect x="{x}" y="32" width="226" height="30" rx="10" class="f-b1"/>'
        b += T(x + 113, 52, h, 'f-h') + T(x + 113, 82, ls, 'f-s')
        if i < 2:
            b += arrow(x + 226, 97, x + 236, 97)
    tg = [('60 to 80', 'MAP, mmHg'), ('over 2.1', 'Cardiac index'), ('0.5 to 2', 'Urine, ml/kg/h'),
          ('10 kPa or more', 'PaO2 (FiO2 under 0.4)'), ('5 to 6.5 kPa', 'PaCO2 (pH over 7.25)'),
          ('under 150', 'Sodium, mmol/L'), ('4 to 10', 'Glucose, mmol/L'), ('36 to 37.5 °C', 'Temperature')]
    for i, (big, small) in enumerate(tg):
        x = 10 + (i % 4) * 177
        y = 176 + (i // 4) * 74
        b += f'<rect x="{x}" y="{y}" width="168" height="64" rx="9" class="f-ok"/>'
        b += T(x + 84, y + 28, big, 'f-h') + T(x + 84, y + 48, small, 'f-s')
    b += T(360, 340, 'Desmopressin 1 to 4 micrograms IV for diabetes insipidus · 30 to 45° head up', 'f-s')
    return svg(352, b)


def f2_uk_allocation():
    """NHSBT heart allocation tiers (POL228/13, POL229/12)."""
    rows = [('Super-urgent (SUHAS)', ['Cat 11: temporary VAD or VA-ECMO', 'Cat 12: balloon pump or exceptional', '(adjudication panel)'],
             ['Named patient, national', 'Local zonal centre first, then by', 'time on super-urgent list'], 'warn'),
            ('Urgent (UHAS)', ['Cat 21: inpatient on inotropes or balloon,', 'index under 2.0, plus shock, organ', 'injury or high PVR · 22: LVAD problems'],
             ['Named patient, national', 'Ranked by blood group, then zone,', 'then time on urgent list'], 'b1'),
            ('Non-urgent (NUHAS)', ['Two or more: class III to IV, peak', 'VO2 under 14, NT-proBNP over 1600,', 'index under 2, repeated admissions'],
             ['Offered to a centre', 'Local zone, then adult centre rota;', 'DCD hearts offered here'], 'b0')]
    b = T(150, 20, 'Tier', 'f-h') + T(340, 20, 'Who qualifies', 'f-h') + T(605, 20, 'How the heart is offered', 'f-h')
    for i, (t, q, o, c) in enumerate(rows):
        y = 32 + i * 96
        b += box(10, y, 170, 84, t, c, 'f-h')
        b += box(190, y, 300, 84, q, 'b1', 'f-s')
        b += box(500, y, 210, 84, o, 'b0', 'f-s')
        b += arrow(180, y + 42, 189, y + 42) + arrow(490, y + 42, 499, y + 42)
        if i < 2:
            b += arrow(95, y + 84, 95, y + 95)
    b += T(360, 336, 'A heart moves down only after every patient above has declined. Fast-track: 45 minutes to respond.', 'f-s')
    return svg(348, b)


def f2_pgd():
    """ISHLT 2014 primary graft dysfunction grading."""
    b = T(12, 20, 'Primary graft dysfunction: within 24 hours, no secondary cause', 'f-h', 'start')
    b += box(10, 32, 700, 50, ['Dysfunction: LVEF 40% or less, or RAP over 15 and PCWP over 20 with index under 2.0', '(or mean pressure under 70 mmHg) for over 1 hour'], 'b1', 'f-s')
    spec = [('Mild PGD-LV', ['Dysfunction plus', 'inotrope score', 'under 10'], 'ok'),
            ('Moderate PGD-LV', ['Dysfunction plus', 'inotrope score over 10,', 'or a new balloon pump'], 'b0'),
            ('Severe PGD-LV', ['Needs ECMO, LVAD,', 'BiVAD or percutaneous', 'LVAD (not balloon alone)'], 'warn'),
            ('PGD-RV', ['RAP over 15, PCWP', 'under 15, index under 2.0;', 'TPG under 15 or PASP', 'under 50; or an RVAD'], 'b1')]
    for i, (h, ls, c) in enumerate(spec):
        x = 10 + i * 177
        b += arrow(x + 84, 82, x + 84, 98)
        b += f'<rect x="{x}" y="100" width="168" height="112" rx="10" class="f-{c}"/>'
        b += T(x + 84, 124, h, 'f-h') + T(x + 84, 152, ls, 'f-s')
    b += T(360, 236, 'Inotrope score = dopamine + dobutamine + amrinone + 15 × milrinone + 100 × (adrenaline + noradrenaline), µg/kg/min', 'f-s')
    return svg(248, b)


def f2_cpet():
    """ISHLT 2016 CPET listing thresholds."""
    return tiles([('12 or less', ['Peak VO2, ml/kg/min,', 'on a beta-blocker'], 'warn'),
                  ('14 or less', ['Peak VO2 if', 'beta-blocker intolerant'], 'warn'),
                  ('50% or less', ['Of predicted: under 50s', 'and women (IIa)'], 'b1'),
                  ('35 or more', ['VE/VCO2 slope if', 'RER under 1.05 (IIb)'], 'b1')], 104)


# ---- figs_F3.py



def _f3_card(x, y, w, h, head, lines, hcls='b1', bcls='b0', lh=17, top=58):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="f-{bcls}"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="10" class="f-{hcls}"/>'
    if isinstance(head, str):
        head = [head]
    out += T(x + w / 2, y + 22, head[0], 'f-h')
    out += T(x + w / 2, y + top, lines, 'f-s')
    return out


def f3_risk_tiers():
    """ISHLT 2021 three-tier contraindication scheme with the main thresholds."""
    cols = [
        ('Absolute contraindication', 'warn', [
            'GFR under 40 (unless multi-organ)', 'ACS, MI or stroke in 30 days',
            'Cirrhosis with portal hypertension', 'Septic shock; active TB',
            'HIV with detectable viral load', 'Active smoking, vaping, drugs',
            'Cancer with high recurrence risk', 'Non-ambulant, poor rehab outlook',
            'Repeated non-adherence']),
        ('Substantially increased', 'b1', [
            'Age over 70', 'BMI over 35 or under 16', 'LVEF under 40%',
            'CABG needed at transplant', 'M. abscessus, B. cenocepacia,',
            'B. gladioli, L. prolificans', 'On ECLS (ECMO bridge)',
            'Retransplant within 1 year,', 'or for RAS or AMR-type CLAD']),
        ('Increased risk', 'b1', [
            'Age 65 to 70', 'BMI 30 to 34.9 or 16 to 17', 'GFR 40 to 60; LVEF 40 to 50%',
            'Prior CABG; PCI-treatable CAD', 'Frailty; osteoporosis',
            'Connective tissue disease, GORD', 'Prior thoracic surgery',
            'or pleurodesis', 'Mechanical ventilation']),
    ]
    b = ''
    for i, (head, hc, ls) in enumerate(cols):
        x = 10 + i * 236
        b += _f3_card(x, 10, 226, 210, head, ls, hc)
    b += box(10, 232, 700, 40, 'Several risk factors together may multiply risk: judge the whole patient', 'ok', 'f-s')
    return svg(282, b)


def f3_referral_listing():
    """Referral and listing triggers by disease, ISHLT 2021."""
    rows = [
        ('COPD',
         ['BODE 5 to 6 plus one of: frequent', 'exacerbations, BODE up over 1 in 2 years,', 'PA:aorta over 1 on CT, FEV1 20 to 25%'],
         ['BODE 7 to 10; supporting: FEV1 under', '20%, moderate to severe PH, severe', 'exacerbations, chronic hypercapnia']),
        ('Fibrotic ILD',
         ['FVC under 80% or DLCO under 40%; or', 'in 2 years FVC fall 10% or DLCO fall 15%', '(relative); any oxygen need'],
         ['In 6 months: FVC or DLCO down over 10%', '(absolute), walk SpO2 under 88% or 50 m', 'lost; PH; admission for decline']),
        ('Cystic fibrosis',
         ['FEV1 under 30%; or under 40% with walk', 'under 400 m, PaCO2 over 50, hypoxaemia,', 'PH, haemoptysis, pneumothorax'],
         ['A referral criterion plus: FEV1 under', '25%, 30% fall in 12 months, over 28 days', 'in hospital, ventilation, PH, BMI under 18']),
        ('PAH',
         ['NYHA III to IV on escalating therapy;', 'ESC/ERS intermediate or high risk;', 'parenteral therapy needed; PVOD or PCH'],
         ['III to IV after 3 months of combination', 'therapy with a prostanoid; CI under 2;', 'RAP over 15; walk under 350 m']),
    ]
    b = T(178 + 140, 24, 'Refer for assessment', 'f-h') + T(468 + 121, 24, 'List for transplant', 'f-h')
    y = 36
    for lab, ref, lst in rows:
        b += box(10, y, 112, 74, lab.split(' ', 1) if ' ' in lab else lab, 'b1', 'f-h')
        b += f'<rect x="130" y="{y}" width="290" height="74" rx="9" class="f-b0"/>' + T(275, y + 21, ref, 'f-s')
        b += arrow(421, y + 37, 434, y + 37)
        b += f'<rect x="436" y="{y}" width="274" height="74" rx="9" class="f-warn"/>' + T(573, y + 21, lst, 'f-s')
        y += 82
    b += T(360, y + 14, 'Refer early, before listing criteria are met, so that barriers such as weight can be fixed.', 'f-s')
    return svg(y + 26, b)


def f3_pgd_grading():
    """ISHLT 2016 PGD grades and time points."""
    spec = [('Grade 0', ['No diffuse oedema', 'on the film,', 'any P/F ratio'], 'ok'),
            ('Grade 1', ['Oedema on film', 'P/F over 300'], 'b0'),
            ('Grade 2', ['Oedema on film', 'P/F 200 to 300'], 'b1'),
            ('Grade 3', ['Oedema on film', 'P/F under 200, or ECMO', 'for hypoxaemia'], 'warn')]
    b = ''
    for i, (g, ls, c) in enumerate(spec):
        x = 10 + i * 177
        b += f'<rect x="{x}" y="10" width="168" height="104" rx="10" class="f-{c}"/>'
        b += T(x + 84, 34, g, 'f-h') + T(x + 84, 60, ls, 'f-s')
    b += line(40, 160, 680, 160)
    for i, (lab, sub) in enumerate([('T0', ['within 6 h of', 'second reperfusion']), ('T24', '± 6 h'), ('T48', '± 6 h'), ('T72', '± 6 h')]):
        x = 60 + i * 200
        b += f'<circle cx="{x}" cy="160" r="15" class="f-b1"/>' + T(x, 165, lab, 'f-s')
        b += T(x + (6 if i == 0 else 0), 194, sub, 'f-s')
    b += T(360, 138, 'Grade at four time points; use the worst P/F of that day (ideally PEEP 5, FiO2 1.0)', 'f-s')
    b += box(10, 222, 226, 62, ['Inhaled NO or epoprostenol:', 'grade as if not given;', 'record separately'], 'b0', 'f-s')
    b += box(247, 222, 226, 62, ['ECMO for RV failure with', 'no oedema on the film:', '"ungradable"'], 'b0', 'f-s')
    b += box(484, 222, 226, 62, ['No arterial gas: use SpO2/FiO2', 'with cut-offs 235 and 315;', 'FiO2 under 0.4 is never grade 3'], 'b0', 'f-s')
    return svg(294, b)


def f3_uk_allocation():
    """NHSBT lung allocation tiers (POL230 v15.1, POL231 v8)."""
    b = ''
    spec = [('Super-urgent (SULAS)', ['On VV-ECMO or iLA as a bridge,', 'already on the list; not on', 'IPPV; free of sepsis and', 'other organ failure'],
             ['Named patient, national;', 'order: time on SU list'], 'warn'),
            ('Urgent (ULAS)', ['Expected survival under 90 days', 'and a disease category:', 'COPD, CF, IPF or PAH', '(gas, pH, RHC criteria)'],
             ['Named patient, national;', 'identical ABO first, then', 'time on urgent list'], 'b1'),
            ('Non-urgent (NULAS)', ['Maximal therapy; expected', 'survival after transplant', 'over 5 years; a disease', 'criterion met'],
             ['Centre offer: zonal centre', 'first, then the adult lung', 'centre rota; centre picks'], 'b0')]
    for i, (head, crit, offer, c) in enumerate(spec):
        x = 10 + i * 236
        b += f'<rect x="{x}" y="10" width="226" height="200" rx="10" class="f-b0"/>'
        b += f'<rect x="{x}" y="10" width="226" height="34" rx="10" class="f-{c}"/>'
        b += T(x + 113, 32, head, 'f-h')
        b += T(x + 113, 66, crit, 'f-s')
        b += line(x + 16, 140, x + 210, 140, 'f-grid')
        b += T(x + 113, 162, offer, 'f-s')
        if i < 2:
            b += arrow(x + 227, 110, x + 235, 110)
    b += box(10, 222, 345, 58, ['Paediatric donor lungs go to children first;', 'small adults (155 cm or less) next'], 'ok', 'f-s')
    b += box(365, 222, 345, 58, ['ABO-incompatible patients get no SU or U offer;', 'donor height limits set per patient'], 'ok', 'f-s')
    return svg(290, b)


def f3_clad_stages():
    """CLAD stages by current FEV1 as % of baseline."""
    x0, x1 = 60, 680
    sc = (x1 - x0) / 100
    b = T(12, 22, 'CLAD stage by current FEV1 as % of baseline', 'f-h', 'start')
    segs = [(0, 35, 'CLAD 4', 'under 35%', 'warn'), (35, 51, 'CLAD 3', '35 to 50%', 'warn'),
            (51, 66, 'CLAD 2', '51 to 65%', 'b1'), (66, 81, 'CLAD 1', '66 to 80%', 'b1'),
            (81, 100, 'CLAD 0', 'over 80%', 'ok')]
    for lo, hi, lab, rng, c in segs:
        xa, xb = x0 + lo * sc, x0 + hi * sc
        b += f'<rect x="{xa + 1}" y="44" width="{xb - xa - 2}" height="54" rx="6" class="f-{c}"/>'
        b += T((xa + xb) / 2, 66, lab, 'f-h') + T((xa + xb) / 2, 86, rng, 'f-s')
    for v in (0, 20, 40, 60, 80, 100):
        b += line(x0 + v * sc, 102, x0 + v * sc, 110) + T(x0 + v * sc, 126, f'{v}%', 'f-s')
    b += T(360, 152, 'Baseline: mean of the two best post-transplant FEV1 values, more than 3 weeks apart', 'f-s')
    b += box(10, 166, 345, 70, ['BOS: FEV1 down 20% or more,', 'FEV1/FVC under 0.7, TLC kept,', 'no opacities on CT'], 'b0', 'f-s')
    b += box(365, 166, 345, 70, ['RAS: FEV1 down 20% or more,', 'TLC 90% of baseline or less,', 'persistent opacities on imaging'], 'warn', 'f-s')
    return svg(246, b)


def f3_early_hypoxaemia():
    """What to exclude before calling early hypoxaemia PGD (ISHLT 2016 PGD statement, Table 3)."""
    spec = [('Airway', ['Blocked or misplaced tube;', 'bronchus plugged by', 'sputum or blood']),
            ('Vascular', ['Pulmonary arterial or', 'venous anastomotic', 'obstruction']),
            ('Cardiac', ['Acute LV dysfunction;', 'RV/LV dyssynchrony after', 'severe pulmonary hypertension']),
            ('Parenchymal', ['Infection, rejection,', 'aspiration, haemorrhage,', 'TRALI, SIRS']),
            ('Pleural', ['Haemothorax,', 'effusion,', 'pneumothorax']),
            ('Chest wall', ['Open chest'])]
    b = box(160, 6, 400, 36, 'Hypoxaemia and infiltrates in the first 72 hours', 'b1', 'f-h')
    for i, (h, ls) in enumerate(spec):
        x = 10 + (i % 3) * 236
        y = 56 + (i // 3) * 118
        b += _f3_card(x, y, 226, 106, h, ls, 'warn', top=56)
    b += box(10, 296, 700, 38, 'If none applies and the film shows diffuse oedema: grade as PGD', 'ok', 'f-s')
    return svg(344, b)


# ---- figs_F4.py



def f4_pacing_systems():
    """Two pacing systems: thoracic phrenic nerve electrodes and laparoscopic intramuscular electrodes."""
    b = T(180, 22, 'A. Phrenic nerve pacing (thoracic)', 'f-h') + T(540, 22, 'B. Intramuscular diaphragm pacing', 'f-h')
    b += line(360, 34, 360, 360, 'f-grid')
    # Panel A: chest outline, heart, phrenic nerves, electrodes, receivers
    b += '<path d="M40 330 L40 120 C40 60 100 44 180 44 C260 44 320 60 320 120 L320 330" class="f-l"/>'
    b += '<path d="M44 300 C100 262 150 262 180 280 C210 262 260 262 316 300" class="f-l"/>'
    b += '<ellipse cx="186" cy="214" rx="54" ry="48" class="f-b1"/>' + T(186, 218, 'Heart', 'f-s')
    b += '<path d="M150 50 C140 110 124 170 128 220 C130 250 124 270 120 282" class="f-nerve"/>'
    b += '<path d="M212 50 C222 110 246 170 244 220 C242 250 248 270 252 282" class="f-nerve"/>'
    for cx, cy in [(134, 150), (232, 150)]:
        b += f'<rect x="{cx - 9}" y="{cy - 6}" width="18" height="12" rx="3" class="f-warn"/>'
    b += '<rect x="64" y="96" width="34" height="22" rx="5" class="f-b0"/><rect x="266" y="96" width="34" height="22" rx="5" class="f-b0"/>'
    b += '<path d="M125 150 C110 146 90 134 81 118" class="f-dash"/><path d="M241 150 C256 146 276 134 283 118" class="f-dash"/>'
    b += T(81, 90, 'Receiver', 'f-s') + T(283, 90, 'Receiver', 'f-s') + T(134, 174, 'Electrode', 'f-s', 'end')
    b += T(180, 300, 'Diaphragm', 'f-s')
    b += box(20, 312, 320, 44, ['Electrode on each phrenic nerve, mid-mediastinum;', 'receiver under the skin, external antenna'], 'b0', 'f-s')
    # Panel B: diaphragm seen from below, motor points, hook electrodes, external stimulator
    b += '<path d="M390 230 C390 120 470 90 540 110 C610 90 690 120 690 230 Z" class="f-b0"/>'
    b += T(540, 132, 'Abdominal surface of diaphragm', 'f-s')
    b += '<path d="M540 230 L540 175" class="f-l"/>'
    for cx, cy in [(480, 186), (600, 186)]:
        b += f'<circle cx="{cx}" cy="{cy}" r="6" class="f-warn"/>'
    b += T(480, 172, 'Motor point', 'f-s') + T(600, 172, 'Motor point', 'f-s')
    b += '<path d="M480 186 C480 240 520 270 540 290 M600 186 C600 240 560 270 540 290" class="f-dash"/>'
    b += '<rect x="500" y="288" width="80" height="22" rx="5" class="f-b1"/>' + T(540, 303, 'Stimulator', 'f-s')
    b += T(420, 222, 'Right', 'f-s') + T(660, 222, 'Left', 'f-s')
    b += box(380, 312, 320, 44, ['Laparoscopic hook electrode at the mapped motor', 'point of each side; wires exit to a 4-channel stimulator'], 'b0', 'f-s')
    return svg(368, b)


def f4_pacing_selection():
    """Candidate selection pathway for diaphragm pacing."""
    b = box(210, 10, 300, 42, ['Ventilator-dependent', 'chronic respiratory failure'], 'b1', 'f-h')
    b += arrow(300, 52, 150, 80) + arrow(360, 52, 360, 80) + arrow(420, 52, 590, 80)
    b += box(10, 82, 270, 56, ['High cervical cord injury (C2 or above)', 'or central hypoventilation'], 'b0')
    b += box(290, 82, 160, 56, ['C3 to C5 injury with', 'phrenic loss'], 'warn')
    b += box(460, 82, 250, 56, ['Motor neurone disease', '(ALS)'], 'warn')
    b += arrow(145, 138, 145, 164)
    b += box(10, 166, 270, 74, ['Test both phrenic nerves: conduction', 'study and fluoroscopy or ultrasound;', 'descent about 4 cm on stimulation'], 'b0')
    b += arrow(370, 138, 370, 164)
    b += box(290, 166, 160, 74, ['Not a pacing', 'candidate; consider', 'nerve transfer'], 'b1')
    b += arrow(585, 138, 585, 164)
    b += box(460, 166, 250, 74, ['Do not use (NICE IPG593):', 'shorter survival in DiPALS', 'and RespiStimALS'], 'warn', 'f-h')
    b += arrow(145, 240, 145, 266)
    b += box(10, 268, 270, 74, ['Both intact and diaphragm contracts:', 'wait for neurological stability', '(about 12 months after injury)'], 'ok')
    b += arrow(280, 305, 300, 305)
    b += box(302, 268, 408, 74, ['MDT with spinal injury and home ventilation experience', 'selects; NICE IPG762: special arrangements,', 'audit every patient'], 'b0')
    return svg(352, b)


def f4_als_trials():
    """Charts of the two ALS pacing trials."""
    h1, b1 = bars([('NIV alone (DiPALS)', 22.5, 'b1'), ('NIV plus pacing (DiPALS)', 11.0, 'warn')], ' months', 25,
                  'DiPALS: pacing halved median survival (HR 2.27)')
    h2, b2 = bars([('Sham stimulation', 8.8, 'b1'), ('Active pacing', 6.0, 'warn')], ' months', 25,
                  'RespiStimALS: pacing shortened median NIV-free survival (HR 1.96)')
    b = b1 + f'<g transform="translate(0 {h1})">{b2}</g>'
    return svg(h1 + h2, b)


def f4_diaphragm_supply():
    """Diaphragm from below (anterior at top, patient's right on the viewer's left)."""
    b = '<path d="M60 260 C60 120 200 50 360 60 C520 50 660 120 660 260 Z" class="f-b0"/>'
    b += '<path d="M270 150 C300 112 420 112 450 150 C440 190 400 200 360 182 C320 200 280 190 270 150 Z" class="f-b1"/>'
    b += T(360, 146, 'Central tendon', 'f-s')
    b += '<circle cx="300" cy="170" r="12" class="f-lumen"/>' + T(300, 200, 'IVC', 'f-s')
    b += '<ellipse cx="384" cy="212" rx="11" ry="14" class="f-lumen"/>' + T(402, 212, 'Oesophagus', 'f-s', 'start')
    b += '<circle cx="360" cy="252" r="12" class="f-lumen"/>' + T(360, 286, 'Aorta', 'f-s')
    b += '<circle cx="300" cy="170" r="4" class="f-warn"/><circle cx="490" cy="140" r="5" class="f-warn"/>'
    for (x, y) in [(160, 110), (90, 190), (160, 250), (250, 255)]:
        b += f'<path d="M296 168 Q{(296 + x) / 2} {(168 + y) / 2 - 18} {x} {y}" class="f-nerve"/>'
    for (x, y) in [(570, 100), (630, 190), (570, 250), (470, 255)]:
        b += f'<path d="M490 140 Q{(490 + x) / 2} {(140 + y) / 2 - 18} {x} {y}" class="f-nerve"/>'
    b += '<path d="M352 248 C300 236 250 226 180 214" class="f-vessel" style="stroke-width:4"/>'
    b += '<path d="M368 248 C420 232 470 216 540 204" class="f-vessel" style="stroke-width:4"/>'
    b += T(12, 22, 'Seen from below: anterior at top, patient\'s right on the left', 'f-h', 'start')
    b += T(84, 290, 'Right', 'f-s', 'start') + T(636, 290, 'Left', 'f-s', 'end')
    b += T(150, 62, 'Right phrenic enters via caval opening', 'f-s')
    b += T(590, 62, 'Left phrenic pierces the dome', 'f-s')
    b += T(205, 272, 'Inferior phrenic artery', 'f-s')
    b += box(10, 304, 345, 62, ['Phrenic (C3 to C5): sole motor supply;', 'branches radiate on the inferior surface'], 'b0', 'f-s')
    b += box(365, 304, 345, 62, ['Inferior phrenic arteries (aorta) on the', 'abdominal surface; margins from lower', 'intercostal, subcostal, musculophrenic'], 'b1', 'f-s')
    return svg(376, b)


def f4_diaphragm_patch():
    """Fixation of a prosthetic patch after total hemidiaphragm resection."""
    b = T(360, 22, 'Prosthetic hemidiaphragm: where to anchor the patch', 'f-h')
    b += '<path d="M60 250 C120 150 600 150 660 250" class="f-dash"/>'
    b += T(64, 196, 'Native dome', 'f-s', 'start')
    b += '<path d="M90 270 C160 200 560 200 630 270 Z" class="f-ok"/>'
    b += T(360, 246, 'Patch (PTFE most used; set low and taut)', 'f-s')
    b += '<rect x="560" y="268" width="80" height="16" rx="4" class="f-b1"/>' + T(600, 300, 'Ribs: lateral', 'f-s')
    b += '<rect x="70" y="268" width="70" height="16" rx="4" class="f-b1"/>' + T(105, 300, 'Pericardium: medial', 'f-s')
    b += '<rect x="320" y="270" width="80" height="16" rx="4" class="f-b1"/>' + T(360, 300, 'Crus: posterior', 'f-s')
    b += box(10, 56, 340, 92, ['Left side', 'Dehiscence and hernia are the main risk', '(5 to 7.6%); keep a 1 to 2 cm crural rim;', 'or anchor to a titanium L-plate (T9 to T10)'], 'warn', 'f-s')
    b += box(370, 56, 340, 92, ['Right side', 'Liver supports the patch, hernia rare;', 'cut a notch for the IVC so the cava and', 'hepatic veins are not compressed'], 'b0', 'f-s')
    b += box(10, 314, 700, 44, ['Level: 10th intercostal space posteriorly, 8th to 9th anteriorly and laterally (Solli 2017)'], 'b1', 'f-s')
    return svg(368, b)


def f4_chest_wall_algorithm():
    """Chest wall reconstruction decision after resection, from TSRA ch. 27."""
    b = box(210, 10, 300, 40, 'Full-thickness chest wall defect', 'b1', 'f-h')
    b += arrow(300, 50, 170, 78) + arrow(420, 50, 550, 78)
    b += box(10, 80, 330, 60, ['Under 5 cm, or covered by the scapula'], 'ok')
    b += box(380, 80, 330, 60, ['Over 5 cm, 4 or more ribs,', 'or sternum involved'], 'warn')
    b += arrow(175, 140, 175, 166) + arrow(545, 140, 545, 166)
    b += box(10, 168, 330, 60, ['Local tissue advancement only', '(no skeletal reconstruction)'], 'ok')
    b += box(380, 168, 330, 74, ['Skeletal: synthetic mesh on heavy', 'non-absorbable sutures, metal struts', 'if needed; no synthetic if contaminated'], 'b0')
    b += arrow(545, 242, 545, 266)
    b += box(380, 268, 330, 74, ['Soft tissue: latissimus dorsi,', 'pectoralis major or rectus abdominis', 'flap, especially if irradiated'], 'b0')
    b += box(10, 250, 330, 92, ['Why reconstruct: stability, chest wall', 'mechanics, avoid contraction and', 'scapular entrapment, protect the', 'mediastinum, stop lung herniation'], 'b1', 'f-s')
    return svg(352, b)


# ---- figs_F5.py



def f5_pericardiocentesis():
    """Subxiphoid pericardiocentesis, schematic sagittal view, with the alternative routes."""
    b = T(12, 22, 'Pericardiocentesis: routes and drain rules (ESC 2025, section 6.3.2.1)', 'f-h', 'start')
    # sagittal schematic: sternum, xiphoid, heart in pericardial sac, diaphragm, liver
    b += '<path d="M150 60 L170 230" class="f-l" style="stroke-width:9;stroke-linecap:round"/>'
    b += T(128, 120, 'Sternum', 'f-s', 'end')
    b += '<path d="M170 230 L184 262" class="f-l" style="stroke-width:5;stroke-linecap:round"/>'
    b += T(160, 278, 'Xiphoid', 'f-s', 'end')
    # pericardial sac (effusion) and heart
    b += '<ellipse cx="290" cy="170" rx="120" ry="88" class="f-track"/>'
    b += '<ellipse cx="295" cy="165" rx="86" ry="60" class="f-b0"/>'
    b += T(295, 162, 'Heart', 'f-h') + T(295, 180, '(right ventricle lies', 'f-s') + T(295, 195, 'next to the needle)', 'f-s')
    b += T(395, 92, 'Effusion', 'f-s', 'start')
    # diaphragm and liver
    b += '<path d="M120 300 C200 262 340 262 470 300" class="f-l"/>'
    b += T(114, 304, 'Diaphragm', 'f-s', 'end')
    b += '<path d="M205 306 C260 290 350 292 430 318 L430 340 L205 340 Z" class="f-b1"/>'
    b += T(320, 332, 'Liver', 'f-s')
    # needle from subxiphoid region into inferior sac
    b += '<line x1="196" y1="300" x2="236" y2="240" class="f-cut" style="stroke-width:3"/>'
    b += '<circle cx="236" cy="240" r="4" class="f-b1"/>'
    b += T(184, 330, 'Subxiphoid entry (usual)', 'f-h', 'end')
    # alternative apical / left lateral marker
    b += arrow(470, 210, 404, 196)
    b += T(476, 206, ['Apical or left lateral', 'route: alternative'], 'f-s', 'start')
    # rule boxes
    b += box(520, 40, 190, 70, ['Guidance: echo,', 'CT or fluoroscopy', 'needle 16 to 20 G'], 'b0', 'f-s')
    b += box(520, 230, 190, 86, ['First drainage usually', 'under 500 ml (avoid', 'decompression syndrome)', 'Remove at under 30 ml/day'], 'ok', 'f-s')
    b += box(10, 356, 700, 44, ['Complications 4 to 10% depending on monitoring. While waiting: avoid positive-pressure',
                                'ventilation and diuretics; fluids may help for a short time (ESC 2025, section 11.8.3)'], 'warn', 'f-s')
    return svg(410, b)


def f5_triage():
    """ESC 2025 Figure 12 triage score, laid out as three columns."""
    b = T(12, 22, 'Urgent pericardiocentesis triage score (ESC 2025, Figure 12)', 'f-h', 'start')
    cols = [
        ('Aetiology', [('Malignant disease', '2'), ('Tuberculosis', '2'), ('Recent radiotherapy', '1'),
                       ('Recent viral infection', '1'), ('Recurrent effusion', '1'), ('Terminal renal failure', '1'),
                       ('Immunosuppression', '1'), ('Dysthyroidism', '-1'), ('Systemic autoimmune', '-1')]),
        ('Clinical', [('Orthopnoea', '3'), ('Pulsus paradoxus >10', '2'), ('Rapid worsening', '2'),
                      ('Dyspnoea, tachypnoea', '1'), ('Rising sinus rate', '1'), ('Oliguria', '1'),
                      ('Central BP <95 mmHg', '0.5'), ('Pericardial pain', '0.5'), ('Friction rub', '0.5'),
                      ('Slow evolution', '-1')]),
        ('Imaging', [('Circumferential large', '3'), ('Left atrial collapse', '2'), ('IVC dilated, fixed', '1.5'),
                     ('RV collapse', '1.5'), ('Cardiomegaly on film', '1'), ('Low QRS voltage', '1'),
                     ('Moderate effusion', '1'), ('RA collapse', '1'), ('Flow variation', '1'),
                     ('Swinging heart', '1'), ('Electrical alternans', '0.5'), ('Small effusion', '-1')]),
    ]
    for i, (head, items) in enumerate(cols):
        x = 10 + i * 238
        b += f'<rect x="{x}" y="38" width="226" height="{34 + len(items) * 21}" rx="9" class="f-b1"/>'
        b += T(x + 113, 60, head, 'f-h')
        for j, (lab, pts) in enumerate(items):
            y = 84 + j * 21
            b += T(x + 12, y, lab, 'f-s', 'start')
            cls = 'f-n'
            b += T(x + 214, y, pts, cls, 'end')
    b += box(10, 336, 700, 44, ['Immediate drainage to be considered at a total over 6 from at least two categories;',
                                'lower scores: drainage may be deferred (expert consensus, not validated)'], 'warn', 'f-s')
    return svg(390, b)


def f5_routes():
    """Choice of drainage route, from ESC 2025 recommendation tables and TSRA ch. 86."""
    b = T(12, 22, 'Which drainage? (ESC 2025 Tables 12, 21, 23; TSRA ch. 86)', 'f-h', 'start')
    b += box(250, 36, 220, 44, ['Tamponade or symptomatic', 'effusion needing drainage'], 'b1', 'f-h')
    b += arrow(300, 80, 110, 110) + arrow(340, 80, 290, 110) + arrow(380, 80, 430, 110) + arrow(420, 80, 610, 110)
    b += box(10, 112, 170, 92, ['Free, accessible', 'fluid', 'Needle drainage,', 'imaging-guided', '(I C)'], 'ok', 'f-s')
    b += box(190, 112, 170, 92, ['Purulent, clotted, or', 'not reachable by', 'needle', 'Surgical drainage', '(I C)'], 'b0', 'f-s')
    b += box(370, 112, 170, 92, ['Relapsing despite', 'medical treatment', '', 'Pleuro-pericardial', 'window (I C)'], 'b0', 'f-s')
    b += box(550, 112, 160, 92, ['Early after', 'cardiac surgery', '', 'Re-sternotomy', '(TSRA)'], 'warn', 'f-s')
    b += box(10, 222, 345, 80, ['Malignant: needle drainage with drain', 'left 3 to 6 days (I B); fluid cytology (I C);',
                                'systemic treatment; no talc (reduced efficacy', 'against window or pericardiectomy)'], 'b1', 'f-s')
    b += box(365, 222, 345, 80, ['Purulent: urgent needle drainage and/or', 'surgical window (I C); intrapericardial',
                                 'fibrinolysis to be considered (IIa B)', 'to drain fully and prevent constriction'], 'b1', 'f-s')
    b += box(10, 318, 700, 44, ['Balloon pericardiotomy: not first or second line; rare cases (recurrent malignant effusion,',
                                'no surgical option, terminal illness). Window may open to left pleura or, in selected cases, peritoneum'], 'track', 'f-s')
    return svg(372, b)


def f5_constrictive():
    """ESC 2025 Table 18: three constrictive syndromes and their treatment."""
    b = T(12, 22, 'Constrictive syndromes and their treatment (ESC 2025, Table 18)', 'f-h', 'start')
    b += line(40, 64, 690, 64) + line(40, 58, 40, 70) + line(360, 58, 360, 70) + line(690, 58, 690, 70)
    b += T(40, 52, 'Diagnosis', 'f-s') + T(360, 52, '3 to 6 months', 'f-s') + T(686, 52, 'Later', 'f-s', 'end')
    spec = [('Transient', ['Reversible: settles', 'spontaneously or with', 'anti-inflammatory drugs', '(10 to 20% of acute', 'pericarditis cases)'],
             ['3 to 6 months of', 'empirical anti-', 'inflammatory drugs'], 'ok'),
            ('Effusive-constrictive', ['Right atrial pressure', 'fails to fall by 50%', 'or below 10 mmHg', 'after pericardiocentesis'],
             ['Pericardiocentesis, then', 'medical treatment;', 'surgery (visceral', 'pericardiectomy) if', 'persistent'], 'b0'),
            ('Chronic', ['Constriction still', 'present after 3 to', '6 months'],
             ['Radical pericardiectomy;', 'medical treatment if', 'advanced or high', 'surgical risk'], 'warn')]
    for i, (h, d, tx, c) in enumerate(spec):
        x = 10 + i * 240
        b += box(x, 84, 220, 36, h, 'b1', 'f-h')
        b += box(x, 128, 220, 104, d, 'track', 'f-s')
        b += arrow(x + 110, 232, x + 110, 252)
        b += box(x, 254, 220, 100, tx, c, 'f-s')
    b += box(10, 368, 700, 44, ['Active inflammation (raised CRP, pericardial oedema or LGE on CMR) points to a trial of',
                                'anti-inflammatory treatment first (I C); permanent constriction without inflammation: pericardiectomy (I C)'], 'b1', 'f-s')
    return svg(422, b)


def f5_constriction_risk():
    """Risk of progression to constriction by aetiology and Mayo echo criteria performance."""
    out = T(12, 22, 'Bacterial pericarditis carries the highest risk of later constriction', 'f-h', 'start')
    lab_w, span = 250, W - 250 - 110
    rows = [('Bacterial (esp. purulent)', 20, 30, '20 to 30%', 'warn'),
            ('Immune-mediated or neoplastic', 2, 5, '2 to 5%', 'b0'),
            ('Viral or idiopathic', 0, 1, 'under 1%', 'ok')]
    y = 40
    for lab, lo, hi, txt, c in rows:
        out += T(lab_w - 10, y + 19, lab, '', 'end')
        out += f'<rect x="{lab_w}" y="{y + 4}" width="{span * hi / 30}" height="22" rx="4" class="f-track"/>'
        out += f'<rect x="{lab_w + span * lo / 30}" y="{y + 4}" width="{max(3, span * (hi - lo) / 30)}" height="22" rx="4" class="f-{c}"/>'
        out += T(lab_w + span * hi / 30 + 8, y + 20, txt, 'f-n', 'start')
        y += 34
    out += T(12, y + 12, 'Range bars from zero; ESC 2025, section 11.9. Treated tuberculosis: from over 80% to under 10%.', 'f-s', 'start')
    y += 40
    out += T(12, y + 4, 'Mayo echo criteria for constriction (ESC 2025, section 11.9.3)', 'f-h', 'start')
    y += 14
    h2, b2 = bars([('Sensitivity, criteria as defined', 87, 'b0'), ('Specificity, criteria as defined', 91, 'b0'),
                   ('Sensitivity, all criteria present', 64, 'warn'), ('Specificity, all criteria present', 97, 'ok')],
                  '%', 100, None, 250)
    out += f'<g transform="translate(0 {y - 18})">{b2}</g>'
    y += h2 - 18
    out += T(12, y + 8, 'Septal bounce or shift, plus medial e′ over 8 cm/s or hepatic vein expiratory', 'f-s', 'start')
    out += T(12, y + 25, 'diastolic reversal ratio over 0.78', 'f-s', 'start')
    return svg(y + 40, out)


# ---- figs_F6.py



def _f6_card(x, y, w, h, head, lines, hcls='b1', bcls='b0', tcls='f-s'):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="f-{bcls}"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="10" class="f-{hcls}"/>'
    out += T(x + w / 2, y + 21, head, 'f-h')
    out += T(x + w / 2, y + 54, lines, tcls)
    return out


def f6_noncardioplegic():
    """Four ways of operating without cardioplegia, compared."""
    cols = [('Intermittent clamp', 'and fibrillation'), ('Hypothermic', 'fibrillatory arrest'),
            ('On-pump', 'beating heart'), ('Off-pump', '(OPCAB)')]
    rows = [('Bypass', ['Yes', 'Yes', 'Yes', 'No']),
            ('Aortic clamp', ['Brief, one per distal', 'None (side clamp', 'None', 'None (side clamp']),
            ('', ['', 'for proximals)', '', 'or clampless)']),
            ('Heart', ['Fibrillating, empty', 'Fibrillating, vented', 'Beating, empty', 'Beating, ejecting']),
            ('Temperature', ['32 to 33°C', '28 to 32°C', 'Varies', 'Normal']),
            ('Protection by', ['Short ischaemia,', 'Continuous coronary', 'Continuous coronary', 'Regional ischaemia']),
            ('', ['cooling, empty heart', 'perfusion, cooling', 'perfusion, no work', 'only; shunts'])]
    lw = 118
    cw = (W - 10 - lw) / 4
    b = ''
    for i, (a, c) in enumerate(cols):
        x = lw + i * cw
        b += f'<rect x="{x + 3}" y="8" width="{cw - 6}" height="46" rx="9" class="f-b1"/>'
        b += T(x + cw / 2, 27, a, 'f-h') + T(x + cw / 2, 44, c, 'f-s')
    y = 62
    for lab, vals in rows:
        if lab:
            b += line(10, y, W - 10, y, 'f-grid')
            y += 4
        b += T(12, y + 16, lab, 'f-h', 'start')
        for i, v in enumerate(vals):
            b += T(lw + i * cw + cw / 2, y + 16, v, 'f-s')
        y += 22
    y += 8
    b += box(10, y, 345, 52, ['Avoid fibrillation with LV hypertrophy or', 'poor venting: subendocardial flow suffers'], 'warn', 'f-s')
    b += box(365, y, 345, 52, ['No clamp: the option for a calcified', 'or porcelain ascending aorta'], 'ok', 'f-s')
    return svg(y + 62, b)


def f6_iccf_steps():
    """Intermittent cross-clamp fibrillation: one cycle per graft."""
    steps = [('1', 'Cool', ['32 to 33°C', 'on bypass']),
             ('2', 'Fibrillate', ['Fibrillator,', 'about 10 mA AC']),
             ('3', 'Clamp aorta', ['Distal', 'anastomosis']),
             ('4', 'Unclamp', ['Reperfuse the', 'myocardium']),
             ('5', 'Defibrillate', ['10 to 15 J;', 'then proximal'])]
    b = ''
    w = 128
    for i, (n, a, s) in enumerate(steps):
        x = 10 + i * (w + 14)
        cls = 'warn' if n == '3' else ('ok' if n in '45' else 'b0')
        b += f'<rect x="{x}" y="14" width="{w}" height="104" rx="10" class="f-{cls}"/>'
        b += f'<circle cx="{x + 22}" cy="36" r="14" class="f-b1"/>' + T(x + 22, 41, n, 'f-h')
        b += T(x + w / 2, 70, a, 'f-h')
        b += T(x + w / 2, 90, s, 'f-s')
        if i < 4:
            b += arrow(x + w + 1, 66, x + w + 13, 66)
    b += '<path d="M 540 120 C 540 160 380 168 230 160 C 210 159 205 150 206 124" class="f-dash" fill="none" marker-end="url(#ah)"/>'
    b += T(380, 182, 'Repeat steps 2 to 5 for each graft; rewarm during the last distal', 'f-s')
    b += box(10, 196, 345, 58, ['Ischaemia per clamp usually 15 to 20 min;', 'myocardial pH may not recover fully', 'between clamps (Dunning 2006)'], 'b1', 'f-s')
    b += box(365, 196, 345, 58, ['Each clamp is another aortic', 'manipulation: clamp periods predicted', 'stroke in the Coimbra series'], 'warn', 'f-s')
    return svg(264, b)


def f6_sirs_cascade():
    """Triggers, pathways and consequences of the inflammatory response to bypass."""
    b = T(110, 20, 'Triggers', 'f-h') + T(360, 20, 'Pathways activated', 'f-h') + T(610, 20, 'Consequences', 'f-h')
    trig = [['Blood on foreign', 'surface (oxygenator)'], ['Shed mediastinal', 'blood (suckers)'],
            ['Ischaemia and', 'reperfusion'], ['Cooling and', 'non-pulsatile flow']]
    for i, t in enumerate(trig):
        y = 34 + i * 76
        b += box(10, y, 200, 62, t, 'b1', 'f-s')
    path = [('Contact system', 'XII, XI, prekallikrein, kininogen'),
            ('Complement', 'coats the membrane; C3a'),
            ('Platelets and thrombin', 'surface and tissue factor'),
            ('Fibrinolysis', 'from shed blood'),
            ('Leucocytes, cytokines', 'IL-6, IL-8, TNF; oxidants'),
            ('Glycocalyx shedding', 'heparan sulphate (DAMP)'),
            ('Stress hormones', 'catecholamines, vasopressin')]
    for i, (a, s) in enumerate(path):
        y = 34 + i * 43
        b += f'<rect x="250" y="{y}" width="220" height="38" rx="8" class="f-b0"/>'
        b += T(360, y + 16, a, 'f-h') + T(360, y + 31, s, 'f-s')
    cons = [['Vasoplegia'], ['Surface-induced', 'coagulopathy, bleeding'], ['Lung injury'],
            ['Acute kidney injury'], ['Myocardial injury'], ['Gut ischaemia']]
    for i, c in enumerate(cons):
        y = 34 + i * 50
        b += box(510, y, 200, 42, c, 'warn', 'f-s')
    for y in (65, 141, 217, 293):
        b += arrow(211, y, 248, y if y < 300 else 290)
    for y in (90, 190, 290):
        b += arrow(471, y, 508, y)
    b += box(10, 348, 700, 62, ['Modifiers: coated circuits · closed or reduced circuits (MiECC) · separate cardiotomy blood ·',
                               'ultrafiltration · off-pump surgery · steroids (dampen markers; no outcome gain) · haemoadsorption'], 'ok', 'f-s')
    return svg(420, b)


def f6_q10():
    """Relative metabolic rate by temperature using the Q10 rule."""
    pts = [('37°C normothermia', 37), ('32°C mild', 32), ('28°C high-moderate', 28),
           ('24°C low-moderate', 24), ('20°C deep', 20)]
    items = []
    for lab, t in pts:
        v = round(100 * 2 ** ((t - 37) / 10))
        cls = 'b1' if t == 37 else ('ok' if t <= 20 else 'b0')
        items.append((lab, v, cls))
    h, b = bars(items, '%', 110, 'Q10 rule: metabolic rate about halves for each 10°C fall', lab_w=200)
    b += box(10, h + 4, 345, 70, ['Guideline: cerebral metabolism falls', '6 to 7% per °C; O2 use 50 to 60% of', 'baseline at 25 to 28°C'], 'b1', 'f-s')
    b += box(365, h + 4, 345, 70, ['Isolated deep hypothermic arrest:', 'keep to 30 to 40 min', '(18°C in TSRA ch. 79)'], 'warn', 'f-s')
    b += T(10, h + 96, 'Bars computed as 2^((T − 37)/10); illustrative, not measured values', 'f-s', 'start')
    return svg(h + 106, b)


def f6_alpha_ph():
    """Alpha-stat and pH-stat compared."""
    b = _f6_card(10, 10, 345, 196, 'Alpha-stat', ['Blood gases not corrected for', 'patient temperature', '',
                                                'Standard for adults on cooled bypass', 'Better neurological and cognitive', 'outcome in three 1990s RCTs',
                                                'Guideline: IIa, B'], 'ok')
    b += _f6_card(365, 10, 345, 196, 'pH-stat', ['Blood gases corrected to', 'patient temperature',
                                               'CO2 added to the sweep gas', 'Strategy changes cerebral blood flow,', 'not cerebral metabolism (Stephan 1992)',
                                               'Worse adult outcomes in those RCTs', 'Not the adult standard'], 'b1')
    return svg(216, b)


def f6_do2():
    """DO2 equations, thresholds and a worked example."""
    b = box(10, 10, 700, 74, ['CaO2 (mL/dL) = 1.34 × Hb (g/dL) × SaO2 + 0.003 × PaO2 (mmHg)',
                             'DO2i (mL/min/m²) = pump flow index (L/min/m²) × CaO2 × 10',
                             'O2ER = VO2 ÷ DO2  ·  Fick: VO2 = flow × (CaO2 − CvO2)'], 'b1', '')
    h, c = bars([('Hb 7 g/dL', 240, 'warn'), ('Hb 8 g/dL', 272, 'warn'), ('Hb 9 g/dL', 304, 'ok'), ('Hb 10 g/dL', 336, 'ok')],
                '', 400, 'Worked example: flow 2.4 L/min/m², SaO2 100%, PaO2 200 mmHg', lab_w=170)
    span = W - 170 - 90
    x280 = 170 + span * 280 / 400
    c += f'<line x1="{x280}" y1="38" x2="{x280}" y2="{h - 4}" class="f-cut"/>'
    c += T(x280 + 6, h + 8, 'DO2i 280: class I, A (AKI)', 'f-s', 'start')
    b += f'<g transform="translate(0 92)">{c}</g>'
    y = 92 + h + 20
    b += _f6_tiles_row(y, [('280', ['Lower limit, mL/min/m²', 'EACTS 2024 (I, A)'], 'ok'),
                       ('270', ['Optimal threshold,', 'Australasian registry'], 'b0'),
                       ('300', ['Target in the', 'Mukaida RCT'], 'b0'),
                       ('15 min', ['Below 300 for longer,', 'with CPB over 121 min'], 'warn')])
    return svg(y + 104, b)


def _f6_tiles_row(y, items, h=92):
    n = len(items)
    w = (W - 20 - (n - 1) * 14) / n
    out = ''
    for i, (big, small, cls) in enumerate(items):
        x = 10 + i * (w + 14)
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="f-{cls}"/>'
        out += T(x + w / 2, y + 36, big, 'f-big')
        out += T(x + w / 2, y + 60, small, 'f-s')
    return out


# ---- figs_F7.py



def f7_conduit_handling():
    """Conduit handling by conduit type, ESC/EACTS 2024 consensus (Sandner, Eur Heart J 2025)."""
    b = ''
    cols = [
        ('Internal thoracic artery', [
            ('High sternal wound risk,', 'or bilateral ITA:', 'skeletonise', 'ok'),
            ('Papaverine around or on', 'the artery (luminal use', 'risks intimal injury)', 'b1'),
        ]),
        ('Radial artery', [
            ('Open harvest is standard;', 'skeletonise only 2 to 3 cm', 'at each end', 'ok'),
            ('Verapamil plus nitroglycerine;', 'store in a solution', 'without blood', 'b1'),
        ]),
        ('Saphenous vein', [
            ('Low leg wound risk: open,', 'preferably no-touch.', 'High risk: endoscopic', 'ok'),
            ('Buffered storage, not saline;', 'avoid high-pressure', 'distension', 'b1'),
        ]),
    ]
    for i, (head, rows) in enumerate(cols):
        x = 10 + i * 238
        b += box(x, 10, 226, 40, head, 'b0', 'f-h')
        y = 62
        for l1, l2, l3, c in rows:
            b += arrow(x + 113, y - 12, x + 113, y - 2)
            b += box(x, y, 226, 72, [l1, l2, l3], c, 'f-s')
            y += 88
    b += box(10, 250, 700, 62, ['After surgery: aspirin within 6 h · add clopidogrel or ticagrelor for year 1 if bleeding',
                                'risk is not high · high-intensity statin · calcium-channel blocker for 1 year after a radial graft'], 'warn', 'f-s')
    b += line(10, 240, 710, 240, 'f-grid')
    return svg(322, b)


def f7_radial_steps():
    """Radial artery pathway: assessment, harvest, handling, after surgery."""
    steps = [
        ('Before', ['Allen test:', 'complete palmar', 'arch; no prior', 'procedure through', 'the artery']),
        ('Harvest', ['Open harvest;', 'fascia opened full', 'length; skeletonise', 'only 2 to 3 cm', 'at the ends']),
        ('Energy', ['Harmonic scalpel:', 'less spasm, larger', 'lumen; bipolar more', 'precise than', 'monopolar']),
        ('Handling', ['Verapamil plus', 'nitroglycerine;', 'store without', 'blood (blood', 'adds spasm)']),
        ('After', ['Amlodipine or', 'diltiazem for 1 year', '(non-randomised', 'evidence)']),
    ]
    b = ''
    for i, (h, ls) in enumerate(steps):
        x = 10 + i * 142
        b += box(x, 10, 130, 36, h, 'b0', 'f-h')
        b += box(x, 56, 130, 104, ls, 'b1', 'f-s')
        if i < 4:
            b += arrow(x + 131, 28, x + 141, 28)
    b += T(360, 184, 'Avoid in diabetes with peripheral vascular disease (spasm, calcification): TSRA Review ch. 50', 'f-s')
    return svg(196, b)


def f7_vein_trials():
    """REGROUP and the Tian no-touch RCT, figures as quoted in the 2024 ESC/EACTS consensus."""
    h1, b1 = bars([('Open harvest, 2.8 years', 15.5, 'b1'), ('Endoscopic harvest, 2.8 years', 13.9, 'b0'),
                   ('Open harvest, 4.7 years', 23.5, 'b1'), ('Endoscopic harvest, 4.7 years', 21.9, 'b0')],
                  '%', 30, 'REGROUP: death, MI or repeat revascularisation did not differ', 280)
    h2, b2 = bars([('No-touch, occluded at 12 months', 3.7, 'ok'), ('Conventional, occluded at 12 months', 6.5, 'warn'),
                   ('No-touch, leg wound surgery, 3 mo', 10.3, 'warn'), ('Conventional, leg wound surgery, 3 mo', 4.3, 'ok')],
                  '%', 30, 'No-touch RCT (2,655): fewer occlusions, more leg wound surgery', 280)
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


def f7_antiplatelet_timeline():
    """Antithrombotic timeline around CABG: EACTS 2024 perioperative guideline and ESC/EACTS 2025 consensus."""
    b = line(30, 64, 700, 64)
    ticks = [(40, '7 days'), (130, '5 days'), (210, '3 days'), (300, 'Surgery'),
             (390, '6 to 24 h'), (470, '48 h'), (560, '3 months'), (690, '12 months')]
    for x, lab in ticks:
        b += line(x, 58, x, 70) + T(x, 48, lab, 'f-s')
    b += T(30, 22, 'Stop before elective CABG; aspirin continues', 'f-h', 'start')
    b += box(10, 84, 110, 40, 'Prasugrel', 'warn', 'f-s') + box(124, 84, 80, 40, 'Clopidogrel', 'warn', 'f-s')
    b += box(208, 84, 84, 40, 'Ticagrelor', 'warn', 'f-s')
    b += box(310, 84, 150, 40, ['Aspirin restarted', 'by 24 h, ideally 6 h'], 'ok', 'f-s')
    b += box(464, 84, 236, 40, ['P2Y12 restarted once bleeding', 'is no longer a concern'], 'b0', 'f-s')
    b += box(296, 140, 414, 36, 'ACS: aspirin plus ticagrelor or prasugrel for 12 months (consensus)', 'b1', 'f-s')
    b += box(296, 184, 414, 36, 'CCS, low bleeding risk: DAPT for 12 months may be considered (IIb B)', 'b1', 'f-s')
    b += box(296, 228, 300, 36, 'TOP-CABG: 3 months of DAPT non-inferior', 'ok', 'f-s')
    b += box(10, 140, 280, 124, ['Post-operative AF', 'UFH or LMWH within 24 h (IIa C)', 'OAC at least 4 weeks if AF at', 'discharge (I B), then reassess', 'OAC plus one antiplatelet;', 'no triple therapy'], 'b0', 'f-s')
    b += T(360, 290, 'Lifelong aspirin 75 to 100 mg after CABG (ESC 2024, I A)', 'f-h')
    return svg(302, b)


def f7_tacsi_topcabg():
    """TACSI and TOP-CABG, ESC Congress 2025."""
    h1, b1 = bars([('DAPT (ticagrelor + aspirin), MACE', 4.8, 'b1'), ('Aspirin alone, MACE', 4.6, 'b1'),
                   ('DAPT, major bleeding', 4.9, 'warn'), ('Aspirin alone, major bleeding', 2.0, 'ok')],
                  '%', 15, 'TACSI (2,201 after ACS): DAPT added bleeding, not protection', 290)
    h2, b2 = bars([('3 months DAPT, graft occlusion', 10.79, 'ok'), ('12 months DAPT, graft occlusion', 11.19, 'b1'),
                   ('3 months DAPT, BARC 2 or more bleeding', 8.26, 'ok'), ('12 months DAPT, BARC 2 or more', 13.19, 'warn')],
                  '%', 15, 'TOP-CABG (2,290): 3 months non-inferior, less bleeding', 290)
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


def _f7_ring(cx, cy, defect, cls_def='f-warn'):
    """Short-axis ring; defect is (start_deg, end_deg) or None."""
    import math
    out = f'<circle cx="{cx}" cy="{cy}" r="40" class="f-b0"/><circle cx="{cx}" cy="{cy}" r="22" class="f-lumen"/>'
    if defect:
        a0, a1 = [math.radians(a) for a in defect]
        def p(r, a):
            return f'{cx + r * math.cos(a):.1f} {cy + r * math.sin(a):.1f}'
        out += (f'<path d="M{p(40, a0)} A40 40 0 0 1 {p(40, a1)} L{p(22, a1)} A22 22 0 0 0 {p(22, a0)} Z" class="{cls_def}"/>')
    return out


def f7_spect_reading():
    """Reading stress and rest perfusion images (ESC 2024 CCS guideline, section 3.3.2)."""
    b = T(250, 22, 'Stress', 'f-h') + T(400, 22, 'Rest', 'f-h') + T(600, 22, 'Reading', 'f-h')
    rows = [(None, None, 'Normal uptake at stress and rest', 'ok'),
            ((200, 320), None, 'Defect at stress that fills in at rest: ischaemia', 'warn'),
            ((200, 320), (200, 320), 'Defect at stress and rest: fixed (scar)', 'b1')]
    for i, (ds, dr, txt, c) in enumerate(rows):
        y = 80 + i * 104
        b += _f7_ring(250, y, ds) + _f7_ring(400, y, dr)
        b += box(470, y - 30, 240, 60, txt.split(': ') if ': ' in txt else txt, c, 'f-s')
    b += box(10, 44, 170, 90, ['SPECT: technetium-99m', 'tracers; avoid', 'thallium-201', '(more radiation)'], 'b1', 'f-s')
    b += box(10, 146, 170, 90, ['PET: ammonia, water', 'or rubidium-82;', 'absolute flow;', 'MFR under 2.0 abnormal'], 'b1', 'f-s')
    b += box(10, 248, 170, 60, ['High risk: ischaemia', '10% of LV or more'], 'warn', 'f-s')
    b += T(360, 340, 'Extra clues to severe disease: transient ischaemic dilatation, fall in post-stress EF, calcium score', 'f-s')
    return svg(352, b)


# ---- figs_F8.py



def _f8_heart(sam=True):
    """Long-axis outline (apex left, aorta top right, left atrium bottom right)."""
    b = ''
    # left ventricular cavity and left atrium
    b += '<path d="M70 175 C70 120 110 96 170 96 L520 96 L520 168 L470 252 L170 252 C110 252 70 228 70 175 Z" class="f-lumen"/>'
    b += '<path d="M520 160 C600 150 690 170 700 220 C708 270 640 300 560 296 C510 292 476 276 470 256 Z" class="f-lumen"/>'
    # aorta (open to the right)
    b += '<rect x="520" y="62" width="186" height="94" class="f-lumen" style="stroke:none"/>'
    b += '<path d="M520 62 L706 62 M706 156 L520 156" class="f-l"/>'
    # septum with basal bulge
    b += ('<path d="M74 150 C80 100 120 62 170 62 L520 62 L520 100 C500 104 486 146 444 150 '
          'C410 152 392 112 360 104 L170 104 C126 104 100 124 96 160 Z" class="f-b1"/>')
    # posterior wall
    b += '<path d="M74 196 C84 248 120 286 170 286 L470 286 L470 254 L170 254 C126 254 100 236 96 196 Z" class="f-b1"/>'
    # papillary muscle
    b += '<path d="M300 254 C306 226 334 222 346 254 Z" class="f-b0"/>'
    # aortic valve cusps (open)
    b += line(522, 66, 548, 82) + line(522, 152, 548, 138)
    # posterior mitral leaflet
    b += '<path d="M470 254 C468 236 462 224 452 214" class="f-l" fill="none" style="stroke-width:3.5px"/>'
    if sam:
        b += '<path d="M520 166 C500 176 476 176 458 160 C452 154 448 150 446 148" class="f-l" fill="none" style="stroke-width:3.5px"/>'
        b += '<line x1="458" y1="162" x2="330" y2="230" class="f-l" stroke-dasharray="3 3"/>'
    else:
        b += '<path d="M520 166 C506 184 486 200 466 212" class="f-l" fill="none" style="stroke-width:3.5px"/>'
        b += '<line x1="466" y1="212" x2="330" y2="230" class="f-l" stroke-dasharray="3 3"/>'
    b += '<line x1="452" y1="214" x2="338" y2="232" class="f-l" stroke-dasharray="3 3"/>'
    return b


def f8_sam_mechanism():
    b = _f8_heart(True)
    b += arrow(150, 196, 410, 166) + arrow(540, 110, 660, 110)
    b += arrow(500, 214, 640, 262, dash=True)
    b += T(170, 84, 'Basal septal hypertrophy', 'f-h', 'start')
    b += T(606, 104, 'Aorta', 'f-s')
    b += T(600, 284, 'Left atrium', 'f-s')
    b += T(240, 214, 'Ejection flow', 'f-s')
    b += T(324, 274, 'Papillary muscle', 'f-s')
    b += T(14, 322, ['Systolic anterior motion: flow drags the anterior mitral leaflet into the narrowed outflow,',
                     'where it meets the septum. The leaflets no longer meet, so the leak is mid to late systolic',
                     'and directed posteriorly or laterally. A central or anterior jet suggests intrinsic mitral disease.'], 'f-s', 'start')
    b += T(14, 384, ['Elongated leaflets, anomalous papillary muscle insertion and anteriorly displaced papillary',
                     'muscles add to the obstruction (AHA/ACC 2024, sections 3.1 and 3.3).'], 'f-s', 'start')
    b += T(300, 128, 'Contact point: obstruction', 'f-h') + line(380, 132, 440, 150)
    b += T(612, 244, 'Leak', 'f-s')
    return svg(426, b)


def f8_myectomy_area():
    b = _f8_heart(False)
    # resection trough: basal part and distal extension
    b += ('<path d="M518 100 C500 104 486 146 444 150 C410 152 392 112 360 104 L330 104 '
          'L330 84 C380 84 410 112 444 114 C480 112 498 90 518 80 Z" class="f-warn"/>')
    b += '<path d="M330 86 L250 92 L250 104" class="f-cut" stroke-dasharray="5 4"/>'
    b += T(170, 46, 'Rectangular trough cut into the basal septum (shaded)', 'f-h', 'start')
    b += T(606, 104, 'Aorta', 'f-s') + T(600, 270, 'Left atrium', 'f-s')
    b += T(210, 150, ['Extension to the papillary', 'muscle bases if mid-cavity', 'obstruction (limited data)'], 'f-s')
    b += T(14, 322, 'Starts below the aortic valve and runs beyond the point of mitral leaflet to septum contact (ESC 2023).', 'f-s', 'start')
    b += box(10, 336, 228, 78, ['Too deep: septal defect.', 'Risk higher if septum', '16 mm or less at contact'], 'warn', 'f-s')
    b += box(246, 336, 228, 78, ['Conduction tissue:', 'AV block; left bundle', 'branch block is common'], 'warn', 'f-s')
    b += box(482, 336, 228, 78, ['Aortic cusps:', 'regurgitation. Check all', 'of these on TOE after bypass'], 'warn', 'f-s')
    return svg(424, b)


def f8_srt_pathway():
    b = box(170, 6, 380, 44, ['Symptoms with outflow gradient 50 mmHg or more', '(at rest, Valsalva or exercise)'], 'b1', 'f-s')
    b += arrow(360, 50, 360, 66)
    b += box(120, 68, 480, 40, 'Non-vasodilating beta-blocker; verapamil or diltiazem if not tolerated', 'b0', 'f-s')
    b += arrow(360, 108, 360, 124)
    b += box(170, 126, 380, 34, 'Still symptomatic', 'b1', 'f-h')
    b += arrow(290, 160, 180, 182) + arrow(430, 160, 540, 182)
    b += box(10, 184, 340, 76, ['Add mavacamten (ESC IIa A; AHA 1 B-R)', 'or disopyramide (ESC I B) with an AV', 'nodal blocker; not both together'], 'b0', 'f-s')
    b += box(370, 184, 340, 76, ['Septal reduction: NYHA III to IV (I B)', 'or recurrent exertional syncope (IIa C);', 'NYHA II with SAM-related MR, AF or', 'large atrium at expert centres (IIb C)'], 'b0', 'f-s')
    b += arrow(470, 260, 300, 288) + arrow(610, 260, 610, 288)
    b += box(150, 290, 300, 92, ['Myectomy preferred: children, other', 'surgery needed (mitral, papillary,', 'coronary, aortic valve), septum', '30 mm or more, gradient 100 or more'], 'ok', 'f-s')
    b += box(470, 290, 240, 92, ['Alcohol ablation: surgery', 'contraindicated or too risky,', 'suitable septal artery', '(AHA 1 C-LD)'], 'b1', 'f-s')
    b += T(360, 404, 'Either way: experienced operators in an HCM team (ESC I C; AHA 1 C-LD for centres).', 'f-s')
    return svg(416, b)


def f8_myosin_trials():
    h1, b1 = bars([('Mavacamten', 37, 'ok'), ('Placebo', 17, 'b1')], '%', 100,
                  'EXPLORER-HCM (n=251): met the primary functional end point at 30 weeks')
    h2, b2 = bars([('Mavacamten', 17.9, 'ok'), ('Placebo', 76.8, 'warn')], '%', 100,
                  'VALOR-HCM (n=112): still eligible for septal reduction at 16 weeks')
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


def f8_icd_risk():
    return tiles([('Under 4%', ['5-year risk: no ICD;', 'LGE 15% or more or', 'EF under 50%: IIb'], 'ok'),
                  ('4 to <6%', ['ICD may be', 'considered', '(IIb B)'], 'b1'),
                  ('6% or more', ['ICD should be', 'considered', '(IIa B)'], 'warn'),
                  ('Arrest or VT', ['Secondary', 'prevention ICD', '(I B)'], 'warn')], 126)


def f8_srt_targets():
    h1, b1 = bars([('Myectomy: heart block, pacemaker', 5, 'b0'), ('Alcohol ablation: heart block', 10, 'warn'),
                   ('Myectomy: repeat procedure', 3, 'b0'), ('Alcohol ablation: repeat procedure', 10, 'warn'),
                   ('Either: 30-day mortality', 1, 'b1')], '%', 20,
                  'AHA/ACC 2024 Table 5: the most a centre should accept', 300)
    h2, b2 = bars([('Low-volume hospitals', 15.6, 'warn'), ('Middle tertile', 9.6, 'b1'), ('High-volume hospitals', 3.8, 'ok')],
                  '%', 20, 'Myectomy in-hospital mortality by hospital volume (US, 2003 to 2011)', 300)
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


# ---- figs_F9.py



def f9_postop_pacing():
    """Pacing decisions after cardiac surgery, ESC 2021 section 8.2."""
    b = box(210, 8, 300, 36, 'Bradycardia after cardiac surgery', 'b1', 'f-h')
    b += arrow(290, 44, 120, 70) + arrow(360, 44, 360, 70) + arrow(430, 44, 600, 70)
    b += box(10, 72, 220, 52, ['High-degree or', 'complete AV block'], 'b0')
    b += box(250, 72, 220, 52, ['Sinus node dysfunction', '(surgery or transplant)'], 'b0')
    b += box(490, 72, 220, 52, ['Tricuspid surgery and', 'pacing needed'], 'b0')
    b += arrow(120, 124, 120, 146)
    b += box(10, 148, 220, 70, ['Observe at least 5 days', '(I, C); usual practice', '3 to 7 days'], 'ok')
    b += arrow(360, 124, 360, 146)
    b += box(250, 148, 220, 70, ['Observe up to 6 weeks', 'before a permanent', 'system (IIa, C)'], 'ok')
    b += arrow(600, 124, 600, 146)
    b += box(490, 148, 220, 70, ['Epicardial ventricular lead;', 'avoid transvalvular', 'leads (IIa, C)'], 'ok')
    b += arrow(120, 218, 120, 240)
    b += box(10, 242, 220, 88, ['Shorten if low or no', 'escape rhythm and', 'recovery unlikely; CHB', 'within 24 h of valve surgery', 'lasting 48 h: earlier PPM'], 'warn', 'f-s')
    b += arrow(360, 218, 360, 240)
    b += box(250, 242, 220, 88, ['Heart transplant:', 'chronotropic incompetence', 'beyond 6 weeks: pace', 'for quality of life', '(IIa, C)'], 'warn', 'f-s')
    b += arrow(600, 218, 600, 240)
    b += box(490, 242, 220, 88, ['Bioprosthesis or ring:', 'CS lead or epicardial', 'lead (IIa, C).', 'Mechanical TV: no', 'transvalvular lead (III, C)'], 'warn', 'f-s')
    b += box(10, 344, 700, 46, ['Endocarditis surgery with complete AV block in theatre plus a predictor of persistence:',
                               'consider an immediate epicardial pacemaker (IIa, C)'], 'b1', 'f-s')
    b += T(12, 408, 'Predictors: pre-operative conduction disease, S. aureus, intracardiac abscess, tricuspid involvement, previous valve surgery.', 'f-s', 'start')
    return svg(420, b)


def f9_tavi_pacing():
    """Conduction disturbance after TAVI, ESC 2021 section 8.3."""
    b = box(230, 8, 260, 36, 'ECG after TAVI', 'b1', 'f-h')
    for x in (95, 275, 445, 625):
        b += arrow(360, 44, x, 70)
    b += box(10, 72, 170, 66, ['Complete or high-', 'degree AV block', 'for 24 to 48 h'], 'b0')
    b += box(190, 72, 170, 66, ['New alternating', 'bundle branch', 'block'], 'b0')
    b += box(370, 72, 150, 66, ['Pre-existing RBBB', 'plus any new', 'disturbance'], 'b0')
    b += box(530, 72, 180, 66, ['New LBBB, QRS over', '150 ms or PR over', '240 ms, stable 48 h'], 'b0')
    for x in (95, 275, 445, 620):
        b += arrow(x, 138, x, 160)
    b += box(10, 162, 170, 52, ['Permanent pacing', '(I, B)'], 'ok')
    b += box(190, 162, 170, 52, ['Permanent pacing', '(I, C)'], 'ok')
    b += box(370, 162, 150, 52, ['Early pacing', '(IIa, B)'], 'ok')
    b += box(530, 162, 180, 52, ['Ambulatory ECG or', 'EP study (IIa, C)'], 'warn')
    b += box(10, 228, 345, 52, ['Pre-existing conduction disease, QRS or PR', 'longer by over 20 ms: monitor or EPS (IIb, C)'], 'warn', 'f-s')
    b += box(365, 228, 345, 52, ['RBBB with no pacing indication: no', 'prophylactic pacemaker before TAVI (III, C)'], 'track', 'f-s')
    b += T(12, 300, 'Pacemaker after TAVI: 3.4 to 25.9% in trials and registries. RBBB is the strongest predictor.', 'f-s', 'start')
    b += T(12, 318, 'Others: older age, male, mitral annular or LVOT calcification, short membranous septum, self-expanding valve,', 'f-s', 'start')
    b += T(12, 335, 'deep implant, oversizing, balloon post-dilatation.', 'f-s', 'start')
    return svg(346, b)


def f9_routes():
    """Schematic heart (anterior view) showing the routes for a pacing lead."""
    b = T(12, 22, 'Where the lead goes: transvenous, leadless and epicardial routes (schematic)', 'f-h', 'start')
    b += '<path d="M262 36 L262 128" class="f-vessel" style="stroke-width:14px"/>'
    b += '<path d="M262 300 L262 400" class="f-vessel" style="stroke-width:14px"/>'
    b += T(282, 50, 'SVC', 'f-s', 'start') + T(282, 396, 'IVC', 'f-s', 'start')
    b += '<ellipse cx="510" cy="232" rx="112" ry="100" class="f-b1"/>' + T(580, 196, 'LV', 'f-h')
    b += '<ellipse cx="268" cy="196" rx="56" ry="70" class="f-b1"/>' + T(246, 206, 'RA', 'f-h')
    b += '<path d="M318 170 Q400 150 470 180 Q500 260 440 322 Q360 330 318 260 Z" class="f-b0"/>' + T(400, 236, 'RV', 'f-h')
    b += '<ellipse cx="236" cy="138" rx="24" ry="14" class="f-b0"/>' + T(196, 120, 'RA appendage', 'f-s', 'end')
    # transvenous leads
    b += '<path d="M258 36 L258 118 Q254 136 240 140" class="f-l" fill="none" style="stroke-width:2.5px"/>'
    b += '<path d="M265 36 L268 200 Q300 230 360 236 Q400 244 410 290" class="f-l" fill="none" style="stroke-width:2.5px"/>'
    b += '<path d="M270 36 L274 250 Q300 300 420 336 Q540 340 600 296 Q618 270 614 250" class="f-dash" fill="none"/>'
    b += '<circle cx="240" cy="140" r="4" class="f-ah"/><circle cx="410" cy="292" r="4" class="f-ah"/><circle cx="614" cy="248" r="4" class="f-ah"/>'
    # leadless capsule via IVC
    b += '<path d="M254 400 L254 280 Q290 290 352 286" class="f-dash" fill="none"/>'
    b += '<rect x="352" y="278" width="28" height="13" rx="6" class="f-warn"/>'
    # epicardial leads
    b += '<path d="M690 200 Q660 210 622 214" class="f-nerve" fill="none"/><circle cx="622" cy="214" r="5" class="f-ah"/>'
    b += '<path d="M380 420 Q376 360 372 326" class="f-nerve" fill="none"/><circle cx="372" cy="324" r="5" class="f-ah"/>'
    # labels
    b += box(10, 160, 170, 84, ['Transvenous: cephalic', 'or axillary vein first', '(IIa, B); RA appendage', 'and RV septum'], 'b0', 'f-s')
    b += box(10, 256, 170, 70, ['LV via a coronary', 'sinus vein (dashed);', 'quadripolar (IIa, C)'], 'b0', 'f-s')
    b += box(10, 338, 170, 84, ['Leadless: capsule into', 'the RV from the femoral', 'vein; cardiac surgery', 'on site'], 'warn', 'f-s')
    b += box(470, 34, 240, 54, ['Mid-septal RV lead if perforation', 'risk is high (IIb, C)'], 'b0', 'f-s')
    b += box(560, 344, 150, 84, ['Epicardial LV lead:', 'thoracotomy or', 'minimally invasive;', 'if CS lead fails'], 'ok', 'f-s')
    b += line(690, 200, 700, 200, 'f-nerve') + T(704, 188, 'to LV epicardium', 'f-s', 'end')
    b += box(392, 400, 160, 50, ['Epicardial RV lead:', 'sternotomy or subxiphoid'], 'ok', 'f-s')
    return svg(460, b)


def f9_aad():
    """Modernised classification of antiarrhythmic drugs (Lei et al.)."""
    rows = [('0', 'HCN channel (If)', 'Ivabradine', 'b1'),
            ('I', 'Sodium channel Nav1.5', 'Ia quinidine, procainamide, disopyramide · Ib lidocaine, mexiletine · Ic flecainide, propafenone · Id ranolazine', 'b0'),
            ('II', 'G-protein signalling: beta, adenosine A1, M2', 'Beta-blockers (bisoprolol, esmolol…) · isoprenaline, adrenaline · adenosine · atropine', 'b0'),
            ('III', 'Potassium channels', 'Amiodarone, dronedarone (non-selective) · sotalol, dofetilide, ibutilide (IKr) · vernakalant (IKur) · nicorandil (KATP opener)', 'b0'),
            ('IV', 'Calcium handling: L-type channel, RyR2', 'Verapamil, diltiazem · RyR2 block: flecainide, carvedilol, dantrolene', 'b0'),
            ('V', 'Mechanosensitive channels', 'No approved drug', 'f-track'),
            ('VI', 'Gap junctions (connexins)', 'No approved drug', 'f-track'),
            ('VII', 'Upstream remodelling', 'ACE inhibitors, ARBs, statins, omega-3, SGLT2 inhibitors (unproven as anti-arrhythmics)', 'b1')]
    b = T(12, 22, 'Eight classes: Vaughan Williams I to IV kept, 0, V, VI and VII added', 'f-h', 'start')
    y = 36
    for c, tgt, ex, cls in rows:
        cls = cls.replace('f-', '')
        b += f'<rect x="10" y="{y}" width="56" height="44" rx="8" class="f-{cls}"/>' + T(38, y + 30, c, 'f-big')
        b += T(78, y + 18, tgt, 'f-h', 'start')
        words, lines, cur = ex.split(' '), [], ''
        for w in words:
            if len(cur) + len(w) > 92:
                lines.append(cur.strip()); cur = ''
            cur += w + ' '
        lines.append(cur.strip())
        b += T(78, y + 36, lines, 'f-s', 'start')
        y += 50 + 17 * (len(lines) - 1)
    b += T(12, y + 14, 'Oral amiodarone acts mainly on IKr (class III); IV amiodarone also has class I, II and IV actions.', 'f-s', 'start')
    return svg(y + 26, b)


def f9_complications():
    h, b = bars([('Tricuspid regurgitation', (5, 15), 'warn'),
                 ('Any complication', (5, 15), 'warn'),
                 ('Lead reintervention', (1.0, 5.9), 'b0'),
                 ('Haematoma', (2.1, 5.3), 'b0'),
                 ('Diaphragm stimulation', (0.5, 5), 'b0'),
                 ('Pneumothorax', (0.5, 2.2), 'b0'),
                 ('Death within 30 days', (0.8, 1.4), 'b1'),
                 ('Cardiac perforation', (0.3, 0.7), 'b1')],
                '%', 16, 'Pacemaker complications: TR and lead problems are the common ones (ESC 2021 Table 12)', lab_w=210)
    return svg(h, b)


def f9_praetorian():
    h, b = bars([('Inappropriate shocks: S-ICD', 9.7, 'warn'),
                 ('Inappropriate shocks: transvenous', 7.3, 'b1'),
                 ('Device complications: S-ICD', 5.9, 'ok'),
                 ('Device complications: transvenous', 9.8, 'b1')],
                '%', 12, 'PRAETORIAN (849, mean 49 months): S-ICD non-inferior; fewer complications, more inappropriate shocks', lab_w=260)
    return svg(h, b)


# ---- figs_F10.py

import math


def f10_pcs_algorithm():
    """Post-cardiotomy low output: 2025 EACTS/STS/AATS tMCS guideline, Tables 6 and 10, section 9.2."""
    b = box(160, 8, 400, 44, ['Cannot separate from bypass, or low output', 'early after surgery despite optimal therapy'], 'b1', 'f-h')
    b += arrow(360, 52, 360, 72)
    b += box(110, 74, 500, 44, ['First correct the correctable: TOE, grafts, valve or repair,', 'tamponade, rhythm, preload, ventilation'], 'b0', 'f-s')
    b += arrow(360, 118, 360, 138)
    b += box(160, 140, 400, 40, 'Recovery, transplant or durable VAD possible?', 'b1', 'f-h')
    b += arrow(200, 180, 120, 206) + arrow(520, 180, 600, 206)
    b += T(150, 196, 'No', 'f-s', 'end') + T(570, 196, 'Yes', 'f-s', 'start')
    b += box(10, 208, 220, 56, ['tMCS not recommended', '(III C)'], 'warn', 'f-s')
    b += box(250, 208, 460, 56, ['Immediate transition to tMCS (I B),', 'before irreversible organ injury; delay is harmful'], 'ok', 'f-s')
    b += arrow(480, 264, 480, 282)
    b += box(250, 284, 148, 66, ['LV only:', 'full-support mAFP', 'over partial'], 'b0', 'f-s')
    b += box(406, 284, 148, 66, ['Both ventricles:', 'VA-ECLS + mAFP,', 'or 2 pumps (I C)'], 'b0', 'f-s')
    b += box(562, 284, 148, 66, ['Heart and lungs:', 'VA-ECLS or', 'oxyBVAD (I C)'], 'b0', 'f-s')
    b += box(10, 284, 220, 66, ['Shock Team chooses', 'type and modality', '(I B)'], 'b1', 'f-s')
    b += box(10, 362, 700, 40, 'On VA-ECLS: timely LV unloading (IIa B) · distal limb perfusion cannula (I) · MAP 80 mmHg or more (I B)', 'b1', 'f-s')
    return svg(412, b)


def f10_protected():
    """Protected cardiac surgery: when tMCS goes in, with class and level (2025 guideline, Table 5)."""
    b = line(30, 40, 690, 40)
    pts = [(30, 'Before surgery'), (250, 'In theatre'), (470, 'Weaning from bypass'), (690, 'After surgery')]
    for x, lab in pts:
        b += line(x, 34, x, 46) + T(x, 26, lab, 'f-s', 'start' if x == 30 else ('end' if x == 690 else 'middle'))
    b += box(10, 60, 165, 118, ['Bridge to repair:', 'post-infarct rupture,', 'structural lesion,', 'refractory instability', 'IIb B'], 'b0', 'f-s')
    b += box(185, 60, 165, 118, ['Planned implant', 'when low output', 'is likely: helps', 'wean from bypass', 'IIa C'], 'b0', 'f-s')
    b += box(360, 60, 165, 118, ['Difficulty', 'weaning:', 'start tMCS early', '', 'I B'], 'ok', 'f-s')
    b += box(535, 60, 175, 118, ['Little chance of', 'recovery but a', 'transplant or durable', 'VAD candidate', 'I C'], 'ok', 'f-s')
    b += box(10, 192, 700, 40, ['Shock Team decides type and modality (I B). Age, comorbidity, lactate and kidney injury', 'predict death and are weighed before starting (IIa B)'], 'b1', 'f-s')
    return svg(242, b)


def f10_flows():
    """Maximum flow by temporary device, 2025 guideline section 5 and Table 4."""
    h, b = bars([('Intra-aortic balloon pump', (0.5, 1.0), 'b1'),
                 ('Microaxial pump, partial (left)', 3.5, 'b0'),
                 ('Microaxial pump, right-sided', 4, 'b0'),
                 ('Microaxial pump, full (left)', 5.5, 'ok'),
                 ('Centrifugal temporary VAD', 10, 'ok')], ' L/min', 11,
                'Most a device can add: a balloon pump adds under 1 L/min', 270)
    b += T(12, h + 4, 'Partial-support microaxial pump: 3.5 L/min in the text, 4.3 L/min peak in Table 4. Centrifugal VAD at 5,500 rpm.', 'f-s', 'start')
    return svg(h + 16, b)


def f10_weaning():
    """Weaning signals on VA-ECLS or microaxial pump, 2025 guideline Table 25 and section 16."""
    return tiles([('MAP 65+', ['mmHg with VIS under 10:', 'may wean (IIb C)'], 'b1'),
                  ('VTI 12 cm', ['LVOT velocity-time', 'integral or more'], 'b0'),
                  ('PAPi 0.9+', ['with adequate', 'RV function'], 'b0'),
                  ('Stop', ['if the LV or RV dilates', 'on echo (III C)'], 'warn')], 104)


def _f10_arc(cx, cy, r, a1, a2):
    """SVG arc path points from angle a1 to a2 (degrees, 0 = right, 90 = down)."""
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    large = 1 if (a2 - a1) % 360 > 180 else 0
    return x1, y1, x2, y2, large


def _f10_wedge(cx, cy, r1, r2, a1, a2, cls):
    ox1, oy1, ox2, oy2, lg = _f10_arc(cx, cy, r2, a1, a2)
    ix1, iy1, ix2, iy2, _ = _f10_arc(cx, cy, r1, a1, a2)
    return (f'<path d="M{ox1:.1f} {oy1:.1f} A{r2} {r2} 0 {lg} 1 {ox2:.1f} {oy2:.1f} '
            f'L{ix2:.1f} {iy2:.1f} A{r1} {r1} 0 {lg} 0 {ix1:.1f} {iy1:.1f} Z" class="{cls}"/>')


def _f10_heart(cx, cy, ro=66, ri=44):
    """Short-axis sketch: RV crescent on the left (septal side), LV ring on top."""
    b = f'<path d="M{cx - 20} {cy - ro - 8} C{cx - 150} {cy - ro - 30} {cx - 150} {cy + ro + 30} {cx - 20} {cy + ro + 8} Z" class="f-b0"/>'
    b += f'<path d="M{cx - 40} {cy - ro + 14} C{cx - 128} {cy - ro - 6} {cx - 128} {cy + ro + 6} {cx - 40} {cy + ro - 14} Z" class="f-lumen"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{ro}" class="f-b0"/><circle cx="{cx}" cy="{cy}" r="{ri}" class="f-lumen"/>'
    return b


def f10_vsd_repair():
    """Post-infarction VSD: primary patch repair against infarct exclusion (TSRA ch. 51)."""
    ro, ri, cy = 66, 44, 128
    b = ''
    for cx, title in [(150, 'Primary repair (more common)'), (510, 'Infarct exclusion')]:
        b += T(cx + 40, 22, title, 'f-h')
        b += _f10_heart(cx, cy, ro, ri)
        if cx == 150:
            b += _f10_wedge(cx, cy, ri, ro, 158, 202, 'f-warn')
            b += f'<rect x="{cx - ro - 3}" y="{cy - 8}" width="{ro - ri + 6}" height="16" class="f-lumen" style="stroke:none"/>'
            b += f'<path d="M{cx - ri + 3} {cy - 24} Q{cx - ri + 9} {cy} {cx - ri + 3} {cy + 24}" class="f-cut" style="stroke-width:5"/>'
            for dy in (-16, 0, 16):
                b += f'<rect x="{cx - ro - 12}" y="{cy + dy - 4}" width="9" height="8" rx="2" class="f-b1"/>'
                b += line(cx - ro - 3, cy + dy, cx - ri + 3, cy + dy, 'f-dash')
            b += line(cx - ri + 8, cy - 18, cx + 80, cy - 40, 'f-l')
            b += T(cx + 84, cy - 52, ['Necrotic septum debrided;', 'patch sewn to healthy', 'endocardium'], 'f-s', 'start')
            b += line(cx - ro - 8, cy + 20, cx - 40, cy + 100, 'f-l')
            b += T(cx - 40, cy + 116, ['Pledgeted mattress sutures from', 'the RV side, through septum, then patch'], 'f-s', 'start')
        else:
            b += _f10_wedge(cx, cy, ri, ro, 140, 250, 'f-warn')
            b += f'<rect x="{cx - ro - 3}" y="{cy - 8}" width="{ro - ri + 6}" height="16" class="f-lumen" style="stroke:none"/>'
            x1, y1 = cx + ri * math.cos(math.radians(134)), cy + ri * math.sin(math.radians(134))
            x2, y2 = cx + ri * math.cos(math.radians(256)), cy + ri * math.sin(math.radians(256))
            b += f'<path d="M{x1:.1f} {y1:.1f} Q{cx - 4} {cy - 2} {x2:.1f} {y2:.1f}" class="f-cut" style="stroke-width:5"/>'
            b += line(cx - 12, cy - 6, cx + 80, cy - 40, 'f-l')
            b += T(cx + 84, cy - 52, ['Large patch sewn to', 'non-infarcted septum', 'and LV wall'], 'f-s', 'start')
            b += T(cx - 40, cy + 116, ['No debridement: defect and infarct', 'are shut out of the high-pressure LV'], 'f-s', 'start')
        b += T(cx - 92, cy + 5, 'RV', 'f-s') + T(cx + 22, cy + 30, 'LV', 'f-s')
    b += box(10, 272, 700, 44, ['Graft first (cardioplegia down the grafts) · open the LV through the infarct beside the septum ·',
                                'close in two layers, 2-0 Prolene on felt strips · replace the mitral valve if the papillary muscle is involved'], 'b1', 'f-s')
    b += '<rect x="20" y="326" width="18" height="12" class="f-warn"/>' + T(44, 336, 'Infarcted muscle', 'f-s', 'start')
    b += line(170, 332, 196, 332, 'f-cut') + T(202, 336, 'Patch', 'f-s', 'start')
    b += '<rect x="262" y="327" width="9" height="8" rx="2" class="f-b1"/>' + T(278, 336, 'Pledget', 'f-s', 'start')
    return svg(346, b)


# ---- figs_F11.py



def f11_pmi_thresholds():
    h, b = bars([('Fourth UDMI type 5 (+ supporting sign)', 10, 'b1'),
                 ('ARC-2 (+ supporting sign)', 35, 'b1'),
                 ('SCAI or ARC-2 injury, troponin alone', 70, 'b0'),
                 ('VISION: 30-day death, days 2 to 3', 59, 'warn'),
                 ('VISION: 30-day death, day 1', 218, 'warn')],
                '× URL', 240, 'Troponin after CABG: the level tied to death is far above the definitions', lab_w=290)
    b += T(12, h + 4, 'VISION figures are troponin I after isolated CABG or AVR. URL: upper reference limit (99th centile).', 'f-s', 'start')
    return svg(h + 16, b)


def f11_pmi_findings():
    h, b = bars([('Acute graft failure', 62, 'warn'),
                 ('No culprit found', 31.7, 'b1'),
                 ('Incomplete revascularisation', 6, 'b0'),
                 ('New native coronary lesion', 3.5, 'b0')],
                '%', 100, 'Angiography for suspected PMI after CABG: two thirds are graft failure', lab_w=260)
    b += T(12, h + 4, 'Meta-analysis of 1,104 patients restudied after CABG, as quoted in the EACTS 2024 statement.', 'f-s', 'start')
    return svg(h + 16, b)


def f11_ckmb_risk():
    h, b = bars([('CK-MB 1 to 5 × URL', 1.69, 'b1'),
                 ('5 to 10 × URL', 2.98, 'b1'),
                 ('10 to 20 × URL', 4.47, 'b0'),
                 ('20 to 40 × URL', 8.73, 'warn'),
                 ('Over 40 × URL', 27.01, 'warn')],
                '', 30, 'Relative risk of death climbs steeply with CK-MB after CABG', lab_w=220)
    b += T(12, h + 4, 'Domanski meta-analysis, 18,908 CABG patients; model-estimated relative risk; follow-up varied (EACTS 2024, Table 4).', 'f-s', 'start')
    return svg(h + 16, b)


def f11_pmi_pathway():
    b = box(10, 10, 700, 54, ['Suspect: ischaemic ECG change · ventricular arrhythmia · biomarker rise',
                              'new regional wall motion abnormality · haemodynamic instability'], 'b1')
    b += arrow(360, 64, 360, 84)
    b += box(110, 86, 500, 54, ['Weigh them together: ECG and echo are non-specific', 'after surgery and biomarkers rise late'], 'b0')
    b += arrow(250, 140, 170, 168) + arrow(470, 140, 550, 168)
    b += box(10, 170, 320, 58, ['Severe ischaemia, large area at risk', 'or instability'], 'warn', 'f-h')
    b += box(390, 170, 320, 58, ['Asymptomatic occlusion found', 'or small territory'], 'b1')
    b += arrow(170, 228, 170, 250)
    b += box(10, 252, 320, 54, ['Urgent coronary angiography (I, C)', 'then ad hoc Heart Team decision (I, C)'], 'b0')
    b += arrow(550, 228, 550, 250)
    b += box(390, 252, 320, 54, ['Revascularise if the artery is a', 'good size and supplies a large area'], 'b1')
    b += arrow(110, 306, 110, 330) + arrow(240, 306, 300, 330)
    b += box(10, 332, 270, 92, ['Emergency PCI', 'Target the native vessel or', 'the mammary graft; avoid an', 'acutely occluded vein graft'], 'ok')
    b += box(300, 332, 410, 92, ['Redo surgery', 'Anatomy unsuitable for PCI', 'several important grafts occluded', 'or a clear anastomotic error'], 'warn')
    return svg(434, b)


def f11_embolectomy():
    # anterior view: patient's right on the viewer's left
    b = T(12, 22, "Patient's right", 'f-s', 'start') + T(708, 22, "Patient's left", 'f-s', 'end')
    b += '<path d="M210 40 L210 270" class="f-vessel" style="opacity:.35"/>' + T(210, 292, 'SVC', 'f-h')
    b += '<path d="M470 170 C420 170 360 168 150 168" class="f-vessel" style="stroke-width:24"/>'
    b += '<path d="M340 330 L340 140 C340 60 450 50 490 96" class="f-vessel" style="opacity:.8;stroke-width:34"/>'
    b += T(340, 352, 'Aorta', 'f-h')
    b += '<path d="M470 330 L470 180 C470 160 500 150 670 140" class="f-vessel" style="stroke-width:30"/>'
    b += line(452, 318, 488, 318, 'f-l')
    b += T(680, 118, 'Left PA', 'f-h', 'end') + T(150, 146, 'Right PA', 'f-h', 'start')
    b += '<path d="M470 296 L470 186 C474 166 520 158 610 150" class="f-cut" style="stroke-width:3"/>'
    b += '<path d="M245 168 L305 168" class="f-cut" style="stroke-width:3"/>'
    b += arrow(536, 250, 478, 250) + T(542, 240, ['1. Main PA, lengthwise,', 'from 1 to 2 cm above', 'the valve'], '', 'start')
    b += arrow(580, 84, 570, 146) + T(500, 50, ['2. Extend onto the left PA towards', 'the pericardial reflection'], 'f-s', 'start')
    b += arrow(120, 236, 268, 176) + T(12, 254, ['3. Separate right PA', 'incision between', 'SVC and aorta'], 'f-s', 'start')
    b += T(496, 314, ['Valve level: the conal branches of', 'the right coronary are the landmark'], 'f-s', 'start')
    b += box(10, 370, 700, 74, ['Then: forceps and suction · open both pleurae and compress the lungs to deliver distal clot',
                                'Retrograde flush through the pulmonary veins needs a cross-clamp and cardioplegia',
                                'Patent foramen ovale: cross-clamp and cardioplegia to avoid air embolism · patch rarely needed'], 'b0', 'f-s')
    return svg(454, b)


def f11_cteph_types():
    cols = [(150, 'Main and branch PA', 'Type I', 'Visible clot in the main or branch PA', 'ok'),
            (320, 'Lobar', 'Type II', 'Organised thrombus in the lobar branches; commonest, 40 to 70%', 'ok'),
            (490, 'Segmental', 'Type III', 'Obstruction at segmental level', 'b1'),
            (640, 'Subsegmental', 'Type IV', 'Subsegmental branches only', 'warn')]
    b = ''
    for i, (x, lev, ty, desc, c) in enumerate(cols):
        x0 = [60, 230, 400, 570][i]
        w = [170, 170, 170, 140][i]
        b += f'<rect x="{x0}" y="6" width="{w - 4}" height="44" rx="8" class="f-{c}"/>'
        b += T(x0 + (w - 4) / 2, 24, ty, 'f-h') + T(x0 + (w - 4) / 2, 42, lev, 'f-s')
    # vessel tree
    b += '<path d="M20 180 L150 180" class="f-vessel" style="stroke-width:26"/>'
    for y1 in (110, 250):
        b += f'<path d="M150 180 C190 180 210 {y1} 320 {y1}" class="f-vessel" style="stroke-width:16"/>'
        for y2 in (y1 - 36, y1 + 36):
            b += f'<path d="M320 {y1} C360 {y1} 380 {y2} 490 {y2}" class="f-vessel" style="stroke-width:9"/>'
            for y3 in (y2 - 14, y2 + 14):
                b += f'<path d="M490 {y2} C520 {y2} 540 {y3} 640 {y3}" class="f-vessel" style="stroke-width:4"/>'
    for x in (230, 400, 570):
        b += line(x, 54, x, 300, 'f-dash')
    b += T(20, 330, 'Description of each type as TSRA Review ch. 82 gives it:', 'f-s', 'start')
    y = 352
    for x, lev, ty, desc, c in cols:
        b += T(20, y, f'{ty}: {desc}', 'f-s', 'start')
        y += 18
    b += box(10, y + 6, 700, 58, ['TSRA criteria for endarterectomy: NYHA III to IV · PVR over 300 dyn·s·cm⁻⁵', 'surgically accessible disease (main to subsegmental) · comorbidity not prohibitive'], 'b0', 'f-s')
    return svg(y + 74, b)


# ---- figs_F12.py
"""F12 drawings: sternal wound infection, sternal fixation, descending necrotising mediastinitis."""



def f12_el_oakley():
    """El Oakley and Wright classification as a grid: time of presentation by risk factors."""
    b = T(12, 22, 'El Oakley and Wright: when it presents, and whether risk factors are present', 'f-h', 'start')
    x0, xs = 170, [170, 330, 490, 700]
    for x, lab in [(170, 'Operation'), (330, '2 weeks'), (490, '6 weeks')]:
        b += line(x, 44, x, 214, 'f-grid') + T(x, 40, lab, 'f-s')
    b += T(600, 40, 'later', 'f-s')
    b += T(160, 92, ['No risk', 'factors'], 'f-h', 'end')
    b += T(160, 166, ['1 or more', 'risk factors'], 'f-h', 'end')
    b += box(174, 58, 152, 66, ['Type I', 'within 2 weeks'], 'ok')
    b += box(334, 58, 152, 66, ['Type II', '2 to 6 weeks'], 'b0')
    b += box(174, 134, 152, 66, ['Type IIIA', 'as I, with risk'], 'warn')
    b += box(334, 134, 152, 66, ['Type IIIB', 'as II, with risk'], 'warn')
    b += box(494, 58, 206, 142, ['Type V', 'first presents', 'after 6 weeks'], 'b1')
    b += box(10, 222, 345, 50, ['Type IVA: I, II or III after one', 'failed therapeutic trial'], 'warn')
    b += box(365, 222, 345, 50, ['Type IVB: I, II or III after more', 'than one failed therapeutic trial'], 'warn')
    b += T(360, 296, 'Risk factors: diabetes, obesity, immunosuppression. A failed trial is any operation meant to treat it.', 'f-s')
    return svg(308, b)


def f12_dswi_path():
    """Management pathway for deep sternal wound infection."""
    b = box(190, 8, 340, 48, ['Suspected DSWI: pain on coughing, discharge,', 'sternal click, fever'], 'b1')
    b += arrow(360, 56, 360, 76)
    b += box(150, 78, 420, 44, 'CT chest, cultures, broad antibiotics, glucose control', 'b0')
    b += arrow(290, 122, 180, 150) + arrow(430, 122, 540, 150)
    b += box(10, 152, 330, 58, ['Sternum stable, no exposed bone or wire:', 'open, debride, NPWT'], 'b0')
    b += box(380, 152, 330, 58, ['Unstable sternum or exposed bone or wire:', 'theatre, remove wires, debride'], 'warn')
    b += arrow(500, 210, 470, 238) + arrow(600, 210, 620, 238)
    b += box(300, 240, 230, 66, ['Early dehiscence,', 'healthy bone: rewire', '(pectoral advancement)'], 'ok')
    b += box(540, 240, 170, 66, ['Infected, bone', 'loss: NPWT', 'bridge'], 'warn')
    b += arrow(175, 210, 175, 330) + arrow(625, 306, 625, 330)
    b += box(10, 332, 700, 58, ['Theatre dressing changes every 2 to 4 days until clean, then delayed closure:',
                               'rewire or plate if bone allows; otherwise pectoralis, rectus, omentum or latissimus'], 'b0')
    b += T(360, 412, 'Restabilise the sternum: sharp edges under suction can tear the right ventricle.', 'f-s')
    return svg(424, b)


def f12_flaps():
    """Front-of-chest sketch of the flaps used to close a sternal wound."""
    b = '<path d="M210 40 C260 20 460 20 510 40 L560 120 L540 330 L180 330 L160 120 Z" class="f-track"/>'
    b += '<rect x="344" y="44" width="32" height="190" rx="10" class="f-b1"/>'
    b += arrow(300, 30, 340, 50) + T(296, 30, 'Sternum', 'f-s', 'end')
    # pectoralis major fans
    b += '<path d="M180 70 L340 56 L340 200 L200 150 Z" class="f-b0"/>'
    b += '<path d="M540 70 L380 56 L380 200 L520 150 Z" class="f-b0"/>'
    b += T(258, 112, ['Pectoralis', 'major'], 'f-s') + T(462, 112, ['Pectoralis', 'major'], 'f-s')
    # rectus abdominis
    b += '<rect x="300" y="240" width="40" height="88" rx="6" class="f-ok"/>'
    b += '<rect x="380" y="240" width="40" height="88" rx="6" class="f-ok"/>'
    # omentum
    b += '<path d="M430 300 C470 300 500 310 510 326" class="f-dash"/>' + T(470, 348, 'omentum (from below)', 'f-s')
    # latissimus behind
    b += '<path d="M160 130 C130 200 140 280 180 320" class="f-dash"/>'
    b += T(20, 30, 'Choice by level of the defect', 'f-h', 'start')
    b += arrow(610, 90, 520, 110) + T(616, 70, ['Pectoralis: upper', 'and middle; the', 'workhorse. Lower', 'third may need the', 'insertion divided'], 'f-s', 'start')
    b += arrow(612, 250, 424, 284) + T(616, 232, ['Rectus: lower', 'third; usually the', 'side opposite the', 'LIMA'], 'f-s', 'start')
    b += arrow(612, 318, 512, 326) + T(616, 318, ['Omentum: any', 'level, fills dead', 'space, resists', 'infection'], 'f-s', 'start')
    b += arrow(110, 230, 150, 230) + T(104, 214, ['Latissimus', '(on the back):', 'bulk for massive', 'loss'], 'f-s', 'end')
    return svg(400, b)


def f12_npwt():
    """Mortality with NPWT against conventional treatment in comparative series."""
    items = [('Petzina 2010, NPWT (n=69)', 5.8, 'ok'), ('Petzina 2010, conventional (n=49)', 24.5, 'warn'),
             ('Deniz 2012, NPWT (n=47)', 8.5, 'ok'), ('Deniz 2012, conventional (n=43)', 23.2, 'warn'),
             ('Matched series, NPWT (n=22)', 5, 'ok'), ('Matched series, conventional (n=22)', 36, 'warn')]
    h, b = bars(items, '%', 40, 'Death after mediastinitis: lower with NPWT in non-randomised series', lab_w=290)
    b += T(360, h + 4, 'In-hospital (Petzina, matched series) or 90-day (Deniz). No randomised trial exists.', 'f-s')
    return svg(h + 18, b)


def f12_plates():
    """Allen RCT: CT union and sternal complications with plates against wires."""
    items = [('Union at 3 months, plates', 41, 'ok'), ('Union at 3 months, wires', 16, 'b1'),
             ('Union at 6 months, plates', 80, 'ok'), ('Union at 6 months, wires', 67, 'b1'),
             ('Sternal complications, plates', 0, 'ok'), ('Sternal complications, wires', 5, 'warn')]
    h, b = bars(items, '%', 100, 'Rigid plates healed the sternum sooner than wires (RCT, 236 patients)', lab_w=270)
    return svg(h, b)


def f12_endo():
    """Sagittal sketch of the mediastinum with the Endo and Sugio-Okamoto extents."""
    b = T(12, 22, 'Descending necrotising mediastinitis: extent sets the drainage', 'f-h', 'start')
    # outline: neck and mediastinum, sagittal, anterior on the left
    b += '<rect x="60" y="150" width="130" height="190" rx="8" class="f-warn"/>'   # lower anterior
    b += '<rect x="200" y="150" width="130" height="190" rx="8" class="f-b0"/>'    # lower posterior
    b += '<rect x="60" y="60" width="270" height="82" rx="8" class="f-ok"/>'       # above carina
    b += line(50, 146, 340, 146, 'f-cut') + T(345, 150, 'Carina', 'f-s', 'start')
    b += T(195, 92, 'Type I: above the carina', 'f-h') + T(195, 112, 'cervical or VATS drainage', 'f-s')
    b += T(125, 236, ['Lower', 'anterior'], 'f-h') + T(265, 236, ['Lower', 'posterior'], 'f-h')
    b += T(60, 360, 'Front', 'f-s', 'start') + T(330, 360, 'Back', 'f-s', 'end')
    # routes from neck
    b += arrow(100, 36, 100, 58) + T(108, 46, 'pretracheal', 'f-s', 'start')
    b += arrow(290, 36, 290, 58) + T(282, 46, 'retrovisceral', 'f-s', 'end')
    # legend boxes on right
    b += box(400, 60, 310, 56, ['IIA: lower anterior', 'subxiphoid plus neck, VATS or thoracotomy'], 'warn')
    b += box(400, 126, 310, 56, ['IIB: lower anterior and posterior', 'thoracotomy or VATS'], 'b1')
    b += box(400, 192, 310, 56, ['IIC (Sugio-Okamoto): lower', 'posterior only; reached via retrovisceral'], 'b0')
    b += box(400, 258, 310, 84, ['All types: open the neck, broad', 'antibiotics with anaerobic cover,', 'repeat CT; spread below the carina', 'raises odds of 90-day death (OR 4.6)'], 'b1')
    return svg(374, b)


# ---- figs_F13.py



def f13_ng122_timeline():
    """NICE NG122 version history, from the guideline's update information (read 21 November 2026)."""
    b = T(12, 22, 'NICE NG122: what changed, and when', 'f-h', 'start')
    b += line(30, 76, 700, 76)
    pts = [
        (82, 'Mar 2019', ['Replaces CG121;', 'new: nodes, brain', 'imaging, stage 3a N2'], 'b1'),
        (214, 'Aug 2022', ['Drug advice moved', 'into treatment', 'pathways'], 'b1'),
        (346, '2022 to 2023', ['Pathways updated', 'as appraisals', 'publish'], 'b1'),
        (478, 'Mar 2024', ['Exon 20 insertion', 'pathways removed', '(the notes\' text)'], 'b0'),
        (624, 'Feb 2026', ['1.2.12 now NGS', 'panels; appraisal', 'links; general care', 'advice removed'], 'warn'),
    ]
    for x, d, lines_, cls in pts:
        b += f'<circle cx="{x}" cy="76" r="7" class="f-{cls}"/>'
        b += T(x, 60, d, 'f-h')
        b += box(x - 64, 92, 128, 86, lines_, cls, 'f-s')
    b += T(360, 204, 'Lobectomy (1.5.1), staging (1.2.19 to 1.2.22) and fitness (1.4) carry no 2024 or 2026 amendment tag', 'f-s')
    return svg(218, b)


def f13_ng122_periop():
    """NG122 section 1.6 as linked in the February 2026 text."""
    b = T(12, 22, 'NG122 (Feb 2026): drug options around resection, by timing', 'f-h', 'start')
    # columns
    cols = [(10, 'Before surgery'), (250, 'Before and after'), (490, 'After surgery')]
    for x, h in cols:
        b += box(x, 38, 220, 32, h, 'b1', 'f-h')
    b += box(10, 82, 220, 92, ['Nivolumab + chemotherapy', 'tumour 4 cm or more', 'or node positive', 'TA876 (1.6.8)'], 'b0')
    b += box(250, 82, 220, 92, ['Durvalumab (TA1030, 1.6.9)', 'no EGFR or ALK alteration', 'Pembrolizumab (TA1017, 1.6.10)', 'high recurrence risk'], 'b0')
    b += box(490, 82, 220, 92, ['Platinum doublet: offer N1 to 2', 'consider N0 over 4 cm', 'PS 0 to 1 (1.6.11 to 1.6.13)'], 'b0')
    b += box(490, 184, 220, 70, ['Osimertinib 3 years: EGFR', 'ex19del or L858R, 1b to 3a', 'TA1043 (1.6.14)'], 'ok')
    b += box(490, 264, 220, 70, ['Alectinib: ALK positive', '1b (4 cm or more) to 3a', 'TA1014 (1.6.15)'], 'ok')
    b += box(490, 344, 220, 70, ['After platinum, high risk:', 'atezolizumab TA1071,', 'pembrolizumab TA1037 (1.6.16)'], 'b1')
    b += box(10, 184, 460, 70, ['Test EGFR and ALK before choosing a chemo-immunotherapy route:', 'an EGFR or ALK-driven tumour goes to the targeted adjuvant boxes'], 'warn')
    b += arrow(470, 219, 488, 219) + arrow(470, 230, 488, 290)
    b += box(10, 264, 460, 70, ['Not resectable: chemoradiotherapy (1.6.17), then durvalumab', 'if PD-L1 1% or more and no progression (TA798, 1.6.18)'], 'b1')
    b += T(240, 372, ['Not linked in the guideline text read:', 'perioperative nivolumab TA1127 and', 'osimertinib after chemoradiotherapy TA1156', '(both named elsewhere in the notes)'], 'f-s')
    return svg(424, b)


def f13_staging_compare():
    """Mediastinal staging: NICE NG122 (read 21 Nov 2026) against ERS/ESGE/ESTS 2026 (abstract, as in the notes)."""
    b = box(230, 10, 260, 48, ['Curative treatment possible;', 'CT then PET-CT done'], 'b1', 'f-h')
    b += arrow(360, 58, 360, 80)
    b += box(150, 82, 420, 50, ['Nodes 10 mm or more, or PET-positive, and nodal', 'status changes treatment: tissue needed'], 'b0')
    b += arrow(360, 132, 360, 154)
    b += box(150, 156, 420, 50, ['Endosonography first: EBUS-TBNA, EUS-FNA or both', '(NICE 1.2.20 to 1.2.21; European 2026 the same)'], 'ok')
    b += arrow(360, 206, 360, 228)
    b += box(230, 230, 260, 40, 'Systematic sampling negative', 'b1', 'f-h')
    b += arrow(300, 270, 190, 300) + arrow(420, 270, 530, 300)
    b += box(10, 302, 340, 80, ['NICE NG122 (1.2.22)', 'Consider surgical staging if suspicion', 'stays high and it would change treatment'], 'warn')
    b += box(370, 302, 340, 80, ['ERS/ESGE/ESTS 2026', 'Confirmatory mediastinoscopy not', 'recommended after negative systematic EBUS/EUS'], 'b0')
    b += T(360, 404, 'A technically inadequate or incomplete negative is not N0 under either document', 'f-s')
    return svg(416, b)


def f13_palliative():
    """NG122 sections 1.13 to 1.19: problem to recommended intervention."""
    rows = [
        ('Impending airway obstruction', 'RT and/or debulking or stent; rapid-access team', '1.14.1 to 1.14.3'),
        ('Pleural effusion', 'Aspirate or drain; talc pleurodesis for lasting relief', '1.15.1 to 1.15.2'),
        ('Breathlessness', 'Non-drug: breathing control, coping, psychology', '1.15.3 to 1.15.4'),
        ('Cough', 'Consider opioid: codeine or morphine', '1.15.5'),
        ('Hoarseness (RLN palsy)', 'Refer to ENT for advice', '1.15.6'),
        ('SVC obstruction', 'Chemo-RT by stage and PS; stent if severe or failed', '1.15.7 to 1.15.8'),
        ('Brain metastases', 'Dexamethasone, lowest effective dose; then NG99', '1.16.1 to 1.16.2'),
        ('Painful bone metastasis', 'Single-fraction RT; denosumab per TA265; NG234', '1.17.1 to 1.17.2'),
        ('Weight, appetite, swallowing, low mood', 'MDT with supportive and palliative care', '1.18.1'),
    ]
    b = T(12, 22, 'NG122 palliative recommendations: problem, action, number', 'f-h', 'start')
    y = 36
    for p, a, n in rows:
        b += box(10, y, 236, 34, p, 'b1', 'f-s')
        b += arrow(248, y + 17, 262, y + 17)
        b += box(264, y, 336, 34, a, 'b0', 'f-s')
        b += T(608, y + 22, n, 'f-n', 'start')
        y += 42
    b += box(10, y + 4, 700, 40, ['All alongside: palliative radiotherapy when symptoms arise or at once (1.13.1);',
                                    'clinical nurse specialist at every stage (1.1.1)'], 'ok', 'f-s')
    return svg(y + 56, b)


# ---- figs_F14.py



def _f14_torso(ox, anast, cuts):
    """One anterior-view torso panel. anast: 'chest' or 'neck'. cuts: list of 'abdo', 'rchest', 'lneck'."""
    cx = ox + 115
    b = f'<rect x="{cx - 26}" y="34" width="52" height="40" rx="10" class="f-b0"/>'
    b += f'<rect x="{ox + 20}" y="66" width="190" height="250" rx="44" class="f-b0"/>'
    # diaphragm
    b += f'<path d="M{ox + 26} 222 C{ox + 70} 192 {ox + 160} 192 {ox + 204} 222" class="f-dash"/>'
    # residual oesophagus (above anastomosis) and gastric conduit (below)
    ay = 118 if anast == 'chest' else 56
    b += f'<rect x="{cx - 6}" y="36" width="12" height="{ay - 36}" rx="5" class="f-lumen"/>'
    b += f'<rect x="{cx - 9}" y="{ay}" width="18" height="{214 - ay}" rx="7" class="f-b1"/>'
    b += f'<path d="M{cx - 9} 212 C{cx - 30} 236 {cx - 20} 270 {cx + 10} 272 C{cx + 40} 272 {cx + 36} 236 {cx + 9} 212 Z" class="f-b1"/>'
    b += f'<circle cx="{cx}" cy="{ay}" r="7" class="f-warn"/>'
    if 'abdo' in cuts:
        b += line(cx + 44, 236, cx + 44, 300, 'f-cut')
    if 'rchest' in cuts:
        b += f'<path d="M{ox + 26} 168 C{ox + 40} 150 {ox + 62} 140 {ox + 84} 136" class="f-cut"/>'
    if 'lneck' in cuts:
        b += line(cx + 22, 40, cx + 34, 72, 'f-cut')
    b += T(ox + 34, 92, 'R', 'f-s') + T(ox + 196, 92, 'L', 'f-s')
    return b


def f14_oesophagectomy_approaches():
    spec = [
        (0, 'Ivor Lewis', 'chest', ['abdo', 'rchest'],
         ['Abdomen + right chest', 'Anastomosis in the chest', 'Lower and middle third', 'Leak 11% (harder to control)']),
        (245, 'McKeown (three-hole)', 'neck', ['abdo', 'rchest', 'lneck'],
         ['Abdomen + right chest + neck', 'Anastomosis in the neck', 'Upper thoracic tumours', 'Fullest lymphadenectomy']),
        (490, 'Transhiatal', 'neck', ['abdo', 'lneck'],
         ['Abdomen + left neck', 'No thoracotomy', 'Distal third and GOJ', 'Blunt, blind mediastinal step']),
    ]
    b = ''
    for ox, title, anast, cuts, notes in spec:
        b += T(ox + 115, 22, title, 'f-h')
        b += _f14_torso(ox, anast, cuts)
        b += box(ox + 10, 330, 210, 82, notes, 'b0')
    b += T(360, 436, 'Red line: incision.  Amber ring: anastomosis.  Shaded tube: gastric conduit on the right gastroepiploic artery.', 'f-s')
    b += T(360, 454, 'Cervical leak 19% against intrathoracic 11%, but intrathoracic leak carries three times the mortality (TSRA ch. 31).', 'f-s')
    return svg(466, b)


def f14_ng83_pathway():
    b = box(110, 8, 500, 52, ['Oesophageal or GOJ cancer: specialist OG MDT', 'FDG PET-CT if fit for radical treatment (not for T1a)'], 'b1', 'f-h')
    b += arrow(220, 60, 120, 88) + arrow(360, 60, 360, 88) + arrow(500, 60, 600, 88)
    b += box(10, 90, 220, 96, ['Suspected T1N0', 'EMR for staging', 'T1bN0 SCC: definitive CRT', 'or surgery (shared choice)'], 'b0')
    b += box(250, 90, 220, 96, ['Resectable SCC', 'Choice: radical CRT, or', 'CRT then surgery'], 'b0')
    b += box(490, 90, 220, 96, ['Localised adenocarcinoma', '(not T1N0): chemo before,', 'chemo before and after,', 'or CRT before surgery'], 'b0')
    b += arrow(360, 186, 360, 208) + arrow(600, 186, 500, 208) + arrow(120, 186, 230, 208)
    b += box(120, 210, 480, 40, 'After neoadjuvant treatment: reassess response, reconsider surgery', 'b1')
    b += arrow(360, 250, 360, 272)
    b += box(110, 274, 500, 56, ['Surgery in a specialist unit by OG surgeons', 'Open or minimally invasive (incl. hybrid); consider two-field nodes'], 'ok')
    b += arrow(360, 330, 360, 352)
    b += box(70, 354, 580, 40, 'Residual disease after neoadjuvant CRT, complete resection: nivolumab (TA746)', 'warn')
    b += arrow(360, 394, 360, 416)
    b += box(110, 418, 500, 56, ['Follow-up: symptoms to watch for and rapid MDT access', 'No routine clinical or radiological surveillance for recurrence'], 'b0')
    return svg(484, b)


def f14_esopec():
    h, b = bars([('FLOT: 3-year overall survival', 57.4, 'ok'),
                 ('CROSS: 3-year overall survival', 50.7, 'b1'),
                 ('FLOT: 3-year progression-free', 51.6, 'ok'),
                 ('CROSS: 3-year progression-free', 35.0, 'b1')],
                '%', 70, 'ESOPEC (n=438): FLOT beat CROSS, death HR 0.70 (0.53 to 0.92)', lab_w=270)
    b += T(360, h + 8, 'Median survival 66 against 37 months; 90-day postoperative mortality 3.1% against 5.6% (Hoeppner, NEJM 2025).', 'f-s')
    return svg(h + 20, b)


def f14_sano():
    b = box(10, 10, 200, 46, ['Neoadjuvant CRT', '(12 Dutch hospitals)'], 'b0')
    b += arrow(210, 33, 250, 33)
    b += box(252, 10, 216, 46, ['Clinical complete', 'response (n=309)'], 'b1', 'f-h')
    b += arrow(468, 33, 508, 33)
    b += box(510, 10, 200, 46, ['Stepped-wedge cluster', 'randomisation by hospital'], 'b0')
    b += arrow(560, 56, 440, 86) + arrow(660, 56, 660, 86)
    b += box(230, 88, 326, 92, ['Active surveillance (n=198)', 'Response checks every 3 months in year 1,', '4 in year 2, 6 in year 3, then yearly', 'Surgery only for locoregional regrowth'], 'ok')
    b += box(570, 88, 140, 92, ['Standard', 'oesophagectomy', '(n=111)'], 'b1')
    h, ch = bars([('Active surveillance', 74, 'ok'), ('Standard surgery', 71, 'b1')], '%', 100,
                 '2-year overall survival (modified ITT): non-inferior', lab_w=200)
    b += f'<g transform="translate(0,190)">{ch}</g>'
    b += T(360, 190 + h + 8, 'HR 1.14 (0.74 to 1.78); median DFS 35 against 49 months; 74 to 76% adenocarcinoma (van der Wilk, Lancet Oncol 2025).', 'f-s')
    return svg(190 + h + 20, b)


def f14_trial_results():
    out = ''
    y = 0
    for items, unit, vmax, title in [
        ([('Nivolumab', 22.4, 'ok'), ('Placebo', 11.0, 'b1')], ' months', 30,
         'CheckMate 577: median DFS doubled (HR 0.69); OS gain not significant'),
        ([('Nivolumab', 51.7, 'ok'), ('Placebo', 35.3, 'b1')], ' months', 60,
         'CheckMate 577 final OS: HR 0.85 (0.70 to 1.04), p=0.11'),
        ([('Robot-assisted MIE', 69.4, 'ok'), ('Thoracoscopic MIE', 56.2, 'b1')], '%', 80,
         'RAMIE: 5-year overall survival, non-inferior (HR 0.71)'),
    ]:
        h, b = bars(items, unit, vmax, title, lab_w=200)
        out += f'<g transform="translate(0,{y})">{b}</g>'
        y += h + 4
    out += T(360, y + 8, 'Kelly NEJM 2021 and ASCO 2025 abstract 4000; RAMIE, Lancet Gastroenterol Hepatol 2026 (superiority exploratory).', 'f-s')
    return svg(y + 20, out)


# ---- figs_F15.py



def f15_la_doses():
    h, b = bars([('Lidocaine, plain', 3, 'b1'), ('Lidocaine with adrenaline', 7, 'ok'),
                 ('Prilocaine, plain', 6, 'b1'), ('Prilocaine with adrenaline', 8, 'ok'),
                 ('Ropivacaine (either)', 3, 'b1'),
                 ('Bupivacaine (either)', 2, 'warn'), ('Levobupivacaine (either)', 2, 'warn')],
                ' mg/kg', 9, 'Maximum dose: bupivacaine allows least, and adrenaline does not raise it', 260)
    b += T(12, h + 4, 'Adrenaline raises the limit for lidocaine and prilocaine only. Doses are additive across agents.', 'f-s', 'start')
    return svg(h + 16, b)


def f15_last_lipid():
    b = T(12, 20, 'Lipid emulsion 20% (propofol is not a substitute)', 'f-h', 'start')
    b += line(40, 62, 690, 62)
    for x, lab in [(40, '0 min'), (300, '5 min'), (560, '10 min')]:
        b += line(x, 56, x, 68) + T(x, 50, lab, 'f-s')
    b += box(10, 80, 240, 78, ['Bolus 1.5 ml/kg over 2 to 3 min', '(about 100 ml at 70 kg)', 'Start infusion 15 ml/kg/h'], 'b0', 'f-s')
    b += box(260, 80, 220, 78, ['Not restored or worse:', 'repeat bolus', 'Infusion may double', 'to 30 ml/kg/h'], 'b0', 'f-s')
    b += box(490, 80, 220, 78, ['Still not restored:', 'third and last bolus'], 'b0', 'f-s')
    b += box(10, 170, 700, 34, 'Do not exceed 12 ml/kg in total (about 840 ml at 70 kg)', 'warn', 'f-h')
    b += box(10, 216, 345, 96, ['Cardiac arrest: standard CPR plus lipid', 'Adrenaline 1 microgram/kg or less', 'Avoid vasopressin', 'Recovery may take over an hour; consider bypass'], 'warn', 'f-s')
    b += box(365, 216, 345, 96, ['No arrest: treat hypotension and', 'arrhythmia conventionally; consider lipid', 'Seizures: small doses of benzodiazepine', 'Afterwards: daily amylase or lipase'], 'b1', 'f-s')
    return svg(322, b)


def f15_skinprep():
    b = box(250, 8, 220, 40, 'Skin preparation', 'b1', 'f-h')
    b += arrow(310, 48, 160, 78) + arrow(410, 48, 560, 78)
    b += box(30, 80, 260, 44, 'Chlorhexidine suitable', 'b0') + box(430, 80, 260, 44, 'Chlorhexidine contraindicated', 'b0')
    b += arrow(110, 124, 90, 154) + arrow(210, 124, 230, 154) + arrow(510, 124, 490, 154) + arrow(610, 124, 630, 154)
    b += T(92, 144, 'usual site', 'f-s', 'end') + T(230, 144, 'mucous membrane', 'f-s', 'start')
    b += T(492, 144, 'alcohol suitable', 'f-s', 'end') + T(632, 144, 'no alcohol', 'f-s', 'start')
    b += box(10, 156, 165, 62, ['Alcoholic', 'chlorhexidine', 'First choice'], 'ok', 'f-s')
    b += box(185, 156, 165, 62, ['Aqueous', 'chlorhexidine'], 'b0', 'f-s')
    b += box(370, 156, 165, 62, ['Alcoholic', 'povidone-iodine'], 'b0', 'f-s')
    b += box(545, 156, 165, 62, ['Aqueous', 'povidone-iodine'], 'b0', 'f-s')
    b += box(10, 232, 700, 40, 'With diathermy: let the preparation dry by evaporation; do not let alcohol pool', 'warn', 'f-s')
    return svg(282, b)


def f15_prospect():
    rows = [('First choice', 'Paravertebral block', 'Single shot A · continuous A', 'ok'),
            ('Alternative', 'Erector spinae plane block', 'Single shot A · continuous B', 'ok'),
            ('Second choice', 'Serratus anterior plane block', 'Single shot A · continuous D', 'b0'),
            ('Not recommended', 'Thoracic epidural', 'Less invasive blocks are non-inferior', 'warn'),
            ('Not recommended', 'Intercostal, intrapleural, wound infiltration', 'Little procedure-specific evidence', 'warn')]
    b = T(12, 20, 'Regional analgesia for VATS (PROSPECT, grade of recommendation)', 'f-h', 'start')
    for i, (tier, name, grade, c) in enumerate(rows):
        y = 34 + i * 46
        b += box(10, y, 160, 38, tier, c, 'f-s')
        b += box(180, y, 300, 38, name, 'b1', 'f-s')
        b += T(492, y + 24, grade, 'f-s', 'start')
    y = 34 + 5 * 46 + 4
    b += box(10, y, 700, 40, 'With every block: paracetamol and an NSAID or COX-2 inhibitor (D); opioids for rescue only (D)', 'b0', 'f-s')
    return svg(y + 50, b)


def f15_lvr_pathway():
    b = box(200, 8, 320, 40, 'COPD: pulmonary rehabilitation completed', 'b1', 'f-h')
    b += arrow(360, 48, 360, 70)
    b += box(120, 72, 480, 62, ['Respiratory review for lung volume reduction', 'FEV1 under 50%, not smoking, walks 140 m or more in 6 min,', 'breathlessness that limits quality of life'], 'b0', 'f-s')
    b += arrow(360, 134, 360, 156)
    b += box(120, 158, 480, 62, ['Refer to the lung volume reduction MDT', 'Hyperinflation on plethysmography · emphysema on', 'unenhanced CT · other illness optimised'], 'b0', 'f-s')
    b += arrow(250, 220, 150, 248) + arrow(360, 220, 360, 248) + arrow(470, 220, 570, 248)
    b += box(20, 250, 210, 52, ['Lung volume', 'reduction surgery'], 'ok', 'f-s')
    b += box(255, 250, 210, 52, ['Endobronchial valves', '(no collateral ventilation)'], 'ok', 'f-s')
    b += box(490, 250, 210, 52, ['Coils: only in a', 'clinical trial'], 'warn', 'f-s')
    b += box(20, 318, 330, 52, ['Breathless with a bulla of a third of the', 'hemithorax or more: bullectomy assessment'], 'b1', 'f-s')
    b += box(370, 318, 330, 52, ['Transplant referral: earlier lung volume', 'reduction does not rule it out'], 'b1', 'f-s')
    return svg(380, b)


def f15_nett():
    h1, b1 = bars([('Surgery', 15, 'ok'), ('Medical therapy', 3, 'b1')], '%', 50,
                  'NETT at 24 months: exercise capacity improved in 15% against 3%', 200)
    h2, b2 = bars([('Surgery', 33, 'ok'), ('Medical therapy', 9, 'b1')], '%', 50,
                  'Quality of life improved in 33% against 9%', 200)
    b3 = T(12, h1 + h2 + 6, 'Overall mortality did not differ (risk ratio 1.01). 1,218 randomised.', 'f-s', 'start')
    return svg(h1 + h2 + 20, b1 + f'<g transform="translate(0 {h1})">{b2}</g>' + b3)


# ---- figs_F16.py


_f16_ST = 'fill="none" style="stroke-width:3.5px;stroke-linecap:round"'


def f16_ross_steps():
    b = ''
    # pulmonary root (left) and aortic root (right) as cylinders
    def root(x, y, w, h, lab, cls):
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="f-{cls}"/>'
        cy = y + h - 34
        for k in range(3):
            x0 = x + 8 + k * (w - 16) / 3
            x1 = x0 + (w - 16) / 3
            s += f'<path d="M{x0} {cy - 18} Q{(x0 + x1) / 2} {cy + 14} {x1} {cy - 18}" class="f-l" {_f16_ST}/>'
        s += T(x + w / 2, y - 8, lab, 'f-h')
        return s
    b += root(30, 40, 100, 150, 'Pulmonary root', 'b0')
    b += root(200, 40, 100, 150, 'Aortic root', 'b1')
    b += line(20, 182, 140, 182, 'f-cut') + T(80, 204, 'Cut about 5 mm below', 'f-s') + T(80, 220, 'the pulmonary cusps', 'f-s')
    b += '<circle cx="230" cy="122" r="9" class="f-lumen"/><circle cx="272" cy="122" r="9" class="f-lumen"/>'
    b += T(250, 212, 'Coronary buttons', 'f-s')
    b += '<path d="M130 70 C160 30 175 30 200 60" class="f-l" fill="none" marker-end="url(#ah)"/>'
    b += T(165, 26, 'Autograft', 'f-s')
    b += box(30, 240, 270, 50, ['Pulmonary homograft (or xenograft)', 'rebuilds the RV outflow tract'], 'ok', 'f-s')
    b += arrow(80, 228, 80, 240)
    steps = [
        ('1', 'Check the pulmonary valve: reject large fenestrations,', 'retraction or marked asymmetry'),
        ('2', 'Harvest the autograft; keep 2 to 3 mm of muscle; mind the', 'left main, LAD and first septal branch'),
        ('3', 'Excise the aortic valve; mobilise both coronary buttons', 'annuloplasty if AR or annulus 27 mm or more'),
        ('4', 'Sew the autograft into the LVOT, commissures at 120 degrees;', 'R-NC commissure slightly higher (conduction)'),
        ('5', 'Reimplant buttons; homograft to RVOT; distal suture line at', 'autograft STJ, graft if ascending is large'),
    ]
    y = 30
    for n, a, c in steps:
        b += f'<circle cx="345" cy="{y + 12}" r="12" class="f-b0"/>' + T(345, y + 17, n, 'f-n')
        b += T(366, y + 9, a, 'f-s', 'start') + T(366, y + 26, c, 'f-s', 'start')
        y += 52
    return svg(304, b)


def f16_ross_freedom():
    h, b = bars([('5 years', 97, 'ok'), ('15 years', 90, 'ok'), ('20 years', 84, 'b0'), ('25 years', 70, 'warn')],
                '%', 100, 'German Ross Registry (n=2,444): freedom from autograft reintervention', lab_w=150)
    b += T(12, h + 6, 'Linearised autograft reintervention 0.69% per patient-year; any Ross reintervention 84.7% free at 15 years', 'f-s', 'start')
    return svg(h + 20, b)


def _f16_root(cx, y0, asc, j, s, a, cls='f-vessel'):
    """Side profile of an aortic root; returns path plus annulus/coaptation y."""
    ys, yj, yb = y0, y0 + 40, y0 + 118
    p = (f'<path d="M{cx - asc} {ys} L{cx - j} {yj} C{cx - s - 6} {yj + 20} {cx - s - 6} {yb - 30} {cx - a} {yb}" class="f-l" fill="none"/>'
         f'<path d="M{cx + asc} {ys} L{cx + j} {yj} C{cx + s + 6} {yj + 20} {cx + s + 6} {yb - 30} {cx + a} {yb}" class="f-l" fill="none"/>')
    return p, yb


def f16_ar_classes():
    spec = [('Ia', 'STJ and ascending', 36, 38, 30, 20, 'gap', ['STJ remodelling or', 'ascending graft'], 'b0'),
            ('Ib', 'Sinuses and STJ', 22, 34, 44, 20, 'gap', ['Valve-sparing', 'root replacement'], 'b0'),
            ('Ic', 'Annulus', 20, 22, 32, 34, 'gap', ['Circumferential', 'annuloplasty'], 'b0'),
            ('Id', 'Perforation', 20, 22, 30, 20, 'hole', ['Pericardial patch;', 'annuloplasty'], 'b0'),
            ('II', 'Prolapse', 20, 22, 30, 20, 'prolapse', ['Central plication;', 'free-margin', 'support'], 'warn'),
            ('III', 'Restriction', 20, 22, 30, 20, 'restrict', ['Shave, decalcify,', 'patch; often', 'replaced'], 'b1')]
    b = T(12, 20, 'Repair-oriented functional classification of aortic regurgitation', 'f-h', 'start')
    w = 110
    for i, (n, lab, asc, j, s, a, mode, rep, cls) in enumerate(spec):
        x = 10 + i * (w + 8)
        cx = x + w / 2
        b += f'<rect x="{x}" y="32" width="{w}" height="270" rx="10" class="f-{cls}"/>'
        b += T(cx, 54, 'Type ' + n, 'f-h') + T(cx, 72, lab, 'f-s')
        p, yb = _f16_root(cx, 86, asc, j, s, a)
        b += p
        if mode == 'gap':
            gx = 7
            b += f'<path d="M{cx - a} {yb} Q{cx - a / 2} {yb - 6} {cx - gx} {yb - 26}" class="f-l" {_f16_ST}/>'
            b += f'<path d="M{cx + a} {yb} Q{cx + a / 2} {yb - 6} {cx + gx} {yb - 26}" class="f-l" {_f16_ST}/>'
            b += f'<path d="M{cx} {yb - 40} L{cx} {yb + 22}" class="f-dash"/>'
        elif mode == 'hole':
            b += f'<path d="M{cx - a} {yb} Q{cx - a / 2} {yb - 6} {cx} {yb - 28}" class="f-l" {_f16_ST}/>'
            b += f'<path d="M{cx + a} {yb} Q{cx + a / 2} {yb - 6} {cx} {yb - 28}" class="f-l" {_f16_ST}/>'
            b += f'<circle cx="{cx - 10}" cy="{yb - 12}" r="4" class="f-lumen"/>'
        elif mode == 'prolapse':
            b += f'<path d="M{cx - a} {yb} Q{cx - 8} {yb + 14} {cx + 4} {yb + 10}" class="f-l" {_f16_ST}/>'
            b += f'<path d="M{cx + a} {yb} Q{cx + a / 2} {yb - 6} {cx} {yb - 28}" class="f-l" {_f16_ST}/>'
        else:
            b += f'<path d="M{cx - a} {yb} Q{cx - a + 4} {yb - 10} {cx - 8} {yb - 18}" class="f-l" fill="none" style="stroke-width:7px;stroke-linecap:round"/>'
            b += f'<path d="M{cx + a} {yb} Q{cx + a - 4} {yb - 10} {cx + 8} {yb - 18}" class="f-l" fill="none" style="stroke-width:7px;stroke-linecap:round"/>'
        b += T(cx, 250, rep, 'f-s')
    b += T(12, 322, 'Types Ia to Ic: normal cusps, dilated functional aortic annulus. Dashed line: central regurgitant jet.', 'f-s', 'start')
    return svg(334, b)


def f16_vsrr():
    b = ''
    # reimplantation
    cx = 130
    b += T(cx, 22, 'Reimplantation (David)', 'f-h')
    b += f'<rect x="{cx - 60}" y="40" width="120" height="170" rx="6" class="f-b0"/>'
    for k in range(3):
        x0 = cx - 50 + k * 33.3
        b += f'<path d="M{x0} 150 Q{x0 + 16.6} 186 {x0 + 33.3} 150" class="f-l" {_f16_ST}/>'
    b += '<circle cx="80" cy="110" r="9" class="f-lumen"/><circle cx="180" cy="110" r="9" class="f-lumen"/>'
    b += line(cx - 70, 222, cx + 70, 222, 'f-cut')
    for k in range(7):
        b += line(cx - 60 + k * 20, 210, cx - 60 + k * 20, 226, 'f-l')
    b += T(cx, 246, 'Subannular sutures 2 to 3 mm below nadirs', 'f-s')
    b += T(cx, 266, 'Valve sits inside the graft; graft fixes', 'f-s') + T(cx, 283, 'the annulus. Commonest graft 30 mm', 'f-s')
    # remodelling
    cx = 400
    b += T(cx, 22, 'Remodelling (Yacoub) with ring', 'f-h')
    path = (f'M{cx - 60} 40 L{cx + 60} 40 L{cx + 60} 120 '
            f'Q{cx + 50} 200 {cx + 20} 200 L{cx + 20} 130 Q{cx} 120 {cx - 20} 130 L{cx - 20} 200 Q{cx - 50} 200 {cx - 60} 120 Z')
    b += f'<path d="{path}" class="f-b0"/>'
    b += T(cx, 172, 'Neo-', 'f-s') + T(cx, 188, 'sinus', 'f-s')
    b += '<circle cx="355" cy="110" r="9" class="f-lumen"/><circle cx="445" cy="110" r="9" class="f-lumen"/>'
    b += f'<ellipse cx="{cx}" cy="214" rx="72" ry="10" class="f-stent"/>'
    b += T(cx, 246, 'Three tongues sewn to the sinus remnants', 'f-s')
    b += T(cx, 266, 'External ring at the basal ring; keeps', 'f-s') + T(cx, 283, 'sinus dynamics. Commonest graft 28 mm', 'f-s')
    b += box(530, 50, 180, 92, ['EACTS 2026:', 'equivalent when', 'remodelling has a', 'circumferential ring'], 'ok', 'f-s')
    b += box(530, 156, 180, 92, ['Prefer reimplantation:', 'annulus over 25 to 28 mm,', 'Marfan, dissection,', 'weak root tissue'], 'warn', 'f-s')
    b += T(370, 310, 'Both: restore an annulus to STJ ratio of 1.2 to 1.3 and check effective height 9 to 10 mm after the root', 'f-s')
    return svg(322, b)


def f16_repair_toe():
    rows = ['Residual AR', 'Coaptation length', 'Effective height', 'Mean / peak gradient', 'Annulus']
    cols = [('Accept', 'ok', ['Grade 1 or less, central', '4 mm or more', '9 mm or more', '15 / 30 mmHg or less', '21 to 24 mm']),
            ('Questionable', 'b1', ['Trivial eccentric jet', 'not listed', 'Billowing cusp', 'Restricted, no gradient', '25 mm']),
            ('Back on bypass', 'warn', ['Over grade 1, or eccentric', 'under 4 mm', 'under 9 mm', 'over 15 / 30 mmHg', '26 to 27 mm'])]
    b = T(12, 20, 'Post-repair TOE check under normal loading (EACTS 2026, Table 6 of the document)', 'f-h', 'start')
    for i, r in enumerate(rows):
        b += T(140, 74 + i * 36, r, '', 'end')
    for j, (h, cls, vals) in enumerate(cols):
        x = 152 + j * 190
        b += f'<rect x="{x}" y="32" width="180" height="214" rx="10" class="f-{cls}"/>'
        b += T(x + 90, 52, h, 'f-h')
        for i, v in enumerate(vals):
            b += T(x + 90, 74 + i * 36, v, 'f-s')
    b += T(12, 266, 'Also questionable: a central jet from overcorrection.', 'f-s', 'start')
    return svg(278, b)


def f16_iad():
    b = box(200, 10, 320, 56, ['Suspect: wall haematoma seen, or sudden fall in', 'right radial pressure or cerebral oximetry'], 'warn', 'f-s')
    b += arrow(360, 66, 360, 86)
    b += box(200, 88, 320, 44, ['Reduce flow through the cannula; confirm on TOE'], 'b1', 'f-s')
    b += arrow(300, 132, 160, 158) + arrow(420, 132, 560, 158)
    b += box(10, 160, 330, 74, ['Central aortic cannulation', 'Move arterial inflow to axillary or femoral;', 'TOE shows flow in the true lumen'], 'b0', 'f-s')
    b += box(380, 160, 330, 74, ['Peripheral cannulation (minimal access)', 'Stop retrograde flow; convert to sternotomy;', 'antegrade central perfusion'], 'b0', 'f-s')
    b += arrow(175, 234, 300, 262) + arrow(545, 234, 420, 262)
    b += box(160, 264, 400, 58, ['Cool to 25 to 28 C with selective cerebral perfusion;', 'replace ascending aorta, hemiarch as needed'], 'ok', 'f-s')
    b += T(360, 344, 'Series of 31 (Wu 2026): in-hospital mortality 29%; total circulatory arrest in 39%', 'f-s')
    return svg(356, b)


# ---- figs_F17.py



def f17_stat_categories():
    h, b = bars([('Category 1 (59 codes)', (0.2, 1.3), 'ok'),
                 ('Category 2 (73 codes)', (1.4, 2.9), 'ok'),
                 ('Category 3 (46 codes)', (3.0, 6.8), 'b1'),
                 ('Category 4 (37 codes)', (6.9, 13.0), 'warn'),
                 ('Category 5 (17 codes)', (13.5, 38.7), 'warn')],
                '%', 45, 'STAT 2020: mortality rises about tenfold from category 1 to 5', 210)
    b += T(12, h + 4, 'Estimated in-hospital mortality range of the procedures in each category (STS database 2010 to 2017, 161,351 operations)', 'f-s', 'start')
    return svg(h + 16, b)


def f17_stat_examples():
    rows = [('Category 1', 'score 0.1 to 0.3', 'ok',
             ['ASD patch 0.1 · VSD patch 0.2 · coarctation end-to-end 0.2',
              'Fallot without ventriculotomy 0.3 · sinus of Valsalva aneurysm 0.3']),
            ('Category 2', 'score 0.4 to 0.7', 'ok',
             ['Ross 0.4 · one-and-a-half ventricle repair 0.4 · bidirectional Glenn 0.5',
              'Fallot transannular patch 0.5 · extracardiac Fontan 0.6']),
            ('Category 3', 'score 0.8 to 1.2', 'b1',
             ['Arterial switch 0.8 · complete AVSD 0.8 · Konno 0.8',
              'Rastelli 0.9 · pulmonary atresia with VSD repair 1.1']),
            ('Category 4', 'score 1.3 to 2.6', 'warn',
             ['Heart transplant 1.4 · switch with VSD 1.4 · modified BT shunt 1.5',
              'PA band 1.7 · TAPVC 1.9 · interrupted arch 2.1 · truncus 2.4']),
            ('Category 5', 'score 2.9 to 5.0', 'warn',
             ['Damus-Kaye-Stansel 2.9 · heart-lung transplant 3.2 · double switch 3.4',
              'Yasui 3.6 · Norwood 4.0 · truncus with interrupted arch 5.0'])]
    b = ''
    for i, (cat, sc, cls, items) in enumerate(rows):
        y = 10 + i * 60
        b += f'<rect x="10" y="{y}" width="150" height="52" rx="9" class="f-{cls}"/>'
        b += T(85, y + 22, cat, 'f-h') + T(85, y + 40, sc, 'f-s')
        b += f'<rect x="170" y="{y}" width="540" height="52" rx="9" class="f-b1"/>'
        b += T(182, y + 22, items, 'f-s', 'start')
    b += T(12, 322, 'Number after each operation: STAT mortality score (0.1 to 5.0), STS-EACTS list dated 24 June 2020', 'f-s', 'start')
    return svg(334, b)


def f17_nchda_monitoring():
    b = box(10, 10, 700, 40, 'Every procedure coded in NCHDA (EPCC codes) · life status at 30 days from ONS', 'b1')
    b += arrow(360, 50, 360, 70)
    b += box(10, 72, 700, 78, ['PRAiS2 predicts each child\'s 30-day risk from: specific procedure (16 groups) ·',
                               'diagnosis (11 groups) · age and weight · univentricular heart · bypass or not ·',
                               'comorbidity: congenital, acquired, severity of illness, additional cardiac risk'], 'b0')
    b += arrow(360, 150, 360, 170)
    b += box(10, 172, 700, 40, 'Summed over a hospital\'s last three years: predicted survival and its predicted range', 'b0')
    b += arrow(120, 212, 120, 236) + arrow(360, 212, 360, 236) + arrow(600, 212, 600, 236)
    b += box(10, 238, 220, 62, ['Within range:', 'in line with expected'], 'ok')
    b += box(250, 238, 220, 62, ['Beyond alert limit', '(2 SD, 97.5%)'], 'warn')
    b += box(490, 238, 220, 62, ['Beyond alarm limit', '(3 SD, 99.5%)'], 'warn')
    b += box(250, 316, 460, 44, 'Negative outlier: Department of Health outlier policy applies', 'b1', 'f-s')
    b += arrow(480, 300, 480, 314)
    b += box(10, 316, 220, 44, ['Units also review VLAD', 'charts, usually monthly'], 'b1', 'f-s')
    return svg(370, b)


def f17_nchda_10yr():
    h1, b1 = bars([('VSD', 96.9, 'ok'), ('Coarctation', 96.7, 'ok'), ('Tetralogy of Fallot', 95.1, 'ok'),
                   ('Aortic stenosis', 94.4, 'ok'), ('Transposition', 93.1, 'ok'), ('AVSD', 88.5, 'b1'),
                   ('Functionally univentricular', 86.7, 'b1'), ('Pulmonary atresia', 81.0, 'warn'),
                   ('Hypoplastic left heart', 57.6, 'warn')],
                  '%', 100, 'Ten-year survival: lowest in hypoplastic left heart and pulmonary atresia', 230)
    h2, b2 = bars([('VSD', 6.1, 'ok'), ('Coarctation', 19.8, 'b1'), ('Transposition', 20.9, 'b1'),
                   ('AVSD', 21.6, 'b1'), ('Tetralogy of Fallot', 26.6, 'b1'), ('Aortic stenosis', 31.2, 'b1'),
                   ('Hypoplastic left heart', 54.5, 'warn'), ('Functionally univentricular', 57.3, 'warn'),
                   ('Pulmonary atresia', 66.8, 'warn')],
                  '%', 100, 'Ten-year reintervention: highest in pulmonary atresia', 230)
    foot = T(12, h1 + h2 + 2, 'England and Wales, children born 2000 to 2022, NCHDA linked to ONS (Brown and colleagues, JAHA 2024)', 'f-s', 'start')
    return svg(h1 + h2 + 14, b1 + f'<g transform="translate(0 {h1})">{b2}</g>' + foot)


def f17_paivs_outcomes():
    h1, b1 = bars([('Intact septum, 1 year', 80.6, 'warn'), ('Intact septum, 5 years', 79.3, 'warn'),
                   ('Intact septum, 10 years', 78.6, 'warn'), ('With VSD, 1 year', 89.2, 'b1'),
                   ('With VSD, 5 years', 83.4, 'b1'), ('With VSD, 10 years', 82.1, 'b1')],
                  '%', 100, 'Survival: the intact-septum deaths cluster in the first year', 230)
    h2, b2 = bars([('Intact septum, 1 year', 44.9, 'warn'), ('Intact septum, 5 years', 52.8, 'warn'),
                   ('Intact septum, 10 years', 58.9, 'warn'), ('With VSD, 1 year', 32.0, 'b1'),
                   ('With VSD, 5 years', 62.0, 'b1'), ('With VSD, 10 years', 69.9, 'b1')],
                  '%', 100, 'Cumulative reintervention beyond the expected pathway', 230)
    foot = T(12, h1 + h2 + 2, 'Pulmonary atresia, England and Wales 2000 to 2022: intact septum n=512, with VSD n=1,131 (NCHDA linked to ONS)', 'f-s', 'start')
    return svg(h1 + h2 + 14, b1 + f'<g transform="translate(0 {h1})">{b2}</g>' + foot)


def f17_lsvc():
    b = T(180, 22, 'Unroofed coronary sinus with left SVC', 'f-h') + T(540, 22, 'Bilateral bidirectional Glenn', 'f-h')
    b += line(360, 10, 360, 340, 'f-dash')
    b += '<rect x="30" y="140" width="110" height="110" rx="20" class="f-b1"/>' + T(85, 200, 'RA', 'f-h')
    b += '<rect x="160" y="140" width="130" height="110" rx="20" class="f-b0"/>' + T(225, 166, 'LA', 'f-h')
    b += '<path d="M85 66 L85 140" class="f-vessel"/>' + T(85, 46, 'Right SVC', 'f-s')
    b += '<path d="M318 66 L318 270 C318 284 300 286 280 286 L150 286 L130 252" class="f-vessel"/>'
    b += T(318, 46, 'Left SVC', 'f-s')
    b += T(225, 312, 'Coronary sinus, opening to the RA', 'f-s')
    b += arrow(225, 278, 225, 236)
    b += T(225, 196, ['Unroofed:', 'right-to-left', 'into the LA'], 'f-s')
    b += T(180, 336, 'Left SVC with an unroofed coronary sinus: Raghib syndrome', 'f-s')
    b += '<path d="M470 66 L470 130" class="f-vessel"/>' + '<path d="M610 66 L610 130" class="f-vessel"/>'
    b += T(470, 46, 'Right SVC', 'f-s') + T(610, 46, 'Left SVC', 'f-s')
    b += '<path d="M410 136 L670 136" class="f-vessel"/>'
    b += T(540, 170, 'Confluent pulmonary arteries', 'f-s')
    b += T(540, 198, ['Each cava divided from the heart and sewn', 'end-to-side to its own pulmonary artery'], 'f-s')
    b += box(395, 250, 300, 62, ['TSRA: a persistent left SVC', 'needs a bilateral bidirectional', 'Glenn at stage 2'], 'b0', 'f-s')
    return svg(350, b)


# ---- figs_F18.py



def f18_capacity_test():
    """Mental Capacity Act 2005 ss1 to 4: presumption, two-stage test, then best interests."""
    b = box(160, 10, 400, 40, 'Start: presume capacity (s1(2)); help the person decide (s1(3))', 'b1', 'f-s')
    b += arrow(360, 50, 360, 72)
    b += box(110, 74, 500, 50, ['Stage 1 (s2(1)): is there an impairment of, or disturbance in,',
                                'the functioning of the mind or brain? Temporary counts'], 'b0', 'f-s')
    b += arrow(610, 99, 640, 99) + box(642, 74, 70, 50, ['No: has', 'capacity'], 'ok', 'f-s')
    b += arrow(360, 124, 360, 146) + T(372, 140, 'Yes', 'f-s', 'start')
    b += box(10, 148, 700, 30, 'Stage 2 (s3(1)): because of it, is the person unable to do any one of these, for this decision, now?', 'b1', 'f-s')
    xs = [10, 187, 364, 541]
    labs = [['Understand', 'the relevant information'], ['Retain it', '(briefly is enough)'],
            ['Use or weigh it', 'in reaching a decision'], ['Communicate', 'the decision by any means']]
    for x, lab in zip(xs, labs):
        b += arrow(x + 84, 178, x + 84, 194)
        b += box(x, 196, 169, 50, lab, 'b0', 'f-s')
    b += arrow(360, 246, 360, 266) + T(372, 260, 'Unable to do one or more', 'f-s', 'start')
    b += box(160, 268, 400, 34, 'Lacks capacity for this decision at this time', 'warn', 'f-s')
    b += arrow(360, 302, 360, 322)
    b += box(10, 324, 340, 92, ['Check first', 'Valid, applicable advance decision (ss24 to 26)?',
                                'Health and welfare LPA (s9) or deputy?',
                                'They decide; LPA covers life-sustaining', 'treatment only if it says so (s11)'], 'b1', 'f-s')
    b += box(370, 324, 340, 92, ['Otherwise: best interests (s4)', 'Past and present wishes, beliefs, values',
                                 'Consult carers, LPA, deputy, named people',
                                 'Least restrictive option (s1(6))',
                                 'Nobody to consult and serious treatment: IMCA (s37)'], 'b1', 'f-s')
    b += T(360, 436, 'Unwise decisions do not by themselves show incapacity (s1(4)). Disputes are decided on the balance of probabilities (s2).', 'f-s')
    return svg(448, b)


def f18_who_consents():
    """Who gives consent: adult with capacity, adult lacking capacity, 16 to 17, under 16."""
    b = box(10, 10, 700, 34, 'Who decides? (England and Wales)', 'b1', 'f-h')
    cols = [
        ('Adult, has capacity', ['Patient decides', 'May refuse, even if', 'unwise or life-ending', 'Montgomery disclosure'], 'ok'),
        ('Adult, lacks capacity', ['Valid advance decision', 'or LPA / deputy decides', 'Otherwise act in best', 'interests (MCA ss4, 5)'], 'b0'),
        ('Aged 16 or 17', ['Presumed to have capacity', 'MCA applies from 16', 'If lacking: parent consent', 'or best interests'], 'b0'),
        ('Under 16', ['Gillick competent:', 'child may consent', 'If not: one person with', 'parental responsibility'], 'b0'),
    ]
    for i, (h, lines, cls) in enumerate(cols):
        x = 10 + i * 178
        b += arrow(x + 82, 44, x + 82, 64)
        b += box(x, 66, 164, 36, h, cls, 'f-h')
        b += box(x, 110, 164, 92, lines, 'b1', 'f-s')
    b += box(10, 216, 700, 56, ['Refusal by a competent under-18: parents cannot override it simply by consenting (GMC 0 to 18);',
                                'in England, Wales and Northern Ireland the law is complex: seek legal advice about applying to court'], 'warn', 'f-s')
    b += box(10, 282, 700, 40, ['Emergency, no one able to consent: give treatment immediately necessary to save life or prevent',
                               'serious deterioration, least restrictive option; explain afterwards (GMC consent paras 62 to 64)'], 'b1', 'f-s')
    return svg(332, b)


def f18_consent_law():
    """Montgomery and McCulloch: two stages of the duty, with the exceptions."""
    b = box(10, 10, 340, 108, ['Stage 1: which options are reasonable?', 'Professional practice test',
                               '(Bolam; Hunter v Hanley in Scotland),', 'tested by Bolitho logic',
                               'McCulloch v Forth Valley [2023] UKSC 26'], 'b0', 'f-s')
    b += arrow(350, 64, 368, 64)
    b += box(370, 10, 340, 108, ['Stage 2: what must be disclosed?', 'Material risks of each reasonable option,',
                                 'including no treatment', 'Reasonable patient in this position, or this',
                                 'patient (Montgomery [2015] UKSC 11, para 87)'], 'ok', 'f-s')
    b += arrow(540, 118, 540, 140)
    b += box(370, 142, 340, 74, ['Materiality is not a percentage (para 89):', 'nature of risk, effect on this life,',
                                 'benefits, alternatives, the patient'], 'b1', 'f-s')
    b += box(10, 142, 340, 74, ['Dialogue, not a signature (para 90)', 'Comprehensible information; no',
                                'bombarding with technical detail'], 'b1', 'f-s')
    b += box(10, 230, 700, 58, ['Exceptions: patient chooses not to know (para 85) · necessity, e.g. unconscious and urgent (para 88) ·',
                                'therapeutic exception, narrow: serious harm to health, never to steer the choice (paras 88, 91)'], 'warn', 'f-s')
    return svg(298, b)


def f18_candour():
    """Duty of candour: statutory (organisation, Regulation 20) and professional (individual, GMC and NMC)."""
    b = T(12, 22, 'After a notifiable safety incident: what happens and who owes it', 'f-h', 'start')
    steps = [('1', ['Act to put', 'it right']), ('2', ['Tell in person,', 'as soon as', 'practicable']),
             ('3', ['Account of', 'what is known;', 'say what is not']), ('4', ['Apologise:', 'personal,', 'sincere']),
             ('5', ['Offer support', 'and a named', 'contact']), ('6', ['Written', 'notification;', 'keep records'])]
    w, gap = 106, 12
    b += line(30, 110, 690, 110, 'f-l')
    for i, (n, lab) in enumerate(steps):
        x = 10 + i * (w + gap)
        b += f'<circle cx="{x + w / 2}" cy="110" r="14" class="f-b0"/>' + T(x + w / 2, 115, n, 'f-n')
        b += box(x, 132, w, 66, lab, 'b1', 'f-s')
    b += T(360, 60, 'Do not wait for the investigation; be clear what has and has not been established', 'f-s')
    b += T(360, 78, 'Statutory written notice follows the in-person conversation (Regulation 20)', 'f-s')
    b += box(10, 214, 345, 108, ['Statutory (organisation)', 'Regulation 20, 2014 Regulations; CQC',
                                 'Death, severe, moderate or prolonged', 'psychological harm (28 days or more)',
                                 'Owed by the provider, not the individual'], 'b0', 'f-s')
    b += box(365, 214, 345, 108, ['Professional (each clinician)', 'GMC and NMC joint guidance',
                                  'Any harm or distress, or potential harm', 'Near miss: judgement whether to tell;',
                                  'report it; never block others raising concerns'], 'ok', 'f-s')
    b += box(10, 334, 700, 36, 'An apology is not an admission of legal liability (GMC candour guidance; Compensation Act 2006 s2)', 'warn', 'f-s')
    return svg(380, b)


def f18_safeguarding_hours():
    """Intercollegiate safeguarding: minimum learning over three years by level."""
    h1, b1 = bars([('Children L1 (all staff)', 2, 'track'), ('Children L2 (most adult surgeons)', 4, 'b1'),
                   ('Children L3 core', 8, 'b0'), ('Children L3 additional competencies', 12, 'b0')],
                  ' h', 26, 'Children (2019 ICD): most adult surgeons are level 2', lab_w=300)
    h2, b2 = bars([('Adults L1', 2, 'track'), ('Adults L2', 3, 'b1'), ('Adults L3 (assess and plan care)', 8, 'b0'),
                   ('Adults L4 (named professionals)', 24, 'warn')],
                  ' h', 26, 'Adults (2024 ICD): learning hours per 3 years', lab_w=300)
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


# ---- figs_F19.py

import math


def f19_two_by_two():
    """Worked 2x2 table: same test (Sn 90%, Sp 80%) at two prevalences."""
    b = ''
    specs = [(10, 'Prevalence 20% (1,000 referred patients)', (180, 160, 20, 640), '52.9%', '97.0%'),
             (370, 'Prevalence 2% (1,000 screened people)', (18, 196, 2, 784), '8.4%', '99.7%')]
    for x0, title, (tp, fp, fn, tn), ppv, npv in specs:
        b += T(x0 + 170, 22, title, 'f-h')
        b += T(x0 + 150, 48, 'Disease present', 'f-s') + T(x0 + 270, 48, 'Disease absent', 'f-s')
        b += T(x0 + 50, 86, 'Test +', 'f-h') + T(x0 + 50, 146, 'Test −', 'f-h')
        b += box(x0 + 92, 58, 116, 52, [f'TP {tp:,}'], 'ok', 'f-h')
        b += box(x0 + 212, 58, 116, 52, [f'FP {fp:,}'], 'warn', 'f-h')
        b += box(x0 + 92, 118, 116, 52, [f'FN {fn:,}'], 'warn', 'f-h')
        b += box(x0 + 212, 118, 116, 52, [f'TN {tn:,}'], 'ok', 'f-h')
        b += box(x0 + 10, 184, 155, 46, ['PPV = TP ÷ (TP+FP)', ppv], 'b1', 'f-s')
        b += box(x0 + 175, 184, 155, 46, ['NPV = TN ÷ (TN+FN)', npv], 'b1', 'f-s')
    b += line(360, 12, 360, 236, 'f-dash')
    b += box(10, 248, 700, 58, ['Sensitivity = TP ÷ (TP+FN) = 90% and specificity = TN ÷ (TN+FP) = 80% in both panels.',
                               'LR+ = 0.90 ÷ 0.20 = 4.5 · LR− = 0.10 ÷ 0.80 = 0.125 · only the predictive values move'], 'b0', 'f-s')
    return svg(316, b)


def f19_forest_plot():
    """Forest plot anatomy with five invented trials (odds ratio, log scale)."""
    x0, x1 = 300, 640
    lo, hi = math.log(0.25), math.log(4)

    def X(v):
        return x0 + (math.log(v) - lo) / (hi - lo) * (x1 - x0)
    studies = [('Trial A (n=120)', 0.55, 0.22, 1.40, 7), ('Trial B (n=900)', 0.78, 0.60, 1.01, 14),
               ('Trial C (n=260)', 1.10, 0.62, 1.95, 9), ('Trial D (n=1,400)', 0.72, 0.58, 0.89, 16),
               ('Trial E (n=80)', 0.40, 0.12, 1.30, 6)]
    b = T(12, 20, 'Study', 'f-h', 'start') + T(470, 20, 'Odds ratio (95% CI), log scale', 'f-h')
    y = 48
    for lab, est, l, h, s in studies:
        b += T(12, y + 5, lab, '', 'start')
        b += line(X(l), y, X(h), y, 'f-l')
        b += f'<rect x="{X(est) - s / 2:.1f}" y="{y - s / 2}" width="{s}" height="{s}" class="f-b1"/>'
        b += T(700, y + 5, f'{est:.2f} ({l:.2f} to {h:.2f})', 'f-s', 'end')
        y += 30
    py = y + 8
    pe, pl, ph = 0.74, 0.63, 0.87
    b += f'<path d="M{X(pl):.1f} {py} L{X(pe):.1f} {py - 9} L{X(ph):.1f} {py} L{X(pe):.1f} {py + 9} Z" class="f-warn"/>'
    b += T(12, py + 5, 'Pooled estimate', 'f-h', 'start') + T(700, py + 5, '0.74 (0.63 to 0.87)', 'f-s', 'end')
    b += T(12, py + 24, 'I² = 12% (low)', 'f-s', 'start')
    ay = py + 40
    b += line(X(1), 32, X(1), ay, 'f-l') + line(x0, ay, x1, ay, 'f-l')
    for v in (0.25, 0.5, 1, 2, 4):
        b += line(X(v), ay, X(v), ay + 6) + T(X(v), ay + 20, f'{v:g}', 'f-s')
    b += T(X(0.5), ay + 40, '← favours treatment', 'f-s') + T(X(2), ay + 40, 'favours control →', 'f-s')
    b += T(X(1) + 6, 40, 'line of no effect', 'f-s', 'start')
    by = ay + 56
    b += box(10, by, 226, 62, ['Square: study estimate;', 'size = weight', '(inverse variance)'], 'b0', 'f-s')
    b += box(247, by, 226, 62, ['Horizontal line: 95% CI;', 'crossing 1 = not', 'significant alone'], 'b0', 'f-s')
    b += box(484, by, 226, 62, ['Diamond: pooled effect;', 'width = its 95% CI'], 'b0', 'f-s')
    return svg(by + 72, b)


def f19_funnel_plot():
    """Funnel plot: invented units against volume, national rate 2.5%, 2 and 3 SD limits."""
    gx0, gx1, gy0, gy1 = 70, 600, 30, 300
    nmax, pmax = 1600, 8.0
    p0 = 0.025

    def X(n):
        return gx0 + n / nmax * (gx1 - gx0)

    def Y(p):
        return gy1 - p / pmax * (gy1 - gy0)
    b = T(12, 18, 'Risk-adjusted mortality (%) by number of operations in the period', 'f-h', 'start')
    for p in range(0, 9, 2):
        b += line(gx0, Y(p), gx1, Y(p), 'f-grid') + T(gx0 - 8, Y(p) + 4, f'{p}', 'f-s', 'end')
    for n in range(0, 1601, 400):
        b += T(X(n), gy1 + 18, f'{n:,}', 'f-s')
    b += T((gx0 + gx1) / 2, gy1 + 38, 'Number of operations (volume)', 'f-s')
    b += line(gx0, gy0, gx0, gy1) + line(gx0, gy1, gx1, gy1)
    b += line(gx0, Y(2.5), gx1, Y(2.5), 'f-l')
    for z, cls in ((2, 'f-dash'), (3, 'f-cut')):
        up, dn = [], []
        for n in range(60, 1601, 20):
            se = math.sqrt(p0 * (1 - p0) / n)
            up.append(f'{X(n):.1f} {Y(min(pmax, 100 * (p0 + z * se))):.1f}')
            dn.append(f'{X(n):.1f} {Y(max(0, 100 * (p0 - z * se))):.1f}')
        b += f'<path d="M{" L".join(up)}" class="{cls}"/><path d="M{" L".join(dn)}" class="{cls}"/>'
    units = [(150, 2.0), (220, 4.1), (310, 1.3), (380, 3.2), (450, 2.9), (520, 1.9), (610, 2.4),
             (700, 3.0), (780, 1.7), (860, 2.2), (950, 2.8), (1040, 3.6), (1150, 2.1), (1280, 2.6), (1450, 4.1)]
    for n, p in units:
        cls = 'f-warn' if p > 100 * (p0 + 2 * math.sqrt(p0 * (1 - p0) / n)) else 'f-b1'
        b += f'<circle cx="{X(n):.1f}" cy="{Y(p):.1f}" r="6" class="{cls}"/>'
    b += T(612, Y(2.5) + 4, 'National 2.5%', 'f-s', 'start')
    b += line(330, 52, 370, 52, 'f-dash') + T(378, 56, '2 SD limit (about 95%): alert', 'f-s', 'start')
    b += line(330, 74, 370, 74, 'f-cut') + T(378, 78, '3 SD limit (99.8%): alarm', 'f-s', 'start')
    b += T(X(1110), Y(3.6) + 24, 'Alert only', 'f-s')
    b += T(X(1450) - 10, Y(4.1) - 12, 'Alarm', 'f-h', 'end')
    b += T(X(220), Y(4.1) + 24, '4.1%, n=220: inside', 'f-s')
    return svg(gy1 + 50, b)


def f19_vlad():
    """VLAD built from an invented run of 120 operations."""
    risks = [0.02, 0.03, 0.015, 0.05, 0.02, 0.08, 0.03, 0.02, 0.04, 0.12] * 12
    deaths = {17, 44, 81, 86, 92, 97, 103}
    cum, pts = 0.0, [(0, 0.0)]
    for i, p in enumerate(risks, 1):
        cum += p - (1 if i in deaths else 0)
        pts.append((i, cum))
    gx0, gx1, gy0, gy1 = 70, 690, 40, 250
    vmin, vmax = -4, 3

    def X(i):
        return gx0 + i / 120 * (gx1 - gx0)

    def Y(v):
        return gy0 + (vmax - v) / (vmax - vmin) * (gy1 - gy0)
    b = T(12, 20, 'VLAD: cumulative expected minus observed deaths (net lives saved)', 'f-h', 'start')
    for v in range(vmin, vmax + 1):
        b += line(gx0, Y(v), gx1, Y(v), 'f-grid') + T(gx0 - 8, Y(v) + 4, f'{v:+d}' if v else '0', 'f-s', 'end')
    b += line(gx0, Y(0), gx1, Y(0), 'f-l')
    for i in range(0, 121, 20):
        b += T(X(i), gy1 + 18, str(i), 'f-s')
    b += T((gx0 + gx1) / 2, gy1 + 36, 'Consecutive operations', 'f-s')
    b += '<path d="M' + ' L'.join(f'{X(i):.1f} {Y(v):.1f}' for i, v in pts) + '" class="f-cut"/>'
    b += T(X(40), Y(2.4), ['Survivor: line rises by', 'the predicted risk (e.g. +0.03)'], 'f-s')
    b += T(X(30) + 30, Y(-1.6), ['Death: line falls by', '1 minus predicted risk'], 'f-s', 'start')
    b += arrow(X(80), Y(-2.4) + 4, X(86), Y(-1.4))
    b += T(X(74), Y(-2.8) + 14, 'Cluster of deaths (cases 81 to 103)', 'f-h', 'end')
    b += box(10, gy1 + 48, 700, 40, 'Each step = predicted risk − outcome (1 if died, 0 if survived). Worked for these notes; invented data.', 'b0', 'f-s')
    return svg(gy1 + 98, b)


def f19_nlca2026():
    """NLCA State of the Nation 2026, England 2024 diagnoses, against standards."""
    h, b = bars([('Stage 1-2 curative treatment (80%)', 78.9, 'warn'),
                 ('Stage 3A curative treatment', 59.1, 'b1'),
                 ('Pathological diagnosis (90%)', 81.7, 'warn'),
                 ('SACT, advanced NSCLC (70%)', 63, 'warn'),
                 ('SACT, small-cell (70%)', 71.2, 'ok'),
                 ('NSCLC resection rate (17%)', 21.8, 'ok'),
                 ('Survival 90 days after surgery', 98.4, 'ok')],
                '%', 100, 'NLCA 2026 (England, 2024): most standards narrowly missed', 290)
    return svg(h, b)


def f19_frailty():
    return tiles([('< 0.8 m/s', ['5-metre gait speed'], 'warn'), ('CFS 4+', ['Clinical Frailty Scale'], 'warn'),
                  ('SPPB < 10', ['Short Physical', 'Performance Battery'], 'warn'),
                  ('Fried 3+', ['of 5 criteria'], 'warn')], 104)


# ---- figs_F20.py



def f20_ptx2024():
    """ERS/EACTS/ESTS 2024 pneumothorax guideline: headline recommendations by strength (abstract)."""
    b = T(12, 22, 'ERS/EACTS/ESTS 2024: what the guideline recommends (abstract)', 'f-h', 'start')
    b += box(10, 36, 226, 92, ['Strong for', 'Needle aspiration rather', 'than a chest drain for', 'initial PSP treatment'], 'ok', 'f-s')
    b += box(247, 36, 226, 92, ['Conditional for', 'Conservative care: stable', 'PSP with minimal', 'symptoms'], 'b0', 'f-s')
    b += box(484, 36, 226, 92, ['Conditional for', 'Ambulatory management', 'for initial PSP', 'treatment'], 'b0', 'f-s')
    b += box(10, 140, 345, 92, ['Conditional for', 'Early surgery at the first PSP', 'when the patient puts preventing', 'recurrence first'], 'b1', 'f-s')
    b += box(365, 140, 345, 92, ['Conditional for', 'Autologous blood patch for', 'secondary pneumothorax with', 'a persistent air leak'], 'b1', 'f-s')
    b += box(10, 244, 700, 64, ['No recommendation possible: bronchial valves · suction ·',
                               'pleurodesis added to surgical resection · type of surgical pleurodesis'], 'warn', 'f-s')
    return svg(318, b)


def f20_sabrtrials():
    """Timeline of randomised SABR versus surgery trials (registry records)."""
    x0, x1, y0, y1 = 120, 700, 2008, 2034
    def X(y):
        return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    b = line(x0, 52, x1, 52)
    for yr in (2008, 2012, 2016, 2020, 2024, 2028, 2032):
        b += line(X(yr), 46, X(yr), 58) + T(X(yr), 38, str(yr), 'f-s')
    b += line(X(2026.9), 30, X(2026.9), 268, 'f-dash') + T(X(2026.9) + 4, 284, 'Now (November 2026)', 'f-s', 'start')
    rows = [
        ('STARS, ROSEL', 2008, 2015, 'track', 'Closed for slow accrual; pooled 58 patients (2015)'),
        ('STABLE-MATES', 2015.5, 2028.9, 'b0', 'High risk: sublobar vs SABR; 272 planned; 3-year OS'),
        ('VALOR (VA)', 2017.3, 2032.7, 'b1', 'Fit: anatomical resection vs SABR; 670 planned; OS'),
    ]
    for i, (n, a, z, cls, note) in enumerate(rows):
        y = 74 + i * 64
        b += T(x0 - 8, y + 22, n, 'f-h', 'end')
        b += f'<rect x="{X(a):.0f}" y="{y + 4}" width="{X(z) - X(a):.0f}" height="26" rx="6" class="f-{cls}"/>'
        b += T(x0, y + 50, note, 'f-s', 'start')
    b += T(12, 284, 'Bar ends: start to primary completion (estimated where in the future)', 'f-s', 'start')
    return svg(296, b)


def f20_stars10():
    """Revised STARS 10-year results (ASTRO 2025 abstract)."""
    h, b = bars([('Overall: SABR', 69, 'b0'), ('Overall: VATS lobectomy', 66, 'b1'),
                 ('Cancer-specific: SABR', 92, 'b0'), ('Cancer-specific: VATS lobectomy', 89, 'b1'),
                 ('Recurrence-free: SABR', 57, 'b0'), ('Recurrence-free: VATS lobectomy', 65, 'b1')],
                '%', 100, 'Revised STARS at 10 years: no significant difference (80 vs 80 matched)', 260)
    return svg(h, b)


def f20_hilar():
    """Control of a bleeding hilum, in order (TSRA ch. 115)."""
    b = T(12, 22, 'Bleeding hilum: temporary control, then definitive repair', 'f-h', 'start')
    steps = [('1', ['Anterolateral', 'thoracotomy', '(often in the ED)']),
             ('2', ['Finger compression', 'of the hilum']),
             ('3', ['Hilar clamp;', 'or deflate and twist', 'the lung 180°, pack']),
             ('4', ['To theatre:', 'one-lung ventilation,', 'wide pleural opening'])]
    for i, (n, ls) in enumerate(steps):
        x = 10 + i * 177
        b += box(x, 38, 166, 84, ls, 'b0', 'f-s')
        b += f'<circle cx="{x + 18}" cy="52" r="11" class="f-b1"/>' + T(x + 18, 57, n, 'f-h')
        if i < 3:
            b += arrow(x + 166, 80, x + 176, 80)
    b += arrow(360, 122, 360, 146)
    b += box(10, 148, 700, 44, ['Exposure: divide the inferior pulmonary ligament; open the pericardium in front of the hilum,',
                               'parallel to the phrenic nerve'], 'b1', 'f-s')
    b += arrow(130, 192, 130, 214) + arrow(360, 192, 360, 214) + arrow(590, 192, 590, 214)
    b += box(10, 216, 226, 66, ['Bronchus or pulmonary', 'artery: repair'], 'ok', 'f-s')
    b += box(247, 216, 226, 66, ['Pulmonary vein tear:', 'usually lobectomy', '(repair thromboses)'], 'b0', 'f-s')
    b += box(484, 216, 226, 66, ['Devastating injury: stapled', 'pneumonectomy; mortality', 'over 50% (right heart failure)'], 'warn', 'f-s')
    return svg(292, b)


def f20_chestwall():
    """Chest wall injuries in TSRA ch. 115: facts and when to plate."""
    b = tiles_row = ''
    spec = [('About 40%', ['of blunt trauma patients', 'have rib fractures'], 'b1'),
            ('Over 50%', ['major head injury with', 'first or second rib fracture'], 'warn'),
            ('Over 70%', ['of scapular fractures', 'come with polytrauma'], 'warn')]
    w = (W - 20 - 2 * 14) / 3
    for i, (big, small, cls) in enumerate(spec):
        x = 10 + i * (w + 14)
        b += f'<rect x="{x:.0f}" y="10" width="{w:.0f}" height="96" rx="10" class="f-{cls}"/>'
        b += T(x + w / 2, 46, big, 'f-big') + T(x + w / 2, 70, small, 'f-s')
    b += T(12, 136, 'Flail chest: standard care first', 'f-h', 'start')
    b += box(10, 146, 700, 40, 'Restrained crystalloid · aggressive physiotherapy · regional block or epidural', 'b0', 'f-s')
    b += arrow(360, 186, 360, 208)
    b += T(12, 226, 'Consider plating (who benefits is not clearly defined: level III)', 'f-h', 'start')
    b += box(10, 236, 226, 64, ['Pulmonary toilet failing', 'because of pain'], 'b1', 'f-s')
    b += box(247, 236, 226, 64, ['Cannot be weaned from', 'the ventilator'], 'b1', 'f-s')
    b += box(484, 236, 226, 64, ['Chest already open (VATS', 'or thoracotomy) for', 'another reason'], 'b1', 'f-s')
    return svg(310, b)
