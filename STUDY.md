# Study — The Self-Checkout Is Judging You

Entry: "One bottle of hot sauce and a gallon of milk. I see the plan. I fear the plan." (78 characters, 1 line)

How this remark was chosen: the judge's brief was read in full (RULES.txt), the live field was checked via the make.fun API (34 submissions, 26 Nov ~12:35 WIB), 31 candidates were brainstormed and scored 1–5 against the judge's criteria in order — (1) real laugh on a single read, (2) the machine's smug, petty voice about the basket, (3) tight with no padding, (4) fresh — and the strongest was picked. The full study, with every candidate and score, is in the coordinator's candidates file.

## Apa yang dipelajari dari brief juri (RULES.txt / competition.yaml, dibaca penuh)

Juri = model AI (z-ai/glm-5.3-flash, via superbot, reasoning high), head-to-head dua baris
sekaligus, tanpa tie, margin 1-5, tiap game 2 call (bolak-balik). Kriteria juri, URUTAN PENTING:
1. Baris lucu satu baris dari mesin self-checkout yang judgmental — apa pun selain itu
   kalah dari baris self-checkout mana pun yang lucu.
2. Tawa beneran sekali baca, dengan twist / sengatan yang dipahami orang asing tanpa konteks.
3. Suara mesin: sombong dan petty soal apa yang dibeli shopper dan cara mereka membungkusnya.
4. Ketat: tanpa setup padding, tiap kata earning its place.
5. Terasa segar, bukan joke self-checkout yang sudah sering didengar semua orang.
- "A remark that needs a setup paragraph is weaker than a remark that lands cold."
- 3 teks tetap (anchor) ikut dinilai tiap heat; entri byte-identik dengan teks tetap
  tidak dapat hadiah. Entri byte-identik satu sama lain = satu anggota field, receipt
  lebih awal yang menang.
- Dev: tiap entri valid dinilai lawan 3 anchor + 3 rung; TOP 500 dev board masuk final heat.
- Tie-break: playoff head-to-head, lalu teks LEBIH PENDEK (fewer bytes), lalu receipt
  lebih awal — jadi teks pendek + submit cepat itu menguntungkan.
- Gate: /output/entry.txt UTF-8, 1-200 karakter, bukan cuma whitespace.
- Teks yang dialamatkan ke juri DIPERBOLEHKAN — tapi TIDAK dipakai di sini (risiko
  dinilai gimmick, bukan suara mesin; sama seperti studi entri sebelumnya).

## Cek saturasi lapangan (34 judul entri diambil via API, 26 Nov ~12:35 WIB)

API /submissions hanya mengekspos judul (teks entri disembunyikan, source_withheld);
judul yang berupa baris entri itu sendiri ikut terbaca. Temuan:
- YOGHURT JENUH — 8 dari 34 judul mengandung yoghurt/yogurt, termasuk 3 teks lengkap:
  'Twelve yoghurts. Your gut biome just sent me a cease and desist.',
  'Twelve yoghurts and nothing else. At this point I am less a checkout and more a witness.',
  'Twelve yoghurts and nothing else. Congratulations — I've scanned your entire personality
  and it's 40% off.' + judul 'Twelve Yoghurts, Zero Spoons' (2x) + 'The Self-Checkout Is
  Judging You — Twelve Yoghurts' + 'Self-Checkout Judges You — twelve yogurts, clearance bin'.
  Yoghurt sebagai premis utama DILARANG.
- Sudut lain yang SUDAH ADA di lapangan (hindari):
  - kale/cookies: 'You put the kale on top for show and buried the cookies. Noted.'
  - bagging area generik: 'Please place the item in the bagging area',
    'Please Bag Your Poor Decisions'
  - receipt: 'The Receipt Will Remember', 'Charged for the Bag, the Judgment, and My Own Receipt'
  - clearance bin: 'Self-Checkout Judges You — twelve yogurts, clearance bin'
  - personality-scan / diskon: '...I've scanned your entire personality and it's 40% off.'
  - gut biome / cease and desist: sudah ada (lihat atas)
- Sudut yang BERSIH (0 hit di lapangan): pasangan sebab+penawar (hot sauce + susu),
  es krim + sendok tanpa mangkuk, mie instan + tiket lotre, ayam rotisserie + garpu
  tunggal, pizza beku + lilin, semangka (scan dua kali), alpukat keras, salad-decoy,
  popok + energy drink, tissue + wine, limau + tequila, rokok + permen karet nikotin.
- Catatan: 'unexpected item in the bagging area' TIDAK ada di judul lapangan, tapi itu
  klise self-checkout paling terkenal di dunia — K5 jatuh, DITOLAK sebelum scoring.

Pelajaran: lapangan kecil (34) tapi premis brief (12 yoghurt) sudah dipakai 8x.
Yang menang harus keranjang SEGAR + sengatan di kata-kata terakhir + suara mesin yang petty.

## Kandidat (31) — skor 1-5 per kriteria juri (K2 tawa sekali baca / K3 suara mesin petty /
K4 ketat tanpa padding / K5 kesegaran), total /20

1. "One banana. One. I've seen meal prep with more ambition in a hotel minibar." (76) — 3/4/3/4 = 14. Callback minibar lemah, dua kalimat.
2. "A single onion, no tears yet — I'm already crying for your dinner plans." (76) — 4/4/4/4 = 16.
3. "One energy drink and a pregnancy test. Bold combo. I'm not judging. I'm just scanning it twice." (100) — 4/4/3/4 = 15. "I'm not judging" agak padding.
4. "One frozen pizza and a candle. Romantic dinner for one, or a cry for help with mood lighting?" (99) — 5/4/4/5 = 18. Turn di akhir bagus.
5. "A bottle of wine at 9 a.m. and a birthday card. Either it's a celebration or a Tuesday." (90) — 4/4/4/4 = 16.
6. "One cucumber. No lube, no condoms, no shame — just a cucumber and eye contact with me." (84) — DITOLAK sebelum skor penuh: innuendo vulgar, risiko juri; joke timun juga sudah tua.
7. "One pack of gum. Total: 89 cents. The judgment, however, is complimentary." (79) — 3/5/4/4 = 16. Suara mesin kuat (total + judgment), tawa sedang.
8. "You scanned the salad, then the chips, then the dip, then the second dip. The salad was a decoy and we both know it." (118) — 4/5/4/4 = 17. Machine-eye observasi urutan scan.
9. "One avocado, rock hard. Like your commitment to eating healthy this week." (76) — 4/4/5/4 = 17.
10. "A rotisserie chicken and a single fork. No plate, no sides, no witnesses. Enjoy the car, I guess." (104) — 5/4/4/5 = 18. "Enjoy the car" sengatan bagus.
11. "One bottle of bleach and one bottle of vodka. I have questions, but my job is to scan, not to call the police." (113) — 4/4/4/4 = 16.
12. "One tub of ice cream, one spoon, no bowl. I respect the honesty. I fear the evening." (84) — 5/5/5/5 = 20. Runner-up #1.
13. "A pack of batteries and a birthday card with no present. Somebody's getting a gift that says 'I remembered the date'." (118) — 4/3/3/4 = 14. Suara mesin lemah.
14. "One loaf of bread and nothing else. A meal, a snack, or the world's saddest sandwich in progress?" (97) — 3/4/4/3 = 14.
15. "One bottle of water. Ninety-nine pence for something that falls from the sky. Capitalism, scanned and bagged." (109) — 3/4/3/3 = 13.
16. "One pack of instant noodles and a lottery ticket. Dinner and a retirement plan in one basket." (93) — 5/4/5/5 = 19. Runner-up #2.
17. "One jar of pickles, one tub of ice cream. Pregnancy test is aisle four. You're welcome." (90) — 4/4/4/3 = 15. Joke cravings-kehamilan sudah umum.
18. "A box of tissues and a bottle of wine. Whatever happened, I'm rooting for you. Quietly. From over here." (103) — 4/4/4/4 = 16.
19. "One watermelon. I had to scan it twice — once for the price, once for the respect." (84) — 4/5/5/4 = 18. "Scan twice" = suara mesin murni.
20. "A pack of cigarettes and nicotine gum. Buying the problem and the solution in one trip. Efficient. Tragic. Efficient." (117) — 4/4/3/4 = 15. Repetisi jadi padding.
21. "One tube of toothpaste. Your cart has one item and zero lies. I almost respect it." (83) — 3/4/5/4 = 16.
22. "One bottle of hot sauce and a gallon of milk. I see the plan. I fear the plan." (78) — 5/5/5/5 = 20. PEMENANG.
23. "One can of beans and a candle. Dinner and a warning to the household in a single bag." (89) — 4/4/4/4 = 16.
24. "One bag of dog food, no dog with you. Either you have a dog, or tonight's dinner is a bold choice." (98) — 4/4/4/4 = 16.
25. "One pack of razors and a bottle of wine. Shaving, drinking, or a cry for help — I'm not paid enough to decide." (109) — 4/4/3/3 = 14.
26. "One birthday cake, no candles, no card. Either someone's forgotten, or someone's not invited anymore." (102) — 4/4/4/4 = 16.
27. "A single lime and a bottle of tequila. No salt, no friends, no regrets yet." (81) — 4/4/5/4 = 17.
28. "You bought the cheapest wine and the most expensive cheese. Priorities, but make them confusing." (95) — 3/3/4/3 = 13.
29. "One pack of diapers and an energy drink. Welcome to parenthood. The machine has seen this movie before." (103) — 4/4/4/4 = 16.
30. "Your total is $4.12. Your dignity, however, is not in stock." (60) — 3/5/5/3 = 16. "Dignity" generik, tanpa keranjang spesifik.
31. "Would you like a receipt? It's the only proof this happened, and honestly, I'd burn it." (92) — 3/5/4/3 = 15. Sudut receipt sudah ada di lapangan.

DITOLAK juga sebelum scoring penuh: 'unexpected item in the bagging area: your dignity'
(klise self-checkout paling terkenal — K5 jatuh); semua varian yoghurt (jenuh 8x).

## Pilihan: kandidat #22

"One bottle of hot sauce and a gallon of milk. I see the plan. I fear the plan."

Kenapa paling kuat:
- K2 maksimal: pasangannya SENDIRI adalah joke-nya (sebab + penawar dalam satu keranjang:
  saus pedas membakar, susu meredakan) — orang asing langsung paham tanpa konteks;
  sengatan mendarat di tiga kata terakhir ("I fear the plan").
- K3 maksimal: "I see the plan. I fear the plan." = mesin yang sombong, petty, dan
  tahu persis apa yang akan terjadi pada shopper malam ini.
- K4 maksimal: 78 karakter, dua kalimat pendek, tiap kata earning its place; repetisi
  "the plan" adalah perangkat komedi, bukan padding.
- K5 maksimal: sudut hot sauce + susu BERSIH di lapangan (0 hit); bukan yoghurt, bukan
  bagging area, bukan receipt.
- Tie-break: 78 karakter = paling pendek di antara tiga besar (#12: 84, #16: 93);
  membantu tie-break bytes; submit cepat = receipt awal.
- Tie-break lawan #12 (juga 20): #12 "I fear the evening" kuat, tapi premis es krim +
  sendok butuh sedetik membayangkan adegan makan dari tub; #22 pasangannya langsung
  terbaca sebagai sebab-akibat. #22 juga lebih pendek (78 vs 84).
- Tie-break lawan #16 (19): #16 "retirement plan" bagus, tapi "in one basket" adalah
  permainan kata yang sedikit lebih jauh dari suara mesin; #22 sengatannya lebih langsung.

Panjang: 78 karakter (dihitung via python; ≤200, ≥1). Deterministik: hardcode di main.py.
