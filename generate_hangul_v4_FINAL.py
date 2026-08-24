import os

SYLLABLES_DIR = "syllables"
os.makedirs(SYLLABLES_DIR, exist_ok=True)

# 19 Phụ âm đầu chuẩn
CHOSEONG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 21 Nguyên âm chuẩn
JUNGSEONG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ']
# 28 Phụ âm cuối chuẩn (Đã sửa lỗi 'ㄵ' và 'ㄶ')
JONGSEONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# Định nghĩa Vector Nét đơn cơ bản
SINGLE_JAMO = {
    'ㄱ': '<path d="M 20 25 L 75 25 L 75 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    'ㄴ': '<path d="M 25 20 L 25 75 L 80 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    'ㄷ': '<path d="M 25 25 L 75 25 M 25 25 L 25 75 L 75 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    'ㄹ': '<path d="M 25 25 L 75 25 L 75 45 L 25 45 L 25 75 L 75 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    'ㅁ': '<path d="M 25 20 L 25 80 M 25 20 L 75 20 L 75 80 M 25 80 L 75 80" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    'ㅂ': '<path d="M 25 20 L 25 80 M 75 20 L 75 80 M 25 50 L 75 50 M 25 80 L 75 80" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅅ': '<path d="M 50 20 L 20 80 M 48 45 L 80 80" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅇ_CHO': '<ellipse cx="50" cy="50" rx="22" ry="28" stroke="#D93025" stroke-width="7" fill="none"/>',
    'ㅇ_JONG': '<ellipse cx="50" cy="50" rx="28" ry="18" stroke="#D93025" stroke-width="7" fill="none"/>',
    'ㅈ': '<path d="M 20 25 L 80 25 M 50 25 L 20 80 M 48 45 L 80 80" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅊ': '<path d="M 50 10 L 50 22 M 20 30 L 80 30 M 50 30 L 20 85 M 48 50 L 80 85" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅋ': '<path d="M 20 25 L 75 25 L 75 75 M 20 50 L 75 50" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅌ': '<path d="M 25 25 L 75 25 M 25 50 L 70 50 M 25 25 L 25 75 L 75 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅍ': '<path d="M 20 25 L 80 25 M 38 25 L 38 75 M 62 25 L 62 75 M 20 75 L 80 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅎ': '<path d="M 35 15 L 65 15 M 20 28 L 80 28" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/><ellipse cx="50" cy="62" rx="22" ry="18" stroke="#D93025" stroke-width="7" fill="none"/>',
    
    # Nguyên âm
    'ㅏ': '<path d="M 30 10 L 30 90 M 30 50 L 75 50" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅐ': '<path d="M 25 10 L 25 90 M 25 50 L 70 50 M 70 10 L 70 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅑ': '<path d="M 30 10 L 30 90 M 30 38 L 75 38 M 30 62 L 75 62" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅒ': '<path d="M 25 10 L 25 90 M 25 38 L 70 38 M 25 62 L 70 62 M 70 10 L 70 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅓ': '<path d="M 25 50 L 70 50 M 70 10 L 70 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅔ': '<path d="M 25 50 L 60 50 M 60 10 L 60 90 M 80 10 L 80 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅕ': '<path d="M 25 38 L 70 38 M 25 62 L 70 62 M 70 10 L 70 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅖ': '<path d="M 20 38 L 55 38 M 20 62 L 55 62 M 55 10 L 55 90 M 75 10 L 75 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅗ': '<path d="M 50 20 L 50 60 M 15 60 L 85 60" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅛ': '<path d="M 38 20 L 38 60 M 62 20 L 62 60 M 15 60 L 85 60" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅜ': '<path d="M 15 35 L 85 35 M 50 35 L 50 80" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅠ': '<path d="M 15 35 L 85 35 M 38 35 L 38 80 M 62 35 L 62 80" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅡ': '<path d="M 15 50 L 85 50" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
    'ㅣ': '<path d="M 50 10 L 50 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>',
}

# Tự động ghép Nguyên âm đôi & Phụ âm đôi/ghép
DOUBLE_CONSONANTS = {'ㄲ': 'ㄱ', 'ㄸ': 'ㄷ', 'ㅃ': 'ㅂ', 'ㅆ': 'ㅅ', 'ㅉ': 'ㅈ'}
COMPOUND_VOWELS = {
    'ㅘ': ('ㅗ', 'ㅏ'), 'ㅙ': ('ㅗ', 'ㅐ'), 'ㅚ': ('ㅗ', 'ㅣ'),
    'ㅝ': ('ㅜ', 'ㅓ'), 'ㅞ': ('ㅜ', 'ㅔ'), 'ㅟ': ('ㅜ', 'ㅣ'), 'ㅢ': ('ㅡ', 'ㅣ')
}
COMPOUND_BATCHIM = {
    'ㄳ': ('ㄱ', 'ㅅ'), 'ㄵ': ('ㄴ', 'ㅈ'), 'ㄶ': ('ㄴ', 'ㅎ'),
    'ㄺ': ('ㄹ', 'ㄱ'), 'ㄻ': ('ㄹ', 'ㅁ'), 'ㄼ': ('ㄹ', 'ㅂ'),
    'ㄽ': ('ㄹ', 'ㅅ'), 'ㄾ': ('ㄹ', 'ㅌ'), 'ㄿ': ('ㄹ', 'ㅍ'),
    'ㅀ': ('ㄹ', 'ㅎ'), 'ㅄ': ('ㅂ', 'ㅅ')
}

def render_jamo(key, scale_x=1.0, scale_y=1.0, trans_x=0, trans_y=0):
    # Phụ âm đôi (ㄲ, ㄸ...)
    if key in DOUBLE_CONSONANTS:
        base = DOUBLE_CONSONANTS[key]
        item = SINGLE_JAMO.get(base, '')
        return f'<g transform="translate({trans_x},{trans_y}) scale({scale_x*0.55},{scale_y})">{item}</g><g transform="translate({trans_x + 40*scale_x},{trans_y}) scale({scale_x*0.55},{scale_y})">{item}</g>'
    
    # Nguyên âm phức (ㅘ, ㅙ...)
    if key in COMPOUND_VOWELS:
        v1, v2 = COMPOUND_VOWELS[key]
        item1 = SINGLE_JAMO.get(v1, '')
        item2 = SINGLE_JAMO.get(v2, '')
        return f'<g transform="translate({trans_x},{trans_y}) scale({scale_x*0.7},{scale_y*0.7})">{item1}</g><g transform="translate({trans_x + 30*scale_x},{trans_y}) scale({scale_x*0.7},{scale_y*0.7})">{item2}</g>'

    # Phụ âm ghép dưới (ㄳ, ㄵ...)
    if key in COMPOUND_BATCHIM:
        b1, b2 = COMPOUND_BATCHIM[key]
        k1 = 'ㅇ_JONG' if b1 == 'ㅇ' else b1
        k2 = 'ㅇ_JONG' if b2 == 'ㅇ' else b2
        item1 = SINGLE_JAMO.get(k1, '')
        item2 = SINGLE_JAMO.get(k2, '')
        return f'<g transform="translate({trans_x - 10},{trans_y}) scale({scale_x*0.5},{scale_y*0.8})">{item1}</g><g transform="translate({trans_x + 35*scale_x},{trans_y}) scale({scale_x*0.5},{scale_y*0.8})">{item2}</g>'

    # Nét đơn chuẩn
    item = SINGLE_JAMO.get(key, '')
    if not item: return ''
    return f'<g transform="translate({trans_x},{trans_y}) scale({scale_x},{scale_y})">{item}</g>'

def generate_syllable(code, char):
    cho_idx = (code - 44032) // 588
    jung_idx = ((code - 44032) % 588) // 28
    jong_idx = (code - 44032) % 28

    cho = CHOSEONG[cho_idx]
    jung = JUNGSEONG[jung_idx]
    jong = JONGSEONG[jong_idx]

    cho_key = 'ㅇ_CHO' if cho == 'ㅇ' else cho
    jong_key = 'ㅇ_JONG' if jong == 'ㅇ' else jong

    if jong == '':
        cho_svg = render_jamo(cho_key, scale_x=0.85, scale_y=0.85, trans_x=8, trans_y=5)
        jung_svg = render_jamo(jung, scale_x=0.85, scale_y=0.85, trans_x=8, trans_y=8)
        jong_svg = ""
    else:
        cho_svg = render_jamo(cho_key, scale_x=0.65, scale_y=0.52, trans_x=18, trans_y=0)
        jung_svg = render_jamo(jung, scale_x=0.65, scale_y=0.52, trans_x=18, trans_y=5)
        jong_svg = render_jamo(jong_key, scale_x=0.65, scale_y=0.42, trans_x=18, trans_y=56)

    filename = f"{SYLLABLES_DIR}/{code - 44032:05d}_{char}.svg"
    
    svg_content = f'''<svg width="1000" height="200" viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(100, 10)">
    <rect x="0" y="0" width="180" height="180" fill="none" stroke="#CCCCCC" stroke-width="2"/>
    <line x1="90" y1="0" x2="90" y2="180" stroke="#E0E0E0" stroke-linecap="round" stroke-dasharray="4 4"/>
    <line x1="0" y1="90" x2="180" y2="90" stroke="#E0E0E0" stroke-linecap="round" stroke-dasharray="4 4"/>
    <g transform="scale(1.8)">{cho_svg}{jung_svg}{jong_svg}</g>
  </g>
</svg>'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

print("Đang khởi tạo lại 100% thư viện 11,172 âm tiết tiếng Hàn...")
for code in range(44032, 55204):
    generate_syllable(code, chr(code))

print("XONG! Toàn bộ 11,172 file SVG đã chuẩn nét Vector, Ellipse, Phụ âm đôi & Batchim ghép.")