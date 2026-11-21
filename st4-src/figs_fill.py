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
