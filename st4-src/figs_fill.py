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


# ---- figs_F21.py



def f21_pe_risk():
    b = box(110, 10, 500, 54, ['Acute PE: haemodynamically unstable?',
                               'cardiac arrest · obstructive shock · persistent hypotension'], 'b1')
    b += box(200, 100, 510, 46, 'PESI class III to V, or sPESI 1 or more?', 'b1')
    b += box(200, 184, 340, 52, ['RV dysfunction on echo or CT', 'and a raised troponin?'], 'b1')
    # Q1 yes -> high; no -> Q2
    b += arrow(150, 64, 93, 270) + T(104, 120, 'Yes', 'f-h', 'end')
    b += arrow(455, 64, 455, 98) + T(466, 86, 'No', 'f-h', 'start')
    # Q2 yes -> Q3 ; no -> low
    b += arrow(370, 146, 370, 182) + T(380, 170, 'Yes', 'f-h', 'start')
    b += arrow(640, 146, 630, 270) + T(646, 214, 'No', 'f-h', 'start')
    # Q3 -> int-high / int-low
    b += arrow(290, 236, 273, 270) + T(232, 258, 'Both', 'f-h', 'middle')
    b += arrow(450, 236, 453, 270) + T(462, 258, 'One or none', 'f-s', 'start')
    cols = [(10, 'High', 'warn'), (190, 'Intermediate-high', 'warn'), (370, 'Intermediate-low', 'b1'), (550, 'Low', 'ok')]
    for x, lab, c in cols:
        b += box(x, 272, 166 if x < 550 else 160, 40, lab, c, 'f-h')
    tx = [['UFH bolus now (I, C)', 'Systemic lysis (I, B)', 'Lysis barred or failed:', 'surgery (I, C) or', 'catheter (IIa, C)', 'ECMO with either (IIb, C)'],
          ['Anticoagulate, admit', 'and monitor', 'Deteriorates: rescue', 'lysis (I, B), or surgery', 'or catheter (IIa, C)'],
          ['Anticoagulate, admit', 'No routine primary', 'lysis (III, B)'],
          ['Anticoagulate', 'Consider early', 'discharge (IIa, A)']]
    for (x, lab, c), lines in zip(cols, tx):
        b += box(x, 324, 166 if x < 550 else 160, 120, lines, 'b0', 'f-s')
    b += T(360, 466, 'PE team for high-risk and selected intermediate-risk PE (IIa, C). Routine IVC filter: not recommended (III, A).', 'f-s')
    return svg(480, b)


def f21_cteph_pathway():
    b = box(110, 10, 500, 46, ['CTEPH confirmed: V/Q mismatch, CTPA or DSA,', 'right heart catheter (mPAP over 20, PVR over 2 WU)'], 'b1')
    b += arrow(360, 56, 360, 76)
    b += box(110, 78, 500, 46, ['Lifelong therapeutic anticoagulation (I, C)', 'Test for antiphospholipid syndrome; VKA if present (I, C)'], 'b0')
    b += arrow(360, 124, 360, 144)
    b += box(110, 146, 500, 46, ['CTEPH team with a PEA surgeon decides', 'operability and treatment (I, C)'], 'b0')
    b += arrow(250, 192, 170, 222) + arrow(470, 192, 550, 222)
    b += T(160, 210, 'Operable', 'f-h', 'end') + T(566, 210, 'Inoperable', 'f-h', 'start')
    b += box(10, 224, 320, 64, ['Pulmonary endarterectomy (I, B)', 'under deep hypothermic arrest'], 'ok', 'f-h')
    b += box(390, 224, 320, 64, ['Riociguat (I, B) and / or', 'balloon angioplasty (I, B)'], 'ok', 'f-h')
    b += arrow(170, 288, 170, 312)
    b += box(10, 314, 320, 54, ['Persistent or recurrent PH', 'after endarterectomy'], 'warn')
    b += arrow(330, 341, 388, 270)
    b += box(390, 300, 320, 68, ['PVR over 4 WU: drugs before BPA (IIa, B)', 'Multimodal treatment (IIa, C)',
                                 'Mostly distal disease: BPA (IIb, C)'], 'b1', 'f-s')
    b += box(10, 392, 700, 46, ['Long-term follow-up at the CTEPH centre (I, C): right heart catheter 3 to 6 months',
                                'after intervention, then yearly echo and exercise testing'], 'b1')
    b += arrow(360, 368, 360, 390)
    return svg(448, b)


def f21_cteph_lesions():
    # tapering vessel from proximal (left) to distal (right)
    b = T(12, 22, 'Proximal', 'f-s', 'start') + T(708, 22, 'Distal', 'f-s', 'end')
    b += '<path d="M20 40 L20 120 L700 84 L700 76 Z" class="f-b0"/>'
    b += '<path d="M40 50 L40 110 L150 100 L150 60 Z" class="f-b1"/>'
    for x in (300, 430, 560):
        b += f'<line x1="{x}" y1="{64 + (x - 20) * 0.0}" x2="{x}" y2="{102 - (x - 20) * 0.03}" class="f-l"/>'
    b += T(95, 85, 'organised clot', 'f-s')
    b += T(430, 140, 'webs and bands narrow the lumen', 'f-s')
    spec = [('Proximal fibrotic obstruction', '10 to 40 mm', 20, 210, 'ok', 'PEA'),
            ('Segmental and subsegmental', '2 to 10 mm', 190, 360, 'b1', 'PEA or BPA'),
            ('Subsegmental webs', '0.5 to 5 mm', 340, 510, 'b1', 'BPA'),
            ('Webs under 0.5 mm', '± microvasculopathy', 490, 620, 'b1', 'BPA'),
            ('Microvasculopathy', 'under 0.05 mm', 600, 700, 'warn', 'Drugs')]
    y = 162
    for lab, size, x1, x2, c, tx in spec:
        b += f'<rect x="{x1}" y="{y}" width="{x2 - x1}" height="26" rx="6" class="f-{c}"/>'
        b += T((x1 + x2) / 2, y + 18, tx, 'f-h')
        anchor = 'start' if x1 < 400 else 'end'
        tx_x = x2 + 8 if anchor == 'start' else x1 - 8
        b += T(tx_x, y + 18, f'{lab}, {size}', 'f-s', anchor)
        y += 34
    b += T(360, y + 14, 'Treatment by lesion level and vessel size; ranges overlap, so mixed disease may need PEA plus BPA.', 'f-s')
    return svg(y + 28, b)


def f21_cath_trials():
    h1, b1 = bars([('Catheter lysis + anticoagulation', 4.0, 'ok'), ('Anticoagulation alone', 10.3, 'warn'),
                   ('Major bleeding: catheter', 4.1, 'b1'), ('Major bleeding: anticoagulation', 3.0, 'b1')],
                  '%', 15, 'HI-PEITHO (n=544): 7-day PE death, collapse or recurrence fell', lab_w=270)
    h2, b2 = bars([('Deterioration or bailout: LBMT', 1.8, 'ok'), ('Deterioration or bailout: CDT', 5.4, 'warn'),
                   ('ICU admission: LBMT', 41.6, 'ok'), ('ICU admission: CDT', 98.6, 'warn')],
                  '%', 100, 'PEERLESS (n=550): thrombectomy needed less ICU care than CDT', lab_w=270)
    b = b1 + f'<g transform="translate(0 {h1})">{b2}</g>'
    b += T(12, h1 + h2 + 4, 'HI-PEITHO RR 0.39 (0.20 to 0.77); bleeding RR 1.4 (0.6 to 3.4), no ICH. PEERLESS: no difference in death or bleeding.', 'f-s', 'start')
    return svg(h1 + h2 + 18, b)


def f21_embolectomy_mortality():
    h, b = bars([('Meta-analysis 1965 to 2015 (Kalra)', 26.3, 'b1'),
                 ('Meta-analysis to 2024 (Rahouma)', 22.0, 'b1'),
                 ('NY State: thrombolysis, 30-day', 15, 'b0'),
                 ('NY State: surgery, 30-day', 13, 'b0'),
                 ('STS database: all', 12, 'ok'),
                 ('STS database: arrest before surgery', 32, 'warn')],
                '%', 40, 'Surgical embolectomy: early death 12 to 26% across series, 32% after arrest', lab_w=290)
    b += T(12, h + 4, 'In-hospital mortality unless stated. NY State and STS figures as quoted in the ESC 2019 guideline; non-randomised.', 'f-s', 'start')
    return svg(h + 16, b)


def f21_papworth():
    h, b = bars([('Cohort 1 (1997 onwards)', 12.3, 'warn'), ('Cohort 2', 4.0, 'b1'),
                 ('Cohort 3', 3.4, 'b1'), ('Cohort 4 (to 2019)', 1.9, 'ok')],
                '%', 15, 'Royal Papworth, 2,116 endarterectomies: 30-day mortality fell to 1.9%', lab_w=230)
    b += T(12, h + 4, 'Four consecutive cohorts of 529. The first took 12 years, the last under 3. PVR fell by about 60% in every cohort.', 'f-s', 'start')
    return svg(h + 16, b)


# ---- figs_F22.py



def _f22_pairs(groups, vmax, title, lab_w=230, note=None):
    """Grouped horizontal bars. groups: (group heading, [(label, value, cls, text)])."""
    y = 18
    out = T(12, y + 4, title, 'f-h', 'start')
    y += 22
    span = W - lab_w - 110
    for head, rows in groups:
        out += T(12, y + 16, head, 'f-s', 'start')
        y += 24
        for lab, v, cls, txt in rows:
            out += T(lab_w - 10, y + 19, lab, '', 'end')
            out += f'<rect x="{lab_w}" y="{y + 4}" width="{max(2, span * v / vmax):.1f}" height="22" rx="4" class="f-{cls}"/>'
            out += T(lab_w + span * v / vmax + 8, y + 20, txt, 'f-n', 'start')
            y += 30
        y += 6
    if note:
        for i, s in enumerate(note):
            out += T(12, y + 10 + i * 17, s, 'f-s', 'start')
        y += 17 * len(note) + 4
    return svg(y + 8, out)


def f22_shock_trials():
    """Primary end point (all-cause death) in DanGer Shock and ECLS-SHOCK, from the papers."""
    return _f22_pairs([
        ('DanGer Shock (NEJM 2024): death at 180 days, n = 355. HR 0.74 (0.55 to 0.99), P = 0.04', [
            ('Microaxial pump + standard care', 45.8, 'ok', '45.8% (82/179)'),
            ('Standard care', 58.5, 'b1', '58.5% (103/176)')]),
        ('ECLS-SHOCK (NEJM 2023): death at 30 days, n = 417. RR 0.98 (0.80 to 1.19), P = 0.81', [
            ('VA-ECLS + usual care', 47.8, 'b0', '47.8% (100/209)'),
            ('Usual care', 49.0, 'b1', '49.0% (102/208)')]),
    ], 70, 'Infarct-related shock: the pump lowered death, VA-ECLS did not',
        note=['Both raised complications: DanGer composite safety end point 24.0% v 6.2%;',
              'ECLS-SHOCK moderate or severe bleeding 23.4% v 9.6%, limb ischaemia needing intervention 11.0% v 3.8%.'])


def f22_ecpr_trials():
    """Primary end points of the three ECPR trials, from the papers."""
    return _f22_pairs([
        ('ARREST (Lancet 2020), 1 centre, refractory VF: survival to discharge', [
            ('ECMO-facilitated resuscitation', 43, 'ok', '43% (6/14)'),
            ('Standard ACLS', 7, 'b1', '7% (1/15)')]),
        ('Prague OHCA (JAMA 2022), 1 centre: 180-day survival, CPC 1 to 2. P = 0.09', [
            ('Invasive strategy (ECPR)', 31.5, 'b0', '31.5% (39/124)'),
            ('Standard ACLS', 22.0, 'b1', '22.0% (29/132)')]),
        ('INCEPTION (NEJM 2023), 10 centres: 30-day survival, CPC 1 to 2. P = 0.52', [
            ('ECPR', 20, 'b0', '20% (14/70)'),
            ('Conventional CPR', 16, 'b1', '16% (10/62)')]),
    ], 60, 'ECPR: only the small single-centre trial was positive',
        note=['ARREST stopped at its first interim analysis (posterior probability of benefit 0.986).',
              'Prague OHCA stopped for futility at 256 of 285. INCEPTION: median 74 minutes from arrest to ECMO flow.'])


def f22_scai_ladder():
    """SCAI shock stages A to E, 2019 definition with the 2022 update criteria."""
    rows = [
        ('A', 'At risk', 'No shock yet: large or prior infarct, acute heart failure', 'Warm, perfused; normal lactate; SBP 100+', 'ok'),
        ('B', 'Beginning', 'Hypotension or tachycardia, NO hypoperfusion', 'SBP under 90, MAP under 60 or fall over 30; HR 100+', 'b1'),
        ('C', 'Classic', 'Hypoperfusion needing one drug or device beyond fluid', 'Lactate 2+; cold, clammy; urine under 30 mL/h; CI under 2.2', 'b0'),
        ('D', 'Deteriorating', 'Worse despite initial therapy: more drugs or MCS added', 'Lactate rising and over 2; organ function worsening', 'warn'),
        ('E', 'Extremis', 'Circulatory collapse, often CPR or ECMO-CPR', 'Lactate 8+; pH under 7.2; bolus pressors', 'warn'),
    ]
    b = T(12, 22, 'SCAI shock stages: the step from B to C is hypoperfusion', 'f-h', 'start')
    y = 36
    for i, (s, name, desc, crit, cls) in enumerate(rows):
        x = 10 + i * 22
        w = 700 - i * 22
        b += f'<rect x="{x}" y="{y}" width="{w}" height="50" rx="9" class="f-{cls}"/>'
        b += T(x + 22, y + 32, s, 'f-big')
        b += T(x + 48, y + 21, name, 'f-h', 'start')
        b += T(x + 48, y + 39, desc, 'f-s', 'start')
        b += T(706, y + 21, crit, 'f-s', 'end')
        y += 56
    b += box(10, y + 6, 700, 58, ['Modifier: 2019 "A" = any cardiac arrest (e.g. stage "BA").',
                                  '2022 update: arrest modifier only with coma (GCS under 9), i.e. concern for anoxic brain injury.',
                                  'Reassess the stage over time; 2022 adds aetiology, phenotype, age and frailty as other risk axes.'], 'b1', 'f-s')
    return svg(y + 74, b)


def f22_scai_mortality():
    """Jentzer 2019, Mayo cardiac ICU, unadjusted in-hospital mortality by SCAI stage (abstract)."""
    h, b = bars([('A at risk (46.0% of patients)', 3.0, 'ok'),
                 ('B beginning (30.0%)', 7.1, 'b1'),
                 ('C classic (15.7%)', 12.4, 'b0'),
                 ('D deteriorating (7.3%)', 40.4, 'warn'),
                 ('E extremis (1.0%)', 67.0, 'warn')], '%', 80,
                'In-hospital death jumps from stage C to D (10,004 cardiac ICU patients)', 250)
    b += T(12, h + 4, 'Jentzer et al, JACC 2019, Mayo Clinic 2007 to 2015, unadjusted. Cardiac arrest added risk: adjusted OR 3.99.', 'f-s', 'start')
    return svg(h + 16, b)


def f22_mech_pathway():
    """ESC 2023 ACS guideline: mechanical complication pathway, with class and level."""
    b = box(150, 8, 420, 52, ['Warning signs after infarct: sudden hypotension, recurrent pain,',
                              'new murmur (acute MR or VSD), congestion, raised JVP'], 'b1', 'f-s')
    b += arrow(360, 60, 360, 80)
    b += box(170, 82, 380, 40, 'Emergency transthoracic echo (I C)', 'b0', 'f-h')
    b += arrow(360, 122, 360, 142)
    b += box(150, 144, 420, 40, 'Mechanical complication confirmed: Heart Team now', 'b1', 'f-h')
    b += arrow(250, 184, 130, 210) + arrow(360, 184, 360, 210) + arrow(470, 184, 590, 210)
    b += box(10, 212, 230, 86, ['Unstable or in shock:', 'IABP while awaiting', 'surgery (IIa C)'], 'warn', 'f-s')
    b += box(250, 212, 220, 86, ['Emergency surgical or', 'catheter repair if', 'haemodynamically', 'unstable (I C)'], 'ok', 'f-s')
    b += box(480, 212, 230, 86, ['Coronary disease:', 'CABG at the time', 'of repair (text,', 'no class given)'], 'b0', 'f-s')
    b += box(10, 310, 700, 40, ['Surgery is the treatment of choice; catheter repair for prohibitive risk. Pre-emptive temporary MCS:',
                                'a new trend, benefit unproven. Involve palliative care where appropriate.'], 'b1', 'f-s')
    return svg(360, b)


# ---- figs_F23.py



def _f23_card(x, y, w, h, head, lines, hcls='b1', bcls='b0', top=58):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="f-{bcls}"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="10" class="f-{hcls}"/>'
    out += T(x + w / 2, y + 22, head, 'f-h')
    out += T(x + w / 2, y + top, lines, 'f-s')
    return out


def f23_biopsy_route():
    """Transvenous right ventricular endomyocardial biopsy: route and sampling site."""
    b = ''
    # heart outline
    b += '<path d="M200 160 C200 120 250 110 290 118 L320 126 C370 116 440 130 470 180 C505 240 480 330 410 360 C350 382 300 362 262 326 C226 292 200 232 200 160 Z" class="f-b0"/>'
    # veins: right IJ and SVC into RA, IVC from below
    b += '<path d="M180 14 L182 90 C184 120 200 140 224 160" class="f-vessel"/>'
    b += '<path d="M232 280 L232 404" class="f-vessel"/>'
    # right atrium
    b += '<ellipse cx="250" cy="214" rx="42" ry="58" class="f-b1"/>'
    b += T(244, 206, 'RA', 'f-h')
    # tricuspid valve
    b += line(292, 222, 304, 262, 'f-cut') + line(304, 262, 300, 232, 'f-grid')
    b += T(286, 286, 'TV', 'f-s', 'end')
    # septum
    b += '<path d="M410 176 C440 230 444 300 412 350" class="f-l" style="stroke-width:6"/>'
    b += T(360, 210, 'RV', 'f-h')
    b += T(450, 150, 'LV', 'f-h')
    # sheath
    b += '<rect x="170" y="50" width="24" height="12" rx="3" class="f-b1"/>'
    # bioptome path (jugular)
    b += '<path d="M182 56 C184 120 200 146 228 172 C262 204 290 236 330 270 C360 296 384 312 410 316" class="f-l" style="stroke-width:2.6" marker-end="url(#ah)"/>'
    # femoral path
    b += '<path d="M240 404 C240 340 262 300 312 284" class="f-dash" marker-end="url(#ah)"/>'
    b += '<circle cx="412" cy="316" r="9" class="f-warn"/>'
    # labels on left
    b += T(160, 26, ['Right internal jugular', 'vein: usual route'], 'f-s', 'end')
    b += T(160, 72, '7 F sheath', 'f-s', 'end')
    b += T(220, 424, 'Femoral vein and IVC: alternative route', 'f-s', 'start')
    # labels on right
    b += T(500, 236, ['Bioptome passed down', 'the SVC, through the RA', 'and tricuspid valve'], 'f-s', 'start')
    b += line(496, 246, 336, 272, 'f-grid')
    b += T(500, 316, ['Sample the RV side of the', 'septum towards the apex;', '2 to 6 pieces, usually 4'], 'f-s', 'start')
    b += line(496, 320, 424, 318, 'f-grid')
    b += T(500, 172, ['Interventricular', 'septum'], 'f-s', 'start')
    b += line(496, 184, 432, 214, 'f-grid')
    # boxes
    b += box(10, 440, 345, 86, ['Serious events 1.0% of 1,896 biopsies:', 'severe TR in 12 (6 valve replacements),',
                                'tamponade in 6 (pericardiocentesis)', '(Strecker 2012, single centre)'], 'warn', 'f-s')
    b += box(365, 440, 345, 86, ['Before: INR under 1.5;', 'anticoagulant stopped 16 h before,',
                                 'restarted 12 h after', '(StatPearls)'], 'ok', 'f-s')
    return svg(536, b)


def f23_rejection_grading():
    """ISHLT 2004 cellular grades and 2013 pAMR grades on endomyocardial biopsy."""
    b = T(12, 22, 'Acute cellular rejection: ISHLT 2004 revised grades', 'f-h', 'start')
    cel = [('0R', 'None', ['No infiltrate'], 'Nothing', 'ok'),
           ('1R', 'Mild', ['Interstitial or', 'perivascular infiltrate;', 'up to 1 focus of', 'myocyte damage'], 'No treatment; repeat biopsy', 'b0'),
           ('2R', 'Moderate', ['2 or more foci of', 'infiltrate with', 'myocyte damage'], 'Treat (high-dose steroid)', 'b1'),
           ('3R', 'Severe', ['Diffuse infiltrate,', 'multifocal myocyte', 'damage, with or without', 'oedema, haemorrhage,', 'vasculitis'], 'Treat; ATG if severe', 'warn')]
    for i, (g, s, ls, act, c) in enumerate(cel):
        x = 10 + i * 177
        b += f'<rect x="{x}" y="36" width="168" height="168" rx="10" class="f-{c}"/>'
        b += T(x + 84, 62, g, 'f-big') + T(x + 84, 84, s, 'f-h')
        b += T(x + 84, 108, ls, 'f-s')
        b += f'<rect x="{x + 6}" y="212" width="156" height="40" rx="8" class="f-track"/>'
        b += T(x + 84, 236, act, 'f-s')
    b += T(360, 274, 'Any grade with haemodynamic compromise: methylprednisolone 1 g IV daily for 3 days (TSRA ch. 74)', 'f-s')
    y0 = 300
    b += T(12, y0, 'Antibody-mediated rejection: ISHLT 2013 pathological (pAMR) grades', 'f-h', 'start')
    amr = [('pAMR 0', ['Histology and', 'immunostaining', 'both negative'], 'ok'),
           ('pAMR 1 (H+)', ['Histology', 'positive,', 'immuno negative'], 'b0'),
           ('pAMR 1 (I+)', ['Histology', 'negative, C4d', 'or CD68 positive'], 'b0'),
           ('pAMR 2', ['Histology and', 'immunostaining', 'both positive'], 'b1'),
           ('pAMR 3', ['Severe: plus', 'myocyte necrosis,', 'thrombi, bleeding,', 'mixed infiltrate'], 'warn')]
    for i, (g, ls, c) in enumerate(amr):
        x = 10 + i * 141.6
        b += _f23_card(x, y0 + 14, 133, 118, g, ls, c, 'b0', top=60)
    b += box(10, y0 + 144, 345, 56, ['Histology: microvascular injury,', 'intravascular activated mononuclear cells'], 'b1', 'f-s')
    b += box(365, y0 + 144, 345, 56, ['Immuno positive: C4d in over 50% of', 'capillaries; CD68 in 10% or more'], 'b1', 'f-s')
    return svg(y0 + 210, b)


def f23_bslt():
    """Bilateral sequential lung transplant: sequence and anastomosis order."""
    b = ''
    # chest outline and clamshell incision
    b += '<path d="M60 70 C60 40 120 26 180 26 L540 26 C600 26 660 40 660 70 L660 300 C660 330 600 340 540 340 L180 340 C120 340 60 330 60 300 Z" class="f-track"/>'
    # heart
    b += '<ellipse cx="360" cy="150" rx="58" ry="66" class="f-b1"/>'
    b += T(360, 146, 'Heart', 'f-h') + T(360, 166, 'LA behind', 'f-s')
    # lungs
    b += '<path d="M290 70 C220 50 130 80 112 160 C100 220 150 300 240 300 C280 300 300 260 300 220 L300 110 Z" class="f-b0"/>'
    b += '<path d="M430 70 C500 50 590 80 608 160 C620 220 570 300 480 300 C440 300 420 260 420 220 L420 110 Z" class="f-b0"/>'
    b += T(360, 48, "Viewed from the front (patient's right on the left); numbers give the order, not the position", 'f-s')
    b += T(190, 120, ['Right lung', 'implant FIRST'], 'f-h') + T(530, 120, ['Left lung', 'implant SECOND'], 'f-h')
    b += T(190, 160, ['(worse side on V/Q;', 'right if no difference)'], 'f-s')
    b += T(530, 160, ['after the right lung is', 'reperfused and working'], 'f-s')
    # hilum numbered anastomoses right
    for cx, side in ((292, 'r'), (428, 'l')):
        b += f'<circle cx="{cx}" cy="110" r="13" class="f-warn"/>' + T(cx, 115, '1', 'f-h')
        b += f'<circle cx="{cx}" cy="150" r="13" class="f-ok"/>' + T(cx, 155, '2', 'f-h')
        b += f'<circle cx="{cx}" cy="190" r="13" class="f-b1"/>' + T(cx, 195, '3', 'f-h')
    b += '<path d="M90 236 C160 270 260 256 360 238 C460 256 560 270 630 236" class="f-cut" style="stroke-width:3"/>'
    b += T(360, 326, 'Incision (red): clamshell, 4th space, or bilateral anterior thoracotomies', 'f-s')
    # legend boxes
    yl = 356
    b += box(10, yl, 226, 78, ['1 Bronchus (deepest)', '4-0 running: membranous', 'wall, then cartilage'], 'warn', 'f-s')
    b += box(247, yl, 226, 78, ['2 Pulmonary artery', '5-0 Prolene running;', 'trim to avoid kinking'], 'ok', 'f-s')
    b += box(484, yl, 226, 78, ['3 Left atrial cuff', '4-0 Prolene, everting;', 'last stitches loose to de-air'], 'b1', 'f-s')
    b += box(10, yl + 90, 700, 58, ['Reperfuse: flush, release PA clamp gradually over about 10 min, tie LA suture; protective',
                                    'ventilation; confirm gases and haemodynamics before the second pneumonectomy'], 'b0', 'f-s')
    b += box(10, yl + 158, 700, 42, 'Support (CPB or ECMO) if: CI under 1.5, mean PAP over 40 to 50, SaO2 under 90%, RV failure', 'warn', 'f-s')
    return svg(yl + 210, b)


def f23_dcd_heart():
    """DCD heart trial (Schroder 2023) and PROCEED II results."""
    items = [('DCD on OCS, 6-month survival', 94, 'ok'),
             ('DBD cold storage, 6-month survival', 90, 'b0'),
             ('DCD, moderate or severe PGD', 22, 'warn'),
             ('DBD, moderate or severe PGD', 10, 'b1')]
    h, b = bars(items, '%', 100, 'DCD heart trial 2023: survival non-inferior, PGD twice as common', lab_w=290)
    items2 = [('OCS, 30-day survival', 94, 'ok'), ('Cold storage, 30-day survival', 97, 'b0')]
    h2, b2 = bars(items2, '%', 100, 'PROCEED II 2015 (DBD hearts): 30-day survival non-inferior', lab_w=290)
    return svg(h + h2, b + f'<g transform="translate(0,{h})">{b2}</g>')


def f23_evlp_trials():
    """Donor lung perfusion trials: conversion and PGD grade 3."""
    items = [('DEVELOP-UK (UK, EVLP)', 34, 'b1'), ('NOVEL (US, EVLP)', 50.9, 'ok')]
    h, b = bars(items, '%', 100, 'Rejected donor lungs used after EVLP: one-third to one-half', lab_w=290)
    items2 = [('INSPIRE: OCS Lung', 17.7, 'ok'), ('INSPIRE: cold storage', 29.7, 'b0'),
              ('NOVEL: EVLP lungs', 8.9, 'ok'), ('NOVEL: standard lungs', 9.5, 'b0')]
    h2, b2 = bars(items2, '%', 40, 'PGD grade 3 within 72 h: less with OCS Lung, same after EVLP', lab_w=290)
    items3 = [('DEVELOP-UK: EVLP recipients', 38.8, 'warn'), ('DEVELOP-UK: standard', 3.2, 'b0')]
    h3, b3 = bars(items3, '%', 40, 'DEVELOP-UK: ECMO after transplant much more frequent', lab_w=290)
    return svg(h + h2 + h3, b + f'<g transform="translate(0,{h})">{b2}</g>' + f'<g transform="translate(0,{h + h2})">{b3}</g>')


# ---- figs_F24.py



def f24_meso_pathway():
    """UK mesothelioma pathway from BTS 2018, ESMO 2021, NICE TA818/TA1125 and MARS 2."""
    b = T(12, 22, 'Pleural mesothelioma: the pathway as the 2026 evidence stands', 'f-h', 'start')
    b += box(170, 36, 380, 50, ['Unilateral pleural thickening or effusion,', 'asbestos history taken'], 'b1')
    b += arrow(360, 86, 360, 104)
    b += box(110, 106, 500, 66, ['Tissue: biopsy, thoracoscopy preferred (ESMO III, B);',
                                 'IHC with 2 mesothelial and 2 carcinoma markers;',
                                 'report subtype. Cytology alone only if biopsy not possible'], 'b0')
    b += arrow(360, 172, 360, 190)
    b += box(110, 192, 500, 50, ['Contrast CT thorax and upper abdomen; PET-CT only if', 'excluding spread would change management (BTS D)'], 'b0')
    b += arrow(250, 242, 110, 268) + arrow(360, 242, 360, 268) + arrow(470, 242, 610, 268)
    # three columns
    b += box(10, 270, 220, 120, ['Effusion', 'Talc (slurry or poudrage)', 'or IPC by choice (BTS A)', 'Talc over VATS partial', 'pleurectomy (BTS A)'], 'ok', 'f-s')
    b += box(250, 270, 220, 120, ['Radical surgery', 'No EPP (BTS B)', 'No EPD outside a trial', '(BTS D); MARS 2: worse', 'survival with EPD'], 'warn', 'f-s')
    b += box(490, 270, 220, 120, ['Systemic, ECOG 0 to 1', 'Nivolumab + ipilimumab', '(NICE TA818, 2 years)', 'or platinum-pemetrexed', '(BTS A, ESMO I, A)'], 'b0', 'f-s')
    b += box(10, 404, 340, 66, ['Radiotherapy: no prophylactic tract RT (BTS A);', 'no pre- or postoperative RT (BTS A);', 'palliative RT for localised pain (BTS D)'], 'b1', 'f-s')
    b += box(370, 404, 340, 66, ['Pembrolizumab + chemotherapy (IND.227):', 'NICE TA1125 terminated, no recommendation;', 'trials preferred at first and second line'], 'b1', 'f-s')
    b += T(360, 492, 'All patients: regional mesothelioma MDT, named nurse specialist, compensation advice (BTS D, GPP)', 'f-s')
    return svg(504, b)


def f24_meso_trials():
    """Median overall survival in the three randomised trials, from the trial abstracts."""
    items = [
        ('CheckMate 743: nivo + ipi', 18.1, 'b1'),
        ('CheckMate 743: chemotherapy', 14.1, 'track'),
        ('IND.227: pembro + chemo', 17.3, 'b1'),
        ('IND.227: chemotherapy', 16.1, 'track'),
        ('MARS 2: EPD + chemo', 19.3, 'warn'),
        ('MARS 2: chemotherapy alone', 24.8, 'ok'),
    ]
    h, b = bars(items, ' mo', 30, 'Immunotherapy added months; radical surgery cost them (median OS)', lab_w=260)
    b += T(12, h + 4, ['HR for death: CheckMate 743 0.74; IND.227 0.79. MARS 2: restricted mean survival',
                       'at 2 years 1.9 months lower with surgery. Different populations: MARS 2 took',
                       'resectable disease after two cycles of chemotherapy; the others, unresectable disease.'], 'f-s', 'start')
    return svg(h + 52, b)


def f24_cm743_histology():
    """CheckMate 743 median OS by histology, as reported in NICE TA818 (2-year data)."""
    items = [
        ('Non-epithelioid: nivo + ipi', 18.1, 'b1'),
        ('Non-epithelioid: chemotherapy', 8.8, 'track'),
        ('Epithelioid: nivo + ipi', 18.7, 'b1'),
        ('Epithelioid: chemotherapy', 16.5, 'track'),
    ]
    h, b = bars(items, ' mo', 25, 'CheckMate 743: the gain is concentrated in non-epithelioid disease', lab_w=260)
    b += T(12, h + 4, ['HR 0.46 (0.31 to 0.68) non-epithelioid; 0.86 (0.69 to 1.08) epithelioid (2-year data).',
                       'Subgroups were not powered; NICE TA818 did not restrict by histology.'], 'f-s', 'start')
    return svg(h + 34, b)


def f24_iaslc_criteria():
    """IASLC 2016 criteria for two lung tumours (Detterbeck, JTO 2016, Tables 2 and 3), redrawn as a comparison."""
    b = T(12, 22, 'Two lung tumours: separate primaries or one cancer? (IASLC 2016)', 'f-h', 'start')
    b += box(10, 36, 340, 36, 'Separate primary lung cancers', 'ok', 'f-h')
    b += box(370, 36, 340, 36, 'Single source (metastasis)', 'warn', 'f-h')
    b += T(360, 96, 'Decisive', 'f-h')
    b += box(10, 106, 340, 76, ['Clearly different histological types', 'Clearly different on comprehensive', 'histology (resected); squamous from CIS'], 'ok', 'f-s')
    b += box(370, 106, 340, 76, ['Exactly matching breakpoints on', 'comparative genomic hybridisation'], 'warn', 'f-s')
    b += T(360, 206, 'Relative (weigh together)', 'f-h')
    b += box(10, 216, 340, 110, ['Different appearance or PET uptake', 'Different driver mutation pattern', 'Different growth rates', 'No nodal or systemic metastases'], 'b0', 'f-s')
    b += box(370, 216, 340, 110, ['Same radiological appearance', 'Similar growth pattern', 'Significant nodal or systemic metastases', 'Same biomarker pattern and histotype'], 'b1', 'f-s')
    b += box(10, 340, 700, 50, ['Multiple ground-glass or lepidic lesions are neither: classify as multifocal lung cancer.',
                               'Final call by preponderance of evidence at an MDT. Martini-Melamed (1975) is to be replaced.'], 'b1', 'f-s')
    return svg(400, b)


def f24_mplc_decision():
    """Decision diagram for a second lung lesion, from ACCP 2013 and IASLC 2016."""
    b = box(200, 10, 320, 44, ['Proven or suspected NSCLC with', 'a second lung lesion'], 'b1', 'f-h')
    b += arrow(360, 54, 360, 72)
    b += box(110, 74, 500, 50, ['MDT judgement on clinical, radiological and histological', 'features (ACCP 2C; IASLC criteria)'], 'b0')
    b += arrow(360, 124, 360, 142)
    b += box(110, 144, 500, 50, ['Before resecting two primaries: invasive mediastinal', 'staging and extrathoracic imaging (ACCP 1B)'], 'b0')
    b += arrow(360, 194, 360, 212)
    b += box(230, 214, 260, 38, 'N2 or distant disease?', 'b1', 'f-h')
    b += arrow(490, 233, 548, 233) + T(518, 226, 'Yes', 'f-s')
    b += box(550, 210, 160, 46, ['Favours one cancer:', 'MDT, treat by stage'], 'warn', 'f-s')
    b += arrow(360, 252, 360, 270) + T(372, 266, 'No', 'f-s', 'start')
    # four outcome boxes
    xs = [10, 188, 366, 544]
    spec = [
        (['Same lobe', 'Lobectomy (1B);', 'no separate work-up', 'of the nodule (1B)'], 'ok'),
        (['Other ipsilateral', 'lobe: exclude benign', 'or primary (1C);', 'resect each (1B)'], 'ok'),
        (['Contralateral:', 'consider resecting', 'each if reserve', 'allows (2C)'], 'b0'),
        (['Multifocal ground-', 'glass: curative intent,', 'sublobar resection', 'of all if feasible (2C)'], 'b0'),
    ]
    b += line(98, 272, 632, 272)
    for x, (ls, c) in zip(xs, spec):
        b += arrow(x + 88, 272, x + 88, 288)
        b += box(x, 290, 176, 88, ls, c, 'f-s')
    b += box(10, 392, 700, 46, ['Unexpected second cancer in another lobe at operation: resect each lesion if reserve is adequate and N2 is', 'negative (1C). Lung-sparing resection keeps options open for the next primary.'], 'b1', 'f-s')
    return svg(448, b)


# ---- figs_F25.py



def f25_metabolic():
    b = box(250, 8, 220, 40, 'Surgical or traumatic injury', 'b1', 'f-h')
    b += arrow(300, 48, 170, 78) + arrow(420, 48, 550, 78)
    b += box(20, 80, 300, 54, ['Afferent nerve signals', 'hypothalamus, pituitary, sympathetic'], 'b0')
    b += box(400, 80, 300, 54, ['Tissue damage: cytokines', 'IL-6 peaks at 12 to 24 hours'], 'b0')
    b += arrow(110, 134, 110, 162) + arrow(250, 134, 250, 162)
    b += box(10, 164, 200, 112, ['Rise', 'ACTH, cortisol, GH,', 'vasopressin, prolactin,', 'catecholamines, glucagon,', 'renin, aldosterone'], 'warn', 'f-s')
    b += box(220, 164, 140, 112, ['Fall', 'insulin, testosterone,', 'oestrogen, T3', '', 'No change: TSH,', 'LH, FSH'], 'b1', 'f-s')
    b += arrow(550, 134, 550, 162)
    b += box(380, 164, 330, 112, ['Acute phase response (liver)', 'Up: CRP, fibrinogen, complement', 'Down: albumin, transferrin', 'Fever, neutrophilia, iron and zinc', 'sequestered, muscle proteolysis'], 'b0', 'f-s')
    b += arrow(180, 276, 180, 302) + arrow(545, 276, 545, 302)
    b += box(10, 304, 700, 96, ['Metabolic result: catabolism', 'Carbohydrate: more glucose made, less used; hyperglycaemia (insulin deficiency, then resistance)',
                               'Protein: muscle breakdown for gluconeogenesis and acute phase proteins (up to about 0.5 kg lean mass a day)',
                               'Fat: lipolysis and ketones · Salt and water: retained for 3 to 5 days (vasopressin, aldosterone); potassium lost'], 'b1', 'f-s')
    b += T(12, 422, 'Peak after surgery:  cortisol 0 to 4 h  ·  IL-6 12 to 24 h  ·  white cells 24 to 48 h  ·  CRP 24 to 72 h', 'f-s', 'start')
    b += T(12, 442, 'Cortisol cuts cytokine output (negative feedback); normal feedback on ACTH is lost', 'f-s', 'start')
    return svg(454, b)


def f25_vq():
    h, b = bars([('Right upper lobe', 35, 'warn'), ('Right middle lobe', 92, 'warn'), ('Right lower lobe', 63, 'warn'),
                 ('Left upper lobe', 4, 'ok'), ('Left lower lobe', 7, 'ok')],
                '%', 100, 'Planar zones misjudge the right lobes: patients whose lobar share differed by over 10% from SPECT/CT', 200)
    b += T(12, h + 4, 'Planar thirds cannot follow the fissures; the right middle lobe cannot be separated (n=75, Arnon-Sheleg, J Nucl Med 2020)', 'f-s', 'start')
    return svg(h + 16, b)


def f25_jet():
    b = T(12, 20, 'Manual jet (Sanders) ventilation through a rigid bronchoscope', 'f-h', 'start')
    b += box(10, 44, 130, 52, ['Oxygen', 'wall supply'], 'b1', 'f-s')
    b += arrow(140, 70, 172, 70)
    b += box(174, 44, 150, 52, ['Reducing valve', 'about 1.5 bar (20 psi)'], 'b0', 'f-s')
    b += arrow(324, 70, 356, 70)
    b += box(358, 44, 130, 52, ['Hand trigger', 'short bursts'], 'b0', 'f-s')
    b += '<path d="M488 70 C540 70 560 92 560 128" class="f-l"/>'
    # rigid scope, horizontal
    b += '<rect x="120" y="150" width="520" height="34" rx="6" class="f-track"/>'
    b += '<rect x="120" y="150" width="520" height="34" rx="6" class="f-b1" style="fill-opacity:0.25"/>'
    b += T(380, 172, 'Rigid bronchoscope barrel (open at the proximal end)', 'f-s')
    b += '<path d="M560 128 L560 150" class="f-l" marker-end="url(#ah)"/>'
    b += T(548, 140, 'Injector needle at side port', 'f-s', 'end')
    b += arrow(80, 160, 118, 160) + arrow(80, 176, 118, 176)
    b += T(74, 158, ['Room air', 'entrained'], 'f-s', 'end')
    b += arrow(640, 167, 700, 167)
    b += T(700, 202, ['Into the trachea:', 'jet plus entrained air'], 'f-s', 'end')
    b += '<path d="M118 196 C90 210 70 214 50 214" class="f-dash" marker-end="url(#ah)"/>'
    b += T(40, 236, 'Passive expiration out of the open barrel: keep this path clear', 'f-s', 'start')
    b += box(10, 254, 345, 108, ['Settings (de Lima 2018)', 'Driving pressure about 1.5 bar (20 psi)', 'Inspiration 30 to 40% of the cycle',
                                 'Low frequency 10 to 30/min; high 120 to 600/min', 'PEEP held at 10 cmH2O or less'], 'b0', 'f-s')
    b += box(365, 254, 345, 108, ['Dangers', 'Barotrauma: pneumothorax, surgical emphysema', 'Air trapping if expiration is blocked',
                                  'Hypercapnia: check end-tidal CO2 in pauses', 'Entrained air lowers and varies the FiO2'], 'warn', 'f-s')
    return svg(372, b)


def f25_pleural():
    b = T(360, 18, 'Pleural fluid turnover (rabbit figures, mL/kg/h, Zocchi 2002)', 'f-h')
    b += '<rect x="10" y="34" width="700" height="60" rx="8" class="f-b1"/>'
    b += T(360, 58, 'Chest wall: parietal pleura over systemic capillaries (intercostal arteries)', 'f-s')
    b += T(360, 76, 'Capillary pressure about 18 cmH2O (dog)', 'f-s')
    b += '<rect x="10" y="98" width="700" height="160" rx="4" class="f-track"/>'
    b += arrow(60, 80, 60, 142) + T(76, 124, 'Filtration 0.15 to 0.20 (net about +4 cmH2O)', 'f-n', 'start')
    b += arrow(680, 142, 680, 80) + T(664, 124, 'Stomata to lymph 0.07', 'f-n', 'end')
    b += T(360, 166, 'Pleural space: about 0.26 mL/kg in man, 5 to 24 micrometres thick', 'f-s')
    b += T(360, 184, 'Liquid pressure about -6 to -9 cmH2O; protein 0.9 to 2.5 g/dL; pH about 7.6', 'f-s')
    b += T(360, 202, 'Cells about 1,700 per mm3, mostly macrophages', 'f-s')
    b += T(76, 242, 'Starling absorption 0.10', 'f-n', 'start')
    b += T(436, 242, 'Cellular: ion-coupled 0.07, vesicles 0.02', 'f-s', 'start')
    b += '<rect x="10" y="262" width="700" height="60" rx="8" class="f-b0"/>'
    b += T(360, 290, 'Lung: visceral pleura (bronchial supply); pulmonary capillary pressure about 10 cmH2O', 'f-s')
    b += T(360, 308, 'Absorbs by Starling forces (net about 4 cmH2O)', 'f-s')
    b += arrow(60, 214, 60, 276) + arrow(420, 214, 420, 276)
    b += box(10, 334, 345, 94, ['Lymphatic stomata', 'Parietal pleura only: diaphragm, lower', 'intercostal spaces, caudal mediastinum',
                                '1 to 6 micrometres; open wider on inspiration'], 'ok', 'f-s')
    b += box(365, 334, 345, 94, ['Reserve and failure', 'Lymph flow rises steeply with volume:', 'about 20-fold in sheep; human estimate',
                                 'about 34 rising to about 700 mL/day'], 'warn', 'f-s')
    return svg(438, b)


def f25_goitre():
    b = T(12, 20, 'Retrosternal goitre: lowest extent on CT sets the approach', 'f-h', 'start')
    levels = [(58, 'Neck'), (110, 'Thoracic inlet'), (190, 'Aortic arch'), (262, 'Pericardium'), (330, 'Right atrium')]
    for y, lab in levels:
        b += line(20, y, 300, y, 'f-grid') + T(24, y - 6, lab, 'f-s', 'start')
    # goitre shapes
    b += '<path d="M220 50 C258 50 266 100 254 140 C246 168 196 168 188 140 C176 100 184 50 220 50 Z" class="f-ok"/>'
    b += T(221, 128, '1', 'f-big')
    b += '<path d="M282 54 C306 56 310 120 306 190 C304 238 272 244 268 200 C262 140 260 56 282 54 Z" class="f-b0"/>'
    b += T(287, 200, '2', 'f-big')
    b += '<path d="M160 60 C184 60 190 140 186 220 C184 300 176 336 160 336 C142 336 136 290 138 220 C140 140 138 60 160 60 Z" class="f-warn"/>'
    b += T(162, 290, '3', 'f-big')
    b += box(320, 36, 390, 56, ['Grade 1: above the aortic arch', 'Cervical collar incision (about 95%)'], 'ok', 'f-s')
    b += box(320, 100, 390, 56, ['Grade 2: arch to pericardium', 'Manubriotomy or partial sternotomy'], 'b0', 'f-s')
    b += box(320, 164, 390, 56, ['Grade 3: down to the right atrium', 'Full sternotomy'], 'warn', 'f-s')
    b += box(320, 228, 390, 56, ['Posterior mediastinal, to the posterior pleura', 'Neck plus right posterolateral thoracotomy'], 'warn', 'f-s')
    b += box(320, 292, 390, 70, ['CT signs that favour a sternal approach', 'Below the arch or carina · posterior extension', 'Conical, wider than the inlet · ectopic or recurrent'], 'b1', 'f-s')
    b += T(12, 384, 'Grades from Huins et al., Int J Surg 2008 (as given in StatPearls); approaches from Simo, Nixon, Ofo (Open Atlas)', 'f-s', 'start')
    return svg(396, b)


def f25_blocks():
    b = T(12, 20, 'Paravertebral and erector spinae plane targets (transverse section, one side)', 'f-h', 'start')
    # skin line
    b += line(20, 50, 700, 50, 'f-grid') + T(24, 44, 'Skin (posterior)', 'f-s', 'start')
    # erector spinae muscle
    b += '<path d="M80 62 C160 56 300 58 380 70 C390 100 380 128 360 136 L100 136 C80 120 76 90 80 62 Z" class="f-b1"/>'
    b += T(230, 100, 'Erector spinae muscle', 'f-s')
    # vertebral body and spinous process
    b += '<rect x="30" y="150" width="40" height="80" rx="8" class="f-b1"/>' + T(50, 248, 'Lamina', 'f-s')
    b += '<path d="M70 156 L330 148 L332 166 L70 176 Z" class="f-b0"/>'
    b += T(200, 186, 'Transverse process', 'f-s')
    # ESP injection layer
    b += '<path d="M100 142 L360 140" class="f-duct"/>'
    # SCTL
    b += line(330, 170, 430, 232, 'f-dash')
    b += T(440, 240, ['Superior costo-', 'transverse ligament'], 'f-s', 'start')
    # paravertebral space wedge
    b += '<path d="M70 236 L340 180 L430 236 L360 280 L70 280 Z" class="f-ok" style="fill-opacity:0.55"/>'
    b += T(200, 262, 'Paravertebral space', 'f-h')
    # pleura
    b += '<path d="M60 296 C200 296 420 290 700 250" class="f-l"/>'
    b += T(600, 300, 'Parietal pleura', 'f-s', 'start')
    b += '<path d="M100 290 L120 270" class="f-nerve"/>'
    b += T(24, 316, 'Spinal nerve, sympathetic chain and intercostal vessels lie in the space', 'f-s', 'start')
    # needles
    b += '<path d="M470 54 L362 140" class="f-cut"/>' + T(478, 70, ['ESP: needle onto the tip of', 'the transverse process, deep', 'to the muscle; fluid lifts it'], 'f-s', 'start')
    b += '<path d="M560 110 L370 232" class="f-cut"/>' + T(568, 140, ['PVB: through the', 'ligament; pleura', 'pushed down'], 'f-s', 'start')
    b += box(10, 330, 345, 92, ['Paravertebral (Nair 2020)', 'T4 to T5 for thoracic surgery', '20 to 25 ml covers 4 to 5 dermatomes',
                                'Pneumothorax, puncture, hypotension each under 1%'], 'b0', 'f-s')
    b += box(365, 330, 345, 92, ['Erector spinae (Chin 2021)', 'Over 10 ml; 20 to 30 ml usual', 'Spread 3 to 6 levels, mostly in the plane',
                                 'Dorsal rami always; ventral rami variable'], 'b0', 'f-s')
    return svg(432, b)


# ---- figs_F26.py



def _f26_torso(cx, top=50, bot=330, half=72):
    """Simple torso outline (no arms), centred on cx."""
    return (f'<path d="M{cx - 30} {top} L{cx - half + 4} {top + 16} L{cx - half} {top + 80} '
            f'L{cx - half + 10} {bot - 60} L{cx - half + 16} {bot} L{cx + half - 16} {bot} '
            f'L{cx + half - 10} {bot - 60} L{cx + half} {top + 80} L{cx + half - 4} {top + 16} '
            f'L{cx + 30} {top} Z" class="f-b0"/>')


def _f26_num(x, y, n, cls='b1'):
    return (f'<circle cx="{x}" cy="{y}" r="11" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def f26_flap_sites():
    """Flap and skeletal choice by chest wall defect site (front and back schematic)."""
    b = T(12, 22, 'Chest wall defect site and first-choice cover', 'f-h', 'start')
    # front torso
    fx = 100
    b += _f26_torso(fx)
    b += f'<rect x="{fx - 8}" y="66" width="16" height="130" rx="5" class="f-track"/>'
    for i in range(6):
        y = 92 + i * 30
        b += f'<path d="M{fx - 12} {y} C{fx - 40} {y + 6} {fx - 56} {y + 12} {fx - 62} {y + 22}" class="f-grid" fill="none"/>'
        b += f'<path d="M{fx + 12} {y} C{fx + 40} {y + 6} {fx + 56} {y + 12} {fx + 62} {y + 22}" class="f-grid" fill="none"/>'
    b += f'<rect x="{fx - 26}" y="60" width="52" height="62" rx="8" class="f-dash"/>'
    b += _f26_num(fx, 91, 1, 'warn')
    b += f'<rect x="{fx - 16}" y="128" width="32" height="76" rx="8" class="f-dash"/>'
    b += _f26_num(fx, 166, 2, 'warn')
    b += f'<ellipse cx="{fx + 44}" cy="176" rx="18" ry="34" class="f-dash"/>'
    b += _f26_num(fx + 44, 176, 3)
    b += f'<ellipse cx="{fx - 54}" cy="170" rx="13" ry="34" class="f-dash"/>'
    b += _f26_num(fx - 54, 170, 4)
    b += T(fx, 352, 'Front', 'f-h')
    # back torso
    bx = 268
    b += _f26_torso(bx)
    b += f'<line x1="{bx}" y1="58" x2="{bx}" y2="322" class="f-grid"/>'
    for s in (-1, 1):
        b += (f'<path d="M{bx + s * 12} 78 L{bx + s * 52} 72 L{bx + s * 30} 148 Z" class="f-track"/>'
              f'<path d="M{bx + s * 12} 78 L{bx + s * 52} 72 L{bx + s * 30} 148 Z" class="f-l"/>')
    b += f'<line x1="{bx - 70}" y1="150" x2="{bx + 70}" y2="150" class="f-dash"/>'
    b += T(bx, 168, 'scapular tip, about 4th rib', 'f-s')
    b += _f26_num(bx + 34, 108, 5, 'ok')
    b += f'<ellipse cx="{bx + 34}" cy="222" rx="24" ry="30" class="f-dash"/>'
    b += _f26_num(bx + 34, 222, 6)
    b += T(bx, 352, 'Back', 'f-h')
    # legend
    rows = [
        (1, 'warn', 'Sternum and upper anterior wall',
         ['Pectoralis major: thoracoacromial (dominant)', 'plus IMA perforators; advancement preferred']),
        (2, 'warn', 'Total sternectomy, long vertical defect',
         ['VRAM: robust skin island; rectus', 'flaps carry hernia risk about 13%']),
        (3, 'b1', 'Anterolateral',
         ['Latissimus dorsi; or TRAM, which', 'covers defects up to about 40 cm']),
        (4, 'b1', 'Lateral',
         ['Latissimus dorsi (thoracodorsal): the', 'workhorse; seroma in up to 79%']),
        (5, 'ok', 'Upper posterior, under the scapula',
         ['Skeletal repair usually not needed up', 'to about 10 cm; muscle cover alone']),
        (6, 'b1', 'Posterior, below the 4th rib',
         ['Reconstruct: scapular tip can catch', 'in the defect; latissimus cover']),
    ]
    for i, (n, cls, head, sub) in enumerate(rows):
        y = 44 + i * 52
        b += _f26_num(366, y + 10, n, cls)
        b += T(386, y + 15, head, 'f-h', 'start')
        b += T(386, y + 32, sub, 'f-s', 'start')
    b += box(10, 368, 700, 62, ['Fallbacks: omentum for anterior defects when pedicled flaps fail or are unsuitable (needs a skin graft;',
                                'abdominal morbidity). Free flap when local muscles are resected, injured or irradiated:',
                                'internal mammary vessels for anterior, thoracodorsal for lateral recipients'], 'b1', 'f-s')
    return svg(440, b)


def f26_subxiphoid_window():
    """Subxiphoid pericardial window: surface marking, sagittal view and numbered sequence."""
    b = T(12, 22, 'Subxiphoid pericardial window, step by step', 'f-h', 'start')
    # Panel A: surface view
    cx = 110
    b += T(cx, 46, 'A  Surface', 'f-h')
    b += f'<rect x="{cx - 9}" y="60" width="18" height="110" rx="4" class="f-track"/>'
    b += f'<rect x="{cx - 9}" y="60" width="18" height="110" rx="4" class="f-dash"/>'
    b += T(cx - 16, 96, 'Sternum', 'f-s', 'end')
    b += f'<path d="M{cx - 7} 170 L{cx} 194 L{cx + 7} 170" class="f-l"/>'
    b += T(cx + 12, 188, 'Xiphoid', 'f-s', 'start')
    b += f'<path d="M{cx - 10} 168 C{cx - 40} 190 {cx - 70} 214 {cx - 90} 252" class="f-l"/>'
    b += f'<path d="M{cx + 10} 168 C{cx + 40} 190 {cx + 70} 214 {cx + 90} 252" class="f-l"/>'
    b += T(22, 272, 'Costal margin', 'f-s', 'start')
    b += f'<line x1="{cx}" y1="180" x2="{cx}" y2="236" class="f-cut" style="stroke-width:4"/>'
    b += T(cx, 254, '3 to 5 cm midline incision', 'f-s')
    b += (f'<line x1="{cx + 28}" y1="272" x2="{cx + 38}" y2="282" class="f-cut"/>'
          f'<line x1="{cx + 38}" y1="272" x2="{cx + 28}" y2="282" class="f-cut"/>')
    b += T(cx + 46, 276, ['Drain via', 'stab wound'], 'f-s', 'start')
    # Panel B: sagittal
    sx = 250
    b += T(sx + 120, 46, 'B  Side view', 'f-h')
    b += f'<path d="M{sx + 14} 60 L{sx + 34} 178" class="f-l" style="stroke-width:8;stroke-linecap:round"/>'
    b += f'<path d="M{sx + 34} 178 L{sx + 46} 202" class="f-dash" style="stroke-width:3"/>'
    b += T(sx + 28, 214, 'Xiphoid excised', 'f-s', 'end')
    b += f'<ellipse cx="{sx + 130}" cy="140" rx="74" ry="58" class="f-track"/>'
    b += f'<ellipse cx="{sx + 130}" cy="140" rx="74" ry="58" class="f-l"/>'
    b += f'<ellipse cx="{sx + 136}" cy="136" rx="48" ry="36" class="f-b1"/>'
    b += T(sx + 136, 141, 'Heart', 'f-h')
    b += T(sx + 196, 80, 'Effusion', 'f-s', 'start')
    b += f'<path d="M{sx + 98} 192 Q{sx + 116} 202 {sx + 138} 199" class="f-cut" style="stroke-width:5"/>'
    b += T(sx + 146, 224, '2 to 3 cm window', 'f-s', 'start')
    b += f'<path d="M{sx + 6} 262 C{sx + 80} 226 {sx + 160} 226 {sx + 236} 262" class="f-l"/>'
    b += T(sx + 176, 284, 'Diaphragm', 'f-s', 'start')
    b += f'<path d="M{sx + 70} 268 C{sx + 100} 254 {sx + 140} 256 {sx + 170} 268 L{sx + 170} 306 L{sx + 70} 306 Z" class="f-b0"/>'
    b += T(sx + 120, 294, 'Liver', 'f-s')
    b += f'<path d="M{sx + 22} 290 C{sx + 44} 262 {sx + 76} 226 {sx + 108} 196" class="f-duct" style="stroke-width:3"/>'
    b += T(sx + 16, 308, 'Drain', 'f-s', 'start')
    # Panel C: steps
    steps = [
        '1 Supine; GA (local possible)',
        '2 Incise over xiphoid into midline',
        '3 Open linea alba; excise xiphoid',
        '4 Finger dissection behind sternum;',
        '   lift it; expose lower pericardium',
        '5 Grasp, open, suck out fluid;',
        '   send fluid and excised patch',
        '6 Finger sweep: loculi, adhesions,',
        '   nodules; inspect epicardium',
        '7 28 to 32 F drain into pericardium',
        '   via stab wound; layered closure',
    ]
    b += '<rect x="500" y="36" width="210" height="258" rx="9" class="f-b0"/>'
    b += T(605, 56, 'C  Sequence', 'f-h')
    for i, st in enumerate(steps):
        b += T(508, 80 + i * 19, st, 'f-s', 'start')
    b += box(10, 324, 700, 46, ['Drain out at under 100 ml in 24 h (usually 48 to 72 h). Advantages: supine, quick, local anaesthesia',
                                'possible, no one-lung ventilation. Weakness: more recurrence than thoracotomy (9.4% against 0%, Langdon 2016)'], 'warn', 'f-s')
    return svg(380, b)


def f26_window_outcomes():
    """Langdon 2016: subxiphoid against left anterior mini-thoracotomy window."""
    h1, b1 = bars([('Subxiphoid (n=127)', 9.4, 'warn'), ('Anterior thoracotomy (n=52)', 0, 'b0')],
                  '%', 12, 'Recurrent moderate or large effusion: subxiphoid more (P=0.02)')
    h2, b2 = bars([('Subxiphoid', 32.4, 'b0'), ('Anterior thoracotomy', 78.3, 'warn')],
                  ' mg', 100, 'IV morphine equivalent in first 48 h: thoracotomy more (P=0.0001)')
    h3, b3 = bars([('Subxiphoid', 7.1, 'b1'), ('Anterior thoracotomy', 7.7, 'b1')],
                  '%', 12, '30-day mortality: no difference (P=1.00)')
    b = b1 + f'<g transform="translate(0,{h1})">{b2}</g>' + f'<g transform="translate(0,{h1 + h2})">{b3}</g>'
    b += T(12, h1 + h2 + h3 + 8, 'Langdon, Seery, Kulik, J Cardiothorac Surg 2016; retrospective, 179 windows, 2002 to 2015', 'f-s', 'start')
    return svg(h1 + h2 + h3 + 20, b)


def f26_incision_map():
    """Thoracic incisions and their complications, with sourced numbers."""
    b = T(12, 22, 'Incisions and what goes wrong with them', 'f-h', 'start')
    # front torso
    fx = 150
    b += (f'<path d="M{fx - 40} 44 L{fx - 104} 64 L{fx - 112} 150 L{fx - 98} 280 L{fx - 90} 320 '
          f'L{fx + 90} 320 L{fx + 98} 280 L{fx + 112} 150 L{fx + 104} 64 L{fx + 40} 44 Z" class="f-b0"/>')
    b += T(fx, 340, 'Front', 'f-h')
    b += T(fx - 70, 40, "patient's right", 'f-s', 'middle')
    # nipples
    b += f'<circle cx="{fx - 58}" cy="140" r="4" class="f-b1"/><circle cx="{fx + 58}" cy="140" r="4" class="f-b1"/>'
    # sternotomy
    b += f'<line x1="{fx}" y1="58" x2="{fx}" y2="200" class="f-cut" style="stroke-width:4"/>'
    b += _f26_num(fx + 16, 80, 1, 'warn')
    # clamshell: inframammary curve across sternum
    b += f'<path d="M{fx - 100} 150 C{fx - 70} 176 {fx - 30} 172 {fx} 164 C{fx + 30} 172 {fx + 70} 176 {fx + 100} 150" class="f-cut" style="stroke-width:3"/>'
    b += _f26_num(fx + 74, 188, 2, 'warn')
    # right anterior mini-thoracotomy (viewer's left)
    b += f'<path d="M{fx - 82} 196 C{fx - 70} 204 {fx - 52} 206 {fx - 38} 202" class="f-cut" style="stroke-width:4"/>'
    b += _f26_num(fx - 60, 222, 3, 'warn')
    # subxiphoid
    b += f'<line x1="{fx}" y1="214" x2="{fx}" y2="250" class="f-cut" style="stroke-width:4"/>'
    b += _f26_num(fx + 16, 238, 4, 'warn')
    # side view (patient's left side up, back to the right)
    sx = 420
    b += f'<rect x="{sx - 110}" y="50" width="220" height="270" rx="60" class="f-b0"/>'
    b += T(sx, 340, 'Left side (back to the right)', 'f-h')
    b += f'<path d="M{sx + 40} 70 L{sx + 92} 74 L{sx + 70} 160 Z" class="f-track"/>'
    b += f'<path d="M{sx + 40} 70 L{sx + 92} 74 L{sx + 70} 160 Z" class="f-l"/>'
    b += T(sx + 74, 66, 'Scapula', 'f-s', 'middle')
    for i in range(5):
        y = 120 + i * 32
        b += f'<path d="M{sx - 96} {y + 24} C{sx - 30} {y + 6} {sx + 40} {y} {sx + 100} {y - 8}" class="f-grid" fill="none"/>'
    # posterolateral thoracotomy around scapular tip
    b += f'<path d="M{sx - 70} 196 C{sx - 20} 196 {sx + 40} 186 {sx + 70} 172 C{sx + 84} 160 {sx + 92} 130 {sx + 96} 104" class="f-cut" style="stroke-width:4"/>'
    b += _f26_num(sx - 80, 216, 5, 'warn')
    # VATS ports
    for (px, py) in [(sx - 60, 252), (sx - 10, 236), (sx + 30, 274)]:
        b += f'<circle cx="{px}" cy="{py}" r="6" class="f-b1"/>'
    b += _f26_num(sx + 56, 254, 6)
    # legend
    leg = [
        (1, 'Sternotomy: deep wound infection,', 'dehiscence (Cardiac 17 tab)'),
        (2, 'Clamshell: sternal problem needing', 'surgery 11.4% (Kim 2025); IMAs tied'),
        (3, 'Mini-thoracotomy: lung hernia, 20', 'in 1,381 MICS (Cetinkaya 2020)'),
        (4, 'Subxiphoid: less pain than anterior', 'thoracotomy (Langdon 2016)'),
        (5, 'Thoracotomy: chronic pain 57% at 3 mo,', '47% at 6 mo (Bayman 2014)'),
        (6, 'VATS: chronic pain 35% pooled; three', 'ports OR 4.3 (Chen 2023)'),
    ]
    for i, (n, l1, l2) in enumerate(leg):
        col, row = i % 2, i // 2
        x, y = 10 + col * 355, 362 + row * 46
        b += _f26_num(x + 12, y + 14, n, 'warn' if n < 6 else 'b1')
        b += T(x + 30, y + 12, l1, 'f-s', 'start')
        b += T(x + 30, y + 29, l2, 'f-s', 'start')
    b += box(560, 50, 150, 120, ['Intercostal nerve', 'injury: retractor,', 'rib fracture,', 'pericostal sutures,', 'drains, rigid ports'], 'b1', 'f-s')
    b += box(560, 186, 150, 120, ['Lower risk: no rib', 'spreader, fewer', 'ports, early drain', 'removal, intracostal', 'closure'], 'ok', 'f-s')
    return svg(506, b)


def f26_chronic_pain():
    """Chronic pain after thoracotomy and VATS, from two meta-analyses and one cohort."""
    h, b = bars([
        ('Thoracotomy, 3 months (meta-analysis)', 57, 'warn'),
        ('Thoracotomy, 6 months (meta-analysis)', 47, 'warn'),
        ('VATS, pooled (meta-analysis)', 35.3, 'b0'),
        ('Thoracotomy, 6 months (Iowa cohort)', 33, 'warn'),
        ('VATS, 6 months (Iowa cohort)', 25, 'b0'),
    ], '%', 70, 'Chronic pain: about half after thoracotomy; VATS lowers it but does not abolish it', lab_w=300)
    b += T(12, h + 4, 'Bayman and Brennan 2014 (thoracotomy, 17 and 15 studies); Chen 2023 (VATS, 17 studies); Bayman 2017 (99 patients)', 'f-s', 'start')
    return svg(h + 16, b)


# ---- figs_F27.py
"""F27 figures: AKI (KDIGO, trials), GI complications, mesenteric ischaemia pathway,
internal jugular ultrasound view, thoracic and cardiac VTE prophylaxis chart."""



def _f27_card(x, y, w, h, head, lines, cls='b0', hcls='b1'):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="f-{cls}"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="10" class="f-{hcls}"/>'
    out += T(x + w / 2, y + 21, head, 'f-h')
    out += T(x + w / 2, y + 54, lines, 'f-s')
    return out


def f27_kdigo():
    b = T(12, 20, 'KDIGO 2012 staging of acute kidney injury: the higher stage by either criterion counts', 'f-h', 'start')
    spec = [('Stage 1', 'ok', ['1.5 to 1.9 x baseline', 'or a rise of 26.5 µmol/L', '(0.3 mg/dL) or more in 48 h'],
             ['under 0.5 ml/kg/h', 'for 6 to 12 hours']),
            ('Stage 2', 'warn', ['2.0 to 2.9 x baseline', '', ''],
             ['under 0.5 ml/kg/h', 'for 12 hours or more']),
            ('Stage 3', 'warn', ['3 x baseline or more,', 'or 354 µmol/L (4.0 mg/dL)', 'or more, or RRT started'],
             ['under 0.3 ml/kg/h for 24 h', 'or anuria for 12 hours'])]
    for i, (st, hc, cr, uo) in enumerate(spec):
        x = 10 + i * 238
        b += f'<rect x="{x}" y="34" width="226" height="214" rx="10" class="f-b0"/>'
        b += f'<rect x="{x}" y="34" width="226" height="34" rx="10" class="f-{hc}"/>'
        b += T(x + 113, 57, st, 'f-h')
        b += T(x + 113, 90, 'Serum creatinine', 'f-h')
        b += T(x + 113, 110, cr, 'f-s')
        b += line(x + 16, 168, x + 210, 168, 'f-grid')
        b += T(x + 113, 190, 'Urine output', 'f-h')
        b += T(x + 113, 210, uo, 'f-s')
    b += box(10, 260, 700, 44, ['After bypass, haemodilution can leave creatinine below the preoperative value,',
                               'so creatinine alone misses or delays AKI: use urine output as well (ADQI 20)'], 'b1', 'f-s')
    return svg(314, b)


def f27_aki_trials():
    h1, b1 = bars([('Accelerated: 90-day death', 43.9, 'b1'), ('Standard: 90-day death', 43.7, 'b1'),
                   ('Accelerated: RRT-dependent', 10.4, 'warn'), ('Standard: RRT-dependent', 6.0, 'ok'),
                   ('Accelerated: adverse events', 23.0, 'warn'), ('Standard: adverse events', 16.5, 'ok')],
                  '%', 60, 'STARRT-AKI (n=2,927): earlier RRT did not save lives and left more on dialysis', 260)
    h2, b2 = bars([('KDIGO bundle: any AKI', 55.1, 'ok'), ('Standard care: any AKI', 71.7, 'warn'),
                   ('KDIGO bundle: stage 2 or 3', 29.7, 'ok'), ('Standard care: stage 2 or 3', 44.9, 'warn')],
                  '%', 100, 'PrevAKI (n=276, biomarker-positive): the KDIGO bundle cut AKI within 72 h', 260)
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


def f27_gi_mortality():
    h, b = bars([('Mesenteric ischaemia (n=104)', 45, 'warn'), ('Liver, pancreas, biliary (n=139)', 27, 'warn'),
                 ('GI bleeding (n=259)', 17, 'b1'), ('Any serious GI complication', 14, 'b1'),
                 ('No GI complication', 1.6, 'ok')], '%', 60,
                'In-hospital mortality by GI complication: mesenteric ischaemia kills almost half', 280)
    return svg(h, b)


def f27_mesenteric():
    b = box(150, 6, 420, 58, ['Suspect: lactate not clearing despite resuscitation, high or rising',
                              'vasopressors, distension, feed intolerance, bloody stool, new sepsis'], 'b1', 'f-s')
    b += arrow(360, 64, 360, 82)
    b += box(150, 84, 420, 44, ['Optimise output and volume; cut vasoconstrictors if possible;',
                               'measure bladder pressure; no single lactate or D-dimer decides'], 'b0', 'f-s')
    b += arrow(360, 128, 360, 146)
    b += box(150, 148, 420, 40, 'Urgent CT angiography, arterial and venous phases, any renal function', 'b0', 'f-s')
    b += arrow(250, 188, 120, 216) + arrow(360, 188, 360, 216) + arrow(470, 188, 600, 216)
    b += _f27_card(10, 218, 220, 116, 'Embolus or thrombus', ['SMA occluded:', 'revascularise first', '(endovascular often),', 'then resect dead bowel'], 'b0', 'warn')
    b += _f27_card(250, 218, 220, 116, 'NOMI pattern', ['Poor enhancement, wall', 'thickening, pneumatosis,', 'portal gas; SMA patent'], 'b0', 'warn')
    b += _f27_card(490, 218, 220, 116, 'Peritonitis or necrosis', ['Laparotomy without', 'delaying for imaging;', 'resect, leave in', 'discontinuity'], 'b0', 'warn')
    b += arrow(300, 334, 250, 360) + arrow(420, 334, 470, 360)
    b += box(90, 362, 260, 56, ['Abdominal compartment syndrome:', 'decompression laparotomy (I C)'], 'warn', 'f-s')
    b += box(370, 362, 260, 56, ['Consider papaverine into the SMA: 80 mg,', 'then 30 to 60 mg/h for 24 to 72 h (IIb C)'], 'ok', 'f-s')
    b += box(10, 432, 700, 40, 'Resection after revascularisation: no primary anastomosis, planned second look (IIa C); antibiotics for all (I C)', 'b1', 'f-s')
    return svg(482, b)


def f27_ij_ultrasound():
    b = T(180, 20, 'Transverse (short-axis) view, right neck', 'f-h')
    # skin line and probe
    b += '<rect x="80" y="34" width="200" height="22" rx="6" class="f-b1"/>' + T(180, 50, 'Probe, marker to patient right', 'f-s')
    b += line(40, 60, 320, 60, 'f-l')
    b += T(36, 64, 'Skin', 'f-s', 'end')
    # sternocleidomastoid
    b += '<path d="M70 72 C120 66 240 66 290 78 L280 104 C220 96 130 96 80 100 Z" class="f-b0"/>'
    b += T(180, 90, 'Sternocleidomastoid', 'f-s')
    # IJV (lateral, larger, compressible) and carotid (medial, round)
    b += '<ellipse cx="140" cy="140" rx="44" ry="28" class="f-lumen"/>' + T(140, 145, 'IJV', 'f-h')
    b += '<circle cx="232" cy="150" r="20" class="f-lumen"/>' + T(232, 155, 'CCA', 'f-h')
    b += T(140, 186, ['Lateral, larger,', 'compresses, fills', 'with head down'], 'f-s')
    b += T(250, 196, ['Medial, round,', 'pulsatile'], 'f-s')
    b += T(60, 240, 'Lateral', 'f-s') + T(300, 240, 'Medial', 'f-s')
    # needle out-of-plane target
    b += '<circle cx="140" cy="122" r="4" class="f-cut"/>'
    b += arrow(80, 120, 132, 122)
    b += T(76, 116, 'Tip', 'f-s', 'end')
    # right panel: long axis in-plane
    b += line(360, 10, 360, 260, 'f-dash')
    b += T(540, 20, 'Long-axis (in-plane) view', 'f-h')
    b += '<rect x="440" y="34" width="200" height="22" rx="6" class="f-b1"/>'
    b += line(390, 60, 700, 60, 'f-l')
    b += '<path d="M400 120 L700 120 L700 160 L400 160 Z" class="f-lumen"/>' + T(620, 145, 'IJV', 'f-h')
    b += T(540, 50, 'Probe', 'f-s')
    b += '<line x1="430" y1="60" x2="520" y2="130" class="f-cut"/>'
    b += T(500, 84, ['Whole shaft and', 'tip in view'], 'f-s', 'start')
    b += '<path d="M520 134 C560 140 620 140 690 138" class="f-dash"/>'
    b += T(600, 184, ['Wire seen in the vein in both planes', 'before dilating; dilate gently'], 'f-s')
    b += box(380, 214, 330, 40, 'Tip in the SVC; chest film after IJ or subclavian', 'ok', 'f-s')
    return svg(266, b)


def f27_vte():
    cols = ['Parenteral drug vs none', 'LMWH over UFH', 'Add IPC or stockings', 'Extend to 28 to 35 days', 'Routine screening']
    rows = [('Lobectomy or segmentectomy', ['Suggest (low)', 'Suggest (mod)', 'Suggest (v low)', 'If mod/high risk (low)', 'Against (v low)'],
             ['ok', 'ok', 'b1', 'b1', 'warn']),
            ('Pneumonectomy, extended', ['Suggest (low)', 'Suggest (mod)', 'Suggest (v low)', 'Suggest (low)', 'Suggest (v low)'],
             ['ok', 'ok', 'b1', 'ok', 'b1']),
            ('Oesophagectomy', ['Suggest (low)', 'Suggest (mod)', 'Suggest (v low)', 'Suggest (low)', 'Suggest (v low)'],
             ['ok', 'ok', 'b1', 'ok', 'b1'])]
    b = T(12, 20, 'Thoracic cancer surgery (ESTS/AATS 2022, adopted 2024): all conditional, certainty in brackets', 'f-h', 'start')
    x0, cw = 170, 106
    for j, c in enumerate(cols):
        words = c.split(' ')
        half = (len(words) + 1) // 2
        b += T(x0 + j * cw + cw / 2, 44, [' '.join(words[:half]), ' '.join(words[half:])], 'f-s')
    for i, (lab, cells, cls) in enumerate(rows):
        y = 70 + i * 50
        labs = {'Lobectomy or segmentectomy': ['Lobectomy or', 'segmentectomy'],
                'Pneumonectomy, extended': ['Pneumonectomy or', 'extended resection'],
                'Oesophagectomy': ['Oesophagectomy']}[lab]
        b += T(162, y + 28 - (len(labs) - 1) * 8, labs, '', 'end')
        for j, (t, c) in enumerate(zip(cells, cls)):
            x = x0 + j * cw
            b += f'<rect x="{x + 3}" y="{y + 4}" width="{cw - 6}" height="40" rx="7" class="f-{c}"/>'
            parts = t.split(' (')
            b += T(x + cw / 2, y + 21, parts[0], 'f-s') + T(x + cw / 2, y + 37, '(' + parts[1], 'f-s')
    b += T(12, 248, 'DOACs only within trials. Timing (before or after operation): no recommendation.', 'f-s', 'start')
    b += T(12, 284, 'Cardiovascular surgery (European 2024 update, chapter 1)', 'f-h', 'start')
    b += box(10, 296, 226, 58, ['Cardiac: drug prophylaxis', 'from 6 to 24 h, if no', 'major bleeding (1C)'], 'ok', 'f-s')
    b += box(247, 296, 226, 58, ['Vascular, higher risk', '(open TAAA, AAA, TEVAR):', 'start under 24 h (2C)'], 'b1', 'f-s')
    b += box(484, 296, 226, 58, ['LMWH first line over UFH', 'in cardiac and vascular', 'surgery: less HIT (2B)'], 'b1', 'f-s')
    return svg(366, b)


# ---- figs_F28.py



def f28_blast():
    """Mechanisms of blast injury (CDC Primer and Essential Facts; StatPearls; MSD Manual table)."""
    b = T(12, 22, 'Blast injury: five mechanisms', 'f-h', 'start')
    cx, cy = 140, 200
    # pressure wave rings
    for r in (48, 82, 116):
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="f-dash"/>'
    # starburst
    import math
    pts = []
    for i in range(16):
        rr = 26 if i % 2 == 0 else 12
        a = math.pi * 2 * i / 16
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    b += f'<polygon points="{" ".join(pts)}" class="f-warn"/>'
    # fragments
    for ang in (200, 235, 270, 160):
        a = math.radians(ang)
        b += arrow(cx + 34 * math.cos(a), cy + 34 * math.sin(a), cx + 74 * math.cos(a), cy + 74 * math.sin(a))
    # person struck by the wave
    px, py = 262, 176
    b += f'<circle cx="{px}" cy="{py - 34}" r="9" class="f-b1"/>'
    b += line(px, py - 25, px, py + 10) + line(px - 14, py - 12, px + 14, py - 12)
    b += line(px, py + 10, px - 10, py + 34) + line(px, py + 10, px + 10, py + 34)
    b += arrow(px + 8, py + 46, px + 36, py + 46, dash=True)
    b += T(px + 2, py + 66, 'thrown', 'f-s')
    b += T(cx, 340, ['Rings: overpressure wave', '(high-order explosives only)'], 'f-s')
    b += T(cx - 96, 82, 'fragments', 'f-s')
    spec = [
        ('Primary: blast wave (overpressure)', 'Gas-filled organs: ear drum, lung, bowel, eye.',
         'TM rupture commonest; blast lung commonest fatal one', 'b1'),
        ('Secondary: fragments and debris', 'Penetrating and blunt wounds, occult eye',
         'penetration; small wounds can hide deep injury', 'b0'),
        ('Tertiary: body thrown by blast wind', 'Fractures, traumatic amputation, open or',
         'closed brain injury (as in a high fall or crash)', 'b0'),
        ('Quaternary: everything else', 'Burns, crush, smoke, dust and toxic inhalation',
         '(CO, cyanide), worsening of chronic disease', 'b0'),
        ('Quinary: absorbed material', 'Radiological or biological contamination;',
         'hyperinflammatory state out of keeping with wounds', 'track'),
    ]
    for i, (h, l1, l2, cls) in enumerate(spec):
        y = 36 + i * 70
        b += f'<rect x="318" y="{y}" width="392" height="62" rx="9" class="f-{cls}"/>'
        b += T(330, y + 19, h, 'f-h', 'start') + T(330, y + 37, l1, 'f-s', 'start') + T(330, y + 53, l2, 'f-s', 'start')
    b += T(12, 396, 'Confined space (bus, building, mine) and structural collapse raise injury and death rates.', 'f-s', 'start')
    return svg(408, b)


def f28_ssrf():
    """Rib fixation: guideline position and randomised evidence, flail versus non-flail."""
    b = T(12, 22, 'Rib fixation: what the guideline and trials show', 'f-h', 'start')
    b += box(10, 34, 345, 40, 'Flail chest (or severe deformity)', 'b1', 'f-h')
    b += box(365, 34, 345, 40, 'Non-flail: 3 or more displaced fractures', 'b1', 'f-h')
    b += box(10, 84, 345, 66, ['EAST 2017: conditional FOR fixation', '(very low quality; 986 flail patients;',
                              'lower mortality, pneumonia, ventilation)'], 'ok', 'f-s')
    b += box(365, 84, 345, 66, ['EAST 2017: no recommendation', '(no studies of non-flail patients alone)'], 'track', 'f-s')
    b += box(10, 160, 345, 84, ['Dehghan 2022 RCT, 207 patients', 'Ventilator-free days 22.7 vs 20.6 (p = 0.09)',
                               'Deaths 0% vs 6% (p = 0.01); gain only in', 'those ventilated at randomisation'], 'b0', 'f-s')
    b += box(365, 160, 345, 66, ['Pieracci 2020 (CWIS), 110, mostly observational', 'Pain at 2 weeks 2.9 vs 4.5 (p < 0.01);',
                                'pleural complications 0% vs 10%'], 'ok', 'f-s')
    b += box(365, 236, 345, 66, ['Marasco 2022 RCT, 124 not ventilated', 'No difference in pain (McGill) or quality',
                                'of life at 3 and 6 months'], 'warn', 'f-s')
    b += box(365, 312, 345, 66, ['Meyer 2023 RCT, 84 severe non-clinical flail', 'Longer hospital stay (RR 1.48);',
                                'no quality-of-life gain to 6 months'], 'warn', 'f-s')
    b += box(10, 254, 345, 124, ['Reading of the trials', 'Clearest benefit: flail chest in a', 'ventilated patient.',
                                'Non-flail fractures in a patient who', 'is not ventilated: trials conflict'], 'b1', 'f-s')
    b += T(12, 400, 'Green: favours fixation · amber: no benefit or harm · grey: no recommendation, or primary end point missed', 'f-s', 'start')
    return svg(412, b)


def _f28_seg(x0, extra=''):
    """A longitudinal aortic segment: wall (tint) with lumen."""
    return ('<g transform="translate(0 20)">'
            f'<rect x="{x0 + 14}" y="84" width="142" height="64" rx="6" class="f-b1"/>'
            f'<rect x="{x0 + 14}" y="96" width="142" height="40" class="f-lumen" style="stroke:none"/>'
            + line(x0 + 14, 96, x0 + 156, 96) + line(x0 + 14, 136, x0 + 156, 136) + extra + '</g>')


def f28_btai():
    """BTAI grades I to IV (SVS) with ESVS 2026 grade and SVS 2026 / ESVS 2026 management."""
    b = T(12, 22, 'Blunt thoracic aortic injury: grade, appearance and management', 'f-h', 'start')
    names = [('Grade I', 'Intimal tear'), ('Grade II', 'Intramural haematoma'),
             ('Grade III', 'Pseudoaneurysm'), ('Grade IV', 'Rupture')]
    for i, (g, n) in enumerate(names):
        x0 = 10 + i * 178
        b += T(x0 + 85, 46, g + ' (SVS)', 'f-h') + T(x0 + 85, 64, n, 'f-s')
        if i == 0:
            b += _f28_seg(x0, f'<path d="M{x0 + 80} 96 L{x0 + 92} 112 L{x0 + 96} 96" class="f-l"/>')
        elif i == 1:
            b += _f28_seg(x0, f'<path d="M{x0 + 50} 96 Q{x0 + 85} 118 {x0 + 120} 96 Z" class="f-warn"/>')
        elif i == 2:
            b += (f'<path d="M{x0 + 60} 106 C{x0 + 56} 72 {x0 + 116} 72 {x0 + 110} 106" class="f-b1"/>'
                  + _f28_seg(x0, f'<rect x="{x0 + 66}" y="84" width="38" height="13" class="f-lumen" style="stroke:none"/>'
                             f'<path d="M{x0 + 66} 96 C{x0 + 64} 66 {x0 + 106} 66 {x0 + 104} 96" class="f-lumen"/>'))
        else:
            b += _f28_seg(x0, f'<rect x="{x0 + 74}" y="84" width="22" height="13" class="f-lumen" style="stroke:none"/>')
            for dx, dy in ((-18, -26), (0, -34), (18, -26)):
                b += line(x0 + 85, 104, x0 + 85 + dx * 0.8, 104 + dy * 0.6, 'f-cut')
            b += T(x0 + 130, 86, 'free blood', 'f-s')
    rows = [(222, 'ESVS 2026 grade', ['1', '1', '2', '3'], 'f-h'),
            (252, 'SVS 2026', ['Non-operative; no', 'Non-operative; one', 'Stable: TEVAR', 'Emergent'], 'f-s'),
            (268, '', ['routine imaging', 'CTA at 1 to 3 months', 'after 24 hours', 'repair'], 'f-s'),
            (298, 'ESVS 2026', ['Non-operative', 'Non-operative', 'High risk: < 24 h;', 'Immediate'], 'f-s'),
            (314, '', ['(class I)', '(class I)', 'otherwise > 24 h', 'TEVAR (class I)'], 'f-s')]
    for y, lab, cells, cls in rows:
        if lab:
            b += line(10, y - 16, 710, y - 16, 'f-grid')
        for i, c in enumerate(cells):
            b += T(10 + i * 178 + 85, y, c, cls)
    b += T(12, 194, 'Rows: ESVS 2026 grade · SVS 2026 management · ESVS 2026 management', 'f-s', 'start')
    b += box(10, 330, 700, 44, ['Medical (anti-impulse) therapy, ESVS 2026: systolic 90 to 110 mmHg, heart rate under 100;',
                               'with brain injury, cerebral perfusion comes first (both societies)'], 'b0', 'f-s')
    return svg(384, b)


def f28_btai_mort():
    """Aortic-related mortality by grade (systematic review and VQI, as cited in ESVS 2026)."""
    h, b = bars([('SVS grades I-II (review, 2,897)', 1, 'ok'), ('SVS grades III-IV (review)', 18, 'warn'),
                 ('Grade I, non-operative (VQI)', 2.4, 'b0'), ('Grade II, non-operative (VQI)', 0.9, 'b0')],
                '%', 20, 'Minimal aortic injury rarely kills: aortic-related deaths by grade', 270)
    return svg(h, b)


def f28_ptx2024():
    """ERS/EACTS/ESTS 2024 spontaneous pneumothorax: recommendations with strength and certainty (full text)."""
    b = T(12, 22, 'ERS/EACTS/ESTS 2024: recommendation, strength, certainty', 'f-h', 'start')
    b += box(10, 34, 345, 36, 'Primary spontaneous (PSP)', 'b1', 'f-h')
    b += box(365, 34, 345, 36, 'Secondary spontaneous (SSP)', 'b1', 'f-h')
    left = [(['Minimal symptoms, clinically and radiologically', 'stable, any size: conservative care',
              'Conditional · very low'], 'b0', 66),
            (['Needs intervention: needle aspiration', 'rather than a chest drain', 'Strong · low'], 'ok', 66),
            (['Ambulatory care where expertise and an', 'outpatient pathway exist', 'Conditional · low'], 'b0', 66),
            (['First episode, recurrence prevention', 'is the priority: consider early surgery', 'Conditional · low'], 'b0', 66)]
    right = [(['Conservative care, aspiration,', 'early surgery: no recommendation'], 'track', 50),
             (['Against an 8 Fr ambulatory device', 'for initial treatment', 'Conditional against · very low'], 'warn', 66),
             (['Persistent air leak, unfit for surgery:', 'autologous blood patch 1-2 mL/kg', 'Conditional · very low'], 'b0', 66),
             (['Surgical fitness and timing: age, comorbidity,', 'lung disease, PS, ASA, emphysema on CT',
               'Narrative question'], 'b1', 66)]
    for col, x in ((left, 10), (right, 365)):
        y = 80
        for ls, cls, h in col:
            b += box(x, y, 345, h, ls, cls, 'f-s')
            y += h + 8
    b += box(10, 378, 700, 44, ['No recommendation (very low certainty): bronchial valves · suction · VATS with or without',
                               'pleurodesis · pleurectomy versus chemical pleurodesis'], 'track', 'f-s')
    b += box(10, 430, 700, 44, ['All: stop smoking · no flying with an untreated pneumothorax, then wait 7 days after',
                               'radiological resolution · diving discouraged for life unless pleurectomy'], 'b1', 'f-s')
    return svg(484, b)


# ---- figs_F29.py

import math
import random


def f29_notss():
    """NOTSS v1.2: four categories, twelve elements, rating scale."""
    cats = [
        ('Situation awareness', ['Gathering information', 'Understanding', 'information',
                                 'Projecting and', 'anticipating future state'], 'b1'),
        ('Decision making', ['Considering options', 'Selecting and', 'communicating option',
                             'Implementing and', 'reviewing decisions'], 'b1'),
        ('Communication and teamwork', ['Exchanging information', 'Establishing a shared',
                                        'understanding', 'Co-ordinating team', 'activities'], 'b1'),
        ('Leadership', ['Setting and maintaining', 'standards', 'Supporting others',
                        'Coping with pressure'], 'b1'),
    ]
    b = box(220, 8, 280, 40, 'NOTSS: 4 categories, 12 elements', 'b0', 'f-h')
    w, gap = 166, 12
    for i, (name, els, cls) in enumerate(cats):
        x = 10 + i * (w + gap)
        b += arrow(360, 48, x + w / 2, 70)
        b += box(x, 72, w, 46, name if len(name) < 20 else name.replace(' and ', ' and|').split('|'), cls, 'f-h')
        b += f'<rect x="{x}" y="128" width="{w}" height="124" rx="9" class="f-b0"/>'
        b += T(x + 10, 150, els, 'f-s', 'start')
    b += T(10, 280, 'Rating after each case (under five minutes, as a debrief):', 'f-h', 'start')
    scale = [('4 Good', 'ok'), ('3 Acceptable', 'ok'), ('2 Marginal', 'warn'), ('1 Poor', 'warn'), ('N/A not required', 'b0')]
    for i, (lab, cls) in enumerate(scale):
        b += box(10 + i * 142, 292, 132, 34, lab, cls, 'f-s')
    b += T(360, 352, 'Formative use (training, debrief, self-reflection); not recommended for summative assessment.', 'f-s')
    return svg(364, b)


def f29_natssips():
    """NatSSIPs 2 (CPOC 2023): the eight sequential standards in order."""
    steps = [('1', ['Consent and', 'verification,', 'site marking']), ('2', ['Team brief', '(start of', 'session)']),
             ('3', ['Sign In', '(before', 'anaesthesia)']), ('4', ['Time Out', '(just before', 'skin prep)']),
             ('5', ['Implant use', 'and', 'verification']), ('6', ['Reconciling', 'items', '(counts)']),
             ('7', ['Sign Out', '(before', 'leaving)']), ('8', ['Handover', 'and', 'debrief'])]
    b = T(10, 20, 'NatSSIPs 2: the eight sequential standards', 'f-h', 'start')
    w, gap = 80, 9
    for i, (n, lab) in enumerate(steps):
        x = 10 + i * (w + gap)
        cls = 'warn' if n in ('4', '6') else 'b1'
        b += f'<rect x="{x}" y="34" width="{w}" height="96" rx="9" class="f-{cls}"/>'
        b += T(x + w / 2, 56, n, 'f-n')
        b += T(x + w / 2, 80, lab, 'f-s')
        if i < 7:
            b += arrow(x + w, 82, x + w + gap, 82)
    b += box(10, 146, 345, 78, ['Organisational standards: people (patients,', 'named board lead, staffing, training),',
                                'processes, performance (data, observation)'], 'b0', 'f-s')
    b += box(365, 146, 345, 78, ['Proportionate: full count for major procedures', 'and any cavity; proportionate count for minor',
                                 'and needle procedures. No mandatory LocSSIP'], 'b0', 'f-s')
    b += T(360, 246, 'Amber: Time Out (the most critical check) and counts (stop, recount, search, X-ray before the patient leaves).', 'f-s')
    return svg(258, b)


def _f29_km(times):
    """times: list of (t, event 1/0). Returns step list [(t, S)], censor list [(t, S)]."""
    times = sorted(times)
    n = len(times)
    s = 1.0
    steps, cens = [(0, 1.0)], []
    i = 0
    while i < len(times):
        t = times[i][0]
        d = sum(1 for tt, e in times if tt == t and e == 1)
        c = sum(1 for tt, e in times if tt == t and e == 0)
        if d:
            s *= (1 - d / n)
            steps.append((t, s))
        if c:
            cens.extend([(t, s)] * c)
        n -= d + c
        i += d + c
    return steps, cens


def _f29_at_risk(times, t):
    return sum(1 for tt, e in times if tt >= t)


def f29_km_guide():
    """Kaplan-Meier reading guide with invented data for two arms of 20."""
    A = [(2, 1), (3, 1), (4, 1), (5, 0), (6, 1), (7, 1), (8, 1), (9, 0), (10, 1), (11, 1), (13, 1), (14, 0),
         (16, 1), (18, 1), (21, 0), (24, 1), (27, 0), (30, 0), (33, 0), (36, 0)]
    B = [(4, 1), (7, 1), (9, 0), (12, 1), (15, 1), (17, 0), (19, 1), (22, 0), (25, 1), (28, 0), (30, 0), (31, 0),
         (32, 1), (33, 0), (34, 0), (35, 0), (36, 0), (36, 0), (36, 0), (36, 0)]
    gx0, gx1, gy0, gy1, tmax = 96, 520, 40, 280, 36

    def X(t):
        return gx0 + t / tmax * (gx1 - gx0)

    def Y(s):
        return gy1 - s * (gy1 - gy0)
    b = T(12, 20, 'Reading a Kaplan-Meier plot (invented data, 20 patients per arm)', 'f-h', 'start')
    for s in (0, 0.25, 0.5, 0.75, 1.0):
        b += line(gx0, Y(s), gx1, Y(s), 'f-grid') + T(gx0 - 8, Y(s) + 4, f'{s:.2f}', 'f-s', 'end')
    for t in range(0, 37, 6):
        b += T(X(t), gy1 + 16, str(t), 'f-s')
    b += T((gx0 + gx1) / 2, gy1 + 34, 'Months from randomisation', 'f-s')
    b += T(30, (gy0 + gy1) / 2 + 4, 'S(t)', 'f-s')
    b += line(gx0, gy0, gx0, gy1) + line(gx0, gy1, gx1, gy1)
    for data, cls, lab in ((A, 'f-cut', 'Control'), (B, 'f-l', 'Treatment')):
        steps, cens = _f29_km(data)
        d = f'M{X(0):.1f} {Y(1):.1f}'
        prev = 1.0
        for t, s in steps[1:]:
            d += f' H{X(t):.1f} V{Y(s):.1f}'
            prev = s
        d += f' H{X(tmax):.1f}'
        b += f'<path d="{d}" class="{cls}" style="stroke-width:2.2"/>'
        for t, s in cens:
            b += line(X(t), Y(s) - 6, X(t), Y(s) + 6, cls)
    # median line
    med = next(t for t, s in _f29_km(A)[0] if s <= 0.5)
    b += line(gx0, Y(0.5), X(med), Y(0.5), 'f-dash')
    b += line(X(med), Y(0.5), X(med), gy1, 'f-dash')
    b += T(X(med) + 4, gy1 - 6, f'control median {med} months', 'f-s', 'start')
    b += T(X(36), Y(0.5) - 8 - 0, '', 'f-s')
    # labels on curves
    b += T(X(28), Y(0.68) - 4, 'Treatment', 'f-h', 'start') + T(X(26), Y(0.22) + 16, 'Control', 'f-h', 'start')
    # annotations right
    ax = 534
    b += box(ax, 40, 176, 54, ['Each drop = an event;', 'height = 1/number at risk'], 'b0', 'f-s')
    b += box(ax, 102, 176, 54, ['Tick = censored patient', '(no drop; leaves risk set)'], 'b0', 'f-s')
    b += box(ax, 164, 176, 54, ['Median: where S(t)', 'crosses 0.5'], 'b0', 'f-s')
    b += box(ax, 226, 176, 54, ['Tail: few at risk, so', 'wide CI; do not over-read'], 'warn', 'f-s')
    b += arrow(ax, 254, X(33) + 6, Y(0.5))
    # numbers at risk
    ry = gy1 + 58
    b += T(12, ry, 'Number at risk', 'f-h', 'start')
    for k, (data, lab) in enumerate(((B, 'Treatment'), (A, 'Control'))):
        y = ry + 20 + k * 18
        b += T(12, y, lab, 'f-s', 'start')
        for t in range(0, 37, 6):
            b += T(X(t), y, str(_f29_at_risk(data, t)), 'f-s')
    by = ry + 66
    b += box(10, by, 345, 62, ['Log-rank test: compares whole curves', '(observed v expected events at each death);',
                               'gives a P value, not an effect size'], 'b1', 'f-s')
    b += box(365, by, 345, 62, ['Hazard ratio (Cox): one number for the whole', 'follow-up; valid only if hazards are',
                                'proportional (curves should not cross)'], 'b1', 'f-s')
    return svg(by + 72, b)


def f29_grade_ladder():
    """GRADE certainty ladder: start level, five down, three up."""
    lv = [('High', 'Very confident the true effect is close', 'ok'),
          ('Moderate', 'Likely close; could be substantially different', 'b1'),
          ('Low', 'May be substantially different', 'b1'),
          ('Very low', 'Likely to be substantially different', 'warn')]
    b = T(360, 20, 'GRADE certainty of evidence (GRADE Handbook, 2013)', 'f-h')
    for i, (name, desc, cls) in enumerate(lv):
        y = 36 + i * 58
        b += f'<rect x="196" y="{y}" width="290" height="50" rx="9" class="f-{cls}"/>'
        b += T(341, y + 20, name, 'f-h') + T(341, y + 39, desc, 'f-s')
    b += box(10, 39, 150, 44, ['Randomised trials', 'start here'], 'b0', 'f-s') + arrow(160, 61, 194, 61)
    b += box(10, 155, 150, 44, ['Observational', 'studies start here'], 'b0', 'f-s') + arrow(160, 177, 194, 177)
    b += T(10, 228, ['Case series usually', 'very low; expert', 'opinion is not', 'evidence'], 'f-s', 'start')
    b += box(520, 36, 190, 120, ['Rate DOWN (1 or 2 each)', 'Risk of bias', 'Inconsistency', 'Indirectness',
                                 'Imprecision', 'Publication bias'], 'warn', 'f-s')
    b += box(520, 166, 190, 104, ['Rate UP', 'Large effect (RR >2 or', '<0.5; two levels if >5', 'or <0.2); dose-response;',
                                  'confounding would shrink it'], 'ok', 'f-s')
    b += '<path d="M500 50 L500 262" class="f-l" marker-end="url(#ah)"/>'
    b += '<path d="M180 262 L180 50" class="f-l" marker-end="url(#ah)"/>'
    b += box(10, 284, 700, 44, ['Recommendation strength (strong or weak/conditional) also weighs benefits against harms,',
                               'values and preferences, and resources: a strong recommendation can rest on low certainty.'], 'b0', 'f-s')
    return svg(336, b)


def _f29_cusum_data():
    rnd = random.Random(117)
    pts = []
    for i in range(240):
        p = min(0.6, max(0.01, rnd.lognormvariate(math.log(0.04), 0.8)))
        if i >= 150:  # odds of death doubled from patient 151 (invented)
            o = 2 * p / (1 - p)
            ptrue = o / (1 + o)
        else:
            ptrue = p
        y = 1 if rnd.random() < ptrue else 0
        pts.append((p, y))
    return pts


def f29_ra_cusum():
    """Risk-adjusted CUSUM (Steiner 2000 weights, R0=1, RA=2, h=4.5) on invented data."""
    pts = _f29_cusum_data()
    R0, RA, h = 1.0, 2.0, 4.5
    xs, x = [0.0], 0.0
    signal = None
    for i, (p, y) in enumerate(pts):
        if y:
            w = math.log(((1 - p + R0 * p) * RA) / ((1 - p + RA * p) * R0))
        else:
            w = math.log((1 - p + R0 * p) / (1 - p + RA * p))
        x = max(0.0, x + w)
        if signal is None and x >= h:
            signal = i + 1
            sigval = x
            xs.append(x)
            x = 0.0  # reset after the signal and review
            continue
        xs.append(x)
    n = len(pts)
    gx0, gx1, gy0, gy1, ymax = 60, 700, 40, 250, 6.0

    def X(i):
        return gx0 + i / n * (gx1 - gx0)

    def Y(v):
        return gy1 - min(v, ymax) / ymax * (gy1 - gy0)
    deaths = sum(y for p, y in pts)
    exp = sum(p for p, y in pts)
    b = T(12, 20, f'Risk-adjusted CUSUM, invented series of {n} operations: signal at patient {signal}', 'f-h', 'start')
    for v in range(0, 7):
        b += line(gx0, Y(v), gx1, Y(v), 'f-grid') + T(gx0 - 8, Y(v) + 4, str(v), 'f-s', 'end')
    for i in range(0, n + 1, 40):
        b += T(X(i), gy1 + 16, str(i), 'f-s')
    b += T((gx0 + gx1) / 2, gy1 + 34, 'Consecutive operations', 'f-s')
    b += line(gx0, gy0, gx0, gy1) + line(gx0, gy1, gx1, gy1)
    b += line(gx0, Y(h), gx1, Y(h), 'f-cut') + T(gx0 + 6, Y(h) - 6, 'Control limit h = 4.5', 'f-s', 'start')
    b += line(X(150), gy0, X(150), gy1, 'f-dash') + T(X(150) - 4, Y(2.6), ['odds of death', 'doubled from here'], 'f-s', 'end')
    d = 'M' + ' L'.join(f'{X(i):.1f} {Y(v):.1f}' for i, v in enumerate(xs))
    b += f'<path d="{d}" class="f-l"/>'
    if signal:
        b += f'<circle cx="{X(signal):.1f}" cy="{Y(sigval):.1f}" r="6" class="f-warn"/>'
        b += T(X(signal) - 12, Y(h) - 24, ['signal: review the deaths,', 'then reset to 0'], 'f-s', 'end')
    by = gy1 + 50
    b += box(10, by, 228, 70, ['Death: add log[2 / (1 + p)]', 'p = 2.5%: +0.67', 'p = 54%: +0.26'], 'warn', 'f-s')
    b += box(246, by, 228, 70, ['Survival: add log[1 / (1 + p)]', 'p = 2.5%: −0.02', 'p = 54%: −0.43'], 'ok', 'f-s')
    b += box(482, by, 228, 70, ['Floor at zero; signal at h.', f'Series: {deaths} deaths v', f'{exp:.1f} predicted'], 'b0', 'f-s')
    return svg(by + 80, b)


# ---- figs_F30.py



def f30_radial_landmarks():
    """Left forearm, volar view, elbow to the left: open radial harvest landmarks (Blitz 2013)."""
    b = ''
    # forearm outline
    b += '<path d="M70 70 C200 52 480 92 640 112 L640 238 C480 250 200 270 70 262 Z" class="f-b1"/>'
    b += T(360, 30, 'Radial (thumb) side', 'f-s') + T(360, 292, 'Ulnar side', 'f-s')
    b += T(66, 50, 'Elbow', 'f-h', 'start') + T(654, 100, 'Wrist', 'f-h', 'end')
    # creases
    b += line(110, 64, 110, 266, 'f-dash') + T(112, 282, 'Elbow crease', 'f-s', 'start')
    b += line(612, 108, 612, 242, 'f-dash') + T(610, 258, 'Wrist crease', 'f-s', 'end')
    # brachioradialis belly along radial side
    b += '<path d="M90 76 C180 66 300 76 380 96 C330 112 220 112 96 104 Z" class="f-b0"/>'
    b += T(230, 104, 'Brachioradialis', 'f-s')
    b += '<path d="M380 96 C470 108 560 116 628 122" class="f-l" style="stroke-width:5;opacity:.45"/>'
    b += T(470, 96, 'BR tendon to radial styloid', 'f-s')
    # FCR tendon
    b += '<path d="M330 196 C430 190 540 184 628 182" class="f-l" style="stroke-width:5;opacity:.45"/>' + T(520, 202, 'FCR tendon', 'f-s')
    # biceps tendon inverted V
    b += '<path d="M60 150 L118 162 L60 182" class="f-l" style="stroke-width:3"/>'
    b += T(56, 214, ['Biceps tendon', 'and aponeurosis'], 'f-s', 'start')
    # radial artery
    b += '<path d="M118 162 C220 150 330 138 430 140 C520 142 580 146 628 150" class="f-vessel" style="stroke-width:10"/>'
    # ulnar artery
    b += '<path d="M118 166 C220 200 360 222 628 216" class="f-vessel" style="stroke-width:7;opacity:.35"/>'
    b += T(300, 232, 'Ulnar artery', 'f-s')
    # recurrent radial artery
    b += '<path d="M138 158 C130 140 112 126 94 120" class="f-vessel" style="stroke-width:5"/>'
    b += arrow(180, 50, 108, 120) + T(186, 52, 'Recurrent radial a.', 'f-s', 'start')
    # superficial palmar branch
    b += '<path d="M600 149 C616 160 624 172 634 186" class="f-vessel" style="stroke-width:5"/>'
    # incision
    b += '<path d="M126 150 C230 132 330 122 430 126 C510 130 560 136 600 140" class="f-cut" stroke-dasharray="8 5"/>'
    # nerves
    b += '<path d="M100 82 C170 76 230 78 300 84" class="f-nerve" stroke-dasharray="2 4"/>'
    b += '<path d="M300 116 C380 124 460 130 600 132" class="f-nerve"/>'
    # callouts
    b += arrow(250, 320, 200, 80) + T(250, 336, ['Lateral antebrachial cutaneous n.:', 'superficial fascia over BR'], 'f-s')
    b += arrow(470, 320, 450, 131) + T(480, 336, ['Superficial radial n.:', 'lateral to the artery'], 'f-s')
    b += arrow(690, 160, 638, 178) + T(700, 140, ['Superficial', 'palmar a.'], 'f-s', 'end')
    # bottom boxes
    b += box(10, 378, 228, 70, ['Incision: edge of BR, from', '1 cm below elbow crease', 'to 1 cm above wrist crease'], 'warn', 'f-s')
    b += box(246, 378, 228, 70, ['Proximal limit: just below', 'recurrent radial origin.', 'Distal: above palmar branch'], 'b0', 'f-s')
    b += box(482, 378, 228, 70, ['Clamp distally: confirm', 'back-bleeding before', 'division; leave deep fascia open'], 'ok', 'f-s')
    return svg(458, b)


def f30_radial_trials():
    """RAPCO 10-year patency and RADIAL 10-year composite."""
    h1, b1 = bars([('Radial, under 70', 89, 'ok'), ('Free right ITA, under 70', 80, 'b1'),
                   ('Radial, 70 or over', 85, 'ok'), ('Saphenous vein, 70 or over', 71, 'b1')],
                  '%', 100, 'RAPCO: radial grafts had the highest estimated 10-year patency', 260)
    h2, b2 = bars([('Radial artery (534)', 31.0, 'ok'), ('Saphenous vein (502)', 41.6, 'warn')],
                  '%', 100, 'RADIAL pooled: fewer deaths, MI or repeat revascularisation (HR 0.73)', 260)
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


def f30_uk_tavi():
    """UK TAVI 1-year outcomes (Toff, JAMA 2022)."""
    h, b = bars([('Death, TAVI', 4.6, 'b0'), ('Death, surgery', 6.6, 'b1'),
                 ('Major bleeding, TAVI', 7.2, 'ok'), ('Major bleeding, surgery', 20.2, 'warn'),
                 ('Vascular complication, TAVI', 10.3, 'warn'), ('Vascular complication, surgery', 2.4, 'ok'),
                 ('Pacemaker, TAVI', 14.2, 'warn'), ('Pacemaker, surgery', 7.3, 'ok'),
                 ('Stroke, TAVI', 5.2, 'b0'), ('Stroke, surgery', 2.6, 'b1')],
                '%', 25, 'UK TAVI (913, age 70+): TAVI non-inferior for 1-year death', 260)
    return svg(h, b)


def f30_smart_protect():
    """SMART (Herrmann, NEJM 2024) and BHF PROTECT-TAVI (Kharbanda, NEJM 2025)."""
    h1, b1 = bars([('Self-expanding (Evolut)', 9.4, 'ok'), ('Balloon-expandable (SAPIEN 3)', 41.6, 'warn')],
                  '%', 50, 'SMART: valve dysfunction at 12 months, annulus 430 mm² or less', 270)
    h2, b2 = bars([('Self-expanding', 9.4, 'b0'), ('Balloon-expandable', 10.6, 'b1')],
                  '%', 50, 'SMART: death, disabling stroke or HF admission (non-inferior)', 270)
    h3, b3 = bars([('Sentinel protection (3,795)', 2.1, 'b0'), ('No protection (3,799)', 2.2, 'b1')],
                  '%', 50, 'BHF PROTECT-TAVI: stroke by 72 h did not differ (P = 0.94)', 270)
    return svg(h1 + h2 + h3, b1 + f'<g transform="translate(0 {h1})">{b2}</g>'
               + f'<g transform="translate(0 {h1 + h2})">{b3}</g>')


def f30_extraction_indications():
    """HRS 2017 lead extraction indications by class of recommendation."""
    rows = [
        ('Definite CIED infection (pocket, lead, device): complete removal', 'I B-NR', 'ok'),
        ('Valve endocarditis, even without proven lead involvement', 'I B-NR', 'ok'),
        ('Persistent or recurrent bacteraemia or fungaemia, no other source', 'I B-NR', 'ok'),
        ('Purulence around intrathoracic epicardial leads or patches', 'I C-EO', 'ok'),
        ('Thromboembolism from lead thrombus not treatable otherwise', 'I C-EO', 'ok'),
        ('SVC stenosis or occlusion blocking a needed lead or stent', 'I C-EO', 'ok'),
        ('Life-threatening arrhythmia from a retained lead', 'I C-EO', 'ok'),
        ('Severe chronic pain at device or lead, not otherwise manageable', 'IIa C-EO', 'b1'),
        ('Ipsilateral venous occlusion, access needed for a new lead', 'IIa C-LD', 'b1'),
        ('More than 4 leads on one side or more than 5 through the SVC', 'IIa C-LD', 'b1'),
        ('Lead interferes with cancer treatment; abandoned lead interferes', 'IIa C-EO', 'b1'),
        ('Recalled lead; to allow MRI; working non-recalled lead', 'IIb C', 'warn'),
    ]
    b = T(10, 22, 'HRS 2017: when to extract (class and level of evidence)', 'f-h', 'start')
    y = 32
    for txt, cl, c in rows:
        b += f'<rect x="10" y="{y}" width="700" height="28" rx="7" class="f-{c}"/>'
        b += T(22, y + 19, txt, '', 'start') + T(698, y + 19, cl, 'f-n', 'end')
        y += 33
    b += box(10, y + 6, 700, 40, ['Superficial incisional infection alone is not an indication; erosion of any part means removing the whole system'], 'b0', 'f-s')
    return svg(y + 56, b)


def f30_epicardial_lv():
    """Left lateral minithoracotomy for an epicardial LV lead (Fang 2015, Kim 2022)."""
    b = ''
    # chest wall, left lateral view
    b += T(360, 22, 'Patient right side down, left chest raised 30 to 40 degrees; right lung ventilated', 'f-h')
    b += '<path d="M60 70 C140 50 300 46 420 60 L420 330 C300 340 140 340 60 320 Z" class="f-b1"/>'
    for i, y in enumerate([96, 136, 176, 216, 256]):
        b += f'<path d="M66 {y} C160 {y - 14} 300 {y - 14} 414 {y}" class="f-grid" style="fill:none"/>'
    b += T(56, 166, '4th ICS', 'f-s', 'end')
    b += '<path d="M170 168 C210 160 260 160 300 166" class="f-cut" style="stroke-width:4"/>'
    b += T(236, 154, 'Incision, 4th ICS', 'f-s')
    # heart through window
    b += '<ellipse cx="240" cy="250" rx="80" ry="54" class="f-b0"/>'
    b += '<path d="M176 222 C210 240 250 248 300 236" class="f-nerve"/>' + T(170, 218, 'Phrenic n.', 'f-s', 'end')
    b += '<path d="M190 268 C220 288 260 292 296 280" class="f-vessel" style="stroke-width:5"/>'
    b += '<circle cx="246" cy="262" r="7" class="f-warn"/>'
    b += T(240, 356, 'LV lateral wall (pericardium opened in front of the phrenic nerve)', 'f-s')
    # tunnelling to pocket
    b += '<rect x="340" y="76" width="56" height="34" rx="8" class="f-b0"/>' + T(368, 98, 'Pocket', 'f-s')
    b += '<path d="M246 262 C300 220 330 160 350 110" class="f-dash"/>'
    # right panel notes
    b += box(450, 50, 260, 70, ['Target: between circumflex', 'and obtuse marginal, below', 'the left atrial appendage'], 'warn', 'f-s')
    b += box(450, 130, 260, 70, ['Accept: threshold under 2 V', 'at 0.4 ms, R wave over 5 mV,', 'impedance 200 to 2000 ohm'], 'ok', 'f-s')
    b += box(450, 210, 260, 52, ['Test at 10 V: no phrenic', 'capture'], 'b0', 'f-s')
    b += box(450, 272, 260, 66, ['Tunnel via 3rd ICS to pocket;', 'partial pericardial closure;', 'small pleural drain'], 'b0', 'f-s')
    return svg(370, b)


# ---- figs_F31.py

import math


def _f31_sector(cx, cy, r, a0, a1, cls):
    """Pie sector from angle a0 to a1 (degrees, 0 = east, clockwise positive as in SVG)."""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    return (f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f} Z" class="f-{cls}"/>')


def f31_sova_rupture():
    cx, cy, r = 230, 210, 62
    b = T(230, 20, 'Aortic root in short axis (schematic)', 'f-h')
    # chambers around the root
    b += box(250, 40, 170, 46, ['RV outflow tract', 'below pulmonary valve'], 'b1', 'f-s')
    b += box(40, 40, 170, 46, ['RV at the crista', 'supraventricularis'], 'b1', 'f-s')
    b += box(10, 168, 92, 84, ['Right', 'atrium'], 'b1', 'f-s')
    b += box(70, 300, 130, 40, 'Right ventricle (inlet)', 'b1', 'f-s')
    b += box(250, 312, 150, 40, 'Left atrium', 'b1', 'f-s')
    b += box(350, 178, 90, 64, ['LV outflow', '(rare)'], 'b1', 'f-s')
    # the three sinuses
    b += _f31_sector(cx, cy, r, 210, 330, 'warn')
    b += _f31_sector(cx, cy, r, 330, 450, 'b0')
    b += _f31_sector(cx, cy, r, 90, 210, 'b0')
    b += T(cx, cy - 26, 'R', 'f-h') + T(cx + 28, cy + 26, 'L', 'f-h') + T(cx - 28, cy + 26, 'N', 'f-h')
    # Sakakibara types
    b += arrow(250, 160, 300, 90) + T(286, 128, 'I', 'f-h', 'start')
    b += arrow(212, 158, 150, 90) + T(166, 128, 'II', 'f-h', 'end')
    b += arrow(176, 190, 106, 196) + T(144, 184, 'IIIa', 'f-s')
    b += arrow(186, 238, 140, 296) + T(170, 290, 'IIIv', 'f-s', 'start')
    b += arrow(196, 246, 106, 238) + T(150, 234, 'IV', 'f-h')
    b += arrow(262, 250, 300, 308, True) + arrow(288, 214, 346, 210, True)
    b += T(cx, 372, 'Solid arrows: Sakakibara types · dashed: left sinus, rare', 'f-s')
    # right panel
    x = 470
    b += T(x + 120, 20, 'Sakakibara and Konno (1962)', 'f-h')
    rows = [('I', ['Right sinus to RV outflow', 'below the pulmonary valve'], 'warn'),
            ('II', ['Right sinus to RV', 'at the crista'], 'warn'),
            ('IIIa', ['Right sinus to', 'right atrium'], 'warn'),
            ('IIIv', ['Posterior right sinus', 'to RV (inlet)'], 'warn'),
            ('IV', ['Non-coronary sinus', 'to right atrium'], 'b0')]
    for i, (t, d, c) in enumerate(rows):
        y = 34 + i * 46
        b += f'<rect x="{x}" y="{y}" width="52" height="38" rx="8" class="f-{c}"/>' + T(x + 26, y + 24, t, 'f-h')
        b += T(x + 60, y + 16, d, 'f-s', 'start')
    b += box(x, 270, 240, 96, ['Rupture: into RV about 60%,', 'RA about 30% (Arcario 2021)',
                               'Sinus: right 65 to 85%,', 'non-coronary 10 to 30%'], 'b1', 'f-s')
    return svg(384, b)


def f31_paivs_pathway():
    b = box(160, 8, 400, 44, ['Newborn with PA-IVS: prostaglandin, echo', '(RV parts, tricuspid size, sinusoids, atrial septum)'], 'b1', 'f-s')
    b += arrow(360, 52, 360, 70)
    b += box(160, 72, 400, 44, ['Coronary angiography: is coronary flow', 'dependent on RV pressure (RVDCC)?'], 'b0', 'f-s')
    b += arrow(250, 116, 140, 146) + arrow(470, 116, 580, 146)
    b += T(170, 134, 'No', 'f-h', 'end') + T(550, 134, 'Yes', 'f-h', 'start')
    b += box(10, 148, 300, 60, ['Membranous atresia, bipartite or', 'tripartite RV: decompress (catheter', 'perforation and balloon, or surgical valvotomy)'], 'ok', 'f-s')
    b += box(410, 148, 300, 60, ['Do NOT decompress the RV', '(risk of coronary ischaemia)', 'Shunt or ductal stent'], 'warn', 'f-s')
    b += arrow(160, 208, 160, 228)
    b += box(10, 230, 300, 44, ['Cannot wean prostaglandin: add', 'ductal stent or shunt'], 'b1', 'f-s')
    b += arrow(80, 274, 70, 296) + arrow(160, 274, 160, 296) + arrow(250, 274, 260, 296)
    b += box(10, 298, 100, 58, ['Biventricular', 'repair'], 'ok', 'f-s')
    b += box(115, 298, 92, 58, ['One-and-', 'a-half', '(+ Glenn)'], 'b1', 'f-s')
    b += box(212, 298, 98, 58, ['Single', 'ventricle'], 'warn', 'f-s')
    b += arrow(500, 208, 500, 296) + arrow(640, 208, 640, 296)
    b += box(410, 298, 180, 58, ['Single ventricle', '(Glenn, then Fontan)'], 'warn', 'f-s')
    b += box(600, 298, 110, 58, ['Transplant', '(MCS bridge)'], 'warn', 'f-s')
    b += T(10, 380, 'RV growth decides between the three left-hand outcomes. AATS 2025 RVDCC criterion (first of the', 'f-s', 'start')
    b += T(10, 397, 'published criteria): RV-coronary fistulae plus severe stenosis of 2 of 3 major coronaries, or aortocoronary atresia of 1', 'f-s', 'start')
    return svg(410, b)


def f31_paivs_uk():
    h1, b1 = bars([('First procedure RV decompression', 7.7, 'ok'),
                   ('First procedure shunt or ductal stent', 37.2, 'warn')],
                  '%', 50, 'One-year mortality is five times higher after stage 1 palliation', 290)
    h2, b2 = bars([('Biventricular repair', 55.3, 'ok'), ('Single ventricle (incl. 23 one-and-a-half)', 27.9, 'warn'),
                   ('Not yet committed', 16.8, 'b1')],
                  '%', 70, 'Final pathway of 488 children', 290)
    foot = T(12, h1 + h2 + 2, 'PA-IVS, England and Wales 2000 to 2022 (NCHDA linked to ONS; Dorobantu and colleagues, Circ Cardiovasc Interv 2026)', 'f-s', 'start')
    return svg(h1 + h2 + 14, b1 + f'<g transform="translate(0 {h1})">{b2}</g>' + foot)


def f31_ivc_azygos():
    b = T(180, 20, 'Normal', 'f-h') + T(540, 20, 'Interrupted IVC, azygos continuation', 'f-h')
    b += line(360, 10, 360, 400, 'f-dash')
    for ox, interrupted in [(0, False), (360, True)]:
        ra_x = ox + 150
        b += f'<rect x="{ra_x}" y="120" width="80" height="70" rx="16" class="f-b1"/>' + T(ra_x + 40, 160, 'RA', 'f-h')
        b += f'<path d="M{ra_x + 40} 56 L{ra_x + 40} 120" class="f-vessel" style="stroke-width:10"/>' + T(ra_x + 40, 42, 'SVC', 'f-s')
        b += f'<rect x="{ra_x + 6}" y="236" width="68" height="46" rx="12" class="f-b0"/>' + T(ra_x + 40, 264, 'Liver', 'f-s')
        b += f'<path d="M{ra_x + 40} 190 L{ra_x + 40} 236" class="f-vessel" style="stroke-width:10"/>'
        b += f'<path d="M{ra_x + 40} 380 L{ra_x + 40} 340" class="f-vessel" style="stroke-width:10"/>'
        b += T(ra_x + 40, 396, 'Infrarenal IVC', 'f-s')
        b += f'<path d="M{ra_x + 4} 330 L{ra_x + 76} 330" class="f-vessel" style="stroke-width:10"/>' + T(ra_x + 4, 352, 'Renal veins', 'f-s', 'end')
        az_x = ra_x + 110
        if not interrupted:
            b += f'<path d="M{ra_x + 40} 330 L{ra_x + 40} 282" class="f-vessel" style="stroke-width:10"/>'
            b += f'<path d="M{az_x} 330 L{az_x} 80 C{az_x} 64 {ra_x + 60} 64 {ra_x + 44} 70" class="f-dash"/>'
            b += T(az_x + 8, 200, ['Azygos', '(small)'], 'f-s', 'start')
            b += T(ra_x - 10, 214, ['Hepatic', 'IVC'], 'f-s', 'end')
        else:
            b += f'<path d="M{ra_x + 40} 330 C{ra_x + 40} 316 {az_x} 316 {az_x} 300 L{az_x} 80 C{az_x} 60 {ra_x + 60} 60 {ra_x + 44} 70" class="f-vessel" style="stroke-width:10"/>'
            b += line(ra_x + 26, 300, ra_x + 54, 300, 'f-cut') + line(ra_x + 26, 306, ra_x + 54, 306, 'f-cut')
            b += T(ra_x - 6, 282, ['Suprarenal', 'segment', 'absent'], 'f-s', 'end')
            b += T(az_x + 8, 160, ['Dilated', 'azygos', '(behind', 'the crus)'], 'f-s', 'start')
            b += T(ra_x - 10, 206, ['Hepatic veins', 'by short', 'post-hepatic', 'segment'], 'f-s', 'end')
    return svg(410, b)


def f31_ivc_cannulation():
    b = box(10, 10, 340, 112, ['Bypass with azygos continuation', '(Ghandour 2016)', 'Large cannula high in the SVC: carries',
                               'nearly all lower-body return', 'Small cannula in the post-hepatic IVC'], 'b0', 'f-s')
    b += box(370, 10, 340, 112, ['Do not ligate the azygos', 'It is the only route for lower-body', 'return: inadvertent ligation',
                                 'may be fatal (Ghandour 2016)'], 'warn', 'f-s')
    b += box(10, 136, 340, 74, ['Associations: heterotaxy, polysplenia,', 'AVSD, PAPVC, pulmonary atresia',
                                '(prevalence about 0.6%)'], 'b1', 'f-s')
    b += box(370, 136, 340, 74, ['Imaging trap: a dilated azygos can look', 'like a right paratracheal mass or',
                                 'retrocrural nodes'], 'b1', 'f-s')
    return svg(220, b)


def f31_paeds_arrest():
    b = box(160, 8, 400, 40, 'Arrest in the cardiac ICU after paediatric heart surgery', 'b1', 'f-h')
    b += arrow(360, 48, 360, 64)
    b += box(10, 66, 340, 74, ['Monitored, witnessed VF or pulseless VT:', 'up to 3 stacked shocks, 4 J/kg', '(max 120 to 200 J), then CPR 2 min'], 'b0', 'f-s')
    b += box(370, 66, 340, 74, ['Non-shockable: CPR 15:2, 100 to 120/min,', 'adrenaline 10 mcg/kg (max 1 mg)', 'every 3 to 5 min'], 'b0', 'f-s')
    b += arrow(180, 140, 180, 158) + arrow(540, 140, 540, 158)
    b += box(10, 160, 700, 66, ['Surgical causes first: tamponade, bleeding, shunt or ductal stent obstruction, pacing wire',
                                'failure, tension pneumothorax, pulmonary hypertensive crisis'], 'warn', 'f-s')
    b += arrow(130, 226, 130, 244) + arrow(360, 226, 360, 244) + arrow(590, 226, 590, 244)
    b += box(10, 246, 230, 92, ['Shunt obstruction:', '100% oxygen, heparin', '50 to 100 units/kg, keep', 'systemic BP; reopen'], 'b1', 'f-s')
    b += box(250, 246, 220, 92, ['Not resolving:', 'resternotomy (ERC and', 'STS adult timing: within', '5 min for non-VF/VT)'], 'b1', 'f-s')
    b += box(480, 246, 230, 92, ['Refractory: early ECPR', 'where a programme exists', '(AHA 2025: class 2b,', 'level C-LD)'], 'b1', 'f-s')
    b += T(10, 360, 'Drawn from RCUK 2025 Paediatric Life Support, AHA 2025 PALS sections 10 and 21, and Shah 2024 (guideline timing).', 'f-s', 'start')
    b += T(10, 377, 'The paediatric AHA statement gives no fixed time to reopen; the 5-minute rule comes from adult guidance.', 'f-s', 'start')
    return svg(388, b)


# ---- figs_F41.py



def f41_ozaki_cusp():
    """Ozaki neocusp: sizing, template outline with commissural wings, and the bite ratio along the annulus."""
    b = T(12, 22, 'Measure, cut, sew: one neocusp per sinus', 'f-h', 'start')
    # panel 1: sizer between two commissures
    b += '<path d="M30 200 C60 120 170 120 200 200" class="f-l" style="stroke-width:3"/>'
    b += '<circle cx="34" cy="196" r="6" class="f-b1"/><circle cx="196" cy="196" r="6" class="f-b1"/>'
    b += line(34, 214, 196, 214) + '<line x1="34" y1="208" x2="34" y2="220" class="f-l"/><line x1="196" y1="208" x2="196" y2="220" class="f-l"/>'
    b += T(115, 234, 'Sizer horns on the two', 'f-s') + T(115, 250, 'commissures: distance in mm', 'f-s')
    b += T(115, 110, 'Annulus of one sinus', 'f-s')
    b += T(34, 182, 'C', 'f-s') + T(196, 182, 'C', 'f-s')
    # panel 2: template
    x0 = 250
    b += (f'<path d="M{x0} 70 L{x0+40} 70 L{x0+40} 60 L{x0+170} 60 L{x0+170} 70 L{x0+210} 70 '
          f'L{x0+210} 96 L{x0+176} 100 C{x0+170} 200 {x0+40} 200 {x0+34} 100 L{x0} 96 Z" class="f-b0"/>')
    b += line(x0 + 34, 64, x0 + 176, 64, 'f-dash')
    b += T(x0 + 105, 52, 'Free margin', 'f-s')
    b += T(x0 + 20, 120, 'Wing', 'f-s') + T(x0 + 192, 120, 'Wing', 'f-s')
    b += T(x0 + 105, 140, 'Belly', 'f-s')
    b += T(x0 + 105, 226, 'Cut from 0.6% glutaraldehyde', 'f-s') + T(x0 + 105, 242, 'pericardium with the matching', 'f-s')
    b += T(x0 + 105, 258, 'template; smooth side to the LV', 'f-s')
    # panel 3: bite ratio
    x1 = 500
    b += f'<path d="M{x1} 80 C{x1+20} 200 {x1+190} 200 {x1+210} 80" class="f-l" style="stroke-width:3"/>'
    b += f'<path d="M{x1+12} 72 C{x1+30} 168 {x1+180} 168 {x1+198} 72" class="f-dash"/>'
    b += f'<circle cx="{x1+105}" cy="170" r="5" class="f-b1"/>'
    b += T(x1 + 105, 196, 'Start at the nadir', 'f-s')
    b += T(x1 + 105, 62, 'Solid: annulus. Dashed: neocusp edge', 'f-s')
    b += T(x1 + 105, 226, 'Bites, annulus to cusp:', 'f-s') + T(x1 + 105, 242, '3:1 near the nadir,', 'f-s')
    b += T(x1 + 105, 258, '1:1 near the commissures', 'f-s')
    b += arrow(214, 160, 244, 140) + arrow(464, 140, 494, 140)
    b += box(10, 276, 340, 60, ['Running 4-0 polypropylene along the annulus;', 'wing fixed with a pledgeted U stitch outside'], 'b1', 'f-s')
    b += box(370, 276, 340, 60, ['Check coaptation with the LV vent on suction;', 'TOE after the clamp comes off'], 'ok', 'f-s')
    return svg(346, b)


def f41_ozaki_series():
    return tiles([
        ('850', ['Ozaki series patients,', 'mean 53.7 months'], 'b1'),
        ('85.9%', ['Freedom from death'], 'ok'),
        ('4.2%', ['Cumulative', 'reoperation'], 'warn'),
        ('13 of 15', ['Reoperations that were', 'for endocarditis'], 'warn'),
    ])


def f41_perceval_steps():
    """Perceval implantation: aortotomy height, guiding sutures, sizing, ballooning."""
    b = T(12, 22, 'Perceval: the four steps that decide the result', 'f-h', 'start')
    # root drawing
    b += '<path d="M90 300 C70 250 60 220 80 190 C60 170 64 120 96 100 L96 40" class="f-l" style="stroke-width:3"/>'
    b += '<path d="M250 300 C270 250 280 220 260 190 C280 170 276 120 244 100 L244 40" class="f-l" style="stroke-width:3"/>'
    b += line(80, 300, 260, 300, 'f-dash') + T(60, 304, 'Annulus', 'f-s', 'end')
    b += line(90, 112, 250, 112, 'f-grid') + T(170, 106, 'Sinotubular junction', 'f-s')
    b += line(92, 86, 248, 86, 'f-cut') + T(300, 90, 'Transverse aortotomy 1 to 2 cm', 'f-s', 'start')
    b += T(300, 106, 'above the STJ (3.5 cm above annulus)', 'f-s', 'start')
    # guiding sutures
    for x in (110, 170, 230):
        b += f'<path d="M{x} 310 C{x-6} 290 {x+6} 280 {x} 250" class="f-dash"/>'
        b += f'<circle cx="{x}" cy="310" r="3.5" class="f-b0"/>'
    b += T(300, 290, 'Three guiding sutures, one per sinus at 120°,', 'f-s', 'start')
    b += T(300, 306, '2 to 3 mm below the hinge; cut, never tie', 'f-s', 'start')
    b += box(10, 336, 340, 74, ['Sizing: transparent obturator passes into the LV,', 'white one sits on the annulus. Between sizes', 'take the smaller; minimum size = STJ / 1.3'], 'b0', 'f-s')
    b += box(370, 336, 340, 74, ['Balloon: matching size, 4 atm for 30 s', 'with saline at 37°C in the root;', 'LV vent suction off'], 'warn', 'f-s')
    b += box(300, 150, 410, 74, ['Decalcify the annulus and below the non-coronary', 'cusp, but do not breach it; keep the', 'aortomitral curtain intact'], 'b1', 'f-s')
    return svg(420, b)


def f41_persist_ppi():
    h, b = bars([('Stented bioprosthesis', 3.1, 'b1'), ('Perceval S', 4.9, 'ok'), ('Perceval M', 6.8, 'ok'),
                 ('Perceval L', 7.3, 'ok'), ('Perceval XL', 21.6, 'warn')],
                '%', 25, 'PERSIST-AVR: the extra early pacemakers came mainly from size XL', 230)
    b += T(12, h + 4, 'Early (0 to 30 day) permanent pacemaker; overall 10.4% Perceval against 3.1% stented (Lorusso et al.)', 'f-s', 'start')
    return svg(h + 14, b)


def f41_composite_configs():
    """Arterial graft configurations: Y, T, sequential (parallel vs diamond), extension."""
    b = T(12, 22, 'Composite and sequential arterial grafts', 'f-h', 'start')
    # Y graft
    b += '<path d="M60 50 L60 120 L40 220" class="f-vessel" style="stroke-width:7"/>'
    b += '<path d="M60 120 L110 220" class="f-vessel" style="stroke-width:5"/>'
    b += '<circle cx="60" cy="120" r="7" class="f-b1"/>'
    b += T(60, 44, 'In situ LITA', 'f-s') + T(40, 238, 'LAD', 'f-s') + T(116, 238, 'Diagonal', 'f-s')
    b += T(130, 124, 'Radial or RITA', 'f-s', 'start') + T(130, 140, 'sewn end-to-side', 'f-s', 'start')
    b += T(75, 270, 'Y graft', 'f-h')
    # T graft
    x = 260
    b += f'<path d="M{x} 50 L{x} 220" class="f-vessel" style="stroke-width:7"/>'
    b += f'<path d="M{x} 110 L{x+90} 110 L{x+90} 220" class="f-vessel" style="stroke-width:5"/>'
    b += f'<circle cx="{x}" cy="110" r="7" class="f-b1"/>'
    b += T(x, 44, 'In situ LITA', 'f-s') + T(x, 238, 'LAD', 'f-s') + T(x + 90, 238, 'Marginal', 'f-s')
    b += T(x + 50, 270, 'T graft', 'f-h')
    b += T(x + 50, 100, 'Free graft', 'f-s')
    # sequential
    x = 470
    b += f'<path d="M{x} 50 C{x} 100 {x+10} 120 {x+20} 140 L{x+120} 140 L{x+150} 220" class="f-vessel" style="stroke-width:6"/>'
    b += f'<rect x="{x+28}" y="134" width="30" height="12" rx="5" class="f-b0"/>'
    b += f'<path d="M{x+88} 128 L{x+102} 140 L{x+88} 152 L{x+74} 140 Z" class="f-b0"/>'
    b += T(x + 43, 170, 'Parallel', 'f-s') + T(x + 88, 186, 'Diamond', 'f-s')
    b += T(x + 150, 238, 'End-to-side last', 'f-s')
    b += T(x + 90, 270, 'Sequential (side-to-side)', 'f-h')
    b += T(x + 10, 44, 'Conduit', 'f-s')
    b += box(10, 290, 340, 92, ['Composite: one inflow feeds two or more targets.', 'Build the graft-to-graft join first, then the', 'distal ends (Raza et al.). Caution: single inflow,', 'possible steal (Buxton and Hayward)'], 'b1', 'f-s')
    b += box(370, 290, 340, 92, ['Parallel side-to-side is preferred; diamond if', 'conduit is short. Sequential only if targets lie', 'close together, or a loop may kink.', 'Arterial graft: target 70% or more (90% right)'], 'warn', 'f-s')
    return svg(392, b)


def f41_myectomy_incisions():
    """Surgeon's view through the aortotomy: myectomy incisions (Ralph-Edwards 2017)."""
    b = T(12, 22, "Septal myectomy seen through the aortotomy (surgeon's view, not to scale)", 'f-h', 'start')
    # annulus arcs: three cusps
    b += '<path d="M120 90 C160 190 300 190 340 90" class="f-l" style="stroke-width:3"/>'  # RCC
    b += '<path d="M340 90 C380 190 520 190 560 90" class="f-l" style="stroke-width:3"/>'  # LCC
    b += T(230, 80, 'Right coronary cusp (retracted)', 'f-s') + T(450, 80, 'Left coronary cusp', 'f-s')
    b += T(100, 82, 'Towards the non-', 'f-s', 'end') + T(100, 98, 'coronary cusp', 'f-s', 'end')
    b += '<circle cx="230" cy="166" r="4" class="f-b1"/>' + T(230, 158, 'nadir', 'f-s')
    # membranous septum zone
    b += '<rect x="70" y="180" width="110" height="70" rx="10" class="f-warn"/>'
    b += T(125, 206, 'Membranous', 'f-s') + T(125, 222, 'septum and', 'f-s') + T(125, 238, 'His bundle', 'f-s')
    # mitral annulus
    b += '<path d="M560 110 C600 160 620 220 610 300" class="f-l" style="stroke-width:3"/>'
    b += T(640, 220, ['Anterior', 'mitral', 'leaflet'], 'f-s')
    # trough
    b += '<path d="M222 180 L222 370 L585 370 L585 160 L470 172 L340 180 Z" class="f-b0" style="opacity:.6"/>'
    # incisions
    b += line(222, 180, 222, 370, 'f-cut') + T(212, 300, 'Incision 1', 'f-s', 'end')
    b += line(222, 182, 340, 182, 'f-cut') + line(340, 182, 470, 174, 'f-cut')
    b += T(400, 200, 'Incisions 2 and 3: 2 mm below the hinges', 'f-s')
    b += line(585, 160, 585, 370, 'f-dash') + T(575, 330, 'Stop 4 to 5 mm', 'f-s', 'end') + T(575, 346, 'from mitral annulus', 'f-s', 'end')
    b += T(400, 280, 'Trough: 1 to 1.5 cm deep, 35 to 50 mm long', 'f-t')
    b += T(400, 300, 'leave 8 to 10 mm of septum', 'f-s')
    b += '<path d="M340 182 C330 230 335 250 345 262" class="f-dash"/>'
    b += T(352, 240, 'Do not flare under R-L commissure (VSD)', 'f-s', 'start')
    b += arrow(400, 384, 400, 410) + T(400, 426, 'Towards the apex: at least 1 cm past the SAM contact scar', 'f-s')
    b += box(10, 270, 200, 120, ['Incision 1 starts', '2 mm below the right', 'cusp hinge, 2 mm off its', 'midline towards the', 'membranous septum;', 'further right = block'], 'warn', 'f-s')
    return svg(440, b)


def f41_pacing_wires():
    """Temporary epicardial wires: sites and exit sides (CTSNet step-by-step series)."""
    b = T(12, 22, 'Temporary epicardial wires: where they go and where they exit', 'f-h', 'start')
    b += '<path d="M260 70 C200 90 180 190 230 250 C280 300 420 300 470 240 C520 180 480 80 400 70 Z" class="f-b1"/>'
    b += '<ellipse cx="250" cy="100" rx="40" ry="26" class="f-b0"/>' + T(250, 104, 'RA appendage', 'f-s')
    b += T(380, 170, 'Right ventricle', 'f-s')
    b += '<path d="M240 260 C300 290 400 290 450 255" class="f-dash"/>' + T(345, 304, 'Diaphragmatic RV surface', 'f-s')
    # wires
    b += '<path d="M240 112 C200 200 230 330 300 380" class="f-nerve"/>'
    b += '<path d="M380 280 C400 320 410 350 420 380" class="f-nerve"/>'
    b += line(360, 330, 360, 400, 'f-dash') + T(360, 416, 'Midline (below the sternotomy)', 'f-s')
    b += '<circle cx="300" cy="380" r="5" class="f-b0"/>' + '<circle cx="420" cy="380" r="5" class="f-b0"/>'
    b += T(290, 396, 'Atrial: exits right', 'f-s', 'end') + T(430, 396, 'Ventricular: exits left', 'f-s', 'start')
    b += T(178, 300, "Patient's right", 'f-s', 'end') + T(540, 300, "Patient's left", 'f-s', 'start')
    b += box(530, 60, 180, 110, ['Avoid vessels and', 'grafts; keep atrial', 'bare wire off the RV;', 'straight exit path'], 'warn', 'f-s')
    b += box(10, 60, 150, 110, ['Daily: rhythm,', 'sensing, capture;', 'output at twice', 'the threshold'], 'ok', 'f-s')
    b += box(10, 430, 700, 46, ['Remove by gentle traction; watch for tamponade for a few hours afterwards'], 'b0', 'f-s')
    return svg(486, b)


# ---- figs_F42.py



def _f42_num(x, y, n, cls='b1'):
    return (f'<circle cx="{x}" cy="{y}" r="12" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def f42_safe_triangle():
    """BTS triangle of safety on the lateral chest wall, plus the 'above the rib' rule."""
    b = T(12, 22, 'Chest drain: the triangle of safety (BTS 2010) and the rib rule', 'f-h', 'start')
    # left panel: right lateral chest wall, patient supine, arm abducted behind head
    b += '<path d="M60 70 C90 52 150 46 200 50 L330 58 C350 62 360 80 356 110 L346 330 L70 330 L56 120 Z" class="f-b0"/>'
    # arm going up and back
    b += '<path d="M180 50 C200 30 260 26 330 34 L332 58 L200 56 Z" class="f-track"/>'
    b += '<path d="M180 50 C200 30 260 26 330 34" class="f-l"/>'
    b += T(300, 46, 'arm abducted', 'f-s', 'end')
    # ribs
    for i in range(7):
        y = 104 + i * 32
        b += f'<path d="M66 {y + 14} C150 {y - 4} 260 {y - 4} 352 {y + 10}" class="f-grid" fill="none"/>'
    # pectoralis major lateral border (anterior, patient's front on the left)
    b += '<path d="M108 60 C116 110 120 150 120 214" class="f-cut"/>'
    b += T(96, 262, ['Lateral border', 'of pectoralis major'], 'f-s', 'middle')
    # latissimus dorsi lateral edge (posterior, on the right)
    b += '<path d="M290 60 C282 110 276 160 270 214" class="f-cut"/>'
    b += T(290, 262, ['Lateral edge', 'of latissimus dorsi'], 'f-s', 'middle')
    # fifth space line
    b += line(96, 214, 300, 214, 'f-dash')
    b += T(196, 308, 'Dashed: horizontal level of the 5th space', 'f-s')
    # triangle
    b += '<path d="M200 62 L120 212 L270 212 Z" class="f-ok" style="opacity:.85"/>'
    b += T(196, 160, 'Insert here', 'f-h')
    b += T(196, 178, 'over the top of a rib', 'f-s')
    b += T(196, 82, 'axilla', 'f-s')
    b += T(60, 350, "Patient's front", 'f-s', 'start') + T(346, 350, 'Back', 'f-s', 'end')
    # right panel: rib cross-section
    x0 = 420
    b += T(x0, 76, 'Intercostal space in section', 'f-h', 'start')
    for y in (110, 262):
        b += f'<rect x="{x0 + 20}" y="{y}" width="150" height="46" rx="18" class="f-b1"/>'
    b += T(x0 + 95, 138, 'upper rib', 'f-s') + T(x0 + 95, 290, 'lower rib', 'f-s')
    # neurovascular bundle under the upper rib (VAN)
    b += f'<circle cx="{x0 + 132}" cy="168" r="7" class="f-warn"/>'
    b += f'<circle cx="{x0 + 148}" cy="170" r="6" class="f-warn"/>'
    b += f'<circle cx="{x0 + 162}" cy="172" r="5" class="f-b0"/>'
    b += T(x0 + 20, 196, ['Vein, artery, nerve run in the', 'groove under each rib'], 'f-s', 'start')
    # needle just above lower rib
    b += f'<line x1="{x0 - 10}" y1="250" x2="{x0 + 120}" y2="250" class="f-l" marker-end="url(#ah)" style="stroke-width:2.5"/>'
    b += T(x0 + 20, 242, 'needle just above the lower rib', 'f-s', 'start')
    b += box(x0 - 10, 322, 300, 52, ['Posteriorly the bundle may not be covered by', 'the rib flange: go lateral or anterior'], 'warn', 'f-s')
    return svg(388, b)


def f42_uniportal():
    """Uniportal VATS: one 4 to 5 cm 5th space incision, camera posterior, instruments anterior."""
    b = T(12, 22, 'Uniportal VATS lobectomy: one incision, everything in parallel', 'f-h', 'start')
    # lateral chest wall with ribs, patient lateral, head to the left
    b += '<rect x="30" y="46" width="420" height="250" rx="40" class="f-b0"/>'
    for i in range(6):
        x = 70 + i * 66
        b += f'<path d="M{x} 54 C{x + 20} 120 {x + 22} 220 {x + 6} 290" class="f-grid" fill="none"/>'
    b += T(40, 316, 'Head', 'f-s', 'start') + T(440, 316, 'Feet', 'f-s', 'end')
    b += T(240, 336, 'Ribs drawn running down the page; the incision lies along the 5th space', 'f-s')
    # incision along 5th ICS anterior
    b += '<path d="M236 92 C246 120 250 150 250 176" class="f-cut" style="stroke-width:5"/>'
    b += T(262, 100, ['4 to 5 cm, 5th space,', 'anterior (about the', 'anterior axillary line)'], 'f-s', 'start')
    b += T(70, 80, 'Back', 'f-s', 'start') + T(70, 284, 'Front', 'f-s', 'start')
    b += line(52, 76, 52, 270, 'f-dash')
    # right panel: incision seen face-on
    x0 = 480
    b += T(x0, 60, 'Incision seen end-on', 'f-h', 'start')
    b += f'<rect x="{x0}" y="80" width="220" height="56" rx="28" class="f-lumen"/>'
    b += f'<circle cx="{x0 + 186}" cy="108" r="16" class="f-warn"/>'
    b += T(x0 + 186, 113, 'cam', 'f-s')
    for i, lab in enumerate(['1', '2', '3']):
        b += _f42_num(x0 + 34 + i * 44, 108, lab, 'b1')
    b += T(x0, 160, 'Front', 'f-s', 'start') + T(x0 + 220, 160, 'Back', 'f-s', 'end')
    b += T(x0, 184, ['30 degree scope, no trocar, at the', 'posterior end; 3 or 4 long curved', 'instruments in front of it'], 'f-s', 'start')
    b += box(x0 - 10, 246, 240, 50, ['No rib spreading; one drain at', 'the posterior end of the wound'], 'ok', 'f-s')
    b += box(30, 350, 660, 46, ['Surgeon and assistant both stand in front, on one monitor. Table rolled away for the hilum,',
                                'towards the surgeon for nodes. Series of 222 resections: conversion 3.6%, median stay 3 days'], 'b1', 'f-s')
    return svg(408, b)


def f42_robot_ports():
    """Four-arm completely portal robotic lobectomy port line (Cerfolio)."""
    b = T(12, 22, 'Four-arm totally portal robotic lobectomy: right side (Cerfolio)', 'f-h', 'start')
    # chest wall band with the intercostal space line
    b += '<rect x="30" y="50" width="660" height="170" rx="30" class="f-b0"/>'
    b += line(60, 140, 660, 140, 'f-dash')
    b += T(46, 70, 'Port line: 7th space (upper, middle lobe) or 8th (lower lobe)', 'f-s', 'start')
    b += T(40, 240, "Front (patient's anterior)", 'f-s', 'start') + T(680, 240, 'Back: spine', 'f-s', 'end')
    b += f'<rect x="672" y="60" width="14" height="150" rx="6" class="f-track"/>'
    xs = [150, 330, 510, 640]
    labs = [('Arm 1', 'right hand', '8 mm'), ('Camera', '0 degree', '8 or 12 mm'), ('Arm 2', 'left hand', '8 mm'), ('Arm 3', 'fourth arm', '5 or 8 mm')]
    for x, (a, r, s) in zip(xs, labs):
        b += f'<circle cx="{x}" cy="140" r="14" class="f-warn"/>'
        b += T(x, 92, a, 'f-h') + T(x, 108, r, 'f-s') + T(x, 168, s, 'f-s')
    for (x1, x2, d) in [(150, 330, '9 cm'), (330, 510, '9 cm'), (510, 640, '10 cm')]:
        b += f'<line x1="{x1 + 16}" y1="200" x2="{x2 - 16}" y2="200" class="f-l" marker-end="url(#ah)" marker-start="url(#ah)"/>'
        b += T((x1 + x2) / 2, 196, d, 'f-n')
    b += T(640, 72, '2 to 3 cm from spine', 'f-s', 'end')
    # assistant port below
    b += f'<circle cx="230" cy="290" r="14" class="f-ok"/>'
    b += '<path d="M150 154 L230 276 M330 154 L230 276" class="f-dash"/>'
    b += T(252, 286, ['Assistant 12 mm: just above the diaphragm,', 'as anteroinferior as possible; triangle with', 'camera and arm 1'], 'f-s', 'start')
    b += box(30, 350, 320, 72, ['Si: cart steered in about 15 degrees', 'over the shoulder; 12 mm camera', 'port; 5 mm fourth arm'], 'b1', 'f-s')
    b += box(370, 350, 320, 72, ['Xi: cart from the side, perpendicular,', 'boom rotated into place; all', 'robotic ports 8 mm'], 'b1', 'f-s')
    b += T(12, 444, ['Warm humidified CO2. Ports 2 to 4 on the same rib to spare neurovascular bundles.', 'Distances and sizes from Ramadan, Wei, Cerfolio 2017.'], 'f-s', 'start')
    return svg(472, b)


def f42_diaphragm_incisions():
    """Peripheral circumferential against radial phrenotomy, diaphragm seen from below."""
    b = T(12, 22, 'Opening the diaphragm: circumferential spares the phrenic branches', 'f-h', 'start')
    cx, cy = 250, 200
    b += f'<ellipse cx="{cx}" cy="{cy}" rx="220" ry="150" class="f-b0"/>'
    # central tendon trefoil
    b += (f'<path d="M{cx - 70} {cy + 10} C{cx - 90} {cy - 50} {cx - 30} {cy - 70} {cx} {cy - 40} '
          f'C{cx + 30} {cy - 70} {cx + 90} {cy - 50} {cx + 70} {cy + 10} C{cx + 50} {cy + 40} {cx - 50} {cy + 40} {cx - 70} {cy + 10} Z" class="f-b1"/>')
    b += T(cx, cy - 4, 'central tendon', 'f-s')
    # hiatus
    b += f'<ellipse cx="{cx + 30}" cy="{cy + 76}" rx="20" ry="14" class="f-lumen"/>'
    b += T(cx + 6, cy + 106, 'oesophageal hiatus', 'f-s', 'end')
    # phrenic entry on left hemidiaphragm (right of drawing = patient's left seen from below?) keep generic
    ex, ey = cx + 110, cy - 10
    b += f'<circle cx="{ex}" cy="{ey}" r="7" class="f-warn"/>'
    for dx, dy in [(-30, -110), (60, -95), (95, 10), (40, 110), (-40, 100)]:
        b += f'<path d="M{ex} {ey} Q{ex + dx * 0.4} {ey + dy * 0.6} {ex + dx} {ey + dy}" class="f-nerve"/>'
    b += T(ex + 4, ey - 16, 'phrenic', 'f-s', 'start')
    # circumferential incision: arc 3 to 4 cm inside the costal margin
    b += f'<path d="M{cx - 150} {cy + 96} A190 125 0 0 1 {cx + 150} {cy - 96}" class="f-cut" style="stroke-dasharray:9 5;stroke-width:3"/>'
    b += _f42_num(cx - 166, cy - 30, 'A', 'ok')
    # radial incision from costal margin to hiatus
    b += f'<line x1="{cx + 210}" y1="{cy + 50}" x2="{cx + 48}" y2="{cy + 72}" class="f-cut" style="stroke-width:4"/>'
    b += _f42_num(cx + 160, cy + 80, 'B', 'warn')
    # right-side legend
    x0 = 490
    b += box(x0, 60, 220, 92, ['A Circumferential, 3 to 4 cm', 'rim left on the chest wall:', 'branches are spared'], 'ok', 'f-s')
    b += box(x0, 164, 220, 92, ['B Radial, costal margin to', 'hiatus: crosses the branches', 'and paralyses the muscle'], 'warn', 'f-s')
    b += box(x0, 268, 220, 92, ['Short incision in the central', 'tendon or a limited phrenotomy', 'when access allows'], 'b1', 'f-s')
    b += T(12, 378, 'Seen from below, schematic: the nerve branches on the abdominal surface and radiates outward.', 'f-s', 'start')
    return svg(392, b)


def f42_itmig():
    """ITMIG three-compartment model on an axial schematic."""
    b = T(12, 22, 'ITMIG mediastinal compartments on axial CT (schematic)', 'f-h', 'start')
    cx = 250
    # chest outline
    b += f'<ellipse cx="{cx}" cy="210" rx="230" ry="160" class="f-track"/>'
    b += f'<ellipse cx="{cx}" cy="210" rx="230" ry="160" class="f-l"/>'
    # lungs
    b += f'<ellipse cx="{cx - 130}" cy="210" rx="80" ry="120" class="f-lumen"/>'
    b += f'<ellipse cx="{cx + 130}" cy="210" rx="80" ry="120" class="f-lumen"/>'
    # sternum
    b += f'<rect x="{cx - 30}" y="52" width="60" height="18" rx="6" class="f-b1"/>'
    b += T(cx, 46, 'sternum', 'f-s')
    # prevascular compartment
    b += f'<path d="M{cx - 46} 74 L{cx + 46} 74 C{cx + 56} 100 {cx + 50} 116 {cx + 40} 122 L{cx - 40} 122 C{cx - 50} 116 {cx - 56} 100 {cx - 46} 74 Z" class="f-ok"/>'
    # visceral: pericardium/heart, aorta, oesophagus
    b += f'<path d="M{cx - 44} 124 L{cx + 44} 124 C{cx + 56} 170 {cx + 50} 250 {cx + 38} 286 L{cx - 38} 286 C{cx - 50} 250 {cx - 56} 170 {cx - 44} 124 Z" class="f-b0"/>'
    b += f'<circle cx="{cx - 8}" cy="190" r="26" class="f-b1"/>'
    b += T(cx - 8, 194, 'heart', 'f-s')
    b += f'<circle cx="{cx + 26}" cy="262" r="12" class="f-warn"/>'
    b += f'<circle cx="{cx - 10}" cy="268" r="7" class="f-lumen"/>'
    # vertebral body
    b += f'<rect x="{cx - 32}" y="288" width="64" height="48" rx="14" class="f-b1"/>'
    b += f'<rect x="{cx - 80}" y="296" width="160" height="10" rx="4" class="f-b1"/>'
    # boundary line 1 cm behind anterior vertebral margin
    b += line(cx - 110, 300, cx + 110, 300, 'f-cut')
    # paravertebral
    b += f'<path d="M{cx - 90} 302 L{cx - 34} 302 L{cx - 34} 344 L{cx - 84} 340 Z" class="f-warn"/>'
    b += f'<path d="M{cx + 90} 302 L{cx + 34} 302 L{cx + 34} 344 L{cx + 84} 340 Z" class="f-warn"/>'
    # labels with leader lines
    b += line(cx + 50, 98, 500, 96, 'f-grid') + line(cx + 52, 200, 500, 196, 'f-grid')
    b += line(cx + 86, 320, 500, 312, 'f-grid') + line(cx + 110, 300, 500, 260, 'f-grid')
    b += box(500, 64, 210, 64, ['Prevascular: sternum to', 'pericardium; thymus, fat,', 'nodes, left innominate vein'], 'ok', 'f-s')
    b += box(500, 160, 210, 72, ['Visceral: heart, great vessels,', 'trachea, oesophagus, thoracic', 'duct, nodes'], 'b0', 'f-s')
    b += T(500, 252, ['Red line: 1 cm behind the front', 'of the vertebral bodies'], 'f-s', 'start')
    b += box(500, 290, 210, 64, ['Paravertebral: spine and', 'paravertebral soft tissue;', 'neurogenic tumours'], 'warn', 'f-s')
    b += T(12, 392, ['All three run from thoracic inlet to diaphragm.', 'Assign a mass by its centre on the axial slice where it is widest.'], 'f-s', 'start')
    return svg(420, b)


def f42_tos_outcomes():
    """Pleural breach and success by approach, Suzuki 2022 review."""
    h1, b1 = bars([('Transaxillary (2,326)', 14, 'b1'),
                   ('Supraclavicular + first rib (683)', 19, 'warn'),
                   ('Supraclavicular scalenectomy only (674)', 5, 'b1'),
                   ('Infraclavicular (55)', 7, 'b1'),
                   ('Endoscopic transaxillary (131)', 3, 'ok')],
                  '%', 25, 'Pneumothorax or pleura opened: highest with supraclavicular first rib excision', lab_w=300)
    h2, b2 = bars([('Transaxillary', 76, 'b0'),
                   ('Supraclavicular + first rib', 77, 'b0'),
                   ('Supraclavicular scalenectomy only', 85, 'b0')],
                  '%', 100, 'Pooled success is similar across the three main approaches', lab_w=300)
    b = b1 + f'<g transform="translate(0,{h1})">' + b2 + '</g>'
    b += T(12, h1 + h2 + 12, 'Suzuki et al., J Hand Surg Glob Online 2022; pooled case series, not randomised. Numbers in brackets: patients.', 'f-s', 'start')
    return svg(h1 + h2 + 24, b)


# ---- figs_F43.py



def _f43_g(dy, body):
    return f'<g transform="translate(0,{dy})">{body}</g>'


def f43_bita_mediastinitis():
    h, b = bars([
        ('Single ITA, non-diabetic', (0.2, 1.2), 'ok'),
        ('Skeletonised bilateral ITA', (0.4, 2.6), 'ok'),
        ('Pedicled bilateral ITA, non-diabetic', (1.3, 4.7), 'warn'),
        ('Pedicled bilateral ITA, diabetic (some series)', 10, 'warn'),
    ], '%', 12, 'Mediastinitis: skeletonising brings bilateral ITA close to single ITA', lab_w=330)
    b += T(12, h + 8, 'Ranges across the 24 papers in Toumpoulis, Theakos and Dunning, ICVTS 2007.', 'f-s', 'start')
    b += T(12, h + 25, 'The diabetic pedicled bar is the summary statement "can exceed 10% in some series".', 'f-s', 'start')
    return svg(h + 38, b)


def f43_txa_dose():
    h1, b1 = bars([
        ('Low dose: blood loss day 1', 820, 'warn'),
        ('High dose: blood loss day 1', 590, 'ok'),
    ], ' ml', 1000, 'Tranexamic acid: high dose bleeds less, but seizures rise with dose', lab_w=300)
    h2, b2 = bars([
        ('Low dose: re-operation for bleeding', 6.2, 'warn'),
        ('High dose: re-operation for bleeding', 2.5, 'ok'),
        ('Seizures, 50 mg/kg bolus (registry)', 0.3, 'ok'),
        ('Seizures, over 80 mg/kg total (registry)', 2.6, 'warn'),
    ], '%', 8, None, lab_w=300)
    b = b1 + _f43_g(h1 - 14, b2)
    y = h1 - 14 + h2
    b += T(12, y + 8, 'Bleeding: Sigaut 2014 randomised trial, 569 patients. Seizures: Sharma 2014, 11,529 patients, observational.', 'f-s', 'start')
    b += T(12, y + 25, 'Low dose 10 mg/kg + 1 mg/kg/h + 1 mg/kg prime. High dose 30 mg/kg + 16 mg/kg/h + 2 mg/kg prime.', 'f-s', 'start')
    b += T(12, y + 42, 'As reported in Hodgson, Larvin and Dearman, ICVTS 2015.', 'f-s', 'start')
    return svg(y + 55, b)


def f43_reexploration():
    h1, b1 = bars([
        ('Vivacqua 2011: no return to theatre', 1.8, 'ok'),
        ('Vivacqua 2011: return to theatre', 8.5, 'warn'),
        ('Fröjd 2016: no return to theatre', 2.4, 'ok'),
        ('Fröjd 2016: return to theatre', 7.6, 'warn'),
        ('Ruel 2017 (in hospital): no return', 2.8, 'ok'),
        ('Ruel 2017 (in hospital): return', 12, 'warn'),
    ], '%', 25, 'Death after re-exploration for bleeding: worse, and far worse if delayed', lab_w=300)
    h2, b2 = bars([
        ('Re-explored within 12 hours', 5.1, 'ok'),
        ('Re-explored after 12 hours', 21.5, 'warn'),
    ], '%', 25, None, lab_w=300)
    b = b1 + T(12, h1 + 6, 'Timing (Biancari 2012 meta-analysis, 557,923 patients; relative risk of death 3.27 overall)', 'f-s', 'start')
    b += _f43_g(h1 + 2, b2)
    y = h1 + 2 + h2
    b += T(12, y + 8, 'Mortality at 30 days unless stated. From Ali, Wallwork and Moorjani, ICVTS 2019.', 'f-s', 'start')
    return svg(y + 22, b)


def f43_poaf_prevention():
    h, b = bars([
        ('Beta-blocker: control', 33, 'warn'),
        ('Beta-blocker: treated', 19, 'ok'),
        ('Posterior pericardiotomy: control', 28.1, 'warn'),
        ('Posterior pericardiotomy: done', 10.8, 'ok'),
        ('Atorvastatin 40 mg, 7 days: placebo', 57, 'warn'),
        ('Atorvastatin 40 mg, 7 days: treated', 35, 'ok'),
    ], '%', 70, 'Postoperative AF falls with each of three measures', lab_w=300)
    b += T(12, h + 8, 'Beta-blockers: Crystal 2002, 27 trials (number needed to treat 7). Pericardiotomy: Biancari 2010, 6 trials (NNT 6).', 'f-s', 'start')
    b += T(12, h + 25, 'Statin: ARMYDA-3, 200 patients. As reported in the ICVTS best evidence topics of 2004, 2012 and 2015.', 'f-s', 'start')
    return svg(h + 38, b)


def f43_tr_thresholds():
    return tiles([
        ('≥ 21 mm/m²', ['annulus indexed', 'to body surface area'], 'b0'),
        ('≥ 3.5 cm', ['annulus on', 'transthoracic echo'], 'b0'),
        ('> 70 mm', ['annulus measured', 'at operation'], 'b0'),
        ('AF · lead', ['or rheumatic disease:', 'also favour repair'], 'b1'),
    ], h=100)


# ---- figs_F44.py



def f44_suction_bet():
    """Prolonged air leak with water seal against suction in the trials of the suction best evidence topic."""
    h, b = bars([
        ('Cerfolio 2001, >3 d: water seal', 33, 'ok'),
        ('Cerfolio 2001, >3 d: suction', 93, 'warn'),
        ('Ayed 2003, >5 d: water seal', 2, 'ok'),
        ('Ayed 2003, >5 d: suction', 14, 'warn'),
        ('Alphonso 2005, >6 d: no suction', 10.1, 'ok'),
        ('Alphonso 2005, >6 d: suction', 7.8, 'warn'),
        ('Brunelli 2004, >7 d: water seal', 27.8, 'ok'),
        ('Brunelli 2004, >7 d: suction', 30.1, 'warn'),
    ], '%', 100, 'No trial found less prolonged air leak on suction', lab_w=300)
    b += T(12, h + 4, 'Cerfolio P=0.001, Ayed P=0.03; Alphonso P=0.62, Brunelli P=0.8. Leak definitions differ.', 'f-s', 'start')
    return svg(h + 16, b)


def f44_one_two_drains():
    """Pawelczyk 2007 RCT: one against two drains after lobectomy."""
    h, b = bars([
        ('Opioid use: one drain', 4.8, 'ok'),
        ('Opioid use: two drains', 5.6, 'b1'),
        ('NSAID use: one drain', 6.8, 'ok'),
        ('NSAID use: two drains', 7.7, 'b1'),
        ('Hospital stay: one drain', 7.6, 'ok'),
        ('Hospital stay: two drains', 9.0, 'b1'),
    ], ' days', 10, 'One drain: shorter analgesic use and stay (RCT, n=187)')
    b += T(12, h + 4, 'P=0.0001, 0.002 and 0.001 respectively. Pawelczyk 2007, as tabulated by Dawson and Hosmane 2010.', 'f-s', 'start')
    return svg(h + 16, b)


def f44_pleurodesis():
    """Recurrence and bleeding by pleurodesis method in the Sepehripour 2012 topic."""
    h1, b1 = bars([
        ('Talc (n=279)', 1.79, 'ok'),
        ('Pleurectomy (n=153)', 9.15, 'warn'),
    ], '%', 12, 'Cardillo 2000 cohort: recurrence lower after talc (P=0.00018)')
    h2, b2 = bars([
        ('Recurrence: abrasion', 6.2, 'b1'),
        ('Recurrence: pleurectomy', 4.6, 'b1'),
        ('Bleeding: abrasion', 0.9, 'ok'),
        ('Bleeding: pleurectomy', 7.4, 'warn'),
    ], '%', 12, 'Rena 2008 RCT (220 VATS): same recurrence, more bleeding after pleurectomy')
    b2 = f'<g transform="translate(0,{h1})">{b2}</g>'
    note = T(12, h1 + h2 + 4, 'Rena: recurrence P=0.821; bleeding P=0.036; operating time 38 against 55 min (P=0.0001).', 'f-s', 'start')
    return svg(h1 + h2 + 16, b1 + b2 + note)


def f44_vats_empyema():
    """Fibrinopurulent empyema, VATS against chest tube drainage, from the Chambers 2010 topic."""
    h1, b1 = bars([
        ('VATS', 91, 'ok'),
        ('Chest tube drainage', 44, 'warn'),
    ], '%', 100, 'Fibrinopurulent empyema: treatment success (P<0.05)')
    h2, b2 = bars([
        ('Chest tube time: VATS', 5.8, 'ok'),
        ('Chest tube time: drain only', 9.8, 'warn'),
        ('Hospital stay: VATS', 8.7, 'ok'),
        ('Hospital stay: drain only', 12.8, 'warn'),
    ], ' days', 14, 'Shorter drainage (P=0.03) and stay (P=0.009) after VATS')
    b2 = f'<g transform="translate(0,{h1})">{b2}</g>'
    return svg(h1 + h2, b1 + b2)


# ---- figs_F45.py



def f45_hf_crt():
    """CRT by QRS width and morphology, ESC 2026 heart failure guideline (official slide set)."""
    b = T(12, 22, 'CRT in sinus rhythm, symptomatic, LVEF 35% or less on optimal therapy', 'f-h', 'start')
    b += T(330, 52, 'QRS 130 to 149 ms', 'f-s') + T(560, 52, 'QRS 150 ms or more', 'f-s')
    b += T(200, 92, 'LBBB', 'f-h', 'end') + T(200, 152, 'Not LBBB', 'f-h', 'end')
    b += box(220, 62, 220, 50, ['Should be considered', 'IIa C'], 'b0', 'f-s')
    b += box(450, 62, 220, 50, ['Recommended', 'I A'], 'ok', 'f-s')
    b += box(220, 122, 220, 50, ['May be considered', 'IIb C'], 'b1', 'f-s')
    b += box(450, 122, 220, 50, ['Should be considered', 'IIa C'], 'b0', 'f-s')
    b += box(10, 186, 345, 52, ['QRS under 130 ms and no pacing indication', 'for AV block: not recommended (III A)'], 'warn', 'f-s')
    b += box(365, 186, 345, 52, ['High-degree AV block needing ventricular pacing:', 'CRT rather than RV pacing (IIa B1; was I A in 2021)'], 'b1', 'f-s')
    b += box(10, 248, 345, 52, ['Pacemaker or ICD, LVEF 35% or less, worsening', 'failure, much RV pacing: upgrade to CRT (IIa B1)'], 'b1', 'f-s')
    b += box(365, 248, 345, 52, ['Permanent AF, poor rate control, one or more', 'admissions: AV node ablation with CRT (IIa B1)'], 'b1', 'f-s')
    return svg(310, b)


def f45_hf_advanced():
    """Advanced heart failure pathway, ESC 2026 heart failure guideline (official slide set)."""
    b = box(10, 8, 340, 78, ['Rule of three (any one):', '2 or more admissions in a year (or 1 on inotropes),', 'diuretic resistance, drug intolerance', 'with cardiorenal syndrome'], 'b1', 'f-s')
    b += box(370, 8, 340, 78, ['I NEED HELP (any one): inotropes, NYHA III/IV,', 'end-organ dysfunction, EF under 20%, shocks,', 'admissions, escalating diuretics, low pressure,', 'intolerance of prognostic drugs'], 'b1', 'f-s')
    b += arrow(180, 86, 300, 108) + arrow(540, 86, 420, 108)
    b += box(160, 110, 400, 46, ['Early consultation with an advanced heart failure centre', 'I A'], 'ok', 'f-s')
    b += arrow(360, 156, 360, 174)
    b += box(160, 176, 400, 46, ['Evaluation: cardiopulmonary exercise test (I C)', 'and right heart catheter (I C)'], 'b0', 'f-s')
    b += arrow(250, 222, 180, 246) + arrow(470, 222, 540, 246)
    b += box(10, 248, 340, 64, ['Durable LVAD (I C)', 'bridge to transplant, candidacy or recovery,', 'or destination therapy'], 'ok', 'f-s')
    b += box(370, 248, 340, 64, ['Heart transplantation (I C)', 'refractory to drugs and interventions,', 'no contraindication'], 'ok', 'f-s')
    b += box(10, 324, 700, 44, ['While waiting: continuous inotropes as a bridge (IIa C); temporary support for', 'haemodynamic instability as a bridge (IIa C); rehabilitation after LVAD (I B1)'], 'b1', 'f-s')
    return svg(378, b)


def f45_hf_changes():
    """Recommendations whose class changed between ESC 2021 and ESC 2026 (slide set, revised table)."""
    rows = [('Durable LVAD in advanced HFrEF', 'IIa A / IIa B', 'I C', 'ok'),
            ('Mitral TEER, severe secondary MR, criteria met', 'IIa B', 'I B1', 'ok'),
            ('Revascularisation for angina despite drugs', 'IIa C', 'I C', 'ok'),
            ('Continuous inotropes as a bridge', 'IIb C', 'IIa C', 'b0'),
            ('Pulmonary artery pressure monitoring', 'IIb B', 'IIa B1', 'b0'),
            ('CRT instead of RV pacing in AV block', 'I A', 'IIa B1', 'warn')]
    b = T(12, 22, 'Surgical and device recommendations: 2021 class against 2026 class', 'f-h', 'start')
    b += T(430, 48, '2021', 'f-s') + T(620, 48, '2026', 'f-s')
    y = 58
    for lab, old, new, cls in rows:
        b += T(350, y + 25, lab, 'f-s', 'end')
        b += box(365, y, 130, 38, old, 'b1', 'f-s')
        b += arrow(498, y + 19, 552, y + 19)
        b += box(555, y, 130, 38, new, cls, 'f-s')
        y += 46
    b += T(12, y + 14, 'Top three rows: upgraded to class I. Next two: upgraded to IIa. Last row: downgraded.', 'f-s', 'start')
    return svg(y + 26, b)


# ---- figs_F46.py



def f46_htx_surveillance():
    """Surveillance timeline after heart transplant, ISHLT 2022 (Velleca 2023)."""
    b = T(12, 22, 'Surveillance after heart transplant (ISHLT 2022 guideline, class and level)', 'f-h', 'start')
    x0, x1 = 150, 700
    pts = [(0, 'Day 0'), (0.12, '2 mo'), (0.22, '3 mo'), (0.42, '12 mo'), (0.62, '3 y'), (0.80, '5 y'), (1.0, 'later')]
    ay = 52
    b += line(x0, ay, x1, ay)
    for f, lab in pts:
        x = x0 + f * (x1 - x0)
        b += line(x, ay - 5, x, ay + 5) + T(x, ay - 10, lab, 'f-s')

    def X(f):
        return x0 + f * (x1 - x0)

    rows = [
        ('Biopsy', [(0.0, 0.42, 'ok', 'Surveillance EMB 3 to 12 mo: IIa, C'),
                    (0.42, 0.80, 'b1', 'Higher risk only: IIa, C'),
                    (0.80, 1.0, 'warn', 'Routine: III, C')]),
        ('Gene profile', [(0.12, 0.80, 'ok', 'Low-risk adults, 2 mo to 5 y: IIa, B')]),
        ('DSA', [(0.0, 0.42, 'ok', '1, 3, 6, 12 mo: IIa, C'), (0.42, 1.0, 'b1', 'Then yearly')]),
        ('Angiography', [(0.0, 0.42, 'ok', 'Baseline IVUS 4 to 6 wk and 1 y: IIa, B'),
                         (0.42, 1.0, 'b1', 'Every 1 to 2 years: I, C (less often if CAV-free)')]),
    ]
    y = 74
    for lab, segs in rows:
        b += T(140, y + 23, lab, 'f-h', 'end')
        for f0, f1, cls, txt in segs:
            w = X(f1) - X(f0) - 4
            b += f'<rect x="{X(f0) + 2}" y="{y + 4}" width="{w}" height="30" rx="6" class="f-{cls}"/>'
            b += T(X(f0) + 2 + w / 2, y + 24, txt, 'f-s')
        y += 42
    b += box(10, y + 6, 700, 40, ['Not for rejection monitoring: ECG, BNP, troponin, CRP, routine MRI, ImmuKnow (III)'], 'warn')
    return svg(y + 56, b)


def f46_trough_targets():
    """Tacrolimus troughs with MMF or AZA (ISHLT 2022, IIa, C)."""
    h, b = bars([('Tacrolimus, day 0 to 60', (10, 15), 'b1'),
                 ('Tacrolimus, month 3 to 6', (8, 12), 'b1'),
                 ('Tacrolimus, after 6 months', (5, 10), 'b1'),
                 ('Tacrolimus with mTOR, after 6 mo', (3, 8), 'warn'),
                 ('Everolimus with a CNI', (3, 8), 'ok'),
                 ('Everolimus, CNI-free', (6, 10), 'ok'),
                 ('Sirolimus with a CNI', (4, 12), 'ok'),
                 ('Sirolimus, CNI-free', (8, 15), 'ok')],
                ' ng/ml', 16, 'Target troughs fall with time after transplant (ISHLT 2022)', lab_w=270)
    return svg(h, b)


def f46_uk_tiers():
    """NHSBT CTAG(25)26: adult heart registrations April 2022 to March 2025."""
    h, b = bars([('Super-urgent (187 registrations)', 84, 'ok'),
                 ('Urgent (409)', 68, 'b1'),
                 ('Non-urgent (401)', 25, 'warn')],
                '%', 100, 'Super-urgent listing gets most patients transplanted (UK, 2022 to 2025)', lab_w=270)
    h2, b2 = bars([('Super-urgent', 16, 'ok'), ('Urgent', 56, 'b1')],
                  ' days', 70, 'Median wait to transplant (non-urgent: too few transplants to calculate)', lab_w=270)
    b2 = f'<g transform="translate(0,{h})">{b2}</g>'
    return svg(h + h2, b + b2)


# ---- figs_F47.py



def _f47_stack(*parts):
    """Stack (height, body) chart blocks vertically."""
    out, y = '', 0
    for h, b in parts:
        out += f'<g transform="translate(0 {y})">{b}</g>'
        y += h
    return svg(y, out)


def f47_lowrisk_hr():
    """Time-dependent hazard ratio for death, TAVI vs SAVR, pooled low-risk trials (Heuts, EACTS 2026)."""
    vmax, lab_w = 2.2, 250
    span = W - lab_w - 90
    h, b = bars([('Year 0 to 1', 0.61, 'ok'), ('Years 1 to 3', 0.84, 'ok'),
                 ('Years 3 to 5', 1.05, 'b1'), ('Years 5 to 7', 1.64, 'warn')], '', vmax,
                'Death after TAVI vs SAVR, low risk: hazard ratio turns against TAVI after year 5')
    x1 = lab_w + span * 1 / vmax
    b = f'<line x1="{x1}" y1="40" x2="{x1}" y2="{h - 4}" class="f-dash"/>' + b
    b += T(x1, h + 10, 'HR 1.0 (no difference); below 1 favours TAVI', 'f-s')
    b += T(12, h + 34, 'PARTNER 3, Evolut Low Risk and NOTION pooled, 2,644 patients; only years 5 to 7 significant (1.27 to 2.12)', 'f-s', 'start')
    return svg(h + 46, b)


def f47_tavi_pci():
    """TAVI PCI trial (ESC 2026, NEJM): TAVI first vs PCI first."""
    a = bars([('TAVI first', 22.2, 'ok'), ('PCI first', 24.2, 'b1')], '%', 30,
             'TAVI PCI: TAVI first was non-inferior for the 1-year composite')
    b = bars([('TAVI first', 6.6, 'ok'), ('PCI first', 9.7, 'warn')], '%', 30,
             'Major, disabling or life-threatening bleeding')
    return _f47_stack(a, b)


def f47_season_ar():
    """SEASON-AR (TCT 2026, Circulation): TAVI plus medical therapy vs medical therapy, pure AR."""
    a = bars([('TAVI plus medical therapy', 8.3, 'ok'), ('Medical therapy alone', 24.8, 'warn')], '%', 30,
             'SEASON-AR: death, disabling stroke or HF readmission at 1 year cut by TAVI')
    b = bars([('TAVI plus medical therapy', 3.7, 'ok'), ('Medical therapy alone', 21.3, 'warn')], '%', 30,
             'Heart failure readmission (drives the result)')
    c = bars([('TAVI plus medical therapy', 20.2, 'warn'), ('Medical therapy alone', 2.0, 'b1')], '%', 30,
             'The price: new permanent pacemaker at 30 days')
    return _f47_stack(a, b, c)


def f47_tric_subgroups():
    """TRIC-I-HF win ratio by baseline TR grade (TCT 2026 subgroup report), forest plot."""
    rows = [('All patients (360)', 2.42, 1.76, 3.33, 'b1'),
            ('Severe TR', 3.27, 2.04, 5.26, 'ok'),
            ('Massive TR', 2.16, 1.32, 3.93, 'ok'),
            ('Torrential TR (37)', 1.08, 0.45, 2.55, 'warn')]
    lab_w, x0, span, vmax = 230, 230, 400, 6.0
    X = lambda v: x0 + span * v / vmax
    b = T(12, 22, 'TRIC-I-HF: benefit by TR grade; no clear benefit once torrential', 'f-h', 'start')
    y = 50
    for lab, wr, lo, hi, cls in rows:
        b += T(lab_w - 12, y + 5, lab, '', 'end')
        b += line(X(lo), y, X(hi), y, 'f-l')
        b += line(X(lo), y - 6, X(lo), y + 6, 'f-l') + line(X(hi), y - 6, X(hi), y + 6, 'f-l')
        b += f'<rect x="{X(wr) - 7}" y="{y - 7}" width="14" height="14" class="f-{cls}"/>'
        b += T(X(hi) + 10, y + 5, f'{wr} ({lo} to {hi})', 'f-n', 'start')
        y += 36
    b += f'<line x1="{X(1)}" y1="34" x2="{X(1)}" y2="{y - 14}" class="f-dash"/>'
    b += line(x0, y - 8, x0 + span, y - 8, 'f-grid')
    for v in (0, 1, 2, 3, 4, 5, 6):
        b += T(X(v), y + 8, str(v), 'f-s')
    b += T(x0 + span / 2, y + 28, 'Win ratio for repair (above 1 favours repair; 95% CI)', 'f-s')
    return svg(y + 40, b)


def f47_surviv():
    """SURViV (ACC.26): redo surgical MVR vs transcatheter mitral valve-in-valve."""
    a = bars([('Redo surgical MVR', 20.8, 'warn'), ('Mitral valve-in-valve', 5.3, 'ok')], '%', 25,
             'SURViV: death or disabling stroke at 1 year lower with valve-in-valve')
    b = bars([('Redo surgical MVR', 16.0, 'warn'), ('Mitral valve-in-valve', 2.8, 'ok')], '%', 25,
             'Cardiac readmission at 1 year')
    return _f47_stack(a, b)


# ---- figs_F48.py



def f48_periop_os():
    h, b = bars([
        ('CheckMate 816 (nivolumab, neoadjuvant)', 0.72, 'ok'),
        ('KEYNOTE-671 (pembrolizumab)', 0.72, 'ok'),
        ('RATIONALE-315 (tislelizumab)', 0.65, 'ok'),
        ('Neotorch (toripalimab)', 0.66, 'ok'),
        ('CheckMate 77T (nivolumab), interim', 0.85, 'warn'),
        ('AEGEAN (durvalumab), not yet tested', 0.89, 'warn'),
    ], '', 1.0, 'Hazard ratio for death: four trials significant, two not yet', lab_w=300)
    b += line(300 + (W - 300 - 90), 40, 300 + (W - 300 - 90), h - 8, 'f-dash')
    b += T(300 + (W - 300 - 90), h + 8, '1.0 = no difference', 'f-s')
    b += T(12, h + 8, 'Green: significant. Amber: boundary not crossed or not tested.', 'f-s', 'start')
    return svg(h + 20, b)


def f48_sano5():
    h, b = bars([
        ('Overall survival: surveillance', 50, 'b0'),
        ('Overall survival: surgery', 54, 'b1'),
        ('Distant spread: surveillance', 46, 'warn'),
        ('Distant spread: surgery', 29, 'b1'),
    ], '%', 100, 'SANO at 5 years: survival similar, more distant spread on surveillance', lab_w=260)
    return svg(h, b)


def f48_tactic():
    h, b = bars([
        ('Poudrage plus catheter (2 of 60)', 3, 'ok'),
        ('Poudrage alone (19 of 56)', 34, 'warn'),
    ], '%', 50, 'TACTIC: further invasive pleural procedures by 12 weeks', lab_w=270)
    b += T(12, h + 8, 'Co-primary end points (hospital days, breathlessness over 4 weeks) did not differ.', 'f-s', 'start')
    return svg(h + 20, b)


def f48_screening():
    return tiles([
        ('3.3 million', ['invited for a lung', 'health check'], 'b1'),
        ('800,000', ['low-dose CT', 'scans done'], 'b0'),
        ('10,000', ['lung cancers found', 'by screening'], 'ok'),
        ('0.78', ['late-stage incidence', 'rate ratio, Manchester'], 'ok'),
    ], h=100)


def f48_blvr_select():
    b = box(210, 8, 300, 38, 'Severe emphysema, hyperinflated', 'b1', 'f-h')
    b += arrow(360, 46, 360, 64)
    b += box(60, 66, 600, 56, ['Stop: PaCO2 over 55 mm Hg on best treatment · severe pulmonary hypertension',
                               'decompensated heart failure · mainly paraseptal disease or giant bulla'], 'warn')
    b += arrow(360, 122, 360, 140)
    b += box(60, 142, 600, 56, ['Quantitative CT target lobe: 50% or more below -910 HU,',
                                'or 20% or more below -950 HU, with adjacent fissure 80% or more intact'], 'b0')
    b += arrow(360, 198, 360, 216)
    b += box(60, 218, 600, 56, ['Balloon-occlusion test for collateral ventilation:',
                                'every right-sided lobe; left side if fissure under 95% intact'], 'b0')
    b += arrow(250, 274, 190, 296) + arrow(470, 274, 530, 296)
    b += box(40, 298, 300, 56, ['No collateral ventilation:', 'valves; admit at least 3 nights'], 'ok')
    b += box(380, 298, 300, 56, ['Collateral ventilation present:', 'no valves; consider surgery'], 'b1')
    b += arrow(190, 354, 190, 372)
    b += box(40, 374, 300, 56, ['Review at 4 to 6 weeks, 3 to 6 months,', '12 months; CT if no benefit at 3 months'], 'b0')
    return svg(440, b)


# ---- figs_F49.py



def f49_exam_structure():
    b = ''
    b += T(12, 24, 'FRCS (C-Th): JCIE regulations SR4 v8.0 (reviewed August 2025)', 'f-h', 'start')
    # Section 1
    b += box(20, 44, 680, 30, 'Eligibility: 6 years qualified, 3 structured JCIE references (curriculum: ARCP outcome 1 at end of phase 2)', 'b1', 'f-s')
    b += arrow(360, 74, 360, 92)
    b += box(20, 94, 330, 92, ['Section 1: written (Pearson VUE)', 'Paper 1: 120 SBA, 2 h 15 min', 'Paper 2: 120 SBA, 2 h 15 min'], 'b0')
    b += box(370, 94, 330, 92, ['Rules', 'Pass within 2 years of first attempt', 'Max 4 attempts (JSCFE attempts count)', 'Whole exam within 7 years'], 'warn', 'f-s')
    b += arrow(185, 186, 185, 208)
    b += T(195, 202, 'eligible to proceed', 'f-s', 'start')
    b += T(360, 230, 'Section 2: clinical and oral (format since August 2022)', 'f-h')
    # clinical row
    b += box(20, 244, 160, 74, ['Cardiac', 'intermediate case', '45 min, 3 patients'], 'b1', 'f-s')
    b += box(190, 244, 160, 74, ['Thoracic', 'intermediate case', '45 min, 3 patients'], 'b1', 'f-s')
    b += box(370, 244, 160, 74, ['Cardiac instruments', '+ imaging/investigations', '30 min, 3 + 3 x 5 min'], 'b1', 'f-s')
    b += box(540, 244, 160, 74, ['Thoracic instruments', '+ imaging/investigations', '30 min, 3 + 3 x 5 min'], 'b1', 'f-s')
    # oral row
    b += box(20, 330, 220, 64, ['Oral: cardiac critical', 'conditions / ICU / trauma'], 'ok', 'f-s')
    b += box(250, 330, 220, 64, ['Oral: thoracic critical', 'conditions / ICU / trauma'], 'ok', 'f-s')
    b += box(480, 330, 220, 64, ['Oral: sub-specialty', '(cardiac or thoracic, chosen', 'at application)'], 'ok', 'f-s')
    b += T(360, 414, 'Orals listed with "3 x 30 minute sessions"; the regulations do not give each oral a separate time.', 'f-s')
    b += T(360, 432, 'Max 4 attempts at Section 2, no re-entry.', 'f-s')
    return svg(446, b)


def f49_jcie_results():
    h, b = bars([
        ('Section 1, Type 1 (22 of 30)', 73, 'ok'),
        ('Section 1, not in training (19 of 44)', 43, 'warn'),
        ('Section 1, all candidates (43 of 76)', 57, 'b1'),
        ('Section 2, Type 1 (24 of 25)', 96, 'ok'),
        ('Section 2, not in training (19 of 35)', 54, 'warn'),
        ('Section 2, all candidates (44 of 61)', 72, 'b1'),
    ], '%', 100, 'FRCS (C-Th) 2025-26: Type 1 candidates pass far more often', lab_w=300)
    b += T(12, h + 8, 'Two sittings of each section pooled (JCIE report to SCTS, June 2026). Section 1 = eligible to proceed.', 'f-s', 'start')
    return svg(h + 20, b)


def f49_ocebm():
    b = T(12, 24, 'OCEBM 2011, "Does this intervention help?" (treatment benefits)', 'f-h', 'start')
    rows = [
        ('1', 'Systematic review of randomised trials or n-of-1 trials', 'ok'),
        ('2', 'Randomised trial, or observational study with dramatic effect', 'ok'),
        ('3', 'Non-randomised controlled cohort / follow-up study', 'b0'),
        ('4', 'Case series, case-control or historically controlled studies', 'warn'),
        ('5', 'Mechanism-based reasoning', 'track'),
    ]
    y = 40
    for i, (lv, txt, cls) in enumerate(rows):
        indent = i * 26
        b += box(20 + indent, y, 560 - indent, 40, txt, cls, 'f-s')
        b += T(610, y + 26, f'Level {lv}', 'f-n')
        y += 48
    b += T(12, y + 14, 'Grade down for quality, imprecision, indirectness, inconsistency or a very small absolute effect;', 'f-s', 'start')
    b += T(12, y + 31, 'grade up for a large or very large effect. A systematic review generally beats a single study.', 'f-s', 'start')
    return svg(y + 44, b)


def f49_gdpr():
    b = T(12, 24, 'Using patient data lawfully: two keys under UK GDPR (ICO guidance)', 'f-h', 'start')
    b += box(250, 40, 220, 40, 'Personal data about a living person', 'b1', 'f-s')
    b += arrow(360, 80, 190, 108)
    b += arrow(360, 80, 530, 108)
    b += box(20, 110, 340, 118, ['Key 1: Article 6 lawful basis', 'consent, contract, legal obligation,', 'vital interests, public task (public authorities),', 'recognised legitimate interest,', 'legitimate interests'], 'b0', 'f-s')
    b += box(380, 110, 320, 118, ['Key 2 (health data): Article 9 condition', '(h) health or social care: by or under', 'a professional owing secrecy (Sch 1 para 2)', '(i) public health  (j) research, statistics', '(a) explicit consent  (c) vital interests'], 'warn', 'f-s')
    b += arrow(190, 228, 330, 256)
    b += arrow(540, 228, 390, 256)
    b += box(150, 258, 420, 54, ['Lawful only with both, plus the 7 principles', '(minimum necessary, secure, accountable)'], 'ok', 'f-s')
    b += T(360, 332, 'No appropriate policy document is needed for (h), (i) or (j). A DPIA is needed for large-scale processing.', 'f-s')
    return svg(346, b)


# ---- figs_F50.py



def _f50_p(d, cls):
    return f'<path d="{d}" class="{cls}"/>'


def f50_ebstein_carpentier():
    """Four schematic RVs (inflow view): true annulus at top, displaced leaflets, atrialised part shaded."""
    b = ''
    spec = [
        ('A', 40, 'Moderate displacement', ['Anterior leaflet large, mobile', 'Atrialised RV small, contracts', 'Functional RV adequate'], 'ok'),
        ('B', 85, 'Marked displacement', ['Anterior leaflet large, mobile', 'Atrialised RV large, thin', 'Functional RV small'], 'b0'),
        ('C', 120, 'Marked; anterior tethered', ['Anterior leaflet restricted', 'Atrialised RV large, thin', 'Functional RV very small'], 'warn'),
        ('D', 160, 'Tricuspid sac', ['Leaflets stuck to the wall', 'Only infundibulum left', 'Outflow at anteroseptal comm.'], 'warn'),
    ]
    top, bot = 60, 230
    for i, (t, disp, sub, lines, cls) in enumerate(spec):
        x0 = 12 + i * 177
        cx = x0 + 82
        b += T(cx, 22, f'Type {t}', 'f-h') + T(cx, 40, sub, 'f-s')
        # ventricle outline (U shape)
        b += _f50_p(f'M{cx-62} {top} L{cx-62} {bot-40} Q{cx-62} {bot} {cx} {bot} Q{cx+62} {bot} {cx+62} {bot-40} L{cx+62} {top}', 'f-l')
        # atrialised portion shaded
        y = top + disp * 0.9
        b += f'<rect x="{cx-60}" y="{top+2}" width="120" height="{y-top-2}" class="f-track"/>'
        # true annulus dashed
        b += line(cx - 74, top, cx + 74, top, 'f-dash')
        # leaflets
        if t == 'D':
            b += _f50_p(f'M{cx-60} {top+4} L{cx-60} {y} Q{cx} {y+18} {cx+60} {y} L{cx+60} {top+4}', 'f-cut')
        else:
            # septal leaflet (left wall) displaced
            b += _f50_p(f'M{cx-60} {y} L{cx-24} {y+10}', 'f-cut')
            # anterior leaflet from annulus on right wall
            if t == 'C':
                b += _f50_p(f'M{cx+60} {top+6} Q{cx+40} {y-10} {cx+10} {y+6}', 'f-cut')
                b += line(cx + 22, y + 2, cx + 40, y + 28, 'f-l') + line(cx + 10, y + 6, cx + 14, y + 30, 'f-l')
            else:
                b += _f50_p(f'M{cx+60} {top+6} Q{cx+10} {top+40} {cx-18} {y+4}', 'f-cut')
        b += T(cx, top + 20 if disp > 60 else top + 16, 'atrialised', 'f-s')
        b += T(cx, bot - 18 if t != 'D' else bot - 40, 'functional' if t != 'D' else 'infundibulum', 'f-s')
        b += T(cx, bot + 26, lines, 'f-s')
    b += T(14, 316, 'Dashed line: true tricuspid annulus. Grey: atrialised RV. Thick lines: leaflets.', 'f-s', 'start')
    return svg(326, b)


def f50_atrial_switch_survival():
    h, b = bars([('10 years', 91, 'ok'), ('20 years', 86, 'ok'), ('30 years', 76, 'b0'), ('40 years', 65, 'warn')],
                '%', 100, 'Survival after Senning or Mustard falls to about 65% at 40 years (pooled, 4,409 patients)', lab_w=120)
    b += T(12, h + 8, 'Sudden death was 45% of late deaths; Mustard OR 2.9 for late death against Senning (Venkatesh 2019)', 'f-s', 'start')
    return svg(h + 20, b)


def f50_subclavian_flap():
    b = T(180, 22, '1. Divide subclavian, open across coarctation', 'f-h')
    b += T(540, 22, '2. Turn the flap down as a living patch', 'f-h')
    for ox, after in [(0, False), (360, True)]:
        b += _f50_p(f'M{ox+30} 120 Q{ox+130} 90 {ox+200} 112 L{ox+214} 140 L{ox+214} 330', 'f-vessel')
        b += _f50_p(f'M{ox+100} 100 L{ox+92} 50', 'f-vessel')
        if not after:
            b += _f50_p(f'M{ox+190} 108 L{ox+240} 56', 'f-vessel')
        else:
            b += f'<path d="M{ox+196} 104 L{ox+232} 112 L{ox+240} 230 L{ox+222} 250 L{ox+214} 140 Z" class="f-b0"/>'
    b += T(84, 66, 'LCCA', 'f-s', 'end') + T(40, 150, 'arch', 'f-s', 'start')
    b += T(250, 50, 'L subclavian', 'f-s', 'start')
    b += _f50_p('M222 66 L236 80', 'f-cut') + T(250, 82, 'ligated, divided', 'f-s', 'start')
    b += T(250, 98, '(beyond the vertebral)', 'f-s', 'start')
    b += line(232, 70, 232, 250, 'f-dash')
    b += T(244, 180, ['incision across', 'the coarctation'], 'f-s', 'start')
    b += T(214, 350, 'descending aorta', 'f-s')
    b += T(612, 170, ['flap roofs', 'the narrowed', 'segment'], 'f-s', 'start')
    b += T(574, 350, 'no circumferential suture line', 'f-s')
    b += box(10, 366, 700, 46, ['For: no prosthetic, grows, no circumferential line.',
                               'Against: arm claudication and weaker grip; up to 23% recoarctation in neonates; arch not treated'], 'warn', 'f-s')
    return svg(422, b)


def f50_ross_konno():
    b = T(360, 20, 'Ross-Konno: aortic root opened, seen from above (schematic)', 'f-h')
    cx, cy = 250, 210
    b += f'<circle cx="{cx}" cy="{cy}" r="90" class="f-b1"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="46" class="f-track"/>'
    b += T(cx, cy + 5, 'LVOT', 'f-s')
    b += f'<circle cx="{cx-70}" cy="{cy-56}" r="10" class="f-b0"/>' + T(cx - 86, cy - 62, 'Left coronary button', 'f-s', 'end')
    b += f'<circle cx="{cx+26}" cy="{cy-86}" r="10" class="f-b0"/>' + T(cx + 48, cy - 62, 'Right coronary button', 'f-s', 'start')
    b += f'<path d="M{cx-6} {cy-90} L{cx-30} {cy-150} L{cx+12} {cy-150} Z" class="f-warn"/>'
    b += _f50_p(f'M{cx-4} {cy-46} L{cx-6} {cy-90}', 'f-cut')
    b += arrow(cx - 120, cy - 150, cx - 32, cy - 136) + T(cx - 124, cy - 160, ['Konno incision into', 'the septum, left of the', 'right coronary button'], 'f-s', 'end')
    b += f'<circle cx="{cx+46}" cy="{cy-150}" r="7" class="f-b1"/>' + T(cx + 58, cy - 154, 'medial papillary muscle', 'f-s', 'start')
    b += T(cx + 58, cy - 138, '(keep the incision to its left)', 'f-s', 'start')
    b += T(cx, cy + 112, 'Non-coronary sinus rim kept (3 to 4 mm)', 'f-s')
    ax = 590
    b += T(ax, 104, 'Pulmonary autograft', 'f-h')
    b += f'<rect x="{ax-60}" y="118" width="120" height="100" rx="20" class="f-b0"/>'
    b += T(ax, 172, 'valve', 'f-s')
    b += f'<path d="M{ax-20} 218 L{ax-36} 270 L{ax+20} 270 L{ax+12} 218 Z" class="f-warn"/>'
    b += T(ax, 292, ['infundibular muscle skirt', 'fills the septal gap'], 'f-s')
    b += arrow(ax - 40, 250, cx + 16, cy - 128, True)
    b += box(10, 336, 700, 44, ['Protect the first septal perforator of the LAD at harvest and at the homograft line;',
                               'patch a coexisting VSD rather than using the skirt'], 'b1', 'f-s')
    return svg(390, b)


def f50_kawashima():
    b = T(360, 20, 'Kawashima: bidirectional Glenn with azygos continuation of an interrupted IVC', 'f-h')
    b += f'<rect x="120" y="90" width="320" height="28" rx="12" class="f-b0"/>'
    b += T(380, 109, 'pulmonary arteries', 'f-s')
    b += _f50_p('M260 40 L260 90', 'f-vessel') + T(272, 52, 'SVC', 'f-s', 'start')
    b += _f50_p('M260 66 Q190 66 190 140 L190 330', 'f-vessel')
    b += T(168, 220, ['azygos', 'continuation', '(lower body', 'blood)'], 'f-s', 'end')
    b += line(190, 334, 190, 362, 'f-dash') + T(178, 356, 'interrupted IVC', 'f-s', 'end')
    b += box(270, 170, 170, 64, ['common atrium', '(left isomerism)'], 'b1', 'f-s')
    b += _f50_p('M355 320 L355 234', 'f-vessel')
    b += f'<ellipse cx="355" cy="332" rx="44" ry="14" class="f-warn"/>'
    b += T(355, 366, 'hepatic veins: the only return still entering the atrium', 'f-s')
    b += arrow(440, 104, 490, 104) + arrow(120, 104, 70, 104)
    b += box(500, 130, 210, 92, ['No hepatic blood to lungs:', 'pulmonary AV malformations', 'in 21 to 75%; saturation falls'], 'warn', 'f-s')
    b += box(500, 240, 210, 92, ['Treatment: route the hepatic', 'veins to the PAs (Fontan', 'completion); slow recovery'], 'ok', 'f-s')
    return svg(380, b)


def f50_cctga_repairs():
    b = box(200, 8, 320, 44, ['ccTGA needing repair', '(symptoms, failing RV or worsening TR)'], 'b1', 'f-s')
    b += arrow(300, 52, 150, 82) + arrow(420, 52, 570, 82)
    b += box(10, 84, 290, 50, ['LV conditioned', '(large VSD or pulmonary stenosis)'], 'b0', 'f-s')
    b += box(420, 84, 290, 50, ['LV deconditioned', '(intact septum, no LVOTO)'], 'b0', 'f-s')
    b += arrow(80, 134, 80, 164) + arrow(230, 134, 230, 164)
    b += box(10, 166, 140, 74, ['No fixed LVOTO:', 'atrial switch', '+ arterial switch'], 'ok', 'f-s')
    b += box(160, 166, 140, 74, ['Fixed LVOTO,', 'routable VSD:', 'atrial switch + Rastelli'], 'ok', 'f-s')
    b += arrow(565, 134, 565, 164)
    b += box(420, 166, 290, 74, ['PA band to retrain', 'ready: LV/RV pressure over 0.9,', 'EF over 50 to 55%, LVEDP under 12'], 'warn', 'f-s')
    b += arrow(500, 240, 330, 276) + arrow(640, 240, 640, 270)
    b += box(150, 278, 260, 50, ['Retrained: double switch', '(better when young)'], 'ok', 'f-s')
    b += box(530, 272, 180, 56, ['Not retrainable: destination', 'band, physiological repair', 'or transplant'], 'b1', 'f-s')
    b += box(10, 344, 700, 46, ['Small RA or RV: hemi-Mustard + Glenn. VSD not routable or remote: Fontan.',
                               'Any route: high risk of heart block (anterior AV node)'], 'b1', 'f-s')
    return svg(400, b)


# ---- figs_D1.py
"""Drawing pass D1: coronary anatomy, grafting, cannulation, cardioplegia and venting (23 November 2026)."""



def _d1_d1_v(d, w=7, extra=''):
    """Vessel path with a set stroke width."""
    return f'<path d="{d}" class="f-vessel" style="stroke-width:{w}"{extra}/>'


def _d1_d1_num(x, y, n, cls='b1'):
    return (f'<circle cx="{x}" cy="{y}" r="11" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def _d1_d1_lead(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, 'f-dash')


# ------------------------------------------------------------------ anatomy (c19)

def d1_coronary_tree():
    """Coronary arteries, anterior view, schematic (TSRA ch. 45)."""
    b = T(12, 20, 'Anterior view, schematic', 'f-h', 'start')
    b += T(14, 40, "Patient's right", 'f-s', 'start') + T(706, 40, "Patient's left", 'f-s', 'end')
    # heart outline
    b += '<path d="M220 128 C170 170 170 270 230 320 C300 372 380 392 430 384 C520 340 590 260 560 170 C540 128 470 112 420 118 C360 112 280 108 220 128 Z" class="f-b0"/>'
    # atrioventricular groove (dashed) and anterior interventricular groove
    b += '<path d="M232 138 C220 200 226 262 262 316" class="f-grid" fill="none"/>'
    b += '<path d="M470 140 C520 160 560 200 560 230" class="f-grid" fill="none"/>'
    # great vessels
    b += '<path d="M330 128 L330 40" class="f-vessel" style="stroke-width:46;opacity:.25"/>'
    b += T(330, 62, 'Aorta', 'f-s')
    b += '<rect x="372" y="60" width="54" height="66" rx="14" class="f-b1"/>' + T(399, 96, 'PA', 'f-s')
    b += '<path d="M450 118 C470 96 504 100 506 122 C508 140 486 148 466 142 Z" class="f-b1"/>'
    b += T(520, 104, 'Left atrial appendage', 'f-s', 'start')
    b += _d1_d1_lead(518, 108, 498, 116)
    # left main between PA and LAA
    b += _d1_d1_v('M342 128 C380 134 420 136 446 146', 8)
    # LAD down the anterior interventricular groove
    b += _d1_d1_v('M446 146 C440 210 430 300 418 380', 7)
    # septal perforators (to the left of LAD, short) and diagonals (to the right)
    for y in (196, 246, 296):
        x = 446 - (y - 146) * 0.09
        b += _d1_d1_v(f'M{x:.0f} {y} L{x - 26:.0f} {y + 10}', 3)
    for y, l in ((186, 64), (250, 60)):
        x = 446 - (y - 146) * 0.09
        b += _d1_d1_v(f'M{x:.0f} {y} C{x + 30:.0f} {y + 10} {x + l - 10:.0f} {y + 28} {x + l:.0f} {y + 44}', 4)
    # circumflex in the left AV groove, then out of view
    b += _d1_d1_v('M446 146 C490 152 532 176 552 214', 6)
    b += '<path d="M552 214 C562 236 566 256 566 270" class="f-dash"/>'
    # obtuse marginals
    b += _d1_d1_v('M520 168 C530 200 532 236 528 266', 4)
    b += _d1_d1_v('M548 200 C556 226 556 256 552 284', 4)
    # RCA in the right AV groove
    b += _d1_d1_v('M318 132 C270 132 236 150 230 200 C226 250 236 290 262 316', 7)
    b += '<path d="M262 316 C290 346 330 366 360 372" class="f-dash"/>'
    # RCA branches: conal, SA nodal, acute marginal
    b += _d1_d1_v('M296 134 C300 150 316 160 336 166', 3)
    b += _d1_d1_v('M262 138 C252 118 248 100 254 82', 3)
    b += _d1_d1_v('M236 270 C270 290 300 300 330 300', 4)
    # labels, left side
    b += T(150, 76, ['Sinus (SA) node', 'artery'], 'f-s', 'end') + _d1_d1_lead(154, 80, 252, 92)
    b += T(150, 130, ['Conal branch'], 'f-s', 'end') + _d1_d1_lead(154, 126, 300, 150)
    b += T(150, 196, ['Right coronary in the', 'right AV groove'], 'f-h', 'end') + _d1_d1_lead(154, 200, 226, 206)
    b += T(150, 286, ['Acute marginal', '(distal PDA territory', 'in 10 to 20%)'], 'f-s', 'end') + _d1_d1_lead(154, 290, 270, 290)
    b += T(150, 360, ['To the crux (posterior):', 'see dominance'], 'f-s', 'end') + _d1_d1_lead(154, 362, 300, 356)
    # labels, right side
    b += T(706, 150, ['Left main: between PA', 'and appendage'], 'f-h', 'end') + _d1_d1_lead(600, 150, 410, 136)
    b += T(706, 196, ['Circumflex in the', 'left AV groove'], 'f-h', 'end') + _d1_d1_lead(604, 196, 548, 208)
    b += T(706, 290, ['Obtuse marginals:', 'lateral and inferior wall'], 'f-s', 'end') + _d1_d1_lead(590, 292, 552, 270)
    b += T(706, 350, ['LAD in the anterior', 'interventricular groove'], 'f-h', 'end') + _d1_d1_lead(580, 352, 424, 350)
    b += T(470, 410, 'Diagonals: LV anterior wall', 'f-s', 'start') + _d1_d1_lead(510, 398, 500, 300)
    b += T(360, 410, ['Septal perforators:', 'anterior two thirds of septum'], 'f-s', 'end') + _d1_d1_lead(320, 396, 410, 300)
    return svg(448, b)


def _d1_d1_crux(ox, right_dom):
    """Diaphragmatic surface: AV groove (horizontal) and posterior interventricular groove (vertical)."""
    cx = ox + 170
    b = f'<path d="M{ox + 10} 80 C{ox + 60} 60 {ox + 280} 60 {ox + 330} 80 L{ox + 320} 250 C{ox + 260} 300 {ox + 80} 300 {ox + 20} 250 Z" class="f-b0"/>'
    b += line(ox + 14, 96, ox + 326, 96, 'f-grid') + line(cx, 96, cx, 280, 'f-grid')
    b += T(ox + 18, 90, 'AV groove', 'f-s', 'start')
    b += T(cx + 6, 290, 'posterior IV groove', 'f-s', 'start')
    b += f'<circle cx="{cx}" cy="96" r="5" class="f-ah"/>'
    b += T(cx, 84, 'Crux', 'f-h')
    if right_dom:
        b += _d1_d1_v(f'M{ox + 14} 96 L{cx} 96', 7)                     # RCA to crux
        b += _d1_d1_v(f'M{cx} 96 L{cx} 260', 6)                        # PDA
        b += _d1_d1_v(f'M{cx} 96 L{cx + 90} 96 C{cx + 110} 100 {cx + 120} 120 {cx + 124} 150', 5)  # posterolateral
        b += _d1_d1_v(f'M{cx} 96 L{cx - 8} 70', 3)                     # AV nodal
        b += _d1_d1_v(f'M{ox + 326} 96 L{cx + 112} 96', 5, ' stroke-dasharray="2 0"')  # Cx ends short
        b += T(ox + 30, 120, 'RCA', 'f-h', 'start')
        b += T(ox + 318, 120, 'Cx', 'f-h', 'end')
        b += T(cx - 10, 200, ['PDA', '(from RCA)'], 'f-s', 'end')
        b += T(cx + 132, 170, ['Postero-', 'lateral'], 'f-s', 'start')
    else:
        b += _d1_d1_v(f'M{ox + 326} 96 L{cx} 96', 7)                    # Cx to crux
        b += _d1_d1_v(f'M{cx} 96 L{cx} 260', 6)
        b += _d1_d1_v(f'M{cx} 96 L{cx + 8} 70', 3)
        b += _d1_d1_v(f'M{ox + 14} 96 L{cx - 90} 96', 5)                 # RCA ends short
        b += T(ox + 30, 120, 'RCA', 'f-h', 'start')
        b += T(ox + 318, 120, 'Cx', 'f-h', 'end')
        b += T(cx - 10, 200, ['PDA', '(from Cx)'], 'f-s', 'end')
    b += T(cx + 40, 66, 'AV nodal branch', 'f-s', 'start')
    return b


def d1_dominance():
    """Right against left dominance at the crux (TSRA ch. 45)."""
    b = T(185, 22, 'Right dominant: 70 to 85%', 'f-h') + T(545, 22, 'Left dominant: 10 to 15%', 'f-h')
    b += T(185, 40, 'Inferior (diaphragmatic) surface, schematic', 'f-s') + T(545, 40, 'Inferior (diaphragmatic) surface, schematic', 'f-s')
    b += line(360, 10, 360, 300, 'f-dash')
    b += _d1_d1_crux(15, True) + _d1_d1_crux(375, False)
    b += box(10, 316, 345, 62, ['At the crux the RCA gives the AV nodal', 'branch, then divides into the PDA and', 'the posterolateral artery'], 'b1', 'f-s')
    b += box(365, 316, 345, 62, ['The circumflex gives the PDA and', 'the AV nodal branch'], 'b1', 'f-s')
    b += T(360, 400, 'The PDA runs in the posterior interventricular groove. Proportions as quoted in TSRA ch. 45.', 'f-s')
    return svg(412, b)


def d1_papillary_supply():
    """Papillary muscle blood supply and which one ruptures (TSRA ch. 45 and 51)."""
    cx, cy = 210, 190
    b = T(210, 22, 'LV in short axis, schematic', 'f-h')
    b += T(210, 50, 'anterior', 'f-s') + T(210, 340, 'inferior', 'f-s')
    b += T(84, 194, 'septum', 'f-s', 'end') + T(336, 194, 'lateral', 'f-s', 'start')
    b += f'<circle cx="{cx}" cy="{cy}" r="120" class="f-b0"/><circle cx="{cx}" cy="{cy}" r="84" class="f-lumen"/>'
    # papillary muscles inside the cavity
    b += f'<ellipse cx="{cx + 52}" cy="{cy + 46}" rx="22" ry="16" class="f-b1"/>'
    b += f'<ellipse cx="{cx - 52}" cy="{cy + 50}" rx="22" ry="16" class="f-warn"/>'
    b += T(cx + 52, cy + 51, 'AL', 'f-n') + T(cx - 52, cy + 55, 'PM', 'f-n')
    # supplying arteries on the epicardium
    b += _d1_d1_v(f'M{cx + 40} {cy - 128} C{cx + 86} {cy - 112} {cx + 122} {cy - 56} {cx + 128} {cy - 10}', 6)
    b += T(cx + 100, cy - 128, 'LAD branches', 'f-s', 'start')
    b += _d1_d1_v(f'M{cx + 128} {cy + 10} C{cx + 124} {cy + 66} {cx + 96} {cy + 104} {cx + 56} {cy + 120}', 6)
    b += T(cx + 118, cy + 126, 'Circumflex', 'f-s', 'start')
    b += arrow(cx + 118, cy - 54, cx + 70, cy + 32) + arrow(cx + 112, cy + 90, cx + 70, cy + 60)
    b += _d1_d1_v(f'M{cx - 20} {cy + 128} C{cx - 60} {cy + 124} {cx - 92} {cy + 104} {cx - 110} {cy + 74}', 6)
    b += T(cx - 110, cy + 130, ['RCA (PDA)', 'or circumflex'], 'f-s', 'end')
    b += arrow(cx - 70, cy + 116, cx - 58, cy + 70)
    # right panel
    x = 430
    b += box(x, 40, 280, 96, ['Anterolateral (AL)', 'Dual supply: LAD and circumflex', '25% of papillary ruptures'], 'b1', 'f-s')
    b += box(x, 150, 280, 112, ['Posteromedial (PM)', 'Single supply: terminal branches of', 'the RCA or circumflex (the PDA)',
                                '75% of papillary ruptures'], 'warn', 'f-s')
    b += box(x, 276, 280, 76, ['Rupture: median 13 hours; pulmonary', 'oedema and shock. Mitral replacement', 'with chordal sparing; repair rarely'], 'b0', 'f-s')
    return svg(368, b)


# ------------------------------------------------------------------ bypass (c14)

def d1_cardioplegia_routes():
    """Antegrade root, direct ostial and retrograde coronary sinus delivery (TSRA ch. 45, 49; EACTS 2024)."""
    b = T(12, 20, 'Where each route enters (schematic)', 'f-h', 'start')
    # ascending aorta and root
    b += '<path d="M200 36 L200 170" class="f-vessel" style="stroke-width:44;opacity:.25"/>'
    b += '<ellipse cx="200" cy="182" rx="34" ry="18" class="f-b1"/>' + T(200, 186, 'Root', 'f-s')
    # cross-clamp
    b += '<rect x="150" y="66" width="100" height="10" rx="4" class="f-warn"/>' + T(258, 76, 'Cross-clamp', 'f-h', 'start')
    # root cannula with vent side port
    b += '<path d="M222 118 L290 100" class="f-l" style="stroke-width:4"/>' + f'<circle cx="222" cy="118" r="4" class="f-ah"/>'
    b += T(312, 124, ['Root cannula,', 'below the clamp,', 'on the fat fold;', 'side port vents'], 'f-s')
    b += arrow(200, 100, 200, 150) + T(188, 128, 'A', 'f-h', 'end')
    # heart
    b += '<path d="M120 200 C80 250 100 340 180 368 C250 386 330 350 340 280 C346 230 300 196 250 198 C200 196 160 190 120 200 Z" class="f-b0"/>'
    # coronaries from the root
    b += _d1_d1_v('M172 186 C140 200 118 240 120 290', 6) + T(104, 252, 'RCA', 'f-s', 'end')
    b += _d1_d1_v('M228 188 C262 200 290 230 300 270', 6) + T(312, 236, 'Left main', 'f-s', 'start')
    # ostial cannula marks
    b += f'<circle cx="172" cy="186" r="6" class="f-ok"/><circle cx="228" cy="188" r="6" class="f-ok"/>'
    b += T(200, 218, 'B', 'f-h')
    # right atrium and coronary sinus
    b += '<ellipse cx="96" cy="318" rx="40" ry="30" class="f-b1"/>' + T(70, 362, 'Right atrium', 'f-s')
    b += '<path d="M126 330 C170 352 230 352 290 326" class="f-l" style="stroke-width:5;opacity:.5"/>'
    b += T(250, 392, 'Coronary sinus (posterior AV groove)', 'f-s')
    b += '<path d="M40 300 L132 334" class="f-l" style="stroke-width:3"/>'
    b += '<ellipse cx="140" cy="337" rx="9" ry="6" class="f-warn"/>'
    b += T(36, 292, 'C', 'f-h', 'end')
    b += arrow(250, 332, 160, 338)
    # right-hand boxes
    x = 380
    b += box(x, 30, 330, 104, ['A  Antegrade, aortic root: standard', 'Root 60 to 100 mmHg; arrest in 30 to 60 s',
                               'Fails with aortic regurgitation; poor', 'distribution beyond tight LM or RCA lesions'], 'b1', 'f-s')
    b += box(x, 144, 330, 70, ['B  Direct into the ostia: root open, aortic', 'regurgitation; monitor pressure.',
                               'Risk: ostial injury'], 'ok', 'f-s')
    b += box(x, 224, 330, 122, ['C  Retrograde, coronary sinus: AR, severe', 'proximal disease, flushes air and debris',
                                'Flow 200 to 400 mL/min, CS 30 to 50 mmHg', 'Arrest slower (2 to 4 min); RV less well',
                                'protected; useless with a persistent left SVC'], 'warn', 'f-s')
    b += box(10, 410, 700, 44, ['Combined antegrade plus retrograde: long clamp, severe disease with poor collaterals, AR.',
                                'Cold doses repeated every 20 to 30 min.'], 'b0', 'f-s')
    return svg(464, b)


def d1_arterial_cannulation():
    """Arterial cannulation sites and the ascending aortic technique (TSRA ch. 49; EACTS 2024)."""
    b = T(12, 20, 'Arterial inflow sites (schematic)', 'f-h', 'start')
    # aorta: ascending, arch, descending, iliac/femoral
    b += _d1_d1_v('M150 300 L150 150 C150 70 300 70 300 150 L300 330', 22)
    b += _d1_d1_v('M300 330 L262 384 M300 330 L338 384', 12)
    # innominate to right subclavian / axillary
    b += _d1_d1_v('M180 92 L150 50 L40 50', 10)
    b += _d1_d1_v('M226 76 L226 34', 8) + _d1_d1_v('M262 82 L262 38', 8)
    b += T(232, 30, 'Left carotid, subclavian', 'f-s', 'start')
    b += T(40, 80, 'Right axillary', 'f-s', 'start')
    b += T(120, 380, 'Heart', 'f-s')
    b += '<path d="M100 300 C90 340 140 372 190 360 C210 340 200 304 150 300 Z" class="f-b0"/>'
    # numbered sites
    b += _d1_d1_num(150, 170, 1, 'ok') + _d1_d1_num(70, 50, 2) + _d1_d1_num(262, 384, 3) + _d1_d1_num(180, 92, 4, 'b0')
    b += T(124, 174, ['distal', 'ascending'], 'f-s', 'end')
    # detail inset: two purse-strings, bevel toward the arch
    ix, iy = 360, 40
    b += f'<rect x="{ix}" y="{iy}" width="350" height="150" rx="10" class="f-b0"/>'
    b += T(ix + 12, iy + 20, 'Site 1 in detail', 'f-h', 'start')
    b += f'<path d="M{ix + 30} {iy + 120} L{ix + 320} {iy + 120}" class="f-vessel" style="stroke-width:40;opacity:.25"/>'
    b += f'<ellipse cx="{ix + 150}" cy="{iy + 112}" rx="34" ry="12" class="f-dash"/>'
    b += f'<ellipse cx="{ix + 150}" cy="{iy + 112}" rx="22" ry="7" class="f-dash"/>'
    b += f'<path d="M{ix + 120} {iy + 50} L{ix + 150} {iy + 112} L{ix + 196} {iy + 124}" class="f-l" style="stroke-width:5"/>'
    b += arrow(ix + 200, iy + 124, ix + 270, iy + 124)
    b += T(ix + 316, iy + 112, 'to arch', 'f-s', 'end')
    b += T(ix + 30, iy + 52, ['Two purse-', 'strings'], 'f-s', 'start')
    b += T(ix + 210, iy + 52, ['Bevel toward the arch;', 'epiaortic scan for a soft,', 'atheroma-free site'], 'f-s', 'start')
    # legend boxes
    rows = [(1, 'ok', 'Distal ascending aorta: preferred', 'Systolic under 100 mmHg while cannulating'),
            (2, 'b1', 'Axillary (8 mm side graft)', 'Dissection, arch: antegrade flow; right radial line'),
            (3, 'b1', 'Femoral', 'Arrest, dissection, bleeding, minimal access, redo'),
            (4, 'b0', 'Less common', 'Innominate, iliac, LV apex')]
    for i, (n, c, h, s) in enumerate(rows):
        y = 210 + i * 42
        b += _d1_d1_num(376, y + 10, n, c) + T(396, y + 14, h, 'f-h', 'start') + T(396, y + 31, s, 'f-s', 'start')
    b += box(10, 400, 700, 62, ['Iatrogenic dissection (about 0.1%): blue adventitia, rising line pressure, falling venous return.',
                                'Stop bypass, move the cannula to a peripheral artery or clean aorta in the true lumen, cool, repair.',
                                'Survival about 85% if seen in theatre, about 50% if found afterwards.'], 'warn', 'f-s')
    return svg(472, b)


def _d1_d1_atrium(cx):
    """SVC, right atrium and IVC, vertical, centred on cx."""
    b = f'<rect x="{cx - 16}" y="30" width="32" height="90" rx="10" class="f-b0"/>'
    b += f'<ellipse cx="{cx}" cy="160" rx="48" ry="44" class="f-b1"/>'
    b += f'<rect x="{cx - 18}" y="200" width="36" height="130" rx="10" class="f-b0"/>'
    b += T(cx + 22, 50, 'SVC', 'f-s', 'start') + T(cx + 52, 150, 'RA', 'f-s', 'start') + T(cx + 24, 300, 'IVC', 'f-s', 'start')
    return b


def d1_venous_cannulation():
    """Venous cannulation options (TSRA ch. 49; EACTS 2024)."""
    b = ''
    xs = (110, 360, 610)
    heads = ['Bicaval', 'Two- or three-stage', 'Femoral venous']
    for cx, h in zip(xs, heads):
        b += T(cx, 20, h, 'f-h') + _d1_d1_atrium(cx)
    # bicaval: two single-stage cannulae, snares
    cx = xs[0]
    b += f'<path d="M{cx - 70} 150 C{cx - 40} 150 {cx - 6} 140 {cx - 4} 80" class="f-l" style="stroke-width:6"/>'
    b += f'<path d="M{cx - 70} 176 C{cx - 40} 178 {cx - 6} 190 {cx - 4} 260" class="f-l" style="stroke-width:6"/>'
    b += f'<rect x="{cx - 22}" y="96" width="44" height="7" rx="3" class="f-warn"/><rect x="{cx - 24}" y="236" width="48" height="7" rx="3" class="f-warn"/>'
    b += T(cx - 26, 92, 'snare', 'f-s', 'end') + T(cx - 28, 252, 'snare', 'f-s', 'end')
    # two-stage: one cannula, holes in RA, tip in IVC
    cx = xs[1]
    b += f'<path d="M{cx - 80} 110 C{cx - 30} 120 {cx} 140 {cx} 290" class="f-l" style="stroke-width:7"/>'
    for y in (150, 162, 174):
        b += f'<circle cx="{cx}" cy="{y}" r="3" class="f-lumen"/>'
    for y in (276, 286):
        b += f'<circle cx="{cx}" cy="{y}" r="3" class="f-lumen"/>'
    b += T(cx - 56, 166, ['holes', 'in RA'], 'f-s', 'end') + _d1_d1_lead(cx - 52, 162, cx - 4, 162)
    b += T(cx - 26, 284, ['tip in', 'IVC'], 'f-s', 'end')
    # femoral: long cannula up the IVC
    cx = xs[2]
    b += f'<path d="M{cx} 344 L{cx} 160" class="f-l" style="stroke-width:6"/>'
    b += T(cx - 26, 344, 'from groin', 'f-s', 'end')
    b += box(cx - 100, 360, 200, 56, ['Vacuum or pump assist:', 'long, narrow cannula'], 'b0', 'f-s')
    # notes under the first two
    b += box(10, 360, 200, 56, ['Two single-stage cannulae;', 'snares can obstruct a cava'], 'b0', 'f-s')
    b += box(260, 360, 200, 56, ['One cannula: proximal', 'opening RA, distal IVC'], 'b0', 'f-s')
    b += box(10, 428, 700, 62, ['Femoral: redo, emergency bypass, minimal access. Drainage is passive: venous pressure, table height,',
                                'cannula resistance. Complications: poor drainage, atrial arrhythmia, atrial or caval tear, air',
                                'entrainment, decannulation, caval obstruction from snares or misplaced purse-strings.'], 'warn', 'f-s')
    return svg(500, b)


def d1_venting():
    """Where blood reaches a distended left ventricle, and where to vent it (TSRA ch. 49)."""
    b = T(12, 16, 'Blood reaching the arrested left heart (dashed) and vent sites (V)', 'f-h', 'start')
    nodes = {'RA': (20, 60), 'RV': (20, 170), 'PA': (190, 170), 'Lungs': (360, 170), 'PV': (530, 170),
             'LA': (530, 60), 'LV': (360, 60), 'Ao': (190, 60)}
    labels = {'RA': 'Right atrium', 'RV': 'Right ventricle', 'PA': 'Pulmonary artery', 'Lungs': 'Lungs',
              'PV': 'Pulmonary veins', 'LA': 'Left atrium', 'LV': 'Left ventricle', 'Ao': 'Aortic root'}
    for k, (x, y) in nodes.items():
        cls = 'warn' if k == 'LV' else ('b1' if k in ('LA', 'PV', 'Ao') else 'b0')
        b += box(x, y, 150, 50, labels[k], cls, 'f-h' if k == 'LV' else '')
    # normal path (right heart residual)
    b += arrow(95, 110, 95, 168, True) + arrow(170, 195, 188, 195, True) + arrow(340, 195, 358, 195, True)
    b += arrow(510, 195, 528, 195) + arrow(605, 168, 605, 112) + arrow(528, 85, 512, 85)
    b += T(102, 128, ['incomplete', 'right heart', 'drainage'], 'f-s', 'start')
    # AR, PFO, PDA
    b += arrow(340, 85, 358, 85, True) + T(349, 106, 'AR', 'f-s')
    b += '<path d="M60 60 C60 34 640 34 640 58" class="f-dash" marker-end="url(#ah)"/>' + T(350, 32, 'patent foramen ovale', 'f-s')
    b += arrow(265, 110, 265, 168, True) + T(272, 144, 'PDA', 'f-s', 'start')
    # bronchial/collaterals into pulmonary veins
    b += arrow(605, 270, 605, 222, True) + T(605, 286, ['bronchial arteries and', 'aortopulmonary collaterals'], 'f-s')
    b += T(435, 250, ['Thebesian veins drain', 'into every chamber'], 'f-s')
    # vent badges
    for (x, y) in ((190, 60), (530, 170), (190, 170), (530, 60), (360, 60)):
        b += _d1_d1_num(x + 140, y + 4, 'V', 'ok')
    b += box(10, 318, 700, 80, ['Vent sites: aortic root (side port of the cardioplegia cannula) · right superior pulmonary vein ·',
                                'main pulmonary artery (no valves in the pulmonary circulation) · left atrium or left ventricle directly.',
                                'A distended LV is not perfused by cardioplegia and becomes ischaemic; venting also helps',
                                'rewarming and de-airing.'], 'ok', 'f-s')
    return svg(408, b)


def d1_plsvc():
    """Persistent left SVC: anatomy and what to do (TSRA ch. 49)."""
    b = T(170, 20, 'Persistent left SVC (about 0.5%)', 'f-h')
    # anatomy: right SVC, innominate bridge, left SVC to coronary sinus
    b += _d1_d1_v('M110 50 L110 200', 14) + T(96, 60, 'Right SVC', 'f-s', 'end')
    b += _d1_d1_v('M250 50 L250 250 C250 290 200 300 150 290', 12) + T(264, 60, 'Left SVC', 'f-s', 'start')
    b += _d1_d1_v('M250 90 L110 110', 6, ' stroke-dasharray="6 4"') + T(180, 80, 'innominate vein', 'f-s')
    b += '<ellipse cx="120" cy="250" rx="54" ry="42" class="f-b1"/>' + T(100, 254, 'RA', 'f-s')
    b += T(250, 318, 'into an enlarged coronary sinus', 'f-s')
    b += T(20, 340, 'Echo clue: small innominate vein, large coronary sinus', 'f-s', 'start')
    # decision
    x = 360
    b += box(x, 30, 350, 56, ['Retrograde cardioplegia will not work;', 'bicaval drainage may be inadequate'], 'warn', 'f-s')
    b += arrow(x + 175, 86, x + 175, 104)
    b += box(x, 106, 350, 40, 'Is the innominate (bridging) vein adequate?', 'b1', 'f-h')
    b += arrow(x + 90, 146, x + 90, 168) + arrow(x + 260, 146, x + 260, 168)
    b += box(x, 170, 170, 76, ['Adequate (30%)', 'Occlude (snare) the', 'left SVC on bypass'], 'ok', 'f-s')
    b += box(x + 180, 170, 170, 76, ['Absent (40%) or', 'small (33%): cannulate', 'it, or via the sinus'], 'b0', 'f-s')
    b += box(x, 260, 350, 56, ['No right SVC (about 20% of these):', 'the left SVC cannot be occluded'], 'warn', 'f-s')
    return svg(352, b)


def d1_proximal_strategies():
    """Aortic handling for proximal anastomoses and stroke (network meta-analysis cited by Bojalian 2021)."""
    b = ''
    specs = [('Partial (side) clamp', 36), ('Heartstring-type device', 55), ('Anaortic: no aortic touch', 78)]
    for i, (h, pct) in enumerate(specs):
        x = 10 + i * 236
        cx = x + 113
        b += f'<rect x="{x}" y="10" width="226" height="190" rx="10" class="f-b0"/>'
        b += T(cx, 32, h, 'f-h')
        b += f'<path d="M{cx} 190 L{cx} 60" class="f-vessel" style="stroke-width:40;opacity:.25"/>'
        if i == 0:
            b += f'<path d="M{cx + 6} 90 C{cx - 10} 110 {cx - 10} 140 {cx + 6} 160" class="f-l" style="stroke-width:4"/>'
            b += f'<rect x="{cx + 2}" y="86" width="60" height="8" rx="3" class="f-warn"/><rect x="{cx + 2}" y="156" width="60" height="8" rx="3" class="f-warn"/>'
            b += f'<circle cx="{cx + 12}" cy="125" r="6" class="f-ok"/>' + _d1_d1_v(f'M{cx + 12} 125 C{cx + 50} 125 {cx + 70} 150 {cx + 90} 180', 5)
            b += T(cx - 22, 125, ['aorta', 'clamped'], 'f-s', 'end')
        elif i == 1:
            b += f'<circle cx="{cx + 12}" cy="120" r="9" class="f-ok"/>' + _d1_d1_v(f'M{cx + 12} 120 C{cx + 50} 120 {cx + 70} 150 {cx + 90} 180', 5)
            b += T(cx - 22, 116, ['seal, no', 'clamp'], 'f-s', 'end')
        else:
            b += _d1_d1_v(f'M{cx - 80} 60 C{cx - 60} 110 {cx - 40} 150 {cx - 30} 186', 5)
            b += _d1_d1_v(f'M{cx + 80} 60 C{cx + 60} 110 {cx + 40} 150 {cx + 30} 186', 5)
            b += T(cx, 120, ['in situ', 'mammaries'], 'f-s')
    h, bb = bars([('Anaortic off-pump', 78, 'ok'), ('Heartstring-type proximal device', 55, 'b1'), ('Partial clamp', 36, 'b0')],
                 '%', 100, 'Reduction in perioperative stroke (network meta-analysis as cited)', 260)
    b += f'<g transform="translate(0 210)">{bb}</g>'
    return svg(210 + h, b)


# ------------------------------------------------------------------ coronary surgery (c5)

def _d1_d1_heart_targets(ox, oy):
    """Small anterior heart with aorta, for graft configuration panels."""
    b = f'<path d="M{ox + 30} {oy + 120} C{ox + 10} {oy + 190} {ox + 70} {oy + 250} {ox + 130} {oy + 260} C{ox + 190} {oy + 240} {ox + 220} {oy + 180} {ox + 200} {oy + 120} C{ox + 160} {oy + 104} {ox + 70} {oy + 104} {ox + 30} {oy + 120} Z" class="f-b0"/>'
    b += f'<path d="M{ox + 100} {oy + 116} L{ox + 100} {oy + 50}" class="f-vessel" style="stroke-width:26;opacity:.25"/>'
    # native targets (thin)
    b += _d1_d1_v(f'M{ox + 140} {oy + 126} C{ox + 140} {oy + 170} {ox + 136} {oy + 220} {ox + 130} {oy + 256}', 3)  # LAD
    b += _d1_d1_v(f'M{ox + 150} {oy + 124} C{ox + 190} {oy + 134} {ox + 204} {oy + 170} {ox + 206} {oy + 196}', 3)  # Cx/OM
    b += _d1_d1_v(f'M{ox + 84} {oy + 124} C{ox + 50} {oy + 130} {ox + 34} {oy + 170} {ox + 44} {oy + 210}', 3)   # RCA
    return b


def d1_graft_configs():
    """Conventional grafting against aorta-sparing configurations (TSRA ch. 50; FRCS Atlas draft)."""
    b = ''
    heads = [('In situ LIMA to LAD,', 'vein grafts from the aorta'), ('In situ bilateral', 'mammary arteries'), ('Composite Y-graft', 'on the in situ LIMA')]
    for i, (h1, h2) in enumerate(heads):
        ox = 10 + i * 236
        b += f'<rect x="{ox}" y="10" width="226" height="370" rx="10" class="f-b0"/>'
        b += T(ox + 113, 32, h1, 'f-h') + T(ox + 113, 50, h2, 'f-s')
        b += _d1_d1_heart_targets(ox + 4, 50)
        # subclavians at top
        b += line(ox + 14, 74, ox + 70, 74, 'f-grid') + line(ox + 150, 74, ox + 212, 74, 'f-grid')
        lima = f'M{ox + 196} 74 C{ox + 206} 140 {ox + 170} 200 {ox + 144} 230'
        b += _d1_d1_v(lima, 6)
        b += f'<circle cx="{ox + 144}" cy="230" r="4" class="f-ah"/>'
        if i == 0:
            b += _d1_d1_v(f'M{ox + 110} 150 C{ox + 170} 140 {ox + 210} 200 {ox + 210} 236', 5, ' stroke-dasharray="6 9"')
            b += _d1_d1_v(f'M{ox + 98} 156 C{ox + 40} 150 {ox + 26} 220 {ox + 48} 254', 5, ' stroke-dasharray="6 9"')
            b += f'<circle cx="{ox + 210}" cy="236" r="4" class="f-ah"/><circle cx="{ox + 48}" cy="254" r="4" class="f-ah"/>'
            b += f'<circle cx="{ox + 104}" cy="152" r="5" class="f-warn"/>'
            b += T(ox + 113, 326, ['Proximals on the aorta', '(fat fold): needs a clamp', 'or a proximal device'], 'f-s')
        elif i == 1:
            b += _d1_d1_v(f'M{ox + 30} 74 C{ox + 20} 140 {ox + 30} 210 {ox + 48} 254', 6)
            b += f'<circle cx="{ox + 48}" cy="254" r="4" class="f-ah"/>'
            b += T(ox + 22, 100, 'RIMA', 'f-s', 'start')
            b += T(ox + 113, 326, ['No anastomosis', 'on the aorta'], 'f-s')
        else:
            b += _d1_d1_v(f'M{ox + 186} 150 C{ox + 214} 170 {ox + 216} 210 {ox + 210} 236', 5)
            b += f'<circle cx="{ox + 186}" cy="150" r="5" class="f-ok"/><circle cx="{ox + 210}" cy="236" r="4" class="f-ah"/>'
            b += T(ox + 113, 326, ['Free graft sewn end-to-side', 'onto the LIMA:', 'no aortic touch'], 'f-s')
        b += T(ox + 204, 96, 'LIMA', 'f-s', 'end')
    b += _d1_d1_v('M20 402 L52 402', 6) + T(58, 406, 'Arterial graft', 'f-s', 'start')
    b += _d1_d1_v('M170 402 L202 402', 5, ' stroke-dasharray="6 9"') + T(208, 406, 'Vein graft', 'f-s', 'start')
    b += f'<circle cx="300" cy="402" r="5" class="f-warn"/>' + T(310, 406, 'Aortic proximal', 'f-s', 'start')
    b += f'<circle cx="430" cy="402" r="5" class="f-ok"/>' + T(440, 406, 'Graft-to-graft junction', 'f-s', 'start')
    b += T(360, 432, 'Porcelain aorta: anaortic off-pump surgery with in situ mammaries or composite Y-grafts (Atlas draft).', 'f-s')
    return svg(444, b)


def d1_offpump_exposure():
    """Off-pump exposure: what destabilises the heart and the counter-measures (TSRA ch. 50)."""
    b = T(12, 20, 'Off-pump exposure (arrangement schematic)', 'f-h', 'start')
    # heart lifted by apical suction
    b += '<path d="M90 230 C70 170 110 100 180 84 C240 74 290 110 296 160 C300 210 260 260 200 270 C150 276 104 266 90 230 Z" class="f-b0"/>'
    b += '<ellipse cx="200" cy="70" rx="34" ry="16" class="f-ok"/>' + line(200, 54, 200, 30) + T(240, 40, 'Apical suction device', 'f-s', 'start')
    # target vessel with stabiliser feet
    b += _d1_d1_v('M140 120 C180 160 214 200 236 250', 5)
    b += '<path d="M168 156 L204 196" class="f-l" style="stroke-width:7;opacity:.6"/>'
    b += '<path d="M182 146 L218 186" class="f-l" style="stroke-width:7;opacity:.6"/>'
    b += line(204, 166, 300, 290) + T(304, 302, 'Suction stabiliser on the target', 'f-s', 'start')
    # deep pericardial sutures
    b += '<path d="M110 250 L60 300 M150 268 L120 318" class="f-dash"/>' + T(30, 334, 'Deep pericardial sutures', 'f-s', 'start')
    # right pleura opened
    b += '<path d="M20 120 C30 160 30 200 20 240" class="f-cut" stroke-dasharray="6 4"/>' + T(14, 92, ['Right pleura and', 'pericardium opened'], 'f-s', 'start')
    # shunt inset
    ix, iy = 330, 60
    b += f'<rect x="{ix}" y="{iy}" width="160" height="110" rx="10" class="f-b0"/>' + T(ix + 80, iy + 18, 'Intracoronary shunt', 'f-s')
    b += f'<path d="M{ix + 10} {iy + 70} L{ix + 150} {iy + 70}" class="f-vessel" style="stroke-width:16"/>'
    b += f'<path d="M{ix + 60} {iy + 62} L{ix + 100} {iy + 62}" class="f-cut"/>'
    b += f'<rect x="{ix + 36}" y="{iy + 67}" width="88" height="6" rx="3" class="f-b1"/>'
    b += T(ix + 80, iy + 100, 'risk: air, intimal injury', 'f-s')
    # cause -> counter table
    x = 504
    b += box(x, 34, 206, 30, 'Why it destabilises', 'warn', 'f-h')
    b += box(x, 70, 206, 66, ['RV compressed when the', 'lateral wall is exposed', '(less filling, less output)'], 'b0', 'f-s')
    b += box(x, 142, 206, 50, ['Stabiliser pressure:', 'diastolic dysfunction'], 'b0', 'f-s')
    b += box(x, 198, 206, 34, 'Ischaemia of the target', 'b0', 'f-s')
    b += box(10, 352, 700, 82, ['Counter-measures: head-down (Trendelenburg) · short-acting alpha agonist · LIMA to LAD before',
                                'lifting the heart · deep pericardial sutures · right pleurotomy and pericardiotomy to spare the RV ·',
                                'right hemisternal elevation · apical suction · coronary shunts. Off-pump: fewer transfusions, less early',
                                'renal and cognitive dysfunction; on-pump: more grafts, better circumflex grafting.'], 'ok', 'f-s')
    return svg(444, b)


def d1_redo_cabg():
    """Redo coronary surgery: handling old grafts (TSRA ch. 50)."""
    b = T(12, 20, 'Redo grafting: what to do with the old grafts (arrangement schematic)', 'f-h', 'start')
    b += '<path d="M120 140 C90 220 130 330 240 356 C340 372 420 320 428 240 C434 170 390 128 320 122 C240 116 160 118 120 140 Z" class="f-b0"/>'
    b += '<path d="M250 122 L250 56" class="f-vessel" style="stroke-width:30;opacity:.25"/>' + T(232, 70, 'Aorta', 'f-s', 'end')
    # native targets
    b += _d1_d1_v('M170 150 C168 220 176 280 196 340', 4)
    b += _d1_d1_v('M330 140 C334 200 336 260 340 330', 4)
    b += _d1_d1_v('M380 150 C392 200 396 240 398 290', 4)
    # old vein graft with stenosis, left alone
    b += _d1_d1_v('M238 112 C200 112 176 140 172 200', 6, ' stroke-dasharray="6 9"')
    b += '<rect x="184" y="118" width="16" height="12" rx="3" class="f-warn"/>'
    b += T(14, 52, ['Old vein graft, stenosis over', '50%: leave it in place;', 'do not handle (embolism)'], 'f-s', 'start')
    b += _d1_d1_lead(120, 92, 188, 120)
    # new arterial graft beside it, distal onto native vessel
    b += _d1_d1_v('M10 200 C80 210 140 240 182 270', 6) + '<circle cx="182" cy="270" r="4" class="f-ah"/>'
    b += T(14, 380, ['New arterial graft beside it;', 'distal onto the native vessel'], 'f-s', 'start')
    b += _d1_d1_lead(60, 366, 120, 236)
    # patent old LIMA, clamped
    b += _d1_d1_v('M440 40 C440 120 400 200 338 262', 6) + '<circle cx="338" cy="262" r="4" class="f-ah"/>'
    b += '<rect x="416" y="100" width="44" height="9" rx="3" class="f-warn"/>' + T(448, 128, 'clamp', 'f-s', 'start')
    b += T(470, 392, ['Patent old LIMA to LAD: clamp it', 'while giving cardioplegia'], 'f-s', 'end')
    # new vein graft from the hood of the old one
    b += _d1_d1_v('M226 112 C300 100 380 150 392 220', 5, ' stroke-dasharray="6 9"') + '<circle cx="392" cy="220" r="4" class="f-ah"/>'
    b += '<circle cx="226" cy="112" r="5" class="f-ok"/>'
    b += T(272, 46, ['Proximal onto the hood of', 'a new or old vein graft'], 'f-s', 'start') + _d1_d1_lead(300, 66, 232, 108)
    x = 486
    b += box(x, 40, 224, 112, ['Work-up', 'Angiography incl. mammaries', 'Old operation note', 'Viability; conduit mapping',
                               'CT: retrosternal anatomy'], 'b1', 'f-s')
    b += box(x, 164, 224, 56, ['RV may be stuck to the', 'back of the sternum'], 'warn', 'f-s')
    b += box(x, 232, 224, 76, ['New distal anastomoses', 'go on the native', 'vessel'], 'b0', 'f-s')
    b += box(x, 320, 224, 56, ['Mortality 3 to 8%, mostly', 'perioperative infarction'], 'b0', 'f-s')
    return svg(412, b)


def _d1_d1_ring(cx, cy, ro, ri, iel_dash, label):
    b = f'<circle cx="{cx}" cy="{cy}" r="{ro}" class="f-b0"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{ri + 6}" class="f-b1"/>'
    dash = ' stroke-dasharray="6 5"' if iel_dash else ''
    b += f'<circle cx="{cx}" cy="{cy}" r="{ri + 3}" class="f-l" style="stroke-width:2.5"{dash}/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{ri}" class="f-lumen"/>'
    b += T(cx, cy + 5, label, 'f-s')
    return b


def d1_conduit_wall():
    """Why conduits behave differently (TSRA ch. 50)."""
    b = ''
    cols = [('Internal mammary', False, 46, 34, 'ok',
             ['Non-fenestrated internal', 'elastic lamina', 'High NO and prostacyclin', 'No constriction to', 'noradrenaline']),
            ('Radial artery', True, 58, 28, 'b1',
             ['Fenestrated lamina,', 'thicker wall', 'Spasm, calcification,', 'atheroma; patency hurt', 'by competitive flow']),
            ('Saphenous vein', None, 50, 36, 'warn',
             ['Fails: technical or', 'thrombotic early (up to 10%', 'in 30 days), then intimal', 'hyperplasia, then graft', 'atheroma'])]
    for i, (h, iel, ro, ri, cls, notes) in enumerate(cols):
        x = 10 + i * 236
        cx = x + 113
        b += f'<rect x="{x}" y="10" width="226" height="290" rx="10" class="f-{cls}"/>'
        b += T(cx, 34, h, 'f-h')
        if iel is None:
            b += f'<circle cx="{cx}" cy="106" r="{ro}" class="f-b0"/><circle cx="{cx}" cy="106" r="{ri}" class="f-lumen"/>'
            b += T(cx, 111, 'lumen', 'f-s')
        else:
            b += _d1_d1_ring(cx, 106, ro, ri, iel, 'lumen')
        b += T(cx, 196, notes, 'f-s')
    b += line(560, 330, 590, 330, 'f-l') + T(596, 334, 'continuous lamina', 'f-s', 'start')
    b += f'<line x1="380" y1="330" x2="410" y2="330" class="f-l" stroke-dasharray="6 5"/>' + T(416, 334, 'fenestrated lamina', 'f-s', 'start')
    b += T(12, 334, 'Schematic cross-sections, not to scale', 'f-s', 'start')
    return svg(346, b)


def d1_valve_cabg_sequence():
    """Order of steps for combined valve and coronary surgery (TSRA ch. 54)."""
    G = True
    rows = [('CABG + AVR', [(['TOE; aortic and', 'two-stage venous'], 0), (['Clamp; antegrade', '+ retrograde plegia'], 0),
                            (['LV vent'], 0), (['Distal vein', 'grafts'], G), (['Plegia down', 'the vein grafts'], G),
                            (['Oblique aortotomy;', 'AVR; close'], 0), (['Distal mammary'], G), (['Proximals'], G)]),
            ('CABG + mitral', [(['TOE; bypass'], 0), (['Clamp; antegrade', '+ retrograde plegia'], 0), (['LV vent'], 0),
                               (['Distal vein', 'grafts'], G), (['Left atriotomy', '(interatrial groove)'], 0),
                               (['AF ablation, LAA', 'ligation if AF'], 0), (['Mitral repair or', 'MVR; close atrium'], 0),
                               (['Distal mammary,', 'then proximals'], G)]),
            ('CABG + AVR + mitral', [(['TOE; bypass; clamp;', 'ante + retro; LV vent'], 0), (['Distal vein', 'grafts'], G),
                                     (['Aortotomy: excise', 'the valve, no AVR yet'], 0), (['Left atriotomy;', 'any AF procedure'], 0),
                                     (['Mitral repair or', 'MVR; close atrium'], 0), (['AVR; close', 'the aortotomy'], 0),
                                     (['Distal mammary'], G), (['Proximals'], G)])]
    b = ''
    y = 10
    for head, steps in rows:
        b += T(12, y + 18, head, 'f-h', 'start')
        y += 28
        for j, (s, g) in enumerate(steps):
            x = 10 + (j % 4) * 177
            yy = y + (j // 4) * 52
            cls = 'warn' if g else 'b0'
            b += f'<rect x="{x}" y="{yy}" width="168" height="46" rx="8" class="f-{cls}"/>'
            b += _d1_d1_num(x + 16, yy + 23, j + 1, 'b1')
            b += T(x + 32, yy + (28 if len(s) == 1 else 19), s, 'f-s', 'start')
        y += 112
    b += f'<rect x="12" y="{y}" width="18" height="12" class="f-warn"/>' + T(36, y + 11, 'Grafting steps: vein distals first (cardioplegia can then go down them); mammary and proximals last', 'f-s', 'start')
    return svg(y + 26, b)


def d1_ttfm():
    """Transit-time flow thresholds (FRCS Atlas draft)."""
    return tiles([('15 to 20', ['mean flow (mL/min)', 'should be above'], 'ok'), ('3 to 5', ['pulsatility index', 'should be below'], 'ok'),
                  ('50 to 70%', ['diastolic filling above', '(left-sided grafts)'], 'ok'),
                  ('6 mL/min', ['radial to OM1, PI 8.2:', 'kink, spasm? revise'], 'warn')], 104)




# ---- figs_D2.py
"""D2 drawing pass (22 to 23 November 2026): aortic root, arch, dissection, cord and cerebral
protection, arch anomalies and coarctation. Every label comes from the ST4 notes (c6, c9, g10)
or the TSRA Review chapters 75 to 81, 96 and 97 on disk."""
from math import cos, sin, radians



# ---------------------------------------------------------------- helpers

def _d2_pt(cx, cy, r, deg):
    a = radians(deg)
    return cx + r * cos(a), cy - r * sin(a)


def _d2_arc(cx, cy, r, d1, d2):
    """Path fragment (no M) along a circle from angle d1 to d2 (degrees, d1 > d2 = clockwise on screen)."""
    x2, y2 = _d2_pt(cx, cy, r, d2)
    large = 1 if abs(d1 - d2) > 180 else 0
    sweep = 1 if d1 > d2 else 0
    return f'A{r} {r} 0 {large} {sweep} {x2:.1f} {y2:.1f}'


def _d2_arch_d(cx, cy, r, y_asc, y_desc):
    """Centre line: ascending (x = cx - r) up from y_asc, arch over the top, descending down to y_desc."""
    return f'M{cx - r} {y_asc} L{cx - r} {cy} {_d2_arc(cx, cy, r, 180, 0)} L{cx + r} {y_desc}'


def _d2_vessel(d, w):
    return f'<path d="{d}" class="f-vessel" style="stroke-width:{w}"/>'


def _d2_graft(d, w):
    return f'<path d="{d}" class="f-duct" style="stroke-width:{w};opacity:.75"/>'


def _d2_branch(cx, cy, r, deg, length, w, cls='f-vessel'):
    x1, y1 = _d2_pt(cx, cy, r, deg)
    x2, y2 = _d2_pt(cx, cy, r + length, deg)
    return f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" class="{cls}" style="stroke-width:{w}"/>', (x2, y2)


def _d2_radial(cx, cy, r, deg, half, cls='f-cut', sw=2.5):
    x1, y1 = _d2_pt(cx, cy, r - half, deg)
    x2, y2 = _d2_pt(cx, cy, r + half, deg)
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" style="stroke-width:{sw}"/>'


def _d2_dim(x1, y1, x2, y2):
    """Double-headed measurement arrow."""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="f-l" style="stroke-width:2"'
            ' marker-start="url(#ah)" marker-end="url(#ah)"/>')


def _d2_card(x, y, w, h, head, lines, cls='b0', hcls='b1'):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="f-{cls}"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" class="f-{hcls}"/>'
    out += T(x + w / 2, y + 20, head, 'f-h') + T(x + w / 2, y + 50, lines, 'f-s')
    return out


# ---------------------------------------------------------------- 1 Stanford and DeBakey

def d2_stanford_debakey():
    b = T(12, 20, 'DeBakey types, with the Stanford type each falls into', 'f-h', 'start')
    b += line(10, 262, 530, 262, 'f-dash') + T(14, 256, 'Diaphragm', 'f-s', 'start')
    spec = [('DeBakey I', ['Ascending, arch', 'and descending'], 'I', 'A'),
            ('DeBakey II', ['Ascending only'], 'II', 'A'),
            ('DeBakey IIIa', ['Descending, above', 'the diaphragm'], 'IIIa', 'B'),
            ('DeBakey IIIb', ['Descending, below', 'the diaphragm'], 'IIIb', 'B')]
    for i, (head, desc, k, st) in enumerate(spec):
        x0 = 10 + i * 130
        cx, cy, r = x0 + 62, 110, 32
        b += _d2_vessel(_d2_arch_d(cx, cy, r, 200, 340), 15)
        for deg in (138, 100, 62):
            b += _d2_branch(cx, cy, r, deg, 24, 6)[0]
        a, d = cx - r, cx + r
        sx, sy = _d2_pt(cx, cy, r, 48)
        if k == 'I':
            p = f'M{a} 192 L{a} {cy} {_d2_arc(cx, cy, r, 180, 0)} L{d} 334'
        elif k == 'II':
            p = f'M{a} 192 L{a} {cy}'
        elif k == 'IIIa':
            p = f'M{sx:.1f} {sy:.1f} {_d2_arc(cx, cy, r, 48, 0)} L{d} 260'
        else:
            p = f'M{sx:.1f} {sy:.1f} {_d2_arc(cx, cy, r, 48, 0)} L{d} 334'
        b += f'<path d="{p}" class="f-l" style="stroke-width:3.5"/>'
        b += T(cx, 44, head, 'f-h')
        b += T(cx, 362, desc, 'f-s')
        cls = 'warn' if st == 'A' else 'b1'
        b += box(x0 + 12, 396, 100, 30, 'Stanford ' + st, cls, 'f-h')
    b += box(546, 44, 164, 112, ['Stanford A: involves', 'the ascending aorta,', 'wherever the tear', '(I and II)'], 'warn', 'f-s')
    b += box(546, 166, 164, 112, ['Stanford B: spares the', 'ascending; usually beyond', 'the left subclavian,', 'may involve the arch'], 'b1', 'f-s')
    b += box(546, 288, 164, 96, ['Timing: acute 14 days', 'or less; subacute 15 to', '90 days; chronic over 90'], 'b0', 'f-s')
    b += T(546, 412, 'Dark line: dissected segment', 'f-s', 'start')
    return svg(436, b)


# ---------------------------------------------------------------- 2 malperfusion

def _d2_mp_wall(x0):
    out = line(x0 + 10, 50, x0 + 330, 50) + line(x0 + 10, 140, x0 + 150, 140) + line(x0 + 190, 140, x0 + 330, 140)
    out += line(x0 + 150, 140, x0 + 150, 222) + line(x0 + 190, 140, x0 + 190, 222)
    return out.replace('class="f-l"', 'class="f-l" style="stroke-width:3"')


def d2_malperfusion():
    b = ''
    # dynamic
    x0 = 10
    b += T(x0 + 170, 22, 'Dynamic obstruction', 'f-h')
    b += _d2_mp_wall(x0)
    b += (f'<path d="M{x0 + 10} 78 C{x0 + 90} 78 {x0 + 118} 136 {x0 + 170} 134 '
          f'C{x0 + 222} 132 {x0 + 250} 78 {x0 + 330} 78" class="f-l" style="stroke-width:3.5"/>')
    b += T(x0 + 70, 70, 'False lumen, pressurised', 'f-s', 'start')
    b += T(x0 + 18, 112, 'True lumen', 'f-s', 'start') + T(x0 + 18, 127, 'collapsed', 'f-s', 'start')
    b += T(x0 + 144, 214, 'Branch', 'f-s', 'end')
    b += arrow(x0 + 208, 164, x0 + 192, 146) + T(x0 + 212, 172, ['Flap covers the ostium', '(usually in systole);', 'ostium undamaged'], 'f-s', 'start')
    # static
    x0 = 370
    b += T(x0 + 170, 22, 'Static obstruction', 'f-h')
    b += _d2_mp_wall(x0)
    b += f'<rect x="{x0 + 151}" y="150" width="16" height="64" class="f-warn"/>'
    b += (f'<path d="M{x0 + 10} 96 L{x0 + 140} 96 C{x0 + 162} 96 {x0 + 168} 116 {x0 + 168} 140 '
          f'L{x0 + 168} 218" class="f-l" style="stroke-width:3.5"/>')
    b += T(x0 + 22, 80, 'False lumen', 'f-s', 'start') + T(x0 + 22, 124, 'True lumen', 'f-s', 'start')
    b += arrow(x0 + 120, 186, x0 + 150, 186) + T(x0 + 114, 166, ['Flap runs into', 'the branch:', 'stenosis or', 'thrombosis'], 'f-s', 'end')
    b += T(x0 + 200, 196, ['Haematoma or', 'thrombus in the', 'branch false lumen'], 'f-s', 'start')
    # fixes
    b += box(10, 236, 340, 62, ['Usually resolves with true-lumen flow:', 'central repair (type A), cover the', 'entry tear (type B) or fenestration'], 'ok', 'f-s')
    b += box(370, 236, 340, 62, ['May persist after central repair', 'or TEVAR: stent or reconstruct', 'the branch'], 'warn', 'f-s')
    b += T(360, 322, 'Both can coexist in one branch. Stable malperfusion syndrome, no rupture or tamponade (specialist centres):', 'f-s')
    b += box(10, 334, 220, 62, ['1 Endovascular fenestration', 'or branch stenting'], 'b1', 'f-s')
    b += arrow(230, 365, 250, 365)
    b += box(252, 334, 216, 62, ['2 Recovery of organ', 'failure or shock'], 'b0', 'f-s')
    b += arrow(468, 365, 488, 365)
    b += box(490, 334, 220, 62, ['3 Open type A repair', '(immediate central repair:', 'mortality up to 60 to 70%)'], 'b0', 'f-s')
    return svg(406, b)


# ---------------------------------------------------------------- 3 button Bentall

def _d2_root_walls(cx, top, stj, ann, a=40, s=62, an=42):
    lw = (f'M{cx - a} {top} L{cx - a} {stj} C{cx - s - 4} {stj + 30} {cx - s - 4} {ann - 40} {cx - an} {ann}')
    rw = (f'M{cx + a} {top} L{cx + a} {stj} C{cx + s + 4} {stj + 30} {cx + s + 4} {ann - 40} {cx + an} {ann}')
    return f'<path d="{lw}" class="f-l" style="stroke-width:2.5"/><path d="{rw}" class="f-l" style="stroke-width:2.5"/>'


def _d2_tube(cx, y1, y2, hw=42):
    out = f'<rect x="{cx - hw}" y="{y1}" width="{2 * hw}" height="{y2 - y1}" rx="4" class="f-b0"/>'
    y = y1 + 10
    while y < y2 - 4:
        out += line(cx - hw + 2, y, cx + hw - 2, y, 'f-grid')
        y += 10
    return out


def d2_bentall():
    b = ''
    # panel 1: excise
    cx = 120
    b += T(cx, 22, '1 Excise root and valve', 'f-h')
    b += _d2_root_walls(cx, 46, 108, 248)
    b += line(cx - 52, 106, cx + 52, 106, 'f-cut') + T(cx + 56, 102, 'STJ', 'f-s', 'start')
    b += T(cx, 138, 'Buttons cut out', 'f-s')
    for x, y, dx in ((cx - 54, 172, -1), (cx + 54, 164, 1)):
        b += f'<path d="M{x} {y} L{x + dx * 46} {y - 18}" class="f-vessel" style="stroke-width:8"/>'
        b += f'<circle cx="{x}" cy="{y}" r="7" class="f-lumen"/>'
        b += f'<circle cx="{x}" cy="{y}" r="17" class="f-cut" fill="none" stroke-dasharray="4 3"/>'
    for k in range(3):
        x1 = cx - 40 + k * 26.7
        b += f'<path d="M{x1:.1f} 248 Q{x1 + 13.3:.1f} 222 {x1 + 26.7:.1f} 248" class="f-l" stroke-dasharray="3 3"/>'
    b += T(cx, 272, 'Aneurysmal sinuses and', 'f-s') + T(cx, 289, 'leaflets resected', 'f-s')
    # panel 2: seat conduit
    cx = 360
    b += T(cx, 22, '2 Seat the valved conduit', 'f-h')
    b += _d2_tube(cx, 60, 226)
    b += f'<rect x="{cx - 42}" y="226" width="84" height="22" rx="4" class="f-b1"/>' + T(cx, 242, 'Valve', 'f-s')
    b += line(cx - 60, 256, cx + 60, 256, 'f-l')
    for k in range(9):
        x = cx - 40 + k * 10
        b += line(x, 246, x, 262, 'f-cut')
    b += T(cx, 280, 'Sutured intra-annularly;', 'f-s') + T(cx, 297, 'mechanical or biological', 'f-s')
    b += T(cx + 50, 120, ['Dacron', 'conduit'], 'f-s', 'start')
    # panel 3: buttons and distal
    cx = 600
    b += T(cx, 22, '3 Buttons, then distal end', 'f-h')
    b += f'<rect x="{cx - 42}" y="38" width="84" height="40" rx="4" class="f-b1"/>' + T(cx, 62, 'Native ascending', 'f-s')
    b += line(cx - 50, 80, cx + 50, 80, 'f-cut')
    b += _d2_tube(cx, 82, 226)
    b += f'<rect x="{cx - 42}" y="226" width="84" height="22" rx="4" class="f-b1"/>'
    for x, y, dx in ((cx - 42, 168, -1), (cx + 42, 160, 1)):
        b += f'<path d="M{x + dx * 10} {y} L{x + dx * 52} {y - 20}" class="f-vessel" style="stroke-width:8"/>'
        b += f'<circle cx="{x}" cy="{y}" r="13" class="f-b1"/><circle cx="{x}" cy="{y}" r="6" class="f-lumen"/>'
    b += T(cx, 280, 'Openings cut for the buttons;', 'f-s') + T(cx, 297, 'graft trimmed, distal anastomosis', 'f-s')
    b += box(10, 314, 228, 60, ['Oversize the graft to recreate', 'sinuses, or use a graft with', 'premade sinuses (Valsalva)'], 'b0', 'f-s')
    b += box(246, 314, 228, 60, ['EACTS/STS 2024: root aneurysm', 'with a structurally diseased', 'valve (I, B)'], 'ok', 'f-s')
    b += box(482, 314, 228, 60, ['Elective Bentall: in-hospital', 'mortality 1 to 2%; 10-year', 'survival 78 to 93%'], 'b1', 'f-s')
    return svg(384, b)


# ---------------------------------------------------------------- 4 root options

def d2_root_options():
    b = box(170, 8, 380, 44, ['Root aneurysm: is the valve structurally', 'diseased or calcified?'], 'b1', 'f-h')
    b += arrow(250, 52, 130, 84) + T(176, 72, 'Yes', 'f-h', 'end')
    b += line(480, 52, 480, 72) + T(488, 66, 'No: cusps normal or repairable', 'f-s', 'start')
    b += _d2_card(10, 86, 240, 150, 'Composite valve graft', ['Modified (button) Bentall;', 'mechanical or biological', 'valve; coronary buttons', 'reimplanted', 'EACTS/STS 2024: I, B'], 'b0', 'warn')
    b += _d2_card(262, 86, 220, 150, 'Reimplantation (David)', ['Valve re-suspended inside', 'a tube anchored below the', 'annulus: stabilises it;', 'preferred in connective tissue', 'disease; fewer reinterventions'], 'b0', 'ok')
    b += _d2_card(494, 86, 216, 150, 'Remodelling (Yacoub)', ['Graft recreates three', 'neo-sinuses; annulus not', 'supported. In heritable', 'disease, not without an', 'annuloplasty'], 'b0', 'b1')
    b += line(372, 72, 602, 72) + arrow(372, 72, 372, 84) + arrow(602, 72, 602, 84)
    b += box(10, 248, 340, 60, ['Selected patients: Ross (pulmonary autograft)', 'or stentless porcine root (Freestyle)'], 'b0', 'f-s')
    b += box(362, 248, 348, 60, ['Valve-sparing: tricuspid IIa, B; bicuspid IIb, B', '(specific repair expertise). Elective', 'in-hospital mortality 0.3 to 1.5%'], 'ok', 'f-s')
    b += box(10, 318, 700, 44, ['Ascending phenotype: a root of 45 mm or less is not replaced unless the patient is young,',
                                'has a family history of type A dissection, or has heritable aortic disease'], 'b1', 'f-s')
    return svg(372, b)


# ---------------------------------------------------------------- 5 hemiarch, partial and total arch

def _d2_limb(cx, cy, r, deg, tip):
    sx, sy = _d2_pt(cx, cy, r + 8, deg)
    ex, ey = _d2_pt(cx, cy, r + 30, deg)
    return _d2_graft(f'M{sx:.1f} {sy:.1f} L{ex:.1f} {ey:.1f}', 9) + f'<line x1="{ex - 6:.1f}" y1="{ey:.1f}" x2="{ex + 6:.1f}" y2="{ey:.1f}" class="f-cut" style="stroke-width:2.5"/>'


def d2_arch_repairs():
    b = ''
    heads = [('Hemiarch', ['Bevelled open distal anastomosis', 'under arrest: greater curve near', 'the innominate to the lesser', 'curve opposite the left subclavian']),
             ('Partial arch', ['One or more trunks reimplanted', '(e.g. quadrifurcated graft);', 'distal anastomosis in zone 1', 'or 2']),
             ('Total arch', ['Zones 0 to 2 or beyond; branches', 'as an island, a peninsula or', 'separate grafts (branched graft)', 'Arrest about 60 min'])]
    for i, (h, txt) in enumerate(heads):
        x0 = 10 + i * 236
        cx, cy, r = x0 + 112, 130, 58
        b += T(x0 + 112, 22, h, 'f-h')
        b += _d2_vessel(_d2_arch_d(cx, cy, r, 262, 286), 22)
        tips = {}
        for deg in (132, 98, 64):
            s, tip = _d2_branch(cx, cy, r, deg, 42, 11)
            b += s
            tips[deg] = tip
        if i == 0:
            b += _d2_graft(f'M{cx - r} 238 L{cx - r} {cy} {_d2_arc(cx, cy, r, 180, 112)}', 24)
            x1, y1 = _d2_pt(cx, cy, r + 13, 140)
            x2, y2 = _d2_pt(cx, cy, r - 13, 66)
            b += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="f-cut" style="stroke-width:3"/>'
        elif i == 1:
            b += _d2_graft(f'M{cx - r} 238 L{cx - r} {cy} {_d2_arc(cx, cy, r, 180, 80)}', 24)
            b += _d2_radial(cx, cy, r, 80, 15, sw=3)
            for deg in (132, 98):
                b += _d2_limb(cx, cy, r, deg, tips[deg])
        else:
            b += _d2_graft(f'M{cx - r} 238 L{cx - r} {cy} {_d2_arc(cx, cy, r, 180, 0)} L{cx + r} {cy + 44}', 24)
            b += line(cx + r - 15, cy + 44, cx + r + 15, cy + 44, 'f-cut')
            for deg in (132, 98, 64):
                b += _d2_limb(cx, cy, r, deg, tips[deg])
        b += line(cx - r - 14, 238, cx - r + 14, 238, 'f-cut')
        b += T(cx - r - 18, 254, 'Root', 'f-s', 'end') if i == 0 else ''
        b += T(x0 + 112, 300, txt, 'f-s')
    b += T(12, 384, 'Green: graft. Red line: suture line.', 'f-s', 'start')
    b += box(10, 396, 345, 60, ['Hemiarch: arrest about 20 to 30 min;', 'high-moderate lower-body arrest plus', 'cerebral perfusion (I, C)'], 'ok', 'f-s')
    b += box(365, 396, 345, 60, ['Proximal arch over 45 mm at ascending', 'surgery: hemiarch or more (IIb, B);', 'avoid short ascending grafts (I, C)'], 'b1', 'f-s')
    return svg(466, b)


# ---------------------------------------------------------------- 6 elephant trunk and FET

def d2_et_fet():
    b = ''
    heads = [('Classic ET, stage 1', 'Sternotomy, arrest'), ('Classic ET, stage 2', 'Left thoracotomy or TEVAR'),
             ('Frozen elephant trunk', 'One stage, sternotomy')]
    for i, (h, sub) in enumerate(heads):
        x0 = 10 + i * 236
        cx, cy, r = x0 + 76, 128, 52
        b += T(x0 + 112, 20, h, 'f-h') + T(x0 + 112, 37, sub, 'f-s')
        b += _d2_vessel(_d2_arch_d(cx, cy, r, 236, 340), 32)
        for deg in (132, 98, 64):
            b += _d2_branch(cx, cy, r, deg, 30, 10)[0]
        an = cy + 28
        b += _d2_graft(f'M{cx - r} 214 L{cx - r} {cy} {_d2_arc(cx, cy, r, 180, 0)} L{cx + r} {an}', 20)
        b += line(cx + r - 18, an, cx + r + 18, an, 'f-cut')
        if i < 2:
            b += _d2_graft(f'M{cx + r} {an} L{cx + r} 246', 10)
            if i == 0:
                b += T(cx + r + 22, 206, ['Trunk floats', 'free in the', 'descending', 'aorta'], 'f-s', 'start')
            else:
                b += line(cx + r - 18, 246, cx + r + 18, 246, 'f-cut')
                b += _d2_graft(f'M{cx + r} 246 L{cx + r} 330', 20)
                b += T(cx + r + 22, 266, ['New tube graft', 'sewn to the', 'trunk; or the', 'trunk extended', 'by TEVAR'], 'f-s', 'start')
        else:
            b += f'<path d="M{cx + r} {an + 2} L{cx + r} 286" class="f-stent" style="stroke-width:20"/>'
            zz = f'M{cx + r - 8} {an + 4}'
            y = an + 4
            k = 0
            while y < 282:
                y += 9
                k += 1
                zz += f' L{cx + r + (8 if k % 2 else -8)} {y}'
            b += f'<path d="{zz}" class="f-l"/>'
            b += T(cx + r + 22, 190, ['Stent graft', 'deployed', 'antegrade,', 'direct vision;', 'sewn round:', 'no proximal', 'endoleak'], 'f-s', 'start')
    b += T(12, 376, 'Green: polyester graft. Dashed band: stent graft. Red line: suture line.', 'f-s', 'start')
    b += box(10, 388, 345, 78, ['EACTS/STS 2024: distal anastomosis in zone 2', '(IIa, C); polyester reachable in zone 4 (IIa, C);',
                                'intended one-stage repair: FET (IIa, B); routine', 'CSF drain in FET with limited coverage (III, C)'], 'b0', 'f-s')
    b += box(365, 388, 345, 78, ['FET in type A dissection (TSRA ch. 75): more', 'false-lumen obliteration and true-lumen',
                                 'expansion; paraplegia rises from under 1%', 'to 5 to 10% (up to 15%)'], 'warn', 'f-s')
    return svg(476, b)


# ---------------------------------------------------------------- 7 Ishimaru zones

def d2_arch_zones():
    cx, cy, r = 250, 200, 100
    b = T(12, 22, 'Aortic zones 0 to 4 (Ishimaru), with the Roselli split of zone 0', 'f-h', 'start')
    b += '<ellipse cx="190" cy="282" rx="58" ry="11" class="f-b1"/>' + T(252, 286, 'Right PA', 'f-s', 'start')
    b += _d2_vessel(_d2_arch_d(cx, cy, r, 384, 396), 30)
    tips = {}
    for deg in (128, 100, 72):
        s, tip = _d2_branch(cx, cy, r, deg, 46, 14)
        b += s
        tips[deg] = tip
    b += T(tips[128][0] - 6, tips[128][1] - 6, 'Innominate', 'f-s', 'end')
    b += T(tips[100][0], tips[100][1] - 12, 'Left carotid', 'f-s')
    b += T(tips[72][0] + 6, tips[72][1] - 6, 'Left subclavian', 'f-s', 'start')
    b += '<circle cx="160" cy="350" r="5" class="f-lumen"/>'
    for deg in (121, 92, 64):
        b += _d2_radial(cx, cy, r, deg, 24)
    for y in (330, 276):
        b += line(cx - r - 24, y, cx - r + 24, y, 'f-cut').replace('/>', ' style="stroke-width:2.5"/>')
    for y, lab in ((270, 'T4'), (360, 'T6')):
        b += line(cx + r - 24, y, cx + r + 24, y, 'f-cut').replace('/>', ' style="stroke-width:2.5"/>')
        b += T(cx + r + 30, y + 4, lab, 'f-s', 'start')
    b += line(cx - r - 24, 384, cx - r + 24, 384, 'f-l') + T(cx - r - 30, 388, 'Annulus', 'f-s', 'end')
    for deg, lab in ((152, '0'), (107, '1'), (78, '2')):
        x, y = _d2_pt(cx, cy, r - 46, deg)
        b += T(x, y + 6, lab, 'f-big')
    b += T(cx + r - 44, 244, '3', 'f-big') + T(cx + r - 44, 326, '4', 'f-big')
    b += T(cx - r - 30, 362, '0A', 'f-h', 'end') + T(cx - r - 30, 308, '0B', 'f-h', 'end') + T(cx - r - 30, 230, '0C', 'f-h', 'end')
    b += box(430, 50, 280, 176, ['0A annulus to top of highest coronary', '0B to distal edge of right PA', '0C to distal end of innominate origin',
                                 '1 innominate to left carotid', '2 left carotid to left subclavian', '3 first 2 cm beyond subclavian, to T4',
                                 '4 to mid-descending (T6)', '5 to coeliac; 6 to 9 visceral; 10 and 11 iliac'], 'b0', 'f-s')
    b += box(430, 236, 280, 150, ['Total arch: zones 0 to 2 or beyond', 'Type B (SVS/STS): entry in zone 1', 'or beyond', 'Zone 0A disease: highest mortality',
                                  'Any TEVAR into zone 2: revascularise', 'the left subclavian (I, B)', 'Landing zone at least 25 mm'], 'ok', 'f-s')
    return svg(408, b)


# ---------------------------------------------------------------- 8 hybrid debranching

def _d2_stent(d):
    return f'<path d="{d}" class="f-stent" style="stroke-width:22"/>'


def d2_debranching():
    b = ''
    heads = [('Zone 2 TEVAR', ['Left subclavian revascularised:', 'carotid-subclavian bypass', 'or transposition']),
             ('Zone 1 TEVAR', ['Left carotid and subclavian', 'debranched to the innominate,', 'then staged TEVAR']),
             ('Zone 0 TEVAR', ['All arch vessels debranched', 'to the mid ascending aorta,', 'then staged TEVAR'])]
    for i, (h, txt) in enumerate(heads):
        x0 = 10 + i * 236
        cx, cy, r = x0 + 118, 128, 56
        b += T(x0 + 112, 18, h, 'f-h')
        b += _d2_vessel(_d2_arch_d(cx, cy, r, 250, 262), 22)
        tips = {}
        for deg in (130, 98, 66):
            s, tip = _d2_branch(cx, cy, r, deg, 44, 10)
            b += s
            tips[deg] = tip
        mid = {deg: _d2_pt(cx, cy, r + 30, deg) for deg in (130, 98, 66)}
        if i == 0:
            b += _d2_stent(f'M{_d2_pt(cx, cy, r, 90)[0]:.1f} {_d2_pt(cx, cy, r, 90)[1]:.1f} {_d2_arc(cx, cy, r, 90, 0)} L{cx + r} 236')
            (ax, ay), (bx, by) = mid[98], mid[66]
            b += _d2_graft(f'M{ax:.1f} {ay:.1f} Q{(ax + bx) / 2:.1f} {ay - 34:.1f} {bx:.1f} {by:.1f}', 6)
        elif i == 1:
            b += _d2_stent(f'M{_d2_pt(cx, cy, r, 118)[0]:.1f} {_d2_pt(cx, cy, r, 118)[1]:.1f} {_d2_arc(cx, cy, r, 118, 0)} L{cx + r} 236')
            (ax, ay), (bx, by), (dx, dy) = mid[130], mid[98], mid[66]
            b += _d2_graft(f'M{ax:.1f} {ay:.1f} Q{(ax + bx) / 2:.1f} {ay - 40:.1f} {bx:.1f} {by:.1f} Q{(bx + dx) / 2:.1f} {by - 30:.1f} {dx:.1f} {dy:.1f}', 6)
        else:
            b += _d2_stent(f'M{cx - r} {cy + 56} L{cx - r} {cy} {_d2_arc(cx, cy, r, 180, 0)} L{cx + r} 236')
            ox, oy = cx - r - 11, cy + 92
            jx, jy = cx - r - 34, cy - 46
            b += _d2_graft(f'M{ox} {oy} L{jx} {oy - 26} L{jx} {jy}', 7)
            for deg in (130, 98, 66):
                tx, ty = mid[deg]
                b += _d2_graft(f'M{jx} {jy} Q{(jx + tx) / 2:.1f} {min(jy, ty) - 26:.1f} {tx:.1f} {ty:.1f}', 5)
        b += T(x0 + 112, 284, txt, 'f-s')
    b += T(12, 352, 'Dashed band: stent graft. Green: bypass grafts.', 'f-s', 'start')
    b += box(10, 364, 345, 98, ['Emergency zone 2 cover is often tolerated.', 'Risks of covering the left subclavian:', 'arm ischaemia, vertebral steal, endoleak,',
                                'spinal cord ischaemia'], 'b0', 'f-s')
    b += box(365, 364, 345, 98, ['Revascularise first (elective), and always with:', 'a patent left IMA graft; dominant left or absent', 'right vertebral; left arm fistula; cover over',
                                 '20 cm; previous infrarenal aortic surgery;', 'occluded hypogastric arteries'], 'warn', 'f-s')
    b += box(10, 472, 700, 44, ['Hybrid arch avoids cross-clamp, bypass and arrest but carries more death and stroke (IIb, C);',
                                'avoid zone 0 to 2 landing in native aorta in connective tissue disease'], 'b1', 'f-s')
    return svg(526, b)


# ---------------------------------------------------------------- 9 cerebral perfusion

def d2_cerebral_perfusion():
    cx, cy, r = 222, 200, 70
    b = T(12, 20, "Viewed from the front: patient's right on the left", 'f-s', 'start')
    b += '<rect x="82" y="182" width="28" height="150" rx="12" class="f-b0"/>' + T(96, 350, 'SVC', 'f-h')
    b += _d2_vessel(_d2_arch_d(cx, cy, r, 334, 344), 22)
    s, (px, py) = _d2_branch(cx, cy, r, 130, 40, 12)
    b += s
    b += _d2_vessel(f'M{px:.1f} {py:.1f} L{px:.1f} 50', 10)
    b += _d2_vessel(f'M{px:.1f} {py:.1f} C{px - 30:.1f} {py:.1f} 70 {py + 6:.1f} 40 {py + 6:.1f}', 10)
    s, (lx, ly) = _d2_branch(cx, cy, r, 100, 92, 10)
    b += s
    s, (sx, sy) = _d2_branch(cx, cy, r, 68, 66, 10)
    b += s
    b += T(px - 8, 52, 'R carotid', 'f-s', 'end') + T(lx + 8, 44, 'L carotid', 'f-s', 'start')
    b += T(sx + 6, sy - 4, 'L subclavian', 'f-s', 'start')
    b += arrow(px - 16, 100, px - 16, 66) + arrow(lx - 14, 86, lx - 14, 58)
    b += _d2_graft(f'M46 {py + 6:.1f} L46 {py + 62:.1f} L20 {py + 62:.1f}', 6)
    b += T(56, py + 34, ['Right axillary:', '8 to 10 mm', 'side graft'], 'f-s', 'start')
    x1, y1 = _d2_pt(cx, cy, r + 14, 122)
    x2, y2 = _d2_pt(cx, cy, r + 14, 138)
    b += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="f-cut" style="stroke-width:5"/>'
    b += arrow(206, 250, 176, 146) + T(222, 268, ['Clamp the', 'proximal', 'innominate:', 'unilateral'], 'f-s')
    mx, my = _d2_pt(cx, cy, r + 50, 100)
    b += _d2_graft(f'M{mx + 26:.1f} {my + 8:.1f} L{mx + 2:.1f} {my:.1f}', 5)
    b += arrow(298, 152, mx + 30, my + 10) + T(302, 154, ['L carotid cannula:', 'bilateral'], 'f-s', 'start')
    tx, ty = _d2_pt(cx, cy, r + 40, 68)
    b += _d2_graft(f'M{tx + 24:.1f} {ty + 12:.1f} L{tx + 3:.1f} {ty + 2:.1f}', 5)
    b += T(300, 102, ['Subclavian cannula:', 'trilateral'], 'f-s', 'start')
    b += arrow(96, 320, 96, 196) + T(124, 372, 'Retrograde: perfuse up the SVC', 'f-s', 'start')
    b += box(420, 36, 290, 78, ['Deep arrest alone: 18 °C gives about', '30 to 40 min (TSRA); EACTS: safe up to', 'about 30 min, then injury rises'], 'b0', 'f-s')
    b += box(420, 122, 290, 96, ['Antegrade: arrest under 40 min,', 'unilateral or bilateral; over 40 min,', 'bilateral from the start. Better long-term', 'survival and neurology'], 'ok', 'f-s')
    b += box(420, 226, 290, 78, ['Retrograde via SVC: like antegrade in', 'hemiarch (EACTS); adds nothing to deep', 'arrest alone (TSRA ch. 75)'], 'b1', 'f-s')
    b += box(420, 312, 290, 62, ['Incomplete circle of Willis: trilateral', '(IIa, C). Bilateral NIRS with an', 'algorithm for desaturation (I, C)'], 'warn', 'f-s')
    b += T(12, 396, 'Femoral cannulation is retrograde arterial inflow, not retrograde cerebral perfusion.', 'f-s', 'start')
    return svg(406, b)


# ---------------------------------------------------------------- 10 spinal cord protection

def d2_spinal_cord():
    b = T(12, 20, 'Open thoraco-abdominal repair: protecting the cord', 'f-h', 'start')
    ax = 170
    b += _d2_vessel(f'M{ax} 40 L{ax} 344', 26)
    for y in range(56, 340, 18):
        b += line(ax - 30, y, ax - 13, y) + line(ax + 13, y, ax + 30, y)
    b += f'<rect x="{ax - 40}" y="182" width="80" height="94" rx="8" class="f-ok" style="opacity:.45"/>'
    b += T(ax - 46, 190, 'T8', 'f-h', 'end') + T(ax - 46, 278, 'L1', 'f-h', 'end')
    b += T(ax - 46, 222, ['Reattach', 'segmental', 'arteries'], 'f-s', 'end')
    for y in (96, 160):
        b += line(ax - 22, y, ax + 22, y, 'f-cut').replace('/>', ' style="stroke-width:5"/>')
    b += T(ax - 46, 132, ['Sequential', 'clamping'], 'f-s', 'end')
    b += box(226, 34, 92, 36, 'Left atrium', 'b1', 'f-s')
    b += box(226, 318, 92, 36, 'Femoral artery', 'b1', 'f-s')
    b += _d2_graft('M272 70 L272 318', 6)
    b += T(264, 150, ['Left heart', 'bypass:', 'distal', 'perfusion'], 'f-s', 'end')
    # spine and drain
    sx = 372
    for k in range(9):
        y = 40 + k * 34
        b += f'<rect x="{sx - 26}" y="{y}" width="34" height="28" rx="5" class="f-b0"/>'
    b += f'<rect x="{sx + 12}" y="40" width="22" height="300" rx="8" class="f-track"/>'
    b += f'<path d="M{sx + 23} 40 L{sx + 23} 236" class="f-nerve" style="stroke-width:6"/>'
    b += T(sx + 23, 30, 'Cord', 'f-s')
    b += f'<path d="M{sx + 24} 300 C{sx + 50} 300 {sx + 56} 330 {sx + 80} 336" class="f-l" style="stroke-width:2.5"/>'
    b += T(sx + 56, 300, ['Lumbar', 'CSF drain'], 'f-s', 'start')
    b += T(sx - 34, 280, ['CSF', 'space'], 'f-s', 'end')
    b += box(330, 372, 380, 34, 'Cord perfusion pressure = MAP minus CSF pressure', 'b1', 'f-h')
    b += box(492, 34, 218, 124, ['Drain (EACTS/STS 2024):', 'open TAAA (I, B); endovascular', 'at raised risk (IIa, C); total arch', 'at risk (IIa, C); not routine in', 'FET with limited cover (III, C)'], 'b0', 'f-s')
    b += box(492, 166, 218, 96, ['Also: evoked potentials (no', 'relaxant); 32 to 34 °C; patent', 'left subclavian; no anaemia;', 'stage long coverage'], 'ok', 'f-s')
    b += box(492, 270, 218, 94, ['New paraplegia: drain now', 'once coagulopathy corrected;', 'MAP over 100 mmHg, Hb over', '10 g/dL, volume, cardiovert'], 'warn', 'f-s')
    b += T(12, 372, ['Delayed deficit: up to 2 weeks, after a', 'haemodynamic insult. Permanent paraplegia', 'after open repair 1.5 to 5%.'], 'f-s', 'start')
    return svg(416, b)


# ---------------------------------------------------------------- 11 Kommerell measurements

def d2_kommerell():
    b = T(12, 20, 'Kommerell diverticulum: the three measurements', 'f-h', 'start')
    p = ('M180 40 L180 330 L260 330 L260 204 C292 202 322 176 322 136 L432 66 L416 44 L302 114 '
         'C288 104 272 102 260 102 L260 40 Z')
    b += f'<path d="{p}" class="f-b0"/>'
    b += T(220, 300, 'Descending', 'f-s') + T(220, 316, 'aorta', 'f-s')
    b += _d2_dim(300, 112, 324, 135) + T(294, 132, 'A orifice', 'f-h', 'end')
    b += _d2_dim(182, 160, 318, 160) + T(200, 182, 'B diverticulum', 'f-h', 'start') + T(200, 199, 'plus aorta (DAW)', 'f-h', 'start')
    b += _d2_dim(342, 82, 358, 108) + T(366, 122, ['C 1 cm beyond', 'the ostium'], 'f-h', 'start')
    b += T(420, 36, 'Aberrant subclavian', 'f-s', 'end')
    b += arrow(140, 262, 268, 206) + T(136, 268, ['Diverticulum', '(4th dorsal arch', 'remnant)'], 'f-s', 'end')
    # inset: course
    b += f'<rect x="466" y="36" width="244" height="226" rx="10" class="f-track"/>'
    b += T(588, 56, 'Course (axial, front at top)', 'f-s')
    b += '<circle cx="530" cy="126" r="26" class="f-b0"/>' + T(530, 131, 'Trachea', 'f-s')
    b += '<circle cx="530" cy="192" r="20" class="f-b1"/>' + T(530, 197, 'Oes.', 'f-s')
    for y, lab in ((84, 'In front of trachea 5%'), (161, 'Between 15%'), (226, 'Behind oesophagus 80%')):
        b += f'<circle cx="530" cy="{y}" r="6" class="f-warn"/>' + line(538, y, 576, y, 'f-grid')
        b += T(580, y + 4, lab.split(' ')[-1], 'f-h', 'start')
        b += T(580, y + 20, ' '.join(lab.split(' ')[:-1]), 'f-s', 'start')
    b += box(10, 344, 228, 78, ['Treatment may be considered', '(IIb, C) at A 30 mm or more,', 'B 50 mm or more, or C 30 mm', 'or more'], 'warn', 'f-s')
    b += box(246, 344, 228, 78, ['Symptoms (dysphagia commonest):', 'CTA or MRI (I, C) and treat', '(I, C). Asymptomatic: observe,', 'measuring several times'], 'b0', 'f-s')
    b += box(482, 344, 228, 78, ['Young, fit: open, thoracotomy', 'and carotid-subclavian bypass', '(I, C). Emergency or unfit:', 'hybrid closed-chest (I, C)'], 'ok', 'f-s')
    return svg(432, b)


# ---------------------------------------------------------------- 12 vascular rings

def _d2_ring_base(cx):
    out = '<ellipse cx="%d" cy="62" rx="22" ry="12" class="f-b1"/>' % (cx + 62)
    out += T(cx + 62, 66, 'PA', 'f-s')
    out += '<circle cx="%d" cy="56" r="16" class="f-lumen"/>' % cx + T(cx, 60, 'AA', 'f-s')
    out += '<circle cx="%d" cy="132" r="22" class="f-b0"/>' % cx + T(cx, 136, 'T', 'f-h')
    out += '<circle cx="%d" cy="188" r="17" class="f-b0"/>' % cx + T(cx, 192, 'O', 'f-h')
    out += '<circle cx="%d" cy="246" r="16" class="f-lumen"/>' % (cx + 26) + T(cx + 26, 250, 'DA', 'f-s')
    return out


def _d2_stub(x1, y1, x2, y2, lab, anchor='middle', dy=-6):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" class="f-vessel" style="stroke-width:7"/>'
            + T(x2 + (-4 if anchor == 'end' else 4 if anchor == 'start' else 0), y2 + dy, lab, 'f-s', anchor))


def _d2_cut(x, y):
    return (f'<line x1="{x - 9}" y1="{y - 9}" x2="{x + 9}" y2="{y + 9}" class="f-cut" style="stroke-width:3"/>'
            f'<line x1="{x - 9}" y1="{y + 9}" x2="{x + 9}" y2="{y - 9}" class="f-cut" style="stroke-width:3"/>')


def d2_vascular_rings():
    top = T(12, 18, "Axial schematic as on CT: front at top, patient's right on the left", 'f-s', 'start')
    b = ''
    # panel 1: double arch
    cx = 130
    right = f'M{cx - 12} 64 C{cx - 86} 80 {cx - 84} 214 {cx - 20} 228 C{cx - 4} 232 {cx + 8} 240 {cx + 12} 244'
    left = f'M{cx + 12} 64 C{cx + 62} 84 {cx + 60} 200 {cx + 36} 232'
    b += _d2_vessel(right, 18) + _d2_vessel(left, 9)
    b += _d2_ring_base(cx)
    b += _d2_stub(cx - 62, 92, cx - 96, 70, 'RC', 'end') + _d2_stub(cx - 70, 130, cx - 104, 130, 'RS', 'end')
    b += _d2_stub(cx + 44, 100, cx + 82, 100, 'LC', 'start', 4) + _d2_stub(cx + 50, 140, cx + 88, 140, 'LS', 'start', 4)
    b += f'<path d="M{cx + 72} 72 C{cx + 90} 140 {cx + 76} 220 {cx + 42} 244" class="f-dash" style="stroke-width:2.5"/>'
    b += _d2_cut(cx + 44, 220) + _d2_cut(cx + 82, 180)
    b += T(cx, 290, 'Double aortic arch', 'f-h')
    b += T(cx, 308, ['Right arch dominant 80%,', 'left 10%, balanced 10%'], 'f-s')
    # panel 2: RAA with aberrant LSA
    cx = 370
    right = f'M{cx - 12} 64 C{cx - 86} 80 {cx - 84} 214 {cx - 20} 228 C{cx - 4} 232 {cx + 8} 240 {cx + 12} 244'
    b += _d2_vessel(right, 16)
    b += _d2_ring_base(cx)
    b += f'<ellipse cx="{cx + 40}" cy="232" rx="14" ry="10" class="f-b1"/>'
    b += _d2_stub(cx + 48, 226, cx + 92, 196, 'LS', 'start', 4)
    b += _d2_stub(cx - 30, 66, cx - 34, 36, 'LC', 'end', 4)
    b += _d2_stub(cx - 62, 92, cx - 96, 70, 'RC', 'end') + _d2_stub(cx - 70, 130, cx - 104, 130, 'RS', 'end')
    b += f'<path d="M{cx + 72} 72 C{cx + 92} 140 {cx + 80} 200 {cx + 50} 226" class="f-dash" style="stroke-width:2.5"/>'
    b += _d2_cut(cx + 84, 150)
    b += T(cx + 92, 262, 'Kommerell', 'f-s', 'start')
    b += T(cx, 290, 'Right arch, aberrant left', 'f-h') + T(cx, 307, 'subclavian, left ligamentum', 'f-h')
    b += T(cx, 325, 'Ligamentum PA to descending aorta', 'f-s')
    # panel 3: mirror image
    cx = 600
    right = f'M{cx - 12} 64 C{cx - 86} 80 {cx - 84} 214 {cx - 20} 228 C{cx - 4} 232 {cx + 8} 240 {cx + 12} 244'
    b += _d2_vessel(right, 16)
    b += _d2_ring_base(cx)
    b += _d2_stub(cx - 16, 48, cx + 30, 26, 'L innominate', 'start', 4)
    b += _d2_stub(cx - 62, 92, cx - 96, 70, 'RC', 'end') + _d2_stub(cx - 70, 130, cx - 104, 130, 'RS', 'end')
    b += f'<path d="M{cx + 74} 74 C{cx + 94} 140 {cx + 80} 210 {cx + 42} 244" class="f-dash" style="stroke-width:2.5"/>'
    b += f'<path d="M{cx + 62} 50 C{cx + 60} 34 {cx + 48} 30 {cx + 36} 30" class="f-l" stroke-dasharray="2 3" style="stroke-width:2.5"/>'
    b += T(cx, 290, 'Right arch, mirror-image', 'f-h') + T(cx, 307, 'branching', 'f-h')
    b += T(cx, 325, 'Dotted: ligamentum to innominate', 'f-s')
    b += line(10, 340, 710, 340, 'f-grid')
    b += box(10, 350, 220, 96, ['Divide the lesser arch at its', 'junction with the descending', 'aorta, and the ligamentum;', 'thoracotomy on that side'], 'ok', 'f-s')
    b += box(250, 350, 220, 96, ['Left thoracotomy: divide the', 'ligamentum. Diverticulum may be', 'resected, subclavian moved to', 'the left carotid (not always)'], 'ok', 'f-s')
    b += box(490, 350, 220, 96, ['Ring only if the ligamentum', 'runs PA to descending aorta;', 'to the left innominate', '(commoner): no ring'], 'b1', 'f-s')
    b += T(12, 466, ['AA ascending aorta, DA descending aorta, PA pulmonary artery, T trachea, O oesophagus,',
                     'C carotid, S subclavian. Dashed: left ligamentum. Red X: divide.'], 'f-s', 'start')
    return svg(518, top + f'<g transform="translate(0 20)">{b}</g>')


# ---------------------------------------------------------------- 13 coarctation repairs

def _d2_coarc(cx, cy, r, bot, narrow=(True, True)):
    """Arch and descending aorta drawn as two walls, with an optional waist on each descending wall."""
    ro, ri = r + 11, r - 11
    yw = cy + 30
    out = ''
    for rad, side in ((ro, 0), (ri, 1)):
        x = cx + rad
        dx = -6 if side == 0 else 6
        d = f'M{cx - rad} {cy + 48} L{cx - rad} {cy} {_d2_arc(cx, cy, rad, 180, 0)} L{x} {yw - 10}'
        if narrow[side]:
            d += f' Q{x + dx} {yw} {x} {yw + 10}'
        else:
            d += f' L{x} {yw + 10}'
        d += f' L{x} {bot}'
        out += f'<path d="{d}" class="f-l" style="stroke-width:2.5"/>'
    lx, ly = _d2_pt(cx, cy, ro, 62)
    lx2, ly2 = _d2_pt(cx, cy, ro + 18, 62)
    out += f'<path d="M{lx:.1f} {ly:.1f} L{lx2:.1f} {ly2:.1f}" class="f-vessel" style="stroke-width:10"/>'
    return out, (lx, ly, lx2, ly2), yw


def d2_coarct_repairs():
    b = T(12, 20, 'Coarctation repair options', 'f-h', 'start')
    spec = [('Extended end-to-end', ['Excise, removing ductal tissue;', 'joined under the arch.', 'Neonates and infants']),
            ('Interposition tube graft', ['Adults (no growth, aneurysm in', 'children). ESC 2024: preferred', 'open option if stenting unsuitable']),
            ('Subclavian flap aortoplasty', ['Subclavian turned down over', 'the narrowing. Out of favour:', 'late limb complications']),
            ('Patch aortoplasty', ['Patch over the opened', 'narrowing. Risk of aneurysm', 'or pseudoaneurysm beside it']),
            ('Covered stent', ['First choice for native and', 're-coarctation in adults (ESC);', 'success: gradient under 10 mmHg']),
            ('Extra-anatomic bypass', ['Ascending to descending,', 'for re-repair at other cardiac', 'surgery (IIb, C)'])]
    for i, (h, txt) in enumerate(spec):
        x0 = 10 + (i % 3) * 236
        y0 = 30 + (i // 3) * 214
        cx, cy, r = x0 + 92, y0 + 82, 30
        bot = y0 + 146
        b += f'<rect x="{x0}" y="{y0}" width="226" height="204" rx="10" class="f-track"/>'
        if i == 0:
            w, ls, yw = _d2_coarc(cx, cy, r, bot, (False, False))
            p1 = _d2_pt(cx, cy, r - 11, 40)
            b += w + f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{cx + r + 11} {yw + 8}" class="f-cut" style="stroke-width:3"/>'
        elif i == 1:
            w, ls, yw = _d2_coarc(cx, cy, r, bot, (False, False))
            b += w + f'<rect x="{cx + r - 12}" y="{yw - 18}" width="24" height="40" rx="3" class="f-ok"/>'
            b += line(cx + r - 16, yw - 18, cx + r + 16, yw - 18, 'f-cut') + line(cx + r - 16, yw + 22, cx + r + 16, yw + 22, 'f-cut')
        elif i == 2:
            w, (lx, ly, lx2, ly2), yw = _d2_coarc(cx, cy, r, bot)
            b += w + f'<path d="M{lx - 6:.1f} {ly:.1f} Q{cx + r + 22} {cy + 4} {cx + r + 18} {yw + 18} L{cx + r + 8} {yw + 18} Q{cx + r + 10} {cy + 6} {lx - 14:.1f} {ly + 6:.1f} Z" class="f-ok"/>'
            b += _d2_cut(lx2, ly2)
        elif i == 3:
            w, ls, yw = _d2_coarc(cx, cy, r, bot, (False, True))
            b += w + f'<ellipse cx="{cx + r + 12}" cy="{yw}" rx="7" ry="20" class="f-b1"/>'
        elif i == 4:
            w, ls, yw = _d2_coarc(cx, cy, r, bot, (False, False))
            zz = f'M{cx + r - 9} {yw - 20}'
            for k in range(1, 9):
                zz += f' L{cx + r + (9 if k % 2 else -9)} {yw - 20 + k * 5}'
            b += w + f'<path d="{zz}" class="f-stent" style="stroke-width:2.5"/>'
            b += f'<rect x="{cx + r - 11}" y="{yw - 22}" width="22" height="44" class="f-stent"/>'
        else:
            w, ls, yw = _d2_coarc(cx, cy, r, bot)
            b += w + _d2_graft(f'M{cx - r - 11} {cy + 34} C{cx - r - 30} {cy + 64} {cx + r + 44} {cy + 70} {cx + r + 11} {yw + 34}', 7)
        b += T(x0 + 113, y0 + 18, h, 'f-h')
        b += T(x0 + 113, y0 + 160, txt, 'f-s')
    b += box(10, 462, 700, 44, ['Repair: hypertension with invasive peak-to-peak gradient over 20 mmHg (ESC, I, C), or hypertension with',
                                'over 50% narrowing against the aorta at the diaphragm (EACTS, IIa, C). Lifelong CT or MRI every 3 to 5 years.'], 'b0', 'f-s')
    return svg(516, b)


# ---- figs_D3.py
"""D3 drawings: aortic valve replacement, root enlargement, TAVI, valve-in-valve,
TEER, minimally invasive access, redo routes and mitral repair geometry."""



def _d3_num(x, y, n, cls='b1'):
    return (f'<circle cx="{x}" cy="{y}" r="11" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def _d3_lead(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="f-grid"/>'


def _d3_torso(cx, top=60, bot=400, half=96):
    return (f'<path d="M{cx - 34} {top} L{cx - half + 6} {top + 20} L{cx - half} {top + 110} '
            f'L{cx - half + 12} {bot - 80} L{cx - half + 20} {bot} L{cx + half - 20} {bot} '
            f'L{cx + half - 12} {bot - 80} L{cx + half} {top + 110} L{cx + half - 6} {top + 20} '
            f'L{cx + 34} {top} Z" class="f-b0"/>')


# ------------------------------------------------------------------ c4: AVR


def d3_avr_setup():
    """SAVR by sternotomy: cannulation, vent, cardioplegia, clamp and aortotomy; then the steps."""
    b = T(12, 22, 'Aortic valve replacement by sternotomy: set-up and steps', 'f-h', 'start')
    b += T(12, 42, "Front view, patient's right on the left. Arrangement schematic, not to scale.", 'f-s', 'start')
    # pulmonary trunk (drawn first, partly behind the aorta)
    b += '<path d="M282 300 L282 214 C282 198 324 194 336 210 L346 300 Z" class="f-b1"/>'
    b += T(314, 262, 'PA', 'f-s')
    # ventricles
    b += '<path d="M150 360 C150 312 210 296 270 298 C330 300 372 320 380 360 C390 420 340 470 270 488 C210 470 160 420 150 360 Z" class="f-b0"/>'
    b += T(286, 410, 'LV', 'f-h')
    # SVC, IVC and right atrium
    b += '<rect x="124" y="176" width="30" height="110" class="f-b1"/>'
    b += T(139, 170, 'SVC', 'f-s')
    b += '<rect x="124" y="380" width="30" height="70" class="f-b1"/>'
    b += T(139, 466, 'IVC', 'f-s')
    b += '<ellipse cx="140" cy="330" rx="46" ry="58" class="f-b1"/>'
    b += T(150, 336, 'RA', 'f-h')
    # ascending aorta and arch
    b += ('<path d="M222 304 L222 170 C222 118 300 104 348 126 L392 146 L392 176 L344 156 '
          'C306 140 256 146 256 178 L256 304 Z" class="f-lumen"/>')
    # A aortic cannula at proximal arch
    b += '<path d="M268 124 L300 74" class="f-l" style="stroke-width:5"/>'
    b += _d3_num(318, 74, 'A')
    # B cross-clamp
    b += '<rect x="210" y="190" width="58" height="9" rx="3" class="f-warn"/>'
    b += _d3_num(196, 194, 'B')
    # C antegrade cardioplegia below the clamp
    b += '<path d="M224 226 L196 216" class="f-l" style="stroke-width:3"/>'
    b += _d3_num(182, 222, 'C')
    # D aortotomy: transverse (red) and oblique alternative (dashed)
    b += line(222, 262, 256, 262, 'f-cut')
    b += '<path d="M226 244 L252 282" class="f-dash"/>'
    b += _d3_num(270, 262, 'D', 'warn')
    b += '<circle cx="232" cy="290" r="3.5" class="f-l"/><circle cx="246" cy="292" r="3.5" class="f-l"/>'
    # E two-stage venous cannula: RA appendage into the IVC
    b += '<path d="M62 278 C92 280 118 292 130 320 L138 440" class="f-l" style="stroke-width:5"/>'
    b += _d3_num(48, 278, 'E')
    # F retrograde cardioplegia via RA into the coronary sinus
    b += '<path d="M62 372 C96 374 140 368 166 362 L204 382" class="f-l" stroke-dasharray="4 3" style="stroke-width:2.5"/>'
    b += _d3_num(48, 372, 'F')
    # G LV vent through right superior pulmonary vein (posterior)
    b += '<path d="M62 226 C110 226 180 250 214 320 L248 380" class="f-l" stroke-dasharray="2 4" style="stroke-width:3"/>'
    b += _d3_num(48, 226, 'G')
    # legend
    leg = [('A', 'Aortic cannula in the proximal arch'), ('B', 'Cross-clamp'),
           ('C', 'Antegrade cardioplegia'),
           ('D', 'Transverse aortotomy 1 to 2 cm above the'),
           ('', 'ostia; oblique (dashed) if enlarging the root'),
           ('E', 'Two-stage venous cannula, RA into the IVC'),
           ('F', 'Retrograde cardioplegia, coronary sinus'),
           ('G', 'LV vent via the right superior pulmonary vein')]
    y = 74
    b += f'<rect x="410" y="54" width="300" height="{len(leg) * 20 + 14}" rx="9" class="f-b0"/>'
    for n, s in leg:
        if n:
            b += T(424, y, n, 'f-n', 'start')
        b += T(444, y, s, 'f-s', 'start')
        y += 20
    steps = [('1', 'Heparin 400 units/kg; ACT over 420 s'),
             ('2', 'Bypass; clamp; cold blood cardioplegia,'),
             ('', 'antegrade and retrograde; cool to 32°C'),
             ('3', 'Excise leaflets, debride the annulus'),
             ('', '(sharp, or a crushing clamp for calcium)'),
             ('4', 'Irrigate the LV: no debris left behind'),
             ('5', 'Size with sizers; avoid mismatch;'),
             ('', 'enlarge the root if needed'),
             ('6', 'Pledgeted horizontal mattress sutures,'),
             ('', 'ventricle to aorta, then the sewing ring'),
             ('7', 'Seat the valve supra-annular; tie'),
             ('8', 'Two-layer aortotomy closure; de-air;'),
             ('', 'clamp off; separate from bypass')]
    y0 = 54 + len(leg) * 20 + 30
    y = y0 + 24
    b += f'<rect x="410" y="{y0}" width="300" height="{len(steps) * 19 + 22}" rx="9" class="f-track"/>'
    for n, s in steps:
        if n:
            b += _d3_num(430, y - 4, n, 'b1')
        b += T(448, y, s, 'f-s', 'start')
        y += 19
    return svg(max(y + 10, 500), b)


def d3_avr_danger():
    """Surgeon's view of the annulus: what lies under each commissure; suture technique in section."""
    b = T(12, 22, 'Seating an aortic prosthesis: two structures to respect', 'f-h', 'start')
    b += T(12, 42, 'Annulus from above through the aortotomy, anterior at the top. Schematic, not to scale.', 'f-s', 'start')
    cx, cy, r = 170, 200, 104
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="f-b0"/>'
    import math
    pts = {}
    for name, ang in (('LN', 90), ('NR', -30), ('RL', 210)):
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        pts[name] = (x, y)
        b += line(cx, cy, round(x, 1), round(y, 1), 'f-l')
    b += T(cx, cy - 56, 'Right coronary', 'f-s') + T(cx - 52, cy + 30, 'Left', 'f-s') + T(cx - 52, cy + 46, 'coronary', 'f-s')
    b += T(cx + 54, cy + 30, 'Non-', 'f-s') + T(cx + 54, cy + 46, 'coronary', 'f-s')
    # danger arcs
    x, y = pts['LN']
    b += f'<path d="M{cx - 34} {cy + r - 6} Q{cx} {cy + r + 14} {cx + 34} {cy + r - 6}" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx, cy + r + 30, 1, 'warn')
    x, y = pts['NR']
    b += f'<path d="M{cx + 68} {cy - 80} Q{cx + r + 14} {cy - 56} {cx + r + 2} {cy - 18}" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx + r + 26, cy - 62, 2, 'warn')
    b += box(30, 352, 300, 56, ['1 Below the left to non-coronary', 'commissure: anterior mitral leaflet'], 'warn', 'f-s')
    b += box(30, 416, 300, 56, ['2 Below the non-coronary to right', 'commissure: conduction tissue'], 'warn', 'f-s')
    b += T(180, 492, 'Deep sutures at 2 cause heart block.', 'f-s')
    # section of suture technique on the right
    ox = 380
    b += T(ox + 10, 74, 'In section: pledgeted horizontal mattress', 'f-h', 'start')
    # aortic wall above, LV below, annulus as a shelf
    b += f'<rect x="{ox + 10}" y="96" width="320" height="120" rx="6" class="f-lumen"/>'
    b += T(ox + 250, 118, 'Aortic side', 'f-s')
    b += f'<rect x="{ox + 10}" y="236" width="320" height="120" rx="6" class="f-lumen"/>'
    b += T(ox + 250, 338, 'Ventricular side', 'f-s')
    b += f'<rect x="{ox + 10}" y="216" width="190" height="20" class="f-b1"/>'
    b += T(ox + 105, 231, 'Annulus', 'f-s')
    # sewing ring and valve sitting above annulus
    b += f'<rect x="{ox + 30}" y="180" width="150" height="20" rx="8" class="f-ok"/>'
    b += T(ox + 105, 194, 'Sewing ring', 'f-s')
    b += f'<path d="M{ox + 40} 180 L{ox + 60} 128 L{ox + 160} 128 L{ox + 170} 180" class="f-ok" style="opacity:.6"/>'
    b += T(ox + 110, 160, 'Valve', 'f-s')
    # pledget below annulus and the mattress suture
    b += f'<rect x="{ox + 44}" y="238" width="122" height="10" rx="3" class="f-warn"/>'
    b += T(ox + 105, 266, 'Pledget', 'f-s')
    b += (f'<path d="M{ox + 52} 238 L{ox + 52} 180 M{ox + 158} 238 L{ox + 158} 180 '
          f'M{ox + 52} 180 C{ox + 52} 150 {ox + 40} 140 {ox + 36} 110 M{ox + 158} 180 C{ox + 158} 150 {ox + 170} 140 {ox + 174} 110" class="f-l"/>')
    b += T(ox + 196, 156, 'Tied above the ring', 'f-s', 'start')
    b += box(ox + 10, 372, 320, 100, ['Needle passes ventricle to aorta through the', 'annulus, then through the sewing ring;', 'the valve is seated above the annulus', '(supra-annular) and the sutures tied'], 'b0', 'f-s')
    return svg(504, b)


def d3_avr_sizing():
    """Sizing the annulus and the decision to enlarge."""
    b = T(12, 22, 'Sizing and prosthesis-patient mismatch: when to enlarge the root', 'f-h', 'start')
    b += box(160, 36, 400, 44, ['Excise, debride, irrigate; size the annulus with sizers'], 'b1', 'f-s')
    b += arrow(360, 80, 360, 96)
    b += box(110, 98, 500, 58, ['Small annulus: sizer 21 mm or less, or CT annulus area', 'about 430 mm² or less. Predict the indexed effective', 'orifice area (EOA/BSA) of the largest valve that fits'], 'b0', 'f-s')
    b += arrow(220, 156, 120, 178) + arrow(360, 156, 360, 178) + arrow(500, 156, 600, 178)
    b += box(10, 180, 220, 58, ['Over 0.85 cm²/m²', 'implant that valve'], 'ok', 'f-s')
    b += box(250, 180, 220, 58, ['0.85 or less', 'moderate mismatch'], 'b1', 'f-s')
    b += box(490, 180, 220, 58, ['0.65 or less', 'severe mismatch'], 'warn', 'f-s')
    b += T(12, 258, 'Lower cut-offs apply when BMI is 30 or more.', 'f-s', 'start')
    b += arrow(360, 238, 360, 280) + arrow(600, 238, 600, 280)
    b += T(12, 296, 'Root enlargement: gain in valve size', 'f-h', 'start')
    rows = [('Nicks', 'about 1', 'Non-coronary sinus into the curtain', 'b0'),
            ('Manouguian', '1 to 2', 'L/N commissure into AML and LA roof', 'b0'),
            ('Y-incision', '3 to 4 *', 'L/N commissure, Y under both annuli', 'ok'),
            ('Konno', '2 to 4', 'Right sinus into septum; tunnel obstruction', 'b0')]
    y = 308
    for name, gain, how, cls in rows:
        b += f'<rect x="10" y="{y}" width="700" height="32" rx="7" class="f-{cls}"/>'
        b += T(22, y + 21, name, 'f-n', 'start') + T(170, y + 21, gain, 'f-n', 'start')
        b += T(270, y + 21, how, 'f-s', 'start')
        y += 38
    b += T(12, y + 10, '* 3 to 4 sizes in the course table; the TSRA chapter and the operative table give 2 to 3.', 'f-s', 'start')
    b += box(10, y + 24, 340, 74, ['Alternatives: supra-annular or stentless', 'prosthesis, sutureless valve, full root', 'replacement, TAVI'], 'b0', 'f-s')
    b += box(370, y + 24, 340, 74, ['Younger patients: aim for a bioprosthesis', 'of 23 mm or larger so that a later', 'valve-in-valve is feasible'], 'b1', 'f-s')
    return svg(y + 110, b)


def _d3_root_panel(ox, oy, which):
    """Unrolled aortic root seen from inside, cut through the left to right commissure.
    Order left to right: left sinus, non-coronary sinus, right sinus."""
    w, sw = 330, 110
    top = oy + 14
    hi, ctl = top + 10, top + 150          # commissure level; Bezier control (nadir at top + 80)
    base = top + 124                        # lower edge of the curtain
    sc = ''.join(f' Q{ox + i * sw + sw / 2} {ctl} {ox + (i + 1) * sw} {hi}' for i in range(3))
    b = ''
    # sinus wall above the hinge line
    b += f'<path d="M{ox} {top} L{ox + w} {top} L{ox + w} {hi}' + ''.join(
        f' Q{ox + (2 - i) * sw + sw / 2} {ctl} {ox + (2 - i) * sw} {hi}' for i in range(3)) + ' Z" class="f-lumen"/>'
    # curtain (under L and N) and septum (under R) below the hinge line
    b += (f'<path d="M{ox} {hi} Q{ox + sw / 2} {ctl} {ox + sw} {hi} Q{ox + sw * 1.5} {ctl} {ox + 2 * sw} {hi} '
          f'L{ox + 2 * sw} {base} L{ox} {base} Z" class="f-b1"/>')
    b += f'<path d="M{ox + 2 * sw} {hi} Q{ox + 2.5 * sw} {ctl} {ox + w} {hi} L{ox + w} {top + 176} L{ox + 2 * sw} {top + 176} Z" class="f-b0"/>'
    b += f'<path d="M{ox} {hi}{sc}" class="f-l" style="stroke-width:2.5"/>'
    for i in range(1, 3):
        b += line(ox + i * sw, top, ox + i * sw, hi, 'f-l')
    b += T(ox + 55, top + 28, 'L', 'f-h') + T(ox + 146, top + 28, 'N', 'f-h') + T(ox + 275, top + 28, 'R', 'f-h')
    b += f'<circle cx="{ox + 40}" cy="{top + 50}" r="5" class="f-l"/>'
    b += f'<circle cx="{ox + 262}" cy="{top + 50}" r="5" class="f-l"/>'
    b += T(ox + 78, top + 118, 'Curtain', 'f-s')
    # anterior mitral leaflet below the curtain
    b += f'<path d="M{ox + 30} {base} L{ox + 200} {base} Q{ox + 115} {base + 70} {ox + 30} {base} Z" class="f-ok"/>'
    b += T(ox + 150, base + 20, 'AML', 'f-s')
    b += T(ox + 256, top + 140, 'Septum', 'f-s') + T(ox + 256, top + 156, 'and RVOT', 'f-s')
    # trigones
    b += f'<circle cx="{ox + 34}" cy="{top + 106}" r="5" class="f-warn"/><circle cx="{ox + 206}" cy="{top + 106}" r="5" class="f-warn"/>'
    b += T(ox + 4, base + 52, 'LA roof lies behind', 'f-s', 'start')
    cut = 'class="f-cut" style="stroke-width:3.5"'
    if which == 'nicks':
        b += f'<path d="M{ox + 165} {top} L{ox + 165} {base - 8}" {cut}/>'
    elif which == 'mano':
        b += f'<path d="M{ox + sw} {top} L{ox + sw} {base + 34}" {cut}/>'
    elif which == 'y':
        b += f'<path d="M{ox + sw} {top} L{ox + sw} {top + 96} L{ox + 42} {top + 104} M{ox + sw} {top + 96} L{ox + 198} {top + 104}" {cut}/>'
    elif which == 'konno':
        b += f'<path d="M{ox + 292} {top} L{ox + 292} {top + 170}" {cut}/>'
    return b


def d3_root_unrolled():
    """Root enlargement: the root opened flat, with how deep each incision goes."""
    b = T(12, 22, 'Root enlargement: how far down each incision goes', 'f-h', 'start')
    b += T(12, 42, 'Root opened flat and seen from inside, cut through the left to right commissure. Arrangement schematic.', 'f-s', 'start')
    panels = [('nicks', 'Nicks', ['Middle of the non-coronary sinus, across', 'the annulus into the curtain; stops short', 'of the anterior mitral leaflet. About 1 size']),
              ('mano', 'Manouguian', ['L/N commissure, across the curtain into', 'the anterior mitral leaflet and LA roof.', '1 to 2 sizes. Watch: MR, bleeding, LA closure']),
              ('y', 'Y-incision (Yang)', ['L/N commissure into the curtain, then a Y', 'under both annuli towards each trigone;', 'mitral valve and LA not entered. Rectangular patch']),
              ('konno', 'Konno-Rastan', ['Right sinus left of the right coronary ostium,', 'into septum and RVOT; two patches. Watch:', 'heart block, septal perforator, residual VSD'])]
    for i, (k, name, txt) in enumerate(panels):
        ox = 16 + (i % 2) * 360
        oy = 60 + (i // 2) * 300
        b += f'<rect x="{ox - 8}" y="{oy - 6}" width="346" height="290" rx="10" class="f-track"/>'
        b += T(ox + 4, oy + 10, name, 'f-h', 'start')
        b += _d3_root_panel(ox, oy + 10, k)
        b += T(ox + 4, oy + 230, txt, 'f-s', 'start')
    b += T(12, 676, 'Red line: the incision. Small red rings: fibrous trigones. Black rings in the sinuses: coronary ostia.', 'f-s', 'start')
    return svg(690, b)


# ------------------------------------------------------------------ c20: TAVI


def d3_tavi_access():
    """TAVI access routes on a front-view outline."""
    b = T(12, 22, 'TAVI access routes', 'f-h', 'start')
    b += T(12, 42, "Front view, patient's right on the left. Arrangement schematic.", 'f-s', 'start')
    cx = 150
    b += f'<rect x="{cx - 24}" y="56" width="48" height="34" class="f-b0"/>'
    b += _d3_torso(cx, 86, 520, 116)
    v = 'class="f-l" style="stroke-width:5"'
    # IVC (dashed) to the patient's right of the aorta, iliac vein to the groin
    b += f'<path d="M{cx - 28} 260 L{cx - 2} 420 L{cx - 20} 520" class="f-dash" style="stroke-width:3"/>'
    # aorta: ascending, arch, descending, iliac and femoral arteries
    b += f'<path d="M{cx} 214 L{cx} 160 C{cx} 128 {cx + 40} 128 {cx + 40} 160 L{cx + 40} 420" {v}/>'
    b += f'<path d="M{cx + 40} 420 L{cx + 8} 480 L{cx + 2} 520 M{cx + 40} 420 L{cx + 72} 480 L{cx + 78} 520" {v}/>'
    # arch branches
    b += f'<path d="M{cx + 8} 140 L{cx - 8} 116 L{cx - 10} 60 M{cx - 8} 116 L{cx - 96} 126" {v}/>'
    b += f'<path d="M{cx + 22} 134 L{cx + 22} 60 M{cx + 34} 140 L{cx + 104} 126" {v}/>'
    # heart drawn over the descending aorta
    b += f'<path d="M{cx - 46} 250 C{cx - 46} 214 {cx - 10} 204 {cx + 24} 208 C{cx + 70} 214 {cx + 84} 260 {cx + 66} 296 L{cx + 40} 310 C{cx} 300 {cx - 46} 290 {cx - 46} 250 Z" class="f-b1"/>'
    b += T(cx + 10, 262, 'Heart', 'f-s')
    # transcaval crossing
    b += f'<line x1="{cx - 6}" y1="380" x2="{cx + 34}" y2="380" class="f-cut" marker-end="url(#ah)" style="stroke-width:2.5"/>'
    b += T(cx - 52, 420, 'IVC', 'f-s') + T(cx + 52, 360, 'Aorta', 'f-s', 'start')
    nums = [(cx - 16, 500, 1, 'ok'), (cx + 46, 70, 2, 'b1'), (cx + 112, 146, 3, 'b1'),
            (cx - 34, 108, 4, 'b1'), (cx - 22, 380, 5, 'b1'), (cx + 86, 310, 6, 'warn'), (cx - 22, 176, 7, 'warn')]
    for x, y, n, c in nums:
        b += _d3_num(x, y, n, c)
    rows = [('1', 'Transfemoral', 'By far the commonest; TAVI benefit largely confined to it', 'ok'),
            ('2', 'Transcarotid', 'Alternative when femoral access is unsuitable', 'b0'),
            ('3', 'Transaxillary or transsubclavian', 'Alternative; also used for valve-in-valve', 'b0'),
            ('4', 'Transinnominate', 'Listed by ESC 2025 among non-transfemoral routes', 'b0'),
            ('5', 'Transcaval', 'Femoral vein to IVC, across into the aorta; specialised centres', 'b0'),
            ('6', 'Transapical', 'Fallen out of favour: higher morbidity and mortality', 'warn'),
            ('7', 'Transaortic', 'Less commonly performed in the current era', 'warn')]
    y = 56
    for n, name, txt, c in rows:
        b += f'<rect x="310" y="{y}" width="400" height="46" rx="8" class="f-{c}"/>'
        b += _d3_num(328, y + 23, n, c)
        b += T(346, y + 19, name, 'f-n', 'start') + T(346, y + 37, txt, 'f-s', 'start')
        y += 52
    b += box(310, y + 4, 400, 96, ['Femoral checks on CT: common femoral diameter', '5.0 to 5.5 mm (as printed). Unfavourable:',
                                   'tortuosity (worse with calcium on the outer curve),', 'calcification over 270°, common iliac calcium'], 'b1', 'f-s')
    b += T(12, 548, 'Non-transfemoral TAVI: ESC 2025 IIa B when unsuitable for both surgery and transfemoral access.', 'f-s', 'start')
    return svg(562, b)


def d3_tavi_steps():
    """TAVI: lines in, then the deployment sequence."""
    b = T(12, 22, 'Transfemoral TAVI: lines in, then the sequence', 'f-h', 'start')
    b += T(12, 42, 'Drawn from the procedure steps in the TSRA chapters; the groin sides are interchangeable.', 'f-s', 'start')
    b += box(10, 56, 226, 78, ['Femoral artery, device side', 'Large sheath; closure devices', 'placed before dilating'], 'b1', 'f-s')
    b += box(247, 56, 226, 78, ['Other femoral artery', '6 Fr sheath; pigtail in the', 'sinus for aortography'], 'b0', 'f-s')
    b += box(484, 56, 226, 78, ['Femoral (or jugular) vein', 'Pacing wire in the RV: rapid', 'pacing; back-up for all'], 'b0', 'f-s')
    steps = [('Heparin', ['70 U/kg after access and before entering the arch; ACT 250 to 300 s']),
             ('View', ['Aortogram; co-planar view of all three sinus nadirs (predicted from CT)']),
             ('Cross', ['Cross the valve with a wire; catheter in the LV: simultaneous LV and aortic pressures',
                        'confirm the gradient; pigtail wire in the LV, and the valve advanced over it']),
             ('Protect', ['Coronary guidewire in the at-risk coronary if high risk;',
                          'pre-dilate (e.g. 20 mm balloon) if the device may not be tolerated across the valve']),
             ('Deploy', ['Balloon-expandable or self-expanding, under angiography;',
                         'rapid pacing to prevent displacement']),
             ('Check', ['Aortogram and TEE: paravalvular leak, AR, effusion. Leak more than mild: wait 5 to 10 min;',
                        'then post-dilate, second valve, vascular plug, or surgery if truly low risk'])]
    y = 150
    for i, (h, t) in enumerate(steps):
        hh = 22 + 17 * len(t)
        b += f'<rect x="10" y="{y}" width="700" height="{hh}" rx="8" class="f-b0"/>'
        b += _d3_num(30, y + hh / 2, i + 1, 'b1')
        b += T(50, y + hh / 2 + 5, h, 'f-n', 'start')
        b += T(120, y + hh / 2 - (len(t) - 1) * 8.5 + 5, t, 'f-s', 'start')
        y += hh + 8
    return svg(y + 4, b)


def _d3_root_lax(ox, oy, s=1.0, ostium=True):
    """Aortic root in long axis: LVOT below, annulus, sinuses, STJ, ascending aorta.
    Returns (svg, annulus y, centre x). Width about 220*s."""
    cx = ox + 110 * s
    ann = oy + 200 * s
    stj = oy + 100 * s

    def P(x, y):
        return f'{ox + x * s:.1f} {oy + y * s:.1f}'
    left = f'M{P(56, 270)} L{P(52, 200)} C{P(14, 186)} {P(14, 112)} {P(60, 100)} L{P(60, 10)}'
    right = f'M{P(164, 270)} L{P(168, 200)} C{P(206, 186)} {P(206, 112)} {P(160, 100)} L{P(160, 10)}'
    b = (f'<path d="M{P(56, 270)} L{P(52, 200)} C{P(14, 186)} {P(14, 112)} {P(60, 100)} L{P(60, 10)} '
         f'L{P(160, 10)} L{P(160, 100)} C{P(206, 112)} {P(206, 186)} {P(168, 200)} L{P(164, 270)} Z" class="f-lumen" style="stroke:none"/>')
    b += f'<path d="{left}" class="f-l" style="stroke-width:2"/><path d="{right}" class="f-l" style="stroke-width:2"/>'
    b += f'<line x1="{ox + 40 * s:.1f}" y1="{ann:.1f}" x2="{ox + 180 * s:.1f}" y2="{ann:.1f}" class="f-dash"/>'
    if ostium:
        b += f'<path d="M{P(26, 140)} L{P(0, 132)} M{P(28, 156)} L{P(0, 150)}" class="f-l" style="stroke-width:2"/>'
    return b, ann, cx


def d3_tavi_valves():
    """Balloon-expandable intra-annular against self-expanding supra-annular valves."""
    b = T(12, 22, 'Balloon-expandable and self-expanding TAVI valves', 'f-h', 'start')
    b += T(12, 42, 'Root in long axis; dashed line is the annulus. Arrangement schematic, not to scale.', 'f-s', 'start')
    for i, kind in enumerate(('be', 'se')):
        ox, oy = 70 + i * 360, 56
        r, ann, cx = _d3_root_lax(ox, oy, 1.0)
        b += r
        if kind == 'be':
            b += f'<rect x="{ox + 58}" y="{ann - 26}" width="104" height="42" rx="3" class="f-stent"/>'
            b += f'<path d="M{ox + 62} {ann - 22} L{cx} {ann - 4} L{ox + 158} {ann - 22}" class="f-l" style="stroke-width:2.5"/>'
            b += T(cx, oy + 290, 'SAPIEN 3 Ultra: intra-annular, short frame', 'f-n')
            # coronary height
            b += f'<line x1="{ox + 8}" y1="{ann}" x2="{ox + 8}" y2="{oy + 160}" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
            b += T(cx, oy + 310, 'Arrow: coronary height, usual minimum 10 mm', 'f-s')
        else:
            b += (f'<path d="M{ox + 60} {ann + 18} L{ox + 58} {ann - 20} C{ox + 70} {oy + 150} {ox + 72} {oy + 120} {ox + 64} {oy + 100} '
                  f'L{ox + 50} {oy + 24} L{ox + 170} {oy + 24} L{ox + 156} {oy + 100} C{ox + 148} {oy + 120} {ox + 150} {oy + 150} '
                  f'{ox + 162} {ann - 20} L{ox + 160} {ann + 18} Z" class="f-stent"/>')
            b += f'<path d="M{ox + 70} {oy + 112} L{cx} {oy + 132} L{ox + 150} {oy + 112}" class="f-l" style="stroke-width:2.5"/>'
            b += T(cx, oy + 290, 'Evolut PRO+: supra-annular, tall frame', 'f-n')
    rows = [('', 'Balloon-expandable', 'Self-expanding'),
            ('Sized on', 'Annular area', 'Annular perimeter'),
            ('Steerable / recapturable', 'Yes / no', 'No / yes'),
            ('Pacemaker, low-risk trials', '6.5%', '17.4%'),
            ('Paravalvular leak', 'Less', 'More (low-risk trials)'),
            ('Annular rupture', 'Slightly more (0.2%)', ''),
            ('Gradients (supra-annular)', '', 'Better gradients, less severe PPM'),
            ('Later PCI', 'Lower frame may make it easier', '')]
    y = 384
    for j, (a, c1, c2) in enumerate(rows):
        cls = 'f-b1' if j == 0 else 'f-b0'
        b += f'<rect x="10" y="{y}" width="700" height="28" rx="6" class="{cls}"/>'
        b += T(20, y + 19, a, 'f-n' if a else 'f-s', 'start')
        b += T(250, y + 19, c1, 'f-n' if j == 0 else 'f-s', 'start')
        b += T(480, y + 19, c2, 'f-n' if j == 0 else 'f-s', 'start')
        y += 32
    b += box(10, y + 6, 700, 78, ['Undersize for: severe annular calcium (rupture); narrow root, shallow sinus, low ostia or bulky',
                                  'leaflets (coronary occlusion); porcelain aorta. Oversize by calcium burden: minimal 10%,',
                                  'moderate 5%, severe true size'], 'warn', 'f-s')
    b += T(12, y + 104, 'SMART (annulus 430 mm² or less): 12-month valve dysfunction 9.4% self-expanding, 41.6% balloon-expandable.', 'f-s', 'start')
    return svg(y + 118, b)


def d3_tavi_complications():
    """Where TAVI complications arise, and what to do."""
    b = T(12, 22, 'TAVI complications: where they arise and what to do', 'f-h', 'start')
    b += T(12, 42, 'Root in long axis with a deployed valve. Arrangement schematic.', 'f-s', 'start')
    ox, oy = 20, 70
    r, ann, cx = _d3_root_lax(ox, oy, 1.0)
    b += r
    # deployed frame
    b += f'<rect x="{ox + 58}" y="{ann - 30}" width="104" height="52" rx="3" class="f-stent"/>'
    # displaced native leaflet towards the ostium
    b += f'<path d="M{ox + 54} {ann - 2} L{ox + 40} {oy + 150}" class="f-l" style="stroke-width:4"/>'
    # paravalvular gap
    b += f'<path d="M{ox + 162} {ann - 10} C{ox + 176} {ann - 20} {ox + 180} {ann - 40} {ox + 176} {ann - 60}" class="f-cut" stroke-dasharray="3 3"/>'
    # implant depth below annulus
    b += f'<line x1="{ox + 110}" y1="{ann}" x2="{ox + 110}" y2="{ann + 22}" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    marks = [(ox + 196, ann + 6, 1), (ox - 4, oy + 120, 2), (ox + 130, ann + 50, 3), (ox + 200, ann - 50, 4),
             (ox + 110, oy + 50, 5), (ox + 186, oy + 30, 6)]
    for x, y, n in marks:
        b += _d3_num(x, y, n, 'warn')
    b += T(ox + 110, oy + 300, ['7 Distal vascular injury', 'at the access site'], 'f-s')
    items = [('1 Annular rupture (oversizing)', ['New effusion, shunt, MR, TR or conduction defect. Stable haematoma:',
                                                  'reverse heparin, drain, CT later. Unstable: emergency surgery']),
             ('2 Coronary obstruction', ['Usually the displaced native leaflet. PCI; CPR or ECMO to bridge;',
                                         'rarely CABG and explant. Wire the coronary first if high risk']),
             ('3 AV block', ['Oversizing 16% or more, implant depth over 5 mm (arrow),',
                             'pre-existing RBBB, QRS over 140 ms. EP review if QRS',
                             'over 200 ms or wider by more than 40 ms']),
             ('4 Paravalvular leak (undersizing)', ['More than mild: wait 5 to 10 min; post-dilate, second valve,',
                                                    'vascular plugs, or SAVR if truly low risk']),
             ('5 Migration or embolisation', ['High risk: snare and park in the aorta. Lower risk: surgical',
                                              'extraction and SAVR']),
             ('6 Aortic injury proximal to the left subclavian', ['Dissection or rupture; surgery depends on comorbidity']),
             ('7 Distal vascular injury', ['Keep the wire across. Iliac: covered stent often possible.',
                                           'Femoral: usually surgical patch angioplasty'])]
    y = 56
    for h, t in items:
        hh = 24 + 17 * len(t)
        b += f'<rect x="260" y="{y}" width="450" height="{hh}" rx="8" class="f-b0"/>'
        b += T(272, y + 18, h, 'f-n', 'start') + T(272, y + 36, t, 'f-s', 'start')
        y += hh + 6
    return svg(y + 6, b)


def d3_viv_hazards():
    """Valve-in-valve: the old valve's true inner diameter, coronary obstruction and sinus sequestration."""
    b = T(12, 22, 'Valve-in-valve: three things that go wrong', 'f-h', 'start')
    b += T(12, 42, 'Root in long axis; old surgical valve grey, new transcatheter frame blue dashed. Arrangement schematic.', 'f-s', 'start')
    titles = [('1 Mismatch', ['Old valve inner diameter is', 'the "annulus". Under 20 mm:', 'high gradients, worse results;', 'consider redo SAVR with', 'root enlargement']),
              ('2 Coronary obstruction', ['Old leaflet pushed out as a', 'neo-skirt against the ostium.', 'Low coronary height, narrow', 'sinus, stentless or externally', 'mounted leaflets, high old valve']),
              ('3 Sinus sequestration', ['Neo-skirt reaches the', 'sinotubular junction in a', 'narrow aorta and seals the', 'sinus. TAV-in-TAV: worst with', 'supra-annular high neo-skirt'])]
    for i in range(3):
        ox, oy = 12 + i * 236, 60
        s = 0.92
        r, ann, cx = _d3_root_lax(ox, oy, s)
        b += r
        # old surgical valve: sewing ring and posts
        b += f'<rect x="{ox + 44 * s:.1f}" y="{ann - 8:.1f}" width="{132 * s:.1f}" height="14" rx="6" class="f-b0"/>'
        post_top = oy + (110 if i == 2 else 140) * s
        b += f'<path d="M{ox + 62 * s:.1f} {ann - 8:.1f} L{ox + 62 * s:.1f} {post_top:.1f} M{ox + 158 * s:.1f} {ann - 8:.1f} L{ox + 158 * s:.1f} {post_top:.1f}" class="f-l" style="stroke-width:4;opacity:.5"/>'
        # new frame
        top_f = oy + (40 if i == 2 else 120) * s
        b += f'<rect x="{ox + 66 * s:.1f}" y="{top_f:.1f}" width="{88 * s:.1f}" height="{ann + 10 - top_f:.1f}" rx="3" class="f-stent"/>'
        if i == 0:
            b += f'<line x1="{ox + 66 * s:.1f}" y1="{ann + 26:.1f}" x2="{ox + 154 * s:.1f}" y2="{ann + 26:.1f}" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
        if i == 1:
            b += f'<path d="M{ox + 62 * s:.1f} {post_top:.1f} L{ox + 30 * s:.1f} {oy + 134 * s:.1f}" class="f-cut" style="stroke-width:4"/>'
        if i == 2:
            b += f'<path d="M{ox + 62 * s:.1f} {post_top:.1f} L{ox + 62 * s:.1f} {oy + 98 * s:.1f} M{ox + 158 * s:.1f} {post_top:.1f} L{ox + 158 * s:.1f} {oy + 98 * s:.1f}" class="f-cut" style="stroke-width:4"/>'
        h, t = titles[i]
        b += T(ox + 4, oy + 304, h, 'f-h', 'start')
        b += T(ox + 4, oy + 324, t, 'f-s', 'start')
    y = 480
    b += box(10, y, 345, 96, ['Before: TEE (a paravalvular leak is not', 'treated by valve-in-valve); CT; old note', 'for valve type, size, inner diameter,', 'markers, leaflets and strut height'], 'b1', 'f-s')
    b += box(365, y, 345, 96, ['High risk of severe PPM or coronary', 'obstruction: redo SAVR may be better.', 'Leaflet modification (BASILICA, LAMPOON)', 'and valve fracture: expert centres'], 'warn', 'f-s')
    b += T(12, y + 118, 'At the first TAVI, plan the second: device, neo-skirt height, commissural alignment, implant depth.', 'f-s', 'start')
    return svg(y + 132, b)


def d3_teer():
    """Mitral edge-to-edge repair: route and the double orifice, with anatomy criteria."""
    b = T(12, 22, 'Transcatheter edge-to-edge repair (TEER)', 'f-h', 'start')
    b += T(12, 42, 'Left: route (transfemoral transseptal, as given for PASCAL). Right: valve from the atrium. Arrangement schematic.', 'f-s', 'start')
    # left panel: atria and LV with catheter
    b += '<ellipse cx="110" cy="150" rx="70" ry="62" class="f-b1"/>' + T(80, 140, 'RA', 'f-h')
    b += '<ellipse cx="250" cy="140" rx="70" ry="58" class="f-b1"/>' + T(276, 112, 'LA', 'f-h')
    b += '<path d="M190 210 C190 260 210 330 250 360 C300 330 320 260 316 200 Z" class="f-b0"/>' + T(262, 300, 'LV', 'f-h')
    b += '<line x1="180" y1="100" x2="180" y2="190" class="f-l" style="stroke-width:3"/>'
    b += T(180, 74, 'Septum (ring: puncture site)', 'f-s')
    b += '<rect x="96" y="210" width="28" height="140" class="f-b1"/>' + T(110, 368, 'IVC from the femoral vein', 'f-s')
    b += '<path d="M110 350 L110 170 C110 150 140 140 180 150 C220 160 236 180 246 204" class="f-l" style="stroke-width:3"/>'
    b += '<circle cx="180" cy="150" r="6" class="f-warn"/>'
    # mitral leaflets and clip
    b += '<path d="M200 204 L240 222 M300 200 L254 222" class="f-l" style="stroke-width:3"/>'
    b += '<rect x="240" y="206" width="14" height="26" rx="3" class="f-ok"/>'
    # right panel: en face valve with clip creating double orifice
    vx, vy = 520, 160
    b += f'<ellipse cx="{vx}" cy="{vy}" rx="130" ry="84" class="f-b0"/>'
    b += f'<path d="M{vx - 110} {vy} C{vx - 60} {vy - 30} {vx - 20} {vy + 4} {vx} {vy} C{vx + 20} {vy + 4} {vx + 60} {vy - 30} {vx + 110} {vy}" class="f-l" style="stroke-width:2"/>'
    b += f'<path d="M{vx - 110} {vy} C{vx - 60} {vy + 34} {vx - 20} {vy + 4} {vx} {vy} C{vx + 20} {vy + 4} {vx + 60} {vy + 34} {vx + 110} {vy}" class="f-l" style="stroke-width:2"/>'
    b += f'<rect x="{vx - 9}" y="{vy - 18}" width="18" height="36" rx="3" class="f-ok"/>'
    b += T(vx, vy - 96, 'Anterior leaflet', 'f-s') + T(vx, vy + 108, 'Posterior leaflet', 'f-s')
    b += T(vx - 66, vy + 6, 'orifice', 'f-s') + T(vx + 66, vy + 6, 'orifice', 'f-s')
    b += T(vx, vy + 132, ['Clip joins the leaflets at the jet,', 'like an Alfieri stitch: a double orifice'], 'f-s')
    b += box(10, 400, 345, 132, ['Ideal anatomy', 'Central jet (central two-thirds)', 'Valve area over 4 cm²',
                                 'Posterior leaflet mobile length over 10 mm', 'Flail gap under 10 mm, width under 15 mm',
                                 'No calcium in the grasping zone'], 'ok', 'f-s')
    b += box(365, 400, 345, 132, ['Contraindications', 'Active endocarditis; rheumatic valve', 'Valve area under 3.5 cm²; calcified, stenotic',
                                  'Multiple jets; posterior leaflet under 5 mm', 'Intracardiac thrombus', 'Caval interruption; large septal occluder'], 'warn', 'f-s')
    b += T(12, 556, ['Ventricular secondary MR, ESC 2025 I A: LVEF 20 to 50%, LVESD 70 mm or less, SPAP 70 mmHg or less,',
                     'persistent severe MR despite optimised GDMT and CRT (Table 7 criteria)'], 'f-s', 'start')
    return svg(588, b)


def d3_mics_avr():
    """Minimally invasive AVR: upper hemisternotomy and right anterior thoracotomy."""
    b = T(12, 22, 'Minimally invasive aortic valve replacement: two incisions', 'f-h', 'start')
    b += T(12, 42, "Front view, patient's right on the left; grey curves are ribs 1 to 5. Arrangement schematic.", 'f-s', 'start')
    cx = 160
    b += _d3_torso(cx, 64, 440, 120)
    # sternum
    b += f'<rect x="{cx - 12}" y="74" width="24" height="200" rx="6" class="f-track"/>'
    b += f'<rect x="{cx - 12}" y="74" width="24" height="200" rx="6" class="f-dash"/>'
    # ribs 1 to 5 (grey curves) with the spaces between them numbered on the patient's left
    for k in range(1, 6):
        y = 96 + k * 32
        for sg in (-1, 1):
            b += (f'<path d="M{cx + sg * 16} {y} C{cx + sg * 50} {y + 4} {cx + sg * 86} {y + 12} {cx + sg * 106} {y + 26}" '
                  'class="f-grid" fill="none" style="stroke-width:3"/>')
        if k < 5:
            b += T(cx + 122, y + 46, str(k), "f-s")
    b += T(cx + 122, 120, 'Space', 'f-s')
    # midclavicular line on patient's right
    b += f'<line x1="{cx - 62}" y1="80" x2="{cx - 62}" y2="300" class="f-dash"/>'
    b += T(cx - 62, 316, 'Midclavicular line', 'f-s')
    # A upper hemisternotomy: from the notch down to the 3rd or 4th space
    b += f'<line x1="{cx}" y1="76" x2="{cx}" y2="224" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx + 30, 110, 'A', 'warn')
    # B right anterior thoracotomy in the 2nd or 3rd space at the midclavicular line
    b += f'<path d="M{cx - 92} 198 C{cx - 72} 191 {cx - 52} 184 {cx - 30} 178" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx - 100, 176, 'B', 'warn')
    # femoral access for B
    b += f'<line x1="{cx - 60}" y1="420" x2="{cx - 36}" y2="436" class="f-cut" style="stroke-width:4"/>'
    b += T(cx - 48, 462, 'Femoral access for B', 'f-s')
    b += box(310, 56, 400, 112, ['A Upper hemi-sternotomy: reasonable for most', '6 to 8 cm upper midline, down to the 3rd or 4th', 'space. Aortic and RA appendage cannulation', '(femoral vein if RA access is limited)'], 'b1', 'f-s')
    b += box(310, 176, 400, 112, ['B Right anterior thoracotomy', '2nd or 3rd space, midclavicular line. Needs', 'adequate femoral access for peripheral', 'cannulation; rapid-deployment valves may help'], 'b1', 'f-s')
    b += box(310, 296, 400, 96, ['Relative contraindications: previous pneumonectomy', '(both); chest wall deformity or adhesions from', 'lung surgery (B); anything distorting anatomy or', 'causing right pleural or mediastinal adhesions'], 'warn', 'f-s')
    b += box(310, 400, 400, 96, ['Against full sternotomy: same early mortality, stroke', 'and reoperation for bleeding; stay 1 to 2 days', 'shorter, less pain, fewer transfusions. B: less AF', 'and wound infection; peripheral cannulation risks'], 'ok', 'f-s')
    return svg(508, b)


# ------------------------------------------------------------------ c11: redo


def d3_tviv_or_redo():
    """Failed aortic bioprosthesis: transcatheter valve-in-valve or redo SAVR."""
    b = T(12, 22, 'Failed aortic bioprosthesis: valve-in-valve or redo SAVR?', 'f-h', 'start')
    b += box(110, 36, 500, 62, ['Heart Team. Echo and TEE, CT, coronary angiography, old operation', 'note: valve type and size, true inner diameter, radiopaque markers,',
                                'leaflet configuration, strut height'], 'b1', 'f-s')
    b += arrow(360, 98, 360, 114)
    b += box(110, 116, 500, 46, ['Endocarditis, annular rupture or pseudoaneurysm, or a paravalvular', 'leak that valve-in-valve or balloon dilation cannot treat?'], 'b0', 'f-s')
    b += arrow(610, 139, 636, 139) + T(622, 126, 'Yes', 'f-s')
    b += box(638, 104, 72, 70, ['Explant;', 'redo', 'SAVR'], 'warn', 'f-s')
    b += arrow(360, 162, 360, 178) + T(374, 174, 'No', 'f-s', 'start')
    b += box(10, 180, 340, 96, ['Mismatch risk: inner diameter under 20 mm', 'gives high gradients and worse results;',
                                'aortic valve-in-valve in a small surgical', 'valve risks severe PPM'], 'b0', 'f-s')
    b += box(370, 180, 340, 96, ['Coronary risk: low coronary height, narrow', 'sinuses, narrow or low STJ, tall bulky leaflets,',
                                 'externally mounted leaflets or stentless valve;', 'left coronary more often'], 'b0', 'f-s')
    b += arrow(180, 276, 180, 296) + arrow(540, 276, 540, 296) + arrow(450, 276, 300, 296)
    b += box(10, 298, 340, 76, ['High risk of either: redo SAVR', '(with root enlargement if needed)', 'may be preferable'], 'warn', 'f-s')
    b += box(370, 298, 340, 76, ['Valve-in-valve if chosen at high coronary', 'risk: wire the coronaries before deployment;', 'leaflet modification at expert centres'], 'b1', 'f-s')
    b += box(10, 386, 700, 60, ['Otherwise, at intermediate or high surgical risk with suitable anatomy and prosthesis:', 'transfemoral valve-in-valve (ESC 2025 IIa B); transaxillary the alternative, rarely transapical'], 'ok', 'f-s')
    b += T(12, 470, 'Redo SAVR against valve-in-valve: similar major morbidity and mortality; more paravalvular leak after valve-in-valve;', 'f-s', 'start')
    b += T(12, 487, 'longer ICU and hospital stay and more AF after redo SAVR.', 'f-s', 'start')
    return svg(500, b)


def d3_redo_mitral_routes():
    """Approaches for reoperative mitral surgery."""
    b = T(12, 22, 'Reoperative mitral surgery: the approaches', 'f-h', 'start')
    b += T(12, 42, "Front view, patient's right on the left. Arrangement schematic; incision levels are not given in the source.", 'f-s', 'start')
    cx = 160
    b += _d3_torso(cx, 64, 440, 120)
    b += f'<rect x="{cx - 12}" y="74" width="24" height="200" rx="6" class="f-track"/>'
    # 1 redo sternotomy
    b += f'<line x1="{cx}" y1="76" x2="{cx}" y2="272" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx + 26, 96, 1, 'warn')
    # 2 right thoracotomy (long) and 3 mini-thoracotomy (short), patient's right
    b += f'<path d="M{cx - 116} 250 C{cx - 90} 226 {cx - 60} 214 {cx - 26} 210" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx - 100, 214, 2, 'warn')
    b += f'<path d="M{cx - 82} 176 C{cx - 70} 170 {cx - 56} 166 {cx - 42} 165" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx - 98, 160, 3, 'warn')
    # 4 left thoracotomy
    b += f'<path d="M{cx + 116} 250 C{cx + 90} 226 {cx + 60} 214 {cx + 26} 210" class="f-cut" style="stroke-width:5"/>'
    b += _d3_num(cx + 100, 214, 4, 'warn')
    # 5 transcatheter: femoral vein (transseptal) or apex
    b += f'<line x1="{cx - 60}" y1="420" x2="{cx - 36}" y2="436" class="f-cut" style="stroke-width:4"/>'
    b += _d3_num(cx - 76, 406, 5, 'b1')
    b += f'<circle cx="{cx + 52}" cy="292" r="6" class="f-b1"/>'
    b += _d3_num(cx + 76, 300, 5, 'b1')
    rows = [('1 Redo sternotomy', ['Adequate access; choice when other procedures are needed.', 'Risks: graft injury, sternal dehiscence, cardiac injury'], 'b0'),
            ('2 Right thoracotomy', ['Bicaval; central or femoral arterial (femoral if re-entry is high', 'risk). LA via the interatrial groove or RA and septum.',
                                     'Shorter bypass, fewer transfusions, less LIMA injury'], 'ok'),
            ('3 Mini-thoracotomy', ['Lower mortality and fewer transfusions than redo', 'sternotomy or thoracotomy'], 'ok'),
            ('4 Left thoracotomy', ['When the right chest is unsuitable (radiation, pleurodesis)'], 'b0'),
            ('5 Transcatheter', ['Valve-in-valve or valve-in-ring: transapical or', 'transvenous transseptal; sizing harder in a ring or calcium'], 'b1')]
    y = 56
    for h, t, c in rows:
        hh = 24 + 17 * len(t)
        b += f'<rect x="310" y="{y}" width="400" height="{hh}" rx="8" class="f-{c}"/>'
        b += T(322, y + 18, h, 'f-n', 'start') + T(322, y + 36, t, 'f-s', 'start')
        y += hh + 6
    b += box(10, max(y, 452) + 4, 700, 60, ['Before any of these: CT of what lies behind the sternum; peripheral cannulation and bypass before', 'sternotomy help. Injury to a patent LIMA carries mortality near 50%.'], 'warn', 'f-s')
    return svg(max(y, 452) + 74, b)


# ------------------------------------------------------------------ c1: mitral repair geometry


def d3_mv_sam_predictors():
    """Where the systolic anterior motion predictors are measured on the pre-bypass TOE."""
    b = T(12, 22, 'Predicting systolic anterior motion after mitral repair', 'f-h', 'start')
    b += T(12, 42, 'Long-axis view in systole, left atrium at the top, outflow tract to the right. Arrangement schematic.', 'f-s', 'start')
    # LV wall (outer) and cavity
    b += '<path d="M96 178 C60 280 96 410 196 456 C270 428 330 316 346 204 L336 176 Z" class="f-b1"/>'
    b += '<path d="M122 182 C94 272 124 386 196 424 C244 402 280 316 292 218 L256 182 Z" class="f-lumen"/>'
    # left atrium
    b += '<ellipse cx="168" cy="116" rx="90" ry="60" class="f-lumen"/>'
    b += T(160, 108, 'LA', 'f-h')
    # aortic root and ascending aorta
    b += '<path d="M256 180 L300 64 L380 84 L338 200 Z" class="f-lumen"/>'
    b += T(334, 120, 'Ao', 'f-h')
    b += line(268, 168, 292, 184) + line(330, 190, 306, 182)
    b += T(196, 380, 'LV', 'f-h')
    # mitral leaflets: posterior (tall) and anterior meeting at the coaptation point
    b += '<path d="M124 182 L198 248" class="f-l" style="stroke-width:4"/>'
    b += '<path d="M256 182 L202 250" class="f-l" style="stroke-width:4"/>'
    b += '<circle cx="200" cy="249" r="4" class="f-l"/>'
    # 1 coaptation to septum distance
    b += '<line x1="204" y1="252" x2="284" y2="252" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += _d3_num(244, 272, 1, 'warn')
    # 2 posterior leaflet height (offset dimension line)
    b += '<line x1="110" y1="196" x2="180" y2="258" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += _d3_num(126, 244, 2, 'warn')
    # 3 basal septal thickness
    b += '<line x1="294" y1="214" x2="342" y2="214" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += _d3_num(372, 226, 3, 'warn')
    # 4 aorto-mitral angle at the anterior hinge
    b += '<line x1="256" y1="182" x2="150" y2="182" class="f-dash"/>'
    b += '<line x1="256" y1="182" x2="338" y2="200" class="f-dash"/>'
    b += '<path d="M232 182 A24 24 0 0 0 279 187" class="f-l"/>'
    b += _d3_num(268, 152, 4, 'warn')
    rows = [('1', 'Coaptation to septum under 25 mm', 'OR 5.09'),
            ('2', 'Posterior leaflet height over 15 mm', 'OR 3.80'),
            ('3', 'Basal septum 15 mm or more', 'OR 3.63'),
            ('4', 'Aorto-mitral angle under 120°', 'OR 2.74')]
    y = 64
    for n, t, o in rows:
        b += f'<rect x="420" y="{y}" width="290" height="40" rx="8" class="f-b0"/>'
        b += _d3_num(438, y + 20, n, 'warn')
        b += T(456, y + 17, t, 'f-s', 'start') + T(456, y + 33, o, 'f-n', 'start')
        y += 46
    b += box(420, y + 4, 290, 96, ['Also: anterior to posterior leaflet', 'ratio under 1.3; end-diastolic diameter', 'under 45 mm (small ventricle);', 'bileaflet prolapse; a small ring'], 'b1', 'f-s')
    b += box(10, 470, 345, 96, ['Prevent: bring posterior height under', '15 mm (sliding or folding plasty, or short', 'neochordae) so coaptation moves', 'posteriorly; do not undersize the ring'], 'ok', 'f-s')
    b += box(365, 470, 345, 96, ['If it happens off bypass: fill, stop', 'inotropes, raise afterload, slow the heart.', 'If it persists: back on bypass for height', 'reduction, a larger ring or edge-to-edge'], 'warn', 'f-s')
    return svg(578, b)


def d3_mv_tethering():
    """Tethering measurements that predict failure of a restrictive ring in ventricular secondary MR."""
    b = T(12, 22, 'Secondary MR: when a restrictive ring is likely to fail', 'f-h', 'start')
    b += T(12, 42, 'Tethered leaflets in systole, left atrium at the top. Arrangement schematic, not to scale.', 'f-s', 'start')
    # LA
    b += '<ellipse cx="200" cy="110" rx="120" ry="52" class="f-lumen"/>' + T(200, 104, 'LA', 'f-h')
    # dilated LV
    b += '<path d="M100 160 C40 250 70 400 200 440 C330 400 360 250 300 160 Z" class="f-b1"/>'
    b += '<path d="M112 164 C62 252 92 386 200 420 C308 386 338 252 288 164 Z" class="f-lumen"/>'
    # annular plane and tented leaflets
    P, A, C = (112, 162), (288, 162), (184, 238)
    b += f'<polygon points="{P[0]},{P[1]} {A[0]},{A[1]} {C[0]},{C[1]}" class="f-warn"/>'
    b += f'<line x1="{P[0] - 10}" y1="{P[1]}" x2="{A[0] + 10}" y2="{A[1]}" class="f-dash"/>'
    b += f'<path d="M{P[0]} {P[1]} L{C[0]} {C[1]} M{A[0]} {A[1]} L{C[0]} {C[1]}" class="f-l" style="stroke-width:4"/>'
    # papillary muscles displaced apically and outwards, with chords
    b += '<ellipse cx="110" cy="330" rx="18" ry="30" class="f-b0"/><ellipse cx="290" cy="330" rx="18" ry="30" class="f-b0"/>'
    b += '<path d="M110 300 L148 200 M110 300 L173 227 M290 300 L236 200 M290 300 L200 227" class="f-grid" style="stroke-width:1.5"/>'
    # 1 coaptation depth
    b += f'<line x1="{C[0]}" y1="{P[1]}" x2="{C[0]}" y2="{C[1]}" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += _d3_num(C[0] + 18, 214, 1, 'warn')
    # 2 tenting area
    b += _d3_num(232, 180, 2, 'warn')
    # 3 posterior leaflet angle
    b += f'<path d="M{P[0] + 34} {P[1]} A34 34 0 0 1 {P[0] + 23} {P[1] + 25}" class="f-l"/>'
    b += _d3_num(P[0] + 54, P[1] + 22, 3, 'warn')
    # 4 LV end-diastolic diameter
    b += '<line x1="74" y1="270" x2="326" y2="270" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += _d3_num(200, 290, 4, 'warn')
    b += T(14, 190, 'Posterior', 'f-s', 'start') + T(328, 190, 'Anterior', 'f-s', 'start')
    rows = [('1', 'Coaptation depth (tenting height)', '10 mm or more'),
            ('2', 'Tenting area', 'over 2.5 cm² (ESC: over 1.35 cm²/m² BSA)'),
            ('3', 'Posterior leaflet angle', 'over 45°'),
            ('4', 'LV end-diastolic diameter', 'over 65 mm')]
    y = 64
    for n, t, v in rows:
        b += f'<rect x="390" y="{y}" width="320" height="42" rx="8" class="f-b0"/>'
        b += _d3_num(408, y + 21, n, 'warn')
        b += T(426, y + 17, t, 'f-s', 'start') + T(426, y + 34, v, 'f-n', 'start')
        y += 48
    b += box(390, y + 6, 320, 76, ['With these: annuloplasty alone is', 'likely to fail; chordal-sparing', 'replacement is preferred'], 'warn', 'f-s')
    b += box(10, 460, 700, 60, ['CTSN severe ischaemic MR (2-year report): repair or chordal-sparing replacement gave no difference in', 'ventricular volume or survival; moderate or worse MR returned in 59% after repair against 4% after replacement'], 'b1', 'f-s')
    return svg(532, b)


# ---- figs_D4.py

import math


# ---------------------------------------------------------------- helpers

def _d4_bez(p0, p1, p2, p3, n=16):
    pts = []
    for i in range(n + 1):
        t = i / n
        a = (1 - t) ** 3
        b = 3 * (1 - t) ** 2 * t
        c = 3 * (1 - t) * t ** 2
        d = t ** 3
        pts.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return pts


def _d4_tube(pts, w, cls):
    """Filled tube of width w along a polyline, so vessels take a box class."""
    left, right = [], []
    n = len(pts)
    for i in range(n):
        x0, y0 = pts[max(i - 1, 0)]
        x1, y1 = pts[min(i + 1, n - 1)]
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L * w / 2, dx / L * w / 2
        px, py = pts[i]
        left.append((px + nx, py + ny))
        right.append((px - nx, py - ny))
    poly = left + right[::-1]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in poly) + ' Z'
    return f'<path d="{d}" class="{cls}"/>'


def _d4_pl(pts, cls='f-l', w=None, end=False, dash=False):
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    st = f' style="stroke-width:{w}"' if w else ''
    m = ' marker-end="url(#ah)"' if end else ''
    da = ' stroke-dasharray="6 4"' if dash else ''
    return f'<path d="{d}" class="{cls}"{st}{m}{da}/>'


def _d4_dot(x, y, n, cls='f-b1', r=10):
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>' + T(x, y + 4.5, str(n), 'f-h')


def _d4_lead(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, 'f-grid')


def _d4_g(ox, oy, inner, s=1):
    sc = f' scale({s})' if s != 1 else ''
    return f'<g transform="translate({ox} {oy}){sc}">{inner}</g>'


# body in a 230 x 345 frame, front view, patient's right on the viewer's left
_d4_RIJ = [(102, 40), (102, 70), (101, 100), (100, 118)]
_d4_IVC = [(100, 152), (103, 190), (108, 225), (112, 240)]
_d4_RFV = [(112, 240), (100, 270), (90, 300), (86, 335)]
_d4_LFV = [(112, 240), (124, 270), (134, 300), (138, 335)]
_d4_AO = _d4_bez((120, 128), (118, 80), (150, 72), (140, 104), 12) + [(136, 150), (130, 200), (126, 236)]
_d4_RFA = [(126, 236), (108, 268), (80, 300), (74, 335)]
_d4_LFA = [(126, 236), (138, 268), (148, 300), (152, 335)]


def _d4_body(pa=False):
    b = '<circle cx="115" cy="22" r="17" class="f-track"/>'
    b += ('<path d="M98 38 L132 38 L136 54 C172 58 188 70 190 92 L190 228 C190 250 182 262 176 272 '
          'L168 345 L126 345 L116 282 L114 282 L104 345 L62 345 L54 272 C48 262 40 250 40 228 L40 92 '
          'C42 70 58 58 94 54 Z" class="f-track"/>')
    # arms (short) for the radial line
    b += _d4_tube([(118, 92), (98, 70), (70, 66), (46, 74)], 6, 'f-warn')      # innominate, right subclavian
    b += _d4_tube([(136, 84), (160, 68), (184, 74)], 6, 'f-warn')               # left subclavian
    b += '<ellipse cx="128" cy="142" rx="28" ry="22" class="f-b0"/>'
    b += _d4_tube(_d4_AO, 10, 'f-warn')
    b += _d4_tube(_d4_RFA, 7, 'f-warn') + _d4_tube(_d4_LFA, 7, 'f-warn')
    b += _d4_tube(_d4_RIJ, 9, 'f-b1') + _d4_tube(_d4_IVC, 10, 'f-b1')
    b += _d4_tube(_d4_RFV, 8, 'f-b1') + _d4_tube(_d4_LFV, 8, 'f-b1')
    if pa:
        b += _d4_tube([(124, 146), (132, 126), (146, 112)], 8, 'f-b1')
    b += '<ellipse cx="100" cy="136" rx="14" ry="18" class="f-b1"/>'
    return b


def _d4_lbox(x, y, w, h, lines, cls='b0'):
    ty = y + h / 2 - (len(lines) - 1) * 8.5 + 4
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="f-{cls}"/>' + T(x + 12, ty, lines, 'f-s', 'start')


def _d4_circuit(x, y, w=64, h=40, lab='Circuit'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" class="f-b0"/>'
            + T(x + w / 2, y + 16, lab, 'f-s') + T(x + w / 2, y + 31, 'pump + oxy', 'f-s'))


# block circulation in a 230 x 214 frame
_d4_CB = {'Lungs': (80, 6, 70, 26), 'PA': (8, 46, 66, 26), 'LA': (156, 46, 66, 26), 'RV': (8, 94, 66, 26),
       'LV': (156, 94, 66, 26), 'RA': (8, 142, 66, 26), 'Aorta': (156, 142, 66, 26),
       'Cavae': (8, 186, 66, 26), 'Body': (156, 186, 66, 26)}


def _d4_cbox(k, cls='b0'):
    x, y, w, h = _d4_CB[k]
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="f-{cls}"/>' + T(x + w / 2, y + h / 2 + 4.5, k, 'f-s')


def _d4_circ(hi=()):
    b = ''.join(_d4_cbox(k, 'warn' if k in hi else ('b1' if k in ('PA', 'RV', 'RA', 'Cavae') else 'b0')) for k in _d4_CB)
    for a, c in (('Cavae', 'RA'), ('RA', 'RV'), ('RV', 'PA'), ('LA', 'LV'), ('LV', 'Aorta'), ('Aorta', 'Body')):
        x, y, w, h = _d4_CB[a]
        x2, y2, w2, h2 = _d4_CB[c]
        if y2 < y:
            b += line(x + w / 2, y, x + w / 2, y2 + h2, 'f-grid')
        else:
            b += line(x + w / 2, y + h, x + w / 2, y2, 'f-grid')
    b += line(74, 52, 80, 26, 'f-grid') + line(150, 26, 156, 52, 'f-grid')
    b += line(156, 199, 74, 199, 'f-grid')
    return b


# ---------------------------------------------------------------- 1 IABP position

def d4_iabp_position():
    b = ''
    asc = [(230, 330), (230, 250), (230, 170)]
    arch = _d4_bez((230, 170), (230, 70), (400, 60), (400, 150), 20)
    desc = [(400, 150), (400, 260), (400, 330), (400, 380), (400, 410)]
    b += _d4_tube([(262, 92), (250, 40)], 14, 'f-warn') + _d4_tube([(312, 74), (316, 22)], 12, 'f-warn')
    b += _d4_tube([(362, 84), (380, 30)], 12, 'f-warn')
    b += _d4_tube(asc + arch[1:] + desc[1:], 40, 'f-warn')
    b += _d4_tube([(400, 322), (350, 322)], 10, 'f-warn')            # mesenteric (schematic)
    b += _d4_tube([(400, 352), (456, 352)], 10, 'f-warn') + _d4_tube([(400, 352), (344, 352)], 10, 'f-warn')
    b += '<rect x="389" y="170" width="22" height="128" rx="11" class="f-b1"/>'
    b += _d4_pl([(400, 298), (400, 418)], 'f-l', 2.4)
    b += f'<circle cx="400" cy="168" r="3.5" class="f-b0"/>'
    # labels
    b += T(250, 30, 'Innominate', 'f-s', 'end') + T(322, 16, 'L carotid', 'f-s', 'start')
    b += T(388, 40, 'Left subclavian', 'f-s', 'start')
    b += T(330, 318, 'Mesenteric', 'f-s', 'end') + T(330, 356, 'Renal', 'f-s', 'end') + T(462, 356, 'Renal', 'f-s', 'start')
    b += T(230, 350, 'Ascending aorta', 'f-s')
    b += _d4_lead(420, 168, 470, 120) + T(476, 112, ['Tip 2 to 3 cm distal to the', 'left subclavian origin'], 'f-h', 'start')
    b += _d4_lead(414, 234, 470, 200) + T(476, 192, ['Balloon 25 to 50 ml, sized by height;', 'inflated with helium (low density,', 'absorbed if the balloon ruptures)'], 'f-s', 'start')
    b += _d4_lead(414, 290, 470, 286) + T(476, 282, ['Balloon sits proximal to the', 'mesenteric and renal arteries'], 'f-s', 'start')
    b += T(410, 444, '8 to 9.5 Fr catheter, usually femoral, passed retrograde', 'f-s', 'start')
    b += box(10, 110, 190, 76, ['Too high:', 'subclavian and vertebral', 'occlusion'], 'warn', 'f-s')
    b += box(10, 200, 190, 76, ['Too low: loses effect;', 'mesenteric and renal', 'occlusion'], 'warn', 'f-s')
    b += box(490, 384, 220, 40, ['Daily chest film for position;', 'limb and abdominal checks'], 'b0', 'f-s')
    return svg(456, b)


# ---------------------------------------------------------------- 2 Impella position

def _d4_thick(pts, cls, w):
    """Thick path plus a small separate arrowhead on the last segment."""
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    return _d4_pl(pts, cls, w) + arrow(x1, y1, x2, y2)


def d4_impella_position():
    ox = 90
    i = ''
    i += '<path d="M90 190 C30 240 60 370 190 420 C240 370 240 250 170 190 Z" class="f-b0"/>'
    i += _d4_tube([(130, 196), (130, 120)] + _d4_bez((130, 120), (130, 40), (300, 30), (300, 120), 16)[1:] + [(300, 380)], 50, 'f-warn')
    i += '<path d="M64 300 C74 290 84 300 82 316" class="f-l"/>'
    i += '<path d="M196 330 C184 320 178 334 184 346" class="f-l"/>'
    i += line(100, 196, 160, 196, 'f-cut')
    cath = _d4_bez((145, 96), (155, 40), (300, 50), (300, 140), 14) + [(300, 390)]
    i += _d4_pl(cath, 'f-l', 2.4)
    i += '<rect x="138" y="96" width="16" height="26" rx="4" class="f-b1"/>'
    i += _d4_tube([(146, 122), (148, 196), (154, 262)], 12, 'f-b1')
    i += '<path d="M154 262 C162 296 192 306 192 288 C192 276 176 280 178 292" class="f-l" style="stroke-width:2.2"/>'
    for y in (128, 136):
        i += line(140, y, 152, y, 'f-l')
    i += '<circle cx="148" cy="196" r="4" class="f-warn"/>'
    b = _d4_g(ox, 0, i)
    b += T(ox + 96, 186, 'Aortic valve', 'f-s', 'end')
    b += T(ox + 120, 360, 'LV', 'f-h')
    b += _d4_lead(ox + 138, 108, 166, 84) + T(8, 66, ['Outlet in the aortic', 'root, well above', 'the valve'], 'f-s', 'start')
    b += _d4_lead(ox + 144, 198, 150, 232) + T(8, 226, ['Radiopaque marker', 'at the annulus', '(2.5 and CP)'], 'f-s', 'start')
    b += _d4_lead(ox + 152, 262, 150, 320) + T(8, 316, ['Inlet 3.5 to 4.0 cm', 'below the valve,', 'angled to the apex,', 'away from the', 'papillary muscles'], 'f-s', 'start')
    b += T(10, 446, 'Catheter passed retrograde from the femoral artery (5.0 and 5.5: surgical, direct aortic, axillary or femoral cut-down).', 'f-s', 'start')
    b += T(10, 464, 'Malposition: mitral dysfunction, haemolysis, suction, less support. Confirm with echo.', 'f-s', 'start')
    x = 440
    b += box(x, 10, 270, 84, ['Across the valve (correct):', 'motor current pulsatile; 5.0/LD', 'placement signal high in diastole,', 'near zero in systole'], 'ok', 'f-s')
    b += box(x, 104, 270, 84, ['Entirely in the LV: motor current flat.', '2.5/CP: drop to P-2, pull back', 'until an aortic waveform,', 'then a further 4 cm'], 'warn', 'f-s')
    b += box(x, 198, 270, 66, ['Entirely in the aorta: current flat.', 'Do not reposition without', 'a guidewire'], 'warn', 'f-s')
    b += box(x, 274, 270, 48, ['Outflow blocked (too deep):', 'P-2 and pull back 2 cm'], 'warn', 'f-s')
    b += box(x, 332, 270, 66, ['Wean 1-2 P-levels at a time;', 'never below P-2 (retrograde flow', 'across the aortic valve)'], 'b1', 'f-s')
    return svg(476, b)


# ---------------------------------------------------------------- 3 temporary LV devices

def d4_temp_lv_routes():
    b = ''
    titles = [('Impella 2.5, CP, 5.0, 5.5', ['Micro-axial pump across the', 'aortic valve: inflow in the LV,', 'outflow in the aortic root']),
              ('TandemHeart', ['21 Fr transseptal inflow (femoral', 'vein to LA); outflow 15-17 Fr', 'femoral artery to distal aorta']),
              ('CentriMag (left)', ['Surgical: LV inflow, aortic', 'outflow; extracorporeal', 'maglev centrifugal pump'])]
    for k, (t, sub) in enumerate(titles):
        ox = 10 + k * 240
        b += T(ox + 115, 18, t, 'f-h')
        inner = _d4_circ()
        if k == 0:
            inner += _d4_thick(_d4_bez((156, 110), (128, 116), (128, 148), (156, 154), 10), 'f-cut', 4)
            inner += '<circle cx="135" cy="132" r="9" class="f-ok"/>'
        elif k == 1:
            inner += _d4_pl(_d4_bez((60, 186), (100, 150), (110, 80), (156, 62), 14), 'f-cut', 4)
            inner += T(136, 88, 'septum', 'f-s', 'start')
            inner += _d4_pl([(41, 212), (41, 232), (100, 232)], 'f-cut', 4)
            inner += '<circle cx="115" cy="232" r="10" class="f-ok"/>'
            inner += _d4_thick([(125, 232), (189, 232), (189, 214)], 'f-cut', 4)
            inner += T(30, 250, 'Femoral vein', 'f-s', 'start') + T(200, 250, 'Femoral artery', 'f-s', 'end')
        else:
            inner += _d4_thick(_d4_bez((156, 110), (110, 112), (110, 152), (156, 156), 10), 'f-cut', 4)
            inner += '<circle cx="122" cy="132" r="10" class="f-ok"/>'
        b += _d4_g(ox, 30, inner)
        b += T(ox + 115, 312, sub, 'f-s')
    b += box(10, 368, 345, 76, ['Red line: device path; green circle: pump.', 'TandemHeart: septal patch closure after', 'removal; inflow slipping back into the RA', 'gives a right-to-left shunt and hypoxia'], 'b0', 'f-s')
    b += box(365, 368, 345, 76, ['Flows (TSRA ch. 121): Impella 2.5 up to 2.5,', 'CP 3.0, 5.0 5.0, 5.5 peak 6 L/min;', 'TandemHeart up to 5.0 L/min at 7500 rpm;', 'CentriMag up to 10 L/min'], 'b1', 'f-s')
    return svg(454, b)


# ---------------------------------------------------------------- 4 peripheral VA ECMO

def d4_va_peripheral():
    s = 1.25
    ox, oy = 230, 6
    inner = _d4_body()
    inner += _d4_pl([(80, 345), (86, 330)] + _d4_RFV[::-1][1:] + _d4_IVC[::-1][1:] + [(100, 140)], 'f-l', 3.2)
    inner += _d4_pl([(170, 345), (158, 330), (150, 305)], 'f-cut', 3.6)
    inner += _d4_pl([(176, 318), (160, 318), (154, 332)], 'f-cut', 2)
    inner += '<ellipse cx="128" cy="86" rx="14" ry="9" class="f-dash"/>'
    b = _d4_g(ox, oy, inner, s)

    def P(x, y):
        return ox + s * x, oy + s * y
    b += arrow(*P(140, 228), *P(136, 182)) + arrow(*P(138, 142), *P(140, 112))
    b += _d4_circuit(560, 390, 110, 44, 'Circuit')
    vx, vy = P(80, 345)
    ax, ay = P(170, 345)
    b += _d4_pl([(vx, vy), (vx, 444), (560, 444), (566, 434)], 'f-l', 2.4)
    b += _d4_pl([(640, 390), (640, 372), (ax + 14, 372), (ax, ay)], 'f-cut', 2.4)
    x, y = P(128, 86)
    b += _d4_lead(x - 18, y, 196, 50) + T(190, 22, ['Mixing point: retrograde', 'oxygenated flow meets', 'native LV output. Proximal', 'to the innominate, both', 'radial gases agree but', 'both are poor'], 'f-s', 'end')
    x, y = P(48, 74)
    b += _d4_lead(x, y, 196, 150) + T(190, 146, ['Right radial arterial', 'line in all (ch. 122)'], 'f-s', 'end')
    x, y = P(100, 136)
    b += _d4_lead(x - 18, y, 196, 210) + T(190, 206, ['Drainage (circuit inflow):', 'femoral venous 21-28 Fr,', 'long (55-60 cm); flow is', 'limited more by this', 'cannula than the arterial'], 'f-s', 'end')
    b += T(190, 316, ['Changing flow only', 'moves the mixing point'], 'f-h', 'end')
    b += T(10, 400, ['Full support: about', '2.4 L/m²/min; size', 'cannulas by BSA'], 'f-s', 'start')
    x, y = P(138, 160)
    b += _d4_lead(x + 8, y, 520, 120) + T(526, 104, ['Retrograde aortic flow raises', 'LV afterload: narrower pulse', 'pressure, shorter aortic valve', 'opening, risk of LV distension'], 'f-s', 'start')
    b += box(526, 180, 184, 62, ['Fix differential cyanosis:', 'lungs, 2nd venous', 'cannula, or VAV'], 'b1', 'f-s')
    x, y = P(150, 305)
    b += _d4_lead(x + 6, y, 520, 276) + T(526, 266, ['Return (circuit outflow):', 'femoral arterial 15-18 Fr,', 'short (15 cm)'], 'f-s', 'start')
    x, y = P(158, 326)
    b += _d4_lead(x + 4, y + 4, 520, 336) + T(526, 340, 'Distal perfusion 6-8 Fr, SFA', 'f-s', 'start')
    return svg(456, b)


# ---------------------------------------------------------------- 5 central VA ECMO

def _d4_heart_front():
    """Front view heart in a 420 x 380 frame: RA left, ventricles right, aorta and PA above."""
    b = _d4_tube([(200, 10), (200, 120)], 34, 'f-b1')
    b += _d4_tube([(200, 300), (200, 372)], 34, 'f-b1')
    b += '<path d="M236 170 C300 140 400 150 418 236 C430 300 380 360 340 372 C290 384 250 330 236 280 Z" class="f-b0"/>'
    b += '<path d="M300 170 C330 230 340 300 330 366" class="f-dash"/>'
    b += _d4_tube([(272, 176), (272, 92)] + _d4_bez((272, 92), (272, 20), (380, 20), (380, 92), 14)[1:] + [(380, 130)], 36, 'f-warn')
    b += _d4_tube([(318, 170), (340, 118), (372, 104)], 26, 'f-b1')
    b += '<ellipse cx="200" cy="210" rx="46" ry="74" class="f-b1"/>'
    b += _d4_tube([(160, 190), (118, 182)], 16, 'f-b1')
    return b


def d4_va_central():
    ox, oy = 150, 20
    b = _d4_g(ox, oy, _d4_heart_front())

    def P(x, y):
        return ox + x, oy + y
    b += _d4_pl([P(200, 220), P(176, 300), (300, 410)], 'f-l', 3.6)
    b += _d4_pl([P(272, 116), (380, 64), (612, 64), (612, 380)], 'f-cut', 3.6)
    b += _d4_pl([P(124, 182), (190, 220), (190, 420), (520, 420)], 'f-dash', 2.2)
    b += _d4_pl([P(394, 352), (600, 442), (560, 442)], 'f-dash', 2.2)
    b += _d4_circuit(520, 380, 110, 50, 'Circuit')
    b += _d4_pl([(300, 410), (520, 410)], 'f-l', 3.6)
    b += T(ox + 200, oy + 214, 'RA', 'f-h') + T(ox + 360, oy + 270, 'LV', 'f-h') + T(ox + 272, oy + 270, 'RV', 'f-h')
    b += T(ox + 272, oy + 150, 'Ao', 'f-h') + T(ox + 392, oy + 102, 'PA', 'f-s', 'start')
    b += T(ox + 200, oy + 50, 'SVC', 'f-s') + T(ox + 200, oy + 360, 'IVC', 'f-s')
    b += _d4_lead(*P(118, 182), 140, 182) + T(136, 172, ['Right superior', 'pulmonary vein'], 'f-s', 'end')
    b += T(10, 250, ['Drainage: right', 'atrium (CPB-type', 'configuration)'], 'f-s', 'start')
    b += T(10, 330, ['Vent options for', 'direct LV', 'decompression:', 'RSPV or LV apex', '(dashed)'], 'f-s', 'start')
    b += T(600, 48, 'Return: ascending aorta', 'f-s', 'end')
    b += box(10, 30, 130, 100, ['Usually', 'post-cardiotomy;', 'resternotomy'], 'b1', 'f-s')
    b += box(620, 120, 92, 150, ['Antegrade', 'aortic flow:', 'no differential', 'cyanosis; no', 'limb', 'ischaemia;', 'higher flows'], 'ok', 'f-s')
    b += box(620, 280, 92, 92, ['Risks:', 'bleeding and', 'infection', '(open chest)'], 'warn', 'f-s')
    b += T(360, 466, 'Occasionally LV apex to aorta, axillary artery or transseptal (ch. 122)', 'f-s')
    return svg(478, b)


# ---------------------------------------------------------------- 6 LV distension on VA ECMO

def d4_lv_unloading():
    s = 1.45
    i = _d4_circ(hi=('LV',))
    i += '<rect x="78" y="228" width="74" height="30" rx="6" class="f-b0"/>' + T(115, 247, 'ECMO', 'f-s')
    i += _d4_pl([(41, 212), (41, 243), (78, 243)], 'f-l', 3)
    i += _d4_pl([(152, 243), (228, 243), (228, 155), (222, 155)], 'f-cut', 3)
    i += _d4_pl([(204, 142), (204, 124)], 'f-cut', 1.6)                                   # retrograde through AV
    i += _d4_pl(_d4_bez((156, 112), (130, 116), (130, 146), (156, 150), 8), 'f-dash', 2)     # Impella (option)
    i += _d4_pl([(156, 62), (74, 152)], 'f-dash', 1.4)
    b = _d4_g(10, 26, i, s)

    def P(x, y):
        return 10 + s * x, 26 + s * y
    b += T(10, 16, 'Why the LV fills on peripheral VA ECMO (numbers) and ways to unload it (letters)', 'f-h', 'start')
    b += _d4_dot(*P(41, 80), 1, 'f-warn', 11) + _d4_dot(*P(202, 84), 2, 'f-warn', 11) + _d4_dot(*P(214, 133), 3, 'f-warn', 11)
    b += _d4_dot(*P(130, 132), 'A', 'f-ok', 11) + _d4_dot(*P(102, 121), 'B', 'f-ok', 11)
    b += _d4_dot(*P(96, 60), 'C', 'f-ok', 11) + _d4_dot(*P(222, 108), 'D', 'f-ok', 11)
    x = 370
    b += _d4_lbox(x, 30, 340, 92, ['1  Venous return bypassing the drainage cannula', '2  Bronchial and Thebesian return',
                                '3  Retrograde flow through an incompetent', '    aortic valve (return flow also raises afterload)'], 'warn')
    b += _d4_lbox(x, 132, 340, 74, ['LV pressure over 20-25 mmHg: less myocardial', 'oxygen supply, "flash" pulmonary oedema,', 'LV thrombus despite anticoagulation'], 'b0')
    b += _d4_lbox(x, 216, 340, 92, ['Unload early if: little or no LV function;', 'moderate-severe AR; PA diastolic over 25 mmHg;', 'LVEDD over 50 mm; worsening pulmonary', 'oedema'], 'b1')
    b += _d4_lbox(x, 318, 340, 128, ['First: lower ECMO flow and add inotropes to', 'keep pulsatility 10-20 mmHg; then', 'A  Impella (LV to aorta)', 'B  Atrial septostomy',
                                  'C  Protek Duo for complete venous drainage', 'D  Surgical vent: RSPV, LA, PA or LV apex'], 'ok')
    return svg(456, b)


# ---------------------------------------------------------------- 7 hybrid configurations

def d4_ecmo_reconfig():
    b = ''
    panels = [('VVA: add a venous drainage cannula', 0), ('VAV: add a return cannula to the RA', 1)]
    for k, (t, mode) in enumerate(panels):
        ox = 6 + k * 360
        i = _d4_body()
        i += _d4_pl([(80, 345)] + _d4_RFV[::-1][1:] + _d4_IVC[::-1][1:3], 'f-l', 3)
        i += _d4_pl([(170, 345), (158, 330), (150, 305)], 'f-cut', 3.4)
        i += f'<rect x="150" y="358" width="64" height="30" rx="6" class="f-b0"/>' + T(182, 377, 'ECMO', 'f-s')
        i += _d4_pl([(80, 345), (80, 373), (150, 373)], 'f-l', 3)
        i += _d4_pl([(214, 373), (222, 373), (222, 345), (170, 345)], 'f-cut', 3.4)
        if mode == 0:
            i += _d4_pl([(100, 130), (102, 70), (102, 34), (24, 34), (24, 373), (80, 373)], 'f-l', 3)
        else:
            i += _d4_pl([(100, 128), (102, 70), (102, 30), (226, 30), (226, 345)], 'f-cut', 3.4)
        b += _d4_g(ox, 30, i)
        b += T(ox + 4, 20, t, 'f-h', 'start')
    b += T(250, 70, ['Drainage now from', 'femoral vein and', 'right IJ, joined by', 'a Y-connector on', 'the DRAINAGE side'], 'f-s', 'start')
    b += T(250, 200, ['For: LV distension', 'or poor drainage', 'from the femoral', 'venous cannula'], 'f-s', 'start')
    b += T(250, 300, ['Or a Protek Duo', '(distal lumen in', 'main or right PA):', 'total drainage'], 'f-s', 'start')
    b += T(606, 70, ['Right IJ cannula', 'Y-connected to the', 'RETURN side:', 'oxygenated blood', 'into the RA'], 'f-s', 'start')
    b += T(606, 200, ['For: LV recovering', 'but lungs still', 'failing, with', 'differential', 'cyanosis'], 'f-s', 'start')
    b += T(606, 300, ['Black: drainage', 'Red: return'], 'f-s', 'start')
    b += box(10, 432, 700, 44, ['Next step, VV: LV recovered with ongoing lung failure. If RV support is still needed,', 'a single-cannula VV circuit via Protek Duo bypasses the RV.'], 'b1', 'f-s')
    return svg(486, b)


# ---------------------------------------------------------------- 8 VV ECMO cannulation

def d4_vv_configs():
    b = ''
    heads = ['Femoral to IJ (typical)', 'Femoro-femoral', 'Dual-lumen, right IJ']
    for k, t in enumerate(heads):
        ox = k * 240
        i = _d4_body(pa=(k == 2))
        i += f'<rect x="150" y="358" width="64" height="30" rx="6" class="f-b0"/>' + T(182, 377, 'ECMO', 'f-s')
        if k == 0:
            i += _d4_pl([(80, 345)] + _d4_RFV[::-1][1:] + _d4_IVC[::-1][1:] + [(100, 156)], 'f-l', 3)
            i += _d4_pl([(80, 345), (80, 373), (150, 373)], 'f-l', 3)
            i += _d4_pl([(100, 124), (102, 70), (102, 30), (226, 30), (226, 373), (214, 373)], 'f-cut', 3.2)
        elif k == 1:
            i += _d4_pl([(80, 345)] + _d4_RFV[::-1][1:] + _d4_IVC[::-1][1:3], 'f-l', 3)
            i += _d4_pl([(80, 345), (80, 373), (150, 373)], 'f-l', 3)
            i += _d4_pl([(146, 345)] + _d4_LFV[::-1][1:] + _d4_IVC[::-1][1:] + [(100, 154)], 'f-cut', 3.2)
            i += _d4_pl([(146, 345), (146, 352), (214, 352), (214, 373)], 'f-cut', 3.2)
        else:
            i += _d4_pl([(102, 30), (102, 70), (100, 118), (112, 140), (126, 140), (138, 118)], 'f-cut', 3)
            i += _d4_pl([(98, 30), (98, 70), (96, 126)], 'f-l', 3)
            i += _d4_pl([(100, 30), (100, 10), (226, 10), (226, 373), (214, 373)], 'f-cut', 3)
            i += _d4_pl([(96, 10), (20, 10), (20, 373), (150, 373)], 'f-l', 3)
        b += _d4_g(ox + 2, 26, i)
        b += T(ox + 117, 16, t, 'f-h')
    b += T(122, 438, ['Drainage: multistage femoral,', 'tip in the intrahepatic IVC', '(ch. 71) or at the IVC-RA', 'junction (ch. 123). Return: IJ', 'to the cavo-atrial junction', 'Up to 7 L/min'], 'f-s')
    b += T(362, 438, ['Return through the other', 'femoral vein, tip cephalad', 'to the drainage tip', 'Two groins: harder to', 'mobilise; more recirculation', '3 to 6 L/min'], 'f-s')
    b += T(602, 438, ['One site; patient can walk;', 'placed under fluoroscopy', 'and echo. Protek Duo drains', 'the RA and returns to the', 'PA (ch. 122)', 'About 5 L/min'], 'f-s')
    b += box(10, 548, 700, 44, ['Recirculation: return blood drained straight back when the tips are close, giving persistent', 'hypoxia. Keep tips about 8 cm apart; shortest, widest drainage cannula (Poiseuille).'], 'warn', 'f-s')
    return svg(602, b)


# ---------------------------------------------------------------- 9 LVAD components

def d4_lvad_components():
    i = _d4_heart_front()
    graft = [(372, 398), (300, 414), (200, 414), (130, 386), (120, 300), (124, 200), (150, 132), (200, 112), (252, 108)]
    i += _d4_tube(_d4_bez((372, 398), (250, 440), (110, 430), (118, 300), 16) + _d4_bez((118, 300), (124, 160), (190, 104), (254, 108), 14)[1:], 12, 'f-ok')
    i += _d4_tube([(388, 336), (360, 300)], 16, 'f-ok')                    # inflow cannula into the LV
    i += '<circle cx="398" cy="370" r="34" class="f-ok"/>' + T(398, 375, 'Pump', 'f-s')
    i += '<ellipse cx="384" cy="330" rx="22" ry="8" transform="rotate(-50 384 330)" class="f-b1"/>'   # sewing ring
    i += _d4_pl([(410, 402), (430, 450), (430, 486)], 'f-l', 3)
    sc = 0.82
    ox, oy = 168, 8
    b = _d4_g(ox, oy, i, sc)

    def P(x, y):
        return ox + sc * x, oy + sc * y
    b += T(*P(200, 214), 'RA', 'f-h') + T(*P(360, 250), 'LV', 'f-h') + T(*P(270, 260), 'RV', 'f-h')
    b += T(*P(272, 150), 'Ao', 'f-h') + T(*P(200, 50), 'SVC', 'f-s')
    b += _d4_lead(*P(370, 312), 548, 214) + T(552, 196, ['Inflow cannula: LV apex', '(apical dimple or', 'slightly anterior), aimed', 'at the mitral valve (TOE)'], 'f-s', 'start')
    b += _d4_lead(*P(394, 324), 548, 282) + T(552, 280, ['Sewing ring: twelve', '2-0 pledgetted', 'mattress sutures'], 'f-s', 'start')
    b += _d4_lead(*P(432, 370), 548, 350) + T(552, 348, ['Intrapericardial', 'centrifugal pump:', 'no pocket needed'], 'f-s', 'start')
    b += _d4_lead(*P(430, 480), 548, 418) + T(552, 416, ['Driveline through', 'the rectus sheath,', 'out to controller', 'and batteries'], 'f-s', 'start')
    b += _d4_lead(*P(254, 108), 160, 40) + T(156, 22, ['Outflow graft', 'bevelled 45-60° to', 'the lateral greater', 'curvature, proximal', 'ascending aorta'], 'f-s', 'end')
    b += _d4_lead(*P(118, 300), 160, 300) + T(156, 270, ['Graft runs to the', 'right and lies', 'lateral to the RA:', 'no compression,', 'safe at re-entry'], 'f-s', 'end')
    b += T(156, 396, ['Do not wrap', 'the graft', 'completely', '(III C)'], 'f-s', 'end')
    b += box(10, 120, 140, 100, ['Correct AR at', 'implant: it makes', 'a loop aorta to', 'LV to pump'], 'warn', 'f-s')
    b += box(10, 474, 700, 44, ['TOE after implant: inflow unobstructed, septum in the midline. Close any septal defect.', 'Keep mean pressure above 65 mmHg: low pressure invites suck-down and RV failure (ch. 72).'], 'b1', 'f-s')
    return svg(528, b)


# ---------------------------------------------------------------- 10 driveline

def _d4_abdo(ox):
    b = f'<path d="M{ox + 20} 30 C{ox + 60} 70 {ox + 90} 90 {ox + 115} 70 C{ox + 140} 90 {ox + 170} 70 {ox + 210} 30" class="f-l"/>'
    b += line(ox + 115, 10, ox + 115, 72, 'f-cut')
    b += f'<rect x="{ox + 70}" y="70" width="40" height="190" rx="18" class="f-track"/>'
    b += f'<rect x="{ox + 120}" y="70" width="40" height="190" rx="18" class="f-track"/>'
    b += f'<circle cx="{ox + 115}" cy="190" r="6" class="f-b0"/>'
    return b


def d4_lvad_driveline():
    b = T(120, 18, 'Standard tunnel', 'f-h') + T(360, 18, 'Double tunnel', 'f-h')
    for ox in (0, 240):
        b += _d4_abdo(ox + 5)
        b += T(ox + 120, 212, 'umbilicus', 'f-s')
    # standard: pump near xiphoid, through rectus, exit halfway umbilicus to costal margin (left side)
    b += '<circle cx="132" cy="60" r="12" class="f-ok"/>'
    b += _d4_pl([(140, 70), (146, 100), (150, 120)], 'f-ok', 5) + _d4_pl([(150, 120), (174, 130), (186, 134)], 'f-dash', 2)
    b += '<circle cx="188" cy="135" r="5" class="f-warn"/>'
    b += T(120, 236, ['Through posterior sheath and', 'rectus, peritoneum intact; exit', 'halfway from umbilicus to', 'costal margin'], 'f-s')
    # double tunnel
    b += '<circle cx="372" cy="60" r="12" class="f-ok"/>'
    b += _d4_pl([(380, 70), (384, 120), (382, 170)], 'f-ok', 5)
    b += _d4_pl([(382, 170), (420, 160), (436, 112)], 'f-dash', 2)
    b += '<circle cx="437" cy="110" r="5" class="f-warn"/>'
    b += T(360, 236, ['Within the rectus sheath toward', 'the umbilicus, then subcutaneous', 'to the left upper quadrant'], 'f-s')
    b += T(360, 312, 'Curves: costal margins. Solid green: in the rectus sheath. Dashed: subcutaneous. Red dot: exit.', 'f-s')
    # cross-section
    x0, w = 490, 220
    b += T(x0 + w / 2, 18, 'Layers (cross-section)', 'f-h')
    layers = [('Skin', 36, 10, 'f-warn'), ('Fat', 46, 50, 'f-track'), ('Rectus', 112, 46, 'f-b1'), ('Preperitoneal', 172, 26, 'f-track')]
    for lab, y, h, cls in layers:
        b += f'<rect x="{x0}" y="{y}" width="{w}" height="{h}" class="{cls}"/>'
    b += line(x0, 104, x0 + w, 104, 'f-l') + line(x0, 162, x0 + w, 162, 'f-l') + line(x0, 200, x0 + w, 200, 'f-dash')
    b += T(x0 + w - 4, 100, 'anterior sheath', 'f-s', 'end') + T(x0 + w - 4, 176, 'posterior sheath', 'f-s', 'end')
    b += T(x0 + w - 4, 214, 'peritoneum (not entered)', 'f-s', 'end')
    b += T(x0 + w - 4, 76, 'fat', 'f-s', 'end') + T(x0 + w - 4, 140, 'rectus', 'f-s', 'end')
    path = [(x0 + 14, 186), (x0 + 40, 170), (x0 + 70, 120), (x0 + 100, 70), (x0 + 120, 50)]
    b += _d4_pl(path, 'f-ok', 7)
    b += _d4_pl([(x0 + 120, 50), (x0 + 130, 34), (x0 + 136, 22)], 'f-l', 3)
    b += _d4_lead(x0 + 90, 82, x0 + 30, 236) + T(x0 + 4, 250, ['Velour all inside the tunnel;', 'only silicone touches the', 'skin (silicone-skin interface)'], 'f-s', 'start')
    b += box(10, 326, 700, 60, ['Tunnel before heparin if possible; agree the side with the patient before surgery; anchor the line near the exit', 'and fix it externally while it heals. Alternatives: postauricular (Jarvik 2000), chest wall.'], 'b1', 'f-s')
    return svg(396, b)


# ---------------------------------------------------------------- 11 pump speed and the septum

def _d4_vent_panel(ox, lv_rx, sep_dx, rv_big, mr, av):
    b = f'<ellipse cx="{ox + 120 + lv_rx / 2}" cy="150" rx="{100 + lv_rx + (12 if rv_big else 0)}" ry="{104 + lv_rx / 3}" class="f-b0"/>'
    b += f'<ellipse cx="{ox + 160}" cy="34" rx="40" ry="16" class="f-b1"/>' + T(ox + 160, 38, 'LA', 'f-s')
    sx = ox + 100
    b += f'<path d="M{sx} 54 Q{sx + sep_dx} 150 {sx} 248" class="f-l" style="stroke-width:5"/>'
    b += line(ox + 138, 52, ox + 168, 52, 'f-cut') + T(ox + 130, 66, 'MV', 'f-s', 'end')
    b += line(ox + 182, 60, ox + 204, 70, 'f-cut') + T(ox + 208, 60, 'AV', 'f-s', 'start')
    b += f'<rect x="{ox + 148}" y="214" width="16" height="44" rx="4" class="f-ok"/>'
    b += T(ox + 56, 156, 'RV', 'f-h') + T(ox + 160, 156, 'LV', 'f-h')
    if mr:
        b += _d4_pl([(ox + 152, 90), (ox + 152, 60)], 'f-cut', 2) + arrow(ox + 152, 64, ox + 152, 44)
    b += T(ox + 120, 278, av, 'f-s')
    return b


def d4_lvad_speed():
    b = ''
    b += T(125, 18, 'Poor unloading', 'f-h') + T(365, 18, 'Target', 'f-h') + T(605, 18, 'Speed too high', 'f-h')
    b += _d4_g(0, 26, _d4_vent_panel(0, 14, 0, False, True, 'Aortic valve opens more often'))
    b += _d4_g(0, 26, _d4_vent_panel(245, 0, 0, False, False, 'Aortic valve opens intermittently'))
    b += _d4_g(0, 26, _d4_vent_panel(485, 0, 60, True, False, 'Septum shifted leftward'))
    b += _d4_lbox(10, 326, 225, 110, ['As with pump thrombosis on echo:', 'larger LV, more frequent aortic', 'valve opening, worsening MR,', 'lower inflow/outflow velocities'], 'warn')
    b += _d4_lbox(250, 326, 220, 110, ['Intermittent aortic valve', 'opening, no significant MR,', 'septum in the midline, inflow', 'unobstructed (TOE)'], 'ok')
    b += _d4_lbox(485, 326, 225, 110, ['Leftward septal shift and RV', 'failure; adjust speed to', 'optimise filling without', 'suction (Task Force 4)'], 'warn')
    b += T(360, 458, ['At pump start: MAP 75-90 mmHg; CVP 14 mmHg or less desirable;', 'persistent RV failure needs mechanical RV support without delay.'], 'f-s')
    return svg(490, b)


# ---------------------------------------------------------------- 12 pump thrombosis and obstruction

def d4_lvad_thrombosis():
    b = ''
    xs = [(10, 'LV', 'b0'), (150, 'Inflow cannula', 'b1'), (300, 'Rotor (pump)', 'ok'), (450, 'Outflow graft', 'b1'), (600, 'Aorta', 'b0')]
    for x, lab, cls in xs:
        b += box(x, 10, 110, 40, lab, cls, 'f-s')
    for k in range(4):
        b += arrow(xs[k][0] + 110, 30, xs[k + 1][0], 30)
    b += box(120, 70, 170, 96, ['Inflow (pre-pump)', 'obstruction:', 'power FALLS'], 'b1', 'f-s')
    b += box(300, 70, 140, 96, ['Intrapump', 'thrombus: power', 'RISES (acute', 'or slow)'], 'warn', 'f-s')
    b += box(450, 70, 260, 96, ['Outflow (post-pump) obstruction:', 'power FALLS; LDH not markedly', 'raised unless secondary pump', 'thrombosis. Presents with RV', 'failure and falling flows'], 'b1', 'f-s')
    b += arrow(205, 50, 205, 70) + arrow(355, 50, 370, 70) + arrow(505, 50, 520, 70)
    b += _d4_lbox(10, 180, 340, 132, ['Clues: flow or power change, a radial pulse', 'returns (poor unloading), low-output HF,', 'arrhythmia, shock, emboli', 'Haemolysis: LDH better than plasma free Hb;', 'HeartMate II: 2.5 x upper limit of normal'], 'b0')
    b += _d4_lbox(360, 180, 350, 132, ['Outflow obstruction causes: kink, twist,', 'thrombosis, external compression (the', 'commonest; wrapping the graft lets blood', 'and debris collect). HeartMate 3: build-up', 'between bend relief and outflow mimics clot'], 'b0')
    b += _d4_lbox(10, 324, 340, 96, ['Work-up: log files to the manufacturer;', 'echo first (ramp study for HeartMate II,', 'HVAD); CT angiogram of the outflow graft;', 'right heart catheter if HF signs'], 'b1')
    b += _d4_lbox(360, 324, 350, 96, ['Treat: IV heparin (or bivalirudin); pump', 'exchange is definitive (I B); selected', 'centrifugal pumps: thrombolysis (IIa C);', 'recurrence: exchange to HeartMate 3 (IIb C)'], 'ok')
    return svg(430, b)


# ---------------------------------------------------------------- 13 temporary RVAD

def d4_temp_rvad():
    b = ''
    heads = [('Impella RP', ['Percutaneous, femoral vein:', 'IVC to MPA across the', 'pulmonary valve; up to 4.0', 'L/min; under 2 weeks']),
             ('Protek Duo + TandemHeart', ['Dual-lumen cannula from the', 'jugular: RA to MPA; patient', 'mobile; bedside removal;', 'oxygenator can be added']),
             ('CentriMag (right)', ['Surgical: femoral vein or', 'RA inflow, main PA outflow;', 'weeks; LV, RV or both;', 'oxygenator can be added'])]
    for k, (t, sub) in enumerate(heads):
        ox = 10 + k * 240
        b += T(ox + 115, 18, t, 'f-h')
        i = _d4_circ(hi=('RV',))
        if k == 0:
            i += _d4_pl([(74, 199), (96, 190), (96, 70), (74, 62)], 'f-cut', 4) + arrow(84, 66, 75, 62)
            i += '<circle cx="96" cy="108" r="9" class="f-ok"/>'
            i += T(104, 140, 'across PV', 'f-s', 'start')
        elif k == 1:
            i += _d4_pl([(74, 155), (112, 155), (112, 140)], 'f-l', 4)
            i += '<circle cx="112" cy="128" r="11" class="f-ok"/>'
            i += _d4_pl([(112, 116), (112, 62), (78, 59)], 'f-cut', 4) + arrow(90, 60, 75, 59)
            i += T(124, 90, 'jugular', 'f-s', 'start')
        else:
            i += _d4_pl([(74, 155), (112, 155), (112, 140)], 'f-l', 4)
            i += _d4_pl([(74, 199), (112, 186), (112, 160)], 'f-dash', 2)
            i += '<circle cx="112" cy="128" r="11" class="f-ok"/>'
            i += _d4_pl([(112, 116), (112, 62), (78, 59)], 'f-cut', 4) + arrow(90, 60, 75, 59)
        b += _d4_g(ox, 30, i)
        b += T(ox + 115, 266, sub, 'f-s')
    b += _d4_lbox(10, 342, 345, 112, ['Severe RV failure right after LVAD: temporary', 'RVAD at the index operation (I B); early tRVAD', 'in preference to VA-ECLS (IIa B). Recoverable', 'RV: temporary percutaneous RVAD; not', 'recoverable: durable BiVAD or TAH'], 'b1')
    b += _d4_lbox(365, 342, 345, 112, ['Not with: pulmonary haemorrhage, primary', 'pulmonary hypertensive crisis. PE rules out', 'right-sided mAFP or percutaneous RV support;', 'RA or caval thrombus rules out venous', 'cannulation'], 'warn')
    b += _d4_lbox(10, 464, 700, 60, ['Durable pump as RVAD: inflow low on the RA free wall facing the tricuspid orifice, shortened with felt spacers;', 'outflow graft narrowed, as a CF pump on low pulmonary impedance can out-pump the LVAD (pulmonary oedema)'], 'b0')
    return svg(534, b)


# ---------------------------------------------------------------- 14 PA catheter float

def _d4_smooth(pts):
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for k in range(len(pts) - 1):
        p0 = pts[max(k - 1, 0)]; p1 = pts[k]; p2 = pts[k + 1]; p3 = pts[min(k + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d


def d4_swan_float():
    y0, k = 300, 7.0          # y for 0 mmHg, px per mmHg

    def Y(p):
        return y0 - k * p
    b = ''
    for p in (0, 10, 20, 30):
        b += line(60, Y(p), 704, Y(p), 'f-grid') + T(52, Y(p) + 4, str(p), 'f-s', 'end')
    b += T(14, 70, 'mmHg', 'f-s', 'start')
    for x in (220, 380, 540):
        b += line(x, 70, x, y0, 'f-dash')
    zones = [(140, 'Right atrium', '2 to 6'), (300, 'Right ventricle', '25/3'), (460, 'Pulmonary artery', '25/10'), (622, 'Wedged', 'reflects LA: 6 to 12')]
    for x, n, v in zones:
        b += T(x, 52, n, 'f-h') + T(x, 70, v, 'f-s')
    pts = []
    # RA: small a, c, v waves between 2 and 6 mmHg
    for bx in (64, 142):
        pts += [(bx, 3), (bx + 14, 6), (bx + 24, 4.5), (bx + 32, 5), (bx + 42, 2.5), (bx + 58, 5.5), (bx + 70, 2.2)]
    # RV: diastole 0 to 3, systole 25
    for bx in (226, 302):
        pts += [(bx, 2), (bx + 6, 3), (bx + 14, 22), (bx + 22, 25), (bx + 36, 24), (bx + 46, 4), (bx + 52, 0.5), (bx + 70, 3)]
    # PA: systolic 25, dicrotic notch, diastole down to 10
    for bx in (386, 462):
        pts += [(bx, 11), (bx + 6, 10), (bx + 16, 23), (bx + 24, 25), (bx + 36, 19), (bx + 40, 17), (bx + 44, 18.5), (bx + 58, 13), (bx + 72, 10.5)]
    # Wedge: damped atrial-type waves, 8 to 11
    for bx in (546, 620):
        pts += [(bx, 9), (bx + 14, 11), (bx + 28, 8.5), (bx + 44, 11), (bx + 60, 8.2), (bx + 72, 9)]
    pts = [(x, Y(p)) for x, p in pts]
    b += f'<path d="{_d4_smooth(pts)}" class="f-l" style="stroke-width:2.6"/>'
    b += _d4_pl([(226, Y(25)), (530, Y(25))], 'f-cut', 1.6)
    b += T(380, Y(29.5), 'Systolic stays the same from RV to PA', 'f-h')
    b += arrow(370, Y(1), 370, Y(9.6)) + T(370, y0 + 18, 'diastolic rises (about 3 to 10)', 'f-s')
    b += T(622, Y(14), 'balloon inflated', 'f-s')
    b += _d4_lbox(10, 334, 345, 92, ['Right atrial (CVP) trace: a, c and v waves;', 'RV preload. Wedge (PCWP) is an indirect', 'measure of left atrial pressure: LV preload,', 'less reliable just after bypass'], 'b1')
    b += _d4_lbox(365, 334, 345, 92, ['From the same catheter: PA pressures,', 'thermodilution output, SVR and PVR,', 'and mixed venous saturation from PA', 'blood (normal 60 to 80%)'], 'b0')
    return svg(436, b)


# ---------------------------------------------------------------- 15 shock profiles

def d4_shock_profiles():
    cols = ['BP', 'CVP', 'Output', 'Wedge', 'SVR']
    rows = [('Failing, congested', ['Normal', 'High', 'Low', 'High', 'Normal or high'], ['Venodilator, diuretic,', 'inotrope']),
            ('Hypertensive', ['High', 'High', 'Normal', 'High', 'High'], ['Vasodilator']),
            ('Hypovolaemic', ['Low', 'Low', 'Low', 'Low', 'Normal'], ['Volume']),
            ('Cardiogenic shock', ['Low', 'High', 'Low', 'High', 'High'], ['Inotrope, balloon pump,', 'vasodilator']),
            ('Vasoplegic', ['Low', 'Normal or low', 'Normal or high', 'Normal or low', 'Low'], ['Alpha agonist'])]
    cw, x0, y0, rh = 84, 160, 36, 46
    b = T(10, 26, 'Pattern', 'f-h', 'start')
    for j, c in enumerate(cols):
        b += T(x0 + j * cw + cw / 2, 26, c, 'f-h')
    b += T(x0 + 5 * cw + 8, 26, 'Treatment', 'f-h', 'start')

    def cls(v):
        return 'warn' if v.startswith('High') else ('b1' if v.startswith('Low') else 'b0')
    for r, (name, vals, tx) in enumerate(rows):
        y = y0 + r * rh
        b += T(10, y + rh / 2 + 4, name, 'f-h', 'start')
        for j, v in enumerate(vals):
            words = v.split(' or ')
            lab = [words[0] + ' or', words[1]] if len(words) > 1 else [v]
            b += box(x0 + j * cw + 2, y + 3, cw - 4, rh - 6, lab, cls(v), 'f-s')
        b += T(x0 + 5 * cw + 8, y + rh / 2 + (4 if len(tx) == 1 else -4), tx, 'f-s', 'start')
    yb = y0 + len(rows) * rh + 10
    b += T(10, yb + 6, 'Red: high. Blue: low. Grey: normal (TSRA ch. 116).', 'f-s', 'start')
    b += _d4_lbox(10, yb + 18, 345, 92, ['Tamponade: drains stop suddenly with', 'instability; equal pressures on the catheter', '(left and right filling pressures equal)'], 'warn')
    b += _d4_lbox(365, yb + 18, 345, 92, ['RV failure: low output despite volume with a', 'normal LV. Atlas draft, unchecked: CVP over', '15, normal or low wedge, low index,', 'CVP to wedge ratio over 0.8'], 'b1')
    return svg(yb + 120, b)


# ---- figs_D5.py
"""D5 drawings: Fallot, transposition, truncus, arch obstruction, rings, duct and shunts.
Every label comes from the ST4 notes (corpus pages g8, g10, g11) or the TSRA chapter text."""
import math



# ---------------------------------------------------------------- helpers

def _d5_pts(spec, step=4.0):
    """Sample a path spec: ('M',x,y), ('L',x,y), ('C',x1,y1,x2,y2,x,y)."""
    pts, cur = [], None
    for s in spec:
        if s[0] == 'M':
            cur = (s[1], s[2])
            pts.append(cur)
        elif s[0] == 'L':
            x, y = s[1], s[2]
            n = max(1, int(math.hypot(x - cur[0], y - cur[1]) / step))
            for i in range(1, n + 1):
                t = i / n
                pts.append((cur[0] + (x - cur[0]) * t, cur[1] + (y - cur[1]) * t))
            cur = (x, y)
        elif s[0] == 'C':
            x1, y1, x2, y2, x, y = s[1:]
            est = (math.hypot(x1 - cur[0], y1 - cur[1]) + math.hypot(x2 - x1, y2 - y1)
                   + math.hypot(x - x2, y - y2))
            n = max(2, int(est / step))
            x0, y0 = cur
            for i in range(1, n + 1):
                t = i / n
                a, b_, c, d = (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3
                pts.append((a * x0 + b_ * x1 + c * x2 + d * x, a * y0 + b_ * y1 + c * y2 + d * y))
            cur = (x, y)
    return pts


def _d5_tube(spec, w, cls='f-lumen'):
    """A vessel drawn as a closed outline along a centreline; w is a width or a function of (x, y)."""
    p = _d5_pts(spec)
    n = len(p)
    left, right = [], []
    for i in range(n):
        a, c = p[max(0, i - 1)], p[min(n - 1, i + 1)]
        tx, ty = c[0] - a[0], c[1] - a[1]
        L = math.hypot(tx, ty) or 1
        nx, ny = -ty / L, tx / L
        wi = w(p[i][0], p[i][1]) if callable(w) else w
        left.append((p[i][0] + nx * wi / 2, p[i][1] + ny * wi / 2))
        right.append((p[i][0] - nx * wi / 2, p[i][1] - ny * wi / 2))
    ring = left + right[::-1]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in ring) + ' Z'
    return f'<path d="{d}" class="{cls}"/>'


def _d5_line_path(spec, cls='f-l', extra=''):
    p = _d5_pts(spec)
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in p)
    return f'<path d="{d}" class="{cls}"{extra}/>'


def _d5_poly(points, cls):
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in points) + ' Z'
    return f'<path d="{d}" class="{cls}"/>'


def _d5_circ(x, y, r, cls):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>'


def _d5_num(x, y, s, cls='f-b1'):
    return _d5_circ(x, y, 10, cls) + T(x, y + 5, s, 'f-h')


def _d5_sector(cx, cy, r, a0, a1, cls):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return (f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z" class="{cls}"/>')


def _d5_cutmark(x, y, ang, half=12):
    """Two short parallel red bars across a vessel at (x, y); ang is the vessel direction in degrees."""
    a = math.radians(ang + 90)
    dx, dy = math.cos(a) * half, math.sin(a) * half
    ox, oy = math.cos(math.radians(ang)) * 3, math.sin(math.radians(ang)) * 3
    return (line(x - dx - ox, y - dy - oy, x + dx - ox, y + dy - oy, 'f-cut')
            + line(x - dx + ox, y - dy + oy, x + dx + ox, y + dy + oy, 'f-cut'))


def _d5_dashcut(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="f-cut" stroke-dasharray="5 3"/>'


def _d5_compass(x, y, front=True):
    """Small orientation key. front=True: front view; otherwise axial seen from the feet."""
    b = arrow(x, y, x, y - 26) + arrow(x, y, x + 26, y)
    if front:
        b += T(x, y - 32, 'Head', 'f-s') + T(x + 32, y + 4, "Patient's left", 'f-s', 'start')
    else:
        b += T(x, y - 32, 'Anterior', 'f-s') + T(x + 32, y + 4, "Patient's left", 'f-s', 'start')
    return b


# ---------------------------------------------------------------- Fallot

def d5_tof_anatomy():
    b = T(12, 20, 'Tetralogy of Fallot: one malalignment, four features (front view, schematic)', 'f-h', 'start')
    # myocardium
    b += ('<path d="M40 330 C40 352 58 358 80 358 L344 358 C366 358 378 348 378 326 L378 210 '
          'C340 192 292 184 250 182 L176 182 L176 128 L150 110 L84 110 L80 134 C72 156 40 176 40 212 Z" class="f-b0"/>')
    # left PA (behind the aorta), with a waist
    b += _d5_poly([(122, 64), (282, 64), (292, 70), (302, 64), (330, 64), (330, 80), (302, 80),
                (292, 74), (282, 80), (122, 80)], 'f-b1')
    # main and right PA with a supravalvar waist
    b += _d5_poly([(98, 124), (100, 106), (96, 94), (96, 80), (26, 80), (26, 64), (124, 64),
                (124, 94), (120, 106), (126, 124)], 'f-b1')
    # aorta overriding the septum
    b += _d5_poly([(176, 186), (176, 36), (246, 36), (246, 186)], 'f-warn')
    # chambers (one lumen: VSD at the top of the septum)
    b += ('<path d="M66 326 L66 214 C66 186 86 168 94 152 L98 124 L126 124 L136 156 C142 172 156 182 176 186 '
          'L246 186 C276 194 330 198 362 212 L362 326 L224 326 L224 252 L198 252 L198 326 Z" class="f-lumen"/>')
    # small pulmonary valve leaflets
    b += '<path d="M99 124 L107 115 M125 124 L117 115" class="f-l" style="stroke-width:3"/>'
    # septoparietal band
    b += '<path d="M72 190 Q92 178 112 186" class="f-l" style="stroke-width:5"/>'
    # coronary crossing the outflow
    b += _d5_line_path([('M', 176, 168), ('C', 150, 172, 116, 196, 96, 218), ('C', 84, 234, 80, 260, 84, 300)],
                    'f-l', ' stroke-dasharray="6 4" style="stroke-width:2.5"')
    # displacement arrow on the conal septum
    b += arrow(170, 150, 140, 136)
    b += T(130, 344, 'RV', 'f-h') + T(300, 300, 'LV', 'f-h') + T(211, 56, 'Aorta', 'f-s')
    b += T(60, 58, 'RPA', 'f-s') + T(252, 58, 'LPA (behind aorta)', 'f-s', 'start')
    # numbered markers
    b += _d5_num(211, 232, '1', 'f-ok') + _d5_num(211, 112, '2', 'f-ok') + _d5_num(116, 158, '3', 'f-ok')
    b += _d5_num(292, 96, '3', 'f-ok') + line(292, 86, 292, 80) + _d5_num(53, 280, '4', 'f-ok')
    b += _d5_num(160, 152, 'S', 'f-warn')
    b += _d5_num(70, 252, 'C', 'f-warn')
    # legend
    x = 402
    rows = [('S', 'f-warn', ['Conal (outlet) septum malaligned', 'anterior and leftward: the cause', 'of all four features']),
            ('1', 'f-ok', ['VSD: large, malalignment type,', 'non-restrictive, under the', 'overriding aortic valve']),
            ('2', 'f-ok', ['Overriding (dextroposed) aorta']),
            ('3', 'f-ok', ['RVOT obstruction at many levels:', 'infundibulum (conal septum plus', 'septoparietal bands), small often',
                           'bicuspid valve, supravalvar waist,', 'branch PA stenosis (left > right)']),
            ('4', 'f-ok', ['RV hypertrophy']),
            ('C', 'f-warn', ['Commonest coronary anomaly: LAD', 'from the RCA crossing the RVOT', '(dashed): at risk at operation'])]
    y = 46
    for s, c, txt in rows:
        b += _d5_num(x + 10, y + 4, s, c) + T(x + 28, y + 8, txt, 'f-s', 'start')
        y += 17 * len(txt) + 10
    return svg(372, b)


def _d5_outflow(cx, kind):
    """RV outflow, annulus and main PA in profile; left wall is anterior."""
    top = [(-18, 100), (-52, 80), (-46, 68), (0, 90), (46, 68), (52, 80), (18, 100)]
    if kind == 'native':
        lw = [(-30, 262), (-30, 214), (-16, 190), (-16, 170), (-12, 160), (-18, 150)]
    elif kind in ('tap', 'mono'):
        lw = [(-30, 262), (-30, 226), (-40, 204), (-40, 130), (-30, 110), (-18, 102)]
    else:  # valve-sparing
        lw = [(-30, 262), (-30, 214), (-22, 190), (-22, 170), (-17, 160), (-20, 150)]
    rw = [(-x, y) for x, y in lw]
    if kind in ('tap', 'mono'):
        rw = [(30, 262), (30, 214), (21, 190), (21, 170), (14, 160), (18, 150)]
    pts = lw + top + rw[::-1]
    return _d5_poly([(cx + x, y) for x, y in pts], 'f-lumen')


def d5_tof_rvot():
    b = T(12, 20, 'Fallot repair: four ways to deal with the pulmonary valve (outflow in profile, anterior wall to the left)', 'f-h', 'start')
    cols = [95, 275, 455, 635]
    kinds = ['tap', 'mono', 'spare', 'conduit']
    heads = ['Transannular patch', 'Monocusp on the patch', 'Valve-sparing', 'RV-PA homograft conduit']
    texts = [['Small annulus (Z-score', 'below −2 for BSA); the', 'arteriotomy is carried into', 'an infundibulotomy.',
              'Free PI: RV dilatation,', 'arrhythmia, later PVR'],
             ['Single cusp of pericardium,', 'matrix or homograft sewn', 'on the patch. May restore',
              'competence; durability', 'uncertain'],
             ['Commissurotomy plus rigid', 'or balloon dilatation.', 'Moderate PS only: does',
              'not relieve severe RVOT', 'obstruction'],
             ['Pulmonary atresia, or a', 'coronary crossing the', 'infundibulum (dashed)']]
    for cx, k, h, tx in zip(cols, kinds, heads, texts):
        b += _d5_outflow(cx, 'native' if k == 'conduit' else k)
        b += T(cx, 42, h, 'f-h')
        if k in ('tap', 'mono'):
            b += _d5_line_path([('M', cx - 30, 226), ('L', cx - 40, 204), ('L', cx - 40, 130), ('L', cx - 30, 110), ('L', cx - 18, 102)],
                            'f-cut', ' style="stroke-width:6"')
            b += f'<path d="M{cx + 14} 160 L{cx + 5} 150" class="f-l" style="stroke-width:3"/>'
        if k == 'mono':
            b += f'<path d="M{cx - 40} 162 Q{cx - 24} 170 {cx - 8} 152" class="f-l" style="stroke-width:3"/>'
        if k == 'spare':
            b += f'<ellipse cx="{cx}" cy="160" rx="22" ry="9" class="f-dash"/>'
            b += arrow(cx - 24, 160, cx - 44, 160) + arrow(cx + 24, 160, cx + 44, 160)
            b += f'<path d="M{cx - 17} 160 L{cx - 9} 151 M{cx + 17} 160 L{cx + 9} 151" class="f-l" style="stroke-width:3"/>'
        if k == 'conduit':
            b += line(cx - 12, 160, cx + 12, 160, 'f-l') + line(cx - 12, 163, cx + 12, 163, 'f-l')
            b += T(cx + 22, 166, 'atretic', 'f-s', 'start')
            b += f'<line x1="{cx - 58}" y1="206" x2="{cx + 56}" y2="206" class="f-l" stroke-dasharray="6 4" style="stroke-width:2.5"/>'
            b += _d5_tube([('M', cx - 30, 236), ('C', cx - 86, 226, cx - 84, 108, cx - 22, 98)], 16, 'f-b0')
            b += line(cx - 80, 167, cx - 60, 167, 'f-l') + line(cx - 80, 172, cx - 60, 172, 'f-l')
        if k == 'tap':
            b += T(cx + 48, 180, ['patch', '(red)'], 'f-s', 'start')
        b += T(cx, 280, 'RV', 'f-s') if k != 'conduit' else T(cx + 10, 280, 'RV', 'f-s')
        b += T(cx - 84, 296 + 2, tx, 'f-s', 'start')
    b += box(10, 412, 700, 58, ['TSRA ch. 98: annulus Z-score below −2 traditionally means a transannular patch. Atlas draft (not checked):',
                                'spare the valve to about −2 to −2.5 and patch below −3. Whatever the choice: resect muscle bands, patch the VSD.'], 'b1', 'f-s')
    return svg(480, b)


# ---------------------------------------------------------------- transposition

def _d5_root(cx, ytop, cls, ybase=250):
    pts = [(cx - 20, ybase), (cx - 30, ybase - 18), (cx - 30, ybase - 52), (cx - 20, ybase - 72), (cx - 20, ytop),
           (cx + 20, ytop), (cx + 20, ybase - 72), (cx + 30, ybase - 52), (cx + 30, ybase - 18), (cx + 20, ybase)]
    return _d5_poly(pts, cls)


def d5_aso_steps():
    b = T(12, 20, 'Arterial switch with coronary transfer and the Lecompte manoeuvre (front view, schematic)', 'f-h', 'start')
    # panel 1
    o = 0
    a, p = o + 70, o + 165
    b += _d5_root(a, 52, 'f-warn') + _d5_root(p, 70, 'f-b1')
    b += _d5_circ(a + 22, 206, 5, 'f-b0') + _d5_circ(a + 20, 230, 5, 'f-b0')
    b += f'<line x1="{p + 20}" y1="104" x2="{o + 226}" y2="92" class="f-duct"/>' + _d5_cutmark(o + 206, 96, -10, 9)
    b += T(o + 222, 84, 'duct', 'f-s', 'end')
    b += _d5_dashcut(a - 34, 166, a + 34, 166) + _d5_dashcut(p - 34, 166, p + 34, 166)
    b += T(a, 46, 'Aorta (from RV)', 'f-s') + T(p, 64, 'PA (from LV)', 'f-s')
    b += T(a - 40, 262, ['ostia in the', 'facing sinuses'], 'f-s', 'start')
    b += T(o + 120, 300, ['1 Divide the duct; divide both', 'great arteries above the STJ'], 'f-s')
    # panel 2
    o = 240
    a, p = o + 70, o + 165
    b += _d5_root(a, 166, 'f-warn') + _d5_root(p, 166, 'f-b1')
    b += f'<circle cx="{a + 22}" cy="206" r="7" class="f-dash"/>' + f'<circle cx="{a + 20}" cy="230" r="7" class="f-dash"/>'
    b += _d5_circ(o + 117, 196, 8, 'f-warn') + _d5_circ(o + 117, 236, 8, 'f-warn')
    b += arrow(a + 30, 204, o + 108, 198) + arrow(a + 28, 232, o + 108, 236)
    b += arrow(o + 126, 196, p - 30, 204) + arrow(o + 126, 236, p - 30, 230)
    b += T(o + 117, 180, 'buttons', 'f-s')
    b += T(a, 132, ['neo-pulmonary', 'root'], 'f-s') + T(p, 132, ['neo-aortic', 'root'], 'f-s')
    b += T(o + 120, 300, ['2 Excise coronary buttons; sew them', 'into the facing sinuses of the', 'pulmonary root (the neo-aorta)'], 'f-s')
    # panel 3
    o = 480
    a, p = o + 70, o + 165
    b += _d5_root(p, 40, 'f-warn')
    b += _d5_circ(p - 22, 206, 5, 'f-b0') + _d5_circ(p - 20, 230, 5, 'f-b0')
    b += _d5_root(a, 166, 'f-b1')
    b += f'<rect x="{a + 16}" y="198" width="12" height="14" rx="3" class="f-b0"/>'
    b += f'<rect x="{a + 14}" y="222" width="12" height="14" rx="3" class="f-b0"/>'
    b += _d5_tube([('M', a, 172), ('C', a, 140, p - 40, 150, p - 40, 120), ('L', p - 40, 98)], 34, 'f-b1')
    b += _d5_tube([('M', o + 14, 96), ('L', o + 232, 96)], 22, 'f-b1')
    b += f'<rect x="{p - 56}" y="90" width="32" height="20" class="f-b1" style="stroke:none"/>'
    b += T(p + 28, 60, 'aorta', 'f-s', 'start') + T(o + 24, 78, 'RPA', 'f-s') + T(o + 222, 78, 'LPA', 'f-s')
    b += T(a - 40, 262, ['pericardial patch', 'at the button sites'], 'f-s', 'start')
    b += T(o + 120, 300, ['3 Lecompte: PA bifurcation in front', 'of the aorta; neo-aorta to ascending', 'aorta; neo-PA root to PA; close VSD', 'via the RA, then the ASD'], 'f-s')
    b += line(240, 40, 240, 290, 'f-grid') + line(480, 40, 480, 290, 'f-grid')
    b += box(10, 372, 345, 76, ['Early: coronary ischaemia from inadequate', 'or malpositioned transfer (main concern);',
                                'anastomotic problems; rarely valve injury'], 'warn', 'f-s')
    b += box(365, 372, 345, 76, ['Late: RVOT obstruction (commonest reason', 'to reoperate), coronary stenosis,',
                                 'neo-aortic root dilatation with AR'], 'b1', 'f-s')
    return svg(458, b)


def d5_tga_leiden():
    b = T(12, 20, 'D-TGA coronaries: the Leiden convention (great arteries in cross-section, arrangement schematic)', 'f-h', 'start')
    ax, ay, r = 190, 150, 56
    px, py = 330, 262
    b += _d5_circ(px, py, 44, 'f-b1') + T(px, py + 5, 'PA', 'f-h')
    b += _d5_sector(ax, ay, r, 165, 285, 'f-b0') + _d5_sector(ax, ay, r, 285, 405, 'f-ok') + _d5_sector(ax, ay, r, 45, 165, 'f-b1')
    b += T(ax + 34, ay - 4, '1', 'f-h') + T(ax - 4, ay + 38, '2', 'f-h') + T(ax - 34, ay - 26, 'NF', 'f-s')
    # coronaries
    sx, sy = ax + r * math.cos(math.radians(-15)), ay + r * math.sin(math.radians(-15))
    b += _d5_line_path([('M', sx, sy), ('C', sx + 30, sy - 8, sx + 50, sy - 10, sx + 64, sy - 14)], 'f-l', ' style="stroke-width:3"')
    b += _d5_line_path([('M', sx + 64, sy - 14), ('C', sx + 80, sy - 30, sx + 92, sy - 50, sx + 104, sy - 70)], 'f-l', ' style="stroke-width:3"')
    b += _d5_line_path([('M', sx + 64, sy - 14), ('C', sx + 90, sy - 8, sx + 110, sy + 6, sx + 126, sy + 24)], 'f-l', ' style="stroke-width:3"')
    tx, ty = ax + r * math.cos(math.radians(105)), ay + r * math.sin(math.radians(105))
    b += _d5_line_path([('M', tx, ty), ('C', tx - 10, ty + 30, tx - 30, ty + 56, tx - 56, ty + 80)], 'f-l', ' style="stroke-width:3"')
    b += T(sx + 108, sy - 76, 'LAD', 'f-s', 'start') + T(sx + 132, sy + 30, 'Cx', 'f-s', 'start')
    b += T(sx + 30, sy - 18, 'left main', 'f-s') + T(tx - 62, ty + 96, 'RCA', 'f-s')
    # observer
    ex, ey = ax + 16 * math.cos(math.radians(220)), ay + 16 * math.sin(math.radians(220))
    b += _d5_circ(ex, ey, 6, 'f-warn') + arrow(ex + 6, ey + 6, ax + 18, ay + 18)
    b += line(ex - 6, ey + 4, 124, 160, 'f-l') + T(14, 166, ['Observer in the', 'non-facing sinus', '(NF), facing the PA'], 'f-s', 'start')
    b += T(ax, ay - r - 10, 'Aorta (anterior, rightward)', 'f-s')
    b += _d5_compass(560, 92, front=False) + T(560, 112, ['Seen from the feet, as on CT'], 'f-s')
    x = 410
    b += T(x, 160, 'Sinus 1 = observer\'s right hand', 'f-h', 'start')
    b += T(x, 180, 'Sinus 2 = observer\'s left hand', 'f-h', 'start')
    b += T(x, 206, ['Commonest pattern 1LCx2R: left main', '(LAD and Cx) from sinus 1, the anterior-', 'leftward sinus; RCA from sinus 2,',
                    'the posterior-rightward sinus.', 'Coronaries usually arise from the', 'two sinuses facing the PA.'], 'f-s', 'start')
    h, bb = bars([('Usual, two separate ostia', (60, 65), 'ok'), ('Circumflex from RCA', (20, 22), 'b1'),
                  ('Single RCA', (9, 10), 'b1'), ('Single LCA', (2, 3), 'b1'), ('Inverted origins', (2, 3), 'b1')],
                 '%', 100, 'Coronary patterns in D-TGA (TSRA ch. 104)', 230)
    foot = T(12, 340 + h + 4, 'Origin from a non-facing sinus (rare) and intramural or between-artery courses make transfer harder.', 'f-s', 'start')
    return svg(340 + h + 14, b + f'<g transform="translate(0 330)">{bb}</g>' + foot)


def _d5_heart2(o, vsd=True):
    """Two-ventricle block: RV left, LV right, VSD at the top of the septum."""
    b = f'<rect x="{o + 10}" y="172" width="210" height="112" rx="18" class="f-b0"/>'
    if vsd:
        b += (f'<path d="M{o + 24} 184 L{o + 206} 184 L{o + 206} 270 L{o + 122} 270 L{o + 122} 218 '
              f'L{o + 108} 218 L{o + 108} 270 L{o + 24} 270 Z" class="f-lumen"/>')
    b += T(o + 60, 262, 'RV', 'f-s') + T(o + 170, 262, 'LV', 'f-s')
    return b


def d5_rastelli():
    b = T(12, 20, 'TGA with VSD and pulmonary stenosis: three ways to route LV to aorta (front view, schematic)', 'f-h', 'start')
    for i, (name, txt) in enumerate([
            ('Rastelli', ['Baffle: LV through the VSD', 'to the aorta. Valved conduit', 'from RV to distal PA']),
            ('REV', ['Same baffle. PA bifurcation', 'sewn straight onto the RV,', 'no conduit; subvalvar muscle',
                     'resected so the baffle is not', 'obstructed. Leaves PR']),
            ('Nikaidoh', ['Aortic root with coronaries', 'moved back into the LVOT', '(old pulmonary valve site);',
                          'VSD patched; RVOT rebuilt', 'round the aortic root'])]):
        o = i * 240
        b += T(o + 120, 46, name, 'f-h')
        if i < 2:
            b += _d5_tube([('M', o + 165, 186), ('L', o + 165, 160)], 28, 'f-b1')
            b += _d5_cutmark(o + 165, 168, 90, 18)
            b += _d5_heart2(o)
            b += _d5_tube([('M', o + 60, 186), ('L', o + 60, 70)], 34, 'f-warn')
            b += T(o + 60, 64, 'aorta', 'f-s')
            b += f'<path d="M{o + 150} 186 C{o + 140} 226 {o + 92} 230 {o + 76} 186" class="f-cut" style="stroke-width:5"/>'
            b += f'<path d="M{o + 170} 240 C{o + 150} 214 {o + 100} 216 {o + 66} 150" class="f-l" stroke-dasharray="4 3" marker-end="url(#ah)"/>'
        if i == 0:
            b += _d5_tube([('M', o + 30, 220), ('C', o + 6, 190, o + 10, 96, o + 60, 100), ('L', o + 150, 100)], 18, 'f-b0')
            b += _d5_tube([('M', o + 150, 100), ('L', o + 210, 100)], 18, 'f-b1')
            b += line(o + 3, 150, o + 27, 150, 'f-l') + line(o + 3, 155, o + 27, 155, 'f-l')
            b += T(o + 196, 90, 'PA', 'f-s') + T(o + 96, 86, 'conduit', 'f-s', 'start')
            b += T(o + 188, 150, 'PA', 'f-s', 'start') + T(o + 188, 166, 'closed', 'f-s', 'start')
        if i == 1:
            b += _d5_tube([('M', o + 34, 186), ('C', o + 20, 130, o + 70, 104, o + 150, 100), ('L', o + 214, 100)], 22, 'f-b1')
            b += f'<rect x="{o + 82}" y="190" width="22" height="18" rx="4" class="f-warn"/>'
            b += T(o + 196, 90, 'PA', 'f-s') + T(o + 188, 150, 'PA', 'f-s', 'start') + T(o + 188, 166, 'closed', 'f-s', 'start')
            b += line(o + 92, 196, o + 92, 300, 'f-grid')
            b += T(o + 98, 316, 'muscle resected', 'f-s', 'start')
        if i == 2:
            b += _d5_heart2(o)
            b += f'<rect x="{o + 43}" y="70" width="34" height="114" class="f-dash"/>'
            b += _d5_tube([('M', o + 50, 186), ('C', o + 30, 140, o + 40, 104, o + 70, 100), ('L', o + 214, 100)], 22, 'f-b1')
            b += _d5_tube([('M', o + 140, 186), ('L', o + 140, 64)], 34, 'f-warn')
            b += line(o + 108, 186, o + 122, 186, 'f-cut') + f'<path d="M{o + 108} 186 L{o + 122} 218" class="f-cut" style="stroke-width:5"/>'
            b += arrow(o + 80, 140, o + 120, 140)
            b += T(o + 140, 58, 'aorta', 'f-s') + T(o + 200, 90, 'PA', 'f-s') + T(o + 60, 62, 'old site', 'f-s')
            b += line(o + 116, 210, o + 116, 290, 'f-grid') + T(o + 122, 304, 'VSD patch', 'f-s', 'start')
        b += T(o + 18, 336, txt, 'f-s', 'start')
        if i:
            b += line(o, 40, o, 410, 'f-grid')
    b += T(12, 440, 'Why not a switch: an arterial switch would leave the LVOT obstruction. Operate at about 6 months, with an aortopulmonary', 'f-s', 'start')
    b += T(12, 457, 'shunt meanwhile if needed. Red curve: baffle; red bars: PA divided; dashed arrow: LV blood to the aorta.', 'f-s', 'start')
    return svg(468, b)


# ---------------------------------------------------------------- truncus

def d5_truncus_types():
    b = T(12, 20, 'Truncus arteriosus: Collett-Edwards types with the Van Praagh equivalents (front view, schematic)', 'f-h', 'start')
    heads = ['Collett-Edwards I', 'II', 'III', 'IV']
    texts = [['Main PA off the trunk,', 'then branches; commonest', 'Van Praagh A1 (or B1)'],
             ['Branch PAs arise close', 'together from the', 'posterior trunk', 'Van Praagh A2'],
             ['Branch PAs from separate,', 'widely spaced origins', 'Van Praagh A2'],
             ['No branch PAs off the', 'trunk; collaterals (thin', 'tubes) from the descending', 'aorta (really pulmonary', 'atresia)']]
    for i, cx in enumerate([95, 275, 455, 635]):
        b += T(cx, 46, heads[i], 'f-h')
        b += f'<rect x="{cx - 62}" y="250" width="124" height="52" rx="12" class="f-b0"/>'
        b += (f'<path d="M{cx - 54} 258 L{cx + 54} 258 L{cx + 54} 294 L{cx + 5} 294 L{cx + 5} 272 '
              f'L{cx - 5} 272 L{cx - 5} 294 L{cx - 54} 294 Z" class="f-lumen"/>')
        b += T(cx - 30, 290, 'RV', 'f-s') + T(cx + 30, 290, 'LV', 'f-s')
        if i == 0:
            b += _d5_tube([('M', cx - 52, 140), ('L', cx - 86, 154)], 14, 'f-b1')
            b += _d5_tube([('M', cx - 52, 140), ('L', cx - 62, 100)], 14, 'f-b1')
            b += _d5_tube([('M', cx - 10, 172), ('L', cx - 52, 140)], 22, 'f-b1')
        if i == 1:
            b += _d5_tube([('M', cx, 160), ('L', cx - 84, 146)], 14, 'f-b1') + _d5_tube([('M', cx, 160), ('L', cx + 84, 146)], 14, 'f-b1')
        if i == 2:
            b += _d5_tube([('M', cx, 196), ('L', cx - 84, 180)], 14, 'f-b1') + _d5_tube([('M', cx, 118), ('L', cx + 84, 102)], 14, 'f-b1')
        if i < 3:
            b += _d5_tube([('M', cx, 258), ('L', cx, 66)], 40, 'f-warn')
            b += f'<path d="M{cx - 19} 258 L{cx - 8} 247 M{cx + 19} 258 L{cx + 8} 247" class="f-l" style="stroke-width:3"/>'
        else:
            for yy in (160, 196):
                b += _d5_tube([('M', cx + 40, yy), ('L', cx + 72, yy - 10)], 6, 'f-b1')
            b += _d5_tube([('M', cx - 16, 258), ('L', cx - 16, 110), ('C', cx - 16, 66, cx + 40, 66, cx + 40, 110), ('L', cx + 40, 240)], 30, 'f-warn')
            b += f'<path d="M{cx - 30} 258 L{cx - 22} 248 M{cx - 2} 258 L{cx - 10} 248" class="f-l" style="stroke-width:3"/>'
        if i == 1:
            b += f'<circle cx="{cx - 8}" cy="160" r="6" class="f-dash"/>' + f'<circle cx="{cx + 8}" cy="160" r="6" class="f-dash"/>'
        b += T(cx - 80, 322, texts[i], 'f-s', 'start')
        if i:
            b += line(cx - 90, 36, cx - 90, 380, 'f-grid')
    b += T(95, 62, 'trunk', 'f-s')
    b += box(10, 396, 700, 74, ['Van Praagh: A = with VSD, B = without. A3: one branch PA absent (unilateral atresia), collateral supply to that',
                                'lung. A4: interrupted or hypoplastic arch, or coarctation: pulmonary dominant, duct-dependent descending aorta.',
                                'Truncal valve (TSRA): three leaflets 70%, four 20%, two 10%; thick, malformed, often regurgitant.'], 'b1', 'f-s')
    return svg(480, b)


def d5_truncus_repair():
    b = T(12, 20, 'Truncus repair (no arch abnormality): before and after (front view, schematic)', 'f-h', 'start')
    for i, o in enumerate([0, 360]):
        b += f'<rect x="{o + 80}" y="232" width="190" height="80" rx="16" class="f-b0"/>'
        b += (f'<path d="M{o + 92} 244 L{o + 258} 244 L{o + 258} 300 L{o + 178} 300 L{o + 178} 266 '
              f'L{o + 164} 266 L{o + 164} 300 L{o + 92} 300 Z" class="f-lumen"/>')
        b += T(o + 112, 292, 'RV', 'f-s') + T(o + 236, 292, 'LV', 'f-s')
        b += T(o + 175, 52, ['Before', 'After'][i], 'f-h')
    # before
    o = 0
    b += _d5_tube([('M', o + 100, 130), ('L', o + 56, 150)], 14, 'f-b1') + _d5_tube([('M', o + 100, 130), ('L', o + 84, 86)], 14, 'f-b1')
    b += _d5_tube([('M', o + 156, 170), ('L', o + 100, 130)], 22, 'f-b1')
    b += _d5_tube([('M', o + 171, 244), ('L', o + 171, 64)], 44, 'f-warn')
    b += f'<ellipse cx="{o + 64}" cy="146" rx="9" ry="13" class="f-cut"/>' + f'<ellipse cx="{o + 86}" cy="94" rx="13" ry="9" class="f-cut"/>'
    b += f'<rect x="{o + 140}" y="76" width="62" height="8" rx="3" class="f-b1"/>'
    b += T(o + 210, 84, 'clamp high', 'f-s', 'start') + T(o + 40, 186, ['snare PAs', 'on bypass'], 'f-s', 'start')
    b += T(o + 171, 160, 'trunk', 'f-s')
    # after
    o = 360
    b += _d5_tube([('M', o + 70, 108), ('L', o + 26, 128)], 14, 'f-b1') + _d5_tube([('M', o + 70, 108), ('L', o + 54, 64)], 14, 'f-b1')
    b += _d5_tube([('M', o + 118, 248), ('C', o + 60, 230, o + 50, 150, o + 70, 112)], 20, 'f-b0')
    b += line(o + 53, 186, o + 77, 186, 'f-l') + line(o + 53, 191, o + 77, 191, 'f-l')
    b += _d5_tube([('M', o + 171, 244), ('L', o + 171, 64)], 44, 'f-warn')
    b += f'<path d="M{o + 149} 150 L{o + 149} 182" class="f-cut" style="stroke-width:6"/>'
    b += f'<path d="M{o + 164} 266 L{o + 178} 244" class="f-cut" style="stroke-width:5"/>'
    b += _d5_cutmark(o + 112, 240, 90, 12)
    b += T(o + 171, 120, 'aorta', 'f-s')
    b += line(o + 146, 166, o + 210, 120, 'f-l') + T(o + 214, 116, ['PA site closed,', 'with or without', 'a patch'], 'f-s', 'start')
    b += T(o + 4, 230, ['conduit', '(valved)'], 'f-s', 'start')
    b += line(o + 176, 256, o + 262, 214, 'f-l') + T(o + 266, 210, ['VSD patch', '(via RV)'], 'f-s', 'start')
    b += T(o + 10, 330, 'Red bars: ventriculotomy, in an avascular part of the RVOT', 'f-s', 'start')
    b += line(355, 40, 355, 320, 'f-grid')
    steps = ['1  Full-flow bypass, moderate hypothermia: distal ascending aortic cannula at the base of the innominate; bicaval; LV vent',
             '    via the right superior pulmonary vein. 2  Snare the PAs as soon as bypass starts, to preserve systemic flow.',
             '3  Clamp the trunk as distally as possible; cardioplegia antegrade, or retrograde if truncal regurgitation is significant.',
             '4  Excise the PAs as a button; repair the trunk defect, with or without a patch; look at the coronaries directly.',
             '5  Ventriculotomy; patch the VSD through it. Close ASD or PFO via the RA, or leave a PFO as a pop-off.',
             '6  Conduit: distal end to the PA confluence, proximal end to the ventriculotomy, with a hood if needed.']
    b += f'<rect x="10" y="346" width="700" height="118" rx="9" class="f-b0"/>' + T(22, 368, steps, 'f-s', 'start')
    return svg(474, b)


# ---------------------------------------------------------------- arch obstruction

def d5_iaa():
    t = T(12, 20, 'Interrupted aortic arch: types A, B and C (front view, schematic)', 'f-h', 'start')
    b = ''
    data = [('Type A: 30%', 164, 196, ['Distal to left subclavian,', 'before the duct inserts;', 'linked with AP window']),
            ('Type B: 65%', 124, 136, ['Between left carotid and', 'left subclavian; commonest;', 'almost all have a VSD;', 'linked with 22q11 deletion']),
            ('Type C: 5%', 84, 96, ['Between innominate and', 'left carotid; very rare'])]
    for i, (head, g0, g1, txt) in enumerate(data):
        o = i * 240
        b += T(o + 120, 6, head, 'f-h')
        b += _d5_tube([('M', o + 116, 300), ('L', o + 128, 214)], 26, 'f-b1')
        b += _d5_tube([('M', o + 128, 214), ('L', o + 196, 176)], 16, 'f-b1')
        for x, lab in ((70, 'In'), (110, 'LC'), (150, 'LS')):
            b += _d5_tube([('M', o + x, 80), ('L', o + x, 34)], 10, 'f-warn') + T(o + x, 28, lab, 'f-s')
        asc = [('M', o + 40, 300), ('L', o + 40, 120), ('C', o + 40, 88, o + 54, 76, o + 80, 76)]
        if i == 0:
            prox = asc + [('L', o + g0, 76)]
            dist = [('M', o + 196, 118), ('L', o + 196, 300)]
            b += f'<path d="M{o + g0 + 4} 76 C{o + 186} 78 {o + 196} 96 {o + 196} 112" class="f-dash"/>'
        else:
            prox = asc + [('L', o + g0, 76)]
            dist = [('M', o + g1, 76), ('L', o + 160, 76), ('C', o + 188, 76, o + 196, 96, o + 196, 124), ('L', o + 196, 300)]
            b += line(o + g0 + 2, 76, o + g1 - 2, 76, 'f-dash')
        b += _d5_tube(prox, 22, 'f-warn') + _d5_tube(dist, 22, 'f-warn')
        b += T(o + 40, 316, 'Ao', 'f-s') + T(o + 116, 316, 'PA', 'f-s') + T(o + 196, 316, 'DAo', 'f-s')
        b += T(o + 162, 234, 'duct', 'f-s')
        b += T(o + 16, 340, txt, 'f-s', 'start')
        if i:
            b += line(o, 36, o + 0.1, 400, 'f-grid')
    b += T(12, 420, 'In innominate · LC left carotid · LS left subclavian · DAo descending aorta. Dashed: the gap (sometimes a fibrous cord).', 'f-s', 'start')
    b += T(12, 437, 'Everything beyond the gap depends on the duct: prostaglandin at diagnosis; irradiated blood until DiGeorge is excluded.', 'f-s', 'start')
    b += box(10, 452, 450, 102, ['One-stage repair: arterial cannulas in the ascending aorta and', 'the duct; DHCA or regional cerebral perfusion (neither shown',
                                 'better); wide mobilisation; resect all ductal tissue; distal', 'transverse arch to proximal descending aorta, with or without',
                                 'a patch; close the VSD; resect prominent conal tissue'], 'ok', 'f-s')
    b += box(470, 452, 240, 102, ['30-day mortality 10 to 15%', 'Commonest reoperation:', 'subaortic stenosis (about 20%);',
                                  'next, recurrent arch', 'obstruction'], 'warn', 'f-s')
    return svg(564 + 40, t + f'<g transform="translate(0 40)">{b}</g>')


def _d5_coarc_w(x, y):
    if y < 110:
        return 26
    return 26 - 15 * math.exp(-((y - 146) / 9) ** 2)


def d5_coarct_repair():
    t = T(12, 20, 'Neonatal coarctation: resection and end-to-end anastomosis (front view, schematic)', 'f-h', 'start')
    b = ''
    heads = ['1 Anatomy', '2 Resect', '3 Join end to end']
    arch = [('M', 10, 80), ('L', 120, 80), ('C', 160, 80, 170, 100, 170, 130), ('L', 170, 300)]
    for i in range(3):
        o = i * 240
        sp = [(s[0],) + tuple(v + (o if k % 2 == 0 else 0) for k, v in enumerate(s[1:])) for s in arch]
        b += T(o + 120, 6, heads[i], 'f-h')
        b += _d5_tube([('M', o + 50, 80), ('L', o + 50, 30)], 10, 'f-warn') + _d5_tube([('M', o + 100, 80), ('L', o + 100, 30)], 10, 'f-warn')
        b += T(o + 50, 24, 'LC', 'f-s') + T(o + 100, 24, 'LS', 'f-s')
        b += _d5_tube([('M', o + 50, 300), ('L', o + 84, 214)], 26, 'f-b1')
        if i == 0:
            b += f'<line x1="{o + 86}" y1="214" x2="{o + 160}" y2="164" class="f-duct"/>'
            b += _d5_tube(sp, _d5_coarc_w, 'f-warn')
            b += _d5_line_path([('M', o + 140, 20), ('L', o + 136, 150), ('C', o + 134, 214, o + 112, 222, o + 108, 196), ('L', o + 100, 120)],
                            'f-nerve')
            b += line(o + 180, 146, o + 196, 146, 'f-l') + T(o + 200, 140, ['coarc-', 'tation'], 'f-s', 'start')
            b += T(o + 112, 250, 'duct', 'f-s') + T(o + 8, 140, ['left RLN', 'hooks round', 'the duct'], 'f-s', 'start')
            b += T(o + 14, 324, ['Just proximal to the duct, distal', 'to the left subclavian. Chronic:', 'intercostal, internal mammary',
                                 'and scapular collaterals'], 'f-s', 'start')
        elif i == 1:
            b += f'<line x1="{o + 86}" y1="214" x2="{o + 112}" y2="197" class="f-duct"/>'
            b += f'<line x1="{o + 134}" y1="182" x2="{o + 160}" y2="164" class="f-duct"/>'
            b += _d5_cutmark(o + 104, 202, -34, 7)
            b += _d5_tube(sp, _d5_coarc_w, 'f-warn')
            b += f'<rect x="{o + 148}" y="124" width="44" height="52" rx="4" class="f-dash"/>'
            b += _d5_dashcut(o + 148, 124, o + 192, 124) + _d5_dashcut(o + 148, 176, o + 192, 176)
            b += T(o + 14, 324, ['Duct ligated and divided. Resect the', 'narrow segment with as much ductal', 'tissue as possible (dashed box)'],
                   'f-s', 'start')
        else:
            b += f'<line x1="{o + 86}" y1="214" x2="{o + 112}" y2="197" class="f-duct"/>' + _d5_cutmark(o + 104, 202, -34, 7)
            b += _d5_tube(sp, 26, 'f-warn')
            b += '<path d="' + ' '.join(f'M{o + 157 + k * 4} 146 L{o + 159 + k * 4} 154' for k in range(7)) + '" class="f-cut"/>'
            b += T(o + 14, 324, ['Direct or extended end-to-end', 'anastomosis (red stitches), off', 'bypass, left posterolateral',
                                 'thoracotomy'], 'f-s', 'start')
        b += T(o + 26, 286, 'PA', 'f-s')
        if i:
            b += line(o, 36, o + 0.1, 390, 'f-grid')
    b += box(10, 400, 345, 94, ['At risk: thoracic duct (chylothorax: drain out only', 'after the first day of feeding); recurrent laryngeal',
                                'nerve (hoarse cry: aspiration risk, ENT and SALT', 'review); phrenic nerve; paraplegia under 0.5%'], 'warn', 'f-s')
    b += box(365, 400, 345, 94, ['After: tight BP control (post-coarctation syndrome:', 'ileus, mesenteric vasculitis); lifelong arm and leg',
                                 'BP. Recoarctation 3 to 15% in neonates and infants:', 'balloon angioplasty is the treatment of choice'], 'b1', 'f-s')
    b += T(12, 514, 'Not drawn: subclavian flap aortoplasty (out of favour: long-term limb problems); tube graft (adults only).', 'f-s', 'start')
    return svg(524 + 40, t + f'<g transform="translate(0 40)">{b}</g>')


def d5_pda_rln():
    t = T(12, 20, 'The duct and the left recurrent laryngeal nerve (front view, arrangement schematic)', 'f-h', 'start')
    b = ''
    b += _d5_tube([('M', 160, 360), ('L', 186, 262)], 34, 'f-b1')
    b += _d5_tube([('M', 200, 250), ('L', 290, 186)], 18, 'f-ok')
    for x, top, lab in ((110, 34, 'Left carotid'), (190, 34, 'Left subclavian')):
        b += _d5_tube([('M', x, 104), ('L', x, top)], 14, 'f-warn') + T(x, top - 8, lab, 'f-s')
    b += _d5_tube([('M', 20, 104), ('L', 220, 104), ('C', 276, 104, 300, 126, 300, 170), ('L', 300, 360)], 34, 'f-warn')
    b += _d5_tube([('M', 186, 256), ('L', 410, 240)], 22, 'f-b1')
    b += _d5_line_path([('M', 262, 30), ('L', 256, 150), ('C', 254, 218, 262, 236, 240, 244), ('C', 220, 250, 212, 230, 212, 204),
                     ('L', 204, 60)], 'f-nerve')
    b += _d5_cutmark(250, 214, -35, 10)
    b += _d5_line_path([('M', 96, 150), ('C', 100, 220, 112, 280, 120, 350)], 'f-nerve', ' stroke-dasharray="6 4"')
    b += T(60, 96, 'Arch', 'f-s') + T(320, 330, ['Descending', 'aorta'], 'f-s', 'start') + T(150, 380, 'Main PA', 'f-s')
    b += T(392, 226, 'LPA', 'f-s') + T(205, 208, 'duct', 'f-s', 'end')
    b += line(270, 236, 330, 270, 'f-l') + T(334, 276, ['Left recurrent', 'laryngeal nerve'], 'f-s', 'start')
    b += T(28, 170, ['Phrenic', '(dashed)'], 'f-s', 'start')
    b += line(255, 222, 330, 200, 'f-l') + T(334, 196, 'clip or ties', 'f-s', 'start')
    x = 440
    b += T(x, 52, 'Why the nerve is there (TSRA ch. 91)', 'f-h', 'start')
    b += T(x, 72, ['The duct is the persistent left 6th arch:', 'aortic end distal to the left subclavian,', 'pulmonary end at the MPA-LPA junction.',
                   'The left RLN loops round it. On the right', 'the 6th arch disappears, so the right RLN', 'hooks round the subclavian (4th arch).'],
           'f-s', 'start')
    b += T(x, 188, 'Surgical closure', 'f-h', 'start')
    b += T(x, 208, ['Clip, ligation, or double ligation and', 'division (thoracotomy, sternotomy or', 'VATS). Preterm: left thoracotomy, clip.',
                    'Hard part: telling PAs, left subclavian,', 'distal arch, descending aorta and duct', 'apart; find and avoid the phrenic and', 'left recurrent laryngeal nerves.'],
           'f-s', 'start')
    b += box(x - 6, 336, 276, 58, ['Left RLN injury on laryngoscopy in up', 'to 25% of preterm infants after closure'], 'warn', 'f-s')
    return svg(404 + 30, t + f'<g transform="translate(0 30)">{b}</g>')


# ---------------------------------------------------------------- vascular rings

def d5_ring_daa():
    b = T(12, 20, 'Double aortic arch: the complete ring and where to divide it (axial, seen from the feet)', 'f-h', 'start')
    b += _d5_tube([('M', 316, 76), ('C', 380, 90, 394, 150, 388, 200), ('C', 384, 230, 380, 244, 376, 254)], 14, 'f-warn')
    b += _d5_tube([('M', 286, 76), ('C', 216, 88, 206, 150, 214, 200), ('C', 222, 262, 282, 278, 346, 270)], 26, 'f-warn')
    b += _d5_circ(300, 64, 22, 'f-warn') + T(300, 69, 'AAo', 'f-s')
    b += _d5_circ(372, 264, 20, 'f-warn') + T(372, 269, 'DAo', 'f-s')
    b += _d5_circ(300, 160, 28, 'f-b0') + T(300, 164, 'Trachea', 'f-s')
    b += _d5_circ(300, 230, 20, 'f-b0') + T(300, 234, 'Oes', 'f-s')
    for x, y, lab, side in ((236, 98, 'Right carotid', 'end'), (214, 140, 'Right subclavian', 'end'),
                            (364, 98, 'Left carotid', 'start'), (390, 140, 'Left subclavian', 'start')):
        b += _d5_circ(x, y, 7, 'f-b0')
        b += T(x - 14 if side == 'end' else x + 14, y + 5, lab, 'f-s', side)
    b += _d5_circ(452, 186, 15, 'f-b1') + T(452, 190, 'LPA', 'f-s')
    b += f'<path d="M444 198 C430 230 410 252 390 262" class="f-dash" style="stroke-width:2.5"/>'
    b += T(440, 238, 'ligamentum', 'f-s', 'start')
    b += _d5_cutmark(384, 226, 100, 12) + _d5_cutmark(420, 236, 140, 9)
    b += T(136, 222, ['Right arch', '(dominant in 80%):', 'right of trachea,', 'behind oesophagus'], 'f-s')
    b += T(340, 36, ['Left arch: in front of', 'and left of the trachea'], 'f-s', 'start')
    b += _d5_compass(60, 330, front=False)
    x = 520
    b += T(x, 52, 'Dominant arch', 'f-h', 'start')
    for k, (lab, v) in enumerate((('Right', '80%'), ('Left', '10%'), ('Balanced', '10%'))):
        b += T(x, 74 + k * 18, lab, 'f-s', 'start') + T(x + 120, 74 + k * 18, v, 'f-n', 'start')
    b += T(x, 146, 'Repair every double arch', 'f-h', 'start')
    b += T(x, 166, ['Symptoms or not. Muscle-', 'sparing thoracotomy, 3rd or', '4th space, on the side of the',
                    'lesser arch (usually left).', 'Test-clamp to confirm flow;', 'divide the lesser arch where',
                    'it joins the descending aorta,', 'and the ligamentum (red', 'bars); free the bands round',
                    'trachea and oesophagus.'], 'f-s', 'start')
    b += box(10, 358, 700, 44, ['An atretic left arch leaves a fibrous remnant invisible on CT or MR: look for secondary signs and warn the surgeon.'],
             'b1', 'f-s')
    return svg(412, b)


def _d5_raa_base(cx, mirror):
    b = _d5_tube([('M', cx - 14, 72), ('C', cx - 90, 88, cx - 92, 180, cx - 60, 228), ('C', cx - 40, 262, cx + 10, 262, cx + 44, 250)], 22, 'f-warn')
    b += _d5_circ(cx, 62, 20, 'f-warn') + T(cx, 67, 'AAo', 'f-s')
    b += _d5_circ(cx + 50, 248, 17, 'f-warn') + T(cx + 50, 252, 'DAo', 'f-s')
    b += _d5_circ(cx, 150, 26, 'f-b0') + T(cx, 154, 'Trachea', 'f-s')
    b += _d5_circ(cx, 212, 17, 'f-b0') + T(cx, 216, 'Oes', 'f-s')
    b += _d5_circ(cx - 62, 98, 7, 'f-b0') + T(cx - 74, 98, 'RC', 'f-s', 'end')
    b += _d5_circ(cx - 82, 146, 7, 'f-b0') + T(cx - 94, 150, 'RS', 'f-s', 'end')
    b += _d5_circ(cx + 84, 136, 14, 'f-b1') + T(cx + 84, 140, 'LPA', 'f-s')
    return b


def d5_ring_raa():
    b = T(12, 20, 'Right aortic arch: when the left ligamentum makes a ring (axial, seen from the feet, arrangement schematic)', 'f-h', 'start')
    cx = 180
    b += T(cx, 44, 'Aberrant left subclavian, Kommerell', 'f-h')
    b += _d5_tube([('M', cx + 60, 244), ('L', cx + 116, 214)], 10, 'f-warn')
    b += _d5_raa_base(cx, False)
    b += f'<ellipse cx="{cx + 70}" cy="238" rx="14" ry="11" class="f-warn"/>'
    b += _d5_circ(cx + 30, 82, 7, 'f-b0') + T(cx + 42, 80, 'LC', 'f-s', 'start')
    b += T(cx + 122, 214, 'LS', 'f-s', 'start')
    b += f'<path d="M{cx + 84} 150 C{cx + 86} 190 {cx + 82} 216 {cx + 76} 228" class="f-dash" style="stroke-width:2.5"/>'
    b += _d5_cutmark(cx + 85, 186, 95, 10)
    b += T(cx + 100, 182, ['left', 'ligamentum'], 'f-s', 'start')
    b += T(cx + 92, 278, 'diverticulum', 'f-s')
    b += T(cx - 170, 304, ['Left carotid, right carotid, right subclavian, then a', 'retro-oesophageal left subclavian from the proximal',
                           'descending aorta (with or without a Kommerell', 'diverticulum). Ring closed by the left ligamentum.',
                           'Left thoracotomy: divide the ligamentum (red bars).', 'Resect the diverticulum and move the left subclavian',
                           'to the left carotid when needed (not always).'], 'f-s', 'start')
    cx = 540
    b += T(cx, 44, 'Mirror-image branching', 'f-h')
    b += _d5_raa_base(cx, True)
    b += _d5_circ(cx + 34, 84, 9, 'f-b0') + T(cx + 46, 74, 'L innominate', 'f-s', 'start')
    b += f'<path d="M{cx + 76} 124 C{cx + 66} 106 {cx + 56} 94 {cx + 42} 90" class="f-dash" style="stroke-width:2.5"/>'
    b += f'<path d="M{cx + 86} 150 C{cx + 88} 190 {cx + 80} 220 {cx + 66} 240" class="f-l" stroke-dasharray="2 4" style="stroke-width:2.5"/>'
    b += T(712, 112, ['to innominate', '(commoner):', 'no ring'], 'f-s', 'end')
    b += T(cx + 100, 196, ['to DAo:', 'ring'], 'f-s', 'start')
    b += T(cx - 170, 304, ['Left innominate, right carotid, right subclavian. A ring', 'only if the left ligamentum runs from the PA to the',
                           'descending aorta (dotted). Running to the left innominate', '(dashed, commoner) it makes no ring. Mirror image is',
                           'almost always with intracardiac disease (truncus,', 'Fallot, tricuspid atresia; 22q11).'], 'f-s', 'start')
    b += line(360, 36, 360, 420, 'f-grid')
    b += _d5_compass(30, 70, front=False) if False else ''
    b += T(12, 440, ['Orientation as on CT: anterior at the top, patient\'s left on the right.',
                     'RC, RS: right carotid and subclavian; LC: left carotid; LS: left subclavian.'], 'f-s', 'start')
    return svg(470, b)


def d5_pa_sling():
    t = T(12, 20, 'Pulmonary artery sling and its repair (axial, seen from the feet, arrangement schematic)', 'f-h', 'start')
    b = ''
    for i, cx in enumerate([180, 540]):
        b += T(cx, 14, ['The sling', 'Repair'][i], 'f-h')
        if i == 0:
            b += _d5_tube([('M', cx - 50, 80), ('C', cx - 64, 140, cx - 30, 168, cx, 168), ('C', cx + 40, 168, cx + 80, 160, cx + 130, 150)], 14, 'f-b1')
        else:
            b += _d5_line_path([('M', cx - 50, 92), ('C', cx - 64, 140, cx - 30, 168, cx, 168), ('C', cx + 40, 168, cx + 80, 160, cx + 120, 152)], 'f-dash')
            b += _d5_tube([('M', cx + 46, 54), ('C', cx + 96, 64, cx + 122, 104, cx + 130, 150)], 14, 'f-b1')
        b += _d5_tube([('M', cx + 70, 34), ('L', cx + 22, 62), ('C', cx - 20, 80, cx - 80, 80, cx - 150, 84)], 24, 'f-b1')
        if i == 1:
            b += _d5_cutmark(cx - 52, 92, 90, 8)
        b += _d5_circ(cx, 120, 26, 'f-b1') + _d5_circ(cx, 120, 19, 'f-lumen') + T(cx + 32, 112, 'Trachea', 'f-s', 'start')
        b += _d5_circ(cx, 206, 17, 'f-b0') + T(cx, 210, 'Oes', 'f-s')
        b += T(cx + 84, 30, 'MPA', 'f-s', 'start') + T(cx - 150, 112, 'RPA', 'f-s', 'start') + T(cx + 130, 178, ['LPA to', 'left hilum'], 'f-s')
    b += T(30, 250, ['LPA arises from the RPA and passes between trachea', 'and oesophagus to the left hilum, compressing the',
                     'distal trachea. Often complete cartilage rings (the', '"ring-sling" complex). Barium: anterior',
                     'oesophageal indentation (rings indent it posteriorly).', 'Bronchoscopy is essential: rings and extent of compression.'],
           'f-s', 'start')
    b += T(390, 250, ['Repair regardless of symptoms. Sternotomy and', 'bypass; divide the LPA from the RPA, bring it in',
                      'front of the trachea, join it to the main PA.', 'Complete rings with stenosis: slide tracheoplasty',
                      '(patch if full mobilisation is not feasible);', 'bronchoscopy after repair.'], 'f-s', 'start')
    b += line(360, 36, 360, 350, 'f-grid')
    return svg(360 + 30, t + f'<g transform="translate(0 30)">{b}</g>')


# ---------------------------------------------------------------- shunts

def _d5_great_vessels(o, classic=False):
    b = _d5_tube([('M', o + 215, 262), ('L', o + 26, 262)], 18, 'f-b1')
    b += _d5_tube([('M', o + 232, 352), ('L', o + 215, 266)], 30, 'f-b1')
    b += _d5_tube([('M', o + 130, 80), ('L', o + 130, 24)], 10, 'f-warn')
    if classic:
        b += _d5_tube([('M', o + 74, 84), ('L', o + 24, 86)], 10, 'f-warn') + _d5_cutmark(o + 78, 84, 0, 8)
    else:
        b += _d5_tube([('M', o + 130, 80), ('L', o + 24, 86)], 10, 'f-warn')
    b += _d5_tube([('M', o + 215, 112), ('L', o + 215, 40)], 10, 'f-warn')
    b += _d5_tube([('M', o + 250, 120), ('L', o + 300, 50)], 10, 'f-warn')
    b += _d5_tube([('M', o + 180, 128), ('C', o + 166, 104, o + 150, 88, o + 130, 80)], 14, 'f-warn')
    b += _d5_tube([('M', o + 170, 340), ('L', o + 170, 170), ('C', o + 170, 110, o + 270, 110, o + 270, 170), ('L', o + 270, 340)], 30, 'f-warn')
    b += _d5_tube([('M', o + 215, 262), ('L', o + 340, 252)], 18, 'f-b1')
    b += T(o + 26, 250, 'RPA', 'f-s', 'start') + T(o + 330, 240, 'LPA', 'f-s', 'end') + T(o + 232, 370, 'MPA', 'f-s')
    b += T(o + 138, 40, 'R carotid', 'f-s', 'start') + T(o + 24, 76, 'R subclavian', 'f-s', 'start') + T(o + 170, 356, 'Aorta', 'f-s')
    return b


def d5_bt_shunt():
    t = T(12, 20, 'Blalock-Taussig shunts, classic and modified (front view, left arch, schematic)', 'f-h', 'start')
    b = ''
    b += T(180, 4, 'Classic (1945)', 'f-h') + T(540, 4, 'Modified: PTFE interposition graft', 'f-h')
    b += _d5_great_vessels(0, classic=True)
    b += _d5_tube([('M', 128, 84), ('C', 98, 100, 90, 200, 90, 254)], 10, 'f-warn')
    b += line(96, 170, 40, 150, 'f-l') + T(14, 126, ['subclavian divided,', 'turned down'], 'f-s', 'start')
    b += _d5_great_vessels(360)
    b += _d5_tube([('M', 460, 88), ('C', 456, 140, 456, 200, 460, 254)], 10, 'f-b0')
    b += line(456, 170, 400, 150, 'f-l') + T(374, 126, ['PTFE graft;', 'artery kept'], 'f-s', 'start')
    b += T(14, 392, ['End-to-side subclavian to PA, side', 'opposite the arch. No prosthesis; flow', 'limited by the subclavian orifice; grows',
                     'with the child. Long dissection, RLN risk,', 'kinking in small infants, rare severe arm', 'ischaemia; hard to take down.'], 'f-s', 'start')
    b += T(374, 392, ['Side-biting clamp; graft end-to-side to', 'the subclavian, then to the PA. Heparin',
                      'usually 1 mg/kg before the anastomosis.', '5 mm better than 4 or 3 mm. Subclavian',
                      'orifice regulates flow; arm flow kept.', 'Seroma or long drainage in 3 to 5%.'], 'f-s', 'start')
    b += line(360, 36, 360, 490, 'f-grid')
    y0 = 512
    b += T(12, y0, 'Pooled comparison (Yuan 2009, Table 1)', 'f-h', 'start') + T(450, y0, 'Modified', 'f-h', 'middle') + T(600, y0, 'Classic', 'f-h', 'middle')
    rows = [('Early shunt failure', '20.8%', '51.7%'), ('Diaphragm paralysis needing plication', '4%', '10%'),
            ('PA distortion', '6.1 to 50%', '17 to 75%'), ('Months to next shunt or repair', '12.4', '26.1 to 27.7'),
            ('Hospital mortality', '3.1 to 11%', '2.3 to 8% (50% under 2 weeks)')]
    for k, (m, a, c) in enumerate(rows):
        y = y0 + 22 + k * 22
        b += line(12, y - 15, 708, y - 15, 'f-grid')
        b += T(12, y, m, 'f-s', 'start') + T(450, y, a, 'f-n') + T(600, y, c, 'f-s')
    y = y0 + 22 + 5 * 22
    b += box(10, y - 6, 700, 44, ['Sternotomy preferred since 1990: PTFE shunts via thoracotomy were 4 times more likely to fail, and left-sided',
                                  'modified shunts 4 times more failure-prone (Odim), although the left side spares the RPA for later anastomosis.'], 'b1', 'f-s')
    return svg(y + 48 + 40, t + f'<g transform="translate(0 40)">{b}</g>')


def d5_shunt_types():
    b = T(12, 20, 'Systemic-to-pulmonary shunts: where each one joins (front view, left arch, schematic)', 'f-h', 'start')
    b += '<rect x="226" y="330" width="210" height="74" rx="18" class="f-b0"/>' + T(262, 394, 'RV', 'f-s')
    b += _d5_tube([('M', 370, 252), ('L', 140, 252)], 20, 'f-b1')
    b += _d5_tube([('M', 386, 340), ('L', 370, 256)], 32, 'f-b1')
    b += _d5_tube([('M', 280, 84), ('L', 280, 26)], 10, 'f-warn') + _d5_tube([('M', 256, 86), ('L', 150, 90)], 10, 'f-warn')
    b += _d5_cutmark(250, 86, 0, 8)
    b += _d5_tube([('M', 385, 114), ('L', 385, 40)], 10, 'f-warn')
    b += _d5_tube([('M', 425, 122), ('C', 440, 90, 470, 66, 580, 62)], 10, 'f-warn')
    b += _d5_tube([('M', 336, 132), ('C', 320, 108, 300, 92, 280, 84)], 14, 'f-warn')
    b += _d5_tube([('M', 330, 344), ('L', 330, 170), ('C', 330, 110, 440, 110, 440, 170), ('L', 440, 330)], 32, 'f-warn')
    b += _d5_tube([('M', 370, 252), ('L', 590, 240)], 20, 'f-b1')
    b += _d5_tube([('M', 372, 300), ('L', 344, 300)], 10, 'f-b1')
    b += _d5_tube([('M', 270, 84), ('C', 236, 104, 222, 190, 222, 244)], 10, 'f-warn')
    b += _d5_tube([('M', 524, 68), ('C', 530, 120, 530, 190, 524, 232)], 10, 'f-b0')
    b += _d5_tube([('M', 284, 346), ('C', 246, 320, 250, 276, 298, 258)], 14, 'f-b0')
    b += '<ellipse cx="330" cy="252" rx="9" ry="7" class="f-b0"/><ellipse cx="440" cy="246" rx="9" ry="7" class="f-b0"/>'
    for n, x, y in (('1', 200, 168), ('2', 552, 150), ('3', 302, 226), ('4', 466, 222), ('5', 414, 300), ('6', 236, 306)):
        b += _d5_num(x, y, n, 'f-ok')
    b += T(170, 252 + 22, 'RPA', 'f-s') + T(580, 262, 'LPA', 'f-s') + T(150, 80, 'R subclavian', 'f-s', 'start')
    b += T(590, 58, 'L subclavian', 'f-s', 'start') + T(385, 200, 'Aorta', 'f-s') + T(456, 320, 'DAo', 'f-s', 'start')
    cards = [('1 Classic Blalock-Taussig', ['Subclavian divided, end-to-side', 'to PA on the side opposite the arch']),
             ('2 Modified Blalock-Taussig', ['PTFE graft from subclavian or', 'brachiocephalic; most used']),
             ('3 Waterston/Cooley', ['Side-to-side ascending aorta to', 'anterior RPA; RPA kinking']),
             ('4 Potts', ['Side-to-side descending aorta to', 'LPA; largely abandoned']),
             ('5 Central (Mee)', ['Main PA end-to-side to the', 'ascending aorta; tiny PAs']),
             ('6 Sano', ['RV-PA conduit: Norwood stage I;', 'possibly more PA reintervention'])]
    for k, (h, tx) in enumerate(cards):
        x, y = 10 + (k % 3) * 236, 420 + (k // 3) * 74
        b += f'<rect x="{x}" y="{y}" width="228" height="66" rx="9" class="f-b0"/>'
        b += T(x + 10, y + 20, h, 'f-h', 'start') + T(x + 10, y + 38, tx, 'f-s', 'start')
    b += T(12, 584, 'Waterston and Potts: flow uncontrolled, set by the size of the anastomosis. They and the central shunts are hard to take down.', 'f-s', 'start')
    return svg(594, b)


# ---- figs_D6.py
"""D6 drawings: septal defects, AVSD, anomalous veins, Ebstein, single ventricle staging.
Every label comes from the ST4 notes (pages g9, g12, g8, g11, g3) or TSRA chapter text on disk."""

import math


def _d6_d6_card(x, y, w, h, head, lines, cls='b0', lh=16):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="f-{cls}"/>'
    out += T(x + 10, y + 19, head, 'f-h', 'start')
    for i, s in enumerate(lines):
        out += T(x + 10, y + 37 + i * lh, s, 'f-s', 'start')
    return out


def _d6_d6_num(x, y, n, cls='b1'):
    return f'<circle cx="{x}" cy="{y}" r="11" class="f-{cls}"/>' + T(x, y + 5, str(n), 'f-h')


def _d6_d6_tube(x1, y1, x2, y2, cls='f-b0'):
    """Axis-aligned tube drawn as a rounded rectangle."""
    x, y = min(x1, x2), min(y1, y2)
    return f'<rect x="{x}" y="{y}" width="{abs(x2 - x1)}" height="{abs(y2 - y1)}" rx="5" class="{cls}"/>'


def _d6_d6_leaf(d, w=4):
    return f'<path d="{d}" class="f-l" style="stroke-width:{w}px;stroke-linecap:round"/>'


def _d6_d6_patch(d, w=5, dash=False):
    da = ' stroke-dasharray="6 4"' if dash else ''
    return f'<path d="{d}" class="f-cut" style="stroke-width:{w}px;stroke-linecap:round"{da}/>'


def _d6_d6_chord(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="f-l" stroke-dasharray="3 3"/>'


# ------------------------------------------------------------------ ASD

def d6_asd_types():
    b = T(12, 18, 'Right atrium opened, septum facing', 'f-h', 'start')
    b += '<rect x="110" y="62" width="340" height="286" rx="26" class="f-b0"/>'
    # SVC and IVC
    b += line(176, 30, 176, 70) + line(264, 30, 264, 70) + T(220, 48, 'SVC', 'f-s')
    b += '<ellipse cx="220" cy="70" rx="44" ry="15" class="f-lumen"/>'
    b += line(172, 340, 172, 376) + line(268, 340, 268, 376) + T(220, 372, 'IVC', 'f-s')
    b += '<ellipse cx="220" cy="336" rx="48" ry="17" class="f-lumen"/>'
    # Eustachian valve on the anterior IVC rim
    b += '<path d="M248 322 C272 314 290 316 304 326" class="f-l" style="stroke-width:3.5px"/>'
    b += T(312, 334, 'Eustachian valve', 'f-s', 'start')
    # tricuspid valve
    b += '<ellipse cx="452" cy="232" rx="50" ry="94" class="f-lumen"/>' + T(452, 236, ['Tricuspid', 'valve'], 'f-s')
    # right upper pulmonary vein into the superior defect
    b += '<rect x="20" y="88" width="160" height="16" rx="6" class="f-b1"/>'
    b += T(20, 62, ['Right upper', 'pulmonary vein'], 'f-s', 'start')
    # 1 secundum in the fossa
    b += '<ellipse cx="250" cy="196" rx="62" ry="50" class="f-dash"/>' + T(250, 262, 'Fossa ovalis', 'f-s')
    b += '<ellipse cx="250" cy="196" rx="38" ry="30" class="f-warn"/>' + _d6_d6_num(250, 196, 1)
    # 2 primum against the AV valve
    b += '<path d="M404 214 C364 236 364 288 400 312 C388 284 388 242 404 214 Z" class="f-warn"/>' + _d6_d6_num(370, 262, 2)
    # 3 superior sinus venosus
    b += '<ellipse cx="196" cy="96" rx="32" ry="17" class="f-warn"/>' + _d6_d6_num(196, 96, 3)
    # 4 inferior sinus venosus
    b += '<ellipse cx="196" cy="312" rx="32" ry="15" class="f-warn"/>' + _d6_d6_num(196, 312, 4)
    # 5 coronary sinus
    b += '<circle cx="330" cy="292" r="17" class="f-warn"/>' + _d6_d6_num(330, 292, 5)
    b += T(116, 394, 'Posterior', 'f-s', 'start') + T(500, 394, 'Anterior', 'f-s', 'end')
    cards = [('1 Secundum, 80%', ['Fossa ovalis; device if rims', 'allow (up to 3.8 cm)']),
             ('2 Primum, 10%', ['AV canal spectrum: cleft,', 'abnormal conduction axis']),
             ('3 Sinus venosus, superior', ['SVC-RA junction; upper lobe', 'veins (both types 4 to 11%)']),
             ('4 Sinus venosus, inferior', ['IVC-RA junction; middle', 'and lower lobe veins']),
             ('5 Coronary sinus, 1 to 2%', ['Unroofed; with a left SVC', '= Raghib syndrome'])]
    for i, (h, ls) in enumerate(cards):
        b += _d6_d6_card(518, 30 + i * 66, 196, 60, h, ls, 'b0')
    b += box(10, 406, 345, 44, ['PFO (up to 30% of hearts) is not a true ASD.', 'Common atrium: no septum (heterotaxy).'], 'b0', 'f-s')
    b += box(365, 406, 345, 44, ['Inferior defect: keep the Eustachian valve out', 'of the patch, or the IVC drains to the LA.'], 'warn', 'f-s')
    return svg(460, b)


# ------------------------------------------------------------------ VSD

def d6_vsd_types():
    b = T(12, 18, 'Right ventricle opened, septum facing', 'f-h', 'start')
    b += ('<path d="M70 330 C40 310 36 262 64 222 L176 84 C188 68 204 60 222 60 L410 60 '
          'C440 60 456 76 456 100 L456 316 C456 334 444 344 424 344 L104 344 C90 344 78 338 70 330 Z" class="f-b0"/>')
    b += '<ellipse cx="262" cy="52" rx="52" ry="15" class="f-lumen"/>' + T(196, 44, 'Pulmonary valve', 'f-s', 'end')
    b += '<ellipse cx="470" cy="214" rx="44" ry="104" class="f-lumen"/>' + T(474, 210, ['Tricuspid', 'valve'], 'f-s')
    b += _d6_d6_leaf('M432 176 C428 210 428 260 438 300', 5) + T(466, 336, 'Septal leaflet', 'f-s')
    b += '<circle cx="434" cy="156" r="5" class="f-ah"/>'
    b += T(420, 94, ['Anteroseptal', 'commissure'], 'f-s', 'end') + line(422, 104, 432, 150)
    # defects
    b += '<ellipse cx="262" cy="92" rx="34" ry="15" class="f-warn"/>' + T(262, 97, 'I', 'f-h')
    b += '<ellipse cx="392" cy="158" rx="30" ry="22" class="f-warn"/>' + T(392, 163, 'II', 'f-h')
    b += '<ellipse cx="400" cy="272" rx="24" ry="22" class="f-warn"/>' + T(400, 277, 'III', 'f-h')
    for x, y in ((206, 176), (136, 268), (250, 236)):
        b += f'<circle cx="{x}" cy="{y}" r="13" class="f-warn"/>' + T(x, y + 5, 'IV', 'f-s')
    # His bundle along the posteroinferior rim of the perimembranous defect
    b += '<path d="M440 196 C420 192 400 186 380 182 C350 178 330 200 312 234 C298 262 286 290 272 318" class="f-nerve"/>'
    b += T(150, 318, ['His bundle: posteroinferior rim', 'of perimembranous defects'], 'f-s', 'middle')
    b += line(226, 318, 276, 308)
    b += T(470, 366, 'III: bundle on its posteroinferior rim too (FRCS Atlas)', 'f-s', 'end')
    cards = [('I Outlet, 8%', ['Beneath pulmonary annulus;', 'closed through the PA;', 'bundle remote (*)']),
             ('II Perimembranous, 80%', ['By the anteroseptal TV', 'commissure; heart block', '1 to 2% (Mussa)']),
             ('III Inlet, 6%', ['Immediately below the', 'septal tricuspid leaflet']),
             ('IV Muscular, 10%', ['Anywhere; may be multiple:', 'close the largest, leave', 'small ones (± PA band)'])]
    ys = [30, 116, 202, 270]
    hs = [80, 80, 62, 80]
    for (h, ls), y, hh in zip(cards, ys, hs):
        b += _d6_d6_card(526, y, 188, hh, h, ls, 'b0')
    b += T(12, 392, ['(*) Outlet point from the FRCS Atlas draft; TSRA ch. 93 warns only for perimembranous and inlet defects.',
                     'Doubly committed defects may cause aortic leaflet prolapse and regurgitation (Mussa 2024).'], 'f-s', 'start')
    return svg(428, b)


# ------------------------------------------------------------------ AVSD

def _d6_d6_heart4(ox, crest, asd=True, common=False, vsd_small=False, cleft=False):
    cx = ox + 113
    b = f'<rect x="{ox + 18}" y="44" width="190" height="192" rx="30" class="f-b0"/>'
    # atrial septum, ending above the valve plane (primum defect)
    b += f'<rect x="{cx - 5}" y="44" width="10" height="{68 if asd else 96}" class="f-b1"/>'
    # ventricular septum
    b += f'<path d="M{cx - 8} 236 L{cx - 5} {crest} L{cx + 5} {crest} L{cx + 8} 236 Z" class="f-b1"/>'
    if asd:
        b += f'<rect x="{cx - 5}" y="114" width="10" height="24" class="f-warn"/>'
    if crest > 150:
        b += f'<rect x="{cx - 5}" y="146" width="10" height="{crest - 148}" class="f-warn"/>'
    if common:
        b += _d6_d6_leaf(f'M{ox + 20} 140 C{ox + 70} 150 {ox + 156} 150 {ox + 206} 140')
    else:
        b += _d6_d6_leaf(f'M{ox + 20} 140 L{cx - 6} 142') + _d6_d6_leaf(f'M{cx + 6} 142 L{ox + 206} 140')
    if vsd_small:
        b += f'<circle cx="{cx}" cy="{crest + 16}" r="6" class="f-warn"/>'
    if cleft:
        b += f'<path d="M{cx + 40} 141 L{cx + 48} 154 L{cx + 56} 141" class="f-cut"/>'
    b += T(ox + 64, 96, 'RA', 'f-s') + T(ox + 162, 96, 'LA', 'f-s')
    b += T(ox + 64, 200, 'RV', 'f-s') + T(ox + 162, 200, 'LV', 'f-s')
    return b


def d6_avsd_forms():
    b = T(12, 18, 'Four-chamber schematic: right heart on the left; red tint = defect', 'f-h', 'start')
    spec = [('Partial', dict(crest=146, cleft=True), ['Primum ASD + cleft left AVV;', 'two orifices on the crest;', 'presents later, like an ASD']),
            ('Transitional', dict(crest=146, vsd_small=True, cleft=True), ['Partial + pressure-restrictive', 'VSD; chords to the septum', 'may cause LVOTO']),
            ('Complete', dict(crest=184, common=True), ['Primum ASD + unrestrictive', 'inlet VSD + common AVV;', 'heart failure at 4 to 6 weeks'])]
    for i, (name, kw, ls) in enumerate(spec):
        ox = 10 + i * 237
        b += _d6_d6_heart4(ox, **kw)
        b += T(ox + 113, 262, name, 'f-h') + T(ox + 113, 282, ls, 'f-s')
    b += T(10 + 113 + 48, 172, 'cleft', 'f-s')
    b += T(247 + 113 + 30, 184, 'small VSD', 'f-s', 'start')
    b += T(484 + 125, 130, 'common valve', 'f-s', 'start')
    b += box(10, 340, 700, 62, ['Left and right AV valves (not mitral and tricuspid): superior and inferior bridging leaflets plus lateral leaflets.',
                                'Unbalanced in 10 to 25%: the ventricle on the side of the smaller orifice is hypoplastic.',
                                'About 75% of complete AVSD children have Down syndrome; partial AVSD rarely does.'], 'b0', 'f-s')
    return svg(412, b)


def _d6_d6_crest_panel(ox, kind):
    cx = ox + 113
    b = f'<rect x="{ox + 14}" y="40" width="198" height="236" rx="20" class="f-b0"/>'
    b += f'<path d="M{cx - 9} 276 L{cx - 5} 170 L{cx + 5} 170 L{cx + 9} 276 Z" class="f-b1"/>'
    b += T(ox + 50, 70, 'RA', 'f-s') + T(ox + 176, 70, 'LA', 'f-s') + T(ox + 32, 212, 'RV', 'f-s') + T(ox + 194, 212, 'LV', 'f-s')
    # papillary muscles
    b += f'<path d="M{ox + 36} 276 C{ox + 40} 240 {ox + 64} 240 {ox + 68} 276 Z" class="f-b0"/>'
    b += f'<path d="M{ox + 158} 276 C{ox + 162} 240 {ox + 186} 240 {ox + 190} 276 Z" class="f-b0"/>'
    b += _d6_d6_leaf(f'M{ox + 16} 112 C{ox + 70} 124 {ox + 156} 124 {ox + 210} 112')
    if kind == 'A':
        b += _d6_d6_chord(cx - 22, 121, cx - 5, 172) + _d6_d6_chord(cx + 22, 121, cx + 5, 172)
        b += _d6_d6_chord(ox + 50, 118, ox + 52, 246) + _d6_d6_chord(ox + 176, 118, ox + 174, 246)
    elif kind == 'B':
        b += _d6_d6_chord(cx - 30, 121, ox + 170, 246) + _d6_d6_chord(cx - 14, 122, ox + 166, 246)
        b += _d6_d6_chord(ox + 50, 118, ox + 52, 246) + _d6_d6_chord(ox + 176, 118, ox + 174, 246)
    else:
        b += _d6_d6_chord(cx - 30, 121, ox + 56, 246) + _d6_d6_chord(ox + 44, 118, ox + 50, 246)
        b += _d6_d6_chord(cx + 30, 121, ox + 170, 246) + _d6_d6_chord(ox + 182, 118, ox + 176, 246)
    return b


def d6_rastelli():
    b = T(12, 18, 'Complete AVSD: superior bridging leaflet seen in a coronal cut (arrangement schematic)', 'f-h', 'start')
    spec = [('A', 'Type A, 75%', ['Chords from each component', 'to its own side of the crest']),
            ('B', 'Type B, rare', ['Straddling chords to a papillary', 'muscle in the other ventricle;', 'almost never balanced']),
            ('C', 'Type C, 25%', ['Free-floating; usually no chords', 'to the crest; goes with TOF', 'and DORV'])]
    for i, (k, name, ls) in enumerate(spec):
        ox = 10 + i * 237
        b += _d6_d6_crest_panel(ox, k)
        b += T(ox + 113, 300, name, 'f-h') + T(ox + 113, 320, ls, 'f-s')
    b += T(10 + 113, 104, 'bridging leaflet', 'f-s') + T(10 + 104, 186, 'crest', 'f-s', 'end')
    b += box(10, 372, 700, 44, ['Coronary sinus and AV node displaced inferiorly; the His bundle runs along the inferior,',
                                'leftward crest for about 50% of its length (TSRA ch. 94).'], 'b0', 'f-s')
    return svg(426, b)


def _d6_d6_patch_panel(ox, kind):
    cx = ox + 113
    b = f'<rect x="{ox + 14}" y="40" width="198" height="236" rx="20" class="f-b0"/>'
    b += f'<path d="M{cx - 9} 276 L{cx - 5} 196 L{cx + 5} 196 L{cx + 9} 276 Z" class="f-b1"/>'
    b += f'<rect x="{cx - 5}" y="40" width="10" height="56" class="f-b1"/>'
    b += T(ox + 50, 70, 'RA', 'f-s') + T(ox + 176, 70, 'LA', 'f-s') + T(ox + 50, 250, 'RV', 'f-s') + T(ox + 176, 250, 'LV', 'f-s')
    b += f'<circle cx="{cx + 4}" cy="202" r="4" class="f-nerve"/>'
    if kind == 'two':
        b += _d6_d6_patch(f'M{cx - 6} 198 L{cx - 6} 150')
        b += _d6_d6_patch(f'M{cx} 148 L{cx - 2} 98', 5, True)
        b += _d6_d6_leaf(f'M{ox + 16} 150 L{cx - 8} 150') + _d6_d6_leaf(f'M{cx + 4} 150 L{ox + 210} 150')
        b += f'<rect x="{cx - 22}" y="194" width="9" height="8" rx="2" class="f-b1"/>'
        b += T(cx - 12, 178, 'VSD patch', 'f-s', 'end') + T(cx + 8, 120, 'ASD patch', 'f-s', 'start')
    elif kind == 'one':
        b += _d6_d6_patch(f'M{cx - 4} 198 L{cx - 2} 98')
        b += _d6_d6_leaf(f'M{ox + 16} 150 L{cx - 6} 150') + _d6_d6_leaf(f'M{cx + 2} 150 L{ox + 210} 150')
        b += f'<rect x="{cx - 20}" y="194" width="9" height="8" rx="2" class="f-b1"/>'
        b += T(cx + 10, 120, 'one patch', 'f-s', 'start')
        b += T(cx + 10, 176, ['leaflets 5 to 10 mm', 'above the crest'], 'f-s', 'start')
    else:
        b += _d6_d6_patch(f'M{cx} 190 L{cx - 2} 98')
        b += _d6_d6_leaf(f'M{ox + 16} 150 C{ox + 60} 152 {cx - 20} 170 {cx - 4} 190')
        b += _d6_d6_leaf(f'M{cx + 4} 190 C{cx + 20} 170 {ox + 166} 152 {ox + 210} 150')
        b += f'<rect x="{cx - 26}" y="204" width="9" height="8" rx="2" class="f-b1"/>'
        b += f'<path d="M{cx - 17} 208 L{cx + 2} 190 L{cx} 160" class="f-l" stroke-dasharray="3 3"/>'
        b += T(cx + 10, 120, 'ASD patch only', 'f-s', 'start')
        b += T(cx - 30, 230, 'pledget', 'f-s', 'end')
    return b


def d6_avsd_patch():
    b = T(12, 18, 'Complete AVSD repair: coronal cut through the crest (yellow ring = His bundle on the crest)', 'f-h', 'start')
    spec = [('two', 'Two-patch', ['Separate VSD and ASD patches;', 'favoured by some for large', 'VSDs, to prevent LVOTO']),
            ('one', 'Traditional one-patch', ['Bridging leaflets divided and', 'reattached to one pericardial', 'patch fixed to the crest']),
            ('mod', 'Modified one-patch (Australian)', ['Pledgeted sutures on the RV side', 'of the crest, through leaflets and', 'ASD patch: tying closes the VSD'])]
    for i, (k, name, ls) in enumerate(spec):
        ox = 10 + i * 237
        b += _d6_d6_patch_panel(ox, k)
        b += T(ox + 113, 300, name, 'f-h') + T(ox + 113, 320, ls, 'f-s')
    b += box(10, 376, 700, 62, ['All: sutures on the RV side of the crest keep away from the His bundle. Close the left AV valve cleft unless',
                                'that would cause stenosis; test with saline; TOE after bypass. Modified one-patch may accentuate the gooseneck',
                                'and LVOTO if the VSD is large. Equivalent results with either patch method (Crawford 2004).'], 'b0', 'f-s')
    return svg(448, b)


def _d6_d6_cs_panel(ox, around):
    b = f'<rect x="{ox + 10}" y="44" width="330" height="236" rx="20" class="f-b0"/>'
    b += _d6_d6_leaf(f'M{ox + 24} 246 L{ox + 326} 246', 5)
    b += T(ox + 215, 270, 'AV valve attached to the crest', 'f-s')
    b += f'<path d="M{ox + 130} 244 A82 66 0 0 1 {ox + 294} 244 Z" class="f-warn"/>'
    b += T(ox + 212, 214, 'Primum ASD', 'f-s')
    b += f'<circle cx="{ox + 70}" cy="206" r="16" class="f-lumen"/>' + T(ox + 70, 210, 'CS', 'f-s')
    b += f'<path d="M{ox + 112} 240 C{ox + 150} 252 {ox + 220} 254 {ox + 300} 254" class="f-nerve"/>'
    b += f'<circle cx="{ox + 110}" cy="238" r="6" class="f-ah"/>'
    b += T(ox + 56, 270, 'AV node', 'f-s') + line(ox + 70, 260, ox + 104, 242)
    if around:
        b += _d6_d6_patch(f'M{ox + 300} 244 C{ox + 300} 150 {ox + 160} 150 {ox + 120} 172 '
                       f'C{ox + 90} 156 {ox + 50} 162 {ox + 42} 196 C{ox + 38} 222 {ox + 46} 236 {ox + 52} 244', 4, True)
    else:
        b += _d6_d6_patch(f'M{ox + 300} 244 C{ox + 300} 150 {ox + 150} 150 {ox + 126} 200 C{ox + 120} 216 {ox + 120} 232 {ox + 124} 244', 4, True)
        b += T(ox + 330, 118, 'very shallow bites near the node', 'f-s', 'end')
        b += line(ox + 200, 124, ox + 128, 210)
    return b


def d6_avsd_cs():
    b = T(12, 18, 'Primum defect from the right atrium (CS = coronary sinus): where the patch suture runs (dashed red)', 'f-h', 'start')
    b += _d6_d6_cs_panel(10, True) + _d6_d6_cs_panel(370, False)
    b += T(185, 306, 'Around the coronary sinus', 'f-h') + T(545, 306, 'In front of the coronary sinus', 'f-h')
    b += T(185, 326, ['Patch runs inferior to and around the', 'sinus, which then drains to the LA', '(small, well-tolerated right-to-left', 'shunt); the common strategy'], 'f-s')
    b += T(545, 326, ['Sinus stays on the RA side; very', 'shallow bites from the inferior septum', 'to the annulus (Crawford leaves the', 'sinus on the RA side routinely)'], 'f-s')
    b += box(10, 404, 700, 40, 'AV node displaced inferiorly towards the coronary sinus; heart block needing a pacemaker 1 to 5% (TSRA ch. 94)', 'b0', 'f-s')
    return svg(454, b)


# ------------------------------------------------------------------ cor triatriatum

def d6_cor_triatriatum():
    b = T(12, 18, 'Cor triatriatum sinister (arrangement schematic)', 'f-h', 'start')
    b += '<rect x="30" y="80" width="150" height="180" rx="22" class="f-b0"/>' + T(105, 170, 'RA', 'f-h')
    b += '<rect x="186" y="50" width="270" height="250" rx="26" class="f-b0"/>'
    # pulmonary veins into the proximal chamber
    for x in (236, 290, 350, 404):
        b += f'<rect x="{x - 9}" y="22" width="18" height="34" rx="6" class="f-b1"/>'
    # membrane with an opening
    b += _d6_d6_leaf('M190 168 L300 182', 6) + _d6_d6_leaf('M332 186 L452 200', 6)
    b += T(321, 112, ['Proximal chamber:', 'pulmonary veins'], 'f-s')
    b += T(330, 238, ['Distal chamber: appendage', 'and mitral valve'], 'f-s')
    b += arrow(316, 150, 316, 214)
    b += T(470, 176, 'Fibromuscular membrane', 'f-s', 'start') + line(468, 172, 420, 194)
    b += T(470, 140, ['Opening(s) of variable', 'size: obstruction'], 'f-s', 'start') + line(468, 146, 326, 182)
    # appendage and mitral valve
    b += '<ellipse cx="206" cy="262" rx="30" ry="18" class="f-b1"/>' + T(206, 296, 'Appendage', 'f-s')
    b += _d6_d6_leaf('M300 300 L350 300', 5) + _d6_d6_leaf('M362 300 L412 300', 5) + T(356, 322, 'Mitral valve', 'f-s')
    # ASD into the venous chamber
    b += '<rect x="176" y="112" width="20" height="26" class="f-warn"/>'
    b += T(105, 64, ['ASD into the venous', 'chamber, if present'], 'f-s')
    b += line(150, 88, 182, 112)
    cards = [('Presentation', ['Set by the opening and any ASD:', 'oedema, poor growth, PH,', 'right heart failure'], 'b0'),
             ('Adults (ACC/AHA 2025)', ['Like mitral stenosis; embolism', 'is the first sign in 16%;', 'anticoagulate if AF, stroke, thrombus'], 'b0'),
             ('Repair', ['Excise the whole membrane,', 'usually transseptal via RA', '(left atriotomy if older)'], 'ok')]
    for i, (h, ls, c) in enumerate(cards):
        b += _d6_d6_card(10 + i * 237, 340, 226, 88, h, ls, c)
    b += box(10, 440, 345, 44, ['Pulmonary vasodilators can be', 'dangerous before repair'], 'warn', 'f-s')
    b += box(365, 440, 345, 44, ['Dexter (divided RA): much rarer;', 'excise the membrane'], 'b0', 'f-s')
    return svg(494, b)


# ------------------------------------------------------------------ PAPVC

def _d6_d6_papvc_panel(ox, kind):
    b = ''
    b += f'<rect x="{ox + 20}" y="140" width="92" height="96" rx="16" class="f-b0"/>' + T(ox + 62, 222, 'RA', 'f-s')
    b += f'<rect x="{ox + 112}" y="140" width="56" height="80" rx="14" class="f-b1"/>' + T(ox + 142, 206, 'LA', 'f-s')
    b += f'<rect x="{ox + 109}" y="172" width="6" height="64" class="f-l"/>'
    b += f'<ellipse cx="{ox + 30}" cy="146" rx="18" ry="12" class="f-b0"/>'
    high = kind in ('warden', 'mod')
    pv_y = 70 if high else 112
    if high:
        b += _d6_d6_tube(ox + 46, 64, ox + 84, 142)
        b += _d6_d6_tube(ox + 46, 18, ox + 84, 44)
        b += line(ox + 42, 64, ox + 88, 64, 'f-cut') + line(ox + 42, 44, ox + 88, 44, 'f-cut')
        conn = 'f-stent' if kind == 'mod' else 'f-l'
        b += f'<path d="M{ox + 52} 40 C{ox + 20} 60 {ox + 10} 100 {ox + 22} 136" class="{conn}" style="stroke-width:{5 if kind == "mod" else 3}px"/>'
        b += _d6_d6_patch(f'M{ox + 46} 142 C{ox + 60} 170 {ox + 90} 176 {ox + 110} 172', 4)
    else:
        b += _d6_d6_tube(ox + 46, 18, ox + 84, 142)
        b += _d6_d6_patch(f'M{ox + 84} {pv_y - 10} C{ox + 70} 140 {ox + 90} 168 {ox + 110} 172', 4)
        if kind == 'two':
            b += _d6_d6_patch(f'M{ox + 46} 110 C{ox + 30} 124 {ox + 30} 148 {ox + 46} 160', 4, True)
    b += _d6_d6_tube(ox + 84, pv_y - 6, ox + 150, pv_y + 6, 'f-b1')
    b += f'<path d="M{ox + 92} {pv_y + 4} C{ox + 80} {pv_y + 40} {ox + 100} 150 {ox + 126} 162" class="f-l" stroke-dasharray="4 3" marker-end="url(#ah)"/>'
    return b


def d6_papvc_repairs():
    b = T(12, 18, 'Right PAPVC with sinus venosus ASD: four repairs (red = baffle or patch; dashed arrow = vein flow)', 'f-h', 'start')
    spec = [('single', 'Single patch', ['Baffle through the ASD;', 'RA closed primarily']),
            ('two', 'Two-patch', ['Second patch closes and', 'enlarges the SVC-RA junction']),
            ('warden', 'Warden', ['SVC divided above the veins;', 'cephalic end to RA appendage;', 'baffle SVC orifice to LA']),
            ('mod', 'Modified Warden (Mayo)', ['As Warden, with a ringed', 'PTFE graft 14 to 20 mm', '(blue dashed)'])]
    for i, (k, name, ls) in enumerate(spec):
        ox = 6 + i * 178
        b += f'<g transform="translate(0 16)">{_d6_d6_papvc_panel(ox, k)}</g>'
        b += T(ox + 88, 278, name, 'f-h') + T(ox + 88, 298, ls, 'f-s')
    b += T(6 + 150, 112, 'vein', 'f-s', 'end') + T(6 + 30, 196, 'RAA', 'f-s')
    b += T(12, 366, 'Mayo algorithm (Said 2012), after TTE and CT or MR angiography', 'f-h', 'start')
    b += box(10, 378, 220, 56, ['Veins under 1 cm above the', 'cavoatrial junction: single patch'], 'ok', 'f-s')
    b += box(245, 378, 220, 56, ['1 cm or more, left SVC with a', 'good bridging vein: caval', 'division, no reimplantation'], 'b1', 'f-s')
    b += box(480, 378, 230, 56, ['1 cm or more, no usable left SVC:', 'Warden if 18 or under;', 'modified Warden if older'], 'b1', 'f-s')
    b += box(10, 446, 700, 44, ['124 right-sided repairs: no early deaths. Late PV obstruction: single patch 5%, two-patch 12%, caval division 0.',
                                'SVC obstruction after caval division 10% (all after traditional Warden; none after the modified Warden).'], 'b0', 'f-s')
    return svg(500, b)


# ------------------------------------------------------------------ TAPVC

def _d6_d6_tapvc_panel(ox, kind):
    b = line(ox + 6, 236, ox + 168, 236, 'f-dash')
    b += f'<rect x="{ox + 20}" y="130" width="62" height="70" rx="14" class="f-b0"/>' + T(ox + 51, 170, 'RA', 'f-s')
    b += f'<rect x="{ox + 88}" y="120" width="62" height="60" rx="14" class="f-b0"/>' + T(ox + 119, 155, 'LA', 'f-s')
    b += arrow(ox + 74, 150, ox + 100, 150)
    b += _d6_d6_tube(ox + 34, 50, ox + 54, 130)
    b += _d6_d6_tube(ox + 34, 50, ox + 150, 66)
    b += _d6_d6_tube(ox + 36, 200, ox + 54, 290)
    # confluence behind the LA, not joined to it
    b += f'<ellipse cx="{ox + 120}" cy="200" rx="34" ry="9" class="f-b1"/>'
    for dx in (-30, -18, 18, 30):
        b += line(ox + 120 + dx, 200, ox + 120 + dx * 1.7, 186 if dx < 0 else 214, 'f-l')
    if kind in ('supra', 'mixed'):
        b += f'<path d="M{ox + 152} 198 C{ox + 168} 180 {ox + 166} 100 {ox + 146} 66" class="f-l" style="stroke-width:5px"/>'
        if kind == 'supra':
            b += f'<path d="M{ox + 156} 120 l10 -6 m-10 0 l10 6" class="f-cut" transform="translate(-2 0)"/>'
    if kind in ('cardiac', 'mixed'):
        b += f'<path d="M{ox + 92} 204 C{ox + 80} 214 {ox + 70} 212 {ox + 62} 198" class="f-l" style="stroke-width:5px"/>'
    if kind == 'infra':
        b += f'<path d="M{ox + 120} 209 C{ox + 120} 250 {ox + 110} 270 {ox + 100} 290" class="f-l" style="stroke-width:5px"/>'
        b += f'<rect x="{ox + 66}" y="290" width="80" height="22" rx="8" class="f-b0"/>' + T(ox + 106, 305, 'portal / IVC', 'f-s')
        b += f'<path d="M{ox + 96} 280 l10 -6 m-10 0 l10 6" class="f-cut"/>'
    return b


def d6_tapvc_types():
    b = T(12, 18, 'TAPVC: the confluence behind the LA drains to a systemic vein (red x = usual obstruction site)', 'f-h', 'start')
    spec = [('supra', 'Supracardiac, 50%', ['Vertical vein up to the', 'innominate vein', 'Repair: ligate the vein at', 'the innominate; confluence', 'to LA; close the ASD']),
            ('cardiac', 'Cardiac, 20%', ['Most often via the', 'coronary sinus', 'Repair: unroof the sinus', 'into the LA; patch ASD and', 'sinus (heart block risk)']),
            ('infra', 'Infracardiac, 25%', ['Down through the diaphragm;', 'most likely obstructed', 'Repair: rotate the heart up;', 'ligate the vein at the', 'diaphragm; confluence to LA']),
            ('mixed', 'Mixed, 5%', ['Several sites', '', 'Repair: combination', 'according to the lesions'])]
    for i, (k, name, ls) in enumerate(spec):
        ox = 6 + i * 178
        b += f'<g transform="translate(0 18)">{_d6_d6_tapvc_panel(ox, k)}</g>'
        b += T(ox + 88, 352, name, 'f-h') + T(ox + 88, 372, ls, 'f-s')
    b += T(6 + 100, 62, 'innominate', 'f-s') + T(6 + 120, 240, 'confluence', 'f-s') + T(6 + 178 * 3 + 168, 250, 'diaphragm', 'f-s', 'end')
    b += box(10, 470, 700, 62, ['Atrial right-to-left shunt is obligatory (arrow). Obstructed supracardiac subset: vertical vein squeezed between',
                                'LPA and left main bronchus. Repair on bypass at 18°C, usually with circulatory arrest; ligate the duct. Early',
                                'mortality 7 to 25% (mainly obstruction); recurrent PV obstruction 5 to 15%: sutureless repair.'], 'b0', 'f-s')
    return svg(542, b)


# ------------------------------------------------------------------ Glenn and Fontan

def _d6_d6_pas(ox, y=80, w=300):
    return (_d6_d6_tube(ox + 20, y, ox + 20 + w, y + 22, 'f-b1')
            + T(ox + 40, y + 38, 'RPA', 'f-s', 'start') + T(ox + w, y + 38, 'LPA', 'f-s', 'end'))


def _d6_d6_ra(ox, x=60, y=170, w=120, h=90):
    return f'<rect x="{ox + x}" y="{y}" width="{w}" height="{h}" rx="18" class="f-b0"/>' + T(ox + x + w / 2, y + h / 2 + 5, 'RA', 'f-s')


def d6_glenn_hemifontan():
    b = T(12, 18, 'Stage II superior cavopulmonary connection (front view; patient\'s right on the left)', 'f-h', 'start')
    # Glenn
    ox = 10
    b += _d6_d6_pas(ox) + _d6_d6_ra(ox)
    b += _d6_d6_tube(ox + 80, 30, ox + 112, 80)
    b += _d6_d6_tube(ox + 80, 128, ox + 112, 170)
    b += line(ox + 76, 128, ox + 116, 128, 'f-cut') + T(ox + 120, 140, 'cardiac end oversewn', 'f-s', 'start')
    b += _d6_d6_tube(ox + 82, 260, ox + 110, 300) + T(ox + 96, 316, 'IVC to RA', 'f-s')
    b += f'<path d="M{ox + 80} 52 C{ox + 50} 52 {ox + 40} 60 {ox + 30} 70" class="f-l" style="stroke-width:4px"/>'
    b += line(ox + 52, 46, ox + 58, 60, 'f-cut') + T(ox + 26, 44, 'azygos tied', 'f-s', 'start')
    b += arrow(ox + 120, 92, ox + 190, 92) + arrow(ox + 76, 92, ox + 34, 92)
    b += T(ox + 118, 46, 'SVC', 'f-s', 'start')
    b += T(ox + 175, 340, 'Bidirectional Glenn', 'f-h')
    b += T(ox + 175, 360, ['SVC divided; cephalic end to the RPA', 'end-to-side; azygos ligated and divided;', 'previous shunt taken down'], 'f-s')
    # Hemi-Fontan
    ox = 370
    b += _d6_d6_pas(ox) + _d6_d6_ra(ox)
    b += _d6_d6_tube(ox + 80, 30, ox + 112, 170)
    b += f'<rect x="{ox + 60}" y="76" width="140" height="30" rx="8" class="f-stent"/>'
    b += _d6_d6_patch(f'M{ox + 76} 150 L{ox + 116} 150', 4)
    b += T(ox + 124, 154, 'PTFE dam in the RA', 'f-s', 'start')
    b += T(ox + 250, 68, 'anterior patch augments PAs', 'f-s')
    b += _d6_d6_tube(ox + 82, 260, ox + 110, 300) + T(ox + 96, 316, 'IVC to RA', 'f-s')
    b += arrow(ox + 120, 92, ox + 190, 92) + arrow(ox + 76, 92, ox + 34, 92)
    b += T(ox + 118, 46, 'SVC', 'f-s', 'start')
    b += T(ox + 175, 340, 'Hemi-Fontan', 'f-h')
    b += T(ox + 175, 360, ['RA-SVC opened onto the opened PAs;', 'dam keeps SVC flow out of the RA;', 'dam excised at lateral tunnel Fontan'], 'f-s')
    b += box(10, 418, 700, 62, ['At 4 to 6 months, when PVR is at its nadir (Mussa: 4 to 5 months, saturation under 75%). SVC flow is about 25 to',
                                '30% of output; saturation afterwards 85 to 90%. Persistent left SVC: bilateral Glenn. Extubate early;',
                                'head up 30°. Hemi-Fontan is more demanding and prone to sinus node dysfunction but simplifies the Fontan.'], 'b0', 'f-s')
    return svg(490, b)


def d6_fontan_types():
    b = T(12, 18, 'Fontan circulation: three ways to bring the IVC to the PAs (front view)', 'f-h', 'start')
    spec = [('ap', 'Atriopulmonary (first)', ['Glenn + RA appendage to', 'the proximal RPA; refractory', 'arrhythmia: convert to TCPC']),
            ('lt', 'Lateral tunnel', ['After hemi-Fontan, 2 to 4 years;', 'PTFE baffle inside the RA;', '3 mm punch fenestration']),
            ('ec', 'Extracardiac conduit', ['After Glenn, 3 to 4 years or', 'about 15 kg; 16 to 20 mm PTFE;', 'fenestration to the RA'])]
    for i, (k, name, ls) in enumerate(spec):
        ox = 10 + i * 237
        b += _d6_d6_tube(ox + 10, 60, ox + 216, 80, 'f-b1')
        b += _d6_d6_tube(ox + 104, 28, ox + 128, 60)
        b += f'<rect x="{ox + 70}" y="130" width="100" height="90" rx="18" class="f-b0"/>' + T(ox + 120, 210, 'RA', 'f-s')
        if k == 'ap':
            b += f'<path d="M{ox + 92} 130 C{ox + 80} 110 {ox + 80} 96 {ox + 86} 80" class="f-l" style="stroke-width:14px;opacity:.35"/>'
            b += T(ox + 64, 112, 'appendage', 'f-s', 'end')
            b += _d6_d6_tube(ox + 106, 220, ox + 128, 260)
            b += arrow(ox + 117, 256, ox + 117, 226)
        elif k == 'lt':
            b += _d6_d6_tube(ox + 106, 220, ox + 128, 260)
            b += _d6_d6_tube(ox + 104, 80, ox + 128, 130)
            b += _d6_d6_patch(f'M{ox + 100} 220 C{ox + 92} 190 {ox + 92} 150 {ox + 100} 130', 4)
            b += f'<circle cx="{ox + 95}" cy="176" r="5" class="f-lumen"/>'
            b += arrow(ox + 117, 254, ox + 117, 86)
            b += T(ox + 84, 180, 'fenestration', 'f-s', 'end')
        else:
            b += _d6_d6_tube(ox + 104, 80, ox + 128, 130)
            b += f'<rect x="{ox + 34}" y="80" width="26" height="180" rx="8" class="f-stent"/>'
            b += _d6_d6_tube(ox + 34, 240, ox + 60, 270)
            b += _d6_d6_tube(ox + 106, 220, ox + 128, 232) + line(ox + 100, 234, ox + 136, 234, 'f-cut')
            b += f'<path d="M{ox + 60} 176 L{ox + 70} 176" class="f-l" style="stroke-width:6px"/>'
            b += arrow(ox + 47, 262, ox + 47, 88)
            b += T(ox + 130, 244, 'RA end oversewn', 'f-s', 'start')
        b += T(ox + 113, 296, name, 'f-h') + T(ox + 113, 316, ls, 'f-s')
    b += T(20, 54, 'RPA', 'f-s', 'start') + T(226, 54, 'LPA', 'f-s', 'end')
    b += box(10, 372, 345, 96, ['Lateral tunnel: less turbulence and energy', 'loss; more even hepatic flow to both lungs', '(helps prevent pulmonary AVMs)', 'Extracardiac: easier; no growth potential'], 'b0', 'f-s')
    b += box(365, 372, 345, 96, ['Fenestration: pop-off that keeps output up', 'while early pressures are high; fewer early', 'effusions; most close spontaneously; costs', 'cyanosis and a route for paradoxical embolism'], 'b1', 'f-s')
    b += box(10, 478, 700, 40, 'Eligibility: adequate PAs · mean PA pressure under 15 mmHg · PVR under 4 WU/m² · competent AV valve · good ventricle', 'ok', 'f-s')
    return svg(528, b)


# ------------------------------------------------------------------ Norwood and hybrid

def _d6_d6_norwood_panel(ox, sano):
    cx = ox + 180
    b = f'<path d="M{cx - 80} 250 C{cx - 80} 214 {cx - 40} 204 {cx} 204 C{cx + 40} 204 {cx + 76} 214 {cx + 76} 250 C{cx + 76} 290 {cx + 20} 310 {cx - 4} 310 C{cx - 40} 310 {cx - 80} 290 {cx - 80} 250 Z" class="f-b0"/>'
    b += T(cx, 270, 'Single RV', 'f-s')
    b += _d6_d6_tube(ox + 40, 150, ox + 160, 168, 'f-b1')
    b += T(ox + 44, 144, 'Branch PAs', 'f-s', 'start')
    b += f'<path d="M{cx + 10} 206 L{cx + 10} 110 C{cx + 10} 60 {cx + 120} 60 {cx + 120} 110 L{cx + 120} 300" class="f-vessel"/>'
    b += f'<path d="M{cx - 18} 206 L{cx - 14} 132 C{cx - 12} 118 {cx - 4} 112 {cx + 4} 112" class="f-vessel" style="stroke-width:8"/>'
    b += f'<path d="M{cx + 40} 72 L{cx + 20} 30" class="f-vessel" style="stroke-width:10"/>'
    b += T(cx + 65, 180, 'Neoaorta', 'f-s')
    b += T(cx - 26, 110 if sano else 196, 'hypoplastic aorta', 'f-s', 'end')
    if sano:
        b += f'<path d="M{cx - 60} 216 C{cx - 80} 190 {ox + 110} 190 {ox + 110} 168" class="f-stent" style="stroke-width:5px"/>'
        b += T(ox + 20, 236, ['RV-PA', 'conduit'], 'f-h', 'start')
    else:
        b += f'<path d="M{cx + 22} 40 C{cx - 40} 40 {ox + 90} 90 {ox + 80} 150" class="f-stent" style="stroke-width:5px"/>'
        b += T(ox + 20, 60, ['Modified BT', 'shunt'], 'f-h', 'start')
    return b


def d6_norwood():
    b = T(12, 18, 'Norwood stage I: two sources of pulmonary flow (front view, arrangement schematic)', 'f-h', 'start')
    b += _d6_d6_norwood_panel(0, False) + _d6_d6_norwood_panel(360, True)
    b += line(360, 30, 360, 316, 'f-dash')
    b += T(180, 332, ['Innominate or right subclavian to the RPA;', 'beyond the valve: systemic run-off and', 'coronary steal'], 'f-s')
    b += T(540, 332, ['RV to the PAs: less run-off; diastolic', 'BP 46 to 49.5 versus 37 to 38.4 mmHg', '(Yuan 2009 pooled table)'], 'f-s')
    b += box(10, 392, 700, 44, ['All: atrial septectomy · main PA divided at the bifurcation and joined to the hypoplastic aorta (neoaorta;',
                                'coronaries arise from the small native root) · shunt for regulated pulmonary flow'], 'b1', 'f-s')
    rows = [('', 'RV-PA', 'BT'), ('Hospital survival', '92 to 93%', '70 to 72%'), ('Interstage mortality', '0', '23%'),
            ('Shunt reintervention', '32%', '17%')]
    for i, (a, r, s) in enumerate(rows):
        y = 452 + i * 24
        cls = 'f-h' if i == 0 else ''
        b += T(170, y + 16, a, cls, 'end') + T(240, y + 16, r, 'f-h' if i == 0 else 'f-n') + T(330, y + 16, s, 'f-h' if i == 0 else 'f-n')
        if i:
            b += line(20, y, 370, y, 'f-grid')
    b += box(390, 452, 320, 92, ['SVR trial: transplant-free survival', 'better with the RV-PA conduit at', '12 months; equal at 3 years, with more', 'reintervention in the RV-PA arm'], 'b0', 'f-s')
    return svg(554, b)


def d6_hybrid():
    b = T(12, 18, 'Hybrid stage I for HLHS: sternotomy, no bypass (arrangement schematic)', 'f-h', 'start')
    cx = 210
    b += f'<path d="M{cx - 80} 290 C{cx - 80} 250 {cx - 40} 240 {cx} 240 C{cx + 40} 240 {cx + 76} 250 {cx + 76} 290 C{cx + 76} 326 {cx + 20} 344 {cx - 4} 344 C{cx - 40} 344 {cx - 80} 326 {cx - 80} 290 Z" class="f-b0"/>'
    b += T(cx, 304, 'Single RV', 'f-s')
    # main PA, duct to descending aorta
    b += f'<path d="M{cx + 10} 242 L{cx + 10} 160 C{cx + 10} 120 {cx + 100} 110 {cx + 120} 150 L{cx + 140} 340" class="f-vessel"/>'
    b += f'<path d="M{cx + 60} 116 C{cx + 90} 112 {cx + 112} 126 {cx + 122} 156" class="f-stent" style="stroke-width:4px"/>'
    b += T(cx + 132, 112, 'Ductal stent', 'f-h', 'start')
    b += T(cx + 150, 352, 'Descending aorta', 'f-s', 'start')
    # branch PAs with bands
    b += _d6_d6_tube(cx - 120, 166, cx + 2, 180, 'f-b1') + _d6_d6_tube(cx + 18, 186, cx + 90, 198, 'f-b1')
    b += f'<rect x="{cx - 80}" y="160" width="10" height="26" rx="3" class="f-warn"/>'
    b += f'<rect x="{cx + 50}" y="180" width="10" height="24" rx="3" class="f-warn"/>'
    b += T(cx - 120, 156, 'RPA band', 'f-h', 'start') + T(cx + 50, 222, 'LPA band', 'f-h')
    # hypoplastic ascending aorta and arch, retrograde
    b += f'<path d="M{cx - 18} 242 L{cx - 18} 90 C{cx - 18} 60 {cx + 60} 56 {cx + 100} 74 L{cx + 118} 140" class="f-l" style="stroke-width:5px"/>'
    b += f'<path d="M{cx + 40} 62 L{cx + 30} 34" class="f-l" style="stroke-width:4px"/>'
    b += arrow(cx + 70, 50, cx + 20, 50)
    b += T(cx - 28, 82, ['Hypoplastic arch:', 'retrograde flow to', 'head and coronaries'], 'f-s', 'end')
    # atria
    b += '<rect x="20" y="250" width="50" height="40" rx="10" class="f-b0"/><rect x="70" y="250" width="50" height="40" rx="10" class="f-b0"/>'
    b += T(45, 275, 'RA', 'f-s') + T(95, 275, 'LA', 'f-s') + arrow(92, 296, 50, 296)
    b += T(70, 320, ['Septostomy or', 'septal stent'], 'f-s')
    b += _d6_d6_card(440, 30, 270, 92, 'High-risk features for Norwood', ['Under 34 weeks; under 2.5 kg; restrictive', 'septum; moderate AV regurgitation or RV', 'dysfunction; extracardiac anomalies'], 'b0')
    b += _d6_d6_card(440, 132, 270, 76, 'Next step', ['Interval Norwood at 6 to 8 weeks, or', 'comprehensive stage II at 3 to 6 months'], 'b1')
    b += _d6_d6_card(440, 218, 270, 112, 'Drawbacks', ['Unrepaired arch: retrograde arch', 'obstruction (cerebral and coronary', 'malperfusion); restrictive septum;', 'branch PA distortion; bigger stage II'], 'warn')
    b += box(10, 360, 700, 44, ['Survival advantage only to 30 days; no difference at 1 year; more unplanned reinterventions.',
                                'Reversed BT (main PA to innominate) can feed the arch and may help ascending aortic growth.'], 'b0', 'f-s')
    return svg(414, b)


# ------------------------------------------------------------------ Ebstein

def d6_ebstein_anatomy():
    b = T(12, 18, 'Ebstein anomaly: four-chamber schematic (right heart on the left)', 'f-h', 'start')
    b += '<rect x="30" y="40" width="430" height="320" rx="40" class="f-b0"/>'
    b += '<rect x="241" y="40" width="10" height="320" class="f-b1"/>'
    # atrialised RV
    b += '<path d="M34 140 L241 140 L241 226 C190 226 120 210 34 240 Z" class="f-warn"/>'
    b += line(34, 140, 241, 140, 'f-dash')
    b += T(60, 134, 'True AV junction (dilated)', 'f-s', 'start')
    b += T(130, 186, 'Atrialised RV', 'f-h')
    # septal leaflet displaced to 226, anterior leaflet sail from true annulus
    b += _d6_d6_leaf('M241 226 L206 236', 5)
    b += _d6_d6_leaf('M40 142 C70 200 80 260 140 290', 5)
    b += T(80, 310, ['Sail-like anterior', 'leaflet'], 'f-s')
    b += '<path d="M232 142 L232 224" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += T(262, 240, ['Septal leaflet displaced', 'at least 0.8 cm/m²'], 'f-s', 'start')
    b += T(130, 90, 'RA (dilated)', 'f-s') + T(196, 334, 'Functional RV', 'f-s')
    b += _d6_d6_leaf('M254 200 L320 204', 4) + _d6_d6_leaf('M380 204 L454 200', 4)
    b += T(350, 120, 'LA', 'f-s') + T(350, 280, 'LV', 'f-s')
    b += '<rect x="241" y="80" width="10" height="26" class="f-warn"/>' + arrow(224, 94, 268, 94)
    b += T(276, 80, 'ASD: right-to-left', 'f-s', 'start')
    b += '<circle cx="246" cy="140" r="6" class="f-ah"/>' + T(258, 158, 'AV node: normal position', 'f-s', 'start')
    items = ['1 Failure of delamination: septal and', '   posterior leaflets adherent, tethered',
             '2 Sail-like anterior leaflet; functional', '   annulus displaced towards the apex',
             '3 Dilated atrialised RV, thin free wall',
             '4 Anterior leaflet redundancy,', '   fenestrations and tethering',
             '5 Dilated true tricuspid annulus']
    b += f'<rect x="474" y="40" width="236" height="200" rx="10" class="f-b0"/>' + T(484, 60, 'Five anatomical features', 'f-h', 'start')
    for i, s in enumerate(items):
        b += T(484, 82 + i * 19, s, 'f-s', 'start')
    b += box(474, 250, 236, 110, ['Accessory pathways in about', '15 to 25%, usually right-sided,', 'often multiple: EP study and', 'ablation before tricuspid surgery'], 'warn', 'f-s')
    return svg(370, b)


def d6_cone():
    b = T(12, 18, 'Da Silva cone reconstruction, seen from the right atrium (arrangement schematic)', 'f-h', 'start')
    for i, (title, ls) in enumerate([('1 Before', ['Leaflets stuck to the RV;', 'small displaced orifice']),
                                      ('2 Delaminate', ['Free the leaflets; relieve RVOT', 'obstruction from the apparatus']),
                                      ('3 Cone', ['360° of leaflet tissue', 'attached at the true annulus'])]):
        cx = 125 + i * 235
        b += f'<circle cx="{cx}" cy="120" r="76" class="f-dash"/>'
        if i == 0:
            b += f'<path d="M{cx - 70} 96 A74 74 0 0 1 {cx + 52} 66" class="f-l" style="stroke-width:6px"/>'
            b += f'<path d="M{cx + 60} 150 A74 74 0 0 1 {cx - 50} 176" class="f-cut" style="stroke-width:10px"/>'
            b += f'<circle cx="{cx + 22}" cy="140" r="16" class="f-lumen"/>'
            b += T(cx, 216, 'true annulus (dashed)', 'f-s')
        elif i == 1:
            b += f'<path d="M{cx - 66} 100 A70 70 0 0 1 {cx + 50} 70" class="f-l" style="stroke-width:6px"/>'
            b += f'<path d="M{cx + 54} 140 A60 60 0 0 1 {cx - 44} 160" class="f-l" style="stroke-width:6px"/>'
            b += arrow(cx, 170, cx, 140) + arrow(cx - 20, 100, cx - 6, 116)
        else:
            b += f'<circle cx="{cx}" cy="120" r="74" class="f-l" style="stroke-width:6px"/>'
            b += f'<circle cx="{cx}" cy="120" r="30" class="f-lumen"/>'
            for a in range(0, 360, 30):
                x1 = cx + 68 * math.cos(math.radians(a)); y1 = 120 + 68 * math.sin(math.radians(a))
                x2 = cx + 82 * math.cos(math.radians(a)); y2 = 120 + 82 * math.sin(math.radians(a))
                b += line(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), 'f-cut')
            b += T(cx, 124, 'cone', 'f-s')
        b += T(cx, 236, title, 'f-h') + T(cx, 256, ls, 'f-s')
        if i < 2:
            b += arrow(cx + 92, 120, cx + 140, 120)
    b += box(10, 300, 345, 96, ['Older children and adults: close the ASD;', 'repair (cone) or replace the valve (bio-', 'prosthesis); selective plication; reduction', 'atrioplasty; arrhythmia surgery'], 'b1', 'f-s')
    b += box(365, 300, 345, 96, ['One-and-a-half ventricle repair (add Glenn):', 'big or poor RV, leftward septal shift, small', 'orifice after repair. Neonate with anatomical', 'pulmonary atresia: Starnes RV exclusion'], 'b0', 'f-s')
    return svg(406, b)


# ---- figs_D7.py
"""D7 drawings: hilar anatomy, VATS access, sleeve variants, pneumonectomy, node map,
vein variants. Original schematics drawn from the ST4 notes and TSRA Review text."""
import math



# ---------------------------------------------------------------- helpers

def _d7_bez(p0, p1, p2, n=14):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


def _d7_tube(pts, w, cls, extra=''):
    """Filled tube of width w along a polyline (vessel or bronchus)."""
    n = len(pts)
    L, R = [], []
    for i, (x, y) in enumerate(pts):
        if i == 0:
            dx, dy = pts[1][0] - x, pts[1][1] - y
        elif i == n - 1:
            dx, dy = x - pts[i - 1][0], y - pts[i - 1][1]
        else:
            dx, dy = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        ln = math.hypot(dx, dy) or 1
        nx, ny = -dy / ln * w / 2, dx / ln * w / 2
        L.append((x + nx, y + ny))
        R.append((x - nx, y - ny))
    d = 'M' + ' L'.join(f'{a:.1f} {b:.1f}' for a, b in L + R[::-1]) + ' Z'
    return f'<path d="{d}" class="{cls}"{extra}/>'


def _d7_num(x, y, n, cls='f-warn'):
    return f'<circle cx="{x}" cy="{y}" r="10" class="{cls}"/>' + T(x, y + 4.5, str(n), 'f-h')


def _d7_leg(x, y, items, gap=8):
    """items: (number or None, [lines]). Numbered legend, returns (svg, end y)."""
    b = ''
    for n, lines in items:
        if n is not None:
            b += _d7_num(x + 10, y + 1, n)
            b += T(x + 28, y + 5, lines, 'f-s', 'start')
        else:
            b += T(x, y + 5, lines, 'f-s', 'start')
        y += 17 * len(lines) + gap
    return b, y


def _d7_cut(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="f-cut" stroke-dasharray="5 3"/>'


# ---------------------------------------------------------------- t9 hilum

def d7_right_hilum():
    """Right hilum from the front with the order of division for upper lobectomy."""
    b = T(12, 22, 'Right hilum from the front: upper lobectomy by the anterior approach', 'f-h', 'start')
    b += T(12, 42, "Arrangement schematic, not to scale. Patient's right on the left. Numbers: order of division.", 'f-s', 'start')
    b += ('<path d="M220 62 C130 56 44 120 36 232 C32 312 48 380 66 404 L300 404 '
          'C314 344 318 290 322 236 C326 150 300 70 220 62 Z" class="f-dash"/>')
    b += T(120, 100, 'Upper lobe', 'f-s') + T(86, 282, 'Middle lobe', 'f-s') + T(130, 386, 'Lower lobe', 'f-s')
    # vagus, behind the hilum
    b += '<path d="M372 56 C366 170 356 280 350 408" class="f-nerve" stroke-dasharray="2 4"/>'
    # airway, the most posterior layer
    b += _d7_tube([(392, 54), (392, 150)], 26, 'f-lumen')
    b += _d7_tube([(392, 148), (440, 178)], 20, 'f-lumen')
    b += _d7_tube([(392, 148), (334, 186)], 22, 'f-lumen')
    b += _d7_tube([(342, 180), (290, 158), (246, 150)], 15, 'f-lumen')
    b += _d7_tube([(336, 184), (316, 262)], 18, 'f-lumen')
    b += _d7_tube([(318, 250), (266, 276)], 11, 'f-lumen')
    b += _d7_tube([(316, 260), (308, 344)], 15, 'f-lumen')
    b += T(408, 72, 'Trachea', 'f-s', 'start')
    # azygos arch over the right main bronchus
    b += _d7_tube(_d7_bez((322, 214), (316, 132), (378, 124)), 11, 'f-warn')
    b += T(316, 116, 'Azygos', 'f-s', 'end')
    # posterior ascending artery (behind the superior vein), dashed
    b += _d7_tube(_d7_bez((298, 290), (272, 262), (240, 238)), 8, 'f-b1', ' stroke-dasharray="4 3"')
    # right pulmonary artery, in front of the bronchus
    b += _d7_tube([(452, 216), (350, 214)] + _d7_bez((350, 214), (304, 222), (298, 270))[1:] + [(288, 344)], 22, 'f-b1')
    b += _d7_tube(_d7_bez((352, 212), (300, 178), (238, 172)), 13, 'f-b1')
    b += T(452, 202, 'Right PA', 'f-s', 'end')
    # superior vein (most anterior) with upper lobe branches and middle lobe vein
    b += _d7_tube(_d7_bez((214, 216), (250, 230), (296, 256)), 10, 'f-warn')
    b += _d7_tube(_d7_bez((218, 250), (262, 252), (296, 258)), 9, 'f-warn')
    b += _d7_tube(_d7_bez((232, 312), (262, 278), (298, 262)), 10, 'f-warn')
    b += _d7_tube([(296, 258), (408, 272)], 20, 'f-warn')
    # inferior vein and the pulmonary ligament
    b += _d7_tube(_d7_bez((236, 352), (330, 334), (410, 334)), 20, 'f-warn')
    b += '<path d="M276 362 L292 404 M300 356 L316 404" class="f-dash"/>'
    b += T(262, 420, 'Pulmonary ligament', 'f-s')
    b += '<ellipse cx="428" cy="304" rx="20" ry="50" class="f-warn"/>' + T(428, 308, 'LA', 'f-s')
    # phrenic, in front
    b += '<path d="M344 56 C340 170 344 290 356 408" class="f-nerve"/>'
    # order of division
    b += _d7_num(204, 232, 1) + _d7_num(234, 194, 2) + _d7_num(232, 136, 3) + _d7_num(232, 262, 4)
    b += _d7_num(70, 230, 5)
    b += T(232, 330, 'Middle lobe vein', 'f-s', 'end')
    lx = 470
    s, y = _d7_leg(lx, 72, [
        (1, ['Superior vein: the upper lobe', 'branches only. Keep the middle', 'lobe vein, which joins it']),
        (2, ['Truncus anterior: the first', 'branch of the right PA']),
        (3, ['Upper lobe bronchus: highest,', 'within 2.5 cm of the carina, just', 'inferomedial to the azygos']),
        (4, ['Posterior ascending artery, behind', 'the bronchus (dashed where the', 'superior vein hides it)']),
        (5, ['Fissures (fissure-last if fused)']),
    ])
    b += s
    s, y = _d7_leg(lx, y + 2, [
        (None, ['Blue: artery. Red: veins. Outlined:', 'airway. Yellow: phrenic 1.5 cm in', 'front (solid), vagus behind (dotted).']),
        (None, ['Main bronchus above its artery', '(eparterial). Afterwards check the', 'middle lobe for torsion.']),
    ])
    b += s
    return svg(432, b)



def d7_left_hilum():
    """Left hilum from the front with the order of division for upper lobectomy."""
    b = T(12, 22, 'Left hilum from the front: upper lobectomy by the anterior approach', 'f-h', 'start')
    b += T(12, 42, "Arrangement schematic, not to scale. Patient's left on the right. Numbers: order of division.", 'f-s', 'start')
    b += ('<path d="M250 70 C340 62 420 124 428 236 C432 316 416 384 398 408 L170 408 '
          'C156 348 152 294 150 240 C148 160 176 80 250 70 Z" class="f-dash"/>')
    b += T(352, 104, 'Upper lobe', 'f-s') + T(384, 300, 'Lingula', 'f-s') + T(350, 392, 'Lower lobe', 'f-s')
    # vagus behind
    b += '<path d="M122 56 C126 170 138 280 146 408" class="f-nerve" stroke-dasharray="2 4"/>'
    # aorta: arch over the left main bronchus, descending behind
    b += _d7_tube(_d7_bez((34, 232), (40, 76), (130, 74)) + _d7_bez((130, 74), (204, 74), (208, 150))[1:] + [(208, 176)], 22, 'f-ok')
    b += T(196, 60, 'Aortic arch', 'f-s', 'start')
    # airway (posterior)
    b += _d7_tube([(80, 54), (80, 150)], 26, 'f-lumen')
    b += _d7_tube([(80, 148), (40, 176)], 20, 'f-lumen')
    b += _d7_tube([(80, 148), (222, 226)], 19, 'f-lumen')
    b += _d7_tube([(222, 224), (236, 334)], 15, 'f-lumen')
    b += T(62, 60, 'Trachea', 'f-s', 'end')
    # left PA: over the main bronchus, then down behind the upper lobe bronchus
    pa = [(64, 262), (126, 214)] + _d7_bez((126, 214), (200, 146), (262, 172))[1:] + _d7_bez((262, 172), (296, 204), (288, 340))[1:]
    b += _d7_tube(pa, 22, 'f-b1')
    b += T(56, 266, 'Main PA', 'f-s', 'end')
    # upper lobe arterial branches
    b += _d7_tube([(206, 166), (210, 132)], 8, 'f-b1')
    b += _d7_tube([(226, 162), (234, 130)], 8, 'f-b1')
    b += _d7_tube(_d7_bez((256, 172), (276, 132), (312, 120)), 9, 'f-b1')
    b += _d7_tube(_d7_bez((292, 254), (322, 262), (352, 282)), 8, 'f-b1')
    # upper lobe bronchus in front of the descending artery
    b += _d7_tube(_d7_bez((216, 222), (262, 206), (318, 182)), 15, 'f-lumen')
    # ligamentum and recurrent nerve
    b += line(150, 86, 166, 171, 'f-l')
    b += '<path d="M176 52 C176 110 176 160 164 166 C152 170 146 156 146 136 C146 104 136 76 130 52" class="f-nerve"/>'
    # veins
    b += _d7_tube(_d7_bez((340, 210), (300, 240), (240, 254)) + _d7_bez((240, 254), (180, 262), (118, 276))[1:], 20, 'f-warn')
    b += _d7_tube(_d7_bez((340, 346), (240, 330), (118, 330)), 20, 'f-warn')
    b += '<path d="M214 352 L200 404 M240 350 L228 404" class="f-dash"/>'
    b += '<ellipse cx="104" cy="306" rx="20" ry="50" class="f-warn"/>' + T(104, 310, 'LA', 'f-s')
    # phrenic in front
    b += '<path d="M180 50 C186 170 178 290 168 408" class="f-nerve"/>'
    b += _d7_num(320, 236, 1) + _d7_num(220, 112, 2) + _d7_num(332, 166, 3) + _d7_num(368, 270, 4) + _d7_num(404, 214, 5)
    b += T(150, 424, 'Plain line: ligamentum, with the recurrent nerve hooked round it', 'f-s', 'start')
    lx = 470
    s, y = _d7_leg(lx, 72, [
        (1, ['Superior vein, once the inferior', 'vein is seen: common trunk in 25%']),
        (2, ['First arterial branches: the short', 'anterior ones hidden by the vein', 'tear; apicoposterior avulsion is', 'the classic injury']),
        (3, ['Upper lobe bronchus']),
        (4, ['Remaining arteries, lingular', 'included (2 to 7 branches in all)']),
        (5, ['Fissure']),
    ])
    b += s
    s, y = _d7_leg(lx, y + 2, [
        (None, ['The artery arches over the bronchus', '(hyparterial) and runs behind the', 'upper lobe bronchus: consider', 'proximal control of the main PA.']),
        (None, ['Recurrent nerve at station 5;', 'phrenic in front, vagus behind.']),
    ])
    b += s
    return svg(438, b)



def d7_fissure_arteries():
    """The pulmonary artery in the oblique fissure on each side."""
    b = T(12, 22, 'The artery in the oblique fissure: what to divide and what to keep', 'f-h', 'start')
    b += T(12, 42, 'Arrangement schematic: each lung seen from the side with the fissure opened; front to the left.', 'f-s', 'start')
    for ox, side in ((0, 'R'), (365, 'L')):
        cx = ox + 175
        b += f'<rect x="{ox + 10}" y="56" width="345" height="300" rx="14" class="f-track"/>'
        b += T(ox + 24, 78, 'Right lung' if side == 'R' else 'Left lung', 'f-h', 'start')
        b += T(ox + 24, 344, 'front', 'f-s', 'start') + T(ox + 342, 344, 'back', 'f-s', 'end')
        b += _d7_tube([(cx, 90), (cx, 314)], 22, 'f-b1')
        if side == 'R':
            b += _d7_tube(_d7_bez((cx, 130), (cx + 40, 118), (cx + 70, 96)), 9, 'f-b1')
            b += T(cx + 76, 100, ['Posterior ascending', '(upper lobe)'], 'f-s', 'start')
            b += _d7_tube(_d7_bez((cx, 190), (cx - 40, 192), (cx - 78, 176)), 10, 'f-b1')
            b += _d7_tube(_d7_bez((cx, 212), (cx - 40, 218), (cx - 74, 226)), 8, 'f-b1')
            b += T(cx - 84, 154, ['Middle lobe', 'artery, 1 or 2'], 'f-s', 'end')
            b += _d7_tube(_d7_bez((cx, 198), (cx + 44, 196), (cx + 80, 206)), 10, 'f-b1')
            b += T(cx + 86, 196, ['Superior', 'segmental'], 'f-s', 'start')
            b += f'<path d="M{cx - 92} 202 L{cx + 104} 202" class="f-dash"/>'
            b += T(cx + 20, 252, ['arise opposite', 'each other'], 'f-s', 'start')
        else:
            b += _d7_tube(_d7_bez((cx, 104), (cx - 30, 92), (cx - 64, 92)), 8, 'f-b1')
            b += _d7_tube(_d7_bez((cx, 126), (cx + 40, 110), (cx + 64, 92)), 9, 'f-b1')
            b += T(cx - 70, 96, 'Anterior', 'f-s', 'end') + T(cx + 70, 96, 'Apicoposterior', 'f-s', 'start')
            b += _d7_tube(_d7_bez((cx, 196), (cx - 40, 200), (cx - 78, 214)), 10, 'f-b1')
            b += T(cx - 84, 180, 'Lingular', 'f-s', 'end')
            b += _d7_tube(_d7_bez((cx, 204), (cx + 44, 204), (cx + 80, 214)), 10, 'f-b1')
            b += T(cx + 86, 204, ['Superior', 'segmental'], 'f-s', 'start')
        # basal arteries
        for dx in (-34, -12, 12, 34):
            b += _d7_tube([(cx, 300), (cx + dx, 336)], 6, 'f-b1')
        b += T(cx + 46, 306, 'Basal arteries', 'f-s', 'start')
    # notes
    b += box(10, 372, 345, 96, ['Right lower: ligament and vein, then basal and', 'superior segmental arteries here, then bronchus.', 'The superior segmental artery may come off the', 'middle lobe artery. Keep the middle lobe artery.'], 'b0', 'f-s')
    b += box(375, 372, 335, 96, ['Left lower: ligament and vein, arteries here,', 'then bronchus; keep the lingular artery and vein.', 'Left upper: 2 to 7 branches in all; identify', 'each one to avoid injury.'], 'b0', 'f-s')
    return svg(478, b)


def d7_vats_access():
    """Multiport VATS access for lobectomy, and what the notes say about uniportal and robotic."""
    b = T(12, 22, 'VATS lobectomy access: patient lateral, chest wall seen from the side', 'f-h', 'start')
    b += T(12, 42, 'Arrangement schematic: only the two sites the notes give are marked; not to scale.', 'f-s', 'start')
    b += '<rect x="20" y="60" width="340" height="300" rx="70" class="f-track"/>'
    b += T(36, 80, 'Front', 'f-s', 'start') + T(344, 350, 'Back', 'f-s', 'end')
    for i in range(7):
        y = 116 + i * 32
        b += f'<path d="M34 {y + 20} C130 {y + 4} 250 {y - 6} 346 {y - 16}" class="f-grid" fill="none"/>'
    b += T(40, 222, '5th space', 'f-s', 'start') + T(40, 318, '8th space', 'f-s', 'start')
    b += line(150, 64, 150, 356, 'f-dash') + line(214, 64, 214, 356, 'f-dash')
    b += T(150, 378, 'Anterior axillary line', 'f-s') + T(256, 396, 'Mid-axillary line', 'f-s')
    b += line(244, 384, 216, 358, 'f-grid')
    b += '<path d="M280 70 L340 74 L316 160 Z" class="f-b0"/>' + T(274, 150, 'Scapula tip', 'f-s', 'end')
    b += '<path d="M118 200 C138 196 160 192 184 188" class="f-cut" style="stroke-width:5"/>'
    b += _d7_num(110, 176, 1)
    b += '<circle cx="214" cy="286" r="8" class="f-b1"/>' + _d7_num(240, 266, 2, 'f-b1')
    b += '<path d="M80 208 C150 198 240 186 300 172" class="f-cut" stroke-dasharray="6 5"/>'
    b += _d7_num(306, 196, 3)
    lx = 384
    s, y = _d7_leg(lx, 70, [
        (1, ['Utility incision: 5th space, anterior', 'axillary line. The 5th space lies on', 'the oblique fissure and the hilum']),
        (2, ['Camera: 8th space']),
        (3, ['Conversion: along the same space as', 'a muscle-sparing lateral thoracotomy;', 'drape for a thoracotomy from the start']),
    ])
    b += s
    s, y = _d7_leg(lx, y + 2, [
        (None, ['Set-up: lateral decubitus, table broken at', 'the 5th space, double-lumen tube or blocker,', 'lung isolated before the first port.']),
        (None, ['Uniportal: no better than multiport in one', 'trial (ERAS/ESTS 2019). Uniportal and', 'subxiphoid uniportal should spare the', 'intercostal nerve most; few good trials.']),
        (None, ['Chronic pain after VATS: three ports', 'OR 4.3 (Chen 2023).']),
        (None, ['Robotic: outcomes like VATS, longer and', 'dearer. No port layout in these notes.']),
    ])
    b += s
    return svg(max(410, y + 4), b)


def _d7_airway(ox, oy, s=1.0):
    """Small frontal airway tree; main bronchi split into proximal and distal parts."""
    P = lambda x, y: (ox + x * s, oy + y * s)  # noqa: E731
    return {
        'trachea': [P(70, 0), P(70, 50)],
        'rmbp': [P(70, 50), P(61, 58)],
        'rmbd': [P(61, 58), P(48, 70)],
        'rul': [P(50, 68), P(14, 54)],
        'bi': [P(48, 70), P(38, 104)],
        'rml': [P(40, 98), P(14, 112)],
        'rll': [P(38, 104), P(34, 146)],
        'lmbp': [P(70, 50), P(88, 67)],
        'lmbd': [P(88, 67), P(108, 86)],
        'lul': [P(104, 82), P(136, 64)],
        'lll': [P(108, 86), P(116, 146)],
    }


def _d7_xcut(a, k, f):
    (x1, y1), (x2, y2) = a[k]
    cx, cy = x1 + (x2 - x1) * f, y1 + (y2 - y1) * f
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy)
    nx, ny = -dy / ln * 11, dx / ln * 11
    return _d7_cut(round(cx + nx, 1), round(cy + ny, 1), round(cx - nx, 1), round(cy - ny, 1))


def d7_sleeve_variants():
    """Which airway each sleeve removes and what is rejoined."""
    b = T(12, 22, 'Sleeve resections: what is removed (red) and what is rejoined', 'f-h', 'start')
    b += T(12, 42, "Schematic airway from the front, patient's right on the left. Ordered from the commonest.", 'f-s', 'start')
    panels = [
        ('Right upper', '', ['rmbd', 'rul'], 'Intermedius to', 'main bronchus', [('rmbp', 0.95), ('bi', 0.2)]),
        ('Left upper', '', ['lmbd', 'lul'], 'Lower lobe bronchus', 'to main bronchus', [('lmbp', 0.95), ('lll', 0.12)]),
        ('Left lower', '', ['lmbd', 'lll'], 'Upper lobe bronchus', 'to main bronchus', [('lmbp', 0.95), ('lul', 0.3)]),
        ('Right upper and', 'middle (extended)', ['rmbd', 'rul', 'bi', 'rml'], 'Lower lobe bronchus', 'to main bronchus', [('rmbp', 0.95), ('rll', 0.12)]),
        ('Right middle and', 'lower (extended)', ['rmbd', 'bi', 'rml', 'rll'], 'Upper lobe bronchus', 'to main bronchus', [('rmbp', 0.95), ('rul', 0.3)]),
    ]
    pw = 140
    for i, (name, sub, removed, r1, r2, cuts) in enumerate(panels):
        ox = 10 + i * pw
        b += f'<rect x="{ox}" y="56" width="{pw - 8}" height="290" rx="10" class="f-track"/>'
        b += T(ox + (pw - 8) / 2, 78, name, 'f-h')
        if sub:
            b += T(ox + (pw - 8) / 2, 96, sub, 'f-s')
        a = _d7_airway(ox - 4, 112, 1.0)
        for k, pts in a.items():
            w = 15 if k == 'trachea' else 10
            b += _d7_tube(pts, w, 'f-warn' if k in removed else 'f-lumen')
        for k, f in cuts:
            b += _d7_xcut(a, k, f)
        b += T(ox + (pw - 8) / 2, 300, r1, 'f-s') + T(ox + (pw - 8) / 2, 317, r2, 'f-s')
    b += T(12, 368, 'Red dashes: the two lines of division, at right angles; both margins go for frozen section.', 'f-s', 'start')
    b += T(12, 386, 'Also: sleeve of the main bronchus alone, without lung, for benign stricture or a low-grade tumour.', 'f-s', 'start')
    b += T(12, 404, 'The longer left main bronchus suits a sleeve; the right upper lobe bronchus arises within 2.5 cm of the carina.', 'f-s', 'start')
    return svg(414, b)


def d7_pneumonectomy_stump():
    """Pneumonectomy: order of division and how the bronchial stump is made and covered."""
    b = T(12, 22, 'Pneumonectomy: order of division and the bronchial stump', 'f-h', 'start')
    b += T(12, 42, 'Schematic of a right pneumonectomy, not to scale. Red: the stump. Left: to avoid. Right: as intended.', 'f-s', 'start')
    for ox, good in ((10, False), (250, True)):
        b += f'<rect x="{ox}" y="56" width="226" height="250" rx="12" class="f-track"/>'
        b += _d7_tube([(ox + 128, 66), (ox + 128, 170)], 30, 'f-lumen')
        b += _d7_tube([(ox + 128, 168), (ox + 178, 210), (ox + 200, 236)], 22, 'f-lumen')
        if good:
            b += _d7_tube([(ox + 128, 168), (ox + 106, 186)], 22, 'f-warn')
            b += _d7_cut(ox + 96, 172, ox + 116, 198)
            b += '<path d="M%d 156 C%d 176 %d 204 %d 214" class="f-duct"/>' % (ox + 80, ox + 82, ox + 94, ox + 114)
            b += T(ox + 113, 252, 'Flush with the carina', 'f-h')
            b += T(ox + 113, 270, ['Green: pleura, pericardial fat,', 'muscle or azygos over it'], 'f-s')
        else:
            b += _d7_tube([(ox + 128, 168), (ox + 60, 222)], 22, 'f-warn')
            b += _d7_cut(ox + 46, 208, ox + 66, 234)
            b += T(ox + 113, 252, 'Long stump', 'f-h')
            b += T(ox + 113, 270, ['Devascularised length: a risk', 'factor for fistula'], 'f-s')
        b += T(ox + 150, 84, 'Trachea', 'f-s', 'start')
    b += box(490, 56, 220, 120, ['Order: inferior ligament,', 'veins, then artery, then', 'bronchus, with frozen', 'section. Keep the phrenic.'], 'b1', 'f-s')
    b += box(490, 186, 220, 120, ['Little diathermy at the', 'carina and subcarinal', 'region. Left side harder:', 'the aorta is in the way.'], 'warn', 'f-s')
    b += box(10, 318, 340, 60, ['Intrapericardial: close a right pericardial', 'defect (herniation, rotation); left is rare'], 'b0', 'f-s')
    b += box(360, 318, 350, 60, ['Generally tolerated if predicted postoperative', 'FEV1 and transfer factor both over 60% (TSRA)'], 'b0', 'f-s')
    return svg(388, b)


def d7_segment_tree():
    """Bronchial tree to segment level, and where artery and veins run in a segment."""
    b = T(12, 22, 'Segmental bronchi by lobe, and the vessels within a segment', 'f-h', 'start')
    b += T(12, 42, "Schematic airway, patient's right on the left: ten segments on the right, eight on the left.", 'f-s', 'start')
    c = 262
    b += _d7_tube([(c, 54), (c, 96)], 20, 'f-lumen')
    b += _d7_tube([(c, 94), (c - 50, 112)], 15, 'f-lumen') + _d7_tube([(c, 94), (c + 54, 116)], 14, 'f-lumen')
    b += _d7_tube([(c - 44, 110), (c - 100, 84)], 11, 'f-lumen')
    b += T(c - 106, 80, 'Upper', 'f-h', 'end') + T(c - 106, 98, ['apical, anterior,', 'posterior'], 'f-s', 'end')
    b += _d7_tube([(c - 50, 112), (c - 68, 170)], 12, 'f-lumen')
    b += T(c - 40, 152, ['bronchus', 'intermedius'], 'f-s', 'start')
    b += _d7_tube([(c - 64, 160), (c - 110, 178)], 9, 'f-lumen')
    b += T(c - 116, 176, 'Middle', 'f-h', 'end') + T(c - 116, 194, 'lateral, medial', 'f-s', 'end')
    b += _d7_tube([(c - 68, 170), (c - 72, 280)], 11, 'f-lumen')
    b += _d7_tube([(c - 70, 196), (c - 112, 226)], 7, 'f-lumen')
    b += T(c - 118, 232, 'Lower: superior', 'f-h', 'end')
    for dx in (-30, -10, 10, 30):
        b += _d7_tube([(c - 72, 276), (c - 72 + dx, 312)], 5, 'f-lumen')
    b += T(c - 80, 332, 'medial, anterior, lateral,', 'f-s') + T(c - 80, 349, 'posterior basal', 'f-s')
    b += _d7_tube([(c + 50, 114), (c + 104, 84)], 10, 'f-lumen')
    b += T(c + 110, 80, 'Upper', 'f-h', 'start') + T(c + 110, 98, ['apicoposterior,', 'anterior'], 'f-s', 'start')
    b += _d7_tube([(c + 78, 100), (c + 110, 140)], 7, 'f-lumen')
    b += T(c + 116, 148, ['superior and', 'inferior lingular'], 'f-s', 'start')
    b += _d7_tube([(c + 54, 116), (c + 66, 280)], 11, 'f-lumen')
    b += _d7_tube([(c + 60, 196), (c + 104, 222)], 7, 'f-lumen')
    b += T(c + 110, 230, 'Lower: superior', 'f-h', 'start')
    for dx in (-20, 0, 20):
        b += _d7_tube([(c + 66, 276), (c + 66 + dx, 312)], 5, 'f-lumen')
    b += T(c + 80, 332, 'anteromedial, lateral,', 'f-s') + T(c + 80, 349, 'posterior basal', 'f-s')
    ix = 530
    b += f'<rect x="{ix}" y="60" width="180" height="290" rx="12" class="f-track"/>'
    b += T(ix + 90, 82, 'Within a segment', 'f-h')
    b += f'<rect x="{ix + 12}" y="98" width="74" height="176" rx="30" class="f-b0"/>'
    b += f'<rect x="{ix + 94}" y="98" width="74" height="176" rx="30" class="f-b0"/>'
    b += _d7_tube([(ix + 44, 274), (ix + 44, 130)], 9, 'f-lumen')
    b += _d7_tube([(ix + 58, 274), (ix + 58, 140)], 6, 'f-b1')
    b += _d7_tube([(ix + 90, 104), (ix + 90, 276)], 6, 'f-warn')
    b += _d7_tube([(ix + 26, 260), (ix + 26, 220), (ix + 34, 180)], 5, 'f-warn')
    b += T(ix + 90, 296, ['Bronchus and artery central;', 'intersegmental vein: keep;', 'intrasegmental vein: divide'], 'f-s')
    b += T(12, 376, 'Bronchi are the most constant; arteries run with them in the centre of the segment; veins run between segments.', 'f-s', 'start')
    b += T(12, 394, 'Segment counting for predicted function uses 19 (10 right, 9 left): see Thoracic 17.', 'f-s', 'start')
    return svg(404, b)


# ---------------------------------------------------------------- t17 pneumonectomy

def d7_stump_sides():
    """Why the right stump fails more often than the left."""
    b = T(12, 22, 'After pneumonectomy: why the right stump is more vulnerable', 'f-h', 'start')
    b += T(12, 42, "Arrangement schematic from the front, patient's right on the left.", 'f-s', 'start')
    b += '<path d="M40 70 C120 60 230 70 290 120 L280 330 L40 330 Z" class="f-dash"/>'
    b += T(130, 290, 'Empty right space', 'f-s')
    b += '<path d="M470 330 L480 150 C520 90 620 80 690 96 L690 330 Z" class="f-dash"/>'
    b += T(600, 290, 'Left space', 'f-s')
    # aorta drawn first: arch over the left main bronchus, descending behind
    b += _d7_tube(_d7_bez((330, 200), (330, 96), (400, 94)) + _d7_bez((400, 94), (452, 96), (454, 170))[1:] + [(458, 320)], 22, 'f-ok')
    b += T(414, 72, 'Aortic arch', 'f-s', 'start')
    b += _d7_tube([(370, 56), (370, 160)], 28, 'f-lumen')
    b += T(354, 66, 'Trachea', 'f-s', 'end')
    # right stump: longer, in the open space
    b += _d7_tube([(370, 158), (306, 204)], 22, 'f-lumen')
    b += _d7_cut(294, 190, 312, 216)
    b += _d7_tube(_d7_bez((318, 260), (306, 234), (316, 206)), 4, 'f-b1')
    b += T(286, 188, ['Longer stump,', 'exposed in the space'], 'f-s', 'end')
    b += T(300, 262, ['One bronchial', 'artery'], 'f-s', 'end')
    # left stump: short, retracts under the arch
    b += _d7_tube([(370, 158), (414, 184)], 20, 'f-lumen')
    b += _d7_cut(410, 172, 420, 196)
    b += _d7_tube(_d7_bez((412, 236), (406, 214), (400, 192)), 4, 'f-b1')
    b += _d7_tube(_d7_bez((430, 236), (424, 212), (412, 192)), 4, 'f-b1')
    b += T(486, 196, ['Retracts under the', 'arch, covered'], 'f-s', 'start')
    b += T(486, 250, ['Two bronchial', 'arteries'], 'f-s', 'start')
    b += box(10, 346, 345, 96, ['Right: worse. Less blood supply and cover, larger', 'lung removed, more strain on the right heart.', 'Fistula after pneumonectomy: 1 to 5% for', 'cancer, up to 10% for infection'], 'warn', 'f-s')
    b += box(365, 346, 345, 96, ['Prevention: divide flush at the carina, little', 'diathermy there, keep the blood supply, and', 'cover the stump (pleura, pericardial fat,', 'muscle). Close a right pericardial defect.'], 'ok', 'f-s')
    return svg(452, b)


def _d7_heart(cx, cy, s=1.0, cls='f-b1'):
    return (f'<path d="M{cx} {cy + 50 * s} C{cx - 70 * s} {cy + 10 * s} {cx - 60 * s} {cy - 50 * s} {cx - 10 * s} {cy - 40 * s} '
            f'C{cx + 10 * s} {cy - 60 * s} {cx + 60 * s} {cy - 40 * s} {cx + 40 * s} {cy + 10 * s} C{cx + 30 * s} {cy + 30 * s} {cx + 10 * s} {cy + 40 * s} {cx} {cy + 50 * s} Z" class="{cls}"/>')


def d7_cardiac_herniation():
    """Cardiac herniation through a pericardial defect, by side."""
    b = T(12, 22, 'Cardiac herniation after intrapericardial pneumonectomy, by side', 'f-h', 'start')
    b += T(12, 42, "Arrangement schematic from the front, patient's right on the left of each drawing.", 'f-s', 'start')
    # left panel: left defect
    for ox, side in ((10, 'L'), (365, 'R')):
        b += f'<rect x="{ox}" y="56" width="345" height="250" rx="12" class="f-track"/>'
        cx = ox + 172
        # pericardium ellipse outline with a gap
        if side == 'L':
            b += f'<path d="M{cx + 70} 120 C{cx + 40} 74 {cx - 90} 74 {cx - 100} 170 C{cx - 96} 250 {cx + 20} 266 {cx + 70} 220" class="f-l"/>'
            b += _d7_heart(cx + 50, 172, 1.0, 'f-warn')
            b += T(cx + 120, 274, ['Ventricle out through', 'the defect'], 'f-s')
            b += T(cx - 70, 252, 'Pericardium', 'f-s')
            b += T(ox + 20, 78, 'Left defect', 'f-h', 'start')
        else:
            b += f'<path d="M{cx - 70} 120 C{cx - 40} 74 {cx + 90} 74 {cx + 100} 170 C{cx + 96} 250 {cx - 20} 266 {cx - 70} 220" class="f-l"/>'
            b += _d7_heart(cx - 10, 172, 1.0, 'f-warn')
            b += f'<path d="M{cx - 80} 130 C{cx - 120} 160 {cx - 110} 210 {cx - 70} 230" class="f-l" marker-end="url(#ah)"/>'
            b += _d7_tube([(cx - 10, 60), (cx - 10, 122)], 12, 'f-b1') + _d7_tube([(cx - 10, 226), (cx - 10, 300)], 12, 'f-b1')
            b += T(cx - 30, 100, 'SVC', 'f-s', 'end') + T(cx - 30, 268, 'IVC', 'f-s', 'end')
            b += T(cx + 80, 290, 'Heart twists; cavae kink', 'f-s')
            b += T(ox + 20, 78, 'Right defect', 'f-h', 'start')
    b += box(10, 318, 345, 78, ['Strangulates the ventricle: diastole, systole', 'and coronary flow fail. Close the defect, or', 'enlarge it widely.'], 'b0', 'f-s')
    b += box(365, 318, 345, 78, ['Rotation obstructs the cavae. Always close a', 'right defect (the right-sided attachments', 'anchor the heart, so left herniation is rare).'], 'b0', 'f-s')
    b += box(10, 406, 700, 60, ['Rare; within 72 hours, often on turning; mortality 50%. Sudden collapse, raised CVP, displaced apex.',
                                'Operated side up, straight to theatre, reduce and patch; if arrested, reopen and reposition first.'], 'warn', 'f-s')
    return svg(476, b)


def d7_ppn_syndrome():
    """Post-pneumonectomy syndrome after right pneumonectomy."""
    b = T(12, 22, 'Post-pneumonectomy syndrome after right pneumonectomy', 'f-h', 'start')
    b += T(12, 42, 'Arrangement schematic. Left: front view of the shift. Right: where the left main bronchus is squeezed.', 'f-s', 'start')
    # front view
    b += '<rect x="10" y="56" width="340" height="290" rx="12" class="f-track"/>'
    b += '<path d="M30 80 C80 70 130 80 150 100 L150 330 L30 330 Z" class="f-dash"/>'
    b += T(80, 200, ['Empty', 'right', 'space'], 'f-s')
    b += _d7_tube([(210, 66), (180, 150)], 24, 'f-lumen')
    b += _d7_tube([(180, 148), (250, 220), (290, 262)], 18, 'f-lumen')
    b += T(232, 100, ['Left main', 'bronchus', 'stretched'], 'f-s', 'start')
    b += _d7_heart(170, 250, 0.9, 'f-warn')
    b += f'<path d="M232 300 C200 330 150 330 120 300" class="f-l" marker-end="url(#ah)"/>'
    b += T(262, 332, 'Rotation into the space', 'f-s')
    # squeeze diagram
    b += '<rect x="370" y="56" width="340" height="290" rx="12" class="f-track"/>'
    b += box(400, 80, 280, 44, 'Pulmonary artery (in front)', 'b1')
    b += '<ellipse cx="540" cy="166" rx="54" ry="22" class="f-b0"/>'
    b += T(540, 170, 'Left main bronchus', 'f-s')
    b += box(400, 208, 132, 50, ['Aortic arch'], 'ok') + box(548, 208, 132, 50, ['Spine'], 'b0')
    b += T(540, 196, 'or', 'f-s')
    b += arrow(540, 126, 540, 142) + arrow(500, 206, 516, 188) + arrow(600, 206, 584, 188)
    b += T(540, 284, ['Compressed between the artery and the', 'arch, or the artery and the spine'], 'f-s')
    b += box(10, 358, 345, 96, ['0.1 to 0.2%, late; commoner after right', 'pneumonectomy and in the young. Breathless,', 'stridor, recurrent pneumonia, dysphagia.', 'Venous return is not impaired.'], 'b0', 'f-s')
    b += box(365, 358, 345, 96, ['Free the stump and main bronchus from', 'the spine and posterior mediastinum,', 're-centre the mediastinum, fill the space', 'with a saline prosthesis; stent as a bridge.'], 'ok', 'f-s')
    return svg(464, b)


def _d7_cxr(ox, oy, level, shift, label, sub, prev=None):
    """Small chest film after right pneumonectomy: fluid in the right space up to `level` (0 to 1)."""
    b = f'<rect x="{ox}" y="{oy}" width="210" height="200" rx="10" class="f-b0"/>'
    top, bot = oy + 28, oy + 182
    mx = ox + 100 + shift
    b += (f'<path d="M{ox + 18} {bot} L{ox + 18} {top + 30} C{ox + 18} {top} {mx - 10} {top} {mx} {top + 8} '
          f'L{mx} {bot} Z" class="f-lumen"/>')
    fy = bot - (bot - top) * level
    b += f'<rect x="{ox + 19}" y="{fy:.0f}" width="{mx - ox - 20}" height="{bot - fy - 1:.0f}" class="f-b1"/>'
    b += line(ox + 18, round(fy), mx, round(fy), 'f-l')
    b += f'<rect x="{mx}" y="{oy + 18}" width="30" height="170" rx="10" class="f-warn"/>'
    b += (f'<path d="M{mx + 34} {bot} L{mx + 34} {top + 10} C{mx + 40} {top} {ox + 192} {top} {ox + 192} {top + 30} '
          f'L{ox + 192} {bot} Z" class="f-lumen"/>')
    if prev is not None:
        py = bot - (bot - top) * prev
        b += f'<line x1="{ox + 18}" y1="{py:.0f}" x2="{mx}" y2="{py:.0f}" class="f-dash"/>'
        b += arrow(ox + 50, round(py) + 2, ox + 50, round(fy) - 3)
    b += T(ox + 105, oy + 222, label, 'f-h') + T(ox + 105, oy + 240, sub, 'f-s')
    return b


def d7_space_film():
    """The pneumonectomy space on the chest film: expected course against a fistula."""
    b = T(12, 22, 'The right pneumonectomy space on the film', 'f-h', 'start')
    b += T(12, 42, "Schematic films, patient's right on the left. Blue: fluid. Red: mediastinum. White: air.", 'f-s', 'start')
    b += _d7_cxr(10, 56, 0.06, 0, 'Early', ['Air, little fluid;', 'drain balanced or clamped'])
    b += _d7_cxr(255, 56, 0.62, -14, 'Weeks to months', ['Fills with fluid; gentle', 'shift towards the space'])
    b += _d7_cxr(500, 56, 0.3, -14, 'Fistula', ['Air-fluid level falls (dashed:', 'before), or mediastinal shift'], prev=0.62)
    b += box(10, 348, 345, 112, ['Worked case: day 8, coughs brownish-pink fluid,', 'level 4 cm lower than yesterday: early fistula.', 'Atlas threshold: a fall of over 1.5 to 2 cm or new', 'air (not checked; TSRA says only "a drop").'], 'b0', 'f-s')
    b += box(365, 348, 345, 112, ['First minute: operated side down, head up;', 'oxygen; drain in that position; cultures and', 'antibiotics; bronchoscopy. Under 2 weeks:', 're-thoracotomy, re-close, flap. Never suction.'], 'warn', 'f-s')
    return svg(470, b)


# ---------------------------------------------------------------- t1 node map

def d7_iaslc_map():
    """IASLC node stations on a frontal schematic of the mediastinum."""
    b = T(12, 22, 'IASLC lymph node stations: where the boundaries fall', 'f-h', 'start')
    b += T(12, 42, "Arrangement schematic from the front, patient's right on the left; not an anatomical tracing.", 'f-s', 'start')
    tx = 300
    b += line(30, 80, 570, 80, 'f-grid') + T(30, 74, 'Clavicles', 'f-s', 'start')
    # aorta first (it lies behind the PA where they cross)
    b += _d7_tube(_d7_bez((tx - 16, 236), (tx + 20, 156), (tx + 90, 166)) + _d7_bez((tx + 90, 166), (tx + 150, 170), (tx + 150, 228))[1:] + [(tx + 152, 262)], 22, 'f-ok')
    # airway
    b += _d7_tube([(tx, 60), (tx, 228)], 28, 'f-lumen')
    b += _d7_tube([(tx, 226), (tx - 50, 260), (tx - 66, 320)], 20, 'f-lumen')
    b += _d7_tube([(tx - 44, 256), (tx - 104, 244)], 12, 'f-lumen')
    b += _d7_tube([(tx, 226), (tx + 70, 276), (tx + 88, 336)], 18, 'f-lumen')
    b += _d7_tube([(tx + 66, 272), (tx + 118, 252)], 12, 'f-lumen')
    # oncological midline
    # innominate vein, azygos, left PA, ligamentum
    b += _d7_tube([(tx + 130, 120), (tx - 40, 150)], 12, 'f-warn')
    b += T(tx + 140, 124, 'Innominate vein', 'f-s', 'start')
    b += _d7_tube(_d7_bez((tx - 70, 262), (tx - 62, 206), (tx - 18, 210)), 11, 'f-warn')
    b += T(tx - 82, 214, 'Azygos', 'f-s', 'end')
    b += _d7_tube([(tx + 16, 286), (tx + 90, 244), (tx + 196, 250)], 16, 'f-b1')
    b += T(tx + 202, 254, 'Left PA', 'f-s', 'start')
    b += line(tx + 94, 178, tx + 96, 238, 'f-l')
    b += T(tx + 168, 154, 'Aortic arch', 'f-s', 'start')
    b += T(tx + 202, 206, 'Ligamentum', 'f-s', 'start') + line(tx + 198, 202, tx + 100, 202, 'f-grid')
    b += _d7_cut(tx + 17, 84, tx + 17, 224)
    # oesophagus, inferior veins, diaphragm
    b += f'<rect x="{tx - 10}" y="304" width="20" height="104" rx="8" class="f-track"/>'
    b += T(tx - 16, 404, 'Oesophagus', 'f-s', 'end')
    b += _d7_tube([(tx - 150, 362), (tx - 40, 356)], 12, 'f-warn') + _d7_tube([(tx + 150, 362), (tx + 40, 356)], 12, 'f-warn')
    b += T(tx - 156, 366, 'Inferior vein', 'f-s', 'end')
    b += line(30, 414, 570, 414, 'f-l') + T(30, 430, 'Diaphragm', 'f-s', 'start')

    def st(x, y, s, cls, w=34, h=22):
        return f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="8" class="{cls}"/>' + T(x, y + 5, s, 'f-h')
    b += st(tx - 60, 62, '1R', 'f-b0') + st(tx + 60, 62, '1L', 'f-b0')
    b += st(tx - 44, 104, '2R', 'f-b1') + st(tx + 46, 106, '2L', 'f-b1')
    b += st(tx - 42, 186, '4R', 'f-b1') + st(tx + 44, 208, '4L', 'f-b1')
    b += st(tx + 120, 218, '5', 'f-warn', 26) + st(tx + 190, 186, '6', 'f-warn', 26)
    b += st(tx, 272, '7', 'f-ok', 26) + st(tx + 30, 334, '8', 'f-ok', 26)
    b += st(tx - 110, 388, '9R', 'f-ok') + st(tx + 110, 388, '9L', 'f-ok')
    b += st(tx - 96, 284, '10R', 'f-b0', 40) + st(tx + 110, 300, '10L', 'f-b0', 40)
    b += st(tx - 120, 322, '11R', 'f-b0', 40) + st(tx + 162, 300, '11L', 'f-b0', 40)
    rows = [
        ('1', 'Cricoid to clavicles; midline splits 1R, 1L'),
        ('2R', 'Down to innominate vein crossing the trachea'),
        ('2L', 'Down to the upper border of the aortic arch'),
        ('3a, 3p', 'Prevascular, retrotracheal (not drawn)'),
        ('4R', 'Down to lower border of azygos; pretracheal too'),
        ('4L', 'Medial to ligamentum, down to left PA upper rim'),
        ('5', 'Lateral to the ligamentum: subaortic, AP window'),
        ('6', 'In front of and lateral to ascending aorta, arch'),
        ('7', 'Carina to lower BI (R) or upper LLL bronchus (L)'),
        ('8', 'Para-oesophageal, below 7 to the diaphragm'),
        ('9', 'Pulmonary ligament: inferior vein to diaphragm'),
        ('10', 'Hilar: below azygos (R) or PA upper rim (L)'),
        ('11', 'Interlobar: between the lobar bronchus origins'),
        ('12-14', 'Lobar, segmental, subsegmental (not drawn)'),
    ]
    y0 = 458
    for i, (s, t) in enumerate(rows):
        x, y = 12 + (i // 7) * 355, y0 + (i % 7) * 19
        b += T(x, y, s, 'f-h', 'start') + T(x + 50, y, t, 'f-s', 'start')
    y = y0 + 7 * 19 + 6
    b += T(12, y, 'Red dashes: oncological midline, the left border of the trachea. Pretracheal nodes right of it are 4R.', 'f-s', 'start')
    b += T(12, y + 18, 'Blue: superior mediastinal. Red: aortic. Green: subcarinal and inferior. Grey: station 1 and N1 (10 to 14).', 'f-s', 'start')
    return svg(y + 30, b)


# ---------------------------------------------------------------- t2 veins

def _d7_lpanel(ox, title, sub):
    b = f'<rect x="{ox}" y="56" width="168" height="250" rx="12" class="f-track"/>'
    b += T(ox + 84, 78, title, 'f-h') + T(ox + 84, 96, sub, 'f-s')
    return b


def d7_vein_variants():
    """Pulmonary vein variants that change a lobectomy."""
    b = T(12, 22, 'Pulmonary vein variants that change the operation', 'f-h', 'start')
    b += T(12, 42, "Arrangement schematic from the front, patient's right on the left. Red: veins. Outlined: airway.", 'f-s', 'start')
    # typical
    ox = 10
    b += _d7_lpanel(ox, 'Typical', '43.5% of 550')
    cx = ox + 84
    b += f'<ellipse cx="{cx}" cy="196" rx="22" ry="34" class="f-warn"/>' + T(cx, 200, 'LA', 'f-s')
    for dy in (-18, 18):
        b += _d7_tube([(cx - 20, 196 + dy), (cx - 66, 190 + dy * 3)], 9, 'f-warn')
        b += _d7_tube([(cx + 20, 196 + dy), (cx + 66, 190 + dy * 3)], 9, 'f-warn')
    b += T(cx, 280, 'Two veins each side', 'f-s')
    # left common trunk
    ox = 186
    b += _d7_lpanel(ox, 'Left common trunk', '32.2%')
    cx = ox + 44
    b += f'<ellipse cx="{cx}" cy="196" rx="20" ry="34" class="f-warn"/>' + T(cx, 200, 'LA', 'f-s')
    b += _d7_tube([(cx + 18, 196), (cx + 60, 196)], 14, 'f-warn')
    b += _d7_tube([(cx + 58, 196), (cx + 104, 140)], 9, 'f-warn') + _d7_tube([(cx + 58, 196), (cx + 104, 252)], 9, 'f-warn')
    b += _d7_cut(cx + 40, 180, cx + 40, 212) + T(cx + 40, 236, 'not here', 'f-s')
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" class="f-duct"/>' % (cx + 74, 154, cx + 92, 170)
    b += T(cx + 54, 142, 'here', 'f-s', 'end')
    b += T(ox + 84, 280, 'Divide the lobar branch', 'f-s')
    # middle lobe vein
    ox = 362
    b += _d7_lpanel(ox, 'Middle lobe vein', 'accessory in 20.4%')
    cx = ox + 128
    b += f'<ellipse cx="{cx}" cy="196" rx="20" ry="34" class="f-warn"/>' + T(cx, 200, 'LA', 'f-s')
    b += _d7_tube([(cx - 18, 180), (cx - 104, 130)], 9, 'f-warn') + _d7_tube([(cx - 18, 214), (cx - 104, 258)], 9, 'f-warn')
    b += _d7_tube([(cx - 66, 156), (cx - 108, 196)], 6, 'f-warn')
    b += _d7_tube([(cx - 108, 200), (cx - 64, 236)], 5, 'f-warn', ' stroke-dasharray="3 2"')
    b += _d7_tube([(cx - 104, 198), (cx - 20, 198)], 5, 'f-warn', ' stroke-dasharray="3 2"')
    b += T(cx - 80, 190, 'ML', 'f-h', 'start')
    b += T(ox + 84, 280, ['Solid: joins the superior vein.', 'Dashed: inferior vein or LA'], 'f-s')
    # behind the bronchus intermedius
    ox = 538
    b += _d7_lpanel(ox, 'Behind the', 'bronchus intermedius')
    cx = ox + 84
    b += _d7_tube([(cx - 70, 136), (cx + 20, 230), (cx + 54, 244)], 7, 'f-warn', ' stroke-dasharray="4 3"')
    b += _d7_tube([(cx + 14, 110), (cx - 6, 170), (cx - 18, 256)], 20, 'f-lumen')
    b += T(cx + 22, 150, 'BI', 'f-h', 'start')
    b += T(cx, 280, ['Posterior or top-segment', 'vein: bleeds at station 7'], 'f-s')
    b += box(10, 318, 345, 78, ['Left common trunk: see the vein of the lobe that', 'stays before firing. Stapling the trunk takes all', 'left venous drainage and the lobe infarcts.'], 'warn', 'f-s')
    b += box(365, 318, 345, 78, ['Also: lingular vein to the inferior vein; anomalous', 'drainage of the lobe that stays; a short trunk', 'needing intrapericardial control.'], 'b0', 'f-s')
    return svg(406, b)


# ---------------------------------------------------------------- t16 node assessment

def d7_six_station_rule():
    """TNM 9 adequate node assessment: three worked examples."""
    b = T(12, 22, 'TNM 9 R status and the node count: three examples (right-sided resection)', 'f-h', 'start')
    b += T(12, 42, 'Illustrative station sets. Blue: station assessed. Red: positive. Margins clear in all three.', 'f-s', 'start')
    stations = ['2R', '4R', '7', '8', '9', '10R', '11R', '12R']
    rows = [
        ('A', {'2R', '4R', '7', '10R', '11R', '12R'}, set(), 'R0', 'ok',
         ['6 stations, 7 and two other', 'mediastinal; highest negative']),
        ('B', {'7', '10R', '11R', '12R'}, set(), 'R0(un)', 'b1',
         ['Limited assessment: 4', 'stations, one mediastinal']),
        ('C', {'2R', '4R', '7', '10R', '11R', '12R'}, {'2R'}, 'R0(un)', 'b1',
         ['Count met, but the highest', 'station assessed is positive']),
    ]
    x0, dx = 70, 42
    for j, s in enumerate(stations):
        b += T(x0 + j * dx, 72, s, 'f-s')
    y = 82
    for lab, done, pos, r, cls, note in rows:
        b += T(20, y + 24, lab, 'f-h', 'start')
        for j, s in enumerate(stations):
            c = 'f-warn' if s in pos else ('f-b1' if s in done else 'f-track')
            b += f'<rect x="{x0 + j * dx - 17}" y="{y + 6}" width="34" height="26" rx="7" class="{c}"/>'
        b += box(408, y + 2, 92, 34, r, cls, 'f-h')
        b += T(512, y + 15, note, 'f-s', 'start')
        y += 54
    b += line(x0 + 4.5 * dx, 60, x0 + 4.5 * dx, y - 10, 'f-dash')
    b += T(x0 + 2 * dx, y + 6, 'Mediastinal (N2)', 'f-s') + T(x0 + 6 * dx, y + 6, 'Hilar and lobar (N1)', 'f-s')
    b += box(10, y + 20, 700, 60, ['Rule: 6 stations, including 7 and at least two other mediastinal; stations, not nodes; invasive staging',
                                   'and operative stations count together. Lobe-specific dissection is no longer an alternative definition.'], 'b0', 'f-s')
    return svg(y + 90, b)




# ---- figs_D8.py
"""D8 drawings: mediastinal staging, mediastinum and thymus, thoracic inlet, trachea.
Every label comes from the notes (corpus2 t1, t5, t12) or TSRA Review ch. 5, 9, 40, 41, 42."""



# ---------------------------------------------------------------- helpers

def _d8_d8_num(x, y, n, cls='b1', r=11):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def _d8_d8_stn(x, y, lab, cls='b1'):
    """Lymph node station marker: a rounded pill with the station number."""
    w = 14 + 7 * len(lab)
    return (f'<rect x="{x - w / 2}" y="{y - 11}" width="{w}" height="22" rx="11" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{lab}</text>')


def _d8_d8_airway(ox=0):
    """Frontal view of trachea, carina and main bronchi (viewer's left = patient's right),
    with azygos vein, aortic arch, left pulmonary artery and oesophagus behind. Not to scale."""
    o = ox
    b = ''
    # oesophagus behind the trachea, slightly to the left
    b += f'<rect x="{o + 232}" y="40" width="44" height="320" rx="16" class="f-dash"/>'
    # vessels drawn first so the airway sits on top
    b += f'<path d="M{o + 96} 360 L{o + 96} 236 C{o + 96} 200 {o + 150} 196 {o + 196} 214" class="f-vessel" style="stroke-width:12"/>'
    b += f'<path d="M{o + 196} 290 L{o + 196} 175 C{o + 200} 126 {o + 300} 116 {o + 318} 168 L{o + 318} 360" class="f-vessel" style="stroke-width:20"/>'
    b += f'<path d="M{o + 250} 240 C{o + 290} 224 {o + 330} 222 {o + 372} 236" class="f-vessel" style="stroke-width:13"/>'
    b += f'<line x1="{o + 286}" y1="160" x2="{o + 290}" y2="226" class="f-dash" style="stroke-width:2.4"/>'
    # trachea and main bronchi
    pts = [(205, 46), (205, 226), (118, 290), (134, 310), (222, 254), (230, 246), (238, 254),
           (326, 310), (342, 290), (255, 226), (255, 46)]
    b += '<polygon points="' + ' '.join(f'{o + x},{y}' for x, y in pts) + '" class="f-b0"/>'
    for i in range(9):
        y = 62 + i * 19
        b += line(o + 207, y, o + 253, y, 'f-grid')
    return b


# ---------------------------------------------------------------- 1 mediastinoscopy path (t12)

def d8_mediastinoscopy_path():
    """Cervical mediastinoscopy in side view: incision, pretracheal tunnel behind the great vessels."""
    b = T(12, 22, 'Cervical mediastinoscopy: side view, front to the left', 'f-h', 'start')
    # skin of neck and chest
    b += '<path d="M72 70 C78 96 86 120 94 146" class="f-l"/>'
    # sternum
    b += '<polygon points="98,150 116,146 150,356 132,360" class="f-b1"/>'
    b += T(112, 300, 'Sternum', 'f-s', 'end')
    b += T(12, 180, 'Sternal notch', 'f-s', 'start') + line(70, 170, 96, 152, 'f-grid')
    # incision
    b += '<line x1="78" y1="110" x2="96" y2="100" class="f-cut" style="stroke-width:4"/>'
    b += T(12, 44, ['3 cm incision,', '2 cm above the notch'], 'f-s', 'start')
    # spine
    for i in range(7):
        b += f'<rect x="392" y="{42 + i * 44}" width="40" height="36" rx="7" class="f-track"/>'
        b += f'<rect x="392" y="{42 + i * 44}" width="40" height="36" rx="7" class="f-dash"/>'
    b += T(414, 370, 'Spine', 'f-s')
    # oesophagus behind trachea
    b += '<polygon points="288,40 318,40 356,350 326,350" class="f-track"/>'
    b += '<polygon points="288,40 318,40 356,350 326,350" class="f-dash"/>'
    b += T(334, 370, 'Oesophagus', 'f-s')
    # trachea
    b += '<polygon points="222,40 264,40 300,296 258,296" class="f-b0"/>'
    for i in range(11):
        y = 58 + i * 22
        x0 = 222 + (y - 40) * 36 / 256
        b += line(x0 + 2, y, x0 + 40, y, 'f-grid')
    b += '<ellipse cx="282" cy="304" rx="26" ry="11" class="f-b0"/>'
    b += T(282, 330, 'Carina', 'f-s')
    b += T(250, 34, 'Trachea', 'f-s')
    # great vessels in front of the trachea
    b += '<circle cx="186" cy="138" r="17" class="f-warn"/>'
    b += T(186, 174, ['Innominate', 'artery'], 'f-s')
    b += '<ellipse cx="200" cy="224" rx="27" ry="22" class="f-warn"/>'
    b += T(196, 264, 'Aortic arch', 'f-s')
    # scope path: neck incision, then down the front of the trachea, behind the vessels
    b += '<path d="M90 106 L222 98 L254 270" class="f-l" style="stroke-width:6;stroke-linecap:round;opacity:.45"/>'
    b += '<path d="M90 106 L222 98 L254 270" class="f-dash"/>'
    b += arrow(246, 226, 253, 266)
    # stations reached
    b += _d8_d8_stn(246, 128, '2') + _d8_d8_stn(262, 206, '4') + _d8_d8_stn(286, 278, '7')
    # steps
    steps = [('1', ['Neck extended; 3 cm incision', '2 cm above the notch']),
             ('2', ['Open the pretracheal fascia']),
             ('3', ['Finger tunnel on the front of the', 'trachea to the carina, behind', 'the great vessels']),
             ('4', ['Scope in with a slow rotating', 'motion; use it for counter-traction']),
             ('5', ['Dissect nodes free before', 'grasping: stations 2, 4, 7, 10']),
             ('6', ['Little diathermy on the left', '(recurrent laryngeal nerve)'])]
    y = 44
    for n, ls in steps:
        b += _d8_d8_num(468, y + 6, n)
        b += T(486, y + 11, ls, 'f-s', 'start')
        y += 17 * len(ls) + 14
    b += box(10, 382, 700, 40, 'Morbidity 1.5 to 3%, mortality under 0.1%: bleeding, air embolism, nerve injury (TSRA ch. 3)', 'b0', 'f-s')
    return svg(432, b)


# ---------------------------------------------------------------- 2 mediastinoscopy hazards (t5)

def d8_mediastinoscopy_hazards():
    """Frontal map of mediastinoscopy stations and where each complication arises."""
    b = T(12, 22, "Where mediastinoscopy goes wrong: front view, patient's right on the left", 'f-h', 'start')
    b += _d8_d8_airway(0)
    # right pulmonary artery passing under the carina towards the right hilum
    b += '<path d="M300 268 C250 282 190 282 128 266" class="f-vessel" style="stroke-width:12"/>'
    # left recurrent laryngeal nerve: down with the vagus, under the arch, up the left side of the trachea
    b += '<path d="M330 48 C334 120 330 190 318 236 C306 262 282 252 276 226 L262 48" class="f-nerve"/>'
    # stations
    b += _d8_d8_stn(186, 92, '2R') + _d8_d8_stn(276, 92, '2L')
    b += _d8_d8_stn(182, 178, '4R') + _d8_d8_stn(272, 196, '4L') + _d8_d8_stn(230, 282, '7')
    # labels on the drawing
    b += T(62, 352, 'Azygos', 'f-s', 'start')
    b += T(330, 112, 'Aortic arch', 'f-s', 'start')
    b += T(384, 250, ['Left pulmonary', 'artery'], 'f-s', 'start')
    b += T(92, 300, ['Right pulmonary', 'artery'], 'f-s', 'end')
    b += T(282, 372, 'Oesophagus (dashed, behind)', 'f-s')
    b += T(338, 46, 'Left recurrent nerve', 'f-s', 'start')
    # hazard numbers on the drawing
    b += _d8_d8_num(150, 206, 1, 'warn') + _d8_d8_num(204, 300, 2, 'warn') + _d8_d8_num(258, 318, 3, 'warn') + _d8_d8_num(300, 214, 4, 'warn')
    # legend
    leg = [(1, '4R: azygos vein', ['Commonest site of major bleeding']),
           (2, '7: right pulmonary artery', ['and right bronchial artery']),
           (3, '7: oesophagus', ['Perforation near station 7']),
           (4, '4L: left recurrent nerve', ['Use cautery sparingly on the left'])]
    y = 46
    for n, h, ls in leg:
        b += _d8_d8_num(468, y + 6, n, 'warn')
        b += T(486, y + 11, h, 'f-h', 'start') + T(486, y + 29, ls, 'f-s', 'start')
        y += 58
    b += box(456, 284, 254, 92, ['Major bleeding 0.1 to 0.6%:', 'pack, haemostatic agents and', 'patience; sternotomy if that fails'], 'b1', 'f-s')
    b += box(10, 392, 700, 44, ['Relative contraindications: innominate or arch aneurysm, previous sternotomy, neck surgery or',
                                'radiotherapy. A calcified innominate artery may raise the risk of stroke.'], 'b0', 'f-s')
    return svg(446, b)


# ---------------------------------------------------------------- 3 endosonography reach (t1)

def d8_endosonography_reach():
    """Which stations EBUS and EUS reach, drawn on a frontal airway and oesophagus (ESTS 2014)."""
    b = T(12, 22, "EBUS and EUS reach: front view, patient's right on the left", 'f-h', 'start')
    b += _d8_d8_airway(0)
    E, U, BO, N = 'b1', 'b0', 'ok', 'warn'
    b += _d8_d8_stn(186, 92, '2R', E) + _d8_d8_stn(276, 92, '2L', E)
    b += _d8_d8_stn(182, 178, '4R', E) + _d8_d8_stn(272, 196, '4L', BO)
    b += _d8_d8_stn(230, 282, '7', BO)
    b += _d8_d8_stn(136, 246, '10R', E) + _d8_d8_stn(318, 262, '10L', E)
    b += _d8_d8_stn(104, 318, '11R', E) + _d8_d8_stn(356, 318, '11L', E)
    b += _d8_d8_stn(254, 336, '8', U) + _d8_d8_stn(254, 376, '9', U)
    b += _d8_d8_stn(256, 136, '6', N) + _d8_d8_stn(350, 196, '5', N)
    # EUS-only markers get a dashed ring so they read without colour
    b += '<rect x="235" y="323" width="38" height="26" rx="13" class="f-dash"/><rect x="235" y="363" width="38" height="26" rx="13" class="f-dash"/>'
    # landmarks
    b += line(255, 40, 255, 30, 'f-grid')
    b += T(12, 150, ['4R becomes 10R at', 'the lower border', 'of the azygos'], 'f-s', 'start')
    b += T(300, 394, ['4L becomes 10L at the', 'upper rim of the left PA'], 'f-s', 'start')
    b += T(30, 400, ['Oesophagus behind', '(dashed)'], 'f-s', 'start')
    # legend
    lx = 470
    leg = [(E, 'EBUS', ['2R, 2L, 4R, 4L, 7, 10, 11, even 12']),
           (BO, 'EBUS and EUS', ['4L and 7']),
           (U, 'EUS only', ['8 and 9: not reached by EBUS or', 'mediastinoscopy, so EUS adds them']),
           (N, 'Neither, routinely', ['5 and 6: EUS not recommended'])]
    y = 46
    for cls, h, s in leg:
        b += f'<rect x="{lx}" y="{y}" width="30" height="20" rx="10" class="f-{cls}"/>'
        if cls == U:
            b += f'<rect x="{lx - 3}" y="{y - 3}" width="36" height="26" rx="13" class="f-dash"/>'
        b += T(lx + 42, y + 15, h, 'f-h', 'start') + T(lx + 42, y + 33, s, 'f-s', 'start')
        y += 40 + 17 * len(s)
    b += box(lx - 6, 314, 246, 108, ['Always seek and describe 4R,', '4L and 7; 3 aspirations per', 'station; nodes over 5 mm.',
                                     'One needle: sample N3, then', 'N2, then N1'], 'b1', 'f-s')
    return svg(440, b)


# ---------------------------------------------------------------- 4 stations 5 and 6 (t1)

def d8_station56_routes():
    """Three routes to the aortopulmonary (5) and para-aortic (6) nodes."""
    b = T(12, 22, "Reaching stations 5 and 6: front view, patient's left on the right", 'f-h', 'start')
    cx = 220
    # chest outline
    b += (f'<path d="M{cx - 40} 52 L{cx - 150} 74 L{cx - 160} 190 L{cx - 148} 380 L{cx + 148} 380 '
          f'L{cx + 160} 190 L{cx + 150} 74 L{cx + 40} 52 Z" class="f-track"/>')
    b += (f'<path d="M{cx - 40} 52 L{cx - 150} 74 L{cx - 160} 190 L{cx - 148} 380 L{cx + 148} 380 '
          f'L{cx + 160} 190 L{cx + 150} 74 L{cx + 40} 52 Z" class="f-l"/>')
    # ribs on the patient's left
    for i, y in enumerate([96, 140, 184, 228]):
        b += f'<path d="M{cx + 18} {y} C{cx + 70} {y + 4} {cx + 120} {y + 14} {cx + 152} {y + 30}" class="f-grid" fill="none"/>'
        b += T(cx + 164, y + 34, f'{i + 1}', 'f-s', 'start')
    # sternum
    b += f'<rect x="{cx - 18}" y="64" width="36" height="210" rx="8" class="f-b0"/>'
    # arch, left pulmonary artery, ligamentum
    b += f'<path d="M{cx - 30} 300 L{cx - 30} 190 C{cx - 26} 140 {cx + 70} 132 {cx + 84} 186 L{cx + 84} 372" class="f-vessel" style="stroke-width:22"/>'
    b += f'<path d="M{cx + 20} 262 C{cx + 60} 244 {cx + 110} 242 {cx + 138} 254" class="f-vessel" style="stroke-width:14"/>'
    b += f'<line x1="{cx + 56}" y1="178" x2="{cx + 60}" y2="246" class="f-dash" style="stroke-width:2.4"/>'
    # phrenic nerve and internal mammary artery
    b += f'<path d="M{cx + 104} 60 C{cx + 126} 140 {cx + 130} 250 {cx + 126} 372" class="f-nerve"/>'
    b += f'<line x1="{cx + 30}" y1="64" x2="{cx + 30}" y2="300" class="f-vessel" style="stroke-width:5"/>'
    # stations
    b += _d8_d8_stn(cx + 40, 120, '6', 'warn') + _d8_d8_stn(cx + 88, 222, '5', 'warn')
    # routes
    b += f'<line x1="{cx + 20}" y1="164" x2="{cx + 66}" y2="164" class="f-cut" style="stroke-width:4"/>'
    b += _d8_d8_num(cx + 2, 182, 'A', 'warn')
    for px, py in [(cx + 144, 236), (cx + 150, 280), (cx + 140, 324)]:
        b += f'<circle cx="{px}" cy="{py}" r="6" class="f-b1"/>'
    b += _d8_d8_num(cx + 118, 300, 'B', 'b1')
    b += f'<line x1="{cx - 16}" y1="44" x2="{cx + 16}" y2="44" class="f-cut" style="stroke-width:4"/>'
    b += f'<path d="M{cx + 6} 48 C{cx + 20} 70 {cx + 34} 86 {cx + 38} 102" class="f-dash" style="stroke-width:2"/>'
    b += arrow(cx + 37, 98, cx + 39, 106)
    b += _d8_d8_num(cx - 30, 40, 'C', 'ok')
    # small labels
    b += T(cx - 44, 236, 'Arch', 'f-s', 'end')
    b += T(cx + 60, 330, 'Left PA', 'f-s') + line(cx + 60, 318, cx + 72, 254, 'f-grid')
    b += T(cx + 2, 316, ['Internal', 'mammary'], 'f-s', 'end')
    b += T(cx + 112, 52, 'Phrenic', 'f-s', 'start')
    b += T(cx - 52, 128, ['Ligamentum', '(dashed); 5 lies', 'lateral to it'], 'f-s', 'end')
    # legend
    lx = 410
    rows = [('A', 'warn', 'Left anterior mediastinotomy', ['Parasternal, 2nd or 3rd space, as medial', 'as possible; stay extrapleural; internal', 'mammary and phrenic at risk']),
            ('B', 'b1', 'Left VATS', ['Double-lumen tube; limited by', 'adhesions; one side only; also 5 to 9']),
            ('C', 'ok', 'Extended cervical mediastinoscopy', ['Same incision as standard; NPV 0.89', 'to 0.97 in experienced centres'])]
    y = 46
    for n, cls, h, ls in rows:
        b += _d8_d8_num(lx + 10, y + 6, n, cls)
        b += T(lx + 28, y + 11, h, 'f-h', 'start') + T(lx + 28, y + 29, ls, 'f-s', 'start')
        y += 36 + 17 * len(ls)
    b += box(lx, 306, 300, 74, ['Routine mediastinoscopy and E(B)US', 'cannot reach 5 and 6. Sample them for', 'a left upper lobe tumour if it changes strategy'], 'b0', 'f-s')
    return svg(392, b)


# ---------------------------------------------------------------- 5 compartments, axial (t5)

def d8_compartments_axial():
    """Three-compartment model on a cross-section (TSRA ch. 42 boundaries)."""
    b = T(12, 22, 'Mediastinal compartments in cross-section (seen from below, front at the top)', 'f-h', 'start')
    cx, cy = 376, 196
    b += f'<ellipse cx="{cx}" cy="{cy}" rx="194" ry="146" class="f-b0"/>'
    # lungs
    b += f'<ellipse cx="{cx - 116}" cy="{cy}" rx="64" ry="108" class="f-track"/><ellipse cx="{cx - 116}" cy="{cy}" rx="64" ry="108" class="f-dash"/>'
    b += f'<ellipse cx="{cx + 116}" cy="{cy}" rx="64" ry="108" class="f-track"/><ellipse cx="{cx + 116}" cy="{cy}" rx="64" ry="108" class="f-dash"/>'
    b += T(cx - 116, cy + 4, 'Lung', 'f-s') + T(cx + 116, cy + 4, 'Lung', 'f-s')
    # sternum and spine
    b += f'<rect x="{cx - 30}" y="54" width="60" height="16" rx="6" class="f-b1"/>'
    b += f'<circle cx="{cx}" cy="300" r="26" class="f-b1"/><rect x="{cx - 6}" y="324" width="12" height="18" rx="4" class="f-b1"/>'
    # anterior compartment
    b += f'<path d="M{cx - 40} 74 Q{cx} 66 {cx + 40} 74 L{cx + 30} 112 Q{cx} 104 {cx - 30} 112 Z" class="f-warn"/>'
    # middle compartment outline
    b += f'<path d="M{cx - 44} 118 Q{cx} 104 {cx + 44} 118 L{cx + 48} 272 Q{cx} 262 {cx - 48} 272 Z" class="f-dash" style="stroke-width:2"/>'
    b += f'<ellipse cx="{cx}" cy="156" rx="40" ry="30" class="f-b0"/>'
    b += T(cx, 154, 'Heart,', 'f-s') + T(cx, 168, 'vessels', 'f-s')
    b += f'<circle cx="{cx - 12}" cy="214" r="12" class="f-lumen"/><circle cx="{cx + 12}" cy="246" r="9" class="f-lumen"/>'
    b += f'<circle cx="{cx + 30}" cy="222" r="11" class="f-b0"/>'
    # posterior compartments (paravertebral gutters)
    b += f'<ellipse cx="{cx - 40}" cy="302" rx="13" ry="24" class="f-ok"/><ellipse cx="{cx + 40}" cy="302" rx="13" ry="24" class="f-ok"/>'
    # labels left
    b += T(12, 60, 'Anterior', 'f-h', 'start')
    b += T(12, 78, ['Sternum to the front of', 'the great vessels and', 'pericardium. Thymus,', 'nodes, internal', 'mammary vessels'], 'f-s', 'start')
    b += line(140, 64, cx - 36, 90, 'f-grid')
    b += T(12, 204, 'Middle (visceral)', 'f-h', 'start')
    b += T(12, 222, ['Back to the front of', 'the spine. Heart, great', 'vessels, trachea,', 'oesophagus, vagus', 'and phrenic nerves'], 'f-s', 'start')
    b += line(130, 200, cx - 46, 196, 'f-grid')
    b += T(580, 262, 'Posterior', 'f-h', 'start')
    b += T(580, 280, ['(paravertebral)', 'Potential space along', 'the spine: sympathetic', 'chain, intercostal', 'bundles'], 'f-s', 'start')
    b += line(576, 270, cx + 54, 298, 'f-grid')
    b += T(580, 190, ['Small circles:', 'trachea, oesophagus,', 'aorta'], 'f-s', 'start')
    b += T(cx, 46, 'Sternum', 'f-s')
    b += box(10, 360, 700, 40, 'Anterior: thymoma, teratoma, lymphoma, thyroid · Middle: nodes, cysts · Posterior: neurogenic tumours', 'b0', 'f-s')
    return svg(410, b)


# ---------------------------------------------------------------- 6 ITMIG thymic nodal map (t5)

def d8_thymic_nodes():
    """ITMIG nodal regions for thymic tumours: anterior (N1) and deep (N2)."""
    b = T(12, 22, 'Thymic tumour nodes: ITMIG anterior (N1) and deep (N2) regions', 'f-h', 'start')
    b += '<rect x="10" y="36" width="700" height="250" rx="16" class="f-b0"/>'
    b += '<rect x="170" y="80" width="380" height="164" rx="14" class="f-b1"/>'
    b += '<rect x="305" y="132" width="110" height="60" rx="12" class="f-warn"/>'
    b += T(360, 160, 'Thymus', 'f-h') + T(360, 178, 'and tumour', 'f-s')
    b += T(360, 100, 'Anterior (perithymic) region: N1', 'f-h')
    b += T(182, 140, ['Prevascular', 'Para-aortic', 'Ascending aortic'], 'f-s', 'start')
    b += T(540, 140, ['Superior and', 'inferior phrenic', 'Supradiaphragmatic'], 'f-s', 'end')
    b += T(360, 216, 'Low anterior cervical', 'f-s')
    b += T(360, 56, 'Deep region: N2', 'f-h')
    b += T(22, 100, ['Internal mammary', 'Lower jugular', 'Supraclavicular'], 'f-s', 'start')
    b += T(698, 100, ['Upper and lower', 'paratracheal', 'Subaortic'], 'f-s', 'end')
    b += T(22, 230, ['Subcarinal'], 'f-s', 'start')
    b += T(698, 230, ['Hilar'], 'f-s', 'end')
    b += T(360, 270, 'IASLC levels: N1 = 1, 3a, 6, pericardial · N2 = 2, 4, 5, 7, 10, internal mammary', 'f-s')
    b += box(10, 298, 345, 76, ['Thymoma: remove anterior mediastinal', 'and anterior cervical nodes routinely;', 'sample deep nodes in stage III and IV'], 'ok', 'f-s')
    b += box(365, 298, 345, 76, ['Thymic carcinoma: N1 plus N2', 'lymphadenectomy strongly advised;', 'nodal spread 20% against 3% in thymoma'], 'warn', 'f-s')
    return svg(384, b)


# ---------------------------------------------------------------- 7 thymectomy extent (t5)

def d8_thymectomy_extent():
    """Extent of thymectomy: phrenic to phrenic, thyroid to diaphragm, with ectopic sites."""
    b = T(12, 22, 'What a complete thymectomy removes (front view)', 'f-h', 'start')
    cx = 230
    # pericardium and heart behind
    b += f'<ellipse cx="{cx}" cy="270" rx="120" ry="76" class="f-track"/><ellipse cx="{cx}" cy="270" rx="120" ry="76" class="f-dash"/>'
    b += T(cx, 334, 'Pericardium', 'f-s')
    # resection field
    b += f'<rect x="{cx - 128}" y="58" width="256" height="304" rx="14" class="f-dash" style="stroke-width:2"/>'
    # phrenic nerves
    b += f'<path d="M{cx - 128} 52 C{cx - 134} 150 {cx - 138} 260 {cx - 132} 366" class="f-nerve"/>'
    b += f'<path d="M{cx + 128} 52 C{cx + 134} 150 {cx + 138} 260 {cx + 132} 366" class="f-nerve"/>'
    # thyroid
    b += f'<ellipse cx="{cx - 26}" cy="56" rx="22" ry="13" class="f-b0"/><ellipse cx="{cx + 26}" cy="56" rx="22" ry="13" class="f-b0"/>'
    b += f'<rect x="{cx - 8}" y="52" width="16" height="10" class="f-b0"/>'
    b += T(cx + 56, 50, 'Thyroid', 'f-s', 'start')
    # innominate vein
    b += f'<path d="M{cx + 104} 112 L{cx - 104} 146" class="f-vessel" style="stroke-width:12"/>'
    b += T(cx - 118, 172, ['Innominate', 'vein'], 'f-s', 'start')
    # thymus: two upper poles and two lobes
    b += f'<path d="M{cx - 16} 80 C{cx - 22} 110 {cx - 28} 140 {cx - 40} 170 C{cx - 74} 210 {cx - 70} 290 {cx - 20} 296 C{cx} 270 {cx} 200 {cx - 6} 160 C{cx - 8} 130 {cx - 8} 100 {cx - 16} 80 Z" class="f-b1"/>'
    b += f'<path d="M{cx + 16} 80 C{cx + 22} 110 {cx + 28} 140 {cx + 40} 170 C{cx + 74} 210 {cx + 70} 290 {cx + 20} 296 C{cx} 270 {cx} 200 {cx + 6} 160 C{cx + 8} 130 {cx + 8} 100 {cx + 16} 80 Z" class="f-b1"/>'
    b += T(cx, 236, 'Thymus', 'f-h')
    # diaphragm
    b += f'<path d="M{cx - 170} 384 C{cx - 80} 352 {cx + 80} 352 {cx + 170} 384" class="f-l"/>'
    b += T(cx - 170, 400, 'Diaphragm', 'f-s', 'start')
    b += T(cx - 150, 46, 'Phrenic', 'f-s', 'middle') + T(cx + 150, 46, 'Phrenic', 'f-s', 'middle')
    # ectopic thymus
    b += _d8_d8_num(cx + 30, 134, 1, 'warn', 9) + _d8_d8_num(cx + 100, 176, 2, 'warn', 9)
    b += _d8_d8_num(cx - 112, 336, 3, 'warn', 9) + _d8_d8_num(cx + 112, 336, 3, 'warn', 9)
    # legend
    lx = 420
    b += T(lx, 56, 'Limits of the dissection', 'f-h', 'start')
    b += T(lx, 76, ['All thymic tissue and anterior', 'mediastinal fat: phrenic to phrenic,', 'thyroid to diaphragm, both upper poles'], 'f-s', 'start')
    b += T(lx, 146, 'Ectopic thymus', 'f-h', 'start')
    for i, s in enumerate(['Behind the innominate vein', 'Aortopulmonary window', 'Cardiophrenic angles']):
        b += _d8_d8_num(lx + 10, 166 + i * 26, i + 1, 'warn', 9) + T(lx + 26, 171 + i * 26, s, 'f-s', 'start')
    b += box(lx - 6, 254, 296, 112, ['With a thymoma: en bloc, capsule', 'unbreached; take adherent pericardium,', 'lung or one phrenic nerve as needed.',
                                     'Never both phrenic nerves; think hard', 'about one if myasthenic'], 'warn', 'f-s')
    return svg(410, b)


# ---------------------------------------------------------------- 8 thymectomy approaches (t5)

def d8_thymectomy_approaches():
    """Thymectomy approaches marked on the chest, with the stage rule from ESMO 2015."""
    b = T(12, 22, 'Thymectomy: approaches and when each is used', 'f-h', 'start')
    cx = 150
    b += (f'<path d="M{cx - 34} 40 L{cx - 34} 62 L{cx - 112} 82 L{cx - 120} 190 L{cx - 108} 340 L{cx + 108} 340 '
          f'L{cx + 120} 190 L{cx + 112} 82 L{cx + 34} 62 L{cx + 34} 40 Z" class="f-b0"/>')
    b += f'<circle cx="{cx - 58}" cy="168" r="4" class="f-b1"/><circle cx="{cx + 58}" cy="168" r="4" class="f-b1"/>'
    # collar incision
    b += f'<path d="M{cx - 26} 54 Q{cx} 62 {cx + 26} 54" class="f-cut" style="stroke-width:4"/>'
    b += _d8_d8_num(cx - 46, 46, 1, 'ok')
    # sternotomy
    b += f'<line x1="{cx}" y1="70" x2="{cx}" y2="234" class="f-cut" style="stroke-width:4"/>'
    b += _d8_d8_num(cx + 16, 110, 2, 'warn')
    # subxiphoid
    b += f'<line x1="{cx}" y1="248" x2="{cx}" y2="284" class="f-cut" style="stroke-width:4"/>'
    b += _d8_d8_num(cx + 16, 270, 3, 'ok')
    # lateral ports, either side
    for s in (-1, 1):
        for dy in (0, 40, 80):
            b += f'<circle cx="{cx + s * (94 - dy / 8)}" cy="{196 + dy}" r="5" class="f-b1"/>'
    b += _d8_d8_num(cx - 104, 304, 4, 'ok') + _d8_d8_num(cx + 104, 304, 4, 'ok')
    # hemiclamshell on patient's left (viewer's right)
    b += f'<path d="M{cx + 3} 140 C{cx + 40} 152 {cx + 80} 156 {cx + 110} 146" class="f-cut" style="stroke-width:3" stroke-dasharray="6 4"/>'
    b += _d8_d8_num(cx + 70, 136, 5, 'b1')
    b += T(cx, 360, "Patient's right on the left", 'f-s')
    lx = 300
    rows = [(1, 'ok', 'Transcervical (and extended)', 'Collar incision, sternum lifted; masses under 4 cm'),
            (2, 'warn', 'Median sternotomy (transsternal)', 'ESMO standard; large or invasive; MGTX arm'),
            (3, 'ok', 'Subxiphoid', 'Alone or combined with ports'),
            (4, 'ok', 'VATS or robotic', 'Unilateral, bilateral, cervical or subxiphoid mixes'),
            (5, 'b1', 'Hemi-clamshell', 'Upper sternal split and anterior thoracotomy;'),
            ]
    y = 44
    for n, cls, h, s in rows:
        b += _d8_d8_num(lx + 10, y + 6, n, cls)
        b += T(lx + 28, y + 11, h, 'f-h', 'start') + T(lx + 28, y + 28, s, 'f-s', 'start')
        y += 44
    b += T(lx + 28, y - 1, 'large thymomas with lateral extension', 'f-s', 'start')
    b += box(lx, 276, 200, 74, ['Presumed stage I,', 'possibly II: minimally', 'invasive by trained hands'], 'ok', 'f-s')
    b += box(lx + 210, 276, 200, 74, ['Stage III: not minimally', 'invasive (no long-term', 'data). Convert if needed'], 'warn', 'f-s')
    b += T(360, 374, 'Port positions are schematic; the sources name the combinations, not the sites.', 'f-s')
    return svg(384, b)


# ---------------------------------------------------------------- 9 inlet and anterior approaches (t5)

def _d8_d8_mini_torso(cx, top=56):
    return (f'<path d="M{cx - 22} {top - 24} L{cx - 22} {top} L{cx - 72} {top + 14} L{cx - 78} {top + 110} '
            f'L{cx - 70} {top + 210} L{cx + 70} {top + 210} L{cx + 78} {top + 110} L{cx + 72} {top + 14} '
            f'L{cx + 22} {top} L{cx + 22} {top - 24} Z" class="f-b0"/>'
            f'<line x1="{cx - 64}" y1="{top + 22}" x2="{cx - 10}" y2="{top + 26}" class="f-grid"/>'
            f'<line x1="{cx + 64}" y1="{top + 22}" x2="{cx + 10}" y2="{top + 26}" class="f-grid"/>'
            f'<rect x="{cx - 8}" y="{top + 16}" width="16" height="120" rx="5" class="f-grid" fill="none"/>')


def d8_inlet_approaches():
    """Dartevelle, Masaoka, hemi-clamshell and clamshell incisions (TSRA ch. 42)."""
    b = T(12, 22, "Anterior approaches to the inlet and large masses (patient's left on the right)", 'f-h', 'start')
    st = 'style="stroke-width:4"'
    xs = [92, 270, 450, 628]
    for x in xs:
        b += _d8_d8_mini_torso(x)
    # Dartevelle: anterior border of SCM down to manubrium, then laterally below the clavicle
    x = xs[0]
    b += f'<path d="M{x + 18} 36 L{x + 6} 84 L{x + 66} 94" class="f-cut" {st}/>'
    # Masaoka: left supraclavicular, upper partial sternotomy, left anterolateral thoracotomy (4th space)
    x = xs[1]
    b += f'<path d="M{x + 16} 70 L{x + 50} 72" class="f-cut" {st}/>'
    b += f'<path d="M{x} 74 L{x} 150" class="f-cut" {st}/>'
    b += f'<path d="M{x} 150 C{x + 30} 160 {x + 56} 162 {x + 76} 152" class="f-cut" {st}/>'
    # hemi-clamshell: upper sternal split and anterior thoracotomy, 4th space
    x = xs[2]
    b += f'<path d="M{x} 70 L{x} 150 C{x + 30} 160 {x + 56} 162 {x + 76} 152" class="f-cut" {st}/>'
    # clamshell: bilateral 4th space inframammary incision with transverse sternotomy
    x = xs[3]
    b += f'<path d="M{x - 76} 150 C{x - 50} 168 {x - 20} 166 {x} 158 C{x + 20} 166 {x + 50} 168 {x + 76} 150" class="f-cut" {st}/>'
    heads = [('Dartevelle', 'anterior cervicothoracic'), ('Masaoka', 'trans-sternal'), ('Hemi-clamshell', 'unilateral'), ('Clamshell', 'bilateral')]
    descs = [['L-shaped: along the', 'sternomastoid to the', 'manubrium, then out', 'below the clavicle;', 'muscle reflected as', 'a myocutaneous flap'],
             ['Left supraclavicular', 'incision, upper partial', 'sternotomy and left', 'anterolateral', 'thoracotomy (4th space)'],
             ['Partial upper sternal', 'split and anterior', 'thoracotomy, usually', 'the 4th space'],
             ['4th space inframammary', 'incision, transverse', 'sternotomy; tie the', 'internal mammaries;', 'divide lateral intercostal', 'fibres, not ribs']]
    uses = [['Superior sulcus tumour', 'invading the inlet'], ['Sulcus tumour with', 'vascular involvement'],
            ['Anterior Pancoast,', 'large lateral thymoma,', 'proximal plexus tumour'], ['Large mass with pleural', 'extension; trauma;', 'bilateral transplant']]
    for i, x in enumerate(xs):
        b += T(x, 290, heads[i][0], 'f-h') + T(x, 307, heads[i][1], 'f-s')
        b += T(x, 330, descs[i], 'f-s')
        b += box(x - 86, 444, 172, 64, uses[i], 'b1', 'f-s')
    return svg(518, b)


# ---------------------------------------------------------------- 10 superior sulcus (t1)

def d8_pancoast_inlet():
    """Thoracic inlet compartments, which approach suits which, and the nerve-root rule."""
    b = T(12, 22, 'Superior sulcus tumour: inlet compartments and the approach', 'f-h', 'start')
    rows = [('Anterior', ['Platysma, sternocleidomastoid,', 'subclavian vein'], 'b1'),
            ('Middle', ['Phrenic nerve, anterior scalene, subclavian artery,', 'brachial plexus, middle and posterior scalene'], 'warn'),
            ('Posterior', ['Sympathetic ganglia, long thoracic nerve, subscapular', 'artery, external branch of the spinal accessory'], 'b0')]
    y = 44
    for name, ls, cls in rows:
        b += f'<rect x="170" y="{y}" width="380" height="64" rx="10" class="f-{cls}"/>'
        b += T(182, y + 22, name, 'f-h', 'start') + T(182, y + 40, ls, 'f-s', 'start')
        y += 72
    b += T(360, 38, 'Front of the inlet', 'f-s') + T(360, 274, 'Back of the inlet, vertebral bodies', 'f-s')
    b += arrow(150, 76, 166, 76) + T(144, 66, 'Anterior', 'f-h', 'end') + T(144, 84, ['(Dartevelle):', 'anterior tumours,', 'vessels or plexus'], 'f-s', 'end')
    b += arrow(150, 220, 166, 220) + T(144, 210, 'Posterior', 'f-h', 'end') + T(144, 228, ['(Shaw-Paulson):', 'vertebral body,', 'posterior centre'], 'f-s', 'end')
    b += T(562, 60, 'What may be taken', 'f-h', 'start')
    b += T(562, 80, ['Subclavian vein:', 'resect and ligate', 'Subclavian artery:', 'resect and reconstruct', 'Phrenic: preserve', 'if possible'], 'f-s', 'start')
    # nerve roots
    b += T(12, 306, 'Lower plexus roots', 'f-h', 'start')
    b += box(10, 316, 230, 56, ['T1 root: well tolerated,', 'mild hand weakness'], 'ok', 'f-s')
    b += box(250, 316, 230, 56, ['C8 root: Klumpke paralysis', 'of hand and forearm, poorly tolerated'], 'warn', 'f-s')
    b += box(490, 316, 220, 56, ['Cord or extensive plexus', 'involvement: do not resect'], 'warn', 'f-s')
    b += box(10, 384, 700, 40, ['Induction chemoradiation, then en bloc R0 resection. MRI first; plexus above T1, over half a vertebral body,', 'or N2 or N3 disease argue against resection.'], 'b0', 'f-s')
    return svg(434, b)


# ---------------------------------------------------------------- 11 tracheal releases (t12)

def d8_tracheal_releases():
    """The five release manoeuvres in their order, placed on the airway."""
    b = T(12, 22, 'Release manoeuvres for a tension-free tracheal anastomosis', 'f-h', 'start')
    cx = 200
    # hyoid, thyroid cartilage, cricoid
    b += f'<rect x="{cx - 46}" y="52" width="92" height="12" rx="6" class="f-b1"/>'
    b += T(cx + 56, 62, 'Hyoid', 'f-s', 'start')
    b += f'<line x1="{cx - 56}" y1="44" x2="{cx + 56}" y2="44" class="f-cut" style="stroke-width:3"/>'
    b += f'<path d="M{cx - 34} 78 L{cx + 34} 78 L{cx + 26} 122 L{cx} 132 L{cx - 26} 122 Z" class="f-b0"/>'
    b += T(cx + 44, 104, 'Larynx', 'f-s', 'start')
    b += f'<rect x="{cx - 24}" y="136" width="48" height="14" rx="5" class="f-b1"/>'
    b += T(cx + 32, 148, 'Cricoid', 'f-s', 'start')
    # trachea with the resected segment
    b += f'<rect x="{cx - 22}" y="154" width="44" height="170" rx="8" class="f-b0"/>'
    for i in range(9):
        b += line(cx - 20, 166 + i * 18, cx + 20, 166 + i * 18, 'f-grid')
    b += f'<rect x="{cx - 26}" y="206" width="52" height="56" rx="6" class="f-warn"/>'
    b += T(cx + 34, 230, 'Segment', 'f-s', 'start') + T(cx + 34, 246, 'resected', 'f-s', 'start')
    b += arrow(cx - 40, 160, cx - 40, 200) + arrow(cx - 40, 300, cx - 40, 268)
    # carina and right main bronchus to the hilum (patient's right on the left)
    b += f'<path d="M{cx - 18} 322 L{cx - 90} 368 M{cx + 18} 322 L{cx + 70} 360" class="f-l" style="stroke-width:12;stroke-linecap:round;opacity:.35"/>'
    b += f'<ellipse cx="{cx - 118}" cy="388" rx="48" ry="34" class="f-track"/><ellipse cx="{cx - 118}" cy="388" rx="48" ry="34" class="f-dash"/>'
    b += T(cx - 118, 392, 'Right hilum', 'f-s')
    b += f'<path d="M{cx - 150} 360 Q{cx - 160} 420 {cx - 118} 430 Q{cx - 76} 420 {cx - 86} 360" class="f-cut" style="stroke-width:2.5"/>'
    b += f'<line x1="{cx - 118}" y1="440" x2="{cx - 118}" y2="474" class="f-cut" style="stroke-width:3"/>'
    b += arrow(cx - 70, 380, cx - 36, 340)
    # numbers
    b += _d8_d8_num(cx + 30, 186, 1) + _d8_d8_num(cx - 82, 44, 3) + _d8_d8_num(cx - 148, 466, 4) + _d8_d8_num(cx - 172, 410, 5)
    # chin stitch inset
    b += f'<circle cx="{cx + 120}" cy="372" r="30" class="f-b0"/>'
    b += f'<path d="M{cx + 132} 400 L{cx + 150} 470" class="f-l" style="stroke-width:8;stroke-linecap:round"/>'
    b += f'<path d="M{cx + 140} 398 C{cx + 158} 420 {cx + 160} 440 {cx + 150} 452" class="f-dash" style="stroke-width:2"/>'
    b += T(cx + 166, 440, 'Chin stitch', 'f-s', 'start')
    b += _d8_d8_num(cx + 82, 410, 2)
    b += T(cx + 120, 330, 'Neck flexed', 'f-s')
    # legend
    lx = 430
    b += T(lx, 46, 'In this order', 'f-h', 'start')
    rows = [('1', ['Pretracheal dissection']),
            ('2', ['Neck flexion to 30 degrees with a', 'chin-to-sternum stitch']),
            ('3', ['Suprahyoid laryngeal release, which', 'drops larynx, cricoid and trachea;', 'preferred to infrahyoid (dysphagia,', 'aspiration)']),
            ('4', ['Divide the inferior pulmonary', 'ligament']),
            ('5', ['Right hilar release: open the', 'pericardium; if needed mobilise the', 'right PA and superior vein'])]
    y = 62
    for n, ls in rows:
        b += _d8_d8_num(lx + 10, y + 6, n)
        b += T(lx + 28, y + 11, ls, 'f-s', 'start')
        y += 17 * len(ls) + 12
    b += box(lx - 6, y + 4, 286, 80, ['All five: up to half the trachea', '(about 6 cm). Beyond them: divide', 'the left main bronchus and reimplant', 'it on the right'], 'ok', 'f-s')
    return svg(486, b)


# ---------------------------------------------------------------- 12 tracheal resection steps (t12)

def _d8_d8_trach(x, y0, y1, w=40):
    b = f'<rect x="{x - w / 2}" y="{y0}" width="{w}" height="{y1 - y0}" rx="8" class="f-b0"/>'
    n = int((y1 - y0 - 10) / 18)
    for i in range(n):
        b += line(x - w / 2 + 2, y0 + 12 + i * 18, x + w / 2 - 2, y0 + 12 + i * 18, 'f-grid')
    return b


def d8_tracheal_resection_steps():
    """Tracheal resection in four panels, from TSRA ch. 40 operative principles."""
    b = T(12, 22, 'Tracheal resection and reconstruction', 'f-h', 'start')
    xs = [92, 270, 450, 628]
    heads = ['A  Expose', 'B  Divide below', 'C  Resect', 'D  Join']
    for i, x in enumerate(xs):
        b += f'<rect x="{x - 84}" y="34" width="168" height="348" rx="10" class="f-track"/>'
        b += T(x, 54, heads[i], 'f-h')
    # A: stricture; circumferential dissection only at the stricture
    x = xs[0]
    b += _d8_d8_trach(x, 66, 300)
    b += f'<path d="M{x - 20} 160 Q{x} 176 {x + 20} 160 L{x + 20} 206 Q{x} 190 {x - 20} 206 Z" class="f-warn"/>'
    b += f'<rect x="{x - 30}" y="152" width="60" height="62" rx="6" class="f-dash" style="stroke-width:2"/>'
    b += T(x, 316, 'Anterior dissection; round', 'f-s')
    b += T(x, 333, ['only at the stricture,', '1 to 1.5 cm'], 'f-s')
    # B: traction sutures and cross-field tube in the distal trachea
    x = xs[1]
    b += _d8_d8_trach(x, 66, 186) + _d8_d8_trach(x, 210, 300)
    b += f'<path d="M{x - 20} 160 Q{x} 176 {x + 20} 160 L{x + 20} 186 L{x - 20} 186 Z" class="f-warn"/>'
    for s in (-1, 1):
        b += f'<path d="M{x + s * 18} 222 C{x + s * 40} 220 {x + s * 52} 210 {x + s * 62} 196" class="f-dash" style="stroke-width:2"/>'
    b += f'<path d="M{x + 74} 140 C{x + 40} 170 {x + 8} 196 {x + 4} 236" class="f-l" style="stroke-width:8;stroke-linecap:round;opacity:.45"/>'
    b += f'<ellipse cx="{x + 4}" cy="244" rx="14" ry="8" class="f-b1"/>'
    b += T(x, 316, 'Traction sutures; divide;', 'f-s')
    b += T(x, 333, ['ventilate across', 'the field'], 'f-s')
    # C: proximal segment lifted off the oesophagus and resected
    x = xs[2]
    b += _d8_d8_trach(x - 12, 66, 150) + _d8_d8_trach(x - 12, 230, 300)
    b += f'<rect x="{x + 12}" y="66" width="30" height="234" rx="10" class="f-dash"/>'
    b += T(x + 48, 250, ['Oeso-', 'phagus'], 'f-s', 'start')
    b += f'<path d="M{x - 32} 150 Q{x - 12} 166 {x + 8} 150 L{x + 8} 186 L{x - 32} 186 Z" class="f-warn"/>'
    b += f'<line x1="{x - 40}" y1="150" x2="{x + 16}" y2="150" class="f-cut" style="stroke-width:3"/>'
    b += T(x, 316, 'Lift the upper segment', 'f-s')
    b += T(x, 333, ['off the oesophagus;', 'resect'], 'f-s')
    # D: end-to-end anastomosis, strap muscle cover
    x = xs[3]
    b += _d8_d8_trach(x, 96, 186) + _d8_d8_trach(x, 186, 270)
    for i in range(6):
        b += f'<line x1="{x - 18 + i * 7.2}" y1="180" x2="{x - 18 + i * 7.2}" y2="192" class="f-l"/>'
    b += f'<rect x="{x + 24}" y="152" width="22" height="70" rx="8" class="f-ok"/>'
    b += T(x + 50, 150, ['Strap', 'muscle'], 'f-s', 'start')
    b += T(x, 316, 'End to end, tension-free,', 'f-s')
    b += T(x, 333, ['single-layer PDS;', 'extubate, neck flexed'], 'f-s')
    b += box(10, 394, 345, 76, ['Not yet: acute airway inflammation,', 'pneumonia, prednisolone over 10 mg a day.', 'Unavoidable tracheostomy: through the stenosis'], 'warn', 'f-s')
    b += box(365, 394, 345, 76, ['Glottic oedema: small uncuffed tube, steroids,', 'fluid restriction, retry in theatre; then', 'tracheostomy two rings below the join'], 'b1', 'f-s')
    return svg(480, b)


# ---------------------------------------------------------------- 13 tracheostomy injuries (t12)

def d8_tracheostomy_injuries():
    """Where each post-tracheostomy injury arises along the tube, in side view."""
    b = T(12, 22, 'Injuries along a tracheostomy tube: side view, front to the left', 'f-h', 'start')
    # sternum and skin
    b += '<path d="M60 40 L84 150" class="f-l"/>'
    b += '<polygon points="88,154 110,150 140,360 118,364" class="f-b1"/>'
    b += T(126, 382, 'Sternum', 'f-s')
    # oesophagus with feeding tube
    b += '<rect x="268" y="40" width="40" height="320" rx="14" class="f-dash"/>'
    b += '<line x1="288" y1="40" x2="288" y2="360" class="f-duct" style="stroke-width:4"/>'
    b += T(316, 356, 'Oesophagus with feeding tube', 'f-s', 'start')
    # trachea
    b += '<rect x="200" y="40" width="64" height="320" rx="12" class="f-b0"/>'
    for i in range(16):
        b += line(202, 54 + i * 19, 214, 54 + i * 19, 'f-grid')
    b += T(232, 34, 'Trachea', 'f-s')
    # innominate artery in front of the lower trachea
    b += '<ellipse cx="170" cy="262" rx="22" ry="18" class="f-warn"/>'
    b += T(100, 256, ['Innominate', 'artery'], 'f-s', 'end') + line(102, 260, 148, 262, 'f-grid')
    # tracheostomy tube: through the skin, stoma, down the lumen; cuff below
    b += '<path d="M40 104 L120 104 C180 104 226 120 230 170 L232 250" class="f-l" style="stroke-width:14;stroke-linecap:round;opacity:.35"/>'
    b += '<path d="M40 104 L120 104 C180 104 226 120 230 170 L232 250" class="f-l"/>'
    b += '<rect x="34" y="88" width="12" height="32" rx="3" class="f-b1"/>'
    b += '<ellipse cx="232" cy="224" rx="30" ry="16" class="f-b1"/>'
    b += T(232, 228, 'cuff', 'f-s')
    # numbered sites
    b += _d8_d8_num(186, 86, 1, 'warn') + _d8_d8_num(250, 170, 2, 'b1') + _d8_d8_num(178, 222, 3, 'warn')
    b += _d8_d8_num(198, 262, 4, 'warn') + _d8_d8_num(306, 212, 5, 'warn')
    lx = 400
    rows = [(1, 'warn', 'Stoma: A-shaped stricture', ['Oversized stoma, leverage, infection;', 'anterior and lateral walls fall in']),
            (2, 'b1', 'Between stoma and cuff', ['Tracheomalacia: cartilage thinned']),
            (3, 'warn', 'Cuff: O-shaped stenosis', ['Pressure necrosis of all layers;', 'shows 3 to 6 weeks after extubation']),
            (4, 'warn', 'Low tube: innominate artery', ['Tip or cuff erodes into it: fistula,', 'heralded by a sentinel bleed']),
            (5, 'warn', 'Cuff in front, feeding tube behind', ['Tracheo-oesophageal fistula: rising', 'secretions, gastric distension'])]
    y = 44
    for n, cls, h, ls in rows:
        b += _d8_d8_num(lx + 10, y + 6, n, cls)
        b += T(lx + 28, y + 11, h, 'f-h', 'start') + T(lx + 28, y + 28, ls, 'f-s', 'start')
        y += 30 + 17 * len(ls)
    return svg(396, b)


# ---------------------------------------------------------------- 14 fistula management (t12)

def d8_fistula_management():
    """Tracheo-innominate bleed: cuff, finger, tube, theatre; and the benign TEF plan."""
    b = T(12, 22, 'Tracheo-innominate fistula: cuff, finger, tube, theatre', 'f-h', 'start')
    # sketch: finger through the stoma pushes the artery forward onto the sternum
    b += '<polygon points="40,140 60,136 92,300 72,304" class="f-b1"/>'
    b += T(60, 322, 'Sternum', 'f-s')
    b += '<rect x="150" y="50" width="54" height="210" rx="12" class="f-b0"/>'
    for i in range(10):
        b += line(152, 64 + i * 19, 162, 64 + i * 19, 'f-grid')
    b += T(178, 44, 'Trachea', 'f-s')
    b += '<ellipse cx="106" cy="200" rx="20" ry="16" class="f-warn"/>'
    b += T(100, 290, ['Innominate artery', 'pressed forward'], 'f-s', 'start')
    b += '<path d="M10 84 L110 84 C150 84 168 104 166 140 L152 186" class="f-l" style="stroke-width:16;stroke-linecap:round;opacity:.4"/>'
    b += arrow(146, 194, 128, 199)
    b += T(14, 68, 'Finger via the stoma', 'f-s', 'start')
    # sequence
    steps = [('1', 'b1', ['Sentinel bleed: treat as a fistula', 'until bronchoscopy shows otherwise']),
             ('2', 'warn', ['Overinflate the tracheostomy cuff']),
             ('3', 'warn', ['Fails: finger through the stoma,', 'press the artery onto the sternum']),
             ('4', 'b1', ['Intubate from above, or a smaller', 'tube through the stoma']),
             ('5', 'ok', ['Theatre: resect the artery and', 'reconstruct, anatomic or extra-', 'anatomic; healthy tissue over the', 'suture lines'])]
    x0, y = 250, 40
    for n, cls, ls in steps:
        h = 17 * len(ls) + 14
        b += f'<rect x="{x0}" y="{y}" width="460" height="{h}" rx="9" class="f-{cls}"/>'
        b += _d8_d8_num(x0 + 18, y + h / 2, n, cls)
        b += T(x0 + 40, y + h / 2 + 5 - (len(ls) - 1) * 8.5, ls, 'f-s', 'start')
        y += h + 8
    b += T(12, y + 22, 'Benign tracheo-oesophageal fistula', 'f-h', 'start')
    y += 34
    st = [['Longer tube,', 'cuff below', 'the fistula'], ['Draining', 'gastrostomy,', 'feeding', 'jejunostomy'], ['Wean from', 'the ventilator'],
          ['Single stage: tracheal', 'resection, oesophageal', 'closure, muscle flap', 'between the two']]
    ws = [150, 150, 150, 220]
    x = 10
    for i, ls in enumerate(st):
        b += box(x, y, ws[i] - 14, 84, ls, 'ok' if i == 3 else 'b0', 'f-s')
        if i < 3:
            b += arrow(x + ws[i] - 14, y + 42, x + ws[i] - 2, y + 42)
        x += ws[i]
    b += box(10, y + 96, 700, 40, 'Malignant fistula: tube and cuff below the fistula, then a stent; stenting both tubes can enlarge it', 'warn', 'f-s')
    return svg(y + 146, b)


# ---------------------------------------------------------------- 15 airway stents (t12)

def d8_airway_stents():
    """Silicone, self-expanding metal and hybrid stents, with sizing rules."""
    b = T(12, 22, 'Airway stents: three types and how to size them', 'f-h', 'start')
    xs = [125, 360, 595]
    for i, x in enumerate(xs):
        # airway wall either side
        b += f'<rect x="{x - 90}" y="44" width="180" height="16" rx="6" class="f-track"/><rect x="{x - 90}" y="140" width="180" height="16" rx="6" class="f-track"/>'
        b += line(x - 90, 60, x + 90, 60, 'f-grid') + line(x - 90, 140, x + 90, 140, 'f-grid')
    # silicone: solid thick-walled tube
    x = xs[0]
    b += f'<rect x="{x - 70}" y="62" width="140" height="76" rx="10" class="f-b1"/>'
    b += f'<rect x="{x - 70}" y="76" width="140" height="48" rx="6" class="f-lumen"/>'
    # metal: open lattice
    x = xs[1]
    d = ''
    for i in range(8):
        a = x - 70 + i * 17.5
        d += f'M{a} 62 L{a + 17.5} 138 M{a + 17.5} 62 L{a} 138 '
    b += f'<path d="{d}" class="f-l"/>'
    b += line(x - 70, 62, x + 70, 62) + line(x - 70, 138, x + 70, 138)
    # hybrid: lattice under a covering
    x = xs[2]
    b += f'<rect x="{x - 70}" y="62" width="140" height="76" rx="6" class="f-ok"/>'
    d = ''
    for i in range(8):
        a = x - 70 + i * 17.5
        d += f'M{a} 62 L{a + 17.5} 138 M{a + 17.5} 62 L{a} 138 '
    b += f'<path d="{d}" class="f-l" style="opacity:.6"/>'
    heads = ['Silicone', 'Self-expanding metal', 'Hybrid (covered)']
    fors = [['Cheap, durable, removable,', 'little granulation'], ['Flexible scope; strong radial', 'force; wide lumen; rarely', 'migrates; tight or distorted', 'stenoses and fistulae'], ['Easier to reposition;', 'little ingrowth']]
    agst = [['Needs rigid bronchoscopy;', 'migrates; narrower lumen', 'plugs with mucus'], ['Granulation, perforation,', 'hard to remove'], ['Dearest; the external', 'covering migrates more']]
    for i, x in enumerate(xs):
        b += T(x, 180, heads[i], 'f-h')
        b += f'<rect x="{x - 112}" y="192" width="224" height="100" rx="9" class="f-ok"/>'
        b += T(x - 102, 210, 'For', 'f-h', 'start') + T(x - 102, 228, fors[i], 'f-s', 'start')
        b += f'<rect x="{x - 112}" y="300" width="224" height="74" rx="9" class="f-warn"/>'
        b += T(x - 102, 318, 'Against', 'f-h', 'start') + T(x - 102, 336, agst[i], 'f-s', 'start')
    b += box(10, 384, 700, 60, ['Size: diameter 1 to 2 mm over the largest balloon; extend 5 to 10 mm beyond disease (metal) or 10 to 15 mm',
                                '(silicone). Mucus plugging 4 to 27%, granulation 4 to 10%, migration 3 to 10%. Trachea and main bronchi only.'], 'b0', 'f-s')
    return svg(454, b)


# ---- figs_D9.py
"""Drawing pass D9: pectus, oesophageal benign disease, perforation, pleura, thoracic duct, thoracic outlet.
Schematics drawn for the ST4 notes from the note text and TSRA Review chapters on disk (22 November 2026)."""
import math



def _d9_num(x, y, n, cls='b1'):
    return (f'<circle cx="{x}" cy="{y}" r="11" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def _d9_band(cx, cy, r1, r2, a0, a1, cls):
    """Annular sector; angles in degrees, 0 at the top, clockwise."""
    if a1 - a0 >= 360:
        return (f'<path d="M{cx - r2} {cy} A{r2} {r2} 0 1 0 {cx + r2} {cy} A{r2} {r2} 0 1 0 {cx - r2} {cy} Z '
                f'M{cx - r1} {cy} A{r1} {r1} 0 1 1 {cx + r1} {cy} A{r1} {r1} 0 1 1 {cx - r1} {cy} Z" '
                f'class="f-{cls}" fill-rule="evenodd"/>')

    def p(r, a):
        t = math.radians(a)
        return cx + r * math.sin(t), cy - r * math.cos(t)
    large = 1 if a1 - a0 > 180 else 0
    x1, y1 = p(r2, a0); x2, y2 = p(r2, a1); x3, y3 = p(r1, a1); x4, y4 = p(r1, a0)
    return (f'<path d="M{x1:.1f} {y1:.1f} A{r2} {r2} 0 {large} 1 {x2:.1f} {y2:.1f} L{x3:.1f} {y3:.1f} '
            f'A{r1} {r1} 0 {large} 0 {x4:.1f} {y4:.1f} Z" class="f-{cls}"/>')


# ---------------------------------------------------------------- pectus

def _d9_chest(cx, dep, top=80, bot=262, half=150):
    """Axial chest outline; dep > 0 pushes the sternum in, dep < 0 pushes it out."""
    s = top + dep
    return (f'<path d="M{cx - half} {top + 90} C{cx - half} {top + 20} {cx - 95} {top - 4} {cx - 52} {top} '
            f'C{cx - 44} {top + 6} {cx - 34} {s} {cx} {s} C{cx + 34} {s} {cx + 44} {top + 6} {cx + 52} {top} '
            f'C{cx + 95} {top - 4} {cx + half} {top + 20} {cx + half} {top + 90} '
            f'C{cx + half} {bot - 20} {cx + 80} {bot} {cx} {bot} C{cx - 80} {bot} {cx - half} {bot - 20} {cx - half} {top + 90} Z" '
            f'class="f-b0"/>')


def d9_nuss():
    """Nuss repair: axial sections before and after the bar is turned."""
    b = T(12, 22, 'Nuss repair: axial section seen from below', 'f-h', 'start')
    b += T(12, 44, "Patient's right", 'f-s', 'start') + T(708, 44, "Patient's left", 'f-s', 'end')
    for cx, dep, after in [(205, 52, False), (535, 14, True)]:
        b += _d9_chest(cx, dep)
        sy = 80 + dep
        b += f'<rect x="{cx - 24}" y="{sy + 1}" width="48" height="12" rx="5" class="f-b1"/>'
        b += f'<circle cx="{cx}" cy="236" r="18" class="f-b1"/>' + T(cx, 240, 'Spine', 'f-s')
        b += f'<ellipse cx="{cx + 38}" cy="196" rx="44" ry="26" class="f-track"/>'
        b += f'<ellipse cx="{cx + 38}" cy="196" rx="44" ry="26" class="f-l"/>' + T(cx + 38, 200, 'Heart', 'f-s')
        if not after:
            b += f'<path d="M{cx - 126} 124 Q{cx} 196 {cx + 126} 124" class="f-l" fill="none" style="stroke-width:6px;stroke-linecap:round"/>'
            b += f'<path d="M{cx - 205} 162 L{cx - 128} 146" class="f-l" style="stroke-width:7px;stroke-linecap:round"/>'
            b += T(cx - 198, 186, ['Thoracoscope', '(right side)'], 'f-s', 'start')
            b += T(cx, 300, 'Before: depressed lower sternum;', 'f-h')
            b += T(cx, 318, 'bar passed behind it, convex side back', 'f-s')
            b += arrow(cx + 70, 132, cx + 40, 154) + T(cx + 66, 126, 'Bar', 'f-s', 'start')
        else:
            b += f'<path d="M{cx - 128} 128 Q{cx} 70 {cx + 128} 128" class="f-l" fill="none" style="stroke-width:6px;stroke-linecap:round"/>'
            for s in (-1, 1):
                b += f'<rect x="{cx + s * 128 - 9}" y="{121}" width="18" height="14" rx="3" class="f-warn"/>'
            b += T(cx, 300, 'After: bar turned 180 degrees;', 'f-h')
            b += T(cx, 318, 'sternum lifted, bar fixed laterally', 'f-s')
            b += T(cx + 108, 156, ['Lateral', 'fixation'], 'f-s')
    b += '<path d="M330 72 C350 46 380 46 400 72" class="f-l" fill="none" marker-end="url(#ah)"/>'
    b += T(365, 40, 'Rotate 180 degrees', 'f-h')
    b += box(10, 338, 226, 64, ['1. Retrosternal tunnel made', 'with a thoracoscopically', 'guided dissector'], 'b0', 'f-s')
    b += box(247, 338, 226, 64, ['2. Convex bar passed,', 'then rotated 180 degrees:', 'the sternum rises'], 'b1', 'f-s')
    b += box(484, 338, 226, 64, ['3. Fixed laterally; out at 2 years.', 'Second bar if older; best', 'done by about 14 years'], 'ok', 'f-s')
    return svg(412, b)


def _d9_rib_pair(cx, y, half_c, rib_len, resect):
    out = ''
    for s in (-1, 1):
        x0 = cx + s * 14
        x1 = cx + s * (14 + half_c)
        x2 = cx + s * (14 + half_c + rib_len)
        out += f'<path d="M{x1} {y + 8} L{x2} {y - 18}" class="f-l" style="stroke-width:6px;stroke-linecap:round"/>'
        if resect:
            out += f'<path d="M{x0} {y - 6} L{x1} {y + 1} L{x1} {y + 15} L{x0} {y + 8} Z" class="f-warn"/>'
            out += f'<path d="M{x0} {y - 9} L{x1} {y - 2} L{x1} {y + 18} L{x0} {y + 11} Z" class="f-dash"/>'
        else:
            out += f'<path d="M{x0} {y - 5} L{x1} {y + 2} L{x1} {y + 13} L{x0} {y + 6} Z" class="f-b0"/>'
    return out


def d9_ravitch():
    """Modified Ravitch: front view of the cartilage resection and side view of the osteotomy and bar."""
    b = T(12, 22, 'Modified Ravitch repair', 'f-h', 'start')
    cx = 170
    b += f'<rect x="{cx - 17}" y="46" width="34" height="38" rx="8" class="f-b1"/>'
    b += f'<rect x="{cx - 13}" y="86" width="26" height="196" rx="8" class="f-b1"/>'
    for i in range(7):
        y = 64 + i * 32
        b += _d9_rib_pair(cx, y, 34 + i * 4, 70 - i * 3, i >= 2)
    b += T(cx, 312, 'Front view', 'f-h')
    b += T(cx + 150, 40, ['Manubrium and first', 'two ribs spared'], 'f-s', 'start')
    b += arrow(cx + 146, 46, cx + 20, 60)
    b += T(cx, 334, ['Shaded: deformed cartilages', 'removed inside their', 'perichondrium (dashed)'], 'f-s')
    # side view: anterior to the left
    ox = 440
    b += T(ox + 110, 40, 'Side view (anterior to the left)', 'f-s')
    b += f'<path d="M{ox + 60} 60 L{ox + 70} 150 L{ox + 120} 262" class="f-dash" style="stroke-width:10px;opacity:.6"/>'
    b += T(ox + 140, 252, ['Before:', 'lower sternum', 'depressed'], 'f-s', 'start')
    b += f'<path d="M{ox + 60} 60 L{ox + 70} 150 L{ox + 74} 262" class="f-l" style="stroke-width:10px;stroke-linecap:round"/>'
    b += f'<path d="M{ox + 58} 146 L{ox + 80} 150 L{ox + 60} 158 Z" class="f-warn"/>'
    b += arrow(ox - 20, 150, ox + 52, 152) + T(ox - 24, 146, ['Wedge', 'osteotomy'], 'f-s', 'end')
    b += f'<circle cx="{ox + 90}" cy="236" r="8" class="f-warn"/>'
    b += arrow(ox + 170, 190, ox + 98, 230) + T(ox + 176, 180, ['Retrosternal bar', '(not in the', 'original Ravitch)'], 'f-s', 'start')
    b += T(ox + 74, 318, 'After: sternum elevated and held', 'f-h')
    b += box(10, 384, 345, 62, ['Excavatum: modified Ravitch, with a bar.', 'Suits a rotated sternum and mixed', 'excavatum and carinatum'], 'b1', 'f-s')
    b += box(365, 384, 345, 62, ['Carinatum: resection and osteotomy as in', 'the original Ravitch; no retrosternal bar.', 'Only if bracing fails or is unsuitable'], 'b0', 'f-s')
    return svg(456, b)


def d9_carinatum():
    """Pectus carinatum: shape compared with excavatum, and the treatment pathway."""
    b = T(12, 22, 'Axial outlines, seen from below', 'f-h', 'start')
    b += _d9_chest(150, 46, top=60, bot=200, half=120)
    b += '<rect x="132" y="104" width="36" height="10" rx="4" class="f-b1"/>'
    b += T(150, 222, 'Excavatum: sternum pushed in', 'f-s')
    b += _d9_chest(450, -30, top=78, bot=200, half=120)
    b += '<rect x="432" y="47" width="36" height="10" rx="4" class="f-b1" transform="rotate(-12 450 52)"/>'
    b += T(450, 222, 'Carinatum: keel-like protrusion', 'f-s')
    b += T(590, 70, ['Often asymmetric:', 'left-sided bulge,', 'sternum twists', 'to the right'], 'f-s', 'start')
    b += box(10, 244, 220, 62, ['Type 1 (pigeon chest)', '10% of deformities; 4:1 male', 'mostly the lower sternum'], 'b0', 'f-s')
    b += arrow(230, 275, 254, 275)
    b += box(256, 244, 196, 62, ['Orthotic bracing first', 'for selected patients'], 'ok', 'f-s')
    b += arrow(452, 282, 490, 282) + T(471, 270, 'fails', 'f-s')
    b += box(492, 244, 218, 62, ['Resect costal cartilages,', 'sternal osteotomy;', 'no retrosternal bar'], 'b1', 'f-s')
    b += box(10, 318, 700, 44, ['Type 2 (Currarino-Silverman, pouter pigeon): early sterno-manubrial fusion, short sternum,',
                               'raised second cartilages; linked to congenital heart disease and coarctation'], 'warn', 'f-s')
    return svg(372, b)


# ---------------------------------------------------------------- oesophagus: motility

def d9_achalasia_hrm():
    """Sketches of high-resolution manometry patterns for the three achalasia subtypes."""
    b = T(12, 20, 'Achalasia subtypes on high-resolution manometry (sketches, one swallow each)', 'f-h', 'start')
    w, top, les, bot = 222, 44, 210, 236
    spec = [('Type I (classic)', 'I'), ('Type II', 'II'), ('Type III (spastic)', 'III')]
    for i, (name, k) in enumerate(spec):
        x = 10 + i * (w + 17)
        b += f'<rect x="{x}" y="{top}" width="{w}" height="{bot - top}" rx="6" class="f-track"/>'
        b += T(x + w / 2, top + 16, name, 'f-h')
        b += line(x + 54, top + 24, x + 54, bot, 'f-dash')
        b += T(x + 58, bot + 14, 'swallow', 'f-s', 'start')
        # LES band: never relaxes
        hh = 26 if k == 'III' else 18
        b += f'<rect x="{x + 6}" y="{les - hh / 2}" width="{w - 12}" height="{hh}" rx="5" class="f-warn"/>'
        b += T(x + w - 10, les + 4, 'LES' if k != 'III' else 'LES, very high', 'f-s', 'end')
        if k == 'II':
            b += f'<rect x="{x + 64}" y="{top + 30}" width="64" height="{les - top - 40}" rx="5" class="f-b1"/>'
            b += T(x + 136, top + 80, ['pan-', 'oesophageal', 'pressurisation'], 'f-s', 'start')
        elif k == 'III':
            for j, (yy, dx) in enumerate([(70, 72), (104, 66), (138, 60), (170, 64)]):
                b += f'<ellipse cx="{x + dx + 30}" cy="{yy + 10}" rx="16" ry="12" class="f-warn"/>'
            b += T(x + 166, 108, ['spastic,', 'premature', 'contractions'], 'f-s')
        else:
            b += T(x + 120, 120, ['no peristalsis', '(aperistalsis)'], 'f-s')
    b += T(12, top + 34, 'upper', 'f-s', 'start')
    b += box(10, 262, w, 70, ['LES over 15 mmHg,', 'aperistalsis;', 'aganglionosis'], 'b0', 'f-s')
    b += box(10 + w + 17, 262, w, 70, ['As type I plus pressurisation;', 'best response (Heller', 'relief 93% in type II)'], 'ok', 'f-s')
    b += box(10 + 2 * (w + 17), 262, w, 70, ['Hardest to treat; ganglion', 'cells preserved; POEM can', 'tailor a long myotomy'], 'warn', 'f-s')
    return svg(342, b)


def _d9_oes_front(cx, goj, top, label=True):
    """Front view of distal oesophagus, junction and stomach (stomach to the patient's left, viewer's right)."""
    out = f'<rect x="{cx - 16}" y="{top}" width="32" height="{goj - top + 6}" rx="8" class="f-b0"/>'
    out += (f'<path d="M{cx - 16} {goj} C{cx - 24} {goj + 40} {cx - 10} {goj + 120} {cx + 50} {goj + 124} '
            f'C{cx + 120} {goj + 126} {cx + 140} {goj + 60} {cx + 110} {goj + 10} '
            f'C{cx + 90} {goj - 26} {cx + 40} {goj - 30} {cx + 16} {goj} Z" class="f-b0"/>')
    out += line(cx - 30, goj, cx + 30, goj, 'f-grid')
    if label:
        out += T(cx - 34, goj + 4, 'GOJ', 'f-s', 'end')
    return out


def _d9_ruler(x, y0, cm_px, cms, ticks):
    out = line(x, y0 - cms[0] * cm_px, x, y0 + cms[1] * cm_px, 'f-grid')
    for c in ticks:
        out += line(x - 4, y0 - c * cm_px, x + 4, y0 - c * cm_px, 'f-grid')
    return out


def d9_heller_poem():
    """Heller myotomy against POEM: extent of the myotomy on each side of the junction."""
    u = 15  # px per cm, schematic
    b = T(180, 22, 'Laparoscopic or robotic Heller', 'f-h') + T(540, 22, 'POEM (peroral endoscopic myotomy)', 'f-h')
    b += line(360, 10, 360, 330, 'f-dash')
    goj = 214
    # Heller
    cx = 170
    b += _d9_oes_front(cx, goj, 44)
    b += f'<path d="M{cx} {goj - 6 * u} L{cx} {goj} C{cx + 4} {goj + 20} {cx + 14} {goj + 34} {cx + 22} {goj + 3 * u}" class="f-cut" style="stroke-width:4px"/>'
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>' % (cx - 80, goj - 6 * u, cx - 80, goj - 2)
    b += T(cx - 86, goj - 3 * u, ['5 to 6 cm', 'on the', 'oesophagus'], 'f-s', 'end')
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>' % (cx - 80, goj + 2, cx - 80, goj + 3 * u)
    b += T(cx - 86, goj + 28, ['3 cm on', 'the stomach'], 'f-s', 'end')
    b += f'<path d="M{cx - 12} 50 C{cx - 8} 110 {cx - 10} 170 {cx - 6} {goj - 4}" class="f-nerve" stroke-dasharray="3 3"/>'
    b += T(cx + 30, 70, ['Preserve the', 'left vagus'], 'f-s', 'start')
    b += box(10, 348, 340, 60, ['Then a partial fundoplication.', 'Relief over 80% (93% in type II)'], 'b1', 'f-s')
    # POEM
    cx = 520
    b += _d9_oes_front(cx, goj, 44)
    b += f'<rect x="{cx - 6}" y="{goj - 10 * u}" width="12" height="{10 * u + 2 * u}" rx="6" class="f-track"/>'
    b += f'<rect x="{cx - 6}" y="{goj - 10 * u}" width="12" height="{10 * u + 2 * u}" rx="6" class="f-dash"/>'
    b += f'<path d="M{cx} {goj - 7 * u} L{cx} {goj + 2 * u}" class="f-cut" style="stroke-width:4px"/>'
    b += f'<circle cx="{cx}" cy="{goj - 10 * u}" r="6" class="f-warn"/>'
    b += arrow(cx + 66, goj - 10 * u + 6, cx + 10, goj - 10 * u) + T(cx + 70, goj - 10 * u, ['Mucosal entry', '10 cm above the', 'GOJ (CO2);', 'clips close it'], 'f-s', 'start')
    b += arrow(cx + 66, goj - 5 * u, cx + 10, goj - 4 * u) + T(cx + 70, goj - 5 * u + 4, ['Submucosal', 'tunnel'], 'f-s', 'start')
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>' % (cx - 80, goj + 2, cx - 80, goj + 2 * u)
    b += T(cx - 86, goj + 22, ['2 cm on', 'the stomach'], 'f-s', 'end')
    b += box(370, 348, 340, 60, ['Success about 90%, similar to Heller,', 'but reflux in 44%'], 'warn', 'f-s')
    b += T(360, 428, 'Dashed: the tunnel. Red: the myotomy. Drawn to an approximate centimetre scale.', 'f-s')
    return svg(440, b)


def d9_fundoplication():
    """Nissen, Toupet and Dor wraps in cross-section."""
    b = T(12, 20, 'Fundoplication in cross-section (anterior at the top)', 'f-h', 'start')
    spec = [('Nissen', 0, 360, '360 degrees, posterior', ['About 2 cm long, loose,', 'over a 54 to 60 Fr bougie.', 'Bloating, cannot belch,', 'dysphagia']),
            ('Toupet', 45, 315, '270 degrees, posterior partial', ['For poor motility;', 'avoid a 360 degree wrap', 'with ineffective', 'motility']),
            ('Dor', -90, 90, '180 degrees, anterior', ['Usually with a', 'myotomy (Heller)'])]
    for i, (name, a0, a1, deg, notes) in enumerate(spec):
        cx = 125 + i * 236
        cy = 118
        b += T(cx, 46, name, 'f-h')
        b += _d9_band(cx, cy, 34, 58, a0, a1, 'b1')
        b += f'<circle cx="{cx}" cy="{cy}" r="30" class="f-b0"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="10" class="f-lumen"/>'
        b += T(cx, 196, deg, 'f-s')
        b += T(cx, 222, notes, 'f-s')
    b += T(12, 316, 'Shaded: gastric fundus wrapped round the oesophagus. Belsey: transthoracic 240 degree wrap.', 'f-s', 'start')
    return svg(330, b)


def _d9_hh_panel(x0, kind):
    cx = x0 + 70
    dy = 176
    out = ''
    out += f'<path d="M{x0 + 4} {dy} L{cx - 16} {dy}" class="f-l" style="stroke-width:6px"/>'
    out += f'<path d="M{cx + 16} {dy} L{x0 + 166} {dy}" class="f-l" style="stroke-width:6px"/>'
    goj = 120 if kind in ('I', 'III', 'IV') else dy
    # main stomach below the diaphragm
    out += (f'<path d="M{cx - 12} {dy} C{cx - 30} {dy + 26} {cx - 22} {dy + 76} {cx + 18} {dy + 82} '
            f'C{cx + 62} {dy + 86} {cx + 82} {dy + 50} {cx + 64} {dy + 20} C{cx + 54} {dy + 4} {cx + 30} {dy} {cx + 12} {dy} Z" class="f-b0"/>')
    if kind in ('I', 'III', 'IV'):
        out += f'<path d="M{cx - 12} {dy + 2} C{cx - 30} {dy - 20} {cx - 26} {goj + 2} {cx} {goj} C{cx + 26} {goj + 2} {cx + 30} {dy - 20} {cx + 12} {dy + 2} Z" class="f-warn"/>'
    if kind in ('II', 'III', 'IV'):
        fx = cx + 40
        out += f'<path d="M{cx + 6} {dy + 4} C{cx + 4} {dy - 30} {fx - 34} {82} {fx} {78} C{fx + 30} {76} {fx + 34} {dy - 40} {cx + 16} {dy + 4} Z" class="f-warn"/>'
    if kind == 'IV':
        out += f'<rect x="{x0 + 8}" y="84" width="34" height="56" rx="14" class="f-ok"/>'
        out += T(x0 + 25, 76, 'colon', 'f-s')
    out += f'<rect x="{cx - 8}" y="34" width="16" height="{goj - 34}" rx="5" class="f-b0"/>'
    out += f'<circle cx="{cx}" cy="{goj}" r="5" class="f-ah"/>'
    return out


def d9_hiatus_types():
    """Hiatus hernia types I to IV."""
    b = T(12, 20, 'Hiatus hernia types (dot: gastro-oesophageal junction; shaded: stomach above the diaphragm)', 'f-h', 'start')
    spec = [('I: sliding', ['GOJ in the chest;', '95% of hiatus hernias;', 'not a true PEH']),
            ('II: paraoesophageal', ['GOJ at the hiatus,', 'fundus herniates;', 'least common PEH']),
            ('III: mixed', ['I plus II: GOJ in chest,', '30% or more of', 'stomach above']),
            ('IV: other organs', ['Colon, pancreas or', 'omentum herniate', 'as well'])]
    for i, (name, lines_) in enumerate(spec):
        x0 = 10 + i * 178
        if i:
            b += line(x0 - 4, 34, x0 - 4, 330, 'f-grid')
        b += _d9_hh_panel(x0, name.split(':')[0])
        b += T(x0 + 85, 296, name, 'f-h') + T(x0 + 85, 314, lines_, 'f-s')
    b += T(14, 168, 'Diaphragm', 'f-s', 'start')
    b += box(10, 372, 700, 42, ['"Giant": loosely a third to a half of the stomach in the chest. Repair aims for 2 to 4 cm of',
                               'tension-free intra-abdominal oesophagus and a closed hiatus'], 'b1', 'f-s')
    return svg(424, b)


def d9_peh_pathway():
    """Paraoesophageal hernia: elective steps and emergency decisions."""
    b = T(12, 20, 'Elective repair', 'f-h', 'start')
    steps = ['Reduce the hernia', 'Excise the sac', ['Mobilise until', '2 to 4 cm lie in the', 'abdomen without', 'tension; else Collis'],
             ['Close the hiatus', '(with or without', 'absorbable mesh)'], ['Anti-reflux: Nissen,', 'Toupet or Dor']]
    for i, s in enumerate(steps):
        x = 10 + i * 142
        s = [s] if isinstance(s, str) else s
        s = [f'{i + 1}. ' + s[0]] + s[1:]
        b += box(x, 30, 132, 80, s, 'ok' if i == 2 else 'b0', 'f-s')
        if i < 4:
            b += arrow(x + 132, 70, x + 142, 70)
    b += T(12, 130, 'Bail-out (over 70, friable tissue, severe dysmotility): gastropexy without anti-reflux procedure.', 'f-s', 'start')
    b += T(12, 156, 'Emergency (gastric volvulus)', 'f-h', 'start')
    b += box(230, 166, 260, 44, ['Endoscopy first; NG tube may', 'decompress and allow resuscitation'], 'b1', 'f-s')
    b += arrow(300, 210, 126, 236) + arrow(360, 210, 360, 236) + arrow(420, 210, 594, 236)
    b += box(10, 238, 226, 92, ['Gross ischaemia or necrosis', 'Subtotal gastrectomy; if', 'unstable, discontinuity and', 'second look at 24 to 48 h'], 'warn', 'f-s')
    b += box(247, 238, 226, 92, ['No ischaemia, stable', 'Definitive repair', 'as above'], 'ok', 'f-s')
    b += box(484, 238, 226, 92, ['No ischaemia, unstable', '(oliguria, pressors, lactate)', 'Reduce and gastropexy;', 'definitive repair later'], 'b1', 'f-s')
    return svg(340, b)


# ---------------------------------------------------------------- perforation

def d9_boerhaave():
    """Boerhaave tear site and the steps of primary repair."""
    b = T(12, 20, 'Boerhaave rupture: site and primary repair', 'f-h', 'start')
    cx = 110
    b += f'<rect x="{cx - 20}" y="40" width="40" height="230" rx="12" class="f-b0"/>'
    b += '<path d="M14 270 C60 256 160 256 210 270" class="f-l" style="stroke-width:6px"/>'
    b += T(160, 292, 'Diaphragm', 'f-s')
    b += f'<path d="M{cx + 8} 180 L{cx + 8} 236" class="f-cut" style="stroke-width:5px"/>'
    b += f'<line x1="{cx - 36}" y1="176" x2="{cx - 36}" y2="262" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += T(cx - 42, 200, ['2 to 6 cm', 'above the', 'diaphragm'], 'f-s', 'end')
    b += T(cx + 40, 104, ["Patient's", 'left'], 'f-s', 'start') + arrow(cx + 40, 134, cx + 76, 134)
    b += T(cx, 340, ['Longitudinal tear,', 'left posterolateral', 'wall (lower third:', 'left thoracotomy)'], 'f-s')
    b += T(cx, 34, 'Thoracic oesophagus, front view', 'f-s')
    titles = [('Open the muscle', ['Extend the myotomy', 'to show the whole', 'mucosal tear']),
              ('Two layers', ['Interrupted absorbable', 'sutures, mucosa then', 'muscle; bougie optional']),
              ('Buttress', ['Vascularised flap:', 'intercostal muscle,', 'pleura, pericardium,', 'diaphragm, omentum'])]
    for i, (h, sub) in enumerate(titles):
        x = 250 + i * 156
        mx = x + 70
        b += _d9_num(x + 6, 50, i + 1, 'b1') + T(x + 22, 55, h, 'f-h', 'start')
        b += f'<rect x="{mx - 34}" y="70" width="68" height="190" rx="14" class="f-b0"/>'
        if i == 0:
            b += f'<path d="M{mx} 92 C{mx - 18} 130 {mx - 18} 200 {mx} 238 C{mx + 18} 200 {mx + 18} 130 {mx} 92 Z" class="f-warn"/>'
            b += f'<path d="M{mx} 120 L{mx} 210" class="f-cut" style="stroke-width:5px"/>'
            b += T(mx + 40, 100, 'muscle', 'f-s', 'start')
            b += T(mx + 40, 168, 'mucosa', 'f-s', 'start') + line(mx + 38, 164, mx + 4, 164, 'f-grid')
        elif i == 1:
            b += f'<path d="M{mx} 96 L{mx} 234" class="f-l"/>'
            for k in range(8):
                y = 104 + k * 17
                b += line(mx - 9, y, mx + 9, y, 'f-cut')
            for k in range(7):
                y = 112 + k * 17
                b += line(mx - 18, y - 4, mx + 18, y + 4, 'f-l')
        else:
            b += f'<path d="M{mx} 96 L{mx} 234" class="f-l"/>'
            b += f'<path d="M{mx - 20} 84 L{mx + 20} 84 L{mx + 26} 250 L{mx - 14} 250 Z" class="f-ok"/>'
            b += f'<path d="M{mx + 22} 84 C{mx + 40} 70 {mx + 60} 62 {mx + 76} 60" class="f-l" stroke-dasharray="4 3"/>'
        b += T(mx, 282, sub, 'f-s')
    b += box(250, 362, 460, 40, 'Then debride, drain widely and place an enteral feeding tube', 'ok', 'f-s')
    return svg(412, b)


def d9_perf_pathway():
    """Oesophageal perforation: management pathway once the diagnosis is made."""
    b = box(170, 8, 380, 44, ['Water-soluble swallow (thin barium if negative)', 'or CT with oral contrast'], 'b0', 'f-s')
    b += arrow(360, 52, 360, 70)
    b += box(120, 72, 480, 44, ['Broad antibiotics with antifungal cover. Endoscopy in theatre', 'to exclude distal obstruction before any repair'], 'b1', 'f-s')
    b += arrow(250, 116, 126, 146) + arrow(360, 116, 360, 146) + arrow(470, 116, 594, 146)
    b += box(10, 148, 226, 106, ['Contained, drains back', 'into the lumen; no sepsis,', 'obstruction or cancer', '', 'Nil by mouth, antibiotics,', 'close observation'], 'ok', 'f-s')
    b += box(247, 148, 226, 106, ['Repairable', '', 'Debride, myotomy to show', 'the tear, two-layer repair,', 'flap, wide drainage, feeding'], 'b1', 'f-s')
    b += box(484, 148, 226, 106, ['Repair not possible or', 'too unstable', '', 'T-tube, exclusion and', 'diversion, resection, or', 'stent with drainage'], 'warn', 'f-s')
    b += T(360, 278, 'Late presentation alone is no longer a reason to avoid primary repair.', 'f-s')
    b += T(12, 306, 'Diseased oesophagus changes the operation', 'f-h', 'start')
    spec = [(['After pneumatic', 'dilatation'], ['Repair; myotomy', 'on opposite wall']),
            (['Benign', 'stricture'], ['Dilate', 'and repair']),
            (['Reflux'], ['Add a', 'fundoplication']),
            (['Resectable cancer,', 'undilatable stricture'], ['Oesophagectomy']),
            (['Unresectable', 'cancer'], ['Stent and', 'drain'])]
    for i, (a, t) in enumerate(spec):
        x = 10 + i * 142
        b += f'<rect x="{x}" y="316" width="132" height="104" rx="10" class="f-b0"/>'
        b += f'<rect x="{x}" y="316" width="132" height="44" rx="10" class="f-track"/>'
        b += T(x + 66, 334 if len(a) > 1 else 342, a, 'f-s')
        b += T(x + 66, 384 if len(t) > 1 else 392, t, 'f-h')
    return svg(430, b)


# ---------------------------------------------------------------- pleura and duct

def _d9_hemi(cx, cls_lung, rx_l, ry_l, peel=True):
    out = (f'<path d="M{cx} 50 C{cx - 120} 50 {cx - 150} 120 {cx - 150} 170 C{cx - 150} 230 {cx - 110} 262 {cx - 40} 262 '
           f'L{cx} 262 Z" class="f-b0"/>')
    if peel:
        out += (f'<path d="M{cx - 2} 64 C{cx - 108} 64 {cx - 136} 124 {cx - 136} 170 C{cx - 136} 222 {cx - 100} 248 {cx - 40} 248 L{cx - 2} 248" '
                f'class="f-warn" fill="none" style="stroke-width:10px;fill:none"/>')
    out += f'<ellipse cx="{cx - 72}" cy="160" rx="{rx_l}" ry="{ry_l}" class="f-{cls_lung}"/>'
    return out


def d9_decortication():
    """Trapped lung: the peel, decortication, and the fallback of incising the peel."""
    b = T(12, 20, 'Fibrothorax: axial sketches of one hemithorax', 'f-h', 'start')
    cxs = [190, 425, 660]
    # panel 1 trapped
    cx = cxs[0]
    b += _d9_hemi(cx, 'b1', 40, 56)
    b += f'<ellipse cx="{cx - 72}" cy="160" rx="50" ry="66" class="f-warn" fill="none" style="fill:none;stroke-width:8px"/>'
    b += T(cx - 72, 164, 'Lung', 'f-s')
    b += T(cx - 70, 290, ['Peel on the pleural', 'surfaces traps the lung'], 'f-s')
    b += T(cx - 70, 40, 'Trapped', 'f-h')
    # panel 2 decorticated
    cx = cxs[1]
    b += _d9_hemi(cx, 'b1', 70, 92, peel=False)
    b += T(cx - 72, 156, ['Lung', 're-expanded'], 'f-s')
    b += T(cx - 70, 290, ['Peel stripped:', 'decortication'], 'f-s')
    b += T(cx - 70, 40, 'Complete', 'f-h')
    # panel 3 incised
    cx = cxs[2]
    b += _d9_hemi(cx, 'b1', 56, 72, peel=False)
    b += f'<ellipse cx="{cx - 72}" cy="160" rx="62" ry="80" class="f-warn" fill="none" style="fill:none;stroke-width:8px" stroke-dasharray="40 14"/>'
    b += T(cx - 72, 164, 'Lung', 'f-s')
    b += T(cx - 70, 290, ['Peel incised in several', 'places: partial', 're-expansion'], 'f-s')
    b += T(cx - 70, 40, 'If complete is impossible', 'f-h')
    b += box(10, 340, 345, 76, ['Decorticate when: significant symptoms;', 'little gain from draining fluid; 50% or', 'more lung compression; 6 weeks of', 'conservative care failed'], 'ok', 'f-s')
    b += box(365, 340, 345, 76, ['Not when: ipsilateral bronchus obstructed;', 'pleural malignancy; infection uncontrolled;', 'significant contralateral disease;', 'prohibitive risk'], 'warn', 'f-s')
    return svg(426, b)


def d9_duct_mass():
    """Axial view just above the hiatus: the tissue taken in a mass ligation of the thoracic duct."""
    b = T(12, 20, 'Just above the hiatus, axial view seen from below', 'f-h', 'start')
    b += T(12, 44, "Patient's right", 'f-s', 'start') + T(708, 44, "Patient's left", 'f-s', 'end')
    cx = 360
    b += f'<path d="M{cx - 70} 74 L{cx + 70} 74" class="f-l" style="stroke-width:5px"/>'
    b += T(cx, 64, 'Pericardium', 'f-s')
    b += (f'<path d="M{cx - 54} 92 L{cx + 70} 92 C{cx + 82} 140 {cx + 60} 196 {cx + 40} 210 L{cx - 46} 210 '
          f'C{cx - 70} 190 {cx - 74} 130 {cx - 54} 92 Z" class="f-warn"/>')
    b += f'<ellipse cx="{cx}" cy="116" rx="26" ry="16" class="f-b0"/>' + T(cx, 120, 'Oesophagus', 'f-s')
    b += f'<circle cx="{cx + 52}" cy="172" r="26" class="f-b1"/>' + T(cx + 52, 176, 'Aorta', 'f-s')
    b += f'<circle cx="{cx - 40}" cy="174" r="11" class="f-b1"/>'
    b += f'<circle cx="{cx + 4}" cy="182" r="6" class="f-duct" style="stroke-width:3px"/>'
    b += f'<rect x="{cx - 34}" y="214" width="68" height="56" rx="16" class="f-b0"/>' + T(cx, 246, 'Vertebra', 'f-s')
    b += arrow(cx - 150, 190, cx - 54, 176) + T(cx - 156, 186, 'Azygos vein', 'f-s', 'end')
    b += arrow(cx + 150, 214, cx + 12, 186) + T(cx + 156, 218, ['Thoracic duct, between', 'aorta and azygos'], 'f-s', 'start')
    b += arrow(cx + 150, 120, cx + 76, 132) + T(cx + 156, 116, ['Shaded: tissue taken', 'in a mass ligation'], 'f-h', 'start')
    b += '<path d="M40 150 L180 150" class="f-l" style="stroke-width:3px" marker-end="url(#ah)"/>'
    b += T(40, 120, ['Right VATS or', 'thoracotomy, 7th space'], 'f-s', 'start')
    b += box(10, 290, 226, 70, ['Cream or olive oil 2 to 3 h', 'before shows the leak;', 'clip or ligate it if seen'], 'b0', 'f-s')
    b += box(247, 290, 226, 70, ['No leak seen: mass-ligate', 'between aorta, spine,', 'oesophagus, azygos, pericardium'], 'b1', 'f-s')
    b += box(484, 290, 226, 70, ['Success over 90%. Left side', 'if imaging or the index', 'operation puts the leak there'], 'ok', 'f-s')
    return svg(370, b)


def d9_chylo_pathway():
    """Chylothorax: diagnosis and stepwise management."""
    b = T(12, 20, 'Pleural fluid triglyceride', 'f-h', 'start')
    b += box(10, 30, 226, 50, ['110 mg/dL or more', '99% diagnostic'], 'warn', 'f-s')
    b += box(247, 30, 226, 50, ['Between the two:', 'look for chylomicrons'], 'b1', 'f-s')
    b += box(484, 30, 226, 50, ['50 mg/dL or less', 'excludes (95%)'], 'ok', 'f-s')
    b += arrow(123, 80, 123, 104)
    steps = [('Drain and re-expand', ['the lung'], 'b0'),
             ('Stop enteral intake', ['parenteral nutrition;', 'MCT diet in theory'], 'b0'),
             ('Lymphangiography', ['and duct embolisation:', 'succeeds in 50 to 70%'], 'b1'),
             ('Operate', ['post-op leak 1 L/day or', 'more for 3 to 5 days'], 'warn')]
    for i, (h, s, c) in enumerate(steps):
        x = 10 + i * 178
        b += f'<rect x="{x}" y="106" width="168" height="84" rx="10" class="f-{c}"/>'
        b += T(x + 84, 130, h, 'f-h') + T(x + 84, 152, s, 'f-s')
        if i < 3:
            b += arrow(x + 168, 148, x + 178, 148)
    b += T(360, 216, 'Morbidity and mortality rise once a leak lasts beyond a week. Ligation: 2.1% mortality, 38.8% morbidity.', 'f-s')
    return svg(228, b)


# ---------------------------------------------------------------- thoracic outlet

def d9_tos_outlet():
    """Thoracic outlet, left side from the front: the three sites of compression and the nerves at risk."""
    b = T(12, 20, 'Thoracic outlet, left side seen from the front (arrangement schematic)', 'f-h', 'start')
    b += T(30, 44, 'Midline', 'f-s', 'start') + T(560, 44, 'Arm', 'f-s', 'end')
    # first rib
    b += '<path d="M70 318 C150 250 300 236 400 300" class="f-l" fill="none" style="stroke-width:11px;stroke-linecap:round"/>'
    b += T(140, 344, 'First rib', 'f-s')
    # cervical rib (if present)
    b += '<path d="M90 236 C140 214 190 210 220 216" class="f-dash" style="stroke-width:5px"/>'
    b += T(40, 258, 'cervical rib, if present', 'f-s', 'start')
    # scalenes
    b += '<path d="M186 54 L206 54 L246 262 L222 266 Z" class="f-b0"/>'
    b += '<path d="M262 54 L292 54 L348 262 L314 260 Z" class="f-b0"/>'
    b += T(170, 70, ['Anterior', 'scalene'], 'f-s', 'end') + T(300, 70, ['Middle', 'scalene'], 'f-s', 'start')
    # plexus and artery through the triangle
    for k in range(3):
        b += f'<path d="M{222 + k * 10} 70 C{232 + k * 10} 160 {258 + k * 8} 236 {292 + k * 8} 244 C{400} {226 + k * 6} {500} {200 + k * 6} {560} {196 + k * 6}" class="f-nerve"/>'
    b += '<path d="M180 344 C230 320 262 286 282 262 C330 236 470 222 560 216" class="f-vessel" style="stroke-width:12px"/>'
    # clavicle and subclavius
    b += '<path d="M60 178 C200 196 360 178 600 140" class="f-l" fill="none" style="stroke-width:14px;stroke-linecap:round;opacity:.35"/>'
    b += T(600, 128, 'Clavicle', 'f-s', 'end')
    # pectoralis minor
    b += '<path d="M600 162 L620 172 L540 340 L500 330 Z" class="f-b0"/>'
    b += T(626, 210, ['Pectoralis', 'minor (to the', 'coracoid)'], 'f-s', 'start')
    # phrenic and long thoracic nerves
    b += '<path d="M205 66 C210 130 216 200 224 258" class="f-nerve" stroke-dasharray="6 3"/>'
    b += '<path d="M276 80 C300 150 320 220 330 320" class="f-nerve" stroke-dasharray="2 3"/>'
    # site numbers
    b += _d9_num(266, 226, 1, 'warn') + _d9_num(372, 266, 2, 'warn') + _d9_num(536, 252, 3, 'warn')
    b += T(330, 372, 'Gold lines: brachial plexus. Red: subclavian artery.', 'f-s')
    rows = [(1, 'Scalene triangle', ['Anterior and middle scalene', 'and the first rib']),
            (2, 'Costoclavicular space', ['Clavicle and first rib;', 'subclavius or scalene bulk']),
            (3, 'Subcoracoid space', ['Under pectoralis minor'])]
    y = 392
    for i, (n, h, s) in enumerate(rows):
        x = 10 + i * 236
        b += f'<rect x="{x}" y="{y}" width="226" height="70" rx="10" class="f-b0"/>'
        b += _d9_num(x + 18, y + 18, n, 'warn') + T(x + 36, y + 23, h, 'f-h', 'start') + T(x + 14, y + 44, s, 'f-s', 'start')
    b += box(10, 472, 345, 58, ['Phrenic nerve (dashed): on the front of anterior', 'scalene, lateral to medial; find it first'], 'b1', 'f-s')
    b += box(365, 472, 345, 58, ['Long thoracic nerve (dotted): pierces middle', 'scalene; injury gives a winged scapula'], 'b1', 'f-s')
    return svg(540, b)


def d9_tos_types():
    """Thoracic outlet syndrome: the three types, their share and treatment."""
    spec = [('Neurogenic', 'over 95%', ['Plexus compression:', 'pain, numbness,', 'paraesthesia'],
             ['Physiotherapy first;', 'operate if it fails'], '90% initial success', 'b1'),
            ('Venous', '3%', ['Effort thrombosis', '(Paget-Schroetter);', 'arm swelling'],
             ['Thrombolysis, then', 'rib resection, scalenectomy,', 'venoplasty or repair'], 'over 90 to 95%', 'warn'),
            ('Arterial', '1%', ['Emboli, thrombosis,', 'aneurysm, claudication'],
             ['Arterial reconstruction', 'with first rib resection,', 'anterior scalenectomy'], 'over 90 to 95%', 'warn')]
    b = ''
    for i, (n, share, feat, tx, res, cls) in enumerate(spec):
        x = 10 + i * 236
        b += f'<rect x="{x}" y="10" width="226" height="300" rx="10" class="f-b0"/>'
        b += f'<rect x="{x}" y="10" width="226" height="34" rx="10" class="f-{cls}"/>'
        b += T(x + 113, 32, n, 'f-h')
        b += T(x + 113, 76, share, 'f-big')
        b += T(x + 113, 104, feat, 'f-s')
        b += line(x + 16, 162, x + 210, 162, 'f-grid')
        b += T(x + 113, 186, tx, '')
        b += line(x + 16, 248, x + 210, 248, 'f-grid')
        b += T(x + 113, 276, res, 'f-s')
    b += box(10, 322, 700, 40, 'Decompression: first rib resection plus scalenectomy, transaxillary or supraclavicular', 'ok', 'f-s')
    return svg(372, b)


# ---- figs_D10.py
"""D10 drawings: thoracic inlet, nerve courses, ductus, pericardial sinuses, cardiac veins,
conduction system, cardiac cycle, pressure-volume loops, Frank-Starling, ventricular
interdependence, lung volumes and spirometry."""



# ---------------------------------------------------------------- helpers

def _d10_smooth(pts, cls='f-l', extra=''):
    """Catmull-Rom curve through points, as one path."""
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]
        p1 = pts[i]
        p2 = pts[i + 1]
        p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return f'<path d="{d}" class="{cls}" fill="none"{extra}/>'


def _d10_num(x, y, n, cls='b1'):
    return (f'<circle cx="{x}" cy="{y}" r="11" class="f-{cls}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" class="f-t f-n">{n}</text>')


def _d10_card(x, y, w, h, head, lines, cls='b0', lh=16):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="f-{cls}"/>'
    out += T(x + 10, y + 19, head, 'f-h', 'start')
    for i, s in enumerate(lines):
        out += T(x + 10, y + 37 + i * lh, s, 'f-s', 'start')
    return out


def _d10_axes(x0, y0, w, h, xlab, ylab, ylab_x=None):
    """Plain axes with arrow heads; origin at (x0, y0 + h)."""
    out = arrow(x0, y0 + h, x0 + w, y0 + h) + arrow(x0, y0 + h, x0, y0)
    out += T(x0 + w, y0 + h + 20, xlab, 'f-s', 'end')
    out += T(ylab_x if ylab_x is not None else x0 + 6, y0 - 6, ylab, 'f-s', 'start')
    return out


# ---------------------------------------------------------------- pericardial sinuses (c19)

def d10_pericardial_sinuses():
    """Posterior wall of the pericardial sac with the heart lifted out: the two reflections and the sinuses."""
    b = T(12, 20, "Back wall of the sac, heart lifted out, seen from the front (patient's right on the left)", 'f-s', 'start')
    b += '<rect x="20" y="32" width="430" height="372" rx="26" class="f-track"/>'
    b += '<rect x="20" y="32" width="430" height="372" rx="26" class="f-grid" fill="none"/>'
    # arterial sleeve
    b += '<rect x="140" y="50" width="200" height="60" rx="24" class="f-b1"/>'
    b += '<circle cx="196" cy="80" r="22" class="f-lumen"/>' + T(196, 85, 'Ao', 'f-h')
    b += '<circle cx="284" cy="80" r="22" class="f-lumen"/>' + T(284, 85, 'PA', 'f-h')
    b += T(240, 128, 'arterial reflection', 'f-s')
    # venous reflection (inverted U)
    b += '<path d="M60 160 L420 160 L420 330 L350 330 L350 206 L130 206 L130 380 L60 380 Z" class="f-b1"/>'
    b += T(240, 180, 'venous reflection', 'f-s')
    for cx, cy, r, lab in [(95, 183, 19, 'SVC'), (95, 254, 15, ''), (95, 304, 15, ''), (95, 354, 20, 'IVC'),
                           (385, 236, 15, ''), (385, 290, 15, '')]:
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="f-lumen"/>'
        if lab:
            b += T(cx, cy + 4, lab, 'f-s')
    b += T(140, 258, 'right upper', 'f-s', 'start') + T(140, 308, 'right lower', 'f-s', 'start')
    b += T(340, 240, 'left upper', 'f-s', 'end') + T(340, 294, 'left lower', 'f-s', 'end')
    b += T(240, 284, 'pulmonary veins', 'f-s')
    # oblique sinus
    b += T(240, 338, 'OBLIQUE SINUS', 'f-h') + T(240, 356, 'blind pouch behind', 'f-s') + T(240, 372, 'the left atrium', 'f-s')
    b += arrow(240, 394, 240, 382)
    # transverse sinus
    b += '<line x1="70" y1="137" x2="410" y2="137" class="f-dash" marker-start="url(#ah)" marker-end="url(#ah)"/>'
    b += line(410, 137, 470, 80, 'f-l')
    # right column
    b += _d10_card(470, 32, 240, 118, 'Transverse sinus', [
        'Behind the aorta and pulmonary', 'artery; in front of the SVC and', 'upper pulmonary veins (the gap',
        'between the two reflections)'], 'b1')
    b += line(300, 342, 470, 214, 'f-l')
    b += _d10_card(470, 160, 240, 104, 'Oblique sinus', [
        'Blind pouch behind the left', 'atrium, bounded by the', 'reflections round the pulmonary', 'veins and IVC'], 'b1')
    b += _d10_card(470, 274, 240, 130, 'Surgical use', [
        'A pulmonary artery band is passed', 'through the transverse sinus', '(Congenital 5 and 8)',
        'Homograft root bleeding: close', 'the transverse sinus first;', 'obliterated at redo (Cardiac 8)'], 'b0')
    return svg(414, b)


# ---------------------------------------------------------------- cardiac veins (c19)

def d10_cardiac_veins():
    """Venous drainage of the heart seen from behind: great cardiac vein, coronary sinus, persistent left SVC."""
    b = T(12, 20, "Heart seen from behind (patient's left on the left)", 'f-s', 'start')
    # ventricles
    b += '<path d="M84 242 C76 312 160 382 290 388 C400 392 470 340 500 246 Z" class="f-b0"/>'
    b += T(300, 340, 'Ventricles (diaphragmatic surface)', 'f-s')
    # left atrium and veins
    b += '<ellipse cx="300" cy="146" rx="120" ry="52" class="f-b0"/>' + T(300, 151, 'Left atrium', 'f-h')
    for cx, cy in [(190, 118), (190, 174), (410, 118), (410, 174)]:
        b += f'<circle cx="{cx}" cy="{cy}" r="15" class="f-lumen"/>'
    b += T(190, 94, 'left PVs', 'f-s') + T(410, 94, 'right PVs', 'f-s')
    # right atrium, cavae
    b += '<rect x="518" y="50" width="44" height="76" rx="10" class="f-b0"/>' + T(540, 42, 'SVC', 'f-s')
    b += '<ellipse cx="546" cy="168" rx="56" ry="48" class="f-b0"/>' + T(560, 164, 'Right', 'f-s') + T(560, 180, 'atrium', 'f-s')
    b += '<rect x="518" y="214" width="48" height="76" rx="10" class="f-b0"/>' + T(542, 262, 'IVC', 'f-s')
    # coronary sinus in the posterior AV groove
    b += '<path d="M112 240 C220 236 400 234 510 216" class="f-vessel" style="stroke-width:16"/>'
    b += '<ellipse cx="512" cy="215" rx="8" ry="10" class="f-lumen"/>'
    b += T(300, 270, 'CORONARY SINUS in the posterior AV groove', 'f-h')
    # great cardiac vein coming round the left margin
    b += '<path d="M70 330 C58 300 76 256 112 240" class="f-vessel" style="stroke-width:10"/>'
    b += arrow(70, 362, 70, 340)
    b += T(14, 384, 'Great cardiac vein, coming round the left', 'f-s', 'start')
    b += T(14, 400, 'AV groove from the anterior interventricular vein', 'f-s', 'start')
    # persistent LSVC
    b += '<path d="M112 40 C108 110 108 180 112 234" class="f-vessel" style="stroke-width:9;opacity:.35" stroke-dasharray="10 6"/>'
    b += T(124, 40, ['Persistent left SVC (when present)', 'drains into the coronary sinus'], 'f-s', 'start')
    # retrograde cannula
    b += '<path d="M700 232 C640 226 580 220 520 216" class="f-stent"/>'
    b += T(706, 252, ['Retrograde cardioplegia', 'cannula in the ostium,', 'beside the IVC'], 'f-s', 'end')
    # boxes
    y = 418
    b += box(10, y, 226, 64, ['Coronary veins usually', 'have no valves'], 'b0', 'f-s')
    b += box(247, y, 226, 64, ['Thebesian veins: about 15% of', 'coronary flow straight into', 'the chambers'], 'b1', 'f-s')
    b += box(484, y, 226, 64, ['A left SVC defeats retrograde', 'cardioplegia unless it is', 'controlled'], 'warn', 'f-s')
    return svg(y + 74, b)


# ---------------------------------------------------------------- conduction system (c19)

def d10_conduction():
    """Conduction system in a frontal four-chamber section."""
    b = T(12, 20, "Four-chamber section seen from the front (patient's right on the left)", 'f-s', 'start')
    # chambers
    b += '<path d="M60 76 C56 54 84 46 110 50 L220 60 L220 172 L70 178 C56 150 56 106 60 76 Z" class="f-b0"/>'
    b += '<path d="M262 60 L372 48 C402 44 430 58 426 88 C424 132 414 158 400 174 L262 172 Z" class="f-b0"/>'
    b += '<path d="M70 188 L222 184 L222 404 C150 386 82 306 70 188 Z" class="f-b0"/>'
    b += '<path d="M262 184 L410 186 C402 300 334 392 262 414 Z" class="f-b0"/>'
    b += '<path d="M222 184 L262 184 L262 414 L222 404 Z" class="f-track"/>'
    b += T(160, 112, 'RA', 'f-h') + T(350, 112, 'LA', 'f-h') + T(150, 280, 'RV', 'f-h') + T(330, 260, 'LV', 'f-h')
    # SVC
    b += '<rect x="80" y="28" width="52" height="30" rx="8" class="f-b0"/>' + T(106, 48, 'SVC', 'f-s')
    # central fibrous body
    b += '<rect x="212" y="174" width="60" height="14" rx="6" class="f-b1"/>'
    # SA node
    b += '<ellipse cx="128" cy="62" rx="14" ry="8" class="f-warn"/>'
    # internodal pathways
    b += _d10_smooth([(136, 66), (170, 84), (196, 130), (206, 160)], 'f-nerve', ' stroke-dasharray="6 4"')
    b += _d10_smooth([(126, 70), (118, 120), (160, 156), (202, 166)], 'f-nerve', ' stroke-dasharray="6 4"')
    b += _d10_smooth([(140, 62), (200, 66), (212, 110), (210, 158)], 'f-nerve', ' stroke-dasharray="6 4"')
    # AV node and His
    b += '<ellipse cx="208" cy="166" rx="11" ry="7" class="f-warn"/>'
    b += _d10_smooth([(216, 170), (232, 184), (242, 204)], 'f-nerve', ' style="stroke-width:4"')
    # left bundle
    b += _d10_smooth([(244, 206), (264, 244), (296, 320), (318, 366)], 'f-nerve')
    b += _d10_smooth([(244, 206), (276, 226), (330, 250), (376, 262)], 'f-nerve')
    b += '<ellipse cx="322" cy="374" rx="15" ry="9" class="f-b1"/>' + '<ellipse cx="384" cy="266" rx="15" ry="9" class="f-b1"/>'
    # right bundle down the septum then across the moderator band
    b += _d10_smooth([(240, 208), (232, 270), (222, 332), (180, 352), (124, 322)], 'f-nerve')
    b += '<path d="M222 338 C190 352 150 344 118 320" class="f-l" style="stroke-width:7;opacity:.25"/>'
    b += '<ellipse cx="112" cy="318" rx="14" ry="10" class="f-b1"/>'
    # labels
    b += line(140, 58, 160, 36) + T(164, 38, 'SA node: under the epicardium, lateral to the cavoatrial junction', 'f-s', 'start')
    b += T(456, 66, ['Dashed: three preferential', 'internodal pathways'], 'f-s', 'start')
    b += line(220, 164, 450, 132) + T(456, 128, ['AV node: centre of the', 'triangle of Koch'], 'f-s', 'start')
    b += line(246, 200, 450, 192) + T(456, 186, ['His bundle pierces the right', 'trigone, then runs between', 'membranous and muscular septum'], 'f-s', 'start')
    b += line(386, 266, 450, 266) + T(456, 262, ['Left bundle fans on the left', 'septum: two branches to the', 'papillary muscle bases'], 'f-s', 'start')
    b += line(108, 328, 70, 404) + T(14, 422, 'Right bundle crosses the moderator band to the anterior papillary muscle', 'f-s', 'start')
    # danger boxes
    y = 440
    b += box(10, y, 226, 78, ['Superior septal approach', 'divides the sinus node artery:', 'pacemaker about 12%'], 'warn', 'f-s')
    b += box(247, y, 226, 78, ['Deep sutures below the', 'non-coronary / right commissure', 'cause heart block'], 'warn', 'f-s')
    b += box(484, y, 226, 78, ['Nodal cells rest at minus 60 to 70', 'mV and depolarise spontaneously;', 'ACh and adenosine block the node'], 'b1', 'f-s')
    return svg(y + 88, b)


# ---------------------------------------------------------------- Frank-Starling (c19)

def d10_starling():
    """Frank-Starling curves: stroke volume against end-diastolic volume, three contractile states."""
    x0, y0, w, h = 70, 40, 400, 280
    b = _d10_axes(x0, y0, w, h, 'End-diastolic volume (preload)', 'Stroke volume')

    def curve(top, fall):
        pts = []
        for i in range(0, 41):
            t = i / 40
            v = top * (1 - (1 - t) ** 2.2) if t < 0.7 else top * (1 - 0.3 ** 2.2) - fall * (t - 0.7) ** 1.6
            pts.append((x0 + 10 + t * (w - 30), y0 + h - v))
        return pts
    up = curve(250, 160)
    mid = curve(185, 150)
    lo = curve(120, 110)
    b += _d10_smooth(up, 'f-l', ' style="stroke-width:2.5"')
    b += _d10_smooth(mid, 'f-l', ' style="stroke-width:3"')
    b += _d10_smooth(lo, 'f-dash')
    b += T(up[22][0] - 6, up[22][1] - 10, 'More contractility', 'f-h', 'end')
    b += T(mid[31][0] + 6, mid[31][1] - 12, 'Normal', 'f-h', 'start')
    b += T(lo[14][0] + 4, lo[14][1] + 24, ['Less contractility,', 'or more afterload'], 'f-s', 'start')
    # operating point moves
    pA = mid[12]
    pB = mid[22]
    pC = up[12]
    b += f'<circle cx="{pA[0]:.0f}" cy="{pA[1]:.0f}" r="6" class="f-warn"/>'
    b += f'<circle cx="{pB[0]:.0f}" cy="{pB[1]:.0f}" r="6" class="f-ok"/>'
    b += f'<circle cx="{pC[0]:.0f}" cy="{pC[1]:.0f}" r="6" class="f-b1"/>'
    b += arrow(pA[0] + 8, pA[1] - 3, pB[0] - 8, pB[1] + 3)
    b += arrow(pA[0], pA[1] - 8, pC[0], pC[1] + 9)
    b += T(pB[0] + 10, pB[1] + 24, 'fluid', 'f-s', 'start') + T(pA[0] - 8, pA[1] - 40, 'inotrope', 'f-s', 'end')
    # optimum
    xo = x0 + 10 + 0.7 * (w - 30)
    b += line(xo, y0 + 20, xo, y0 + h, 'f-dash')
    b += T(xo + 6, y0 + 10, ['beyond the optimum', 'length, force falls'], 'f-s', 'start')
    # right column
    b += _d10_card(494, 40, 216, 120, 'Moving along a curve', [
        'More venous return stretches', 'the sarcomere: more force', '(Frank-Starling). Filling raises',
        'output when preload is low'], 'ok')
    b += _d10_card(494, 170, 216, 126, 'Moving to another curve', [
        'Contractility: same EDV, lower', 'ESV, bigger SV. Up: adrenergic', 'agonists, faster rate, digoxin.',
        'Down: ACh, calcium blockers;', 'more afterload lowers SV'], 'b1')
    b += box(70, 344, 640, 44, 'At rest only 20 to 25% of actin-myosin cross-bridges are engaged: the rest is cardiac reserve', 'b0', 'f-s')
    return svg(398, b)


# ---------------------------------------------------------------- pressure-volume loops

def _d10_pv(ox, oy, sx, sy, edv, esv, edp, p_open, p_peak, p_close, p_min=2, ivc_slant=0, ivr_slant=0, fill_steep=1.0, v0=0):
    """Path for a PV loop. Volumes and pressures are schematic units; (ox, oy) is volume v0, pressure 0."""
    X = lambda v: ox + (v - v0) * sx
    Y = lambda p: oy - p * sy
    pts_eject = []
    for i in range(0, 21):
        t = i / 20
        v = (edv - ivc_slant) - t * ((edv - ivc_slant) - (esv + ivr_slant))
        p = p_open + (p_peak - p_open) * (1 - (1 - 2 * t) ** 2) if t < 0.5 else p_peak - (p_peak - p_close) * ((t - 0.5) / 0.5) ** 1.6
        pts_eject.append((X(v), Y(p)))
    fill = []
    for i in range(0, 21):
        t = i / 20
        v = esv + t * (edv - esv)
        p = p_min + (edp - p_min) * (t ** (2.2 * fill_steep))
        fill.append((X(v), Y(p)))
    d = f'M{X(edv):.1f} {Y(edp):.1f} L{X(edv - ivc_slant):.1f} {Y(p_open):.1f}'
    for x, y in pts_eject[1:]:
        d += f' L{x:.1f} {y:.1f}'
    d += f' L{X(esv):.1f} {Y(p_min):.1f}'
    for x, y in fill[1:]:
        d += f' L{x:.1f} {y:.1f}'
    return d + ' Z', X, Y


def d10_pv_normal():
    """Normal left ventricular pressure-volume loop with its four phases, plus preload, contractility and afterload changes."""
    ox, oy, sx, sy = 70, 330, 2.6, 2.1
    v0 = 20
    b = _d10_axes(ox, 50, 330, 280, '', 'LV pressure (mmHg)')
    b += T(ox + 334, oy + 4, 'LV volume', 'f-s', 'start')
    norm = dict(edv=140, esv=60, edp=7, p_open=80, p_peak=122, p_close=100)
    d, X, Y = _d10_pv(ox, oy, sx, sy, v0=v0, **norm)
    b += f'<path d="{d}" class="f-b1"/>'
    b += f'<path d="{d}" class="f-l" style="stroke-width:2.5"/>'
    for p in (120, 80):
        b += line(ox - 5, Y(p), ox, Y(p)) + T(ox - 8, Y(p) + 4, str(p), 'f-s', 'end')
        b += line(ox, Y(p), X(150), Y(p), 'f-grid')
    b += T(ox - 8, Y(5) + 4, '5', 'f-s', 'end')
    for (v, p) in [(140, 7), (140, 80), (60, 100), (60, 2)]:
        b += f'<circle cx="{X(v):.1f}" cy="{Y(p):.1f}" r="5" class="f-warn"/>'
    b += T(X(140) + 8, Y(7) - 4, 'MV closes', 'f-s', 'start')
    b += T(X(140) + 8, Y(80) + 4, 'AV opens', 'f-s', 'start')
    b += T(X(60) - 8, Y(100) - 6, ['AV closes', '(dicrotic', 'notch)'], 'f-s', 'end')
    b += T(X(60) - 8, Y(2) - 6, 'MV opens', 'f-s', 'end')
    b += T(X(100), Y(132), 'Ejection', 'f-h')
    b += T(X(100), Y(14), 'Filling', 'f-h')
    b += T(X(140) - 8, Y(44), ['Isovolumic', 'contraction'], 'f-h', 'end')
    b += T(X(60) + 8, Y(44), ['Isovolumic', 'relaxation'], 'f-h', 'start')
    b += line(X(60), oy + 4, X(60), oy + 10) + line(X(140), oy + 4, X(140), oy + 10)
    b += T(X(60), oy + 26, 'ESV', 'f-n') + T(X(140), oy + 26, 'EDV', 'f-n')
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>' % (X(60) + 3, oy + 40, X(140) - 3, oy + 40)
    b += T(X(100), oy + 58, 'Stroke volume = EDV minus ESV', 'f-s')

    def mini(y, title, notes, kw):
        mx, my, msx, msy = 476, y + 112, 1.1, 0.58
        out = T(470, y + 12, title, 'f-h', 'start')
        dn, _, _ = _d10_pv(mx, my, msx, msy, v0=40, **norm)
        out += f'<path d="{dn}" class="f-dash"/>'
        dc, _, _ = _d10_pv(mx, my, msx, msy, v0=40, **kw)
        out += f'<path d="{dc}" class="f-l" style="stroke-width:2.2"/>'
        out += line(mx, my, mx + 150, my, 'f-grid')
        for i, s in enumerate(notes):
            out += T(636, y + 44 + i * 15, s, 'f-s', 'start')
        return out
    b += mini(20, 'More preload', ['EDV up,', 'SV up', '(Starling)'], dict(edv=165, esv=62, edp=10, p_open=80, p_peak=126, p_close=102))
    b += mini(150, 'More contractility', ['ESV down,', 'EDV same,', 'SV up'], dict(edv=140, esv=42, edp=7, p_open=80, p_peak=134, p_close=104))
    b += mini(280, 'More afterload', ['SV down', '(preload and', 'contractility', 'constant)'], dict(edv=140, esv=82, edp=7, p_open=100, p_peak=142, p_close=126))
    b += T(470, 416, 'Dashed: normal loop', 'f-s', 'start')
    return svg(426, b)


def d10_pv_valves():
    """Pressure-volume loops in aortic stenosis, acute and chronic aortic regurgitation and acute mitral regurgitation."""
    b = ''
    panels = [
        (10, 10, 'Aortic stenosis', dict(edv=140, esv=62, edp=18, p_open=96, p_peak=196, p_close=160),
         ['Higher LV systolic', 'and diastolic', 'pressures; longer', 'ejection;', 'hypertrophy from', 'wall stress'], ['LVEF trigger', 'under 50%']),
        (365, 10, 'Acute aortic regurgitation', dict(edv=178, esv=70, edp=34, p_open=76, p_peak=118, p_close=96, ivr_slant=-10, fill_steep=0.6),
         ['Sudden rise in EDV;', 'steep rise in', 'LVEDP: pulmonary', 'oedema; forward', 'SV falls'], ['Acute severe:', 'early surgery']),
        (10, 270, 'Chronic aortic regurgitation', dict(edv=220, esv=96, edp=11, p_open=56, p_peak=146, p_close=110, ivr_slant=-10),
         ['LV enlarges; large', 'total SV; wide', 'pulse pressure', '(aortic diastolic', 'falls)'], ['LVEF trigger', '50% or less']),
        (365, 270, 'Acute mitral regurgitation', dict(edv=145, esv=44, edp=12, p_open=40, p_peak=112, p_close=60, ivc_slant=14, ivr_slant=-8),
         ['No true isovolumic', 'phases: ejects into', 'the atrium at once;', 'ESV falls, EF high,', 'forward output low'], ['Primary MR trigger', '60% or less']),
    ]
    norm = dict(edv=140, esv=60, edp=7, p_open=80, p_peak=122, p_close=100)
    for (px, py, title, kw, notes, trig) in panels:
        b += f'<rect x="{px}" y="{py}" width="345" height="250" rx="10" class="f-b0"/>'
        b += T(px + 12, py + 22, title, 'f-h', 'start')
        ox, oy, sx, sy = px + 22, py + 226, 0.92, 0.84
        b += arrow(ox, oy, ox + 190, oy) + arrow(ox, oy, ox, py + 40)
        b += T(ox + 190, oy + 16, 'volume', 'f-s', 'end') + T(ox + 6, py + 46, 'pressure', 'f-s', 'start')
        dn, _, _ = _d10_pv(ox, oy, sx, sy, v0=30, **norm)
        b += f'<path d="{dn}" class="f-dash"/>'
        d, _, _ = _d10_pv(ox, oy, sx, sy, v0=30, **kw)
        b += f'<path d="{d}" class="f-l" style="stroke-width:2.5"/>'
        for i, s in enumerate(notes):
            b += T(px + 218, py + 50 + i * 16, s, 'f-s', 'start')
        b += f'<rect x="{px + 212}" y="{py + 184}" width="124" height="52" rx="7" class="f-warn"/>'
        b += T(px + 274, py + 206, trig, 'f-s')
    b += box(10, 532, 700, 74, ['Dashed: normal loop. The ejection fraction that counts as abnormal rises from 50% in AS',
                                'to 60% in primary MR: in MR part of the stroke volume goes into the low-pressure atrium,',
                                'so EF overstates function (that reasoning is from memory in Cardiac 1)'], 'b1', 'f-s')
    return svg(616, b)


# ---------------------------------------------------------------- Wiggers cardiac cycle (c19)

def d10_wiggers():
    """One cardiac cycle: aortic, LV and LA pressure, LV volume and ECG, with valve events and timing marks."""
    X = lambda t: 92 + 560 * t
    PY = lambda p: 236 - p * 1.3
    b = ''
    # phase band
    phases = [(0.0, 0.02, None), (0.02, 0.09, 'IC'), (0.09, 0.38, 'Ejection'), (0.38, 0.47, 'IR'), (0.47, 1.0, 'Filling')]
    for t0, t1, lab in phases:
        if lab is None:
            continue
        cls = 'f-b1' if lab in ('IC', 'IR') else 'f-b0'
        b += f'<rect x="{X(t0):.1f}" y="30" width="{X(t1) - X(t0):.1f}" height="22" class="{cls}"/>'
        b += T((X(t0) + X(t1)) / 2, 46, lab, 'f-s' if lab in ('IC', 'IR') else 'f-h')
    b += f'<rect x="{X(0.82):.1f}" y="54" width="{X(0.96) - X(0.82):.1f}" height="16" rx="4" class="f-ok"/>'
    b += T((X(0.82) + X(0.96)) / 2, 66, 'atrial kick', 'f-s')
    b += T(14, 46, 'Phase', 'f-s', 'start')
    # event lines
    ev = [(0.02, 'MV closes'), (0.09, 'AV opens'), (0.38, 'AV closes'), (0.47, 'MV opens')]
    for i, (t, lab) in enumerate(ev):
        b += line(X(t), 72, X(t), 470, 'f-dash')
    b += T(X(0.02) - 4, 24, 'MV closes', 'f-s', 'end') + T(X(0.09) + 4, 24, 'AV opens', 'f-s', 'start')
    b += T(X(0.38) - 4, 24, 'AV closes', 'f-s', 'end') + T(X(0.47) + 4, 24, 'MV opens', 'f-s', 'start')
    # pressure axis
    b += line(80, 72, 80, 240, 'f-grid')
    for p in (120, 80, 10):
        b += T(76, PY(p) + 4, str(p), 'f-s', 'end') + line(80, PY(p), 660, PY(p), 'f-grid')
    b += T(14, 150, ['Pressure', 'mmHg'], 'f-s', 'start')
    # aortic pressure
    ao = [(0.0, 82), (0.05, 80.5), (0.09, 80), (0.14, 102), (0.21, 121), (0.3, 114), (0.37, 101), (0.385, 96), (0.40, 101), (0.46, 98), (0.6, 92), (0.8, 86), (1.0, 81)]
    b += _d10_smooth([(X(t), PY(p)) for t, p in ao], 'f-l', ' style="stroke-width:2"')
    # LV pressure
    lv = [(0.0, 8), (0.02, 10), (0.05, 40), (0.09, 81), (0.14, 105), (0.21, 123), (0.3, 116), (0.37, 101), (0.40, 70), (0.44, 20), (0.47, 4), (0.52, 2), (0.65, 4), (0.82, 5), (0.9, 8), (0.95, 7), (1.0, 9)]
    b += _d10_smooth([(X(t), PY(p)) for t, p in lv], 'f-l', ' style="stroke-width:3"')
    # LA pressure
    la = [(0.0, 9), (0.03, 11), (0.07, 7), (0.2, 7), (0.35, 10), (0.45, 13), (0.52, 7), (0.7, 8), (0.88, 11), (0.95, 9), (1.0, 9)]
    b += _d10_smooth([(X(t), PY(p)) for t, p in la], 'f-dash', ' style="stroke-width:1.8"')
    b += T(X(0.25), PY(121) - 8, 'Aorta 120/80', 'f-s')
    b += T(X(0.215), PY(60), 'LV 120/5', 'f-h', 'end')
    b += T(X(0.88), PY(11) - 8, 'a', 'f-h') + T(X(0.45) + 8, PY(13) - 6, 'v', 'f-h')
    b += T(X(0.62), PY(8) - 6, 'LA (dashed)', 'f-s')
    b += T(X(0.385) + 8, PY(96) + 18, 'dicrotic notch', 'f-s', 'start')
    # volume
    vy = lambda v: 362 - v * 0.55
    b += T(14, 300, ['LV', 'volume'], 'f-s', 'start')
    vol = [(0.0, 140), (0.09, 140), (0.2, 100), (0.32, 68), (0.38, 60), (0.47, 60), (0.55, 100), (0.65, 118), (0.8, 124), (0.9, 128), (0.96, 140), (1.0, 140)]
    b += _d10_smooth([(X(t), vy(v)) for t, v in vol], 'f-l', ' style="stroke-width:2.5"')
    b += T(X(0.05) + 14, vy(140) - 8, 'EDV', 'f-n') + T(X(0.425), vy(60) + 18, 'ESV', 'f-n')
    # ECG
    ey = 430
    ecg = [(0.0, 0), (0.005, -40), (0.02, 10), (0.04, 0), (0.24, 0), (0.30, -16), (0.36, 0), (0.84, 0), (0.88, -8), (0.92, 0), (0.995, 0), (1.0, -40)]
    d = 'M%.1f %.1f' % (X(-0.03), ey)
    for t, v in ecg:
        d += ' L%.1f %.1f' % (X(t), ey + v)
    b += f'<path d="{d}" class="f-l" fill="none" style="stroke-width:2"/>'
    b += T(X(0.005), ey - 46, 'R', 'f-h') + T(X(1.0), ey - 46, 'R', 'f-h') + T(X(0.30), ey - 22, 'T', 'f-h') + T(X(0.88), ey - 14, 'P', 'f-h')
    b += T(14, ey + 4, 'ECG', 'f-s', 'start')
    # R-R percentages
    ry = 484
    b += line(X(0), ry, X(1), ry, 'f-l')
    for t, lab in [(0, '0%'), (1, '100%')]:
        b += line(X(t), ry - 5, X(t), ry + 5) + T(X(t), ry + 20, lab, 'f-s')
    b += f'<rect x="{X(0.35):.1f}" y="{ry - 7}" width="{X(0.45) - X(0.35):.1f}" height="14" rx="4" class="f-warn"/>'
    b += f'<rect x="{X(0.70):.1f}" y="{ry - 7}" width="{X(0.80) - X(0.70):.1f}" height="14" rx="4" class="f-ok"/>'
    b += T(X(0.40), ry + 22, 'end-systole 35-45%', 'f-s') + T(X(0.75), ry + 22, 'mid-diastole 70-80%', 'f-s')
    b += T(14, ry + 4, 'R to R', 'f-s', 'start')
    # bottom boxes
    y = 522
    b += box(10, y, 226, 78, ['Balloon pump: inflate at the', 'dicrotic notch (mid T wave),', 'deflate at the R wave'], 'b1', 'f-s')
    b += box(247, y, 226, 78, ['Faster rate shortens diastole:', 'filling is lost at about 150 to', '180 a minute'], 'warn', 'f-s')
    b += box(484, y, 226, 78, ['Atrial contraction gives about', '20% of filling; losing it can cut', 'output by up to 20%'], 'ok', 'f-s')
    b += T(14, y + 100, 'IC, IR: isovolumic contraction and relaxation. Gating windows are the CT phases in Cardiac 9.', 'f-s', 'start')
    return svg(y + 110, b)


# ---------------------------------------------------------------- ventricular interdependence (c19)

def d10_interdependence():
    """Shared septum: normal and pressure-loaded RV in short axis, respiratory discordance, and the RV ischaemia spiral."""
    b = ''
    # short-axis sections
    def section(cx, cy, loaded):
        out = ''
        if not loaded:
            out += f'<path d="M{cx - 6} {cy - 62} C{cx - 70} {cy - 70} {cx - 112} {cy - 20} {cx - 108} {cy + 16} C{cx - 100} {cy + 56} {cx - 50} {cy + 70} {cx - 6} {cy + 60} C{cx - 30} {cy + 30} {cx - 30} {cy - 30} {cx - 6} {cy - 62} Z" class="f-b0"/>'
            out += f'<circle cx="{cx + 26}" cy="{cy}" r="64" class="f-b0"/>'
            out += f'<circle cx="{cx + 26}" cy="{cy}" r="42" class="f-lumen"/>'
            out += T(cx - 66, cy + 4, 'RV', 'f-h') + T(cx + 26, cy + 4, 'LV', 'f-h')
        else:
            out += f'<path d="M{cx + 30} {cy - 66} C{cx - 60} {cy - 92} {cx - 140} {cy - 40} {cx - 132} {cy + 20} C{cx - 120} {cy + 74} {cx - 40} {cy + 92} {cx + 30} {cy + 66} C{cx + 14} {cy + 30} {cx + 14} {cy - 30} {cx + 30} {cy - 66} Z" class="f-warn"/>'
            out += f'<path d="M{cx + 30} {cy - 66} C{cx + 90} {cy - 80} {cx + 120} {cy - 30} {cx + 120} {cy} C{cx + 120} {cy + 30} {cx + 90} {cy + 80} {cx + 30} {cy + 66} C{cx + 14} {cy + 30} {cx + 14} {cy - 30} {cx + 30} {cy - 66} Z" class="f-b0"/>'
            out += f'<path d="M{cx + 40} {cy - 44} C{cx + 86} {cy - 50} {cx + 100} {cy - 20} {cx + 100} {cy} C{cx + 100} {cy + 20} {cx + 86} {cy + 50} {cx + 40} {cy + 44} C{cx + 32} {cy + 20} {cx + 32} {cy - 20} {cx + 40} {cy - 44} Z" class="f-lumen"/>'
            out += T(cx - 60, cy + 4, 'RV', 'f-h') + T(cx + 70, cy + 4, 'LV', 'f-h')
            out += arrow(cx - 20, cy, cx + 14, cy)
        return out
    b += T(12, 20, 'Short axis, patient’s right on the left', 'f-s', 'start')
    b += section(130, 120, False) + T(130, 212, 'Normal', 'f-h')
    b += section(380, 120, True) + T(370, 212, 'RV dilated and pressure-loaded', 'f-h')
    b += T(370, 230, 'leftward septal shift, TR', 'f-s')
    b += _d10_card(520, 34, 190, 186, 'Shifts the septum', [
        'RV-PA uncoupling: volume,', 'ischaemia, more venous', 'return after LVAD start',
        'LVAD speed too high:', 'suction, septal shift and', 'RV failure',
        'Pulmonary embolism:', 'RV dilatation, septal shift'], 'b0')
    # respiratory discordance traces
    y0 = 262
    b += T(12, y0, 'Respiration and systolic pressures at catheter', 'f-h', 'start')

    def traces(x, title, disc):
        out = T(x + 150, y0 + 26, title, 'f-h')
        out += f'<rect x="{x + 40}" y="{y0 + 36}" width="110" height="96" class="f-track"/>'
        out += T(x + 95, y0 + 148, 'inspiration', 'f-s') + T(x + 205, y0 + 148, 'expiration', 'f-s')
        lv = [(x, y0 + 60), (x + 40, y0 + 60), (x + 95, y0 + 80), (x + 150, y0 + 60), (x + 205, y0 + 52), (x + 300, y0 + 58)]
        rv = [(x, y0 + 108), (x + 40, y0 + 108), (x + 95, (y0 + 92) if disc else (y0 + 122)), (x + 150, y0 + 108), (x + 205, (y0 + 116) if disc else (y0 + 102)), (x + 300, y0 + 110)]
        out += _d10_smooth(lv, 'f-l', ' style="stroke-width:2.5"') + _d10_smooth(rv, 'f-dash', ' style="stroke-width:2.2"')
        out += T(x + 304, y0 + 62, 'LV', 'f-s', 'start') + T(x + 304, y0 + 114, 'RV', 'f-s', 'start')
        return out
    b += traces(14, 'Constriction: opposite directions', True)
    b += traces(372, 'Restriction: move together', False)
    # spiral
    y1 = 432
    b += T(12, y1, 'Why systemic hypotension sinks a pressure-loaded RV', 'f-h', 'start')
    s = [('RV systolic pressure', 'nears systemic'), ('RV perfusion depends', 'on aortic pressure'),
         ('Systemic', 'hypotension'), ('RV ischaemia', 'and failure')]
    for i, (a1, a2) in enumerate(s):
        x = 10 + i * 178
        b += box(x, y1 + 12, 160, 50, [a1, a2], 'warn' if i == 3 else 'b1', 'f-s')
        if i < 3:
            b += arrow(x + 161, y1 + 37, x + 177, y1 + 37)
    return svg(y1 + 72, b)


# ---------------------------------------------------------------- nerve courses (c19)

def d10_nerve_courses():
    """Phrenic, vagus and recurrent laryngeal nerves in the mediastinum, front view."""
    b = T(12, 20, "Front view (patient's right on the left); dashed nerve = behind other structures", 'f-s', 'start')
    # trachea and bronchi
    b += '<path d="M348 44 L372 44 L372 222 L420 286 L404 296 L360 240 L316 296 L300 286 L348 222 Z" class="f-b0"/>'
    # hila
    b += '<ellipse cx="190" cy="318" rx="38" ry="44" class="f-b0"/>' + T(166, 322, 'R hilum', 'f-s')
    b += '<ellipse cx="530" cy="318" rx="38" ry="44" class="f-b0"/>' + T(552, 322, 'L hilum', 'f-s')
    # great veins
    b += '<path d="M264 142 L264 290" class="f-vessel" style="stroke-width:22;opacity:.3"/>' + T(264, 308, 'SVC', 'f-s')
    b += '<path d="M508 92 C430 110 330 128 270 142" class="f-vessel" style="stroke-width:13;opacity:.3"/>'
    b += '<path d="M196 82 C226 100 250 122 264 142" class="f-vessel" style="stroke-width:13;opacity:.3"/>'
    b += T(514, 86, 'L brachiocephalic v.', 'f-s', 'start')
    # aorta, branches, pulmonary artery
    b += '<path d="M330 380 C326 290 330 212 376 196 C424 180 454 210 454 262 L454 420" class="f-vessel" style="stroke-width:22"/>'
    b += '<path d="M346 206 L304 150 L190 124" class="f-vessel" style="stroke-width:8"/>'
    b += '<path d="M428 192 L434 54" class="f-vessel" style="stroke-width:8"/>'
    b += T(440, 50, 'L subclavian a.', 'f-s', 'start')
    b += T(330, 400, 'Ao', 'f-s')
    b += '<path d="M372 380 C384 330 420 306 500 310" class="f-vessel" style="stroke-width:16;opacity:.35"/>' + T(400, 360, 'PA', 'f-s')
    b += '<path d="M436 232 L446 300" class="f-duct"/>'
    # right phrenic: inlet, lateral SVC, in front of hilum
    b += _d10_smooth([(232, 40), (236, 100), (248, 150), (248, 230), (220, 300), (206, 380), (204, 440)], 'f-nerve')
    # left phrenic: over the arch, in front of hilum
    b += _d10_smooth([(498, 40), (490, 110), (480, 190), (500, 260), (520, 330), (526, 440)], 'f-nerve')
    # right vagus: in front of R subclavian, recurrent hooks under it; trunk passes behind the hilum
    b += _d10_smooth([(292, 40), (286, 100), (276, 136)], 'f-nerve')
    b += _d10_smooth([(276, 136), (246, 200), (204, 300), (196, 380), (196, 440)], 'f-nerve', ' stroke-dasharray="6 4"')
    b += _d10_smooth([(272, 132), (262, 146), (250, 136), (276, 112), (318, 70), (340, 44)], 'f-nerve')
    # left vagus: in front of the arch, recurrent under the ligament
    b += _d10_smooth([(410, 40), (420, 120), (438, 190), (452, 236)], 'f-nerve')
    b += _d10_smooth([(452, 236), (476, 290), (512, 350), (516, 440)], 'f-nerve', ' stroke-dasharray="6 4"')
    b += _d10_smooth([(448, 250), (452, 304), (436, 312), (414, 250), (392, 140), (380, 44)], 'f-nerve', ' stroke-dasharray="6 4"')
    # left labels
    b += line(236, 104, 130, 70) + T(14, 60, ['R phrenic: behind', 'the ITA at the inlet'], 'f-s', 'start')
    b += line(256, 144, 130, 142) + T(14, 132, ['R recurrent hooks', 'round the R subclavian'], 'f-s', 'start')
    b += line(248, 210, 130, 214) + T(14, 204, ['R phrenic on the lateral', 'surface of the SVC'], 'f-s', 'start')
    b += line(216, 300, 130, 276) + T(14, 268, ['passes in front', 'of the hilum'], 'f-s', 'start')
    b += line(198, 370, 130, 376) + T(14, 370, ['R vagus behind', 'the hilum'], 'f-s', 'start')
    # right labels
    b += line(482, 170, 590, 150) + T(596, 146, ['L phrenic', 'over the arch'], 'f-s', 'start')
    b += line(436, 186, 590, 204) + T(596, 200, ['L vagus crosses', 'in front of the arch'], 'f-s', 'start')
    b += line(442, 270, 590, 258) + T(596, 254, ['Ligamentum', 'arteriosum'], 'f-s', 'start')
    b += line(440, 310, 590, 312) + T(596, 308, ['L recurrent', 'hooks under it'], 'f-s', 'start')
    b += line(514, 380, 590, 376) + T(596, 370, ['L vagus behind', 'the hilum'], 'f-s', 'start')
    # danger boxes
    y = 456
    b += box(10, y, 170, 78, ['ITA harvest:', 'phrenic behind', 'the ITA'], 'warn', 'f-s')
    b += box(186, y, 170, 78, ['Bicaval cannulation:', 'diathermy on the SVC', 'can hit the R phrenic'], 'warn', 'f-s')
    b += box(362, y, 170, 78, ['Distal arch dissection:', 'L vagus and', 'L recurrent'], 'warn', 'f-s')
    b += box(538, y, 172, 78, ['Mediastinoscopy: no', 'cautery on the left of', 'the airway (L recurrent)'], 'warn', 'f-s')
    b += T(360, y + 100, 'Both recurrent nerves ascend in the tracheo-oesophageal groove; the phrenics run 1.5 cm in front of the hila', 'f-s')
    b += T(360, y + 118, 'Strong red: aorta, subclavian arteries; pale: SVC, brachiocephalic veins, PA; green: ligamentum arteriosum', 'f-s')
    return svg(y + 128, b)


# ---------------------------------------------------------------- pharyngeal arches, duct and recurrent nerves (g6)

def d10_arch_derivatives():
    """Fate of the paired aortic arches, the ductus from the left sixth, and why the recurrent nerves hook differently."""
    b = T(12, 20, "Paired arches from the front (patient's right on the left), aortic sac in the middle; dashed = regresses", 'f-s', 'start')
    mid, xr, xl = 360, 150, 570
    ys = {1: 64, 2: 104, 3: 150, 4: 200, 5: 244, 6: 290}
    # aortic sac
    b += f'<rect x="{mid - 18}" y="52" width="36" height="270" rx="12" class="f-b1"/>'
    b += T(mid, 336, 'sac', 'f-s')
    # dorsal aortae
    b += line(xr, 52, xr, 380, 'f-grid') + line(xl, 52, xl, 380, 'f-grid')
    b += T(xr, 396, 'R dorsal aorta', 'f-s') + T(xl, 396, 'L dorsal aorta', 'f-s')
    fates = {
        1: ('Largely regress (maxillary)', 'Largely regress (maxillary)', 'dash', 'dash'),
        2: ('Largely regress (stapedial)', 'Largely regress (stapedial)', 'dash', 'dash'),
        3: ('Common and proximal ICA', 'Common and proximal ICA', 'solid', 'solid'),
        4: ('Proximal R subclavian', 'Arch: L carotid to L subclavian', 'solid', 'solid'),
        5: ('Regresses', 'Regresses', 'dash', 'dash'),
    }
    for n in range(1, 6):
        lr, ll, sr, sl = fates[n]
        y = ys[n]
        b += line(xr, y, mid - 18, y, 'f-dash' if sr == 'dash' else 'f-l') if sr == 'dash' else f'<line x1="{xr}" y1="{y}" x2="{mid - 18}" y2="{y}" class="f-l" style="stroke-width:5"/>'
        b += line(mid + 18, y, xl, y, 'f-dash' if sl == 'dash' else 'f-l') if sl == 'dash' else f'<line x1="{mid + 18}" y1="{y}" x2="{xl}" y2="{y}" class="f-l" style="stroke-width:5"/>'
        b += T((xr + mid - 18) / 2, y - 7, lr, 'f-s') + T((xl + mid + 18) / 2, y - 7, ll, 'f-s')
        b += _d10_num(mid, y, n)
    # sixth arch
    y6 = ys[6]
    b += f'<line x1="{mid - 18}" y1="{y6}" x2="250" y2="{y6}" class="f-l" style="stroke-width:5"/>' + line(250, y6, xr, y6, 'f-dash')
    b += T(300, y6 - 7, 'Proximal RPA', 'f-s') + T(200, y6 - 7, 'distal: regresses', 'f-s')
    b += f'<line x1="{mid + 18}" y1="{y6}" x2="470" y2="{y6}" class="f-l" style="stroke-width:5"/>'
    b += f'<line x1="470" y1="{y6}" x2="{xl}" y2="{y6}" class="f-duct" style="stroke-width:7"/>'
    b += T(424, y6 - 7, 'Proximal LPA', 'f-s') + T(520, y6 - 7, 'DUCTUS', 'f-h')
    b += _d10_num(mid, y6, 6)
    # seventh intersegmental
    b += f'<line x1="{xr}" y1="352" x2="{xr - 34}" y2="352" class="f-l" style="stroke-width:5"/>'
    b += f'<line x1="{xl}" y1="352" x2="{xl + 34}" y2="352" class="f-l" style="stroke-width:5"/>'
    b += T(xr + 8, 357, '7th intersegmental: subclavian', 'f-s', 'start') + T(xl - 8, 357, '7th intersegmental: subclavian', 'f-s', 'end')
    # vagi and recurrent nerves
    b += line(108, 40, 108, 330, 'f-nerve') + line(612, 40, 612, 330, 'f-nerve')
    b += _d10_smooth([(108, 212), (120, 214), (160, 216), (170, 200), (150, 186), (128, 120), (126, 40)], 'f-nerve')
    b += _d10_smooth([(612, 300), (600, 304), (560, 306), (548, 290), (566, 276), (592, 200), (594, 40)], 'f-nerve')
    b += T(100, 36, 'R vagus', 'f-s', 'end') + T(620, 36, 'L vagus', 'f-s', 'start')
    b += T(100, 228, ['R recurrent', 'under the 4th', '(subclavian)'], 'f-s', 'end')
    b += T(620, 318, ['L recurrent', 'under the 6th', '(duct)'], 'f-s', 'start')
    # boxes
    y = 410
    b += _d10_card(10, y, 226, 112, 'Ductus arteriosus', ['Persistent left 6th arch: aortic end', 'distal to the L subclavian,', 'pulmonary end at the main and',
                                                     'left PA junction'], 'ok')
    b += _d10_card(247, y, 226, 112, 'Closure', ['Smooth muscle contracts as oxygen', 'rises and prostaglandin falls:', '90% closed at 48 hours, then',
                                            'fibroses over months'], 'b0')
    b += _d10_card(484, y, 226, 112, 'Recurrent nerves', ['Pulled down by the lowest', 'persistent arch: duct on the left;', 'R subclavian (4th) on the right,',
                                                     'as the R 6th and 5th regress'], 'b1')
    return svg(y + 122, b)


# ---------------------------------------------------------------- thoracic outlet (t19)

def d10_thoracic_outlet():
    """Right thoracic outlet in sagittal section: vein in front of anterior scalene, artery and plexus behind."""
    b = T(12, 20, 'Sagittal section across the first rib, front to the left (arrangement schematic)', 'f-s', 'start')
    # first rib
    b += '<rect x="130" y="256" width="470" height="28" rx="12" class="f-b0"/>' + T(560, 275, 'First rib', 'f-h', 'end')
    # clavicle and subclavius
    b += '<ellipse cx="180" cy="104" rx="60" ry="28" class="f-b0"/>' + T(180, 109, 'Clavicle', 'f-h')
    b += '<ellipse cx="196" cy="154" rx="44" ry="18" class="f-b1"/>' + T(196, 159, 'Subclavius', 'f-s')
    # scalenes
    b += '<path d="M282 256 L318 256 L344 40 L316 40 Z" class="f-b1"/>'
    b += '<path d="M448 256 L506 256 L500 40 L462 40 Z" class="f-b1"/>'
    b += T(330, 34, 'Anterior scalene', 'f-s', 'end') + T(482, 34, 'Middle scalene', 'f-s')
    # interscalene triangle
    b += '<path d="M322 252 L444 252 L400 110 Z" class="f-dash"/>'
    # vein, artery, plexus
    b += '<circle cx="230" cy="226" r="27" class="f-lumen"/>' + T(230, 231, 'V', 'f-h')
    b += '<circle cx="356" cy="236" r="18" class="f-warn"/>' + T(356, 241, 'A', 'f-h')
    for cx, cy in [(384, 196), (404, 172), (420, 148)]:
        b += f'<circle cx="{cx}" cy="{cy}" r="10" class="f-b0"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="4" class="f-ah"/>'
    # phrenic and long thoracic
    b += '<circle cx="316" cy="84" r="6" class="f-warn"/>'
    b += '<path d="M486 60 C478 120 470 170 462 236" class="f-nerve"/>'
    # labels
    b += line(230, 253, 230, 300) + T(150, 316, ['Subclavian vein: in', 'front of anterior scalene'], 'f-s', 'start')
    b += line(356, 254, 356, 300) + T(310, 316, ['Subclavian artery:', 'behind it, with the plexus'], 'f-s', 'start')
    b += line(428, 146, 600, 120) + T(606, 116, ['Brachial', 'plexus'], 'f-s', 'start')
    b += line(309, 82, 112, 54) + T(12, 46, ['Phrenic n. on', 'the front of', 'anterior scalene'], 'f-s', 'start')
    b += line(476, 120, 600, 178) + T(606, 174, ['Long thoracic', 'n. pierces middle', 'scalene'], 'f-s', 'start')
    b += line(104, 136, 104, 252, 'f-l') + line(98, 136, 110, 136) + line(98, 252, 110, 252)
    b += _d10_num(104, 194, 2, 'warn')
    b += _d10_num(398, 226, 1, 'warn')
    b += T(400, 92, 'interscalene', 'f-s') + T(400, 106, 'triangle', 'f-s')
    # site boxes
    y = 356
    b += _d10_card(10, y, 226, 112, '1 Interscalene triangle', ['Anterior and middle scalene and', 'the first rib. Anterior scalene', 'hypertrophy: plexus or artery'], 'b1')
    b += _d10_card(247, y, 226, 112, '2 Costoclavicular space', ['Clavicle to first rib; narrowed', 'by subclavius or scalene', 'hypertrophy. Costoclavicular', 'test: shoulders down and back'], 'b1')
    b += _d10_card(484, y, 226, 112, '3 Subcoracoid space', ['Under pectoralis minor, more', 'lateral (not in this section).', 'FRCS Atlas draft, not checked'], 'b0')
    b += box(10, y + 122, 700, 44, ['Cervical rib also implicated. Decompression: first rib resection plus scalenectomy, transaxillary or supraclavicular'], 'warn', 'f-s')
    return svg(y + 176, b)


# ---------------------------------------------------------------- lung volumes (t17)

def d10_lung_volumes():
    """Spirometer trace with the four volumes and the three capacities."""
    Y = lambda f: 330 - f * 280
    rv, frc, tv, tlc = 0.30, 0.50, 0.60, 1.0
    b = line(60, Y(0), 470, Y(0), 'f-grid') + T(56, Y(0) + 4, '0', 'f-s', 'end')
    b += T(14, 36, 'Volume', 'f-s', 'start')
    pts = []
    x = 130
    # tidal breaths
    for i in range(3):
        pts += [(x, Y(frc)), (x + 22, Y(tv)), (x + 44, Y(frc))]
        x += 44
    # max inspiration then max expiration
    pts += [(x + 40, Y(tlc)), (x + 110, Y(rv)), (x + 150, Y(frc))]
    x += 150
    for i in range(3):
        pts += [(x + 22, Y(tv)), (x + 44, Y(frc))]
        x += 44
    b += _d10_smooth(pts, 'f-l', ' style="stroke-width:2.5"')
    for f, lab in [(tlc, 'TLC'), (tv, ''), (frc, 'FRC level'), (rv, 'RV level')]:
        b += line(60, Y(f), 470, Y(f), 'f-dash')
        if lab:
            b += T(64, Y(f) - 5, lab, 'f-s', 'start')
    b += T(306, Y(tlc) - 8, 'maximal inspiration', 'f-s') + T(380, Y(rv) + 18, 'maximal expiration', 'f-s')
    # stacked volumes
    bx = 490
    for (lo, hi, lab, cls) in [(0, rv, 'RV', 'warn'), (rv, frc, 'ERV', 'b0'), (frc, tv, 'TV', 'ok'), (tv, tlc, 'IRV', 'b0')]:
        b += f'<rect x="{bx}" y="{Y(hi):.1f}" width="60" height="{Y(lo) - Y(hi):.1f}" class="f-{cls}"/>'
        b += T(bx + 30, (Y(lo) + Y(hi)) / 2 + 5, lab, 'f-h')
    # capacities brackets
    def brk(x, lo, hi, lab):
        out = line(x, Y(hi) + 1, x, Y(lo) - 1) + line(x - 5, Y(hi) + 1, x, Y(hi) + 1) + line(x - 5, Y(lo) - 1, x, Y(lo) - 1)
        out += T(x + 6, (Y(lo) + Y(hi)) / 2 + 4, lab, 'f-n', 'start')
        return out
    b += brk(566, 0, frc, 'FRC') + brk(616, rv, tlc, 'VC') + brk(664, 0, tlc, 'TLC')
    y = 350
    b += _d10_card(10, y, 226, 108, 'Residual volume', ['Left after maximal expiration:', '25 to 35% of TLC.', 'Raised with FRC in COPD', '(hyperinflation)'], 'warn')
    b += _d10_card(247, y, 226, 108, 'FRC = RV + ERV', ['Where the inward recoil of the', 'lung balances the outward', 'recoil of the chest wall,', 'at end-expiration'], 'b1')
    b += _d10_card(484, y, 226, 108, 'VC and TLC', ['VC = ERV + TV + IRV', 'TLC = all four volumes.', 'Anaesthesia lowers volumes', 'by 10 to 30% for up to 2 weeks'], 'b0')
    return svg(y + 118, b)


# ---------------------------------------------------------------- spirometry curves (t17)

def d10_spirometry():
    """Forced expiratory volume-time curves: normal, obstructive and restrictive, with COPD grades by FEV1."""
    x0, y0, w, h = 70, 40, 400, 250
    b = _d10_axes(x0, y0, w, h, '', 'Volume exhaled')
    b += T(x0 + w, y0 + h + 38, 'Time (s)', 'f-s', 'end')
    sx = (w - 20) / 6
    X = lambda t: x0 + t * sx
    b += line(X(1), y0 + 6, X(1), y0 + h, 'f-dash') + T(X(1), y0 + h + 18, '1 s', 'f-n')
    for t in (2, 3, 4, 5, 6):
        b += line(X(t), y0 + h, X(t), y0 + h + 5) + T(X(t), y0 + h + 18, str(t), 'f-s')

    def curve(fvc, k):
        import math
        return [(X(t / 10), y0 + h - fvc * (1 - math.exp(-k * t / 10))) for t in range(0, 61)]
    import math
    n = curve(220, 1.7)
    o = curve(160, 0.55)
    r = curve(130, 2.6)
    b += _d10_smooth(n, 'f-l', ' style="stroke-width:3"')
    b += _d10_smooth(o, 'f-dash', ' style="stroke-width:2.2"')
    b += _d10_smooth(r, 'f-l', ' style="stroke-width:1.8;opacity:.6"')
    b += T(X(5.8), n[-1][1] - 8, 'Normal', 'f-h', 'end')
    b += T(X(5.8), o[-1][1] - 8, 'Obstructive', 'f-h', 'end')
    b += T(X(5.8), r[-1][1] + 18, 'Restrictive', 'f-h', 'end')
    for c in (n, o, r):
        p = c[10]
        b += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="5" class="f-warn"/>'
    b += T(X(1) - 10, n[10][1] - 6, 'FEV1', 'f-s', 'end')
    # table at right
    rows = [('', 'Obstruction', 'Restriction'), ('FEV1', 'Down markedly', 'Down'), ('FVC', 'Down', 'Down'), ('FEV1/FVC', 'Down', 'Normal or up')]
    ty = 50
    for i, (a, c1, c2) in enumerate(rows):
        cls = 'f-h' if i == 0 else 'f-s'
        b += T(492, ty + i * 26, a, 'f-n' if i else '', 'start') + T(588, ty + i * 26, c1, cls) + T(668, ty + i * 26, c2, cls)
        if i:
            b += line(488, ty + i * 26 - 18, 710, ty + i * 26 - 18, 'f-grid')
    b += _d10_card(488, 164, 222, 120, 'Thresholds', ['COPD: post-bronchodilator', 'FEV1/FVC under 70% (or below', 'LLN, z under -1.64)',
                                                'Reversibility: FEV1 or FVC up', '12% and 200 ml'], 'b1')
    # GOLD strip
    y = 348
    b += T(12, y, 'COPD severity by FEV1 % predicted (GOLD)', 'f-h', 'start')
    segs = [(0, 30, '(iv) under 30%', 'warn'), (30, 50, '(iii) 30 to under 50%', 'warn'), (50, 80, '(ii) 50 to under 80%', 'b1'), (80, 100, '(i) 80% or more', 'ok')]
    sx2 = 6.9
    for lo, hi, lab, cls in segs:
        b += f'<rect x="{12 + lo * sx2:.1f}" y="{y + 12}" width="{(hi - lo) * sx2:.1f}" height="40" class="f-{cls}"/>'
        b += T(12 + (lo + hi) / 2 * sx2, y + 37, lab, 'f-s')
    for v in (0, 30, 50, 80, 100):
        b += T(12 + v * sx2, y + 70, f'{v}%', 'f-s')
    return svg(y + 80, b)


# ---- figs_D11.py



def _d11_lv(x, y, bulge=True):
    """LV outline in long section, apex down; optional apical bulge."""
    s = (f'<path d="M{x} {y} Q{x-6} {y+70} {x+30} {y+112}" class="f-vessel" fill="none"/>'
         f'<path d="M{x+110} {y} Q{x+116} {y+70} {x+80} {y+112}" class="f-vessel" fill="none"/>'
         f'<line x1="{x}" y1="{y}" x2="{x+110}" y2="{y}" class="f-dash"/>')
    if bulge:
        s += f'<path d="M{x+30} {y+112} Q{x+55} {y+160} {x+80} {y+112}" class="f-l" fill="none"/>'
    return s


def d11_lv_aneurysm_repairs():
    b = T(12, 20, 'Left ventricular aneurysm: four repairs (long section, apex down; arrangement schematic)', 'f-h', 'start')
    names = ['Plication', 'Linear closure', 'Patch closure', 'Endoventricular patch']
    notes = [['Small, no thrombus;', 'not opened; closed in', 'two layers over felt'],
             ['Open, clear thrombus,', 'trim to a 3 cm scar rim;', 'close vertically in two', 'layers with pledgets'],
             ['Partial excision; circular', 'purse-string (Fontan', 'stitch) narrows the', 'neck; Dacron patch'],
             ['Patch inside the cavity;', 'anterior aneurysms;', 'poor for posterior', 'or inferior ones']]
    for i in range(4):
        x = 30 + i * 172
        y = 60
        b += T(x + 55, 44, names[i], 'f-h')
        if i == 0:
            b += _d11_lv(x, y)
            b += f'<line x1="{x+26}" y1="{y+118}" x2="{x+84}" y2="{y+118}" class="f-cut"/><line x1="{x+30}" y1="{y+126}" x2="{x+80}" y2="{y+126}" class="f-cut"/>'
            b += f'<rect x="{x+20}" y="{y+114}" width="8" height="16" rx="2" class="f-ok"/><rect x="{x+82}" y="{y+114}" width="8" height="16" rx="2" class="f-ok"/>'
        elif i == 1:
            b += _d11_lv(x, y, False)
            b += f'<line x1="{x+55}" y1="{y+88}" x2="{x+55}" y2="{y+140}" class="f-cut"/>'
            b += f'<path d="M{x+30} {y+112} L{x+55} {y+140} L{x+80} {y+112}" class="f-vessel" fill="none"/>'
            for k in range(4):
                b += f'<line x1="{x+47}" y1="{y+96+k*12}" x2="{x+63}" y2="{y+96+k*12}" class="f-l"/>'
        elif i == 2:
            b += _d11_lv(x, y, False)
            b += f'<ellipse cx="{x+55}" cy="{y+114}" rx="27" ry="7" class="f-dash" fill="none"/>'
            b += f'<path d="M{x+30} {y+114} Q{x+55} {y+134} {x+80} {y+114}" class="f-stent" fill="none"/>'
        else:
            b += _d11_lv(x, y)
            b += f'<path d="M{x+27} {y+108} Q{x+55} {y+92} {x+83} {y+108}" class="f-stent" fill="none"/>'
        b += T(x + 55, y + 182, notes[i], 'f-s')
    b += box(12, 318, 340, 74, ['Repair for (all relative): angina, heart failure despite', 'treatment, ventricular arrhythmia, embolism, enlargement,', 'rupture or false aneurysm; ESVI over 80 ml/m²'], 'b0', 'f-s')
    b += box(366, 318, 342, 74, ['Not with RV dysfunction or a small residual cavity.', 'Know the coronaries before the ventriculotomy; do not', 'handle the ventricle before the clamp (thrombus)'], 'warn', 'f-s')
    b += T(12, 412, ['Dashed line: mitral level. Dotted line: patch. Red: suture line.', 'STICH: reconstruction added to CABG gave no survival advantage over grafting alone.'], 'f-s', 'start')
    return svg(440, b)


# ---- figs_K3.py



def k3_ppotiers():
    """ppo transfer factor tiers, ERS/ESTS 2025 as taught (Thoracic 2)."""
    return tiles([
        ('Over 60%', ['Normal risk', 'Surgery, no', 'further tests'], 'ok'),
        ('40 to 59%', ['Moderate', 'Stair climb or', 'shuttle; MDT'], 'b0'),
        ('Under 40%', ['High', 'CPET + V/Q SPECT;', 'consider sublobar'], 'b1'),
        ('Under 30%', ['Very high', 'Not absolute; MDT,', 'consent, SABR'], 'warn'),
    ], h=130)


def k3_vo2():
    """Peak VO2 bands as taught on the course slides, with NICE and course pack cut-offs."""
    x0, x1, vmax = 30, W - 30, 30
    sx = lambda v: x0 + (x1 - x0) * v / vmax
    b = T(x0, 22, 'Peak VO2 (mL/kg/min): bands taught on the course slides', 'f-h', 'start')
    bands = [(0, 10, 'warn', ['Under 10: high', 'SABR or ablation']),
             (10, 15, 'b1', ['10 to 15', 'sublobar']),
             (15, 20, 'b0', ['15 to 20', 'lobectomy']),
             (20, 30, 'ok', ['Over 20: low', 'up to pneumonectomy'])]
    for lo, hi, cls, lab in bands:
        b += f'<rect x="{sx(lo)}" y="40" width="{sx(hi) - sx(lo)}" height="56" rx="6" class="f-{cls}"/>'
        b += T((sx(lo) + sx(hi)) / 2, 63, lab, 'f-s')
    for v in (0, 10, 12, 15, 20):
        b += T(sx(v), 114, str(v), 'f-n')
    for v in (12, 15):
        b += line(sx(v), 30, sx(v), 40, 'f-dash') + line(sx(v), 96, sx(v), 101, 'f-dash')
    b += T(sx(12) - 6, 136, 'Course pack high risk: under 12', 'f-s', 'end')
    b += T(sx(15) + 6, 136, 'NICE good function: over 15', 'f-s', 'start')
    return svg(148, b)
