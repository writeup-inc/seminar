#!/usr/bin/env python3
"""Render the two AI training individual briefing pages from one design system."""
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
ASSET = '../ai-kenshu-assets/images/'
CATALOG = 'https://writeup-inc.github.io/saas/ai-kenshu-pack/'
CONTACT = 'https://www.writeup.jp/contact/'

PAGES = {
    'ai-kenshu-direct': {
        'title': '企業向けAI活用研修｜個別説明のご案内',
        'description': 'AI活用研修の開催日は調整中です。経営者・人事・現場責任者向けに、業務から考える研修の進め方を個別にご説明します。',
        'audience': '経営者・人事・現場責任者',
        'code': '企業向け AI活用研修',
        'offer': '企業向けAI活用研修の個別説明を受付中',
        'h1': '社員のAI研修、<br>何から始めますか。',
        'hero': '経営者・人事・現場責任者向け。どの業務から始め、誰が何を学ぶかを整理する個別説明です。',
        'hero_img': '../worklog-insight-oem/images/v3/hero.webp',
        'cta': 'AI研修の個別説明を相談する',
        'facts': [('01', '対象業務を決める', 'まず仕事を一つ選ぶ'), ('02', '学ぶ人を決める', '職種と習熟度を確認'), ('03', '学び方を選ぶ', 'オンラインと対面'), ('04', '効果を確かめる', '現場での使い方を見る')],
        'contents_title': '個別説明でわかる、<br>AI研修の始め方。',
        'contents_intro': '対象業務を選び、学ぶ人と方法、研修後の確かめ方まで順に整理します。',
        'contents_img': 'net.webp',
        'photo_caption': '社員の仕事から、研修を設計する。',
        'contents': [
            ('どの業務から試すか', '頻度が高く、成果を比べやすい業務を一つ選ぶ考え方。'),
            ('何を入力してよいか', '機密情報や個人情報、出力の確認について社内で決めること。'),
            ('誰が何を学ぶか', '基礎をそろえる範囲と、職種・業種に合わせる範囲。'),
            ('研修後に何を見るか', '受講数だけでなく、品質・手戻り・継続利用を見る方法。'),
        ],
        'product_label': 'TRAINING DESIGN',
        'product_title': '学ぶだけで終わらせない、<br>仕事から逆算した研修。',
        'product_intro': 'eラーニングを基本に、必要に応じて講師の訪問も相談できます。研修内容や人数、開始時期は、対象業務を確認してから決めます。',
        'product_img': 'desk.webp',
        'mock_title': '業務から考える研修設計',
        'mock_steps': ['仕事を聞く', '学び方を組む', '現場で試す'],
        'flow': [
            ('01 / LISTEN', '仕事を聞く', '使いたい業務、社員の状況、社内ルールを確認します。'),
            ('02 / LEARN', '学び方を組む', 'オンラインで学ぶ範囲と、対面で深める内容を整理します。'),
            ('03 / APPLY', '現場で試す', '実務で試し、使えた場面と使いにくかった場面を見ます。'),
        ],
        'detail_title': '開催日は調整中。<br>いまは個別説明を受付中です。',
        'detail_intro': '公開セミナーの日時が決まる前に、御社の状況に合わせて内容を聞けます。研修の正式な条件や見積りは、内容を確認した後にご案内します。',
        'details': [('対象', '企業の経営者、人事・教育担当、現場責任者'), ('日時・形式', 'お問い合わせ後に調整します。オンライン・対面の可否もご相談ください。'), ('費用・定員', '公開セミナーの参加費・定員は確認中です。研修費用は個別に確認します。'), ('申込方法', 'お問い合わせフォームに「AI活用研修の直販説明希望」とご記入ください。')],
        'detail_link': '企業向けサービス紹介を見る',
        'detail_url': CATALOG + 'a01/',
        'final_title': '御社の仕事から、<br>研修を考えましょう。',
        'final_intro': '何を教えるかを決める前に、どの仕事に使いたいかを聞かせてください。',
        'final_img': '../worklog-insight-oem/images/v3/night-office.webp',
        'request': ['会社名・対象部署', 'AIを使いたい業務', 'いま困っていること'],
        'photo_credit': 'Pixabayの素材と同サイトのセミナーページの写真を共用。実際の研修・相談風景ではありません。',
    },
    'ai-kenshu-oem': {
        'title': 'AI活用研修OEMパートナー募集｜個別説明',
        'description': 'AI活用研修OEMセミナーの開催日は調整中です。地域の顧客にAI研修を届けたいパートナー候補向けに個別説明を受け付けています。',
        'audience': '地域のパートナー候補',
        'code': 'AI活用研修 OEM',
        'offer': 'AI活用研修のOEMパートナーを募集中',
        'h1': '地域の顧客に、<br>AI研修を届けませんか。',
        'hero': 'AI研修を求める顧客に、貴社と顧客の関係を生かして応える。そのためのOEMパートナー募集です。提供名義を含む取扱条件は個別に確認します。',
        'hero_img': '../worklog-insight-oem/images/v3/hero.webp',
        'cta': 'OEMパートナー説明を相談する',
        'facts': [('01', '2026年度まで', '期間限定の助成2コース'), ('02', '毎月数百本', 'eラーニング研修を制作'), ('03', '売上は5:5', '営業と開発を分担'), ('04', '開発費は弊社', '教材の更新も担う')],
        'facts_label': 'OEMパートナー募集を考える4つの具体',
        'contents_title': 'なぜ今、貴社と<br>AI研修を届けるのか。',
        'contents_intro': 'パートナーを募集する理由を、顧客の課題から提供体制まで順にお伝えします。',
        'contents_img': '../worklog-insight-oem/images/v3/oem-meeting.webp',
        'photo_caption': '顧客との関係から、研修を始める。',
        'contents': [
            ('なぜ今、AI研修なのか', '顧客からAI活用を聞かれたとき、仕事に合う答えが必要です。期間限定の研修助成2コースは2026年度まで。活用の差に、今から向き合います。'),
            ('なぜ自社だけで作らないのか', 'AIの機能が変わるたび、教材の更新が必要です。貴社が顧客を知り、制作と更新は弊社が担うことで、続けられる研修にします。'),
            ('なぜ紹介ではなくOEMなのか', '顧客への提案は貴社が続けます。売上は5:5。貴社名での提供方法や顧客情報の扱いは、個別に条件を確認します。'),
            ('なぜライトアップなのか', 'eラーニング研修を毎月数百本制作。地域・業種の課題に合わせて共同企画し、研修の開発・更新費用を弊社が負担します。'),
        ],
        'contents_note': '助成制度は対象や申請時期に条件があります。期間限定の2コースについては厚生労働省の案内をご確認ください。',
        'contents_source_url': 'https://www.mhlw.go.jp/content/11800000/001514286.pdf',
        'contents_source_url_2': 'https://www.mhlw.go.jp/content/11800000/001687616.pdf',
        'product_label': 'PARTNER MODEL',
        'product_title': '顧客との距離を、<br>研修の強みに変える。',
        'product_intro': '貴社は顧客との関係を保ちながら提案し、ライトアップが研修を開発・更新する。共同企画から受講までの流れを、個別説明で具体化します。',
        'product_img': 'net.webp',
        'mock_title': '地域の顧客へ届ける流れ',
        'mock_steps': ['顧客の仕事を聞く', '研修を組み立てる', '地域へ届ける'],
        'flow': [
            ('01 / LISTEN', '顧客の仕事を聞く', '貴社が業種・職種ごとの困りごとを受け止めます。'),
            ('02 / DESIGN', '研修を組み立てる', '両社でテーマを整理し、ライトアップが教材を開発・更新します。'),
            ('03 / DELIVER', '地域へ届ける', 'eラーニングを軸に、必要に応じた対面研修も検討します。'),
        ],
        'detail_title': '開催日は調整中。<br>まずは貴社と個別に。',
        'detail_intro': '公開セミナーの日時が決まる前に、貴社の顧客と営業地域を聞きながら、取扱いの現実性をご説明します。契約条件は個別に確認します。',
        'details': [('対象', '地域の経営支援会社、士業、金融機関、営業・研修事業者など'), ('日時・形式', 'お問い合わせ後に調整します。形式は個別にご相談ください。'), ('条件', '売上配分は5:5です。販売価格・地域の扱いなどは調整中です。'), ('申込方法', 'お問い合わせフォームに「AI活用研修OEMの個別説明希望」とご記入ください。')],
        'detail_link': 'OEM提供の詳細を見る',
        'detail_url': CATALOG + 'b01/',
        'final_title': 'まず、貴社の顧客を<br>教えてください。',
        'final_intro': '取り扱う商材と顧客の課題が分かれば、研修の届け方を一緒に考えられます。',
        'final_img': '../worklog-insight-oem/images/v3/night-office.webp',
        'request': ['会社名・現在の取扱商材', '主な営業地域', '顧客からよく聞く課題'],
        'photo_credit': 'Pixabayの素材と同サイトのセミナーページの写真を共用。実際のパートナー・研修風景ではありません。',
    },
}


def render(slug, d):
    facts = ''.join(f'<div class="fact"><span class="fact-no mono">{n}</span><strong>{t}</strong><small>{s}</small></div>' for n,t,s in d['facts'])
    contents = ''.join(f'<li><span class="no mono">{i:02d}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for i,(t,p) in enumerate(d['contents'],1))
    flow = ''.join(f'<div class="flow-step"><span class="step-label mono">{n}</span><div><h3>{t}</h3><p>{p}</p></div></div>' for n,t,p in d['flow'])
    mock_steps = ''.join(f'<li><span class="mock-step-no mono">{i:02d}</span><span>{escape(s)}</span></li>' for i,s in enumerate(d['mock_steps'],1))
    details = ''.join(f'<div><dt>{t}</dt><dd>{p}</dd></div>' for t,p in d['details'])
    request = ''.join(f'<li>{s}</li>' for s in d['request'])
    contents_note = ''
    if 'contents_note' in d:
        source_url = d['contents_source_url']
        check_query = quote('人材開発支援助成金の「人への投資促進コース」と「事業展開等リスキリング支援コース」は2026年度までの期間限定か、最新の厚生労働省資料で確認して。出典: ' + source_url)
        contents_note = f'<p class="contents-source">{escape(d["contents_note"])} <a href="{escape(source_url)}" target="_blank" rel="noopener">厚生労働省：事業展開等リスキリング ↗</a> <a href="{escape(d["contents_source_url_2"])}" target="_blank" rel="noopener">厚生労働省：人への投資促進 ↗</a> <a href="https://chatgpt.com/?q={check_query}" target="_blank" rel="noopener">ChatGPTでファクトチェック ↗</a></p>'
    photo = lambda name: name if name.startswith('../') else ASSET + name
    return f'''<!doctype html>
<html lang="ja"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index,follow"><meta name="description" content="{escape(d['description'])}">
<meta name="seminar:title" content="{escape(d['title'])}"><meta name="seminar:summary" content="{escape(d['description'])}">
<meta name="seminar:audience" content="社外"><meta name="seminar:status" content="個別受付">
<title>{escape(d['title'])}</title>
<style>h1,h2,h3,h4,h5,.lead{{word-break:auto-phrase;line-break:strict;overflow-wrap:anywhere}}@supports not (word-break:auto-phrase){{h1,h2,h3,h4,h5,.lead{{word-break:normal}}}} img, svg, video, canvas, iframe {{ max-width: 100%; height: auto; }}</style>
<link rel="stylesheet" href="../ai-kenshu-assets/seminar.css">
</head><body>
<main>
<section class="hero" aria-labelledby="hero-title"><div class="hero-photo" style="background-image:url('{photo(d['hero_img'])}')"></div><div class="hero-veil"></div><div class="hero-frame" aria-hidden="true"><span class="frame-corner tl"></span><span class="frame-corner tr"></span><span class="frame-corner bl"></span><span class="frame-corner br"></span><span class="frame-mark mono"><i></i> AI TRAINING / WORK FIRST</span></div><div class="wrap hero-content"><p class="kicker">{d['code']}</p><h1 id="hero-title">{d['h1']}</h1><p class="hero-offer">{d['offer']}</p><p class="lead">{d['hero']}</p><div class="hero-actions"><a class="btn" href="#contact">{d['cta']} <span aria-hidden="true">↗</span></a></div><p class="hero-status">公開セミナーの開催日は調整中です。</p></div></section>
<div class="facts" aria-label="{escape(d.get('facts_label', '個別説明で確認する4つのこと'))}"><div class="wrap"><div class="facts-grid">{facts}</div></div></div>
<section class="section contents" id="contents" aria-labelledby="contents-title"><div class="wrap"><div class="contents-head"><p class="kicker dark">IN THE BRIEFING</p><h2 id="contents-title">{d['contents_title']}</h2><p class="intro">{d['contents_intro']}</p></div><div class="contents-layout"><figure class="photo-card"><img src="{photo(d['contents_img'])}" alt="{escape('仕事の手元を写したイメージ写真' if slug=='ai-kenshu-direct' else '顧客との打ち合わせを表すイメージ写真')}" loading="lazy"><figcaption>{d['photo_caption']}</figcaption></figure><ol class="content-list">{contents}</ol></div>{contents_note}</div></section>
<section class="section product" aria-labelledby="product-title"><div class="photo-bg" style="background-image:url('{photo(d['product_img'])}')"></div><div class="photo-veil"></div><div class="wrap product-layout"><div class="mock-panel" aria-label="研修設計のイメージ図"><div class="mock-bar"><span class="mock-dot"></span><span class="mock-dot"></span><span class="mock-dot"></span><span class="mono">DESIGN PREVIEW</span></div><div class="mock-body"><p class="mock-eyebrow mono">AI TRAINING / PLANNING</p><h3>{d['mock_title']}</h3><p class="mock-sub">個別説明で、貴社に合う進め方を整理します。</p><ol>{mock_steps}</ol><p class="mock-disclaimer">※ 画面は構成イメージです。実際の提供画面ではありません。</p></div></div><div class="product-copy"><p class="kicker">{d['product_label']}</p><h2 id="product-title">{d['product_title']}</h2><p class="intro">{d['product_intro']}</p><div class="flow" aria-label="ご相談から研修までの流れのイメージ">{flow}</div><p class="flow-note">※ 提供内容・条件は個別に確認します。</p></div></div></section>
<section class="section detail" id="details" aria-labelledby="details-title"><div class="wrap detail-grid"><div><p class="kicker dark">INFORMATION</p><h2 id="details-title">{d['detail_title']}</h2><p class="intro">{d['detail_intro']}</p><a class="text-link" href="{d['detail_url']}">{d['detail_link']} ↗</a></div><div class="info-card"><dl>{details}</dl></div></div></section>
<section class="section final" id="contact" aria-labelledby="contact-title"><div class="photo-bg" style="background-image:url('{photo(d['final_img'])}')"></div><div class="photo-veil"></div><div class="wrap final-grid"><div><p class="kicker">NEXT STEP</p><h2 id="contact-title">{d['final_title']}</h2><p class="intro">{d['final_intro']}</p></div><div class="action-card"><h3>個別説明のお問い合わせ</h3><p>ライトアップの公式フォームに、次の内容を添えてお知らせください。</p><ul>{request}</ul><a class="btn" href="{CONTACT}" target="_blank" rel="noopener">お問い合わせフォームへ <span aria-hidden="true">↗</span></a><p class="note">フォームは別タブで開きます。公開セミナーの日時・参加費・登壇者は調整中です。</p></div></div></section>
</main>
<footer class="foot"><div class="wrap foot-inner"><div><p>株式会社ライトアップ｜AI活用研修</p><p class="credit">写真：{d['photo_credit']}</p></div><nav aria-label="フッターナビ"><a href="{CATALOG}">資料一覧</a><a href="https://www.writeup.jp/company/">運営会社</a><a href="https://www.writeup.jp/privacy/">個人情報保護方針</a></nav></div></footer>
<script src="../ai-kenshu-assets/seminar.js" defer></script>
</body></html>
'''


if __name__ == '__main__':
    for slug, data in PAGES.items():
        (ROOT / slug / 'index.html').write_text(render(slug, data), encoding='utf-8')
