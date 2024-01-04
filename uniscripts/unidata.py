'''Unicode lookup data generated from http://ftp.unicode.org/Public/UNIDATA'''
# pylint: disable=too-many-lines, line-too-long
SCRIPT_ABBREVS  = {
    'Yiii': 'Yi',
    'Mani': 'Manichaean',
    'Geor': 'Georgian',
    'Lydi': 'Lydian',
    'Ethi': 'Ethiopic',
    'Buhd': 'Buhid',
    'Hira': 'Hiragana',
    'Elba': 'Elbasan',
    'Arab': 'Arabic',
    'Kthi': 'Kaithi',
    'Gujr': 'Gujarati',
    'Limb': 'Limbu',
    'Beng': 'Bengali',
    'Knda': 'Kannada',
    'Phlp': 'Psalter_Pahlavi',
    'Hebr': 'Hebrew',
    'Sind': 'Khudawadi',
    'Armi': 'Imperial_Aramaic',
    'Hrkt': 'Katakana_Or_Hiragana',
    'Sidd': 'Siddham',
    'Saur': 'Saurashtra',
    'Hang': 'Hangul',
    'Lina': 'Linear_A',
    'Kali': 'Kayah_Li',
    'Prti': 'Inscriptional_Parthian',
    'Takr': 'Takri',
    'Khmr': 'Khmer',
    'Cans': 'Canadian_Aboriginal',
    'Phnx': 'Phoenician',
    'Sinh': 'Sinhala',
    'Mand': 'Mandaic',
    'Phag': 'Phags_Pa',
    'Linb': 'Linear_B',
    'Avst': 'Avestan',
    'Samr': 'Samaritan',
    'Orkh': 'Old_Turkic',
    'Thaa': 'Thaana',
    'Bamu': 'Bamum',
    'Bugi': 'Buginese',
    'Kana': 'Katakana',
    'Lyci': 'Lycian',
    'Copt': 'Coptic',
    'Laoo': 'Lao',
    'Mong': 'Mongolian',
    'Ugar': 'Ugaritic',
    'Goth': 'Gothic',
    'Vaii': 'Vai',
    'Brah': 'Brahmi',
    'Rjng': 'Rejang',
    'Xpeo': 'Old_Persian',
    'Aghb': 'Caucasian_Albanian',
    'Merc': 'Meroitic_Cursive',
    'Modi': 'Modi',
    'Cprt': 'Cypriot',
    'Egyp': 'Egyptian_Hieroglyphs',
    'Tibt': 'Tibetan',
    'Zzzz': 'Unknown',
    'Armn': 'Armenian',
    'Sora': 'Sora_Sompeng',
    'Mend': 'Mende_Kikakui',
    'Perm': 'Old_Permic',
    'Plrd': 'Miao',
    'Lepc': 'Lepcha',
    'Khoj': 'Khojki',
    'Mtei': 'Meetei_Mayek',
    'Orya': 'Oriya',
    'Bopo': 'Bopomofo',
    'Hano': 'Hanunoo',
    'Osma': 'Osmanya',
    'Brai': 'Braille',
    'Sarb': 'Old_South_Arabian',
    'Cher': 'Cherokee',
    'Java': 'Javanese',
    'Mymr': 'Myanmar',
    'Xsux': 'Cuneiform',
    'Pauc': 'Pau_Cin_Hau',
    'Bass': 'Bassa_Vah',
    'Sylo': 'Syloti_Nagri',
    'Zinh': 'Inherited',
    'Mlym': 'Malayalam',
    'Tavt': 'Tai_Viet',
    'Hani': 'Han',
    'Glag': 'Glagolitic',
    'Cham': 'Cham',
    'Nbat': 'Nabataean',
    'Tagb': 'Tagbanwa',
    'Khar': 'Kharoshthi',
    'Ital': 'Old_Italic',
    'Tirh': 'Tirhuta',
    'Latn': 'Latin',
    'Dsrt': 'Deseret',
    'Bali': 'Balinese',
    'Cari': 'Carian',
    'Tfng': 'Tifinagh',
    'Cyrl': 'Cyrillic',
    'Sund': 'Sundanese',
    'Guru': 'Gurmukhi',
    'Tglg': 'Tagalog',
    'Lisu': 'Lisu',
    'Runr': 'Runic',
    'Palm': 'Palmyrene',
    'Narb': 'Old_North_Arabian',
    'Cakm': 'Chakma',
    'Dupl': 'Duployan',
    'Mahj': 'Mahajani',
    'Tale': 'Tai_Le',
    'Talu': 'New_Tai_Lue',
    'Shaw': 'Shavian',
    'Gran': 'Grantha',
    'Lana': 'Tai_Tham',
    'Deva': 'Devanagari',
    'Telu': 'Telugu',
    'Mroo': 'Mro',
    'Wara': 'Warang_Citi',
    'Hmng': 'Pahawh_Hmong',
    'Taml': 'Tamil',
    'Phli': 'Inscriptional_Pahlavi',
    'Olck': 'Ol_Chiki',
    'Ogam': 'Ogham',
    'Zyyy': 'Common',
    'Batk': 'Batak',
    'Thai': 'Thai',
    'Grek': 'Greek',
    'Mero': 'Meroitic_Hieroglyphs',
    'Nkoo': 'Nko',
    'Syrc': 'Syriac',
    'Shrd': 'Sharada',
}

BUCKETS = [
    [ # 0x0 -> 0x3f
        [ 0x3f, ['Common']],
    ],
    [ # 0x40 -> 0x7f
        [ 0x40, ['Common']],
        [ 0x5a, ['Latin']],
        [ 0x60, ['Common']],
        [ 0x61, ['Latin', 'Common']],
        [ 0x7a, ['Latin']],
        [ 0x7f, ['Common']],
    ],
    [ # 0x80 -> 0xbf
        [ 0xa9, ['Common']],
        [ 0xab, ['Latin', 'Common']],
        [ 0xb9, ['Common']],
        [ 0xbb, ['Latin', 'Common']],
        [ 0xbf, ['Common']],
    ],
    [ # 0xc0 -> 0xff
        [ 0xc0, ['Latin', 'Common']],
        [ 0xd6, ['Latin']],
        [ 0xd7, ['Common']],
        [ 0xd8, ['Latin', 'Common']],
        [ 0xf6, ['Latin']],
        [ 0xf7, ['Common']],
        [ 0xf8, ['Latin', 'Common']],
        [ 0xff, ['Latin']],
    ],
    [ # 0x100 -> 0x13f
        [ 0x13f, ['Latin']],
    ],
    [ # 0x140 -> 0x17f
        [ 0x17f, ['Latin']],
    ],
    [ # 0x180 -> 0x1bf
        [ 0x1bf, ['Latin']],
    ],
    [ # 0x1c0 -> 0x1ff
        [ 0x1ff, ['Latin']],
    ],
    [ # 0x200 -> 0x23f
        [ 0x23f, ['Latin']],
    ],
    [ # 0x240 -> 0x27f
        [ 0x27f, ['Latin']],
    ],
    [ # 0x280 -> 0x2bf
        [ 0x2b8, ['Latin']],
        [ 0x2bf, ['Common']],
    ],
    [ # 0x2c0 -> 0x2ff
        [ 0x2df, ['Common']],
        [ 0x2e4, ['Latin']],
        [ 0x2e9, ['Common']],
        [ 0x2eb, ['Bopomofo']],
        [ 0x2ff, ['Common']],
    ],
    [ # 0x300 -> 0x33f
        [ 0x33f, ['Inherited']],
    ],
    [ # 0x340 -> 0x37f
        [ 0x341, ['Inherited']],
        [ 0x343, ['Inherited', 'Greek']],
        [ 0x344, ['Inherited']],
        [ 0x346, ['Inherited', 'Greek']],
        [ 0x362, ['Inherited']],
        [ 0x36f, ['Latin', 'Inherited']],
        [ 0x373, ['Greek']],
        [ 0x374, ['Common']],
        [ 0x375, ['Greek', 'Common']],
        [ 0x377, ['Greek']],
        [ 0x379, ['Unknown']],
        [ 0x37d, ['Greek']],
        [ 0x37e, ['Common']],
        [ 0x37f, ['Greek', 'Common']],
    ],
    [ # 0x380 -> 0x3bf
        [ 0x380, ['Greek']],
        [ 0x383, ['Unknown']],
        [ 0x384, ['Greek']],
        [ 0x388, ['Greek', 'Common']],
        [ 0x38a, ['Greek']],
        [ 0x38b, ['Unknown']],
        [ 0x3a1, ['Greek']],
        [ 0x3a2, ['Unknown']],
        [ 0x3bf, ['Greek']],
    ],
    [ # 0x3c0 -> 0x3ff
        [ 0x3e1, ['Greek']],
        [ 0x3ef, ['Coptic']],
        [ 0x3ff, ['Greek']],
    ],
    [ # 0x400 -> 0x43f
        [ 0x43f, ['Cyrillic']],
    ],
    [ # 0x440 -> 0x47f
        [ 0x47f, ['Cyrillic']],
    ],
    [ # 0x480 -> 0x4bf
        [ 0x484, ['Cyrillic']],
        [ 0x486, ['Latin', 'Cyrillic', 'Inherited']],
        [ 0x4bf, ['Cyrillic']],
    ],
    [ # 0x4c0 -> 0x4ff
        [ 0x4ff, ['Cyrillic']],
    ],
    [ # 0x500 -> 0x53f
        [ 0x52f, ['Cyrillic']],
        [ 0x530, ['Unknown']],
        [ 0x53f, ['Armenian']],
    ],
    [ # 0x540 -> 0x57f
        [ 0x556, ['Armenian']],
        [ 0x558, ['Unknown']],
        [ 0x55f, ['Armenian']],
        [ 0x560, ['Unknown']],
        [ 0x57f, ['Armenian']],
    ],
    [ # 0x580 -> 0x5bf
        [ 0x587, ['Armenian']],
        [ 0x588, ['Unknown']],
        [ 0x58a, ['Armenian', 'Georgian', 'Common']],
        [ 0x58b, ['Armenian']],
        [ 0x58c, ['Unknown']],
        [ 0x590, ['Armenian']],
        [ 0x5bf, ['Hebrew']],
    ],
    [ # 0x5c0 -> 0x5ff
        [ 0x5c8, ['Hebrew']],
        [ 0x5cf, ['Unknown']],
        [ 0x5ea, ['Hebrew']],
        [ 0x5ef, ['Unknown']],
        [ 0x5f4, ['Hebrew']],
        [ 0x5ff, ['Unknown']],
    ],
    [ # 0x600 -> 0x63f
        [ 0x604, ['Arabic']],
        [ 0x605, ['Common']],
        [ 0x606, ['Arabic', 'Common']],
        [ 0x60b, ['Arabic']],
        [ 0x60d, ['Syriac', 'Thaana', 'Arabic', 'Common']],
        [ 0x61a, ['Arabic']],
        [ 0x61c, ['Syriac', 'Thaana', 'Arabic', 'Common']],
        [ 0x61d, ['Common']],
        [ 0x61e, ['Arabic']],
        [ 0x620, ['Syriac', 'Thaana', 'Arabic', 'Common']],
        [ 0x63f, ['Arabic']],
    ],
    [ # 0x640 -> 0x67f
        [ 0x641, ['Psalter_Pahlavi', 'Syriac', 'Manichaean', 'Arabic', 'Mandaic', 'Common']],
        [ 0x64a, ['Arabic']],
        [ 0x655, ['Syriac', 'Inherited', 'Arabic']],
        [ 0x65f, ['Arabic']],
        [ 0x669, ['Thaana', 'Arabic', 'Common']],
        [ 0x66f, ['Arabic']],
        [ 0x671, ['Syriac', 'Inherited', 'Arabic']],
        [ 0x67f, ['Arabic']],
    ],
    [ # 0x680 -> 0x6bf
        [ 0x6bf, ['Arabic']],
    ],
    [ # 0x6c0 -> 0x6ff
        [ 0x6dc, ['Arabic']],
        [ 0x6dd, ['Common']],
        [ 0x6de, ['Arabic', 'Common']],
        [ 0x6ff, ['Arabic']],
    ],
    [ # 0x700 -> 0x73f
        [ 0x700, ['Syriac', 'Arabic']],
        [ 0x70d, ['Syriac']],
        [ 0x70e, ['Unknown']],
        [ 0x73f, ['Syriac']],
    ],
    [ # 0x740 -> 0x77f
        [ 0x74a, ['Syriac']],
        [ 0x74c, ['Unknown']],
        [ 0x74f, ['Syriac']],
        [ 0x77f, ['Arabic']],
    ],
    [ # 0x780 -> 0x7bf
        [ 0x7b2, ['Thaana']],
        [ 0x7bf, ['Unknown']],
    ],
    [ # 0x7c0 -> 0x7ff
        [ 0x7fb, ['Nko']],
        [ 0x7ff, ['Unknown']],
    ],
    [ # 0x800 -> 0x83f
        [ 0x82d, ['Samaritan']],
        [ 0x82f, ['Unknown']],
        [ 0x83e, ['Samaritan']],
        [ 0x83f, ['Unknown']],
    ],
    [ # 0x840 -> 0x87f
        [ 0x85b, ['Mandaic']],
        [ 0x85d, ['Unknown']],
        [ 0x85f, ['Mandaic']],
        [ 0x87f, ['Unknown']],
    ],
    [ # 0x880 -> 0x8bf
        [ 0x89f, ['Unknown']],
        [ 0x8b2, ['Arabic']],
        [ 0x8bf, ['Unknown']],
    ],
    [ # 0x8c0 -> 0x8ff
        [ 0x8e3, ['Unknown']],
        [ 0x8ff, ['Arabic']],
    ],
    [ # 0x900 -> 0x93f
        [ 0x93f, ['Devanagari']],
    ],
    [ # 0x940 -> 0x97f
        [ 0x950, ['Devanagari']],
        [ 0x952, ['Latin', 'Devanagari', 'Inherited']],
        [ 0x963, ['Devanagari']],
        [ 0x964, ['Tamil', 'Devanagari', 'Khudawadi', 'Gujarati', 'Gurmukhi', 'Telugu', 'Syloti_Nagri', 'Tirhuta', 'Grantha', 'Takri', 'Oriya', 'Kannada', 'Mahajani', 'Malayalam', 'Sinhala', 'Common', 'Bengali']],
        [ 0x965, ['Tamil', 'Devanagari', 'Khudawadi', 'Gujarati', 'Gurmukhi', 'Telugu', 'Syloti_Nagri', 'Tirhuta', 'Grantha', 'Takri', 'Oriya', 'Kannada', 'Mahajani', 'Malayalam', 'Sinhala', 'Limbu', 'Common', 'Bengali']],
        [ 0x966, ['Tamil', 'Devanagari', 'Khudawadi', 'Gujarati', 'Gurmukhi', 'Telugu', 'Syloti_Nagri', 'Tirhuta', 'Grantha', 'Takri', 'Oriya', 'Kannada', 'Mahajani', 'Malayalam', 'Kaithi', 'Sinhala', 'Limbu', 'Bengali']],
        [ 0x96f, ['Devanagari', 'Mahajani', 'Kaithi']],
        [ 0x97f, ['Devanagari']],
    ],
    [ # 0x980 -> 0x9bf
        [ 0x983, ['Bengali']],
        [ 0x984, ['Unknown']],
        [ 0x98c, ['Bengali']],
        [ 0x98e, ['Unknown']],
        [ 0x990, ['Bengali']],
        [ 0x992, ['Unknown']],
        [ 0x9a8, ['Bengali']],
        [ 0x9a9, ['Unknown']],
        [ 0x9b0, ['Bengali']],
        [ 0x9b1, ['Unknown']],
        [ 0x9b3, ['Bengali']],
        [ 0x9b5, ['Unknown']],
        [ 0x9b9, ['Bengali']],
        [ 0x9bb, ['Unknown']],
        [ 0x9bf, ['Bengali']],
    ],
    [ # 0x9c0 -> 0x9ff
        [ 0x9c4, ['Bengali']],
        [ 0x9c6, ['Unknown']],
        [ 0x9c8, ['Bengali']],
        [ 0x9ca, ['Unknown']],
        [ 0x9cf, ['Bengali']],
        [ 0x9d6, ['Unknown']],
        [ 0x9d8, ['Bengali']],
        [ 0x9db, ['Unknown']],
        [ 0x9dd, ['Bengali']],
        [ 0x9de, ['Unknown']],
        [ 0x9e3, ['Bengali']],
        [ 0x9e5, ['Unknown']],
        [ 0x9ef, ['Syloti_Nagri', 'Chakma', 'Bengali']],
        [ 0x9fc, ['Bengali']],
        [ 0x9ff, ['Unknown']],
    ],
    [ # 0xa00 -> 0xa3f
        [ 0xa00, ['Unknown']],
        [ 0xa0a, ['Gurmukhi']],
        [ 0xa0e, ['Unknown']],
        [ 0xa10, ['Gurmukhi']],
        [ 0xa12, ['Unknown']],
        [ 0xa28, ['Gurmukhi']],
        [ 0xa29, ['Unknown']],
        [ 0xa30, ['Gurmukhi']],
        [ 0xa31, ['Unknown']],
        [ 0xa33, ['Gurmukhi']],
        [ 0xa34, ['Unknown']],
        [ 0xa36, ['Gurmukhi']],
        [ 0xa37, ['Unknown']],
        [ 0xa39, ['Gurmukhi']],
        [ 0xa3b, ['Unknown']],
        [ 0xa3f, ['Gurmukhi']],
    ],
    [ # 0xa40 -> 0xa7f
        [ 0xa42, ['Gurmukhi']],
        [ 0xa46, ['Unknown']],
        [ 0xa48, ['Gurmukhi']],
        [ 0xa4a, ['Unknown']],
        [ 0xa4d, ['Gurmukhi']],
        [ 0xa50, ['Unknown']],
        [ 0xa52, ['Gurmukhi']],
        [ 0xa58, ['Unknown']],
        [ 0xa5c, ['Gurmukhi']],
        [ 0xa5d, ['Unknown']],
        [ 0xa5f, ['Gurmukhi']],
        [ 0xa65, ['Unknown']],
        [ 0xa76, ['Gurmukhi']],
        [ 0xa7f, ['Unknown']],
    ],
    [ # 0xa80 -> 0xabf
        [ 0xa80, ['Unknown']],
        [ 0xa8d, ['Gujarati']],
        [ 0xa8e, ['Unknown']],
        [ 0xa91, ['Gujarati']],
        [ 0xa92, ['Unknown']],
        [ 0xaa8, ['Gujarati']],
        [ 0xaa9, ['Unknown']],
        [ 0xab0, ['Gujarati']],
        [ 0xab1, ['Unknown']],
        [ 0xab3, ['Gujarati']],
        [ 0xab4, ['Unknown']],
        [ 0xab9, ['Gujarati']],
        [ 0xabb, ['Unknown']],
        [ 0xabf, ['Gujarati']],
    ],
    [ # 0xac0 -> 0xaff
        [ 0xac5, ['Gujarati']],
        [ 0xac6, ['Unknown']],
        [ 0xace, ['Gujarati']],
        [ 0xacf, ['Unknown']],
        [ 0xad1, ['Gujarati']],
        [ 0xadf, ['Unknown']],
        [ 0xae3, ['Gujarati']],
        [ 0xae5, ['Unknown']],
        [ 0xaef, ['Gujarati', 'Khojki']],
        [ 0xaf2, ['Gujarati']],
        [ 0xaff, ['Unknown']],
    ],
    [ # 0xb00 -> 0xb3f
        [ 0xb00, ['Unknown']],
        [ 0xb03, ['Oriya']],
        [ 0xb04, ['Unknown']],
        [ 0xb0c, ['Oriya']],
        [ 0xb0e, ['Unknown']],
        [ 0xb10, ['Oriya']],
        [ 0xb12, ['Unknown']],
        [ 0xb28, ['Oriya']],
        [ 0xb29, ['Unknown']],
        [ 0xb30, ['Oriya']],
        [ 0xb31, ['Unknown']],
        [ 0xb33, ['Oriya']],
        [ 0xb34, ['Unknown']],
        [ 0xb39, ['Oriya']],
        [ 0xb3b, ['Unknown']],
        [ 0xb3f, ['Oriya']],
    ],
    [ # 0xb40 -> 0xb7f
        [ 0xb44, ['Oriya']],
        [ 0xb46, ['Unknown']],
        [ 0xb48, ['Oriya']],
        [ 0xb4a, ['Unknown']],
        [ 0xb4e, ['Oriya']],
        [ 0xb55, ['Unknown']],
        [ 0xb58, ['Oriya']],
        [ 0xb5b, ['Unknown']],
        [ 0xb5d, ['Oriya']],
        [ 0xb5e, ['Unknown']],
        [ 0xb63, ['Oriya']],
        [ 0xb65, ['Unknown']],
        [ 0xb77, ['Oriya']],
        [ 0xb7f, ['Unknown']],
    ],
    [ # 0xb80 -> 0xbbf
        [ 0xb81, ['Unknown']],
        [ 0xb8a, ['Tamil']],
        [ 0xb8d, ['Unknown']],
        [ 0xb90, ['Tamil']],
        [ 0xb91, ['Unknown']],
        [ 0xb95, ['Tamil']],
        [ 0xb98, ['Unknown']],
        [ 0xb9a, ['Tamil']],
        [ 0xb9b, ['Unknown']],
        [ 0xb9f, ['Tamil']],
        [ 0xba2, ['Unknown']],
        [ 0xba4, ['Tamil']],
        [ 0xba7, ['Unknown']],
        [ 0xbaa, ['Tamil']],
        [ 0xbad, ['Unknown']],
        [ 0xbb9, ['Tamil']],
        [ 0xbbd, ['Unknown']],
        [ 0xbbf, ['Tamil']],
    ],
    [ # 0xbc0 -> 0xbff
        [ 0xbc2, ['Tamil']],
        [ 0xbc5, ['Unknown']],
        [ 0xbc8, ['Tamil']],
        [ 0xbc9, ['Unknown']],
        [ 0xbce, ['Tamil']],
        [ 0xbcf, ['Unknown']],
        [ 0xbd1, ['Tamil']],
        [ 0xbd6, ['Unknown']],
        [ 0xbd8, ['Tamil']],
        [ 0xbe5, ['Unknown']],
        [ 0xbfb, ['Tamil']],
        [ 0xbff, ['Unknown']],
    ],
    [ # 0xc00 -> 0xc3f
        [ 0xc03, ['Telugu']],
        [ 0xc04, ['Unknown']],
        [ 0xc0c, ['Telugu']],
        [ 0xc0d, ['Unknown']],
        [ 0xc10, ['Telugu']],
        [ 0xc11, ['Unknown']],
        [ 0xc28, ['Telugu']],
        [ 0xc29, ['Unknown']],
        [ 0xc39, ['Telugu']],
        [ 0xc3c, ['Unknown']],
        [ 0xc3f, ['Telugu']],
    ],
    [ # 0xc40 -> 0xc7f
        [ 0xc44, ['Telugu']],
        [ 0xc45, ['Unknown']],
        [ 0xc48, ['Telugu']],
        [ 0xc49, ['Unknown']],
        [ 0xc4d, ['Telugu']],
        [ 0xc54, ['Unknown']],
        [ 0xc56, ['Telugu']],
        [ 0xc57, ['Unknown']],
        [ 0xc59, ['Telugu']],
        [ 0xc5f, ['Unknown']],
        [ 0xc63, ['Telugu']],
        [ 0xc65, ['Unknown']],
        [ 0xc6f, ['Telugu']],
        [ 0xc77, ['Unknown']],
        [ 0xc7f, ['Telugu']],
    ],
    [ # 0xc80 -> 0xcbf
        [ 0xc80, ['Telugu']],
        [ 0xc83, ['Kannada']],
        [ 0xc84, ['Unknown']],
        [ 0xc8c, ['Kannada']],
        [ 0xc8d, ['Unknown']],
        [ 0xc90, ['Kannada']],
        [ 0xc91, ['Unknown']],
        [ 0xca8, ['Kannada']],
        [ 0xca9, ['Unknown']],
        [ 0xcb3, ['Kannada']],
        [ 0xcb4, ['Unknown']],
        [ 0xcb9, ['Kannada']],
        [ 0xcbb, ['Unknown']],
        [ 0xcbf, ['Kannada']],
    ],
    [ # 0xcc0 -> 0xcff
        [ 0xcc4, ['Kannada']],
        [ 0xcc5, ['Unknown']],
        [ 0xcc8, ['Kannada']],
        [ 0xcc9, ['Unknown']],
        [ 0xccd, ['Kannada']],
        [ 0xcd4, ['Unknown']],
        [ 0xcd6, ['Kannada']],
        [ 0xcdd, ['Unknown']],
        [ 0xce3, ['Kannada']],
        [ 0xce5, ['Unknown']],
        [ 0xcef, ['Kannada']],
        [ 0xcf0, ['Unknown']],
        [ 0xcf2, ['Kannada']],
        [ 0xcff, ['Unknown']],
    ],
    [ # 0xd00 -> 0xd3f
        [ 0xd00, ['Unknown']],
        [ 0xd03, ['Malayalam']],
        [ 0xd04, ['Unknown']],
        [ 0xd0c, ['Malayalam']],
        [ 0xd0d, ['Unknown']],
        [ 0xd10, ['Malayalam']],
        [ 0xd11, ['Unknown']],
        [ 0xd3a, ['Malayalam']],
        [ 0xd3c, ['Unknown']],
        [ 0xd3f, ['Malayalam']],
    ],
    [ # 0xd40 -> 0xd7f
        [ 0xd44, ['Malayalam']],
        [ 0xd45, ['Unknown']],
        [ 0xd48, ['Malayalam']],
        [ 0xd49, ['Unknown']],
        [ 0xd4f, ['Malayalam']],
        [ 0xd56, ['Unknown']],
        [ 0xd58, ['Malayalam']],
        [ 0xd5f, ['Unknown']],
        [ 0xd63, ['Malayalam']],
        [ 0xd65, ['Unknown']],
        [ 0xd75, ['Malayalam']],
        [ 0xd78, ['Unknown']],
        [ 0xd7f, ['Malayalam']],
    ],
    [ # 0xd80 -> 0xdbf
        [ 0xd81, ['Unknown']],
        [ 0xd83, ['Sinhala']],
        [ 0xd84, ['Unknown']],
        [ 0xd96, ['Sinhala']],
        [ 0xd99, ['Unknown']],
        [ 0xdb1, ['Sinhala']],
        [ 0xdb2, ['Unknown']],
        [ 0xdbb, ['Sinhala']],
        [ 0xdbc, ['Unknown']],
        [ 0xdbe, ['Sinhala']],
        [ 0xdbf, ['Unknown']],
    ],
    [ # 0xdc0 -> 0xdff
        [ 0xdc6, ['Sinhala']],
        [ 0xdc9, ['Unknown']],
        [ 0xdcb, ['Sinhala']],
        [ 0xdce, ['Unknown']],
        [ 0xdd4, ['Sinhala']],
        [ 0xdd5, ['Unknown']],
        [ 0xddf, ['Sinhala']],
        [ 0xde5, ['Unknown']],
        [ 0xdef, ['Sinhala']],
        [ 0xdf1, ['Unknown']],
        [ 0xdf5, ['Sinhala']],
        [ 0xdff, ['Unknown']],
    ],
    [ # 0xe00 -> 0xe3f
        [ 0xe00, ['Unknown']],
        [ 0xe3a, ['Thai']],
        [ 0xe3e, ['Unknown']],
        [ 0xe3f, ['Common']],
    ],
    [ # 0xe40 -> 0xe7f
        [ 0xe40, ['Thai', 'Common']],
        [ 0xe5b, ['Thai']],
        [ 0xe7f, ['Unknown']],
    ],
    [ # 0xe80 -> 0xebf
        [ 0xe80, ['Unknown']],
        [ 0xe82, ['Lao']],
        [ 0xe83, ['Unknown']],
        [ 0xe85, ['Lao']],
        [ 0xe86, ['Unknown']],
        [ 0xe88, ['Lao']],
        [ 0xe89, ['Unknown']],
        [ 0xe8b, ['Lao']],
        [ 0xe8c, ['Unknown']],
        [ 0xe8e, ['Lao']],
        [ 0xe93, ['Unknown']],
        [ 0xe97, ['Lao']],
        [ 0xe98, ['Unknown']],
        [ 0xe9f, ['Lao']],
        [ 0xea0, ['Unknown']],
        [ 0xea3, ['Lao']],
        [ 0xea4, ['Unknown']],
        [ 0xea8, ['Lao']],
        [ 0xea9, ['Unknown']],
        [ 0xeab, ['Lao']],
        [ 0xeac, ['Unknown']],
        [ 0xeb9, ['Lao']],
        [ 0xeba, ['Unknown']],
        [ 0xebe, ['Lao']],
        [ 0xebf, ['Unknown']],
    ],
    [ # 0xec0 -> 0xeff
        [ 0xec4, ['Lao']],
        [ 0xec5, ['Unknown']],
        [ 0xecd, ['Lao']],
        [ 0xecf, ['Unknown']],
        [ 0xed9, ['Lao']],
        [ 0xedb, ['Unknown']],
        [ 0xedf, ['Lao']],
        [ 0xeff, ['Unknown']],
    ],
    [ # 0xf00 -> 0xf3f
        [ 0xf3f, ['Tibetan']],
    ],
    [ # 0xf40 -> 0xf7f
        [ 0xf47, ['Tibetan']],
        [ 0xf48, ['Unknown']],
        [ 0xf6c, ['Tibetan']],
        [ 0xf70, ['Unknown']],
        [ 0xf7f, ['Tibetan']],
    ],
    [ # 0xf80 -> 0xfbf
        [ 0xf97, ['Tibetan']],
        [ 0xf98, ['Unknown']],
        [ 0xfbc, ['Tibetan']],
        [ 0xfbd, ['Unknown']],
        [ 0xfbf, ['Tibetan']],
    ],
    [ # 0xfc0 -> 0xfff
        [ 0xfcc, ['Tibetan']],
        [ 0xfcd, ['Unknown']],
        [ 0xfd4, ['Tibetan']],
        [ 0xfd8, ['Common']],
        [ 0xfda, ['Tibetan']],
        [ 0xfff, ['Unknown']],
    ],
    [ # 0x1000 -> 0x103f
        [ 0x103f, ['Myanmar']],
    ],
    [ # 0x1040 -> 0x107f
        [ 0x1049, ['Myanmar', 'Tai_Le', 'Chakma']],
        [ 0x107f, ['Myanmar']],
    ],
    [ # 0x1080 -> 0x10bf
        [ 0x109f, ['Myanmar']],
        [ 0x10bf, ['Georgian']],
    ],
    [ # 0x10c0 -> 0x10ff
        [ 0x10c5, ['Georgian']],
        [ 0x10c6, ['Unknown']],
        [ 0x10c8, ['Georgian']],
        [ 0x10cc, ['Unknown']],
        [ 0x10ce, ['Georgian']],
        [ 0x10cf, ['Unknown']],
        [ 0x10fa, ['Georgian']],
        [ 0x10fb, ['Common']],
        [ 0x10fc, ['Georgian', 'Common']],
        [ 0x10ff, ['Georgian']],
    ],
    [ # 0x1100 -> 0x113f
        [ 0x113f, ['Hangul']],
    ],
    [ # 0x1140 -> 0x117f
        [ 0x117f, ['Hangul']],
    ],
    [ # 0x1180 -> 0x11bf
        [ 0x11bf, ['Hangul']],
    ],
    [ # 0x11c0 -> 0x11ff
        [ 0x11ff, ['Hangul']],
    ],
    [ # 0x1200 -> 0x123f
        [ 0x123f, ['Ethiopic']],
    ],
    [ # 0x1240 -> 0x127f
        [ 0x1248, ['Ethiopic']],
        [ 0x1249, ['Unknown']],
        [ 0x124d, ['Ethiopic']],
        [ 0x124f, ['Unknown']],
        [ 0x1256, ['Ethiopic']],
        [ 0x1257, ['Unknown']],
        [ 0x125d, ['Ethiopic']],
        [ 0x125f, ['Unknown']],
        [ 0x127f, ['Ethiopic']],
    ],
    [ # 0x1280 -> 0x12bf
        [ 0x1288, ['Ethiopic']],
        [ 0x1289, ['Unknown']],
        [ 0x128d, ['Ethiopic']],
        [ 0x128f, ['Unknown']],
        [ 0x12b0, ['Ethiopic']],
        [ 0x12b1, ['Unknown']],
        [ 0x12b5, ['Ethiopic']],
        [ 0x12b7, ['Unknown']],
        [ 0x12be, ['Ethiopic']],
        [ 0x12bf, ['Unknown']],
    ],
    [ # 0x12c0 -> 0x12ff
        [ 0x12c5, ['Ethiopic']],
        [ 0x12c7, ['Unknown']],
        [ 0x12d6, ['Ethiopic']],
        [ 0x12d7, ['Unknown']],
        [ 0x12ff, ['Ethiopic']],
    ],
    [ # 0x1300 -> 0x133f
        [ 0x1310, ['Ethiopic']],
        [ 0x1311, ['Unknown']],
        [ 0x1315, ['Ethiopic']],
        [ 0x1317, ['Unknown']],
        [ 0x133f, ['Ethiopic']],
    ],
    [ # 0x1340 -> 0x137f
        [ 0x135a, ['Ethiopic']],
        [ 0x135c, ['Unknown']],
        [ 0x137c, ['Ethiopic']],
        [ 0x137f, ['Unknown']],
    ],
    [ # 0x1380 -> 0x13bf
        [ 0x1399, ['Ethiopic']],
        [ 0x139f, ['Unknown']],
        [ 0x13bf, ['Cherokee']],
    ],
    [ # 0x13c0 -> 0x13ff
        [ 0x13f4, ['Cherokee']],
        [ 0x13ff, ['Unknown']],
    ],
    [ # 0x1400 -> 0x143f
        [ 0x143f, ['Canadian_Aboriginal']],
    ],
    [ # 0x1440 -> 0x147f
        [ 0x147f, ['Canadian_Aboriginal']],
    ],
    [ # 0x1480 -> 0x14bf
        [ 0x14bf, ['Canadian_Aboriginal']],
    ],
    [ # 0x14c0 -> 0x14ff
        [ 0x14ff, ['Canadian_Aboriginal']],
    ],
    [ # 0x1500 -> 0x153f
        [ 0x153f, ['Canadian_Aboriginal']],
    ],
    [ # 0x1540 -> 0x157f
        [ 0x157f, ['Canadian_Aboriginal']],
    ],
    [ # 0x1580 -> 0x15bf
        [ 0x15bf, ['Canadian_Aboriginal']],
    ],
    [ # 0x15c0 -> 0x15ff
        [ 0x15ff, ['Canadian_Aboriginal']],
    ],
    [ # 0x1600 -> 0x163f
        [ 0x163f, ['Canadian_Aboriginal']],
    ],
    [ # 0x1640 -> 0x167f
        [ 0x167f, ['Canadian_Aboriginal']],
    ],
    [ # 0x1680 -> 0x16bf
        [ 0x169d, ['Ogham']],
        [ 0x169f, ['Unknown']],
        [ 0x16bf, ['Runic']],
    ],
    [ # 0x16c0 -> 0x16ff
        [ 0x16ea, ['Runic']],
        [ 0x16ed, ['Common']],
        [ 0x16f8, ['Runic']],
        [ 0x16ff, ['Unknown']],
    ],
    [ # 0x1700 -> 0x173f
        [ 0x170c, ['Tagalog']],
        [ 0x170d, ['Unknown']],
        [ 0x1714, ['Tagalog']],
        [ 0x171f, ['Unknown']],
        [ 0x1734, ['Hanunoo']],
        [ 0x1736, ['Buhid', 'Tagbanwa', 'Hanunoo', 'Tagalog', 'Common']],
        [ 0x173f, ['Unknown']],
    ],
    [ # 0x1740 -> 0x177f
        [ 0x1753, ['Buhid']],
        [ 0x175f, ['Unknown']],
        [ 0x176c, ['Tagbanwa']],
        [ 0x176d, ['Unknown']],
        [ 0x1770, ['Tagbanwa']],
        [ 0x1771, ['Unknown']],
        [ 0x1773, ['Tagbanwa']],
        [ 0x177f, ['Unknown']],
    ],
    [ # 0x1780 -> 0x17bf
        [ 0x17bf, ['Khmer']],
    ],
    [ # 0x17c0 -> 0x17ff
        [ 0x17de, ['Khmer']],
        [ 0x17df, ['Unknown']],
        [ 0x17e9, ['Khmer']],
        [ 0x17ef, ['Unknown']],
        [ 0x17f9, ['Khmer']],
        [ 0x17ff, ['Unknown']],
    ],
    [ # 0x1800 -> 0x183f
        [ 0x1801, ['Mongolian']],
        [ 0x1803, ['Phags_Pa', 'Mongolian', 'Common']],
        [ 0x1804, ['Mongolian']],
        [ 0x1806, ['Phags_Pa', 'Mongolian', 'Common']],
        [ 0x1819, ['Mongolian']],
        [ 0x181f, ['Unknown']],
        [ 0x183f, ['Mongolian']],
    ],
    [ # 0x1840 -> 0x187f
        [ 0x1877, ['Mongolian']],
        [ 0x187f, ['Unknown']],
    ],
    [ # 0x1880 -> 0x18bf
        [ 0x18ab, ['Mongolian']],
        [ 0x18af, ['Unknown']],
        [ 0x18bf, ['Canadian_Aboriginal']],
    ],
    [ # 0x18c0 -> 0x18ff
        [ 0x18f5, ['Canadian_Aboriginal']],
        [ 0x18ff, ['Unknown']],
    ],
    [ # 0x1900 -> 0x193f
        [ 0x191e, ['Limbu']],
        [ 0x191f, ['Unknown']],
        [ 0x192b, ['Limbu']],
        [ 0x192f, ['Unknown']],
        [ 0x193b, ['Limbu']],
        [ 0x193f, ['Unknown']],
    ],
    [ # 0x1940 -> 0x197f
        [ 0x1941, ['Limbu']],
        [ 0x1943, ['Unknown']],
        [ 0x194f, ['Limbu']],
        [ 0x196d, ['Tai_Le']],
        [ 0x196f, ['Unknown']],
        [ 0x1974, ['Tai_Le']],
        [ 0x197f, ['Unknown']],
    ],
    [ # 0x1980 -> 0x19bf
        [ 0x19ab, ['New_Tai_Lue']],
        [ 0x19af, ['Unknown']],
        [ 0x19bf, ['New_Tai_Lue']],
    ],
    [ # 0x19c0 -> 0x19ff
        [ 0x19c9, ['New_Tai_Lue']],
        [ 0x19cf, ['Unknown']],
        [ 0x19db, ['New_Tai_Lue']],
        [ 0x19dd, ['Unknown']],
        [ 0x19df, ['New_Tai_Lue']],
        [ 0x19ff, ['Khmer']],
    ],
    [ # 0x1a00 -> 0x1a3f
        [ 0x1a1c, ['Buginese']],
        [ 0x1a1d, ['Unknown']],
        [ 0x1a1f, ['Buginese']],
        [ 0x1a3f, ['Tai_Tham']],
    ],
    [ # 0x1a40 -> 0x1a7f
        [ 0x1a5e, ['Tai_Tham']],
        [ 0x1a5f, ['Unknown']],
        [ 0x1a7c, ['Tai_Tham']],
        [ 0x1a7e, ['Unknown']],
        [ 0x1a7f, ['Tai_Tham']],
    ],
    [ # 0x1a80 -> 0x1abf
        [ 0x1a89, ['Tai_Tham']],
        [ 0x1a8f, ['Unknown']],
        [ 0x1a99, ['Tai_Tham']],
        [ 0x1a9f, ['Unknown']],
        [ 0x1aad, ['Tai_Tham']],
        [ 0x1aaf, ['Unknown']],
        [ 0x1abf, ['Inherited']],
    ],
    [ # 0x1ac0 -> 0x1aff
        [ 0x1aff, ['Unknown']],
    ],
    [ # 0x1b00 -> 0x1b3f
        [ 0x1b3f, ['Balinese']],
    ],
    [ # 0x1b40 -> 0x1b7f
        [ 0x1b4b, ['Balinese']],
        [ 0x1b4f, ['Unknown']],
        [ 0x1b7c, ['Balinese']],
        [ 0x1b7f, ['Unknown']],
    ],
    [ # 0x1b80 -> 0x1bbf
        [ 0x1bbf, ['Sundanese']],
    ],
    [ # 0x1bc0 -> 0x1bff
        [ 0x1bf3, ['Batak']],
        [ 0x1bfb, ['Unknown']],
        [ 0x1bff, ['Batak']],
    ],
    [ # 0x1c00 -> 0x1c3f
        [ 0x1c37, ['Lepcha']],
        [ 0x1c3a, ['Unknown']],
        [ 0x1c3f, ['Lepcha']],
    ],
    [ # 0x1c40 -> 0x1c7f
        [ 0x1c49, ['Lepcha']],
        [ 0x1c4c, ['Unknown']],
        [ 0x1c4f, ['Lepcha']],
        [ 0x1c7f, ['Ol_Chiki']],
    ],
    [ # 0x1c80 -> 0x1cbf
        [ 0x1cbf, ['Unknown']],
    ],
    [ # 0x1cc0 -> 0x1cff
        [ 0x1cc7, ['Sundanese']],
        [ 0x1ccf, ['Unknown']],
        [ 0x1cd2, ['Devanagari', 'Inherited']],
        [ 0x1cd3, ['Common']],
        [ 0x1cd4, ['Devanagari', 'Inherited', 'Common']],
        [ 0x1ce0, ['Devanagari', 'Inherited']],
        [ 0x1ce1, ['Devanagari', 'Common']],
        [ 0x1ce2, ['Devanagari', 'Inherited', 'Common']],
        [ 0x1ce8, ['Devanagari', 'Inherited']],
        [ 0x1cec, ['Common']],
        [ 0x1ced, ['Devanagari', 'Inherited']],
        [ 0x1cee, ['Devanagari', 'Inherited', 'Common']],
        [ 0x1cf1, ['Common']],
        [ 0x1cf3, ['Devanagari', 'Common']],
        [ 0x1cf4, ['Devanagari', 'Inherited']],
        [ 0x1cf5, ['Devanagari', 'Inherited', 'Common']],
        [ 0x1cf6, ['Common']],
        [ 0x1cf7, ['Unknown']],
        [ 0x1cf9, ['Devanagari', 'Inherited']],
        [ 0x1cff, ['Unknown']],
    ],
    [ # 0x1d00 -> 0x1d3f
        [ 0x1d25, ['Latin']],
        [ 0x1d2a, ['Greek']],
        [ 0x1d2b, ['Cyrillic']],
        [ 0x1d2c, ['Latin', 'Cyrillic']],
        [ 0x1d3f, ['Latin']],
    ],
    [ # 0x1d40 -> 0x1d7f
        [ 0x1d5c, ['Latin']],
        [ 0x1d61, ['Greek']],
        [ 0x1d65, ['Latin']],
        [ 0x1d6a, ['Greek']],
        [ 0x1d77, ['Latin']],
        [ 0x1d78, ['Cyrillic']],
        [ 0x1d79, ['Latin', 'Cyrillic']],
        [ 0x1d7f, ['Latin']],
    ],
    [ # 0x1d80 -> 0x1dbf
        [ 0x1dbe, ['Latin']],
        [ 0x1dbf, ['Greek']],
    ],
    [ # 0x1dc0 -> 0x1dff
        [ 0x1dc1, ['Inherited', 'Greek']],
        [ 0x1df5, ['Inherited']],
        [ 0x1dfb, ['Unknown']],
        [ 0x1dff, ['Inherited']],
    ],
    [ # 0x1e00 -> 0x1e3f
        [ 0x1e3f, ['Latin']],
    ],
    [ # 0x1e40 -> 0x1e7f
        [ 0x1e7f, ['Latin']],
    ],
    [ # 0x1e80 -> 0x1ebf
        [ 0x1ebf, ['Latin']],
    ],
    [ # 0x1ec0 -> 0x1eff
        [ 0x1eff, ['Latin']],
    ],
    [ # 0x1f00 -> 0x1f3f
        [ 0x1f15, ['Greek']],
        [ 0x1f17, ['Unknown']],
        [ 0x1f1d, ['Greek']],
        [ 0x1f1f, ['Unknown']],
        [ 0x1f3f, ['Greek']],
    ],
    [ # 0x1f40 -> 0x1f7f
        [ 0x1f45, ['Greek']],
        [ 0x1f47, ['Unknown']],
        [ 0x1f4d, ['Greek']],
        [ 0x1f4f, ['Unknown']],
        [ 0x1f57, ['Greek']],
        [ 0x1f58, ['Unknown']],
        [ 0x1f7d, ['Greek']],
        [ 0x1f7f, ['Unknown']],
    ],
    [ # 0x1f80 -> 0x1fbf
        [ 0x1fb4, ['Greek']],
        [ 0x1fb5, ['Unknown']],
        [ 0x1fbf, ['Greek']],
    ],
    [ # 0x1fc0 -> 0x1fff
        [ 0x1fc4, ['Greek']],
        [ 0x1fc5, ['Unknown']],
        [ 0x1fd3, ['Greek']],
        [ 0x1fd5, ['Unknown']],
        [ 0x1fdb, ['Greek']],
        [ 0x1fdc, ['Unknown']],
        [ 0x1fef, ['Greek']],
        [ 0x1ff1, ['Unknown']],
        [ 0x1ff4, ['Greek']],
        [ 0x1ff5, ['Unknown']],
        [ 0x1ffe, ['Greek']],
        [ 0x1fff, ['Unknown']],
    ],
    [ # 0x2000 -> 0x203f
        [ 0x200b, ['Common']],
        [ 0x200c, ['Inherited', 'Common']],
        [ 0x200d, ['Inherited']],
        [ 0x203f, ['Common']],
    ],
    [ # 0x2040 -> 0x207f
        [ 0x2064, ['Common']],
        [ 0x2065, ['Unknown']],
        [ 0x2070, ['Common']],
        [ 0x2071, ['Latin', 'Common']],
        [ 0x2072, ['Latin']],
        [ 0x2073, ['Unknown']],
        [ 0x207e, ['Common']],
        [ 0x207f, ['Latin', 'Common']],
    ],
    [ # 0x2080 -> 0x20bf
        [ 0x2080, ['Latin', 'Common']],
        [ 0x208f, ['Common']],
        [ 0x209c, ['Latin']],
        [ 0x209f, ['Unknown']],
        [ 0x20bd, ['Common']],
        [ 0x20bf, ['Unknown']],
    ],
    [ # 0x20c0 -> 0x20ff
        [ 0x20cf, ['Unknown']],
        [ 0x20f0, ['Inherited']],
        [ 0x20ff, ['Unknown']],
    ],
    [ # 0x2100 -> 0x213f
        [ 0x2125, ['Common']],
        [ 0x2127, ['Greek', 'Common']],
        [ 0x2129, ['Common']],
        [ 0x212a, ['Latin', 'Common']],
        [ 0x212b, ['Latin']],
        [ 0x2131, ['Common']],
        [ 0x2132, ['Latin']],
        [ 0x2133, ['Latin', 'Common']],
        [ 0x213f, ['Common']],
    ],
    [ # 0x2140 -> 0x217f
        [ 0x214d, ['Common']],
        [ 0x214e, ['Latin']],
        [ 0x214f, ['Latin', 'Common']],
        [ 0x215f, ['Common']],
        [ 0x217f, ['Latin']],
    ],
    [ # 0x2180 -> 0x21bf
        [ 0x2188, ['Latin']],
        [ 0x218a, ['Common']],
        [ 0x218f, ['Unknown']],
        [ 0x21bf, ['Common']],
    ],
    [ # 0x21c0 -> 0x21ff
        [ 0x21ff, ['Common']],
    ],
    [ # 0x2200 -> 0x223f
        [ 0x223f, ['Common']],
    ],
    [ # 0x2240 -> 0x227f
        [ 0x227f, ['Common']],
    ],
    [ # 0x2280 -> 0x22bf
        [ 0x22bf, ['Common']],
    ],
    [ # 0x22c0 -> 0x22ff
        [ 0x22ff, ['Common']],
    ],
    [ # 0x2300 -> 0x233f
        [ 0x233f, ['Common']],
    ],
    [ # 0x2340 -> 0x237f
        [ 0x237f, ['Common']],
    ],
    [ # 0x2380 -> 0x23bf
        [ 0x23bf, ['Common']],
    ],
    [ # 0x23c0 -> 0x23ff
        [ 0x23fa, ['Common']],
        [ 0x23ff, ['Unknown']],
    ],
    [ # 0x2400 -> 0x243f
        [ 0x2426, ['Common']],
        [ 0x243f, ['Unknown']],
    ],
    [ # 0x2440 -> 0x247f
        [ 0x244a, ['Common']],
        [ 0x245f, ['Unknown']],
        [ 0x247f, ['Common']],
    ],
    [ # 0x2480 -> 0x24bf
        [ 0x24bf, ['Common']],
    ],
    [ # 0x24c0 -> 0x24ff
        [ 0x24ff, ['Common']],
    ],
    [ # 0x2500 -> 0x253f
        [ 0x253f, ['Common']],
    ],
    [ # 0x2540 -> 0x257f
        [ 0x257f, ['Common']],
    ],
    [ # 0x2580 -> 0x25bf
        [ 0x25bf, ['Common']],
    ],
    [ # 0x25c0 -> 0x25ff
        [ 0x25ff, ['Common']],
    ],
    [ # 0x2600 -> 0x263f
        [ 0x263f, ['Common']],
    ],
    [ # 0x2640 -> 0x267f
        [ 0x267f, ['Common']],
    ],
    [ # 0x2680 -> 0x26bf
        [ 0x26bf, ['Common']],
    ],
    [ # 0x26c0 -> 0x26ff
        [ 0x26ff, ['Common']],
    ],
    [ # 0x2700 -> 0x273f
        [ 0x273f, ['Common']],
    ],
    [ # 0x2740 -> 0x277f
        [ 0x277f, ['Common']],
    ],
    [ # 0x2780 -> 0x27bf
        [ 0x27bf, ['Common']],
    ],
    [ # 0x27c0 -> 0x27ff
        [ 0x27ff, ['Common']],
    ],
    [ # 0x2800 -> 0x283f
        [ 0x283f, ['Braille']],
    ],
    [ # 0x2840 -> 0x287f
        [ 0x287f, ['Braille']],
    ],
    [ # 0x2880 -> 0x28bf
        [ 0x28bf, ['Braille']],
    ],
    [ # 0x28c0 -> 0x28ff
        [ 0x28ff, ['Braille']],
    ],
    [ # 0x2900 -> 0x293f
        [ 0x293f, ['Common']],
    ],
    [ # 0x2940 -> 0x297f
        [ 0x297f, ['Common']],
    ],
    [ # 0x2980 -> 0x29bf
        [ 0x29bf, ['Common']],
    ],
    [ # 0x29c0 -> 0x29ff
        [ 0x29ff, ['Common']],
    ],
    [ # 0x2a00 -> 0x2a3f
        [ 0x2a3f, ['Common']],
    ],
    [ # 0x2a40 -> 0x2a7f
        [ 0x2a7f, ['Common']],
    ],
    [ # 0x2a80 -> 0x2abf
        [ 0x2abf, ['Common']],
    ],
    [ # 0x2ac0 -> 0x2aff
        [ 0x2aff, ['Common']],
    ],
    [ # 0x2b00 -> 0x2b3f
        [ 0x2b3f, ['Common']],
    ],
    [ # 0x2b40 -> 0x2b7f
        [ 0x2b73, ['Common']],
        [ 0x2b75, ['Unknown']],
        [ 0x2b7f, ['Common']],
    ],
    [ # 0x2b80 -> 0x2bbf
        [ 0x2b95, ['Common']],
        [ 0x2b97, ['Unknown']],
        [ 0x2bb9, ['Common']],
        [ 0x2bbc, ['Unknown']],
        [ 0x2bbf, ['Common']],
    ],
    [ # 0x2bc0 -> 0x2bff
        [ 0x2bc8, ['Common']],
        [ 0x2bc9, ['Unknown']],
        [ 0x2bd1, ['Common']],
        [ 0x2bff, ['Unknown']],
    ],
    [ # 0x2c00 -> 0x2c3f
        [ 0x2c2e, ['Glagolitic']],
        [ 0x2c2f, ['Unknown']],
        [ 0x2c3f, ['Glagolitic']],
    ],
    [ # 0x2c40 -> 0x2c7f
        [ 0x2c5e, ['Glagolitic']],
        [ 0x2c5f, ['Unknown']],
        [ 0x2c7f, ['Latin']],
    ],
    [ # 0x2c80 -> 0x2cbf
        [ 0x2cbf, ['Coptic']],
    ],
    [ # 0x2cc0 -> 0x2cff
        [ 0x2cf3, ['Coptic']],
        [ 0x2cf8, ['Unknown']],
        [ 0x2cff, ['Coptic']],
    ],
    [ # 0x2d00 -> 0x2d3f
        [ 0x2d25, ['Georgian']],
        [ 0x2d26, ['Unknown']],
        [ 0x2d28, ['Georgian']],
        [ 0x2d2c, ['Unknown']],
        [ 0x2d2e, ['Georgian']],
        [ 0x2d2f, ['Unknown']],
        [ 0x2d3f, ['Tifinagh']],
    ],
    [ # 0x2d40 -> 0x2d7f
        [ 0x2d67, ['Tifinagh']],
        [ 0x2d6e, ['Unknown']],
        [ 0x2d71, ['Tifinagh']],
        [ 0x2d7e, ['Unknown']],
        [ 0x2d7f, ['Tifinagh']],
    ],
    [ # 0x2d80 -> 0x2dbf
        [ 0x2d80, ['Ethiopic', 'Tifinagh']],
        [ 0x2d96, ['Ethiopic']],
        [ 0x2d9f, ['Unknown']],
        [ 0x2da6, ['Ethiopic']],
        [ 0x2da7, ['Unknown']],
        [ 0x2dae, ['Ethiopic']],
        [ 0x2daf, ['Unknown']],
        [ 0x2db6, ['Ethiopic']],
        [ 0x2db7, ['Unknown']],
        [ 0x2dbe, ['Ethiopic']],
        [ 0x2dbf, ['Unknown']],
    ],
    [ # 0x2dc0 -> 0x2dff
        [ 0x2dc6, ['Ethiopic']],
        [ 0x2dc7, ['Unknown']],
        [ 0x2dce, ['Ethiopic']],
        [ 0x2dcf, ['Unknown']],
        [ 0x2dd6, ['Ethiopic']],
        [ 0x2dd7, ['Unknown']],
        [ 0x2dde, ['Ethiopic']],
        [ 0x2ddf, ['Unknown']],
        [ 0x2dff, ['Cyrillic']],
    ],
    [ # 0x2e00 -> 0x2e3f
        [ 0x2e3f, ['Common']],
    ],
    [ # 0x2e40 -> 0x2e7f
        [ 0x2e43, ['Common']],
        [ 0x2e7f, ['Unknown']],
    ],
    [ # 0x2e80 -> 0x2ebf
        [ 0x2e99, ['Han']],
        [ 0x2e9a, ['Unknown']],
        [ 0x2ebf, ['Han']],
    ],
    [ # 0x2ec0 -> 0x2eff
        [ 0x2ef3, ['Han']],
        [ 0x2eff, ['Unknown']],
    ],
    [ # 0x2f00 -> 0x2f3f
        [ 0x2f3f, ['Han']],
    ],
    [ # 0x2f40 -> 0x2f7f
        [ 0x2f7f, ['Han']],
    ],
    [ # 0x2f80 -> 0x2fbf
        [ 0x2fbf, ['Han']],
    ],
    [ # 0x2fc0 -> 0x2fff
        [ 0x2fd5, ['Han']],
        [ 0x2fef, ['Unknown']],
        [ 0x2ffb, ['Common']],
        [ 0x2fff, ['Unknown']],
    ],
    [ # 0x3000 -> 0x303f
        [ 0x3000, ['Common']],
        [ 0x3002, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Yi', 'Han', 'Common']],
        [ 0x3004, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x3005, ['Han', 'Common']],
        [ 0x3007, ['Hiragana', 'Katakana', 'Han', 'Common']],
        [ 0x3012, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Yi', 'Han', 'Common']],
        [ 0x3013, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x301c, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Yi', 'Han', 'Common']],
        [ 0x301f, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x3020, ['Common']],
        [ 0x3021, ['Han', 'Common']],
        [ 0x3029, ['Han']],
        [ 0x302d, ['Bopomofo', 'Inherited', 'Han']],
        [ 0x302f, ['Hangul']],
        [ 0x3031, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x3035, ['Hiragana', 'Katakana', 'Common']],
        [ 0x3036, ['Common']],
        [ 0x3037, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x3038, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han']],
        [ 0x303b, ['Han']],
        [ 0x303d, ['Hiragana', 'Katakana', 'Han', 'Common']],
        [ 0x303f, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
    ],
    [ # 0x3040 -> 0x307f
        [ 0x3040, ['Unknown']],
        [ 0x307f, ['Hiragana']],
    ],
    [ # 0x3080 -> 0x30bf
        [ 0x3096, ['Hiragana']],
        [ 0x3098, ['Unknown']],
        [ 0x309a, ['Hiragana', 'Katakana', 'Inherited']],
        [ 0x309c, ['Hiragana', 'Katakana', 'Common']],
        [ 0x309f, ['Hiragana']],
        [ 0x30a1, ['Hiragana', 'Katakana', 'Common']],
        [ 0x30bf, ['Katakana']],
    ],
    [ # 0x30c0 -> 0x30ff
        [ 0x30fa, ['Katakana']],
        [ 0x30fc, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Yi', 'Han', 'Common']],
        [ 0x30fd, ['Hiragana', 'Katakana', 'Common']],
        [ 0x30ff, ['Katakana']],
    ],
    [ # 0x3100 -> 0x313f
        [ 0x3100, ['Katakana']],
        [ 0x3104, ['Unknown']],
        [ 0x312d, ['Bopomofo']],
        [ 0x3130, ['Unknown']],
        [ 0x313f, ['Hangul']],
    ],
    [ # 0x3140 -> 0x317f
        [ 0x317f, ['Hangul']],
    ],
    [ # 0x3180 -> 0x31bf
        [ 0x318e, ['Hangul']],
        [ 0x318f, ['Unknown']],
        [ 0x319f, ['Hiragana', 'Katakana', 'Han', 'Common']],
        [ 0x31ba, ['Bopomofo']],
        [ 0x31bf, ['Unknown']],
    ],
    [ # 0x31c0 -> 0x31ff
        [ 0x31e3, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x31ef, ['Unknown']],
        [ 0x31ff, ['Katakana']],
    ],
    [ # 0x3200 -> 0x323f
        [ 0x321e, ['Hangul']],
        [ 0x321f, ['Unknown']],
        [ 0x323f, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
    ],
    [ # 0x3240 -> 0x327f
        [ 0x3243, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x325f, ['Common']],
        [ 0x327e, ['Hangul']],
        [ 0x327f, ['Common']],
    ],
    [ # 0x3280 -> 0x32bf
        [ 0x32b0, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x32bf, ['Common']],
    ],
    [ # 0x32c0 -> 0x32ff
        [ 0x32cb, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x32cf, ['Common']],
        [ 0x32fe, ['Katakana']],
        [ 0x32ff, ['Unknown']],
    ],
    [ # 0x3300 -> 0x333f
        [ 0x333f, ['Katakana']],
    ],
    [ # 0x3340 -> 0x337f
        [ 0x3357, ['Katakana']],
        [ 0x3370, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x337a, ['Common']],
        [ 0x337f, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
    ],
    [ # 0x3380 -> 0x33bf
        [ 0x33bf, ['Common']],
    ],
    [ # 0x33c0 -> 0x33ff
        [ 0x33df, ['Common']],
        [ 0x33fe, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0x33ff, ['Common']],
    ],
    [ # 0x3400 -> 0x343f
        [ 0x343f, ['Han']],
    ],
    [ # 0x3440 -> 0x347f
        [ 0x347f, ['Han']],
    ],
    [ # 0x3480 -> 0x34bf
        [ 0x34bf, ['Han']],
    ],
    [ # 0x34c0 -> 0x34ff
        [ 0x34ff, ['Han']],
    ],
    [ # 0x3500 -> 0x353f
        [ 0x353f, ['Han']],
    ],
    [ # 0x3540 -> 0x357f
        [ 0x357f, ['Han']],
    ],
    [ # 0x3580 -> 0x35bf
        [ 0x35bf, ['Han']],
    ],
    [ # 0x35c0 -> 0x35ff
        [ 0x35ff, ['Han']],
    ],
    [ # 0x3600 -> 0x363f
        [ 0x363f, ['Han']],
    ],
    [ # 0x3640 -> 0x367f
        [ 0x367f, ['Han']],
    ],
    [ # 0x3680 -> 0x36bf
        [ 0x36bf, ['Han']],
    ],
    [ # 0x36c0 -> 0x36ff
        [ 0x36ff, ['Han']],
    ],
    [ # 0x3700 -> 0x373f
        [ 0x373f, ['Han']],
    ],
    [ # 0x3740 -> 0x377f
        [ 0x377f, ['Han']],
    ],
    [ # 0x3780 -> 0x37bf
        [ 0x37bf, ['Han']],
    ],
    [ # 0x37c0 -> 0x37ff
        [ 0x37ff, ['Han']],
    ],
    [ # 0x3800 -> 0x383f
        [ 0x383f, ['Han']],
    ],
    [ # 0x3840 -> 0x387f
        [ 0x387f, ['Han']],
    ],
    [ # 0x3880 -> 0x38bf
        [ 0x38bf, ['Han']],
    ],
    [ # 0x38c0 -> 0x38ff
        [ 0x38ff, ['Han']],
    ],
    [ # 0x3900 -> 0x393f
        [ 0x393f, ['Han']],
    ],
    [ # 0x3940 -> 0x397f
        [ 0x397f, ['Han']],
    ],
    [ # 0x3980 -> 0x39bf
        [ 0x39bf, ['Han']],
    ],
    [ # 0x39c0 -> 0x39ff
        [ 0x39ff, ['Han']],
    ],
    [ # 0x3a00 -> 0x3a3f
        [ 0x3a3f, ['Han']],
    ],
    [ # 0x3a40 -> 0x3a7f
        [ 0x3a7f, ['Han']],
    ],
    [ # 0x3a80 -> 0x3abf
        [ 0x3abf, ['Han']],
    ],
    [ # 0x3ac0 -> 0x3aff
        [ 0x3aff, ['Han']],
    ],
    [ # 0x3b00 -> 0x3b3f
        [ 0x3b3f, ['Han']],
    ],
    [ # 0x3b40 -> 0x3b7f
        [ 0x3b7f, ['Han']],
    ],
    [ # 0x3b80 -> 0x3bbf
        [ 0x3bbf, ['Han']],
    ],
    [ # 0x3bc0 -> 0x3bff
        [ 0x3bff, ['Han']],
    ],
    [ # 0x3c00 -> 0x3c3f
        [ 0x3c3f, ['Han']],
    ],
    [ # 0x3c40 -> 0x3c7f
        [ 0x3c7f, ['Han']],
    ],
    [ # 0x3c80 -> 0x3cbf
        [ 0x3cbf, ['Han']],
    ],
    [ # 0x3cc0 -> 0x3cff
        [ 0x3cff, ['Han']],
    ],
    [ # 0x3d00 -> 0x3d3f
        [ 0x3d3f, ['Han']],
    ],
    [ # 0x3d40 -> 0x3d7f
        [ 0x3d7f, ['Han']],
    ],
    [ # 0x3d80 -> 0x3dbf
        [ 0x3dbf, ['Han']],
    ],
    [ # 0x3dc0 -> 0x3dff
        [ 0x3dff, ['Han']],
    ],
    [ # 0x3e00 -> 0x3e3f
        [ 0x3e3f, ['Han']],
    ],
    [ # 0x3e40 -> 0x3e7f
        [ 0x3e7f, ['Han']],
    ],
    [ # 0x3e80 -> 0x3ebf
        [ 0x3ebf, ['Han']],
    ],
    [ # 0x3ec0 -> 0x3eff
        [ 0x3eff, ['Han']],
    ],
    [ # 0x3f00 -> 0x3f3f
        [ 0x3f3f, ['Han']],
    ],
    [ # 0x3f40 -> 0x3f7f
        [ 0x3f7f, ['Han']],
    ],
    [ # 0x3f80 -> 0x3fbf
        [ 0x3fbf, ['Han']],
    ],
    [ # 0x3fc0 -> 0x3fff
        [ 0x3fff, ['Han']],
    ],
    [ # 0x4000 -> 0x403f
        [ 0x403f, ['Han']],
    ],
    [ # 0x4040 -> 0x407f
        [ 0x407f, ['Han']],
    ],
    [ # 0x4080 -> 0x40bf
        [ 0x40bf, ['Han']],
    ],
    [ # 0x40c0 -> 0x40ff
        [ 0x40ff, ['Han']],
    ],
    [ # 0x4100 -> 0x413f
        [ 0x413f, ['Han']],
    ],
    [ # 0x4140 -> 0x417f
        [ 0x417f, ['Han']],
    ],
    [ # 0x4180 -> 0x41bf
        [ 0x41bf, ['Han']],
    ],
    [ # 0x41c0 -> 0x41ff
        [ 0x41ff, ['Han']],
    ],
    [ # 0x4200 -> 0x423f
        [ 0x423f, ['Han']],
    ],
    [ # 0x4240 -> 0x427f
        [ 0x427f, ['Han']],
    ],
    [ # 0x4280 -> 0x42bf
        [ 0x42bf, ['Han']],
    ],
    [ # 0x42c0 -> 0x42ff
        [ 0x42ff, ['Han']],
    ],
    [ # 0x4300 -> 0x433f
        [ 0x433f, ['Han']],
    ],
    [ # 0x4340 -> 0x437f
        [ 0x437f, ['Han']],
    ],
    [ # 0x4380 -> 0x43bf
        [ 0x43bf, ['Han']],
    ],
    [ # 0x43c0 -> 0x43ff
        [ 0x43ff, ['Han']],
    ],
    [ # 0x4400 -> 0x443f
        [ 0x443f, ['Han']],
    ],
    [ # 0x4440 -> 0x447f
        [ 0x447f, ['Han']],
    ],
    [ # 0x4480 -> 0x44bf
        [ 0x44bf, ['Han']],
    ],
    [ # 0x44c0 -> 0x44ff
        [ 0x44ff, ['Han']],
    ],
    [ # 0x4500 -> 0x453f
        [ 0x453f, ['Han']],
    ],
    [ # 0x4540 -> 0x457f
        [ 0x457f, ['Han']],
    ],
    [ # 0x4580 -> 0x45bf
        [ 0x45bf, ['Han']],
    ],
    [ # 0x45c0 -> 0x45ff
        [ 0x45ff, ['Han']],
    ],
    [ # 0x4600 -> 0x463f
        [ 0x463f, ['Han']],
    ],
    [ # 0x4640 -> 0x467f
        [ 0x467f, ['Han']],
    ],
    [ # 0x4680 -> 0x46bf
        [ 0x46bf, ['Han']],
    ],
    [ # 0x46c0 -> 0x46ff
        [ 0x46ff, ['Han']],
    ],
    [ # 0x4700 -> 0x473f
        [ 0x473f, ['Han']],
    ],
    [ # 0x4740 -> 0x477f
        [ 0x477f, ['Han']],
    ],
    [ # 0x4780 -> 0x47bf
        [ 0x47bf, ['Han']],
    ],
    [ # 0x47c0 -> 0x47ff
        [ 0x47ff, ['Han']],
    ],
    [ # 0x4800 -> 0x483f
        [ 0x483f, ['Han']],
    ],
    [ # 0x4840 -> 0x487f
        [ 0x487f, ['Han']],
    ],
    [ # 0x4880 -> 0x48bf
        [ 0x48bf, ['Han']],
    ],
    [ # 0x48c0 -> 0x48ff
        [ 0x48ff, ['Han']],
    ],
    [ # 0x4900 -> 0x493f
        [ 0x493f, ['Han']],
    ],
    [ # 0x4940 -> 0x497f
        [ 0x497f, ['Han']],
    ],
    [ # 0x4980 -> 0x49bf
        [ 0x49bf, ['Han']],
    ],
    [ # 0x49c0 -> 0x49ff
        [ 0x49ff, ['Han']],
    ],
    [ # 0x4a00 -> 0x4a3f
        [ 0x4a3f, ['Han']],
    ],
    [ # 0x4a40 -> 0x4a7f
        [ 0x4a7f, ['Han']],
    ],
    [ # 0x4a80 -> 0x4abf
        [ 0x4abf, ['Han']],
    ],
    [ # 0x4ac0 -> 0x4aff
        [ 0x4aff, ['Han']],
    ],
    [ # 0x4b00 -> 0x4b3f
        [ 0x4b3f, ['Han']],
    ],
    [ # 0x4b40 -> 0x4b7f
        [ 0x4b7f, ['Han']],
    ],
    [ # 0x4b80 -> 0x4bbf
        [ 0x4bbf, ['Han']],
    ],
    [ # 0x4bc0 -> 0x4bff
        [ 0x4bff, ['Han']],
    ],
    [ # 0x4c00 -> 0x4c3f
        [ 0x4c3f, ['Han']],
    ],
    [ # 0x4c40 -> 0x4c7f
        [ 0x4c7f, ['Han']],
    ],
    [ # 0x4c80 -> 0x4cbf
        [ 0x4cbf, ['Han']],
    ],
    [ # 0x4cc0 -> 0x4cff
        [ 0x4cff, ['Han']],
    ],
    [ # 0x4d00 -> 0x4d3f
        [ 0x4d3f, ['Han']],
    ],
    [ # 0x4d40 -> 0x4d7f
        [ 0x4d7f, ['Han']],
    ],
    [ # 0x4d80 -> 0x4dbf
        [ 0x4db5, ['Han']],
        [ 0x4dbf, ['Unknown']],
    ],
    [ # 0x4dc0 -> 0x4dff
        [ 0x4dff, ['Common']],
    ],
    [ # 0x4e00 -> 0x4e3f
        [ 0x4e3f, ['Han']],
    ],
    [ # 0x4e40 -> 0x4e7f
        [ 0x4e7f, ['Han']],
    ],
    [ # 0x4e80 -> 0x4ebf
        [ 0x4ebf, ['Han']],
    ],
    [ # 0x4ec0 -> 0x4eff
        [ 0x4eff, ['Han']],
    ],
    [ # 0x4f00 -> 0x4f3f
        [ 0x4f3f, ['Han']],
    ],
    [ # 0x4f40 -> 0x4f7f
        [ 0x4f7f, ['Han']],
    ],
    [ # 0x4f80 -> 0x4fbf
        [ 0x4fbf, ['Han']],
    ],
    [ # 0x4fc0 -> 0x4fff
        [ 0x4fff, ['Han']],
    ],
    [ # 0x5000 -> 0x503f
        [ 0x503f, ['Han']],
    ],
    [ # 0x5040 -> 0x507f
        [ 0x507f, ['Han']],
    ],
    [ # 0x5080 -> 0x50bf
        [ 0x50bf, ['Han']],
    ],
    [ # 0x50c0 -> 0x50ff
        [ 0x50ff, ['Han']],
    ],
    [ # 0x5100 -> 0x513f
        [ 0x513f, ['Han']],
    ],
    [ # 0x5140 -> 0x517f
        [ 0x517f, ['Han']],
    ],
    [ # 0x5180 -> 0x51bf
        [ 0x51bf, ['Han']],
    ],
    [ # 0x51c0 -> 0x51ff
        [ 0x51ff, ['Han']],
    ],
    [ # 0x5200 -> 0x523f
        [ 0x523f, ['Han']],
    ],
    [ # 0x5240 -> 0x527f
        [ 0x527f, ['Han']],
    ],
    [ # 0x5280 -> 0x52bf
        [ 0x52bf, ['Han']],
    ],
    [ # 0x52c0 -> 0x52ff
        [ 0x52ff, ['Han']],
    ],
    [ # 0x5300 -> 0x533f
        [ 0x533f, ['Han']],
    ],
    [ # 0x5340 -> 0x537f
        [ 0x537f, ['Han']],
    ],
    [ # 0x5380 -> 0x53bf
        [ 0x53bf, ['Han']],
    ],
    [ # 0x53c0 -> 0x53ff
        [ 0x53ff, ['Han']],
    ],
    [ # 0x5400 -> 0x543f
        [ 0x543f, ['Han']],
    ],
    [ # 0x5440 -> 0x547f
        [ 0x547f, ['Han']],
    ],
    [ # 0x5480 -> 0x54bf
        [ 0x54bf, ['Han']],
    ],
    [ # 0x54c0 -> 0x54ff
        [ 0x54ff, ['Han']],
    ],
    [ # 0x5500 -> 0x553f
        [ 0x553f, ['Han']],
    ],
    [ # 0x5540 -> 0x557f
        [ 0x557f, ['Han']],
    ],
    [ # 0x5580 -> 0x55bf
        [ 0x55bf, ['Han']],
    ],
    [ # 0x55c0 -> 0x55ff
        [ 0x55ff, ['Han']],
    ],
    [ # 0x5600 -> 0x563f
        [ 0x563f, ['Han']],
    ],
    [ # 0x5640 -> 0x567f
        [ 0x567f, ['Han']],
    ],
    [ # 0x5680 -> 0x56bf
        [ 0x56bf, ['Han']],
    ],
    [ # 0x56c0 -> 0x56ff
        [ 0x56ff, ['Han']],
    ],
    [ # 0x5700 -> 0x573f
        [ 0x573f, ['Han']],
    ],
    [ # 0x5740 -> 0x577f
        [ 0x577f, ['Han']],
    ],
    [ # 0x5780 -> 0x57bf
        [ 0x57bf, ['Han']],
    ],
    [ # 0x57c0 -> 0x57ff
        [ 0x57ff, ['Han']],
    ],
    [ # 0x5800 -> 0x583f
        [ 0x583f, ['Han']],
    ],
    [ # 0x5840 -> 0x587f
        [ 0x587f, ['Han']],
    ],
    [ # 0x5880 -> 0x58bf
        [ 0x58bf, ['Han']],
    ],
    [ # 0x58c0 -> 0x58ff
        [ 0x58ff, ['Han']],
    ],
    [ # 0x5900 -> 0x593f
        [ 0x593f, ['Han']],
    ],
    [ # 0x5940 -> 0x597f
        [ 0x597f, ['Han']],
    ],
    [ # 0x5980 -> 0x59bf
        [ 0x59bf, ['Han']],
    ],
    [ # 0x59c0 -> 0x59ff
        [ 0x59ff, ['Han']],
    ],
    [ # 0x5a00 -> 0x5a3f
        [ 0x5a3f, ['Han']],
    ],
    [ # 0x5a40 -> 0x5a7f
        [ 0x5a7f, ['Han']],
    ],
    [ # 0x5a80 -> 0x5abf
        [ 0x5abf, ['Han']],
    ],
    [ # 0x5ac0 -> 0x5aff
        [ 0x5aff, ['Han']],
    ],
    [ # 0x5b00 -> 0x5b3f
        [ 0x5b3f, ['Han']],
    ],
    [ # 0x5b40 -> 0x5b7f
        [ 0x5b7f, ['Han']],
    ],
    [ # 0x5b80 -> 0x5bbf
        [ 0x5bbf, ['Han']],
    ],
    [ # 0x5bc0 -> 0x5bff
        [ 0x5bff, ['Han']],
    ],
    [ # 0x5c00 -> 0x5c3f
        [ 0x5c3f, ['Han']],
    ],
    [ # 0x5c40 -> 0x5c7f
        [ 0x5c7f, ['Han']],
    ],
    [ # 0x5c80 -> 0x5cbf
        [ 0x5cbf, ['Han']],
    ],
    [ # 0x5cc0 -> 0x5cff
        [ 0x5cff, ['Han']],
    ],
    [ # 0x5d00 -> 0x5d3f
        [ 0x5d3f, ['Han']],
    ],
    [ # 0x5d40 -> 0x5d7f
        [ 0x5d7f, ['Han']],
    ],
    [ # 0x5d80 -> 0x5dbf
        [ 0x5dbf, ['Han']],
    ],
    [ # 0x5dc0 -> 0x5dff
        [ 0x5dff, ['Han']],
    ],
    [ # 0x5e00 -> 0x5e3f
        [ 0x5e3f, ['Han']],
    ],
    [ # 0x5e40 -> 0x5e7f
        [ 0x5e7f, ['Han']],
    ],
    [ # 0x5e80 -> 0x5ebf
        [ 0x5ebf, ['Han']],
    ],
    [ # 0x5ec0 -> 0x5eff
        [ 0x5eff, ['Han']],
    ],
    [ # 0x5f00 -> 0x5f3f
        [ 0x5f3f, ['Han']],
    ],
    [ # 0x5f40 -> 0x5f7f
        [ 0x5f7f, ['Han']],
    ],
    [ # 0x5f80 -> 0x5fbf
        [ 0x5fbf, ['Han']],
    ],
    [ # 0x5fc0 -> 0x5fff
        [ 0x5fff, ['Han']],
    ],
    [ # 0x6000 -> 0x603f
        [ 0x603f, ['Han']],
    ],
    [ # 0x6040 -> 0x607f
        [ 0x607f, ['Han']],
    ],
    [ # 0x6080 -> 0x60bf
        [ 0x60bf, ['Han']],
    ],
    [ # 0x60c0 -> 0x60ff
        [ 0x60ff, ['Han']],
    ],
    [ # 0x6100 -> 0x613f
        [ 0x613f, ['Han']],
    ],
    [ # 0x6140 -> 0x617f
        [ 0x617f, ['Han']],
    ],
    [ # 0x6180 -> 0x61bf
        [ 0x61bf, ['Han']],
    ],
    [ # 0x61c0 -> 0x61ff
        [ 0x61ff, ['Han']],
    ],
    [ # 0x6200 -> 0x623f
        [ 0x623f, ['Han']],
    ],
    [ # 0x6240 -> 0x627f
        [ 0x627f, ['Han']],
    ],
    [ # 0x6280 -> 0x62bf
        [ 0x62bf, ['Han']],
    ],
    [ # 0x62c0 -> 0x62ff
        [ 0x62ff, ['Han']],
    ],
    [ # 0x6300 -> 0x633f
        [ 0x633f, ['Han']],
    ],
    [ # 0x6340 -> 0x637f
        [ 0x637f, ['Han']],
    ],
    [ # 0x6380 -> 0x63bf
        [ 0x63bf, ['Han']],
    ],
    [ # 0x63c0 -> 0x63ff
        [ 0x63ff, ['Han']],
    ],
    [ # 0x6400 -> 0x643f
        [ 0x643f, ['Han']],
    ],
    [ # 0x6440 -> 0x647f
        [ 0x647f, ['Han']],
    ],
    [ # 0x6480 -> 0x64bf
        [ 0x64bf, ['Han']],
    ],
    [ # 0x64c0 -> 0x64ff
        [ 0x64ff, ['Han']],
    ],
    [ # 0x6500 -> 0x653f
        [ 0x653f, ['Han']],
    ],
    [ # 0x6540 -> 0x657f
        [ 0x657f, ['Han']],
    ],
    [ # 0x6580 -> 0x65bf
        [ 0x65bf, ['Han']],
    ],
    [ # 0x65c0 -> 0x65ff
        [ 0x65ff, ['Han']],
    ],
    [ # 0x6600 -> 0x663f
        [ 0x663f, ['Han']],
    ],
    [ # 0x6640 -> 0x667f
        [ 0x667f, ['Han']],
    ],
    [ # 0x6680 -> 0x66bf
        [ 0x66bf, ['Han']],
    ],
    [ # 0x66c0 -> 0x66ff
        [ 0x66ff, ['Han']],
    ],
    [ # 0x6700 -> 0x673f
        [ 0x673f, ['Han']],
    ],
    [ # 0x6740 -> 0x677f
        [ 0x677f, ['Han']],
    ],
    [ # 0x6780 -> 0x67bf
        [ 0x67bf, ['Han']],
    ],
    [ # 0x67c0 -> 0x67ff
        [ 0x67ff, ['Han']],
    ],
    [ # 0x6800 -> 0x683f
        [ 0x683f, ['Han']],
    ],
    [ # 0x6840 -> 0x687f
        [ 0x687f, ['Han']],
    ],
    [ # 0x6880 -> 0x68bf
        [ 0x68bf, ['Han']],
    ],
    [ # 0x68c0 -> 0x68ff
        [ 0x68ff, ['Han']],
    ],
    [ # 0x6900 -> 0x693f
        [ 0x693f, ['Han']],
    ],
    [ # 0x6940 -> 0x697f
        [ 0x697f, ['Han']],
    ],
    [ # 0x6980 -> 0x69bf
        [ 0x69bf, ['Han']],
    ],
    [ # 0x69c0 -> 0x69ff
        [ 0x69ff, ['Han']],
    ],
    [ # 0x6a00 -> 0x6a3f
        [ 0x6a3f, ['Han']],
    ],
    [ # 0x6a40 -> 0x6a7f
        [ 0x6a7f, ['Han']],
    ],
    [ # 0x6a80 -> 0x6abf
        [ 0x6abf, ['Han']],
    ],
    [ # 0x6ac0 -> 0x6aff
        [ 0x6aff, ['Han']],
    ],
    [ # 0x6b00 -> 0x6b3f
        [ 0x6b3f, ['Han']],
    ],
    [ # 0x6b40 -> 0x6b7f
        [ 0x6b7f, ['Han']],
    ],
    [ # 0x6b80 -> 0x6bbf
        [ 0x6bbf, ['Han']],
    ],
    [ # 0x6bc0 -> 0x6bff
        [ 0x6bff, ['Han']],
    ],
    [ # 0x6c00 -> 0x6c3f
        [ 0x6c3f, ['Han']],
    ],
    [ # 0x6c40 -> 0x6c7f
        [ 0x6c7f, ['Han']],
    ],
    [ # 0x6c80 -> 0x6cbf
        [ 0x6cbf, ['Han']],
    ],
    [ # 0x6cc0 -> 0x6cff
        [ 0x6cff, ['Han']],
    ],
    [ # 0x6d00 -> 0x6d3f
        [ 0x6d3f, ['Han']],
    ],
    [ # 0x6d40 -> 0x6d7f
        [ 0x6d7f, ['Han']],
    ],
    [ # 0x6d80 -> 0x6dbf
        [ 0x6dbf, ['Han']],
    ],
    [ # 0x6dc0 -> 0x6dff
        [ 0x6dff, ['Han']],
    ],
    [ # 0x6e00 -> 0x6e3f
        [ 0x6e3f, ['Han']],
    ],
    [ # 0x6e40 -> 0x6e7f
        [ 0x6e7f, ['Han']],
    ],
    [ # 0x6e80 -> 0x6ebf
        [ 0x6ebf, ['Han']],
    ],
    [ # 0x6ec0 -> 0x6eff
        [ 0x6eff, ['Han']],
    ],
    [ # 0x6f00 -> 0x6f3f
        [ 0x6f3f, ['Han']],
    ],
    [ # 0x6f40 -> 0x6f7f
        [ 0x6f7f, ['Han']],
    ],
    [ # 0x6f80 -> 0x6fbf
        [ 0x6fbf, ['Han']],
    ],
    [ # 0x6fc0 -> 0x6fff
        [ 0x6fff, ['Han']],
    ],
    [ # 0x7000 -> 0x703f
        [ 0x703f, ['Han']],
    ],
    [ # 0x7040 -> 0x707f
        [ 0x707f, ['Han']],
    ],
    [ # 0x7080 -> 0x70bf
        [ 0x70bf, ['Han']],
    ],
    [ # 0x70c0 -> 0x70ff
        [ 0x70ff, ['Han']],
    ],
    [ # 0x7100 -> 0x713f
        [ 0x713f, ['Han']],
    ],
    [ # 0x7140 -> 0x717f
        [ 0x717f, ['Han']],
    ],
    [ # 0x7180 -> 0x71bf
        [ 0x71bf, ['Han']],
    ],
    [ # 0x71c0 -> 0x71ff
        [ 0x71ff, ['Han']],
    ],
    [ # 0x7200 -> 0x723f
        [ 0x723f, ['Han']],
    ],
    [ # 0x7240 -> 0x727f
        [ 0x727f, ['Han']],
    ],
    [ # 0x7280 -> 0x72bf
        [ 0x72bf, ['Han']],
    ],
    [ # 0x72c0 -> 0x72ff
        [ 0x72ff, ['Han']],
    ],
    [ # 0x7300 -> 0x733f
        [ 0x733f, ['Han']],
    ],
    [ # 0x7340 -> 0x737f
        [ 0x737f, ['Han']],
    ],
    [ # 0x7380 -> 0x73bf
        [ 0x73bf, ['Han']],
    ],
    [ # 0x73c0 -> 0x73ff
        [ 0x73ff, ['Han']],
    ],
    [ # 0x7400 -> 0x743f
        [ 0x743f, ['Han']],
    ],
    [ # 0x7440 -> 0x747f
        [ 0x747f, ['Han']],
    ],
    [ # 0x7480 -> 0x74bf
        [ 0x74bf, ['Han']],
    ],
    [ # 0x74c0 -> 0x74ff
        [ 0x74ff, ['Han']],
    ],
    [ # 0x7500 -> 0x753f
        [ 0x753f, ['Han']],
    ],
    [ # 0x7540 -> 0x757f
        [ 0x757f, ['Han']],
    ],
    [ # 0x7580 -> 0x75bf
        [ 0x75bf, ['Han']],
    ],
    [ # 0x75c0 -> 0x75ff
        [ 0x75ff, ['Han']],
    ],
    [ # 0x7600 -> 0x763f
        [ 0x763f, ['Han']],
    ],
    [ # 0x7640 -> 0x767f
        [ 0x767f, ['Han']],
    ],
    [ # 0x7680 -> 0x76bf
        [ 0x76bf, ['Han']],
    ],
    [ # 0x76c0 -> 0x76ff
        [ 0x76ff, ['Han']],
    ],
    [ # 0x7700 -> 0x773f
        [ 0x773f, ['Han']],
    ],
    [ # 0x7740 -> 0x777f
        [ 0x777f, ['Han']],
    ],
    [ # 0x7780 -> 0x77bf
        [ 0x77bf, ['Han']],
    ],
    [ # 0x77c0 -> 0x77ff
        [ 0x77ff, ['Han']],
    ],
    [ # 0x7800 -> 0x783f
        [ 0x783f, ['Han']],
    ],
    [ # 0x7840 -> 0x787f
        [ 0x787f, ['Han']],
    ],
    [ # 0x7880 -> 0x78bf
        [ 0x78bf, ['Han']],
    ],
    [ # 0x78c0 -> 0x78ff
        [ 0x78ff, ['Han']],
    ],
    [ # 0x7900 -> 0x793f
        [ 0x793f, ['Han']],
    ],
    [ # 0x7940 -> 0x797f
        [ 0x797f, ['Han']],
    ],
    [ # 0x7980 -> 0x79bf
        [ 0x79bf, ['Han']],
    ],
    [ # 0x79c0 -> 0x79ff
        [ 0x79ff, ['Han']],
    ],
    [ # 0x7a00 -> 0x7a3f
        [ 0x7a3f, ['Han']],
    ],
    [ # 0x7a40 -> 0x7a7f
        [ 0x7a7f, ['Han']],
    ],
    [ # 0x7a80 -> 0x7abf
        [ 0x7abf, ['Han']],
    ],
    [ # 0x7ac0 -> 0x7aff
        [ 0x7aff, ['Han']],
    ],
    [ # 0x7b00 -> 0x7b3f
        [ 0x7b3f, ['Han']],
    ],
    [ # 0x7b40 -> 0x7b7f
        [ 0x7b7f, ['Han']],
    ],
    [ # 0x7b80 -> 0x7bbf
        [ 0x7bbf, ['Han']],
    ],
    [ # 0x7bc0 -> 0x7bff
        [ 0x7bff, ['Han']],
    ],
    [ # 0x7c00 -> 0x7c3f
        [ 0x7c3f, ['Han']],
    ],
    [ # 0x7c40 -> 0x7c7f
        [ 0x7c7f, ['Han']],
    ],
    [ # 0x7c80 -> 0x7cbf
        [ 0x7cbf, ['Han']],
    ],
    [ # 0x7cc0 -> 0x7cff
        [ 0x7cff, ['Han']],
    ],
    [ # 0x7d00 -> 0x7d3f
        [ 0x7d3f, ['Han']],
    ],
    [ # 0x7d40 -> 0x7d7f
        [ 0x7d7f, ['Han']],
    ],
    [ # 0x7d80 -> 0x7dbf
        [ 0x7dbf, ['Han']],
    ],
    [ # 0x7dc0 -> 0x7dff
        [ 0x7dff, ['Han']],
    ],
    [ # 0x7e00 -> 0x7e3f
        [ 0x7e3f, ['Han']],
    ],
    [ # 0x7e40 -> 0x7e7f
        [ 0x7e7f, ['Han']],
    ],
    [ # 0x7e80 -> 0x7ebf
        [ 0x7ebf, ['Han']],
    ],
    [ # 0x7ec0 -> 0x7eff
        [ 0x7eff, ['Han']],
    ],
    [ # 0x7f00 -> 0x7f3f
        [ 0x7f3f, ['Han']],
    ],
    [ # 0x7f40 -> 0x7f7f
        [ 0x7f7f, ['Han']],
    ],
    [ # 0x7f80 -> 0x7fbf
        [ 0x7fbf, ['Han']],
    ],
    [ # 0x7fc0 -> 0x7fff
        [ 0x7fff, ['Han']],
    ],
    [ # 0x8000 -> 0x803f
        [ 0x803f, ['Han']],
    ],
    [ # 0x8040 -> 0x807f
        [ 0x807f, ['Han']],
    ],
    [ # 0x8080 -> 0x80bf
        [ 0x80bf, ['Han']],
    ],
    [ # 0x80c0 -> 0x80ff
        [ 0x80ff, ['Han']],
    ],
    [ # 0x8100 -> 0x813f
        [ 0x813f, ['Han']],
    ],
    [ # 0x8140 -> 0x817f
        [ 0x817f, ['Han']],
    ],
    [ # 0x8180 -> 0x81bf
        [ 0x81bf, ['Han']],
    ],
    [ # 0x81c0 -> 0x81ff
        [ 0x81ff, ['Han']],
    ],
    [ # 0x8200 -> 0x823f
        [ 0x823f, ['Han']],
    ],
    [ # 0x8240 -> 0x827f
        [ 0x827f, ['Han']],
    ],
    [ # 0x8280 -> 0x82bf
        [ 0x82bf, ['Han']],
    ],
    [ # 0x82c0 -> 0x82ff
        [ 0x82ff, ['Han']],
    ],
    [ # 0x8300 -> 0x833f
        [ 0x833f, ['Han']],
    ],
    [ # 0x8340 -> 0x837f
        [ 0x837f, ['Han']],
    ],
    [ # 0x8380 -> 0x83bf
        [ 0x83bf, ['Han']],
    ],
    [ # 0x83c0 -> 0x83ff
        [ 0x83ff, ['Han']],
    ],
    [ # 0x8400 -> 0x843f
        [ 0x843f, ['Han']],
    ],
    [ # 0x8440 -> 0x847f
        [ 0x847f, ['Han']],
    ],
    [ # 0x8480 -> 0x84bf
        [ 0x84bf, ['Han']],
    ],
    [ # 0x84c0 -> 0x84ff
        [ 0x84ff, ['Han']],
    ],
    [ # 0x8500 -> 0x853f
        [ 0x853f, ['Han']],
    ],
    [ # 0x8540 -> 0x857f
        [ 0x857f, ['Han']],
    ],
    [ # 0x8580 -> 0x85bf
        [ 0x85bf, ['Han']],
    ],
    [ # 0x85c0 -> 0x85ff
        [ 0x85ff, ['Han']],
    ],
    [ # 0x8600 -> 0x863f
        [ 0x863f, ['Han']],
    ],
    [ # 0x8640 -> 0x867f
        [ 0x867f, ['Han']],
    ],
    [ # 0x8680 -> 0x86bf
        [ 0x86bf, ['Han']],
    ],
    [ # 0x86c0 -> 0x86ff
        [ 0x86ff, ['Han']],
    ],
    [ # 0x8700 -> 0x873f
        [ 0x873f, ['Han']],
    ],
    [ # 0x8740 -> 0x877f
        [ 0x877f, ['Han']],
    ],
    [ # 0x8780 -> 0x87bf
        [ 0x87bf, ['Han']],
    ],
    [ # 0x87c0 -> 0x87ff
        [ 0x87ff, ['Han']],
    ],
    [ # 0x8800 -> 0x883f
        [ 0x883f, ['Han']],
    ],
    [ # 0x8840 -> 0x887f
        [ 0x887f, ['Han']],
    ],
    [ # 0x8880 -> 0x88bf
        [ 0x88bf, ['Han']],
    ],
    [ # 0x88c0 -> 0x88ff
        [ 0x88ff, ['Han']],
    ],
    [ # 0x8900 -> 0x893f
        [ 0x893f, ['Han']],
    ],
    [ # 0x8940 -> 0x897f
        [ 0x897f, ['Han']],
    ],
    [ # 0x8980 -> 0x89bf
        [ 0x89bf, ['Han']],
    ],
    [ # 0x89c0 -> 0x89ff
        [ 0x89ff, ['Han']],
    ],
    [ # 0x8a00 -> 0x8a3f
        [ 0x8a3f, ['Han']],
    ],
    [ # 0x8a40 -> 0x8a7f
        [ 0x8a7f, ['Han']],
    ],
    [ # 0x8a80 -> 0x8abf
        [ 0x8abf, ['Han']],
    ],
    [ # 0x8ac0 -> 0x8aff
        [ 0x8aff, ['Han']],
    ],
    [ # 0x8b00 -> 0x8b3f
        [ 0x8b3f, ['Han']],
    ],
    [ # 0x8b40 -> 0x8b7f
        [ 0x8b7f, ['Han']],
    ],
    [ # 0x8b80 -> 0x8bbf
        [ 0x8bbf, ['Han']],
    ],
    [ # 0x8bc0 -> 0x8bff
        [ 0x8bff, ['Han']],
    ],
    [ # 0x8c00 -> 0x8c3f
        [ 0x8c3f, ['Han']],
    ],
    [ # 0x8c40 -> 0x8c7f
        [ 0x8c7f, ['Han']],
    ],
    [ # 0x8c80 -> 0x8cbf
        [ 0x8cbf, ['Han']],
    ],
    [ # 0x8cc0 -> 0x8cff
        [ 0x8cff, ['Han']],
    ],
    [ # 0x8d00 -> 0x8d3f
        [ 0x8d3f, ['Han']],
    ],
    [ # 0x8d40 -> 0x8d7f
        [ 0x8d7f, ['Han']],
    ],
    [ # 0x8d80 -> 0x8dbf
        [ 0x8dbf, ['Han']],
    ],
    [ # 0x8dc0 -> 0x8dff
        [ 0x8dff, ['Han']],
    ],
    [ # 0x8e00 -> 0x8e3f
        [ 0x8e3f, ['Han']],
    ],
    [ # 0x8e40 -> 0x8e7f
        [ 0x8e7f, ['Han']],
    ],
    [ # 0x8e80 -> 0x8ebf
        [ 0x8ebf, ['Han']],
    ],
    [ # 0x8ec0 -> 0x8eff
        [ 0x8eff, ['Han']],
    ],
    [ # 0x8f00 -> 0x8f3f
        [ 0x8f3f, ['Han']],
    ],
    [ # 0x8f40 -> 0x8f7f
        [ 0x8f7f, ['Han']],
    ],
    [ # 0x8f80 -> 0x8fbf
        [ 0x8fbf, ['Han']],
    ],
    [ # 0x8fc0 -> 0x8fff
        [ 0x8fff, ['Han']],
    ],
    [ # 0x9000 -> 0x903f
        [ 0x903f, ['Han']],
    ],
    [ # 0x9040 -> 0x907f
        [ 0x907f, ['Han']],
    ],
    [ # 0x9080 -> 0x90bf
        [ 0x90bf, ['Han']],
    ],
    [ # 0x90c0 -> 0x90ff
        [ 0x90ff, ['Han']],
    ],
    [ # 0x9100 -> 0x913f
        [ 0x913f, ['Han']],
    ],
    [ # 0x9140 -> 0x917f
        [ 0x917f, ['Han']],
    ],
    [ # 0x9180 -> 0x91bf
        [ 0x91bf, ['Han']],
    ],
    [ # 0x91c0 -> 0x91ff
        [ 0x91ff, ['Han']],
    ],
    [ # 0x9200 -> 0x923f
        [ 0x923f, ['Han']],
    ],
    [ # 0x9240 -> 0x927f
        [ 0x927f, ['Han']],
    ],
    [ # 0x9280 -> 0x92bf
        [ 0x92bf, ['Han']],
    ],
    [ # 0x92c0 -> 0x92ff
        [ 0x92ff, ['Han']],
    ],
    [ # 0x9300 -> 0x933f
        [ 0x933f, ['Han']],
    ],
    [ # 0x9340 -> 0x937f
        [ 0x937f, ['Han']],
    ],
    [ # 0x9380 -> 0x93bf
        [ 0x93bf, ['Han']],
    ],
    [ # 0x93c0 -> 0x93ff
        [ 0x93ff, ['Han']],
    ],
    [ # 0x9400 -> 0x943f
        [ 0x943f, ['Han']],
    ],
    [ # 0x9440 -> 0x947f
        [ 0x947f, ['Han']],
    ],
    [ # 0x9480 -> 0x94bf
        [ 0x94bf, ['Han']],
    ],
    [ # 0x94c0 -> 0x94ff
        [ 0x94ff, ['Han']],
    ],
    [ # 0x9500 -> 0x953f
        [ 0x953f, ['Han']],
    ],
    [ # 0x9540 -> 0x957f
        [ 0x957f, ['Han']],
    ],
    [ # 0x9580 -> 0x95bf
        [ 0x95bf, ['Han']],
    ],
    [ # 0x95c0 -> 0x95ff
        [ 0x95ff, ['Han']],
    ],
    [ # 0x9600 -> 0x963f
        [ 0x963f, ['Han']],
    ],
    [ # 0x9640 -> 0x967f
        [ 0x967f, ['Han']],
    ],
    [ # 0x9680 -> 0x96bf
        [ 0x96bf, ['Han']],
    ],
    [ # 0x96c0 -> 0x96ff
        [ 0x96ff, ['Han']],
    ],
    [ # 0x9700 -> 0x973f
        [ 0x973f, ['Han']],
    ],
    [ # 0x9740 -> 0x977f
        [ 0x977f, ['Han']],
    ],
    [ # 0x9780 -> 0x97bf
        [ 0x97bf, ['Han']],
    ],
    [ # 0x97c0 -> 0x97ff
        [ 0x97ff, ['Han']],
    ],
    [ # 0x9800 -> 0x983f
        [ 0x983f, ['Han']],
    ],
    [ # 0x9840 -> 0x987f
        [ 0x987f, ['Han']],
    ],
    [ # 0x9880 -> 0x98bf
        [ 0x98bf, ['Han']],
    ],
    [ # 0x98c0 -> 0x98ff
        [ 0x98ff, ['Han']],
    ],
    [ # 0x9900 -> 0x993f
        [ 0x993f, ['Han']],
    ],
    [ # 0x9940 -> 0x997f
        [ 0x997f, ['Han']],
    ],
    [ # 0x9980 -> 0x99bf
        [ 0x99bf, ['Han']],
    ],
    [ # 0x99c0 -> 0x99ff
        [ 0x99ff, ['Han']],
    ],
    [ # 0x9a00 -> 0x9a3f
        [ 0x9a3f, ['Han']],
    ],
    [ # 0x9a40 -> 0x9a7f
        [ 0x9a7f, ['Han']],
    ],
    [ # 0x9a80 -> 0x9abf
        [ 0x9abf, ['Han']],
    ],
    [ # 0x9ac0 -> 0x9aff
        [ 0x9aff, ['Han']],
    ],
    [ # 0x9b00 -> 0x9b3f
        [ 0x9b3f, ['Han']],
    ],
    [ # 0x9b40 -> 0x9b7f
        [ 0x9b7f, ['Han']],
    ],
    [ # 0x9b80 -> 0x9bbf
        [ 0x9bbf, ['Han']],
    ],
    [ # 0x9bc0 -> 0x9bff
        [ 0x9bff, ['Han']],
    ],
    [ # 0x9c00 -> 0x9c3f
        [ 0x9c3f, ['Han']],
    ],
    [ # 0x9c40 -> 0x9c7f
        [ 0x9c7f, ['Han']],
    ],
    [ # 0x9c80 -> 0x9cbf
        [ 0x9cbf, ['Han']],
    ],
    [ # 0x9cc0 -> 0x9cff
        [ 0x9cff, ['Han']],
    ],
    [ # 0x9d00 -> 0x9d3f
        [ 0x9d3f, ['Han']],
    ],
    [ # 0x9d40 -> 0x9d7f
        [ 0x9d7f, ['Han']],
    ],
    [ # 0x9d80 -> 0x9dbf
        [ 0x9dbf, ['Han']],
    ],
    [ # 0x9dc0 -> 0x9dff
        [ 0x9dff, ['Han']],
    ],
    [ # 0x9e00 -> 0x9e3f
        [ 0x9e3f, ['Han']],
    ],
    [ # 0x9e40 -> 0x9e7f
        [ 0x9e7f, ['Han']],
    ],
    [ # 0x9e80 -> 0x9ebf
        [ 0x9ebf, ['Han']],
    ],
    [ # 0x9ec0 -> 0x9eff
        [ 0x9eff, ['Han']],
    ],
    [ # 0x9f00 -> 0x9f3f
        [ 0x9f3f, ['Han']],
    ],
    [ # 0x9f40 -> 0x9f7f
        [ 0x9f7f, ['Han']],
    ],
    [ # 0x9f80 -> 0x9fbf
        [ 0x9fbf, ['Han']],
    ],
    [ # 0x9fc0 -> 0x9fff
        [ 0x9fcc, ['Han']],
        [ 0x9fff, ['Unknown']],
    ],
    [ # 0xa000 -> 0xa03f
        [ 0xa03f, ['Yi']],
    ],
    [ # 0xa040 -> 0xa07f
        [ 0xa07f, ['Yi']],
    ],
    [ # 0xa080 -> 0xa0bf
        [ 0xa0bf, ['Yi']],
    ],
    [ # 0xa0c0 -> 0xa0ff
        [ 0xa0ff, ['Yi']],
    ],
    [ # 0xa100 -> 0xa13f
        [ 0xa13f, ['Yi']],
    ],
    [ # 0xa140 -> 0xa17f
        [ 0xa17f, ['Yi']],
    ],
    [ # 0xa180 -> 0xa1bf
        [ 0xa1bf, ['Yi']],
    ],
    [ # 0xa1c0 -> 0xa1ff
        [ 0xa1ff, ['Yi']],
    ],
    [ # 0xa200 -> 0xa23f
        [ 0xa23f, ['Yi']],
    ],
    [ # 0xa240 -> 0xa27f
        [ 0xa27f, ['Yi']],
    ],
    [ # 0xa280 -> 0xa2bf
        [ 0xa2bf, ['Yi']],
    ],
    [ # 0xa2c0 -> 0xa2ff
        [ 0xa2ff, ['Yi']],
    ],
    [ # 0xa300 -> 0xa33f
        [ 0xa33f, ['Yi']],
    ],
    [ # 0xa340 -> 0xa37f
        [ 0xa37f, ['Yi']],
    ],
    [ # 0xa380 -> 0xa3bf
        [ 0xa3bf, ['Yi']],
    ],
    [ # 0xa3c0 -> 0xa3ff
        [ 0xa3ff, ['Yi']],
    ],
    [ # 0xa400 -> 0xa43f
        [ 0xa43f, ['Yi']],
    ],
    [ # 0xa440 -> 0xa47f
        [ 0xa47f, ['Yi']],
    ],
    [ # 0xa480 -> 0xa4bf
        [ 0xa48c, ['Yi']],
        [ 0xa48f, ['Unknown']],
        [ 0xa4bf, ['Yi']],
    ],
    [ # 0xa4c0 -> 0xa4ff
        [ 0xa4c6, ['Yi']],
        [ 0xa4cf, ['Unknown']],
        [ 0xa4ff, ['Lisu']],
    ],
    [ # 0xa500 -> 0xa53f
        [ 0xa53f, ['Vai']],
    ],
    [ # 0xa540 -> 0xa57f
        [ 0xa57f, ['Vai']],
    ],
    [ # 0xa580 -> 0xa5bf
        [ 0xa5bf, ['Vai']],
    ],
    [ # 0xa5c0 -> 0xa5ff
        [ 0xa5ff, ['Vai']],
    ],
    [ # 0xa600 -> 0xa63f
        [ 0xa62b, ['Vai']],
        [ 0xa63f, ['Unknown']],
    ],
    [ # 0xa640 -> 0xa67f
        [ 0xa67f, ['Cyrillic']],
    ],
    [ # 0xa680 -> 0xa6bf
        [ 0xa69d, ['Cyrillic']],
        [ 0xa69e, ['Unknown']],
        [ 0xa69f, ['Cyrillic']],
        [ 0xa6a0, ['Cyrillic', 'Bamum']],
        [ 0xa6bf, ['Bamum']],
    ],
    [ # 0xa6c0 -> 0xa6ff
        [ 0xa6f7, ['Bamum']],
        [ 0xa6ff, ['Unknown']],
    ],
    [ # 0xa700 -> 0xa73f
        [ 0xa721, ['Common']],
        [ 0xa73f, ['Latin']],
    ],
    [ # 0xa740 -> 0xa77f
        [ 0xa77f, ['Latin']],
    ],
    [ # 0xa780 -> 0xa7bf
        [ 0xa787, ['Latin']],
        [ 0xa78a, ['Common']],
        [ 0xa78e, ['Latin']],
        [ 0xa78f, ['Unknown']],
        [ 0xa7ad, ['Latin']],
        [ 0xa7af, ['Unknown']],
        [ 0xa7b1, ['Latin']],
        [ 0xa7bf, ['Unknown']],
    ],
    [ # 0xa7c0 -> 0xa7ff
        [ 0xa7f6, ['Unknown']],
        [ 0xa7ff, ['Latin']],
    ],
    [ # 0xa800 -> 0xa83f
        [ 0xa82b, ['Syloti_Nagri']],
        [ 0xa82f, ['Unknown']],
        [ 0xa83a, ['Devanagari', 'Khudawadi', 'Gujarati', 'Gurmukhi', 'Tirhuta', 'Takri', 'Mahajani', 'Kaithi', 'Modi', 'Common']],
        [ 0xa83f, ['Unknown']],
    ],
    [ # 0xa840 -> 0xa87f
        [ 0xa877, ['Phags_Pa']],
        [ 0xa87f, ['Unknown']],
    ],
    [ # 0xa880 -> 0xa8bf
        [ 0xa8bf, ['Saurashtra']],
    ],
    [ # 0xa8c0 -> 0xa8ff
        [ 0xa8c5, ['Saurashtra']],
        [ 0xa8cd, ['Unknown']],
        [ 0xa8d9, ['Saurashtra']],
        [ 0xa8df, ['Unknown']],
        [ 0xa8fc, ['Devanagari']],
        [ 0xa8ff, ['Unknown']],
    ],
    [ # 0xa900 -> 0xa93f
        [ 0xa92d, ['Kayah_Li']],
        [ 0xa92f, ['Myanmar', 'Latin', 'Kayah_Li', 'Common']],
        [ 0xa930, ['Rejang', 'Kayah_Li']],
        [ 0xa93f, ['Rejang']],
    ],
    [ # 0xa940 -> 0xa97f
        [ 0xa953, ['Rejang']],
        [ 0xa95e, ['Unknown']],
        [ 0xa95f, ['Rejang']],
        [ 0xa960, ['Rejang', 'Hangul']],
        [ 0xa97c, ['Hangul']],
        [ 0xa97f, ['Unknown']],
    ],
    [ # 0xa980 -> 0xa9bf
        [ 0xa9bf, ['Javanese']],
    ],
    [ # 0xa9c0 -> 0xa9ff
        [ 0xa9cd, ['Javanese']],
        [ 0xa9ce, ['Unknown']],
        [ 0xa9d0, ['Buginese', 'Javanese', 'Common']],
        [ 0xa9d9, ['Javanese']],
        [ 0xa9dd, ['Unknown']],
        [ 0xa9df, ['Javanese']],
        [ 0xa9fe, ['Myanmar']],
        [ 0xa9ff, ['Unknown']],
    ],
    [ # 0xaa00 -> 0xaa3f
        [ 0xaa36, ['Cham']],
        [ 0xaa3f, ['Unknown']],
    ],
    [ # 0xaa40 -> 0xaa7f
        [ 0xaa4e, ['Cham']],
        [ 0xaa4f, ['Unknown']],
        [ 0xaa59, ['Cham']],
        [ 0xaa5b, ['Unknown']],
        [ 0xaa5f, ['Cham']],
        [ 0xaa7f, ['Myanmar']],
    ],
    [ # 0xaa80 -> 0xaabf
        [ 0xaabf, ['Tai_Viet']],
    ],
    [ # 0xaac0 -> 0xaaff
        [ 0xaac3, ['Tai_Viet']],
        [ 0xaada, ['Unknown']],
        [ 0xaadf, ['Tai_Viet']],
        [ 0xaaf7, ['Meetei_Mayek']],
        [ 0xaaff, ['Unknown']],
    ],
    [ # 0xab00 -> 0xab3f
        [ 0xab00, ['Unknown']],
        [ 0xab06, ['Ethiopic']],
        [ 0xab08, ['Unknown']],
        [ 0xab0e, ['Ethiopic']],
        [ 0xab10, ['Unknown']],
        [ 0xab16, ['Ethiopic']],
        [ 0xab1f, ['Unknown']],
        [ 0xab26, ['Ethiopic']],
        [ 0xab27, ['Unknown']],
        [ 0xab2e, ['Ethiopic']],
        [ 0xab2f, ['Unknown']],
        [ 0xab3f, ['Latin']],
    ],
    [ # 0xab40 -> 0xab7f
        [ 0xab5a, ['Latin']],
        [ 0xab5b, ['Common']],
        [ 0xab5c, ['Latin', 'Common']],
        [ 0xab5f, ['Latin']],
        [ 0xab63, ['Unknown']],
        [ 0xab64, ['Latin']],
        [ 0xab65, ['Latin', 'Greek']],
        [ 0xab66, ['Greek']],
        [ 0xab7f, ['Unknown']],
    ],
    [ # 0xab80 -> 0xabbf
        [ 0xabbf, ['Unknown']],
    ],
    [ # 0xabc0 -> 0xabff
        [ 0xabee, ['Meetei_Mayek']],
        [ 0xabef, ['Unknown']],
        [ 0xabf9, ['Meetei_Mayek']],
        [ 0xabff, ['Unknown']],
    ],
    [ # 0xac00 -> 0xac3f
        [ 0xac3f, ['Hangul']],
    ],
    [ # 0xac40 -> 0xac7f
        [ 0xac7f, ['Hangul']],
    ],
    [ # 0xac80 -> 0xacbf
        [ 0xacbf, ['Hangul']],
    ],
    [ # 0xacc0 -> 0xacff
        [ 0xacff, ['Hangul']],
    ],
    [ # 0xad00 -> 0xad3f
        [ 0xad3f, ['Hangul']],
    ],
    [ # 0xad40 -> 0xad7f
        [ 0xad7f, ['Hangul']],
    ],
    [ # 0xad80 -> 0xadbf
        [ 0xadbf, ['Hangul']],
    ],
    [ # 0xadc0 -> 0xadff
        [ 0xadff, ['Hangul']],
    ],
    [ # 0xae00 -> 0xae3f
        [ 0xae3f, ['Hangul']],
    ],
    [ # 0xae40 -> 0xae7f
        [ 0xae7f, ['Hangul']],
    ],
    [ # 0xae80 -> 0xaebf
        [ 0xaebf, ['Hangul']],
    ],
    [ # 0xaec0 -> 0xaeff
        [ 0xaeff, ['Hangul']],
    ],
    [ # 0xaf00 -> 0xaf3f
        [ 0xaf3f, ['Hangul']],
    ],
    [ # 0xaf40 -> 0xaf7f
        [ 0xaf7f, ['Hangul']],
    ],
    [ # 0xaf80 -> 0xafbf
        [ 0xafbf, ['Hangul']],
    ],
    [ # 0xafc0 -> 0xafff
        [ 0xafff, ['Hangul']],
    ],
    [ # 0xb000 -> 0xb03f
        [ 0xb03f, ['Hangul']],
    ],
    [ # 0xb040 -> 0xb07f
        [ 0xb07f, ['Hangul']],
    ],
    [ # 0xb080 -> 0xb0bf
        [ 0xb0bf, ['Hangul']],
    ],
    [ # 0xb0c0 -> 0xb0ff
        [ 0xb0ff, ['Hangul']],
    ],
    [ # 0xb100 -> 0xb13f
        [ 0xb13f, ['Hangul']],
    ],
    [ # 0xb140 -> 0xb17f
        [ 0xb17f, ['Hangul']],
    ],
    [ # 0xb180 -> 0xb1bf
        [ 0xb1bf, ['Hangul']],
    ],
    [ # 0xb1c0 -> 0xb1ff
        [ 0xb1ff, ['Hangul']],
    ],
    [ # 0xb200 -> 0xb23f
        [ 0xb23f, ['Hangul']],
    ],
    [ # 0xb240 -> 0xb27f
        [ 0xb27f, ['Hangul']],
    ],
    [ # 0xb280 -> 0xb2bf
        [ 0xb2bf, ['Hangul']],
    ],
    [ # 0xb2c0 -> 0xb2ff
        [ 0xb2ff, ['Hangul']],
    ],
    [ # 0xb300 -> 0xb33f
        [ 0xb33f, ['Hangul']],
    ],
    [ # 0xb340 -> 0xb37f
        [ 0xb37f, ['Hangul']],
    ],
    [ # 0xb380 -> 0xb3bf
        [ 0xb3bf, ['Hangul']],
    ],
    [ # 0xb3c0 -> 0xb3ff
        [ 0xb3ff, ['Hangul']],
    ],
    [ # 0xb400 -> 0xb43f
        [ 0xb43f, ['Hangul']],
    ],
    [ # 0xb440 -> 0xb47f
        [ 0xb47f, ['Hangul']],
    ],
    [ # 0xb480 -> 0xb4bf
        [ 0xb4bf, ['Hangul']],
    ],
    [ # 0xb4c0 -> 0xb4ff
        [ 0xb4ff, ['Hangul']],
    ],
    [ # 0xb500 -> 0xb53f
        [ 0xb53f, ['Hangul']],
    ],
    [ # 0xb540 -> 0xb57f
        [ 0xb57f, ['Hangul']],
    ],
    [ # 0xb580 -> 0xb5bf
        [ 0xb5bf, ['Hangul']],
    ],
    [ # 0xb5c0 -> 0xb5ff
        [ 0xb5ff, ['Hangul']],
    ],
    [ # 0xb600 -> 0xb63f
        [ 0xb63f, ['Hangul']],
    ],
    [ # 0xb640 -> 0xb67f
        [ 0xb67f, ['Hangul']],
    ],
    [ # 0xb680 -> 0xb6bf
        [ 0xb6bf, ['Hangul']],
    ],
    [ # 0xb6c0 -> 0xb6ff
        [ 0xb6ff, ['Hangul']],
    ],
    [ # 0xb700 -> 0xb73f
        [ 0xb73f, ['Hangul']],
    ],
    [ # 0xb740 -> 0xb77f
        [ 0xb77f, ['Hangul']],
    ],
    [ # 0xb780 -> 0xb7bf
        [ 0xb7bf, ['Hangul']],
    ],
    [ # 0xb7c0 -> 0xb7ff
        [ 0xb7ff, ['Hangul']],
    ],
    [ # 0xb800 -> 0xb83f
        [ 0xb83f, ['Hangul']],
    ],
    [ # 0xb840 -> 0xb87f
        [ 0xb87f, ['Hangul']],
    ],
    [ # 0xb880 -> 0xb8bf
        [ 0xb8bf, ['Hangul']],
    ],
    [ # 0xb8c0 -> 0xb8ff
        [ 0xb8ff, ['Hangul']],
    ],
    [ # 0xb900 -> 0xb93f
        [ 0xb93f, ['Hangul']],
    ],
    [ # 0xb940 -> 0xb97f
        [ 0xb97f, ['Hangul']],
    ],
    [ # 0xb980 -> 0xb9bf
        [ 0xb9bf, ['Hangul']],
    ],
    [ # 0xb9c0 -> 0xb9ff
        [ 0xb9ff, ['Hangul']],
    ],
    [ # 0xba00 -> 0xba3f
        [ 0xba3f, ['Hangul']],
    ],
    [ # 0xba40 -> 0xba7f
        [ 0xba7f, ['Hangul']],
    ],
    [ # 0xba80 -> 0xbabf
        [ 0xbabf, ['Hangul']],
    ],
    [ # 0xbac0 -> 0xbaff
        [ 0xbaff, ['Hangul']],
    ],
    [ # 0xbb00 -> 0xbb3f
        [ 0xbb3f, ['Hangul']],
    ],
    [ # 0xbb40 -> 0xbb7f
        [ 0xbb7f, ['Hangul']],
    ],
    [ # 0xbb80 -> 0xbbbf
        [ 0xbbbf, ['Hangul']],
    ],
    [ # 0xbbc0 -> 0xbbff
        [ 0xbbff, ['Hangul']],
    ],
    [ # 0xbc00 -> 0xbc3f
        [ 0xbc3f, ['Hangul']],
    ],
    [ # 0xbc40 -> 0xbc7f
        [ 0xbc7f, ['Hangul']],
    ],
    [ # 0xbc80 -> 0xbcbf
        [ 0xbcbf, ['Hangul']],
    ],
    [ # 0xbcc0 -> 0xbcff
        [ 0xbcff, ['Hangul']],
    ],
    [ # 0xbd00 -> 0xbd3f
        [ 0xbd3f, ['Hangul']],
    ],
    [ # 0xbd40 -> 0xbd7f
        [ 0xbd7f, ['Hangul']],
    ],
    [ # 0xbd80 -> 0xbdbf
        [ 0xbdbf, ['Hangul']],
    ],
    [ # 0xbdc0 -> 0xbdff
        [ 0xbdff, ['Hangul']],
    ],
    [ # 0xbe00 -> 0xbe3f
        [ 0xbe3f, ['Hangul']],
    ],
    [ # 0xbe40 -> 0xbe7f
        [ 0xbe7f, ['Hangul']],
    ],
    [ # 0xbe80 -> 0xbebf
        [ 0xbebf, ['Hangul']],
    ],
    [ # 0xbec0 -> 0xbeff
        [ 0xbeff, ['Hangul']],
    ],
    [ # 0xbf00 -> 0xbf3f
        [ 0xbf3f, ['Hangul']],
    ],
    [ # 0xbf40 -> 0xbf7f
        [ 0xbf7f, ['Hangul']],
    ],
    [ # 0xbf80 -> 0xbfbf
        [ 0xbfbf, ['Hangul']],
    ],
    [ # 0xbfc0 -> 0xbfff
        [ 0xbfff, ['Hangul']],
    ],
    [ # 0xc000 -> 0xc03f
        [ 0xc03f, ['Hangul']],
    ],
    [ # 0xc040 -> 0xc07f
        [ 0xc07f, ['Hangul']],
    ],
    [ # 0xc080 -> 0xc0bf
        [ 0xc0bf, ['Hangul']],
    ],
    [ # 0xc0c0 -> 0xc0ff
        [ 0xc0ff, ['Hangul']],
    ],
    [ # 0xc100 -> 0xc13f
        [ 0xc13f, ['Hangul']],
    ],
    [ # 0xc140 -> 0xc17f
        [ 0xc17f, ['Hangul']],
    ],
    [ # 0xc180 -> 0xc1bf
        [ 0xc1bf, ['Hangul']],
    ],
    [ # 0xc1c0 -> 0xc1ff
        [ 0xc1ff, ['Hangul']],
    ],
    [ # 0xc200 -> 0xc23f
        [ 0xc23f, ['Hangul']],
    ],
    [ # 0xc240 -> 0xc27f
        [ 0xc27f, ['Hangul']],
    ],
    [ # 0xc280 -> 0xc2bf
        [ 0xc2bf, ['Hangul']],
    ],
    [ # 0xc2c0 -> 0xc2ff
        [ 0xc2ff, ['Hangul']],
    ],
    [ # 0xc300 -> 0xc33f
        [ 0xc33f, ['Hangul']],
    ],
    [ # 0xc340 -> 0xc37f
        [ 0xc37f, ['Hangul']],
    ],
    [ # 0xc380 -> 0xc3bf
        [ 0xc3bf, ['Hangul']],
    ],
    [ # 0xc3c0 -> 0xc3ff
        [ 0xc3ff, ['Hangul']],
    ],
    [ # 0xc400 -> 0xc43f
        [ 0xc43f, ['Hangul']],
    ],
    [ # 0xc440 -> 0xc47f
        [ 0xc47f, ['Hangul']],
    ],
    [ # 0xc480 -> 0xc4bf
        [ 0xc4bf, ['Hangul']],
    ],
    [ # 0xc4c0 -> 0xc4ff
        [ 0xc4ff, ['Hangul']],
    ],
    [ # 0xc500 -> 0xc53f
        [ 0xc53f, ['Hangul']],
    ],
    [ # 0xc540 -> 0xc57f
        [ 0xc57f, ['Hangul']],
    ],
    [ # 0xc580 -> 0xc5bf
        [ 0xc5bf, ['Hangul']],
    ],
    [ # 0xc5c0 -> 0xc5ff
        [ 0xc5ff, ['Hangul']],
    ],
    [ # 0xc600 -> 0xc63f
        [ 0xc63f, ['Hangul']],
    ],
    [ # 0xc640 -> 0xc67f
        [ 0xc67f, ['Hangul']],
    ],
    [ # 0xc680 -> 0xc6bf
        [ 0xc6bf, ['Hangul']],
    ],
    [ # 0xc6c0 -> 0xc6ff
        [ 0xc6ff, ['Hangul']],
    ],
    [ # 0xc700 -> 0xc73f
        [ 0xc73f, ['Hangul']],
    ],
    [ # 0xc740 -> 0xc77f
        [ 0xc77f, ['Hangul']],
    ],
    [ # 0xc780 -> 0xc7bf
        [ 0xc7bf, ['Hangul']],
    ],
    [ # 0xc7c0 -> 0xc7ff
        [ 0xc7ff, ['Hangul']],
    ],
    [ # 0xc800 -> 0xc83f
        [ 0xc83f, ['Hangul']],
    ],
    [ # 0xc840 -> 0xc87f
        [ 0xc87f, ['Hangul']],
    ],
    [ # 0xc880 -> 0xc8bf
        [ 0xc8bf, ['Hangul']],
    ],
    [ # 0xc8c0 -> 0xc8ff
        [ 0xc8ff, ['Hangul']],
    ],
    [ # 0xc900 -> 0xc93f
        [ 0xc93f, ['Hangul']],
    ],
    [ # 0xc940 -> 0xc97f
        [ 0xc97f, ['Hangul']],
    ],
    [ # 0xc980 -> 0xc9bf
        [ 0xc9bf, ['Hangul']],
    ],
    [ # 0xc9c0 -> 0xc9ff
        [ 0xc9ff, ['Hangul']],
    ],
    [ # 0xca00 -> 0xca3f
        [ 0xca3f, ['Hangul']],
    ],
    [ # 0xca40 -> 0xca7f
        [ 0xca7f, ['Hangul']],
    ],
    [ # 0xca80 -> 0xcabf
        [ 0xcabf, ['Hangul']],
    ],
    [ # 0xcac0 -> 0xcaff
        [ 0xcaff, ['Hangul']],
    ],
    [ # 0xcb00 -> 0xcb3f
        [ 0xcb3f, ['Hangul']],
    ],
    [ # 0xcb40 -> 0xcb7f
        [ 0xcb7f, ['Hangul']],
    ],
    [ # 0xcb80 -> 0xcbbf
        [ 0xcbbf, ['Hangul']],
    ],
    [ # 0xcbc0 -> 0xcbff
        [ 0xcbff, ['Hangul']],
    ],
    [ # 0xcc00 -> 0xcc3f
        [ 0xcc3f, ['Hangul']],
    ],
    [ # 0xcc40 -> 0xcc7f
        [ 0xcc7f, ['Hangul']],
    ],
    [ # 0xcc80 -> 0xccbf
        [ 0xccbf, ['Hangul']],
    ],
    [ # 0xccc0 -> 0xccff
        [ 0xccff, ['Hangul']],
    ],
    [ # 0xcd00 -> 0xcd3f
        [ 0xcd3f, ['Hangul']],
    ],
    [ # 0xcd40 -> 0xcd7f
        [ 0xcd7f, ['Hangul']],
    ],
    [ # 0xcd80 -> 0xcdbf
        [ 0xcdbf, ['Hangul']],
    ],
    [ # 0xcdc0 -> 0xcdff
        [ 0xcdff, ['Hangul']],
    ],
    [ # 0xce00 -> 0xce3f
        [ 0xce3f, ['Hangul']],
    ],
    [ # 0xce40 -> 0xce7f
        [ 0xce7f, ['Hangul']],
    ],
    [ # 0xce80 -> 0xcebf
        [ 0xcebf, ['Hangul']],
    ],
    [ # 0xcec0 -> 0xceff
        [ 0xceff, ['Hangul']],
    ],
    [ # 0xcf00 -> 0xcf3f
        [ 0xcf3f, ['Hangul']],
    ],
    [ # 0xcf40 -> 0xcf7f
        [ 0xcf7f, ['Hangul']],
    ],
    [ # 0xcf80 -> 0xcfbf
        [ 0xcfbf, ['Hangul']],
    ],
    [ # 0xcfc0 -> 0xcfff
        [ 0xcfff, ['Hangul']],
    ],
    [ # 0xd000 -> 0xd03f
        [ 0xd03f, ['Hangul']],
    ],
    [ # 0xd040 -> 0xd07f
        [ 0xd07f, ['Hangul']],
    ],
    [ # 0xd080 -> 0xd0bf
        [ 0xd0bf, ['Hangul']],
    ],
    [ # 0xd0c0 -> 0xd0ff
        [ 0xd0ff, ['Hangul']],
    ],
    [ # 0xd100 -> 0xd13f
        [ 0xd13f, ['Hangul']],
    ],
    [ # 0xd140 -> 0xd17f
        [ 0xd17f, ['Hangul']],
    ],
    [ # 0xd180 -> 0xd1bf
        [ 0xd1bf, ['Hangul']],
    ],
    [ # 0xd1c0 -> 0xd1ff
        [ 0xd1ff, ['Hangul']],
    ],
    [ # 0xd200 -> 0xd23f
        [ 0xd23f, ['Hangul']],
    ],
    [ # 0xd240 -> 0xd27f
        [ 0xd27f, ['Hangul']],
    ],
    [ # 0xd280 -> 0xd2bf
        [ 0xd2bf, ['Hangul']],
    ],
    [ # 0xd2c0 -> 0xd2ff
        [ 0xd2ff, ['Hangul']],
    ],
    [ # 0xd300 -> 0xd33f
        [ 0xd33f, ['Hangul']],
    ],
    [ # 0xd340 -> 0xd37f
        [ 0xd37f, ['Hangul']],
    ],
    [ # 0xd380 -> 0xd3bf
        [ 0xd3bf, ['Hangul']],
    ],
    [ # 0xd3c0 -> 0xd3ff
        [ 0xd3ff, ['Hangul']],
    ],
    [ # 0xd400 -> 0xd43f
        [ 0xd43f, ['Hangul']],
    ],
    [ # 0xd440 -> 0xd47f
        [ 0xd47f, ['Hangul']],
    ],
    [ # 0xd480 -> 0xd4bf
        [ 0xd4bf, ['Hangul']],
    ],
    [ # 0xd4c0 -> 0xd4ff
        [ 0xd4ff, ['Hangul']],
    ],
    [ # 0xd500 -> 0xd53f
        [ 0xd53f, ['Hangul']],
    ],
    [ # 0xd540 -> 0xd57f
        [ 0xd57f, ['Hangul']],
    ],
    [ # 0xd580 -> 0xd5bf
        [ 0xd5bf, ['Hangul']],
    ],
    [ # 0xd5c0 -> 0xd5ff
        [ 0xd5ff, ['Hangul']],
    ],
    [ # 0xd600 -> 0xd63f
        [ 0xd63f, ['Hangul']],
    ],
    [ # 0xd640 -> 0xd67f
        [ 0xd67f, ['Hangul']],
    ],
    [ # 0xd680 -> 0xd6bf
        [ 0xd6bf, ['Hangul']],
    ],
    [ # 0xd6c0 -> 0xd6ff
        [ 0xd6ff, ['Hangul']],
    ],
    [ # 0xd700 -> 0xd73f
        [ 0xd73f, ['Hangul']],
    ],
    [ # 0xd740 -> 0xd77f
        [ 0xd77f, ['Hangul']],
    ],
    [ # 0xd780 -> 0xd7bf
        [ 0xd7a3, ['Hangul']],
        [ 0xd7af, ['Unknown']],
        [ 0xd7bf, ['Hangul']],
    ],
    [ # 0xd7c0 -> 0xd7ff
        [ 0xd7c6, ['Hangul']],
        [ 0xd7ca, ['Unknown']],
        [ 0xd7fb, ['Hangul']],
        [ 0xd7ff, ['Unknown']],
    ],
    [ # 0xd800 -> 0xd83f
        [ 0xd83f, ['Unknown']],
    ],
    [ # 0xd840 -> 0xd87f
        [ 0xd87f, ['Unknown']],
    ],
    [ # 0xd880 -> 0xd8bf
        [ 0xd8bf, ['Unknown']],
    ],
    [ # 0xd8c0 -> 0xd8ff
        [ 0xd8ff, ['Unknown']],
    ],
    [ # 0xd900 -> 0xd93f
        [ 0xd93f, ['Unknown']],
    ],
    [ # 0xd940 -> 0xd97f
        [ 0xd97f, ['Unknown']],
    ],
    [ # 0xd980 -> 0xd9bf
        [ 0xd9bf, ['Unknown']],
    ],
    [ # 0xd9c0 -> 0xd9ff
        [ 0xd9ff, ['Unknown']],
    ],
    [ # 0xda00 -> 0xda3f
        [ 0xda3f, ['Unknown']],
    ],
    [ # 0xda40 -> 0xda7f
        [ 0xda7f, ['Unknown']],
    ],
    [ # 0xda80 -> 0xdabf
        [ 0xdabf, ['Unknown']],
    ],
    [ # 0xdac0 -> 0xdaff
        [ 0xdaff, ['Unknown']],
    ],
    [ # 0xdb00 -> 0xdb3f
        [ 0xdb3f, ['Unknown']],
    ],
    [ # 0xdb40 -> 0xdb7f
        [ 0xdb7f, ['Unknown']],
    ],
    [ # 0xdb80 -> 0xdbbf
        [ 0xdbbf, ['Unknown']],
    ],
    [ # 0xdbc0 -> 0xdbff
        [ 0xdbff, ['Unknown']],
    ],
    [ # 0xdc00 -> 0xdc3f
        [ 0xdc3f, ['Unknown']],
    ],
    [ # 0xdc40 -> 0xdc7f
        [ 0xdc7f, ['Unknown']],
    ],
    [ # 0xdc80 -> 0xdcbf
        [ 0xdcbf, ['Unknown']],
    ],
    [ # 0xdcc0 -> 0xdcff
        [ 0xdcff, ['Unknown']],
    ],
    [ # 0xdd00 -> 0xdd3f
        [ 0xdd3f, ['Unknown']],
    ],
    [ # 0xdd40 -> 0xdd7f
        [ 0xdd7f, ['Unknown']],
    ],
    [ # 0xdd80 -> 0xddbf
        [ 0xddbf, ['Unknown']],
    ],
    [ # 0xddc0 -> 0xddff
        [ 0xddff, ['Unknown']],
    ],
    [ # 0xde00 -> 0xde3f
        [ 0xde3f, ['Unknown']],
    ],
    [ # 0xde40 -> 0xde7f
        [ 0xde7f, ['Unknown']],
    ],
    [ # 0xde80 -> 0xdebf
        [ 0xdebf, ['Unknown']],
    ],
    [ # 0xdec0 -> 0xdeff
        [ 0xdeff, ['Unknown']],
    ],
    [ # 0xdf00 -> 0xdf3f
        [ 0xdf3f, ['Unknown']],
    ],
    [ # 0xdf40 -> 0xdf7f
        [ 0xdf7f, ['Unknown']],
    ],
    [ # 0xdf80 -> 0xdfbf
        [ 0xdfbf, ['Unknown']],
    ],
    [ # 0xdfc0 -> 0xdfff
        [ 0xdfff, ['Unknown']],
    ],
    [ # 0xe000 -> 0xe03f
        [ 0xe03f, ['Unknown']],
    ],
    [ # 0xe040 -> 0xe07f
        [ 0xe07f, ['Unknown']],
    ],
    [ # 0xe080 -> 0xe0bf
        [ 0xe0bf, ['Unknown']],
    ],
    [ # 0xe0c0 -> 0xe0ff
        [ 0xe0ff, ['Unknown']],
    ],
    [ # 0xe100 -> 0xe13f
        [ 0xe13f, ['Unknown']],
    ],
    [ # 0xe140 -> 0xe17f
        [ 0xe17f, ['Unknown']],
    ],
    [ # 0xe180 -> 0xe1bf
        [ 0xe1bf, ['Unknown']],
    ],
    [ # 0xe1c0 -> 0xe1ff
        [ 0xe1ff, ['Unknown']],
    ],
    [ # 0xe200 -> 0xe23f
        [ 0xe23f, ['Unknown']],
    ],
    [ # 0xe240 -> 0xe27f
        [ 0xe27f, ['Unknown']],
    ],
    [ # 0xe280 -> 0xe2bf
        [ 0xe2bf, ['Unknown']],
    ],
    [ # 0xe2c0 -> 0xe2ff
        [ 0xe2ff, ['Unknown']],
    ],
    [ # 0xe300 -> 0xe33f
        [ 0xe33f, ['Unknown']],
    ],
    [ # 0xe340 -> 0xe37f
        [ 0xe37f, ['Unknown']],
    ],
    [ # 0xe380 -> 0xe3bf
        [ 0xe3bf, ['Unknown']],
    ],
    [ # 0xe3c0 -> 0xe3ff
        [ 0xe3ff, ['Unknown']],
    ],
    [ # 0xe400 -> 0xe43f
        [ 0xe43f, ['Unknown']],
    ],
    [ # 0xe440 -> 0xe47f
        [ 0xe47f, ['Unknown']],
    ],
    [ # 0xe480 -> 0xe4bf
        [ 0xe4bf, ['Unknown']],
    ],
    [ # 0xe4c0 -> 0xe4ff
        [ 0xe4ff, ['Unknown']],
    ],
    [ # 0xe500 -> 0xe53f
        [ 0xe53f, ['Unknown']],
    ],
    [ # 0xe540 -> 0xe57f
        [ 0xe57f, ['Unknown']],
    ],
    [ # 0xe580 -> 0xe5bf
        [ 0xe5bf, ['Unknown']],
    ],
    [ # 0xe5c0 -> 0xe5ff
        [ 0xe5ff, ['Unknown']],
    ],
    [ # 0xe600 -> 0xe63f
        [ 0xe63f, ['Unknown']],
    ],
    [ # 0xe640 -> 0xe67f
        [ 0xe67f, ['Unknown']],
    ],
    [ # 0xe680 -> 0xe6bf
        [ 0xe6bf, ['Unknown']],
    ],
    [ # 0xe6c0 -> 0xe6ff
        [ 0xe6ff, ['Unknown']],
    ],
    [ # 0xe700 -> 0xe73f
        [ 0xe73f, ['Unknown']],
    ],
    [ # 0xe740 -> 0xe77f
        [ 0xe77f, ['Unknown']],
    ],
    [ # 0xe780 -> 0xe7bf
        [ 0xe7bf, ['Unknown']],
    ],
    [ # 0xe7c0 -> 0xe7ff
        [ 0xe7ff, ['Unknown']],
    ],
    [ # 0xe800 -> 0xe83f
        [ 0xe83f, ['Unknown']],
    ],
    [ # 0xe840 -> 0xe87f
        [ 0xe87f, ['Unknown']],
    ],
    [ # 0xe880 -> 0xe8bf
        [ 0xe8bf, ['Unknown']],
    ],
    [ # 0xe8c0 -> 0xe8ff
        [ 0xe8ff, ['Unknown']],
    ],
    [ # 0xe900 -> 0xe93f
        [ 0xe93f, ['Unknown']],
    ],
    [ # 0xe940 -> 0xe97f
        [ 0xe97f, ['Unknown']],
    ],
    [ # 0xe980 -> 0xe9bf
        [ 0xe9bf, ['Unknown']],
    ],
    [ # 0xe9c0 -> 0xe9ff
        [ 0xe9ff, ['Unknown']],
    ],
    [ # 0xea00 -> 0xea3f
        [ 0xea3f, ['Unknown']],
    ],
    [ # 0xea40 -> 0xea7f
        [ 0xea7f, ['Unknown']],
    ],
    [ # 0xea80 -> 0xeabf
        [ 0xeabf, ['Unknown']],
    ],
    [ # 0xeac0 -> 0xeaff
        [ 0xeaff, ['Unknown']],
    ],
    [ # 0xeb00 -> 0xeb3f
        [ 0xeb3f, ['Unknown']],
    ],
    [ # 0xeb40 -> 0xeb7f
        [ 0xeb7f, ['Unknown']],
    ],
    [ # 0xeb80 -> 0xebbf
        [ 0xebbf, ['Unknown']],
    ],
    [ # 0xebc0 -> 0xebff
        [ 0xebff, ['Unknown']],
    ],
    [ # 0xec00 -> 0xec3f
        [ 0xec3f, ['Unknown']],
    ],
    [ # 0xec40 -> 0xec7f
        [ 0xec7f, ['Unknown']],
    ],
    [ # 0xec80 -> 0xecbf
        [ 0xecbf, ['Unknown']],
    ],
    [ # 0xecc0 -> 0xecff
        [ 0xecff, ['Unknown']],
    ],
    [ # 0xed00 -> 0xed3f
        [ 0xed3f, ['Unknown']],
    ],
    [ # 0xed40 -> 0xed7f
        [ 0xed7f, ['Unknown']],
    ],
    [ # 0xed80 -> 0xedbf
        [ 0xedbf, ['Unknown']],
    ],
    [ # 0xedc0 -> 0xedff
        [ 0xedff, ['Unknown']],
    ],
    [ # 0xee00 -> 0xee3f
        [ 0xee3f, ['Unknown']],
    ],
    [ # 0xee40 -> 0xee7f
        [ 0xee7f, ['Unknown']],
    ],
    [ # 0xee80 -> 0xeebf
        [ 0xeebf, ['Unknown']],
    ],
    [ # 0xeec0 -> 0xeeff
        [ 0xeeff, ['Unknown']],
    ],
    [ # 0xef00 -> 0xef3f
        [ 0xef3f, ['Unknown']],
    ],
    [ # 0xef40 -> 0xef7f
        [ 0xef7f, ['Unknown']],
    ],
    [ # 0xef80 -> 0xefbf
        [ 0xefbf, ['Unknown']],
    ],
    [ # 0xefc0 -> 0xefff
        [ 0xefff, ['Unknown']],
    ],
    [ # 0xf000 -> 0xf03f
        [ 0xf03f, ['Unknown']],
    ],
    [ # 0xf040 -> 0xf07f
        [ 0xf07f, ['Unknown']],
    ],
    [ # 0xf080 -> 0xf0bf
        [ 0xf0bf, ['Unknown']],
    ],
    [ # 0xf0c0 -> 0xf0ff
        [ 0xf0ff, ['Unknown']],
    ],
    [ # 0xf100 -> 0xf13f
        [ 0xf13f, ['Unknown']],
    ],
    [ # 0xf140 -> 0xf17f
        [ 0xf17f, ['Unknown']],
    ],
    [ # 0xf180 -> 0xf1bf
        [ 0xf1bf, ['Unknown']],
    ],
    [ # 0xf1c0 -> 0xf1ff
        [ 0xf1ff, ['Unknown']],
    ],
    [ # 0xf200 -> 0xf23f
        [ 0xf23f, ['Unknown']],
    ],
    [ # 0xf240 -> 0xf27f
        [ 0xf27f, ['Unknown']],
    ],
    [ # 0xf280 -> 0xf2bf
        [ 0xf2bf, ['Unknown']],
    ],
    [ # 0xf2c0 -> 0xf2ff
        [ 0xf2ff, ['Unknown']],
    ],
    [ # 0xf300 -> 0xf33f
        [ 0xf33f, ['Unknown']],
    ],
    [ # 0xf340 -> 0xf37f
        [ 0xf37f, ['Unknown']],
    ],
    [ # 0xf380 -> 0xf3bf
        [ 0xf3bf, ['Unknown']],
    ],
    [ # 0xf3c0 -> 0xf3ff
        [ 0xf3ff, ['Unknown']],
    ],
    [ # 0xf400 -> 0xf43f
        [ 0xf43f, ['Unknown']],
    ],
    [ # 0xf440 -> 0xf47f
        [ 0xf47f, ['Unknown']],
    ],
    [ # 0xf480 -> 0xf4bf
        [ 0xf4bf, ['Unknown']],
    ],
    [ # 0xf4c0 -> 0xf4ff
        [ 0xf4ff, ['Unknown']],
    ],
    [ # 0xf500 -> 0xf53f
        [ 0xf53f, ['Unknown']],
    ],
    [ # 0xf540 -> 0xf57f
        [ 0xf57f, ['Unknown']],
    ],
    [ # 0xf580 -> 0xf5bf
        [ 0xf5bf, ['Unknown']],
    ],
    [ # 0xf5c0 -> 0xf5ff
        [ 0xf5ff, ['Unknown']],
    ],
    [ # 0xf600 -> 0xf63f
        [ 0xf63f, ['Unknown']],
    ],
    [ # 0xf640 -> 0xf67f
        [ 0xf67f, ['Unknown']],
    ],
    [ # 0xf680 -> 0xf6bf
        [ 0xf6bf, ['Unknown']],
    ],
    [ # 0xf6c0 -> 0xf6ff
        [ 0xf6ff, ['Unknown']],
    ],
    [ # 0xf700 -> 0xf73f
        [ 0xf73f, ['Unknown']],
    ],
    [ # 0xf740 -> 0xf77f
        [ 0xf77f, ['Unknown']],
    ],
    [ # 0xf780 -> 0xf7bf
        [ 0xf7bf, ['Unknown']],
    ],
    [ # 0xf7c0 -> 0xf7ff
        [ 0xf7ff, ['Unknown']],
    ],
    [ # 0xf800 -> 0xf83f
        [ 0xf83f, ['Unknown']],
    ],
    [ # 0xf840 -> 0xf87f
        [ 0xf87f, ['Unknown']],
    ],
    [ # 0xf880 -> 0xf8bf
        [ 0xf8bf, ['Unknown']],
    ],
    [ # 0xf8c0 -> 0xf8ff
        [ 0xf8ff, ['Unknown']],
    ],
    [ # 0xf900 -> 0xf93f
        [ 0xf93f, ['Han']],
    ],
    [ # 0xf940 -> 0xf97f
        [ 0xf97f, ['Han']],
    ],
    [ # 0xf980 -> 0xf9bf
        [ 0xf9bf, ['Han']],
    ],
    [ # 0xf9c0 -> 0xf9ff
        [ 0xf9ff, ['Han']],
    ],
    [ # 0xfa00 -> 0xfa3f
        [ 0xfa3f, ['Han']],
    ],
    [ # 0xfa40 -> 0xfa7f
        [ 0xfa6d, ['Han']],
        [ 0xfa6f, ['Unknown']],
        [ 0xfa7f, ['Han']],
    ],
    [ # 0xfa80 -> 0xfabf
        [ 0xfabf, ['Han']],
    ],
    [ # 0xfac0 -> 0xfaff
        [ 0xfad9, ['Han']],
        [ 0xfaff, ['Unknown']],
    ],
    [ # 0xfb00 -> 0xfb3f
        [ 0xfb06, ['Latin']],
        [ 0xfb12, ['Unknown']],
        [ 0xfb17, ['Armenian']],
        [ 0xfb1c, ['Unknown']],
        [ 0xfb36, ['Hebrew']],
        [ 0xfb37, ['Unknown']],
        [ 0xfb3c, ['Hebrew']],
        [ 0xfb3d, ['Unknown']],
        [ 0xfb3f, ['Hebrew']],
    ],
    [ # 0xfb40 -> 0xfb7f
        [ 0xfb41, ['Hebrew']],
        [ 0xfb42, ['Unknown']],
        [ 0xfb44, ['Hebrew']],
        [ 0xfb45, ['Unknown']],
        [ 0xfb4f, ['Hebrew']],
        [ 0xfb7f, ['Arabic']],
    ],
    [ # 0xfb80 -> 0xfbbf
        [ 0xfbbf, ['Arabic']],
    ],
    [ # 0xfbc0 -> 0xfbff
        [ 0xfbc1, ['Arabic']],
        [ 0xfbd2, ['Unknown']],
        [ 0xfbff, ['Arabic']],
    ],
    [ # 0xfc00 -> 0xfc3f
        [ 0xfc3f, ['Arabic']],
    ],
    [ # 0xfc40 -> 0xfc7f
        [ 0xfc7f, ['Arabic']],
    ],
    [ # 0xfc80 -> 0xfcbf
        [ 0xfcbf, ['Arabic']],
    ],
    [ # 0xfcc0 -> 0xfcff
        [ 0xfcff, ['Arabic']],
    ],
    [ # 0xfd00 -> 0xfd3f
        [ 0xfd3d, ['Arabic']],
        [ 0xfd3f, ['Common']],
    ],
    [ # 0xfd40 -> 0xfd7f
        [ 0xfd40, ['Common']],
        [ 0xfd4f, ['Unknown']],
        [ 0xfd7f, ['Arabic']],
    ],
    [ # 0xfd80 -> 0xfdbf
        [ 0xfd8f, ['Arabic']],
        [ 0xfd91, ['Unknown']],
        [ 0xfdbf, ['Arabic']],
    ],
    [ # 0xfdc0 -> 0xfdff
        [ 0xfdc7, ['Arabic']],
        [ 0xfdef, ['Unknown']],
        [ 0xfdf1, ['Arabic']],
        [ 0xfdf3, ['Thaana', 'Arabic']],
        [ 0xfdfc, ['Arabic']],
        [ 0xfdfe, ['Thaana', 'Arabic']],
        [ 0xfdff, ['Unknown']],
    ],
    [ # 0xfe00 -> 0xfe3f
        [ 0xfe0f, ['Inherited']],
        [ 0xfe1a, ['Common']],
        [ 0xfe1f, ['Unknown']],
        [ 0xfe2d, ['Inherited']],
        [ 0xfe2f, ['Unknown']],
        [ 0xfe3f, ['Common']],
    ],
    [ # 0xfe40 -> 0xfe7f
        [ 0xfe44, ['Common']],
        [ 0xfe46, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Han', 'Common']],
        [ 0xfe52, ['Common']],
        [ 0xfe53, ['Unknown']],
        [ 0xfe66, ['Common']],
        [ 0xfe67, ['Unknown']],
        [ 0xfe6b, ['Common']],
        [ 0xfe6f, ['Unknown']],
        [ 0xfe74, ['Arabic']],
        [ 0xfe75, ['Unknown']],
        [ 0xfe7f, ['Arabic']],
    ],
    [ # 0xfe80 -> 0xfebf
        [ 0xfebf, ['Arabic']],
    ],
    [ # 0xfec0 -> 0xfeff
        [ 0xfefc, ['Arabic']],
        [ 0xfefe, ['Unknown']],
        [ 0xfeff, ['Common']],
    ],
    [ # 0xff00 -> 0xff3f
        [ 0xff20, ['Common']],
        [ 0xff3a, ['Latin']],
        [ 0xff3f, ['Common']],
    ],
    [ # 0xff40 -> 0xff7f
        [ 0xff40, ['Common']],
        [ 0xff41, ['Latin', 'Common']],
        [ 0xff5a, ['Latin']],
        [ 0xff60, ['Common']],
        [ 0xff65, ['Hiragana', 'Hangul', 'Bopomofo', 'Katakana', 'Yi', 'Han', 'Common']],
        [ 0xff6f, ['Katakana']],
        [ 0xff71, ['Hiragana', 'Katakana', 'Common']],
        [ 0xff7f, ['Katakana']],
    ],
    [ # 0xff80 -> 0xffbf
        [ 0xff9d, ['Katakana']],
        [ 0xff9f, ['Hiragana', 'Katakana', 'Common']],
        [ 0xffbe, ['Hangul']],
        [ 0xffbf, ['Unknown']],
    ],
    [ # 0xffc0 -> 0xffff
        [ 0xffc1, ['Unknown']],
        [ 0xffc7, ['Hangul']],
        [ 0xffc9, ['Unknown']],
        [ 0xffcf, ['Hangul']],
        [ 0xffd1, ['Unknown']],
        [ 0xffd7, ['Hangul']],
        [ 0xffd9, ['Unknown']],
        [ 0xffdc, ['Hangul']],
        [ 0xffdf, ['Unknown']],
        [ 0xffe6, ['Common']],
        [ 0xffe7, ['Unknown']],
        [ 0xffee, ['Common']],
        [ 0xfff8, ['Unknown']],
        [ 0xfffd, ['Common']],
        [ 0xffff, ['Unknown']],
    ],
]
