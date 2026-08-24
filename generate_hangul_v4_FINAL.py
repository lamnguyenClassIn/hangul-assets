import os

SYLLABLES_DIR = "syllables"
os.makedirs(SYLLABLES_DIR, exist_ok=True)

# Bảng nét Jamo cơ bản kèm Mũi tên & Số thứ tự (Red: Đầu, Blue: Giữa, Green: Cuối)
JAMO_STROKES = {
    'ㄱ': '''<path d="M 20 30 L 75 30 L 75 80" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
           <text x="15" y="25" font-size="12" fill="#D93025" font-weight="bold">1</text>''',
    'ㄴ': '''<path d="M 25 20 L 25 75 L 80 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
           <text x="18" y="18" font-size="12" fill="#D93025" font-weight="bold">1</text>''',
    'ㄷ': '''<path d="M 25 25 L 75 25" stroke="#D93025" stroke-width="7" stroke-linecap="round" fill="none"/>
           <text x="18" y="22" font-size="12" fill="#D93025" font-weight="bold">1</text>
           <path d="M 25 25 L 25 75 L 75 75" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
           <text x="18" y="50" font-size="12" fill="#1A73E8" font-weight="bold">2</text>''',
    'ㄹ': '''<path d="M 25 25 L 75 25 L 75 45 L 25 45 L 25 75 L 75 75" stroke="#D93025" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
           <text x="18" y="22" font-size="12" fill="#D93025" font-weight="bold">1</text>''',
    'ㅇ': '''<ellipse cx="50" cy="50" rx="22" ry="26" stroke="#D93025" stroke-width="7" fill="none"/>
           <text x="46" y="20" font-size="12" fill="#D93025" font-weight="bold">1</text>''',
    'ㅏ': '''<path d="M 30 10 L 30 90" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>
           <text x="20" y="15" font-size="12" fill="#1A73E8" font-weight="bold">1</text>
           <path d="M 30 50 L 75 50" stroke="#1E8E3E" stroke-width="7" stroke-linecap="round" fill="none"/>
           <text x="45" y="42" font-size="12" fill="#1E8E3E" font-weight="bold">2</text>''',
    'ㅜ': '''<path d="M 15 35 L 85 35" stroke="#1A73E8" stroke-width="7" stroke-linecap="round" fill="none"/>
           <text x="10" y="30" font-size="12" fill="#1A73E8" font-weight="bold">1</text>
           <path d="M 50 35 L 50 80" stroke="#1E8E3E" stroke-width="7" stroke-linecap="round" fill="none"/>
           <text x="55" y="55" font-size="12" fill="#1E8E3E" font-weight="bold">2</text>'''
}

def build_full_mizi_svg(char_svg_content):
    return f'''<svg width="1000" height="200" viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .box {{ fill: #FFFFFF; stroke: #CCCCCC; stroke-width: 2; }}
      .grid {{ stroke: #E0E0E0; stroke-width: 1.5; stroke-dasharray: 4 4; }}
    </style>
  </defs>

  <!-- Ô 1: Nét chuẩn + Thứ tự nét + Màu sắc -->
  <g transform="translate(50, 10)">
    <rect x="0" y="0" width="180" height="180" class="box"/>
    <line x1="90" y1="0" x2="90" y2="180" class="grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="grid"/>
    <g transform="scale(1.8)">{char_svg_content}</g>
  </g>

  <!-- Ô 2: Ô tập viết nét mờ (Opacity 25%) -->
  <g transform="translate(280, 10)">
    <rect x="0" y="0" width="180" height="180" class="box"/>
    <line x1="90" y1="0" x2="90" y2="180" class="grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="grid"/>
    <g transform="scale(1.8)" opacity="0.25">{char_svg_content}</g>
  </g>

  <!-- Ô 3: Ô tập viết nét mờ nhẹ (Opacity 12%) -->
  <g transform="translate(510, 10)">
    <rect x="0" y="0" width="180" height="180" class="box"/>
    <line x1="90" y1="0" x2="90" y2="180" class="grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="grid"/>
    <g transform="scale(1.8)" opacity="0.12">{char_svg_content}</g>
  </g>

  <!-- Ô 4: Ô trống cho học sinh tự viết -->
  <g transform="translate(740, 10)">
    <rect x="0" y="0" width="180" height="180" class="box"/>
    <line x1="90" y1="0" x2="90" y2="180" class="grid"/>
    <line x1="0" y1="90" x2="180" y2="90" class="grid"/>
  </g>
</svg>'''

# Ví dụ xuất file 수.svg
su_strokes = JAMO_STROKES['ㅅ'] if 'ㅅ' in JAMO_STROKES else ''
su_strokes += JAMO_STROKES['ㅜ'] if 'ㅜ' in JAMO_STROKES else ''
full_svg = build_full_mizi_svg(su_strokes)

with open(f"{SYLLABLES_DIR}/01268_수.svg", "w", encoding="utf-8") as f:
    f.write(full_svg)

print("Đã tạo file SVG đúc sẵn 4 ô MIZI chuẩn!")