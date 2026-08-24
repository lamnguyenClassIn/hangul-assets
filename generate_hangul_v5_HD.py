import os

SYLLABLES_DIR = "syllables"
os.makedirs(SYLLABLES_DIR, exist_ok=True)

# Bảng Vector HD: Nét chữ dày 12px, Số thứ tự 30px Bold + Viền trắng chống mờ
JAMO_STROKES_HD = {
    'ㄱ': '''
        <path d="M 25 35 L 75 35 L 75 80" stroke="#D93025" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="12" y="32" font-size="30" fill="#D93025" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
    ''',
    'ㄴ': '''
        <path d="M 30 20 L 30 75 L 80 75" stroke="#D93025" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="12" y="25" font-size="30" fill="#D93025" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
    ''',
    'ㄷ': '''
        <path d="M 25 25 L 75 25" stroke="#D93025" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="10" y="25" font-size="30" fill="#D93025" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
        <path d="M 25 25 L 25 75 L 75 75" stroke="#1A73E8" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="10" y="60" font-size="30" fill="#1A73E8" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">2</text>
    ''',
    'ㅅ': '''
        <path d="M 50 20 L 20 80" stroke="#D93025" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="45" y="18" font-size="30" fill="#D93025" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
        <path d="M 45 45 L 80 80" stroke="#1A73E8" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="65" y="55" font-size="30" fill="#1A73E8" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">2</text>
    ''',
    'ㅜ': '''
        <path d="M 15 35 L 85 35" stroke="#1A73E8" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="8" y="30" font-size="30" fill="#1A73E8" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
        <path d="M 50 35 L 50 80" stroke="#1E8E3E" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="58" y="62" font-size="30" fill="#1E8E3E" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">2</text>
    ''',
    'ㅂ': '''
        <path d="M 25 20 L 25 80" stroke="#D93025" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="10" y="25" font-size="30" fill="#D93025" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
        <path d="M 75 20 L 75 80" stroke="#1A73E8" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="82" y="25" font-size="30" fill="#1A73E8" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">2</text>
        <path d="M 25 50 L 75 50" stroke="#1E8E3E" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="45" y="45" font-size="30" fill="#1E8E3E" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">3</text>
        <path d="M 25 80 L 75 80" stroke="#F9AB00" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="45" y="75" font-size="30" fill="#F9AB00" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">4</text>
    ''',
    'ㅏ': '''
        <path d="M 30 10 L 30 90" stroke="#1A73E8" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="12" y="20" font-size="30" fill="#1A73E8" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">1</text>
        <path d="M 30 50 L 75 50" stroke="#1E8E3E" stroke-width="12" stroke-linecap="round" fill="none"/>
        <text x="48" y="42" font-size="30" fill="#1E8E3E" font-weight="bold" font-family="Arial" paint-order="stroke fill" stroke="#FFFFFF" stroke-width="6">2</text>
    '''
}

def create_clean_mizi_row(inner_svg):
    return f'''<svg width="1000" height="200" viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <style>
    .bg-clean {{ fill: #FFFFFF; }}
    .mizi-border {{ fill: #FFFFFF; stroke: #B0B0B0; stroke-width: 3; }}
    .mizi-grid {{ stroke: #D0D0D0; stroke-width: 2; stroke-dasharray: 6 6; }}
  </style>
  <rect width="1000" height="200" class="bg-clean"/>

  <!-- Ô 1: Nét chuẩn HD + Số thứ tự siêu rõ -->
  <g transform="translate(40, 10)">
    <rect width="180" height="180" class="mizi-border"/>
    <line x1="90" y1="0" x2="90" y2="180" class="mizi-grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="mizi-grid"/>
    <g transform="scale(1.8)">{inner_svg}</g>
  </g>

  <!-- Ô 2: Nét mờ 25% -->
  <g transform="translate(280, 10)">
    <rect width="180" height="180" class="mizi-border"/>
    <line x1="90" y1="0" x2="90" y2="180" class="mizi-grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="mizi-grid"/>
    <g transform="scale(1.8)" opacity="0.25">{inner_svg}</g>
  </g>

  <!-- Ô 3: Nét mờ 12% -->
  <g transform="translate(520, 10)">
    <rect width="180" height="180" class="mizi-border"/>
    <line x1="90" y1="0" x2="90" y2="180" class="mizi-grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="mizi-grid"/>
    <g transform="scale(1.8)" opacity="0.12">{inner_svg}</g>
  </g>

  <!-- Ô 4: Ô trống -->
  <g transform="translate(760, 10)">
    <rect width="180" height="180" class="mizi-border"/>
    <line x1="90" y1="0" x2="90" y2="180" class="mizi-grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="mizi-grid"/>
  </g>
</svg>'''

# Sinh lại các file mẫu HD
su_content = JAMO_STROKES_HD['ㅅ'] + JAMO_STROKES_HD['ㅜ']
bak_content = JAMO_STROKES_HD['ㅂ'] + JAMO_STROKES_HD['ㅏ'] + JAMO_STROKES_HD['ㄱ']

with open(f"{SYLLABLES_DIR}/01268_수.svg", "w", encoding="utf-8") as f:
    f.write(create_clean_mizi_row(su_content))

with open(f"{SYLLABLES_DIR}/01824_박.svg", "w", encoding="utf-8") as f:
    f.write(create_clean_mizi_row(bak_content))

print("Tạo xong bộ SVG HD tràn viền sắc nét!")