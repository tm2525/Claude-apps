#!/usr/bin/env python3
"""Build the st4 notes app.

  python3 st4-src/build.py            (run from the repository root)

Inputs
  st4-src/content/<slug>.html   topic pages exported from the Claude doc (HTML fragments)
  st4-src/md/<slug>.md          topic pages written as markdown; '!fig name | caption' places a drawing from figs.py
  st4-src/md/<slug>add.md       markdown appended to an existing content page
  st4/img/                      raster figures used by the content pages
Output
  st4/index.html, st4/sw.js, st4/manifest.webmanifest
"""
import hashlib, json, os, re, sys
from html import escape
import markdown
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'st4')
sys.path.insert(0, HERE)
import figs  # noqa: E402

BUILD_DATE = '19 November 2026'

# slug, title, kind   (kind: topic | course | digest | ref | new)
SECTIONS = [
    ('thoracic', 'Thoracic', [
        ('t1', 'Nodules, diagnosis and staging', 'topic'), ('t2', 'Fitness and surgery', 'topic'),
        ('t3', 'SABR and chemoradiotherapy', 'topic'), ('t4', 'Systemic therapy', 'topic'),
        ('t5', 'Small-cell, mediastinum, endocrine', 'topic'), ('t6', 'Guidelines and evidence', 'topic'),
        ('t7', 'Perioperative and emergencies', 'topic'), ('t8', 'MDT cases and teaching points', 'topic'),
        ('t9', 'Operative technique', 'topic'), ('t11', 'Pleura', 'new'), ('t12', 'Airway', 'new'),
        ('t13', 'Chest wall and diaphragm', 'new'), ('t14', 'Emphysema and lung transplantation', 'new'),
        ('t15', 'Cardiothoracic trauma', 'new'), ('t16', 'Trials and staging update', 'new'),
        ('t17', 'Lung function, resection complications, infection', 'new'),
        ('t10', 'TSRA Primer: thoracic', 'digest'), ('thoracic', 'Course day notes', 'course')]),
    ('cardiac', 'Cardiac', [
        ('c1', 'Mitral valve', 'topic'), ('c2', 'Tricuspid valve', 'topic'), ('c3', 'Pulmonary valve', 'topic'),
        ('c4', 'Aortic valve', 'topic'), ('c5', 'Coronary surgery', 'topic'), ('c6', 'Aorta', 'topic'),
        ('c7', 'AF surgery', 'topic'), ('c8', 'Endocarditis', 'topic'), ('c9', 'TOE and CT', 'topic'),
        ('c10', 'Perioperative and safety', 'topic'), ('c11', 'Redo cardiac surgery', 'topic'),
        ('c14', 'Bypass and myocardial protection', 'new'),
        ('c15', 'Circulatory support and heart transplantation', 'new'),
        ('c16', 'Pericardium, tumours and pulmonary embolism', 'new'),
        ('c17', 'Critical care after cardiac surgery', 'new'),
        ('c18', 'Heart failure surgery and rhythm devices', 'new'),
        ('c12', 'TSRA Primer: adult cardiac', 'digest'), ('c13', 'TSRA Primer: critical care', 'digest'),
        ('cardiac', 'Course day notes', 'course')]),
    ('congenital', 'Congenital', [
        ('g1', 'Guidelines and trials', 'topic'), ('g2', 'Lesions and operations', 'topic'),
        ('g3', 'Adult congenital', 'topic'), ('g4', 'Perioperative and transition', 'topic'),
        ('g5', 'Core principles', 'topic'), ('g6', 'Anatomy and physiology', 'topic'),
        ('congenital', 'Course day notes', 'course')]),
    ('ref', 'Reference', [
        ('frcs', 'FRCS syllabus map', 'ref'), ('trials', 'Trials index', 'ref'),
        ('viva', 'Viva points', 'ref'), ('figures', 'Figure gallery', 'ref'), ('flagged', 'Flagged sections', 'ref')]),
]
CRITICAL = [('Aortic dissection', 'c6'), ('Stridor', 't12'), ('Tension pneumothorax', 't11'),
            ('Cardiac tamponade', 'c16'), ('Acute haemothorax', 't15'), ('Low cardiac output', 'c17'),
            ('Endocarditis', 'c8'), ('Respiratory failure after thoracic surgery', 't17'),
            ('Myocardial ischaemia', 'c5')]
INDEX_PROC = [('Coronary bypass', 'c5'), ('Aortic valve replacement', 'c4'), ('Mitral valve replacement', 'c1'),
              ('Anatomical lung resection', 't9'), ('Empyema: decortication', 't11'),
              ('Pneumothorax surgery', 't11'), ('Mediastinal resection', 't5')]


def kebab(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:70]


def fig_html(name, cap):
    return f'<figure class="svgfig">{figs.FIGS[name]()}<figcaption>{escape(cap)}</figcaption></figure>'


def md_to_sections(slug, text):
    """Markdown -> (title, intro_html, [(h2 text, body html)])"""
    toks = {}

    def fig(m):
        k = f'FIGTOKEN{len(toks)}X'
        toks[k] = fig_html(m.group(1).strip(), m.group(2).strip())
        return '\n' + k + '\n'
    text = re.sub(r'^!fig\s+(\w+)\s*\|\s*(.+)$', fig, text, flags=re.M)
    html = markdown.markdown(text, extensions=['tables', 'sane_lists'])
    for k, v in toks.items():
        html = html.replace(f'<p>{k}</p>', v)
    html = html.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
    html = re.sub(r'<p>(Sources?: )', r'<p class="src">\1', html)
    soup = BeautifulSoup(html, 'lxml').body
    title, intro, secs, cur = '', [], [], None
    for el in list(soup.children):
        if getattr(el, 'name', None) == 'h1':
            title = el.get_text()
        elif getattr(el, 'name', None) == 'h2':
            cur = [el.get_text(), []]
            secs.append(cur)
        elif cur is None:
            intro.append(str(el))
        else:
            if getattr(el, 'name', None) == 'h3':
                el['id'] = f'{slug}--{kebab(cur[0])}-{kebab(el.get_text())}'
            cur[1].append(str(el))
    return title, ''.join(intro), [(a, ''.join(b)) for a, b in secs]


def sec_html(slug, h, body):
    return (f'<details class="sec"><summary><h2 id="{slug}--{kebab(h)}">{escape(h)}</h2><small></small></summary>'
            f'<div class="secb">{body}</div></details>')


def load_pages():
    pages = {}
    cdir = os.path.join(HERE, 'content')
    for f in sorted(os.listdir(cdir)):
        if f.endswith('.html'):
            pages[f[:-5]] = open(os.path.join(cdir, f), encoding='utf-8').read()
    mdir = os.path.join(HERE, 'md')
    for f in sorted(os.listdir(mdir)):
        if not f.endswith('.md'):
            continue
        slug = f[:-3]
        text = open(os.path.join(mdir, f), encoding='utf-8').read()
        if slug.endswith('add'):
            base = slug[:-3]
            _, intro, secs = md_to_sections(base, text)
            add = ''.join(sec_html(base, h, b) for h, b in secs)
            pages[base] = pages[base] + f'<div class="grp">Added {BUILD_DATE}</div>' + intro + add
        else:
            title, intro, secs = md_to_sections(slug, text)
            body = ''.join(sec_html(slug, h, b) for h, b in secs)
            pages[slug] = (f'<h1 id="{slug}--top">{escape(title)}</h1><div class="lead">{intro}</div>'
                           f'<div class="grp">Notes</div>{body}')
    return pages


def harvest(pages, titles):
    """Build the trials index, viva page and figure gallery from every page."""
    trials, viva, gallery = [], [], []
    for slug, html in pages.items():
        soup = BeautifulSoup(html, 'lxml')
        last = {'id': '', 'text': ''}
        for el in soup.find_all(['h2', 'h3', 'table', 'figure']):
            if el.name in ('h2', 'h3'):
                if el.get('id'):
                    last = {'id': el['id'], 'text': el.get_text(' ', strip=True)}
                if 'viva' in el.get_text().lower():
                    det = el.find_parent('details')
                    if det and el.name == 'h2':
                        body = det.find('div', class_='secb')
                        inner = body.decode_contents() if body else ''
                    else:
                        parts = []
                        for sib in el.next_siblings:
                            if getattr(sib, 'name', None) in ('h2', 'h3'):
                                break
                            parts.append(str(sib))
                        inner = ''.join(parts)
                    if inner.strip():
                        viva.append((slug, el.get('id', ''), inner))
            elif el.name == 'table':
                th = el.find(['th', 'td'])
                first = th.get_text(' ', strip=True).lower() if th else ''
                if first.startswith('trial') or first.startswith('study'):
                    trials.append((slug, last['id'], last['text'], str(el)))
            else:
                cap = el.find('figcaption')
                img = el.find('img')
                svg = el.find('svg')
                thumb = f'<img loading="lazy" src="{img["src"]}" alt="">' if img else (str(svg) if svg else '')
                if thumb:
                    gallery.append((slug, last['id'], cap.get_text(' ', strip=True) if cap else '', thumb))
    def link(slug, hid, text):
        return f'<a class="back" href="#{slug}{"/" + hid if hid else ""}">{escape(titles[slug])}{" › " + escape(text) if text else ""}</a>'
    t = ('<h1>Trials index</h1><div class="lead"><p>Every table in the notes whose first column is a trial or study, '
         f'gathered in one place: {len(trials)} tables. Tap the blue line to open the source section. '
         'How each figure was checked is stated in that section.</p></div>')
    cur = None
    for slug, hid, text, table in trials:
        if slug != cur:
            t += f'<div class="grp">{escape(titles[slug])}</div>'
            cur = slug
        t += link(slug, hid, text) + f'<div class="tw">{table}</div>'
    v = ('<h1>Viva points</h1><div class="lead"><p>The viva point lists from every topic. '
         'Cover the page and answer aloud before opening a topic.</p></div>')
    for slug, hid, inner in viva:
        v += (f'<details class="sec"><summary><h2 id="viva--{slug}-{kebab(hid)[-30:]}">{escape(titles[slug])}</h2><small></small></summary>'
              f'<div class="secb">{inner}{link(slug, hid, "open the topic")}</div></details>')
    g = (f'<h1>Figure gallery</h1><div class="lead"><p>All {len(gallery)} figures. Tap one to open its section.</p></div>'
         '<div class="gal">')
    for slug, hid, cap, thumb in gallery:
        g += (f'<a class="gi" href="#{slug}{"/" + hid if hid else ""}"><div class="gt">{thumb}</div>'
              f'<span><b>{escape(titles[slug])}</b>{escape(cap[:110])}</span></a>')
    g += '</div>'
    return t, v, g, len(trials), len(viva), len(gallery)


def main():
    pages = load_pages()
    titles, group = {}, {}
    for g, gname, items in SECTIONS:
        for slug, title, kind in items:
            titles[slug] = title
            group[slug] = g
    missing = [s for s in titles if s not in pages and s not in ('trials', 'viva', 'figures', 'flagged')]
    assert not missing, missing
    # tidy every page: lazy images, section counts
    meta = {}
    for slug in list(pages):
        html = pages[slug].replace('<img ', '<img loading="lazy" ')
        html = re.sub(r'<div class="tools">.*?</div>', '', html, flags=re.S)
        pages[slug] = html
        meta[slug] = (html.count('<details class="sec"'), html.count('<figure'))
    t, v, g, nt, nv, ng = harvest(pages, titles)
    pages['trials'], pages['viva'], pages['figures'] = t, v, g
    pages['flagged'] = ('<h1>Flagged sections</h1><div class="lead"><p>Sections you have starred for another look. '
                        'Stars are kept on this device only.</p></div><div id="flaglist"></div>')
    meta['trials'], meta['viva'], meta['figures'], meta['flagged'] = (nt, 0), (nv, 0), (0, ng), (0, 0)

    # navigation and home
    nav = '<a class="nav home" href="#home" data-slug="home">Home</a>'
    home = ''
    for gk, gname, items in SECTIONS:
        nav += f'<div class="navg" data-g="{gk}"><i></i>{gname}</div><div class="navl" data-g="{gk}">'
        tiles = ''
        n = 0
        for slug, title, kind in items:
            if kind in ('topic', 'new', 'digest'):
                n += 1
            badge = {'new': '<em class="new">new</em>', 'digest': '<em>digest</em>', 'course': '<em>course</em>'}.get(kind, '')
            nav += f'<a class="nav" href="#{slug}" data-slug="{slug}" data-g="{gk}">{escape(title)}{badge}</a>'
            ns, nf = meta.get(slug, (0, 0))
            bits = []
            if ns:
                bits.append(f'{ns} {"tables" if slug == "trials" else "sections"}')
            if nf:
                bits.append(f'{nf} figures')
            tiles += (f'<a class="tile" href="#{slug}" data-slug="{slug}"><b>{escape(title)}</b>'
                      f'<span>{" · ".join(bits)}</span>{badge}<i class="tick"></i></a>')
        nav += '</div>'
        home += (f'<section class="hsec" data-g="{gk}"><div class="hh"><h2>{gname}</h2>'
                 f'<span class="prog" data-g="{gk}"></span></div><div class="tiles">{tiles}</div></section>')
    crit = ''.join(f'<a href="#{s}">{escape(n)}</a>' for n, s in CRITICAL)
    idxp = ''.join(f'<a href="#{s}">{escape(n)}</a>' for n, s in INDEX_PROC)
    total_secs = sum(a for s, (a, b) in meta.items() if s not in ('trials', 'viva'))
    home = (f'<div class="hero"><p class="kick">FRCS (C-Th) revision · built {BUILD_DATE}</p>'
            '<h1>Cardiothoracic surgery notes</h1>'
            f'<p>{len(titles) - 5} topics, {total_secs} sections and {ng} figures, each tied to its source. '
            'Search everything from the bar above, or start from a list below.</p>'
            '<a id="resume" class="resume" hidden></a></div>'
            f'<div class="quick crit"><h3>Critical conditions</h3><div>{crit}</div></div>'
            f'<div class="quick"><h3>Index procedures</h3><div>{idxp}</div></div>' + home +
            '<p class="src">Each section says where it came from: read from the guideline or paper, taken from a textbook chapter, '
            'as taught on the course, or from memory. Personal revision notes, not clinical guidance.</p>')

    secs = f'<section id="tab-home" data-slug="home" data-title="Home" data-g="home" hidden>{home}</section>'
    for slug in titles:
        gk = group[slug]
        gname = dict((a, b) for a, b, c in SECTIONS)[gk]
        head = (f'<div class="phead"><span class="crumb"><a href="#home">Home</a> › {gname}</span>'
                f'<div class="pt"><button class="xall" data-o="1">Open all</button><button class="xall" data-o="0">Close all</button>'
                f'<button class="rev" data-slug="{slug}">Mark as revised</button></div></div><div class="chips"></div>')
        secs += (f'<section id="tab-{slug}" data-slug="{slug}" data-title="{escape(titles[slug])}" data-g="{gk}" hidden>'
                 f'{head}{pages[slug]}</section>')

    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    page = tpl.replace('{{NAV}}', nav).replace('{{SECTIONS}}', secs).replace('{{BUILD}}', BUILD_DATE)
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)

    assets = ['./', 'index.html', 'manifest.webmanifest', 'apple-touch-icon.png', 'icon-192.png', 'icon-512.png']
    assets += ['img/' + f for f in sorted(os.listdir(os.path.join(OUT, 'img')))]
    h = hashlib.sha1(page.encode()).hexdigest()[:10]
    sw = ("const CACHE='st4-" + h + "';\nconst ASSETS=" + json.dumps(assets) + ";\n" +
          "self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(CACHE).then(c=>Promise.all(ASSETS.map(a=>c.add(a).catch(()=>{})))))});\n"
          "self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});\n"
          "self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;const u=new URL(e.request.url);if(u.origin!==location.origin)return;"
          "if(e.request.mode==='navigate'){e.respondWith(fetch(e.request).then(r=>{const c=r.clone();caches.open(CACHE).then(x=>x.put('index.html',c));return r}).catch(()=>caches.match('index.html')));return}"
          "e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(n=>{const c=n.clone();caches.open(CACHE).then(x=>x.put(e.request,c));return n})))});\n")
    open(os.path.join(OUT, 'sw.js'), 'w').write(sw)
    print('pages', len(titles), 'sections', total_secs, 'figures', ng, 'trial tables', nt, 'viva lists', nv,
          'bytes', len(page), 'cache', h)


if __name__ == '__main__':
    main()
