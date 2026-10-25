#!/usr/bin/env python3
"""Generates the static pages of bekol-libi.co.il. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
DOMAIN = "https://bekol-libi.co.il"

PHONE = "0549986355"
PHONE_INTL = "972549986355"
EMAIL = "bekol.libi@gmail.com"
ADDRESS = "בזלת 296, ניל״י"
FACEBOOK = ("https://www.facebook.com/%D7%91%D7%A7%D7%95%D7%9C-%D7%9C%D7%99%D7%91%D7%99-"
            "%D7%90%D7%99%D7%9E%D7%95%D7%9F-%D7%95%D7%AA%D7%A8%D7%A4%D7%99%D7%94-%D7%91%D7%A7%D7%95%D7%9C-"
            "%D7%95%D7%91%D7%9E%D7%95%D7%A1%D7%99%D7%A7%D7%94-102213501276837/")
WHATSAPP = f"https://wa.me/{PHONE_INTL}"

# (slug, nav label) — slugs match the old WordPress URLs so existing links keep working
PAGES = [
    ("", "ראשי"),
    ("הקליניקה", "הקליניקה"),
    ("אודות", "מי אני?"),
    ("טיפול-במוסיקה", "טיפול במוסיקה"),
    ("צור-קשר", "יצירת קשר"),
]

ICON = {
    "guitar": '<svg viewBox="0 0 512 512"><path d="M502.6 54.6 457.4 9.4a32 32 0 0 0-45.3 0l-45.2 45.3a32 32 0 0 0-7.5 33.1l-63 63a128 128 0 0 0-76.9-1.6c-27.5 8-46.8 28.9-54 52.6-4.3 14-16.6 24.3-31.3 25.7C99 230 69 243 47 265c-58.4 58.4-62.3 149.2-1.6 210s151.6 56.8 210-1.6c22-22 35-52 37.4-86.5 1.4-14.7 11.7-27 25.7-31.3 23.7-7.2 44.6-26.5 52.6-54a128 128 0 0 0-1.6-76.9l63-63a32 32 0 0 0 33.1-7.5l45.3-45.2a32 32 0 0 0 0-45.3zM208 352a48 48 0 1 1 0-96 48 48 0 0 1 0 96z"/></svg>',
    "music": '<svg viewBox="0 0 512 512"><path d="M470.4 1.5A32 32 0 0 1 480 24v344c0 44.2-43 80-96 80s-96-35.8-96-80 43-80 96-80c11.2 0 22 1.6 32 4.6V147l-256 76.8V432c0 44.2-43 80-96 80S-32 476.2-32 432s43-80 96-80c11.2 0 22 1.6 32 4.6V128a32 32 0 0 1 22.8-30.6l320-96a32 32 0 0 1 31.6 0z" transform="translate(32 0)"/></svg>',
    "pin": '<svg viewBox="0 0 384 512"><path d="M172.3 501.7C27 291 0 269.4 0 192 0 86 86 0 192 0s192 86 192 192c0 77.4-27 99-172.3 309.7a24 24 0 0 1-39.4 0zM192 272a80 80 0 1 0 0-160 80 80 0 0 0 0 160z"/></svg>',
    "mail": '<svg viewBox="0 0 512 512"><path d="M48 64a48 48 0 0 0-28.8 86.4l217.6 163.2a32 32 0 0 0 38.4 0l217.6-163.2A48 48 0 0 0 464 64H48zM0 176v208a64 64 0 0 0 64 64h384a64 64 0 0 0 64-64V176L294.4 339.2a64 64 0 0 1-76.8 0L0 176z"/></svg>',
    "phone": '<svg viewBox="0 0 512 512"><path d="M164.9 24.6A40 40 0 0 0 117.4 1.4L29.4 25.4A40 40 0 0 0 0 64c0 247.4 200.6 448 448 448a40 40 0 0 0 38.6-29.5l24-88a40 40 0 0 0-23.2-47.5l-96-40a40 40 0 0 0-46.4 11.6L304.7 368A338 338 0 0 1 144 207.3l49.3-40.4a40 40 0 0 0 11.6-46.4l-40-96z"/></svg>',
    "facebook": '<svg viewBox="0 0 512 512"><path d="M512 256C512 114.6 397.4 0 256 0S0 114.6 0 256c0 120 82.7 220.8 194.2 248.5V334.2h-52.8V256h52.8v-33.7c0-87.1 39.4-127.5 125-127.5 16.2 0 44.2 3.2 55.7 6.4V172c-6-.6-16.5-1-29.6-1-42 0-58.2 15.9-58.2 57.2V256h83.6l-14.4 78.2H287v175.9C413.8 494.8 512 386.9 512 256z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 448 512"><path d="M380.9 97.1A223 223 0 0 0 222 31C98.4 31-2.2 131.6-2.2 255.2c0 39.5 10.3 78.1 29.9 112L-4 480l118.7-31.2a223.4 223.4 0 0 0 107.2 27.3h.1c123.5 0 226.3-100.6 226.3-224.2 0-59.9-25.5-116.1-67.4-158.8zM222 438.3c-33.5 0-66.3-9-94.9-26l-6.8-4-70.4 18.5 18.8-68.7-4.4-7A185.2 185.2 0 0 1 36 255.2C36 152.4 119.6 68.8 222.1 68.8c49.7 0 96.3 19.4 131.4 54.5s56.6 81.7 56.5 131.4c0 102.8-85.7 183.6-188 183.6zm101.9-139c-5.6-2.8-33-16.3-38.1-18.1-5.1-1.9-8.8-2.8-12.5 2.8s-14.4 18.1-17.6 21.9c-3.3 3.7-6.5 4.2-12.1 1.4-33.3-16.6-55.1-29.7-77-67.4-5.8-10 5.8-9.3 16.6-30.8 1.8-3.8.9-7-.5-9.8s-12.5-30.2-17.2-41.3c-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2s-9.7 1.4-14.8 7c-5.1 5.6-19.4 19-19.4 46.3s19.9 53.7 22.6 57.4c2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 33-13.5 37.6-26.5s4.6-24.1 3.2-26.5c-1.3-2.5-5-3.9-10.6-6.6z" transform="translate(4 0)"/></svg>',
}

GALLERY = [
    ("IMG_4057-2.jpg", "חדר הטיפולים"), ("IMG-1026.jpg", "הקליניקה"), ("IMG_3976-2-2-1.jpg", "מפגש טיפולי"),
    ("IMG_0935.jpg", "פינת הנגינה"), ("IMG_3817-2.jpg", "כלי נגינה"), ("IMG_4095-2.jpg", "נגינה בפסנתר"),
    ("IMG_3943-2.jpg", "כלי הקשה"), ("IMG-1021.jpg", "הקליניקה"), ("IMG_4076-2.jpg", "מפגש בקליניקה"),
    ("IMG_3829-2.jpg", "פסנתר"), ("IMG_3951-2.jpg", "גיטרה"), ("IMG_4007-2-1.jpg", "אולפן ההקלטות"),
    ("IMG_0932.jpg", "פינת האולפן"),
]


def layout(slug, title, description, body, base):
    nav = "\n".join(
        f'<li><a href="{base}{s + "/" if s else ""}"{" aria-current=\"page\"" if s == slug else ""}>{label}</a></li>'
        for s, label in PAGES)
    foot_nav = "\n".join(f'<a href="{base}{s + "/" if s else ""}">{label}</a>' for s, label in PAGES)
    full_title = f"{title} - בקול ליבי, טיפול במוסיקה" if slug else "בקול ליבי - טיפול רגשי במוסיקה | שירה כהן"
    canonical = f"{DOMAIN}/{slug + '/' if slug else ''}"
    return f"""<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="he_IL">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/img/IMG_4057-2.jpg">
<link rel="icon" href="{base}assets/img/favicon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alef:wght@400;700&family=M+PLUS+Rounded+1c:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/style.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{base}"><img src="{base}assets/img/logo.png" alt="בקול ליבי - אימון ותרפיה בקול ובמוסיקה" width="85" height="58"></a>
    <button class="nav-toggle" aria-label="תפריט" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul class="nav">
{nav}
    </ul>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <nav>{foot_nav}</nav>
    <div>© בקול ליבי · שירה כהן · <a href="tel:{PHONE}">{PHONE}</a></div>
  </div>
</footer>
<a class="wa-float" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="שליחת הודעת וואטסאפ">{ICON["whatsapp"]}</a>
<script src="{base}assets/main.js" defer></script>
</body>
</html>
"""


def contact_block(base, intro):
    return f"""
<div class="contact-grid">
  <div class="reveal">
    <p>{intro}</p>
    <ul class="contact-info">
      <li>{ICON["pin"]}<span>{ADDRESS}</span></li>
      <li>{ICON["mail"]}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{ICON["phone"]}<a href="tel:{PHONE}">{PHONE}</a></li>
    </ul>
    <div class="social">
      <a class="fb" href="{FACEBOOK}" target="_blank" rel="noopener">{ICON["facebook"]} Facebook</a>
      <a class="wa" href="{WHATSAPP}" target="_blank" rel="noopener">{ICON["whatsapp"]} WhatsApp</a>
    </div>
  </div>
  <form class="form reveal">
    <div><label for="f-name">שם *</label><input id="f-name" name="name" required autocomplete="name"></div>
    <div><label for="f-phone">טלפון</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
    <div class="full"><label for="f-email">אימייל *</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
    <div class="full"><label for="f-msg">הודעה *</label><textarea id="f-msg" name="message" required></textarea></div>
    <div class="full"><button class="btn" type="submit">שלח/י</button></div>
    <p class="note full">לחיצה על "שלח/י" תפתח את תוכנת הדואר שלכם עם ההודעה מוכנה לשליחה.</p>
  </form>
</div>"""


def home(base):
    gallery = "\n".join(
        f'<button type="button"><img src="{base}assets/img/{f}" alt="{alt}" loading="lazy"></button>' for f, alt in GALLERY)
    return f"""
<section class="hero">
  <div class="container">
    <h1>טיפול רגשי במוסיקה</h1>
    <p class="lead">לילדים, בני נוער ומבוגרים, בקליניקה פרטית בניל״י</p>
    <div class="btn-row">
      <a class="btn" href="{base}צור-קשר/">לקביעת פגישה</a>
      <a class="btn ghost" href="{base}טיפול-במוסיקה/">מהו טיפול במוסיקה?</a>
    </div>
  </div>
</section>

<section class="container raised">
  <div class="split">
    <div>
      <div class="icon-badge">{ICON["guitar"]}</div>
      <h2>🎶 מוסיקה 🎶</h2>
      <ul class="music-list">
        <li>מסייעת לנו ליצור יחסים בין אישיים וחברויות חדשות</li>
        <li>משפרת את מצב הרוח שלנו</li>
        <li>מאפשרת לנו לבטא את הרגשות שלנו ולפרוק לחצים</li>
        <li>מסייעת לנו להתמודד עם אתגרי החיים</li>
        <li>והיא תופסת מקום מרכזי ביותר בחיינו</li>
      </ul>
    </div>
    <img class="photo" src="{base}assets/img/IMG_4057-2.jpg" alt="חדר הטיפולים בקליניקה" loading="lazy">
  </div>
</section>

<section class="section">
  <div class="container prose reveal">
    <div class="icon-badge" style="margin-inline:auto">{ICON["music"]}</div>
    <h2 class="section-title">החזון שלי</h2>
    <p>אין ספק שהעולם שבחוץ לא תמיד קל ופשוט עבורנו. לאורך השנים אנחנו נאלצים להתמודד עם לא מעט שינויים פיזיים ונפשיים, ועם המון מתחים שהחיים מביאים איתם בכל מיני תקופות שונות בחיינו.</p>
    <p>כל תקופה כזו מביאה איתה מטענים שונים, מעצבת אותנו, ומשפיעה על ההתנהגות וההתנהלות היומיומית שלנו, גם בלי שנהיה מודעים לכך.</p>
    <p>טיפול רגשי במוסיקה ב"קול ליבי" נועד לסייע לילדים, בני נוער ומבוגרים להתמודד עם הקשיים והאתגרים השונים שהם חווים מדי יום, בדרך שונה ויצירתית. השיטה המדהימה הזו מאפשרת לטפל במגוון רחב של בעיות – החל מבעיות רגשיות, חברתיות ולימודיות, ועד להפרעות התנהגות, הפרעות במצב הרוח כמו דיכאון וחרדות, והפרעות קשב וריכוז שהפכו להיות נפוצות מאוד בשנים האחרונות גם בקרב ילדים וגם בקרב מבוגרים.</p>
  </div>
</section>

<section class="section alt">
  <div class="container profile reveal">
    <img src="{base}assets/img/profile.png" alt="שירה כהן" loading="lazy">
    <h2>שירה כהן</h2>
    <p class="role">מטפלת במוסיקה</p>
    <p>נעים להכיר, אני שירה כהן, אמא, זמרת, יוצרת ומטפלת במוסיקה בקליניקה פרטית ובמסגרות של חינוך מיוחד לנוער בסיכון.<br>
    בעלת תואר ראשון B.Ed בחינוך מיוחד לגיל הרך, ותואר שני M.A.A.T בטיפול במוסיקה ובוגרת "רימון בית ספר למוסיקה".</p>
    <a class="btn" href="{base}אודות/">לקריאה נוספת</a>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title reveal">תמונות של הקליניקה</h2>
    <div class="gallery reveal">
{gallery}
    </div>
  </div>
</section>
<div class="lightbox" role="dialog" aria-label="תמונה מוגדלת">
  <button class="lb-close" aria-label="סגירה">×</button>
  <button class="lb-prev" aria-label="הקודמת">›</button>
  <img alt="">
  <button class="lb-next" aria-label="הבאה">‹</button>
</div>

<section class="section alt" id="contact">
  <div class="container">
    <h2 class="section-title reveal">צור קשר</h2>
    {contact_block(base, "לפרטים נוספים וקביעת פגישה")}
  </div>
</section>"""


def about(base):
    return f"""
<section class="hero small"><div class="container"><h1>מי אני?</h1></div></section>
<section class="container raised">
  <div class="split">
    <div>
      <p>נעים להכיר, אני שירה כהן, אמא, זמרת, יוצרת ומטפלת במוסיקה בקליניקה פרטית ובמסגרות של חינוך מיוחד לנוער בסיכון.</p>
      <p>בעלת תואר ראשון B.Ed בחינוך מיוחד לגיל הרך, ותואר שני M.A.A.T בטיפול במוסיקה ובוגרת "רימון בית ספר למוסיקה".</p>
      <p>אני מאמינה שמוסיקה היא מקור לכוח, מהווה עבורנו עוגן ומעניקה לנו ביטחון רב. אני רואה את זה באופן יומיומי, בין היתר בעבודתי עם נערים ונערות בסיכון, שהמוסיקה מאפשרת להם ליצור ולהביע את עצמם בצורה הכי עוצמתית שיש, הרבה מעבר למילים, ומביאה לריפוי פנימי אמיתי של הנפש.</p>
      <p>במשך כעשור עבדתי כגננת בחינוך המיוחד, אבל לא יכולתי להתעלם מהרצון העז והחיבור שלי לצד הרגשי של האדם, מה שהוביל אותי לטיפול הרגשי במוסיקה בו אני עוסקת בשנים האחרונות.</p>
      <p>אין לי ספק שאני מגשימה את החלום שלי כל יום מחדש, וזו זכות גדולה עבורי לשלב בין שני התחומים שאני הכי אוהבת בעולם, מאמינה בהם ומחוברת אליהם בצורה בלתי רגילה –</p>
      <p class="highlight">מוסיקה וטיפול.</p>
    </div>
    <img class="photo tall" src="{base}assets/img/IMG_4130-2.jpg" alt="שירה כהן בקליניקה">
  </div>
</section>
<section class="section"><div class="container" style="text-align:center"><a class="btn" href="{base}צור-קשר/">לקביעת פגישה</a></div></section>"""


def therapy(base):
    return f"""
<section class="hero small"><div class="container"><h1>מהו טיפול במוסיקה ולמי הוא מתאים?</h1></div></section>
<section class="container raised">
  <div class="split reverse">
    <img class="photo tall" src="{base}assets/img/IMG_3976-2-2.jpg" alt="מפגש טיפול במוסיקה">
    <div>
      <p>טיפול במוסיקה (או תרפיה במוסיקה) הוא טיפול נפשי לכל דבר, והוא חלק ממכלול גדול יותר שנקרא "טיפול באומנויות". זוהי שיטת טיפול פסיכולוגית שהיצירה וההבעה הם חלקים בלתי נפרדים ממנה, והיא מאפשרת לנו לטפל בהפרעות נפשיות, בבעיות רגשיות, התנהגותיות וחברתיות בקרב ילדים, מתבגרים ומבוגרים בדרך ייחודית ולא שגרתית.</p>
      <p>טיפול במוסיקה מאפשר לנו לשקם ולרפא את הגוף והנפש באמצעות שירה, נגינה, האזנה לצלילים, כתיבת שירים ואפילו יצירת לחנים חדשים.</p>
      <p>מדובר בטיפול עוצמתי ביותר עבור כל אדם ואדם, וזו דרך מעולה ואפקטיבית שמסייעת לנו להביע רגשות, להתמודד איתם ולעבור תהליכים משמעותיים דרך המוסיקה בתקופות שונות ומשמעותיות בחיינו.</p>
      <a class="btn" href="{base}הקליניקה/">מה מחכה לכם בקליניקה</a>
    </div>
  </div>
</section>
<section class="section"></section>"""


def clinic(base):
    feats = [
        ("IMG_3843-2.jpg", "מגוון שיטות טיפול מעולם המוסיקה", "שירה, אלתור בשירה, כתיבה, הלחנת שירים ויצירת קאברים לשירים מוכרים"),
        ("IMG_3958-2.jpg", "אלתור והבעת רגש באמצעות כלי נגינה שונים", "גיטרות חשמליות, כלי הקשה וכלי נשיפה"),
        ("IMG_4069-2.jpg", "הקלטת שירים באולפן הקלטות", "ביטוי הרגשות השונים בדרך יצירתית ולא שגרתית, וכלי מדהים שמשקף לנו את הכישרון והיכולות הטמונים בנו. באולפן ההקלטות ניתן להקליט שירים מוכרים, ליצור שירים חדשים, ולהישאר עם מזכרת משמעותית שתלווה אותנו לאורך כל החיים."),
        ("img_3773-2-1.jpg", "פיתוח קול טיפולי", "התפתחות אישית ומקצועית וריפוי באמצעות קול ומוסיקה"),
    ]
    cards = "\n".join(
        f'<article class="feature reveal"><img src="{base}assets/img/{img}" alt="{h}" loading="lazy"><div><h3>{h}</h3><p>{p}</p></div></article>'
        for img, h, p in feats)
    return f"""
<section class="hero small">
  <div class="container">
    <h1>להיכנס לקליניקה ולהרגיש בבית…</h1>
    <p class="lead" style="margin-top:1em">להרגיש במקום הכי בטוח שלכם, ולדעת שתצאו ממנו מחוזקים יותר, בטוחים יותר בעצמכם, ועם כלים להתמודד עם העולם שבחוץ.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2 class="section-title reveal">מה מחכה לכם בקליניקה שלי</h2>
    <div class="features">
{cards}
    </div>
  </div>
</section>
<section class="section alt">
  <div class="container prose reveal">
    <ul class="checklist">
      <li>סיוע, תמיכה וליווי מעבר לשעות הטיפול</li>
      <li>הענקת ביטחון למטופל ותמיכה בזמנים קשים</li>
    </ul>
  </div>
</section>"""


def contact(base):
    return f"""
<section class="hero small"><div class="container"><h1>צור קשר</h1></div></section>
<section class="container raised">
  {contact_block(base, "מעניין אתכם לשמוע עוד על טיפול רגשי במוסיקה?<br>מוזמנים להשאיר פרטים בטופס או ליצור איתי קשר")}
</section>
<section class="section"></section>"""


CONTENT = {
    "": ("ראשי", "טיפול רגשי במוסיקה לילדים, בני נוער ומבוגרים - שירה כהן, מטפלת במוסיקה (M.A.A.T), קליניקה פרטית בניל״י.", home),
    "הקליניקה": ("הקליניקה", "הקליניקה של בקול ליבי: שירה, אלתור, כלי נגינה, אולפן הקלטות ופיתוח קול טיפולי.", clinic),
    "אודות": ("מי אני?", "שירה כהן - אמא, זמרת, יוצרת ומטפלת במוסיקה. B.Ed בחינוך מיוחד ו-M.A.A.T בטיפול במוסיקה.", about),
    "טיפול-במוסיקה": ("טיפול במוסיקה", "מהו טיפול במוסיקה ולמי הוא מתאים? טיפול רגשי לילדים, מתבגרים ומבוגרים.", therapy),
    "צור-קשר": ("יצירת קשר", "לפרטים נוספים וקביעת פגישה: 054-9986355, bekol.libi@gmail.com, בזלת 296 ניל״י.", contact),
}

for slug, (title, desc, fn) in CONTENT.items():
    base = "../" if slug else ""
    out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(layout(slug, title, desc, fn(base), base), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))

(ROOT / "CNAME").write_text("bekol-libi.co.il\n")
(ROOT / ".nojekyll").write_text("")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
urls = "\n".join(f"  <url><loc>{DOMAIN}/{s + '/' if s else ''}</loc></url>" for s, _ in PAGES)
(ROOT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
    encoding="utf-8")
(ROOT / "404.html").write_text(layout("404", "הדף לא נמצא", "הדף לא נמצא",
    '<section class="hero small"><div class="container"><h1>הדף לא נמצא</h1>'
    '<p class="lead" style="margin-top:1em">ייתכן שהקישור השתנה.</p><a class="btn" href="/">לדף הבית</a></div></section>',
    "/"), encoding="utf-8")
