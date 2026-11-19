"""Drawings for the notes. Each function returns an inline SVG string.
Colours come from CSS variables in the page, so figures follow light and dark mode."""
from html import escape as E

W = 720


def svg(h, body, w=W):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" xmlns="http://www.w3.org/2000/svg">'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0 0L10 5L0 10z" class="f-ah"/></marker></defs>' + body + '</svg>')


def T(x, y, s, cls='', anchor='middle'):
    if isinstance(s, str):
        s = [s]
    out = ''
    for i, line in enumerate(s):
        out += f'<text x="{x}" y="{y + i * 17}" text-anchor="{anchor}" class="f-t {cls}">{E(line)}</text>'
    return out


def box(x, y, w, h, lines, cls='b0', tcls=''):
    if isinstance(lines, str):
        lines = [lines]
    ty = y + h / 2 - (len(lines) - 1) * 8.5 + 5
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="f-{cls}"/>'
            + T(x + w / 2, ty, lines, tcls))


def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="5 4"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="f-l" marker-end="url(#ah)"{d}/>'


def line(x1, y1, x2, y2, cls='f-l'):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>'


def bars(items, unit, vmax, title=None, lab_w=250):
    """items: (label, value, cls) or (label, (lo, hi), cls). Horizontal bars."""
    y = 18
    out = ''
    if title:
        out += T(12, y + 4, title, 'f-h', 'start')
        y += 26
    span = W - lab_w - 90
    for lab, v, cls in items:
        out += T(lab_w - 10, y + 19, lab, '', 'end')
        if isinstance(v, tuple):
            lo, hi = v
            out += f'<rect x="{lab_w}" y="{y + 4}" width="{span * hi / vmax}" height="22" rx="4" class="f-track"/>'
            out += f'<rect x="{lab_w + span * lo / vmax}" y="{y + 4}" width="{span * (hi - lo) / vmax}" height="22" rx="4" class="f-{cls}"/>'
            out += T(lab_w + span * hi / vmax + 8, y + 20, f'{lo} to {hi}{unit}', 'f-n', 'start')
        else:
            out += f'<rect x="{lab_w}" y="{y + 4}" width="{max(2, span * v / vmax)}" height="22" rx="4" class="f-{cls}"/>'
            out += T(lab_w + span * v / vmax + 8, y + 20, f'{v:g}{unit}', 'f-n', 'start')
        y += 34
    return y + 6, out


def tiles(items, h=110):
    """items: (big, small lines, cls). Equal tiles in a row."""
    n = len(items)
    w = (W - 20 - (n - 1) * 14) / n
    out = ''
    for i, (big, small, cls) in enumerate(items):
        x = 10 + i * (w + 14)
        out += f'<rect x="{x}" y="10" width="{w}" height="{h}" rx="10" class="f-{cls}"/>'
        out += T(x + w / 2, 50, big, 'f-big')
        out += T(x + w / 2, 74, small, 'f-s')
    return svg(h + 20, out)


# ---------------------------------------------------------------- thoracic

def pneumothorax():
    b = box(260, 10, 200, 40, 'Spontaneous pneumothorax', 'b1', 'f-h')
    b += arrow(320, 50, 190, 78) + arrow(400, 50, 530, 78)
    b += box(90, 80, 200, 38, 'Primary (no lung disease)') + box(430, 80, 200, 38, 'Secondary (COPD etc.)')
    b += arrow(150, 118, 100, 148) + arrow(230, 118, 270, 148) + arrow(490, 118, 450, 148) + arrow(570, 118, 620, 148)
    b += box(10, 150, 170, 62, ['Small, stable', 'under 3 cm', 'Observe; film at 6 h'], 'ok')
    b += box(190, 150, 160, 62, ['Large', '3 cm or more', 'Drain'], 'b1')
    b += box(370, 150, 160, 62, ['Small', 'Admit and', 'observe'], 'b0')
    b += box(540, 150, 170, 62, ['Large', 'Always drain'], 'b1')
    b += box(10, 232, 700, 62, ['Operate for: air leak 3 days or more · second ipsilateral · first contralateral',
                               'spontaneous haemothorax · high-risk occupation · remote from care'], 'warn')
    return svg(304, b)


def empyema():
    b = ''
    spec = [('I Exudative', '1 to 2 weeks', 'Free fluid', 'Chest drain', 'ok'),
            ('II Fibrinopurulent', '2 to 4 weeks', 'Fibrin, pus, loculi', 'Lysis or VATS', 'b1'),
            ('III Organising', '4 to 6 weeks', 'Peel, trapped lung', 'Decortication', 'warn')]
    for i, (a, t, f, tx, c) in enumerate(spec):
        x = 10 + i * 240
        b += box(x, 10, 220, 78, [a, t, f], 'b0', '')
        b += arrow(x + 110, 88, x + 110, 112)
        b += box(x, 114, 220, 40, tx, c, 'f-h')
        if i < 2:
            b += arrow(x + 222, 49, x + 238, 49)
    return svg(164, b)


def mars2():
    h, b = bars([('Chemotherapy alone', 24.8, 'ok'), ('Surgery plus chemotherapy', 19.3, 'warn')],
                ' months', 30, 'Median survival, MARS 2 (n=335)')
    return svg(h, b)


def duct():
    b = line(360, 20, 360, 330, 'f-dash')
    b += T(372, 30, 'midline', 'f-s', 'start') + T(64, 30, "Patient's left (seen from behind)", 'f-s', 'start') + T(656, 30, "Patient's right", 'f-s', 'end')
    for y, lab in [(60, 'Neck'), (150, 'T5 to T6'), (262, 'T12 aortic hiatus'), (312, 'L2')]:
        b += line(60, y, 660, y, 'f-grid') + T(64, y - 6, lab, 'f-s', 'start')
    b += '<path d="M392 312 L392 262 L392 160 C392 140 330 150 326 120 L322 78 C320 58 300 52 286 60" class="f-duct"/>'
    b += '<ellipse cx="392" cy="312" rx="13" ry="9" class="f-b1"/>'
    b += T(374, 334, 'Cisterna chyli', 'f-s', 'end')
    b += T(414, 215, ['Runs on the right, between', 'aorta and azygos vein'], '', 'start')
    b += T(200, 138, ['Crosses to the left', 'behind the oesophagus'], '', 'middle')
    b += T(180, 56, ['Ends at the left', 'jugulo-subclavian junction'], '', 'middle')
    b += line(376, 246, 408, 246, 'f-cut') + line(376, 252, 408, 252, 'f-cut')
    b += arrow(470, 249, 412, 249) + T(478, 246, ['Ligate here: low,', 'right chest'], 'f-h', 'start')
    b += box(430, 284, 280, 36, 'Injury below T5: right chylothorax', 'b0')
    b += box(430, 96, 280, 40, 'Injury above T5: left chylothorax', 'b0')
    return svg(346, b)


def trachea():
    b = '<rect x="310" y="40" width="70" height="250" rx="14" class="f-b0"/>'
    for i in range(11):
        b += line(312, 62 + i * 21, 378, 62 + i * 21, 'f-grid')
    b += '<rect x="304" y="26" width="82" height="20" rx="8" class="f-b1"/>'
    b += '<path d="M318 290 L270 340 M372 290 L420 340" class="f-l" style="stroke-width:10;stroke-linecap:round"/>'
    b += T(400, 40, 'Cricoid: the only complete ring', '', 'start')
    b += line(290, 48, 290, 288) + T(280, 170, '10 to 13 cm', 'f-s', 'end') + T(280, 187, '18 to 22 rings', 'f-s', 'end')
    b += arrow(470, 90, 384, 90) + T(476, 86, ['Inferior thyroid arteries', '(upper trachea)'], '', 'start')
    b += arrow(470, 235, 384, 235) + T(476, 231, ['Bronchial arteries', '(lower trachea)'], '', 'start')
    b += T(476, 150, ['Supply enters laterally and is', 'segmental: dissect only 1 to 1.5 cm', 'around the stricture'], 'f-s', 'start')
    b += '<path d="M300 300 C296 220 298 120 304 60" class="f-nerve"/><path d="M392 200 C394 140 392 100 388 60" class="f-nerve"/>'
    b += T(130, 258, ['Recurrent laryngeal nerves', 'in the groove; the left', 'runs the full length'], 'f-s', 'middle')
    b += T(345, 362, 'Carina', 'f-s')
    b += box(10, 300, 230, 44, ['Resectable: up to half', '(about 6 cm) with releases'], 'ok')
    return svg(372, b)


def stenosis():
    b = ''
    b += '<circle cx="180" cy="100" r="70" class="f-b0"/><path d="M180 52 L212 140 L148 140 Z" class="f-lumen"/>'
    b += T(180, 196, 'Stomal stricture: A-shaped', 'f-h') + T(180, 215, 'Anterior and lateral walls fall in', 'f-s')
    b += '<circle cx="540" cy="100" r="70" class="f-b0"/><circle cx="540" cy="100" r="18" class="f-lumen"/>'
    b += T(540, 196, 'Cuff stenosis: circumferential', 'f-h') + T(540, 215, '3 to 6 weeks after extubation', 'f-s')
    return svg(228, b)


def haller():
    b = '<path d="M100 150 C100 40 250 30 330 78 C350 90 370 90 390 78 C470 30 620 40 620 150 C620 250 470 262 360 262 C250 262 100 250 100 150 Z" class="f-b0"/>'
    b += '<rect x="335" y="78" width="50" height="16" rx="6" class="f-b1"/><circle cx="360" cy="222" r="26" class="f-b1"/>'
    b += T(360, 66, 'Sternum', 'f-s') + T(360, 226, 'Spine', 'f-s')
    b += '<line x1="104" y1="150" x2="616" y2="150" class="f-l" marker-start="url(#ah)" marker-end="url(#ah)"/>' + T(200, 142, 'A: transverse diameter', 'f-h')
    b += '<line x1="360" y1="98" x2="360" y2="194" class="f-cut" marker-start="url(#ah)" marker-end="url(#ah)"/>' + T(372, 128, 'B', 'f-h', 'start')
    b += box(140, 276, 440, 44, ['Haller index = A ÷ B', 'Normal 2.5 or less · significant 3.25 or more'], 'ok')
    return svg(330, b)


def margins():
    h, b = bars([('Soft tissue sarcoma', 1, 'b1'), ('Chondroma', 2, 'b1'), ('Chondrosarcoma, low grade', 2, 'b1'),
                 ('Desmoid', (2, 4), 'warn'), ('Chondrosarcoma, high grade', 4, 'warn')], ' cm', 5,
                'Recommended resection margin')
    return svg(h, b)


def diaphragm():
    b = '<ellipse cx="360" cy="170" rx="300" ry="140" class="f-b0"/>'
    b += '<path d="M240 150 C300 110 420 110 480 150 C470 200 400 215 360 190 C320 215 250 200 240 150 Z" class="f-b1"/>'
    b += T(360, 150, 'Central tendon', 'f-s')
    b += '<circle cx="430" cy="160" r="15" class="f-lumen"/>' + T(452, 150, 'Vena cava T8', '', 'start')
    b += '<ellipse cx="330" cy="205" rx="13" ry="17" class="f-lumen"/>' + T(310, 210, 'Oesophagus T10', '', 'end')
    b += '<circle cx="360" cy="270" r="16" class="f-lumen"/>' + T(384, 276, 'Aorta T12 (with azygos, thoracic duct)', '', 'start')
    b += '<ellipse cx="395" cy="40" rx="24" ry="9" class="f-warn"/>' + T(430, 30, 'Morgagni (right, retrosternal)', 'f-s', 'start')
    b += '<ellipse cx="325" cy="40" rx="24" ry="9" class="f-warn"/>' + T(290, 30, 'Larrey (left)', 'f-s', 'end')
    b += '<ellipse cx="150" cy="250" rx="36" ry="14" class="f-warn" transform="rotate(-35 150 250)"/>' + T(40, 300, 'Bochdalek: posterolateral, 90% left', 'f-s', 'start')
    b += T(60, 22, 'Front', 'f-s', 'start') + T(60, 330, 'Back', 'f-s', 'start') + T(40, 175, 'Left', 'f-s', 'start') + T(684, 175, 'Right', 'f-s', 'end')
    return svg(340, b)


def lvrs():
    b = T(330, 26, 'Exercise capacity after rehabilitation', 'f-h') + T(260, 50, 'Low') + T(540, 50, 'High')
    b += T(100, 100, ['Upper lobe', 'predominant'], 'f-h') + T(100, 190, ['Non-upper', 'lobe'], 'f-h')
    b += box(160, 62, 260, 76, ['Survival advantage', 'with surgery'], 'ok', 'f-h')
    b += box(430, 62, 260, 76, ['No survival difference', '(function may improve)'], 'b0')
    b += box(160, 150, 260, 76, ['No survival difference'], 'b0')
    b += box(430, 150, 260, 76, ['Higher risk of death', 'with surgery'], 'warn', 'f-h')
    return svg(240, b)


def ltx():
    b = line(40, 60, 690, 60) + ''
    for x, lab in [(40, 'Day 0'), (190, '72 hours'), (340, '1 month'), (490, '3 months'), (680, 'Years')]:
        b += line(x, 54, x, 66) + T(x, 46, lab, 'f-s')
    b += box(40, 78, 150, 50, ['Primary graft', 'dysfunction, 30%'], 'warn')
    b += box(200, 78, 280, 50, ['Acute rejection, up to 50%', 'Bacterial infection, then CMV'], 'b1')
    b += box(200, 136, 380, 44, 'Airway ischaemia, dehiscence, stenosis', 'b0')
    b += box(500, 78, 190, 50, ['Bronchiolitis', 'obliterans syndrome'], 'warn')
    return svg(190, b)


def lethal():
    spec = [('Obstructed airway', 'Bronchoscopic tube past', 'the injury; surgical airway'),
            ('Tension pneumothorax', 'Chest drain now', '(needle only if no drain)'),
            ('Massive haemothorax', 'Drain; theatre by', 'volume and physiology'),
            ('Open chest wound', 'Cover; drain through', 'a separate site'),
            ('Flail chest', 'Analgesia, physiotherapy,', 'restrained fluids'),
            ('Cardiac tamponade', 'Theatre or resuscitative', 'thoracotomy')]
    b = ''
    for i, (a, l1, l2) in enumerate(spec):
        x = 10 + (i % 3) * 236
        y = 10 + (i // 3) * 112
        b += f'<rect x="{x}" y="{y}" width="226" height="100" rx="10" class="f-b0"/>'
        b += f'<rect x="{x}" y="{y}" width="226" height="34" rx="10" class="f-warn"/>'
        b += T(x + 113, y + 22, a, 'f-h') + T(x + 113, y + 58, [l1, l2], 'f-s')
    return svg(232, b)


def haemothorax():
    return tiles([('1,500 ml', ['on insertion'], 'warn'), ('250 ml/h', ['for 2 to 4 hours'], 'warn'),
                  ('1,500 ml', ['in 24 hours'], 'warn'), ('72 hours', ['VATS for retained', 'haemothorax'], 'b1')], 104)


def aorta():
    b = '<path d="M150 300 L150 170 C150 40 420 40 420 170 L420 330" class="f-vessel"/>'
    for x, lab, tx, an in [(232, 'Innominate', 222, 'end'), (285, 'Left carotid', 285, 'middle'), (338, 'Left subclavian', 350, 'start')]:
        b += f'<path d="M{x} 82 L{x} 34" class="f-vessel" style="stroke-width:16"/>' + T(tx, 18 if an == 'middle' else 40, lab, 'f-s', an)
    b += '<path d="M404 150 L436 165" class="f-cut" style="stroke-width:4"/>'
    b += '<path d="M396 152 C380 170 360 176 340 178" class="f-dash"/>' + T(300, 196, 'Ligamentum arteriosum', 'f-s')
    b += arrow(540, 150, 442, 158) + T(548, 146, ['Isthmus: commonest', 'site of the tear'], 'f-h', 'start')
    b += '<rect x="404" y="120" width="32" height="150" rx="8" class="f-stent"/>'
    b += arrow(540, 240, 440, 240) + T(548, 236, ['Stent graft; the left', 'subclavian is covered', 'in over half'], '', 'start')
    b += T(150, 322, 'Ascending', 'f-s') + T(420, 350, 'Descending', 'f-s')
    b += box(10, 60, 120, 60, ['Second site:', 'innominate', 'origin'], 'b0', 'f-s')
    return svg(360, b)


def tnm9():
    b = box(40, 20, 180, 44, 'N2 (8th edition)', 'b0', 'f-h') + arrow(220, 34, 300, 24) + arrow(220, 50, 300, 78)
    b += box(304, 6, 380, 38, 'N2a: a single N2 station', 'b1') + box(304, 60, 380, 38, 'N2b: more than one N2 station', 'b1')
    b += box(40, 140, 180, 44, 'M1c (8th edition)', 'b0', 'f-h') + arrow(220, 154, 300, 144) + arrow(220, 170, 300, 198)
    b += box(304, 126, 380, 38, 'M1c1: multiple metastases, one organ system', 'b1')
    b += box(304, 180, 380, 38, 'M1c2: metastases in several organ systems', 'b1')
    b += T(360, 246, 'T descriptors unchanged. T1 N2a moves to IIB; T2 N2a is IIIA; T2 N2b is IIIB.', 'f-s')
    return svg(258, b)


def trials():
    h1, b1 = bars([('Segmentectomy', 94.3, 'ok'), ('Lobectomy', 91.1, 'b1')], '%', 100, 'JCOG0802: 5-year overall survival')
    h2, b2 = bars([('VATS lobectomy', 32.8, 'ok'), ('Open lobectomy', 44.3, 'warn')], '%', 100, 'VIOLET: in-hospital complications')
    return svg(h1 + h2, b1 + f'<g transform="translate(0 {h1})">{b2}</g>')


# ---------------------------------------------------------------- cardiac

def cpb():
    b = box(20, 100, 130, 70, ['Heart', '(right atrium', 'or cavae)'], 'b1', '')
    b += arrow(150, 120, 230, 60) + T(176, 74, 'Venous line', 'f-s')
    b += box(232, 30, 130, 50, ['Venous', 'reservoir'], 'b0') + arrow(362, 55, 410, 55)
    b += box(412, 30, 110, 50, 'Pump', 'b0') + arrow(522, 55, 570, 55)
    b += box(572, 22, 138, 66, ['Oxygenator and', 'heat exchanger'], 'b0')
    b += arrow(640, 88, 640, 150) + box(572, 152, 138, 44, 'Arterial filter', 'b0')
    b += arrow(572, 174, 300, 174) + T(430, 166, 'Arterial line', 'f-s')
    b += box(170, 152, 130, 44, 'Ascending aorta', 'b1') + arrow(170, 164, 152, 150)
    b += box(20, 216, 330, 80, ['Vents: aortic root · right superior', 'pulmonary vein · pulmonary artery ·', 'left atrium or ventricle'], 'ok', 'f-s')
    b += box(370, 216, 340, 80, ['Cardioplegia: antegrade (root or ostia)', 'or retrograde (coronary sinus)', 'Flow 2 to 2.5 L/min/m², pressure about 60 mmHg'], 'b0', 'f-s')
    return svg(306, b)


def iabp():
    b = line(40, 250, 690, 250, 'f-grid') + T(44, 268, 'Time', 'f-s', 'start')
    b += '<path d="M40 210 C70 210 80 90 110 90 C135 90 140 150 158 158 C170 150 176 172 196 196 C220 210 230 214 250 214" class="f-l"/>'
    b += '<path d="M250 214 C280 214 290 96 320 96 C340 96 346 150 362 160 C378 60 420 56 440 120 C456 170 470 232 500 236 C530 236 536 110 566 110 C590 110 596 160 614 168 C640 190 660 206 690 210" class="f-cut" style="stroke-width:2.4"/>'
    b += T(110, 76, 'Unassisted systole', 'f-s')
    b += arrow(330, 226, 358, 168) + T(250, 240, 'Inflate at the dicrotic notch', 'f-h')
    b += T(430, 44, ['Augmented diastolic pressure:', 'coronary perfusion rises'], 'f-s')
    b += arrow(500, 196, 500, 230) + T(500, 186, 'Deflate before systole', 'f-h')
    b += T(610, 76, ['Assisted systole:', 'lower afterload'], 'f-s')
    b += T(686, 268, 'Balloon tip sits just beyond the left subclavian artery', 'f-s', 'end')
    return svg(280, b)


def ecmo():
    b = T(180, 22, 'Veno-venous: lungs only', 'f-h') + T(540, 22, 'Veno-arterial: heart and lungs', 'f-h')
    b += line(360, 10, 360, 250, 'f-dash')
    for x in (20, 380):
        b += box(x, 40, 120, 40, 'Vena cava', 'b0') + arrow(x + 120, 60, x + 150, 60)
        b += box(x + 152, 40, 70, 40, 'Pump', 'b0') + arrow(x + 222, 60, x + 248, 60)
        b += box(x + 250, 40, 90, 40, 'Oxygenator', 'b0') + arrow(x + 295, 80, x + 295, 110)
    b += box(190, 112, 150, 40, 'Right atrium', 'b1') + box(550, 112, 150, 40, 'Femoral artery', 'warn')
    b += T(180, 184, ['Keep drainage and return tips', '8 cm apart: recirculation', 'Wean the sweep gas, not the flow'], 'f-s')
    b += T(540, 178, ['Retrograde flow meets native ejection:', 'the upper body may receive', 'desaturated blood. Sample the right arm.', 'Watch for left ventricular distension', 'and limb ischaemia'], 'f-s')
    return svg(262, b)


def htx():
    names = ['Left atrium', 'Inferior vena cava', 'Aorta', 'Pulmonary artery', 'Superior vena cava']
    b = ''
    for i, n in enumerate(names):
        x = 10 + i * 142
        b += f'<circle cx="{x + 20}" cy="34" r="16" class="f-b1"/>' + T(x + 20, 39, str(i + 1), 'f-h')
        b += box(x, 60, 130, 50, n.split(' ', 1) if len(n) > 12 else n, 'b0')
        if i < 4:
            b += arrow(x + 40, 34, x + 138, 34)
    b += box(294, 122, 130, 34, 'Clamp off here', 'ok', 'f-s')
    b += T(360, 180, 'With a long ischaemic time, the aorta is done second.', 'f-s')
    return svg(194, b)


def tamponade():
    b = T(180, 22, 'Tamponade', 'f-h') + T(540, 22, 'Constriction', 'f-h') + line(360, 10, 360, 300, 'f-dash')
    b += T(20, 50, 'Venous pressure', 'f-s', 'start')
    b += '<path d="M20 110 C40 70 60 70 70 100 C80 130 100 140 120 120 C140 100 150 96 170 100 C190 104 200 80 220 76 C240 72 250 100 260 124 C275 140 300 120 330 104" class="f-l"/>'
    b += T(100, 156, 'x descent kept', 'f-s') + T(250, 156, 'y descent absent', 'f-h')
    b += '<path d="M380 110 C400 70 420 70 430 100 C440 140 455 150 470 110 C480 84 500 80 512 96 C525 150 540 156 556 110 C570 80 590 80 600 100 C612 146 625 150 640 110 C650 90 680 88 700 96" class="f-l"/>'
    b += T(450, 172, 'x', 'f-s') + T(535, 178, 'deep y', 'f-h')
    b += T(380, 200, 'Ventricular pressure', 'f-s', 'start')
    b += '<path d="M380 280 L400 280 C410 280 412 216 430 216 C448 216 450 296 462 296 C470 296 474 262 488 260 L540 260 C550 260 552 216 570 216 C588 216 590 296 602 296 C610 296 614 262 628 260 L690 260" class="f-cut" style="stroke-width:2.2"/>'
    b += T(560, 312, 'Dip and plateau: the square root sign', 'f-s')
    b += box(20, 196, 310, 100, ['Both: left and right filling pressures equal', 'Tamponade: pulsus paradoxus usual', 'Constriction: neck veins rise on', 'inspiration (Kussmaul sign)'], 'b0', 'f-s')
    return svg(324, b)


def tumours():
    h, b = bars([('Left atrium', 75, 'b1'), ('Right atrium', 18, 'b1')], '%', 100, 'Where myxomas arise (fossa ovalis stalk)')
    h2, b2 = bars([('Benign', 75, 'ok'), ('Malignant (mostly sarcoma)', 25, 'warn')], '%', 100, 'Primary cardiac tumours')
    return svg(h + h2, b + f'<g transform="translate(0 {h})">{b2}</g>')


def patency():
    h, b = bars([('Left internal mammary, 5 years', 95, 'ok'), ('Left internal mammary, 10 years', 90, 'ok'),
                 ('Radial artery, 5 years', (83, 95), 'b1'), ('Saphenous vein, 10 years', 50, 'warn')],
                '%', 100, 'Graft patency', 270)
    return svg(h, b)


def mi():
    b = line(30, 50, 690, 50)
    for x, lab in [(30, 'Infarct'), (200, '13 hours'), (400, 'Day 5'), (680, 'Day 14')]:
        b += line(x, 44, x, 56) + T(x, 36, lab, 'f-s')
    b += box(110, 70, 190, 96, ['Papillary muscle rupture', 'posteromedial in 75%', 'Operative mortality 27%', 'Untreated 70 to 80%'], 'warn', 'f-s')
    b += box(310, 70, 190, 96, ['Septal rupture', 'anterior-apical two thirds', '30-day mortality 41%', '(inferior 73%)'], 'warn', 'f-s')
    b += box(510, 70, 190, 96, ['Free wall rupture', 'anterior or lateral wall', 'Operative mortality', '12 to 30%'], 'warn', 'f-s')
    b += T(360, 190, 'All are class I indications for emergency surgery with grafting.', 'f-s')
    return svg(202, b)



# ---------------------------------------------------------------- second tranche

def ppo():
    b = box(230, 8, 260, 40, 'Predicted postoperative FEV1 and DLCO', 'b1', 'f-h')
    b += arrow(290, 48, 130, 76) + arrow(360, 48, 360, 76) + arrow(430, 48, 590, 76)
    b += box(20, 78, 220, 44, ['Both over 60%'], 'ok') + box(250, 78, 220, 44, ['Either 30 to 60%'], 'b0') + box(480, 78, 220, 44, ['Either under 30%'], 'warn')
    b += arrow(130, 122, 130, 150) + arrow(360, 122, 360, 150) + arrow(590, 122, 590, 150)
    b += box(20, 152, 220, 44, 'Low risk', 'ok', 'f-h') + box(250, 152, 220, 44, ['Stair climb or 6-minute walk'], 'b0') + box(480, 152, 220, 44, ['Measure VO2 max'], 'b0')
    b += arrow(360, 196, 360, 224) + arrow(470, 186, 500, 196)
    b += box(250, 226, 220, 40, ['Pass: intermediate risk'], 'b1')
    b += T(432, 212, 'fail', 'f-s', 'start')
    b += arrow(540, 196, 520, 224) + arrow(640, 196, 660, 224)
    b += box(480, 226, 105, 52, ['10 to 15:', 'high risk'], 'warn', 'f-s') + box(595, 226, 105, 52, ['Under 10:', 'do not resect'], 'warn', 'f-s')
    return svg(288, b)


def haemsrc():
    h, b = bars([('Bronchial arteries', 90, 'warn'), ('Pulmonary artery', 5, 'b1'), ('Non-bronchial systemic', 5, 'b1')],
                '%', 100, 'Source of bleeding in life-threatening haemoptysis')
    return svg(h, b)


def bleed():
    return tiles([('500 ml', ['in the first hour'], 'warn'), ('400 ml/h', ['for 2 hours'], 'warn'),
                  ('300 ml/h', ['for 3 hours'], 'warn'), ('1 litre', ['in the first 4 hours'], 'warn')], 100)


def berlin():
    return tiles([('200 to 300', ['Mild', 'PaO2/FiO2, mmHg'], 'b1'), ('100 to 200', ['Moderate'], 'warn'),
                  ('Under 100', ['Severe'], 'warn'), ('6 to 8 ml/kg', ['Tidal volume;', 'plateau under 30'], 'ok')], 108)


def lcocauses():
    spec = [('Preload down', ['Bleeding, tamponade,', 'tension pneumothorax,', 'right ventricular failure']),
            ('Contractility down', ['Stunning, ischaemia,', 'graft failure, acidosis,', 'low calcium']),
            ('Afterload up', ['Vasoconstriction,', 'systolic anterior motion,', 'outflow obstruction']),
            ('Rate and rhythm', ['Atrial fibrillation,', 'heart block,', 'ventricular arrhythmia'])]
    b = box(260, 6, 200, 36, 'Low cardiac output', 'b1', 'f-h')
    for i, (a, ls) in enumerate(spec):
        x = 10 + i * 177
        b += arrow(360, 42, x + 84, 66)
        b += f'<rect x="{x}" y="68" width="168" height="110" rx="10" class="f-b0"/><rect x="{x}" y="68" width="168" height="32" rx="10" class="f-warn"/>'
        b += T(x + 84, 89, a, 'f-h') + T(x + 84, 122, ls, 'f-s')
    return svg(188, b)



def nbg():
    spec = [('I', 'Chamber paced', 'O · A · V · D'), ('II', 'Chamber sensed', 'O · A · V · D'),
            ('III', 'Response to sensing', 'O · T · I · D'), ('IV', 'Rate modulation', 'O · R')]
    b = ''
    for i, (n, a, l) in enumerate(spec):
        x = 10 + i * 177
        b += f'<rect x="{x}" y="10" width="168" height="96" rx="10" class="f-b0"/><rect x="{x}" y="10" width="168" height="32" rx="10" class="f-b1"/>'
        b += T(x + 84, 31, 'Position ' + n, 'f-h') + T(x + 84, 64, a) + T(x + 84, 88, l, 'f-n')
    b += box(10, 120, 345, 44, ['DDD: paces both, senses both,', 'inhibits and triggers'], 'ok', 'f-s')
    b += box(365, 120, 345, 44, ['VVI: paces and senses the ventricle,', 'inhibited by a sensed beat'], 'ok', 'f-s')
    return svg(174, b)



def medmass():
    spec = [('Anterior', ['Thymoma', 'Teratoma, germ cell', 'Lymphoma', 'Thyroid'], 'b1'),
            ('Middle (visceral)', ['Lymph nodes', 'Bronchogenic cyst', 'Pericardial cyst', 'Enteric cyst'], 'b0'),
            ('Posterior (paravertebral)', ['Nerve sheath tumours', 'Ganglion cell tumours', 'Paraganglioma'], 'b0')]
    b = T(20, 20, 'Sternum', 'f-s', 'start') + T(700, 20, 'Spine', 'f-s', 'end') + arrow(90, 16, 640, 16)
    for i, (a, ls, c) in enumerate(spec):
        x = 10 + i * 236
        b += f'<rect x="{x}" y="30" width="226" height="130" rx="10" class="f-b0"/><rect x="{x}" y="30" width="226" height="32" rx="10" class="f-b1"/>'
        b += T(x + 113, 51, a, 'f-h') + T(x + 113, 84, ls, 'f-s')
    return svg(170, b)


def oesperf():
    spec = [('Cervical', ['Neck incision along', 'sternocleidomastoid;', 'drain, close if seen']),
            ('Upper and middle thoracic', ['Right thoracotomy;', 'two-layer repair', 'with a flap']),
            ('Lower thoracic', ['Left thoracotomy;', 'two-layer repair', 'with a flap'])]
    b = ''
    for i, (a, ls) in enumerate(spec):
        x = 10 + i * 236
        b += f'<rect x="{x}" y="10" width="226" height="112" rx="10" class="f-b0"/><rect x="{x}" y="10" width="226" height="32" rx="10" class="f-warn"/>'
        b += T(x + 113, 31, a, 'f-h') + T(x + 113, 64, ls, 'f-s')
    b += box(10, 134, 700, 40, 'Always: endoscopy to exclude distal obstruction · debride · drain widely · feeding access', 'ok', 'f-s')
    return svg(184, b)


def maze():
    b = box(10, 10, 226, 96, ['Pulmonary vein isolation', 'Box around all four veins', '70 to 80% alone if paroxysmal;', '56% or less if persistent'], 'b1', 'f-s')
    b += box(247, 10, 226, 96, ['Left atrial set', 'Box, mitral isthmus line,', 'coronary sinus,', 'appendage closed'], 'b0', 'f-s')
    b += box(484, 10, 226, 96, ['Right atrial set', 'Cava to cava line,', 'line to the appendage;', 'can follow clamp removal'], 'b0', 'f-s')
    b += arrow(236, 58, 246, 58) + arrow(473, 58, 483, 58)
    b += box(10, 118, 700, 36, 'All three together make the Cox-Maze lesion set (IV: radiofrequency and cryoablation)', 'ok', 'f-s')
    return svg(164, b)


def asgrade():
    return tiles([('1.0 cm² or less', ['Valve area'], 'warn'), ('40 mmHg or more', ['Mean gradient'], 'warn'),
                  ('4 m/s or more', ['Peak velocity'], 'warn')], 96)



def aothresh():
    h, b = bars([('Loeys-Dietz', (4.0, 4.2), 'warn'), ('At other cardiac surgery', 4.5, 'b1'),
                 ('Marfan, with risk features', 4.5, 'warn'), ('Marfan; bicuspid with a risk factor', 5.0, 'warn'),
                 ('Degenerative; bicuspid without', 5.5, 'b1')], ' cm', 6.5,
                'Elective replacement threshold (American guidelines as quoted)', 290)
    return svg(h, b)


def crawford():
    ext = [('I', 40, 190), ('II', 40, 300), ('III', 120, 300), ('IV', 200, 300), ('V', 120, 190)]
    b = ''
    for y, lab in [(40, 'Left subclavian'), (120, 'T6'), (200, 'Diaphragm, coeliac'), (230, 'Renal arteries'), (300, 'Bifurcation')]:
        b += line(150, y, 700, y, 'f-grid') + T(142, y + 4, lab, 'f-s', 'end')
    for i, (n, y1, y2) in enumerate(ext):
        x = 200 + i * 100
        b += f'<rect x="{x}" y="30" width="30" height="280" rx="12" class="f-b0"/>'
        y2 = 215 if y2 == 190 else y2
        b += f'<rect x="{x - 8}" y="{y1}" width="46" height="{y2 - y1}" rx="18" class="f-warn"/>'
        b += T(x + 15, 22, 'Extent ' + n, 'f-h')
    return svg(322, b)


def taad():
    b = T(12, 20, 'Distal: how much arch', 'f-h', 'start')
    b += box(10, 30, 226, 92, ['Hemiarch', 'No arch tear', 'Arch under 4 cm', 'No carotid or innominate malperfusion'], 'ok', 'f-s')
    b += box(247, 30, 226, 92, ['Total arch', 'Tear in the arch, or', 'arch over 4 cm;', 'reimplant malperfused branches'], 'b1', 'f-s')
    b += box(484, 30, 226, 92, ['Frozen elephant trunk', 'More false lumen closure', 'Paraplegia 5 to 10%', '(under 1% without)'], 'warn', 'f-s')
    b += T(12, 150, 'Proximal: what to do with the root', 'f-h', 'start')
    b += box(10, 160, 226, 92, ['Resuspend and repair', 'No root tear', 'No connective tissue disease', 'Root under 4.5 cm'], 'ok', 'f-s')
    b += box(247, 160, 226, 92, ['Valve-sparing root', 'Root involved,', 'valve preservable;', 'reimplantation if Marfan'], 'b1', 'f-s')
    b += box(484, 160, 226, 92, ['Composite valve graft', 'Valve cannot be kept', 'Coronary buttons', 'reimplanted'], 'warn', 'f-s')
    return svg(262, b)


def carpentier():
    cols = [('I', 'Normal motion', ['Annulus dilated', 'or leaflet perforated'], 'b0'),
            ('II', 'Excess motion', ['Prolapse or flail:', 'chord or papillary rupture'], 'warn'),
            ('IIIa', 'Restricted, both phases', ['Rheumatic,', 'calcific'], 'b1'),
            ('IIIb', 'Restricted in systole', ['Ischaemic tethering,', 'dilated ventricle'], 'b1')]
    b = ''
    w = 166
    st = 'fill="none" style="stroke-width:3.5px;stroke-linecap:round"'
    for i, (n, mot, cause, cls) in enumerate(cols):
        x = 10 + i * (w + 12)
        cx = x + w / 2
        b += f'<rect x="{x}" y="10" width="{w}" height="226" rx="10" class="f-{cls}"/>'
        b += T(cx, 34, 'Type ' + n, 'f-h') + T(cx, 52, mot, 'f-s')
        ax1, ax2, ay = cx - 50, cx + 50, 104
        if n == 'I':
            ax1, ax2 = cx - 66, cx + 66
            l, r = (cx - 12, ay + 22), (cx + 12, ay + 22)
        elif n == 'II':
            l, r = (cx + 2, ay + 22), (cx - 2, ay - 16)
        elif n == 'IIIa':
            l, r = (cx - 9, ay + 26), (cx + 9, ay + 26)
        else:
            l, r = (cx - 12, ay + 40), (cx + 14, ay + 42)
        b += line(x + 10, ay, ax1, ay) + line(ax2, ay, x + w - 10, ay)
        b += f'<path d="M{ax1} {ay} Q{(ax1 + l[0]) / 2 + 4} {ay + 2} {l[0]} {l[1]}" class="f-l" {st}/>'
        rc = (cx + 26, ay - 2) if n == 'II' else ((ax2 + r[0]) / 2 - 4, ay + 2)
        b += f'<path d="M{ax2} {ay} Q{rc[0]} {rc[1]} {r[0]} {r[1]}" class="f-l" {st}/>'
        d = 'stroke-dasharray="3 3"'
        b += f'<line x1="{l[0]}" y1="{l[1]}" x2="{cx - 6}" y2="160" class="f-l" {d}/>'
        if n != 'II':
            b += f'<line x1="{r[0]}" y1="{r[1]}" x2="{cx + 18}" y2="160" class="f-l" {d}/>'
        else:
            b += f'<line x1="{cx + 18}" y1="160" x2="{cx + 12}" y2="140" class="f-l" {d}/>'
        b += T(x + 12, 84, 'Atrium', 'f-s', 'start') + T(x + 12, 178, 'Ventricle', 'f-s', 'start')
        b += T(cx, 202, cause, 'f-s')
    return svg(246, b)


def ffr():
    return tiles([('50%', ['Left main narrowing', 'on angiography'], 'b1'), ('70%', ['Other major artery', 'narrowing'], 'b1'),
                  ('0.80 or less', ['Fractional flow reserve', '(adenosine)'], 'warn'),
                  ('0.89 or less', ['Wave-free ratio', '(no drug)'], 'warn')], 100)


def skeleton():
    b = T(360, 16, 'Anterior', 'f-s') + T(360, 340, 'Posterior', 'f-s') + T(700, 16, "Patient's right", 'f-s', 'end') + T(20, 16, "Patient's left", 'f-s', 'start')
    b += '<circle cx="335" cy="64" r="34" class="f-b0"/>' + T(335, 68, 'Pulmonary', 'f-s')
    b += '<circle cx="365" cy="150" r="42" class="f-warn"/>' + T(365, 154, 'Aortic', 'f-h')
    b += '<ellipse cx="270" cy="238" rx="72" ry="52" class="f-b1"/>' + T(270, 242, 'Mitral', 'f-h')
    b += '<ellipse cx="470" cy="238" rx="66" ry="54" class="f-b1"/>' + T(470, 242, 'Tricuspid', 'f-h')
    b += '<circle cx="372" cy="208" r="6" class="f-ah"/><circle cx="312" cy="186" r="5" class="f-ah"/>'
    b += T(14, 96, ['Pulmonary valve:', 'no fibrous annulus'], 'f-s', 'start') + line(140, 92, 300, 70)
    b += T(14, 150, ['Aortomitral curtain', 'between the trigones'], 'f-s', 'start') + line(150, 152, 306, 184)
    b += T(14, 222, ['Circumflex artery', 'along the lateral', 'annulus'], 'f-s', 'start') + line(128, 232, 198, 236)
    b += T(14, 318, 'Coronary sinus behind the posterior annulus', 'f-s', 'start') + line(200, 306, 250, 292)
    b += T(706, 150, ['Bundle of His pierces', 'the right trigone'], 'f-s', 'end') + line(560, 152, 380, 206)
    b += T(706, 318, 'Node at the septal annulus (triangle of Koch)', 'f-s', 'end') + line(470, 306, 420, 278)
    return svg(346, b)


def koch():
    b = T(12, 20, 'Right atrium opened, septum facing', 'f-h', 'start')
    b += '<ellipse cx="150" cy="235" rx="52" ry="34" class="f-b0"/>' + T(150, 239, 'IVC', 'f-s')
    b += '<ellipse cx="215" cy="110" rx="62" ry="44" class="f-b0"/>' + T(215, 114, 'Fossa ovalis', 'f-s')
    b += '<polygon points="470,62 318,214 548,226" class="f-warn"/>'
    b += '<circle cx="318" cy="214" r="24" class="f-b1"/>' + T(318, 256, 'Coronary sinus', 'f-s')
    b += '<path d="M470 62 Q575 120 548 226 Q530 262 470 274" class="f-l" fill="none" style="stroke-width:3px"/>'
    b += T(590, 150, ['Septal leaflet', 'annulus'], 'f-s', 'start')
    b += T(330, 120, ['Tendon of', 'Todaro'], 'f-s', 'end') + line(336, 122, 392, 138)
    b += '<circle cx="445" cy="170" r="9" class="f-ah"/>' + T(445, 200, 'Node', 'f-h')
    b += arrow(450, 158, 466, 78) + T(480, 50, 'His bundle to the apex', 'f-s', 'start')
    return svg(290, b)


def pressures():
    st = [('Venae cavae', '2 to 6', '70%', 'b1'), ('Right atrium', '2 to 6', '72%', 'b1'), ('Right ventricle', '25/3', '70%', 'b1'),
          ('Pulmonary artery', '25/10', '70%', 'b1'), ('Left atrium', '6 to 12', '100%', 'warn'), ('Left ventricle', '120/5', '100%', 'warn'),
          ('Aorta', '120/80', '100%', 'warn')]
    b = ''
    for i, (n, p, sat, cls) in enumerate(st):
        x = 8 + i * 102
        b += f'<rect x="{x}" y="10" width="92" height="96" rx="9" class="f-{cls}"/>'
        nm = n.split(' ')
        b += T(x + 46, 30, nm if len(nm) > 1 else [n, ''], 'f-s') + T(x + 46, 74, p, 'f-h') + T(x + 46, 94, 'sat ' + sat, 'f-s')
        if i < 6:
            b += arrow(x + 92, 58, x + 101, 58)
    b += T(360, 126, 'Pressures in mmHg. From right ventricle to pulmonary artery only the diastolic changes.', 'f-s')
    return svg(136, b)


def cvpwave():
    pts = [(30, 120), (70, 112), (120, 52), (165, 92), (195, 78), (240, 108), (300, 132), (360, 110), (420, 62), (470, 100), (520, 126), (570, 116), (620, 110), (665, 60), (700, 90)]
    d = f'M{pts[0][0]} {pts[0][1]}'
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {p2[0]} {p2[1]}'
    b = line(30, 150, 700, 150, 'f-grid')
    b += f'<path d="{d}" class="f-l" fill="none" style="stroke-width:3px"/>'
    for x, y, t in [(120, 38, 'a'), (197, 64, 'c'), (300, 148, 'x'), (420, 48, 'v'), (520, 142, 'y'), (665, 46, 'a')]:
        b += T(x, y, t, 'f-h')
    b += T(30, 176, ['a: atrial contraction', 'c: tricuspid closes and bulges'], 'f-s', 'start')
    b += T(270, 176, ['x: atrium relaxes, annulus descends', 'v: venous filling against a closed valve'], 'f-s', 'start')
    b += T(560, 176, ['y: valve opens,', 'atrium empties'], 'f-s', 'start')
    return svg(206, b)


def toeviews():
    b = box(10, 10, 150, 44, 'Upper oesophageal', 'b0', 'f-h') + box(170, 10, 540, 44, 'Arch long and short axis, pulmonary artery: dissection, duct', 'b0', 'f-s')
    b += box(10, 64, 150, 112, 'Mid-oesophageal', 'b1', 'f-h')
    b += box(170, 64, 174, 50, ['Four and five chamber', 'valves, septa, walls'], 'b1', 'f-s')
    b += box(353, 64, 174, 50, ['Mitral commissural', 'P3-P2-P1, A3-A2-A1'], 'b1', 'f-s')
    b += box(536, 64, 174, 50, ['Long axis', 'outflow, root, ascending'], 'b1', 'f-s')
    b += box(170, 126, 265, 50, ['Aortic valve short axis', 'cusps and coronary ostia'], 'b1', 'f-s')
    b += box(445, 126, 265, 50, ['Bicaval', 'cannula and wire position, septum'], 'b1', 'f-s')
    b += box(10, 186, 150, 50, 'Transgastric', 'warn', 'f-h')
    b += box(170, 186, 265, 50, ['Short axis', 'regional wall motion, filling'], 'warn', 'f-s')
    b += box(445, 186, 265, 50, ['Deep transgastric', 'prosthesis gradient, paravalvar leak'], 'warn', 'f-s')
    return svg(246, b)


def ivc():
    return tiles([('3 to 5 mmHg', ['Under 2.1 cm,', 'collapses over 50% on sniff'], 'ok'), ('8 mmHg', ['Under 2.1 cm,', 'does not collapse'], 'b1'),
                  ('15 mmHg', ['Over 2.1 cm,', 'does not collapse'], 'warn')], 100)


def hiatus():
    return tiles([('T8', ['Vena cava, right phrenic', '(central tendon)'], 'b1'), ('T10', ['Oesophagus, vagi', '(within the right crus)'], 'b0'),
                  ('T12', ['Aorta, azygos vein,', 'thoracic duct'], 'warn')], 100)


def ablate():
    b = box(10, 10, 345, 34, 'Immediate: usable in an emergency', 'ok', 'f-h') + box(365, 10, 345, 34, 'Delayed: not in an emergency', 'warn', 'f-h')
    for i, t in enumerate(['Laser', 'Electrocautery', 'Argon plasma', 'Stent']):
        b += box(10 + (i % 2) * 177, 54 + (i // 2) * 44, 168, 36, t, 'b0', 'f-s')
    for i, t in enumerate(['Cryotherapy', 'Photodynamic therapy', 'Brachytherapy']):
        b += box(365, 54 + i * 44, 345, 36, t, 'b0', 'f-s')
    b += box(10, 142, 345, 36, 'Balloon: immediate, rarely definitive', 'b0', 'f-s')
    return svg(188, b)


def nodereach():
    cols = ['2', '4', '7', '5', '10', '11', '8']
    rows = [('Cervical mediastinoscopy', '1110000'), ('Anterior mediastinotomy', '0001000'), ('EBUS', '1110110'), ('Oesophageal ultrasound', '0000001')]
    b = T(250, 24, 'Station', 'f-s', 'end')
    for j, c in enumerate(cols):
        b += T(290 + j * 60, 24, c, 'f-h')
    for i, (n, m) in enumerate(rows):
        y = 36 + i * 40
        b += T(250, y + 22, n, '', 'end')
        for j, v in enumerate(m):
            cls = 'ok' if v == '1' else 'track'
            b += f'<rect x="{264 + j * 60}" y="{y}" width="52" height="32" rx="6" class="f-{cls}"/>'
    b += T(12, 216, 'Paratracheal 2 and 4, subcarinal 7, aortopulmonary 5, hilar 10, interlobar 11, para-oesophageal 8.', 'f-s', 'start')
    return svg(228, b)


def calgb():
    h, b = bars([('Disease-free: sublobar', 63.6, 'b1'), ('Disease-free: lobectomy', 64.1, 'b0'),
                 ('Overall: sublobar', 80.3, 'b1'), ('Overall: lobectomy', 78.9, 'b0')], '%', 100,
                'Five-year survival, tumours of 2 cm or less, node negative', 230)
    return svg(h, b)


def nett():
    return tiles([('0.47', ['Risk ratio for death:', 'upper lobe, low exercise'], 'ok'), ('1.01', ['Risk ratio for death:', 'all patients'], 'b0'),
                  ('2.06', ['Risk ratio for death:', 'non-upper lobe, high exercise'], 'warn')], 100)


FIGS = {k: v for k, v in globals().items() if callable(v) and k not in
        ('svg', 'T', 'box', 'arrow', 'line', 'bars', 'tiles', 'E')}
