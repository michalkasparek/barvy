50 barevných palet vytahaných z knižních ilustrací a obrazů.
 
 Rychlý import palet do kódu:
 
1. ```wget https://github.com/michalkasparek/barvy/blob/master/barvy.json```

2. ```with open('barvy.json', 'r', encoding='utf-8') as vstup:```  
$~~~~$```vstup = json.loads(vstup.read())```

3. ```barvy["název_palety"]```

U naprosté většiny palet je předposlední barva v seznamu černá (či nejtmavší barva na stránce) a poslední bílá (či nejsvětlejší barva na stránce).

Vedle výchozí ručně poskládané palety se generuje ještě seznam ```název_palety_sorted``` poskládaný od nejsytější (typicky černé) po nejméně sytou (typicky bílé).

## jak_s_tim_pohnu_kladka

originál: [Jak s tím pohnu](https://www.digitalniknihovna.cz/mzk/view/uuid:e5747fb0-81c3-11e3-a6e0-005056827e52?page=uuid:76393b40-8c63-11e3-bbb0-5ef3fc9bb22f), kudos: František Škoda

```['#D6534B', '#445B78', '#DB842F', '#70871E', '#EED801', '#5E2D3A', '#81A9D5', '#E09DA3', '#292829', '#FFFFE4']```

![jak_s_tim_pohnu_kladka](palety/jak_s_tim_pohnu_kladka.png)

```['#292829', '#5E2D3A', '#445B78', '#70871E', '#D6534B', '#DB842F', '#81A9D5', '#E09DA3', '#EED801', '#FFFFE4']```

![jak_s_tim_pohnu_kladka_sorted](palety/jak_s_tim_pohnu_kladka_sorted.png)

## rychle_sipy_kocici_pracka_chysta_lecku

originál: [Zlaté údolí (příběhy ze starých časopisů)](https://www.digitalniknihovna.cz/mzk/view/uuid:9b1279b0-4ddc-11e3-9c86-005056827e51?page=uuid:81872710-8f0a-11e3-83a0-005056825209), kudos: Jan Fischer

```['#BC3A5D', '#2B61A2', '#D1BC18', '#1D5939', '#812E59', '#688D34', '#D67BA5', '#D8C6A3', '#C7CE51', '#8EB0CF', '#130D15', '#ECEADC']```

![rychle_sipy_kocici_pracka_chysta_lecku](palety/rychle_sipy_kocici_pracka_chysta_lecku.png)

```['#130D15', '#1D5939', '#812E59', '#2B61A2', '#BC3A5D', '#688D34', '#D67BA5', '#8EB0CF', '#D1BC18', '#C7CE51', '#D8C6A3', '#ECEADC']```

![rychle_sipy_kocici_pracka_chysta_lecku_sorted](palety/rychle_sipy_kocici_pracka_chysta_lecku_sorted.png)

## rychle_sipy_rychlonozka_krasobruslar

originál: [Zlaté údolí (příběhy ze starých časopisů)](https://www.digitalniknihovna.cz/mzk/view/uuid:9b1279b0-4ddc-11e3-9c86-005056827e51?page=uuid:8240da20-8f0a-11e3-83a0-005056825209), kudos: Jan Fischer

```['#CA4955', '#316DC1', '#E4D104', '#1B4D21', '#A9752F', '#D07863', '#9ABFDD', '#7A9648', '#171412', '#F7F5DC']```

![rychle_sipy_rychlonozka_krasobruslar](palety/rychle_sipy_rychlonozka_krasobruslar.png)

```['#171412', '#1B4D21', '#316DC1', '#CA4955', '#A9752F', '#7A9648', '#D07863', '#9ABFDD', '#E4D104', '#F7F5DC']```

![rychle_sipy_rychlonozka_krasobruslar_sorted](palety/rychle_sipy_rychlonozka_krasobruslar_sorted.png)

## arnal_12

originál: [Arnal a dva dračí zuby & jiné příběhy](https://www.digitalniknihovna.cz/mzk/view/uuid:60c17870-1378-11ef-aef8-5ef3fc9bb22f?page=uuid:a24e90a4-c91d-4780-86d3-99d66097ff45), kudos: Kája Saudek

```['#AF4752', '#01A1BC', '#F1AFC5', '#F89E43', '#A1D3D9', '#E6B095', '#9CB872', '#B3CBD2', '#FBE597', '#212625', '#FDFDFF']```

![arnal_12](palety/arnal_12.png)

```['#212625', '#AF4752', '#01A1BC', '#9CB872', '#F89E43', '#E6B095', '#B3CBD2', '#A1D3D9', '#F1AFC5', '#FBE597', '#FDFDFF']```

![arnal_12_sorted](palety/arnal_12_sorted.png)

## arnal_32

originál: [Arnal a dva dračí zuby & jiné příběhy](https://www.digitalniknihovna.cz/mzk/view/uuid:60c17870-1378-11ef-aef8-5ef3fc9bb22f?page=uuid:611cd9f8-fdb6-44d6-8c13-8f045584b85b), kudos: Kája Saudek

```['#DE4D49', '#8F7B9B', '#F27C55', '#43335B', '#F0F2ED', '#BA8A72', '#c1c1c1', '#202622', '#F1F3EE']```

![arnal_32](palety/arnal_32.png)

```['#202622', '#43335B', '#DE4D49', '#8F7B9B', '#BA8A72', '#F27C55', '#c1c1c1', '#F0F2ED', '#F1F3EE']```

![arnal_32_sorted](palety/arnal_32_sorted.png)

## ctyrlistek_mic

originál: [Čtyřlístek: Nebezpečný míč](https://www.digitalniknihovna.cz/mzk/view/uuid:d7cde440-b743-11ed-9a20-5ef3fc9bb22f?page=uuid:773ae6a0-0dfc-4619-86e0-d7260e070955), kudos: Jaroslav Němeček

```['#C66774', '#619AC1', '#BCBE73', '#D6C1BF', '#EDDC73', '#8C8CB0', '#C9D6D8', '#D0A77E', '#E7E5DA', '#5D615E', '#E1E4D7']```

![ctyrlistek_mic](palety/ctyrlistek_mic.png)

```['#5D615E', '#C66774', '#619AC1', '#8C8CB0', '#D0A77E', '#BCBE73', '#D6C1BF', '#C9D6D8', '#EDDC73', '#E1E4D7', '#E7E5DA']```

![ctyrlistek_mic_sorted](palety/ctyrlistek_mic_sorted.png)

## jeden_den_prazdnin_12

originál: [Jeden den prázdnin](https://www.digitalniknihovna.cz/mzk/view/uuid:8bc323c0-5079-11ed-bb57-005056827e52?page=uuid:a897f817-3507-4226-a48e-f244c18f661c), kudos: Kamil Lhoták

```['#788A98', '#D15A41', '#D5B574', '#A6AC83', '#E0AC93', '#D98D72', '#3E403F', '#E8DECA']```

![jeden_den_prazdnin_12](palety/jeden_den_prazdnin_12.png)

```['#3E403F', '#D15A41', '#788A98', '#D98D72', '#A6AC83', '#D5B574', '#E0AC93', '#E8DECA']```

![jeden_den_prazdnin_12_sorted](palety/jeden_den_prazdnin_12_sorted.png)

## dalekohled_8

originál: [Dalekohled, aneb, Kdo nevěří ať tam běží](https://www.digitalniknihovna.cz/mzk/view/uuid:3fde9240-2df4-11e6-ae84-005056827e51?page=uuid:e9853dc0-3d45-11e6-ad5e-5ef3fc9bb22f), kudos: Adolf Hoffmeister

```['#744235', '#7A8C98', '#B27485', '#626F5F', '#C0915A', '#D1B367', '#413940', '#AE7B5C', '#716966', '#EDE4D6']```

![dalekohled_8](palety/dalekohled_8.png)

```['#413940', '#744235', '#626F5F', '#716966', '#AE7B5C', '#7A8C98', '#B27485', '#C0915A', '#D1B367', '#EDE4D6']```

![dalekohled_8_sorted](palety/dalekohled_8_sorted.png)

## dalekohled_64

originál: [Dalekohled, aneb, Kdo nevěří ať tam běží](https://www.digitalniknihovna.cz/mzk/view/uuid:3fde9240-2df4-11e6-ae84-005056827e51?page=uuid:f03260d0-3d45-11e6-ad5e-5ef3fc9bb22f), kudos: Adolf Hoffmeister

```['#90a4ab', '#aa6572', '#6f7e65', '#aa7355', '#6b3c32', '#889da4', '#7e8b67', '#9a5446', '#3a3432', '#ece0d0']```

![dalekohled_64](palety/dalekohled_64.png)

```['#3a3432', '#6b3c32', '#9a5446', '#6f7e65', '#aa6572', '#aa7355', '#7e8b67', '#889da4', '#90a4ab', '#ece0d0']```

![dalekohled_64_sorted](palety/dalekohled_64_sorted.png)

## dalekohled_112

originál: [Dalekohled, aneb, Kdo nevěří ať tam běží](https://www.digitalniknihovna.cz/mzk/view/uuid:3fde9240-2df4-11e6-ae84-005056827e51?page=uuid:f663c430-3d45-11e6-ad5e-5ef3fc9bb22f), kudos: Adolf Hoffmeister

```['#8E4930', '#BF9651', '#A7653F', '#4A4B5F', '#BD9752', '#4C5B43', '#36312D', '#EEE0D1']```

![dalekohled_112](palety/dalekohled_112.png)

```['#36312D', '#4A4B5F', '#4C5B43', '#8E4930', '#A7653F', '#BF9651', '#BD9752', '#EEE0D1']```

![dalekohled_112_sorted](palety/dalekohled_112_sorted.png)

## dalekohled_124

originál: [Dalekohled, aneb, Kdo nevěří ať tam běží](https://www.digitalniknihovna.cz/mzk/view/uuid:3fde9240-2df4-11e6-ae84-005056827e51?page=uuid:f8f01460-3d45-11e6-ad5e-5ef3fc9bb22f), kudos: Adolf Hoffmeister

```['#924d30', '#d2c9bb', '#c1a15e', '#667255', '#a46f4d', '#8f867d', '#7c939b', '#484149', '#b4777e', '#e5dbcc']```

![dalekohled_124](palety/dalekohled_124.png)

```['#484149', '#924d30', '#667255', '#a46f4d', '#8f867d', '#b4777e', '#7c939b', '#c1a15e', '#d2c9bb', '#e5dbcc']```

![dalekohled_124_sorted](palety/dalekohled_124_sorted.png)

## uprka_pout_u_svateho_antonicka

originál: [Joža a Franta Uprkové](https://www.digitalniknihovna.cz/mzk/view/uuid:4071a980-3d57-11e8-84e3-005056827e52?page=uuid:06042f50-6a22-11e8-bfeb-5ef3fc9bb22f), kudos: Joža Uprka

```['#690A05', '#B72D0D', '#E99A2B', '#879BBB', '#354150', '#CB9276', '#313C15', '#54736E', '#6B6222', '#F1D1BB', '#080608', '#F9F7E8']```

![uprka_pout_u_svateho_antonicka](palety/uprka_pout_u_svateho_antonicka.png)

```['#080608', '#690A05', '#313C15', '#354150', '#B72D0D', '#6B6222', '#54736E', '#879BBB', '#CB9276', '#E99A2B', '#F1D1BB', '#F9F7E8']```

![uprka_pout_u_svateho_antonicka_sorted](palety/uprka_pout_u_svateho_antonicka_sorted.png)

## kupka_unik

originál: [František Kupka 1871-1957](https://www.digitalniknihovna.cz/mzk/view/uuid:395a6900-d035-11e7-b06b-005056827e51?page=uuid:b0b33bb0-0caa-11e8-bdb0-005056827e51), kudos: František Kupka

```['#340830', '#723155', '#911B15', '#B48E18', '#B4A134', '#285531', '#637946', '#030434', '#295B89', '#8898A0', '#070120', '#D1C9B3']```

![kupka_unik](palety/kupka_unik.png)

```['#070120', '#030434', '#340830', '#911B15', '#285531', '#723155', '#295B89', '#637946', '#B48E18', '#8898A0', '#B4A134', '#D1C9B3']```

![kupka_unik_sorted](palety/kupka_unik_sorted.png)

## kupka_klavesy_piana_jezero

originál: [František Kupka 1871-1957](https://www.digitalniknihovna.cz/mzk/view/uuid:395a6900-d035-11e7-b06b-005056827e51?page=uuid:b0246930-0caa-11e8-bdb0-005056827e51), kudos: František Kupka

```['#3B0303', '#142637', '#8A1513', '#676416', '#9C503F', '#2D2D09', '#959278', '#020102', '#FEFAE7']```

![kupka_klavesy_piana_jezero](palety/kupka_klavesy_piana_jezero.png)

```['#020102', '#3B0303', '#142637', '#2D2D09', '#8A1513', '#676416', '#9C503F', '#959278', '#FEFAE7']```

![kupka_klavesy_piana_jezero_sorted](palety/kupka_klavesy_piana_jezero_sorted.png)

## stafl_havlbrod_iv

originál: [Šestnáct akvarelů z Havlíčkova Brodu](https://ndk.cz/view/uuid:ed07a3a0-ca09-11ec-aafc-005056827e52?page=uuid:33f437c4-e96d-4f32-932f-7007c19f3703), kudos: Otakar Štáfl

```['#933325', '#424D69', '#5A5E4B', '#A07260', '#9F8455', '#343543', '#AB6E39', '#151412', '#AAA397']```

![stafl_havlbrod_iv](palety/stafl_havlbrod_iv.png)

```['#151412', '#343543', '#424D69', '#933325', '#5A5E4B', '#AB6E39', '#A07260', '#9F8455', '#AAA397']```

![stafl_havlbrod_iv_sorted](palety/stafl_havlbrod_iv_sorted.png)

## solarik_na_okraji_prahy

originál: [Dva světy Karla Solaříka](https://www.digitalniknihovna.cz/mzk/view/uuid:a4604880-8bae-11e2-8593-005056827e52?page=uuid:adaa9d9d-da30-49fb-9605-688df485efd5), kudos: Karel Solařík

```['#AD4439', '#343E50', '#3C4B2B', '#C59553', '#802F2A', '#748852', '#C9B276', '#44616E', '#C09D95', '#141315', '#FEFEFE']```

![solarik_na_okraji_prahy](palety/solarik_na_okraji_prahy.png)

```['#141315', '#343E50', '#3C4B2B', '#802F2A', '#44616E', '#AD4439', '#748852', '#C59553', '#C09D95', '#C9B276', '#FEFEFE']```

![solarik_na_okraji_prahy_sorted](palety/solarik_na_okraji_prahy_sorted.png)

## holan_fotbalove_hriste

originál: [Fotbalové hřiště (Cirkus, Nedělní odpoledne)](https://sbirky.gavu.cz/art/fotbalove-hriste-cirkus-nedelni-odpoledne-13423.html), kudos: Karel Holan

```['#064519', '#7c1216', '#b82f30', '#3e6520', '#00356d', '#73869e', '#636f62', '#ac7203', '#d2912a', '#e67860', '#232022', '#cdcec7']```

![holan_fotbalove_hriste](palety/holan_fotbalove_hriste.png)

```['#232022', '#00356d', '#064519', '#7c1216', '#3e6520', '#b82f30', '#636f62', '#ac7203', '#73869e', '#e67860', '#d2912a', '#cdcec7']```

![holan_fotbalove_hriste_sorted](palety/holan_fotbalove_hriste_sorted.png)

## fila_zatisi

originál: [Zátiší](https://sbirky.gavu.cz/art/zatisi-13159.html), kudos: Emil Filla

```['#d9c165', '#1d3c6b', '#133e32', '#e6c9c5', '#bd7c81', '#f49b02', '#8c4851', '#5a302a', '#77a2b1', '#5c4136', '#aac5b7', '#acb0a7', '#11120f', '#f9f5eb']```

![fila_zatisi](palety/fila_zatisi.png)

```['#11120f', '#133e32', '#1d3c6b', '#5a302a', '#5c4136', '#8c4851', '#bd7c81', '#77a2b1', '#f49b02', '#acb0a7', '#aac5b7', '#d9c165', '#e6c9c5', '#f9f5eb']```

![fila_zatisi_sorted](palety/fila_zatisi_sorted.png)

## hudecek_nocni_chodec

originál: [Noční chodec](https://sbirky.gavu.cz/art/nocni-chodec-13126.html), kudos: František Hudeček

```['#48a385', '#05746b', '#8db768', '#be655e', '#cd8570', '#ebb842', '#885e45', '#2c5377', '#647799', '#6f8685', '#3d3c3b', '#f0c895']```

![hudecek_nocni_chodec](palety/hudecek_nocni_chodec.png)

```['#3d3c3b', '#2c5377', '#05746b', '#885e45', '#647799', '#be655e', '#6f8685', '#48a385', '#cd8570', '#8db768', '#ebb842', '#f0c895']```

![hudecek_nocni_chodec_sorted](palety/hudecek_nocni_chodec_sorted.png)

## kolar_dostihy

originál: [Dostihy](https://sbirky.gavu.cz/art/dostihy-21108.html), kudos: Radomír Kolář

```['#335ca5', '#9f3a90', '#d33c5f', '#df635d', '#34a6a8', '#67a587', '#e57439', '#d0af39', '#6498b1', '#e3caa1', '#a6624b', '#464547', '#f5e9d4']```

![kolar_dostihy](palety/kolar_dostihy.png)

```['#464547', '#335ca5', '#9f3a90', '#d33c5f', '#a6624b', '#34a6a8', '#df635d', '#6498b1', '#67a587', '#e57439', '#d0af39', '#e3caa1', '#f5e9d4']```

![kolar_dostihy_sorted](palety/kolar_dostihy_sorted.png)

## typlt_zememeric

originál: [Zeměměřič](https://sbirky.gavu.cz/art/zememeric-23944.html), kudos: Lubomír Typlt

```['#e60000', '#e5db00', '#9cc002', '#21a055', '#001f80', '#e49996', '#a7ddd6', '#00709c', '#412747', '#6f4693', '#033c46', '#050c19', '#e6e6e4']```

![typlt_zememeric](palety/typlt_zememeric.png)

```['#050c19', '#001f80', '#033c46', '#412747', '#e60000', '#00709c', '#6f4693', '#21a055', '#9cc002', '#e49996', '#e5db00', '#a7ddd6', '#e6e6e4']```

![typlt_zememeric_sorted](palety/typlt_zememeric_sorted.png)

## kadrnozka_jibacoa

originál: [Jibacoa](https://sbirky.gavu.cz/art/jibacoa-20813.html), kudos: Dimitrij Kadrnožka

```['#cd5a60', '#8dc9d2', '#8383a0', '#f4abae', '#717357', '#fee977', '#c4d897', '#faf9f0', '#524b4c']```

![kadrnozka_jibacoa](palety/kadrnozka_jibacoa.png)

```['#524b4c', '#717357', '#cd5a60', '#8383a0', '#8dc9d2', '#f4abae', '#c4d897', '#fee977', '#faf9f0']```

![kadrnozka_jibacoa_sorted](palety/kadrnozka_jibacoa_sorted.png)

## zlate_kvety

originál: [Zlaté květy](https://ndk.cz/view/uuid:3ce7ee90-e3fc-11ed-b90f-005056827e52?page=uuid:8dee3788-c131-49de-be8a-ee481d8ad861)

```['#923644', '#5B6C86', '#9E9B74', '#C29560', '#B48A9A', '#A9514F', '#BD8466', '#3E3543', '#CAB49A']```

![zlate_kvety](palety/zlate_kvety.png)

```['#3E3543', '#923644', '#5B6C86', '#A9514F', '#BD8466', '#9E9B74', '#B48A9A', '#C29560', '#CAB49A']```

![zlate_kvety_sorted](palety/zlate_kvety_sorted.png)

## s_malirem_evropa

originál: [S malířem kolem světa](https://www.digitalniknihovna.cz/mzk/view/uuid:e175ddc0-a1ca-11e2-9a9f-005056827e51?page=uuid:b4cd3840-a7ba-11e2-8c63-5ef3fc9ae867), kudos: Jiří Kalousek

```['#e975b2', '#5d80c1', '#fda24d', '#f77961', '#89a4df', '#ffd71b', '#8eba21', '#ae7645', '#fdc578', '#4B4843', '#FEFEFE']```

![s_malirem_evropa](palety/s_malirem_evropa.png)

```['#4B4843', '#5d80c1', '#ae7645', '#8eba21', '#f77961', '#e975b2', '#89a4df', '#fda24d', '#fdc578', '#ffd71b', '#FEFEFE']```

![s_malirem_evropa_sorted](palety/s_malirem_evropa_sorted.png)

## s_malirem_pristav

originál: [S malířem kolem světa](https://www.digitalniknihovna.cz/mzk/view/uuid:e175ddc0-a1ca-11e2-9a9f-005056827e51?page=uuid:b3b90920-a7ba-11e2-8c63-5ef3fc9ae867), kudos: Jiří Kalousek

```['#d94b60', '#687fa9', '#e3d83b', '#84c0e4', '#cf556b', '#b7d5a9', '#95a8bf', '#b45058', '#a39889', '#1B1417', '#FEFEFE']```

![s_malirem_pristav](palety/s_malirem_pristav.png)

```['#1B1417', '#b45058', '#d94b60', '#cf556b', '#687fa9', '#a39889', '#95a8bf', '#84c0e4', '#b7d5a9', '#e3d83b', '#FEFEFE']```

![s_malirem_pristav_sorted](palety/s_malirem_pristav_sorted.png)

## s_malirem_rio

originál: [S malířem kolem světa](https://www.digitalniknihovna.cz/mzk/view/uuid:e175ddc0-a1ca-11e2-9a9f-005056827e51?page=uuid:d5b300d0-a7ba-11e2-8c63-5ef3fc9ae867&fulltext=rio), kudos: Jiří Kalousek

```['#7C8CCE', '#E7666E', '#FDD22B', '#E79F74', '#7CA6E1', '#F0D27B', '#7B5A57', '#B0CAE6', '#9F7E70', '#90C1F5', '#9E9F91', '#E0DAB5', '#382F22', '#FEFEFE']```

![s_malirem_rio](palety/s_malirem_rio.png)

```['#382F22', '#7B5A57', '#9F7E70', '#E7666E', '#7C8CCE', '#9E9F91', '#7CA6E1', '#E79F74', '#90C1F5', '#B0CAE6', '#FDD22B', '#F0D27B', '#E0DAB5', '#FEFEFE']```

![s_malirem_rio_sorted](palety/s_malirem_rio_sorted.png)

## detska_encyklopedie

originál: [Dětská encyklopedie](https://www.digitalniknihovna.cz/mzk/view/uuid:70adb3c0-db52-11e3-b110-005056827e51?page=uuid:b0bfa660-e347-11e3-bbd5-5ef3fc9bb22f), kudos: Vladimír Fuka

```['#BE7938', '#697E45', '#20353E', '#A7392A', '#9CB19E', '#E3D45F', '#0D0D0B', '#DDD3AF']```

![detska_encyklopedie](palety/detska_encyklopedie.png)

```['#0D0D0B', '#20353E', '#A7392A', '#697E45', '#BE7938', '#9CB19E', '#E3D45F', '#DDD3AF']```

![detska_encyklopedie_sorted](palety/detska_encyklopedie_sorted.png)

## detska_encyklopedie_310

originál: [Dětská encyklopedie](https://www.digitalniknihovna.cz/mzk/view/uuid:82ba69f0-3b8a-11e7-8e0f-005056827e52?page=uuid:bc5b5ed0-5cff-11e7-b92d-005056827e51), kudos: Vladimír Fuka

```['#8B4D36', '#60707C', '#A97F4C', '#93948C', '#BDAC60', '#8B884F', '#34322E', '#D7CDC0']```

![detska_encyklopedie_310](palety/detska_encyklopedie_310.png)

```['#34322E', '#8B4D36', '#60707C', '#8B884F', '#A97F4C', '#93948C', '#BDAC60', '#D7CDC0']```

![detska_encyklopedie_310_sorted](palety/detska_encyklopedie_310_sorted.png)

## rozum_do_kapsy

originál: [Rozum do kapsy](https://www.digitalniknihovna.cz/mzk/view/uuid:d7cb9140-8bc6-11eb-aeb8-005056827e52?page=uuid:2518993a-c9c3-4829-8df9-68391bd3b2bc), kudos: Pavel Rajský

```['#D83A03', '#3A640F', '#0F240A', '#8B2704', '#F9C40A', '#010101', '#FEE7AC']```

![rozum_do_kapsy](palety/rozum_do_kapsy.png)

```['#010101', '#0F240A', '#8B2704', '#3A640F', '#D83A03', '#F9C40A', '#FEE7AC']```

![rozum_do_kapsy_sorted](palety/rozum_do_kapsy_sorted.png)

## rozum_do_kapsy_98

originál: [Rozum do kapsy](https://www.digitalniknihovna.cz/mzk/view/uuid:d7cb9140-8bc6-11eb-aeb8-005056827e52?page=uuid:e135fcd0-ce52-427d-9c54-a2f5dc2b55a4), kudos: Pavel Rajský

```['#242D60', '#AB7629', '#4A682B', '#B51310', '#B86862', '#7F422B', '#D0902B', '#565147', '#386693', '#B1ADA9', '#0F0F0D', '#D1C0A4']```

![rozum_do_kapsy_98](palety/rozum_do_kapsy_98.png)

```['#0F0F0D', '#242D60', '#B51310', '#565147', '#7F422B', '#4A682B', '#386693', '#AB7629', '#B86862', '#D0902B', '#B1ADA9', '#D1C0A4']```

![rozum_do_kapsy_98_sorted](palety/rozum_do_kapsy_98_sorted.png)

## nas_les

originál: [Náš les](https://www.digitalniknihovna.cz/mzk/view/uuid:7a9ad190-c43a-11e2-b6da-005056827e52?page=uuid:166ceed0-342c-11e3-bd38-5ef3fc9ae867), kudos: Antonín Pospíšil

```['#7C4F2E', '#406A55', '#B2C5A4', '#EECE54', '#14150F', '#FFFBDB']```

![nas_les](palety/nas_les.png)

```['#14150F', '#7C4F2E', '#406A55', '#B2C5A4', '#EECE54', '#FFFBDB']```

![nas_les_sorted](palety/nas_les_sorted.png)

## nas_les_plody

originál: [Náš les](https://www.digitalniknihovna.cz/mzk/view/uuid:7a9ad190-c43a-11e2-b6da-005056827e52?page=uuid:250aff90-342c-11e3-bd38-5ef3fc9ae867), kudos: Antonín Pospíšil

```['#C94A34', '#CF865E', '#AEBC32', '#588438', '#3B5657', '#384040', '#171515', '#F5EDE0']```

![nas_les_plody](palety/nas_les_plody.png)

```['#171515', '#384040', '#3B5657', '#C94A34', '#588438', '#CF865E', '#AEBC32', '#F5EDE0']```

![nas_les_plody_sorted](palety/nas_les_plody_sorted.png)

## nas_les_kvety

originál: [Náš les](https://www.digitalniknihovna.cz/mzk/view/uuid:7a9ad190-c43a-11e2-b6da-005056827e52?page=uuid:26dfe6a0-342c-11e3-bd38-5ef3fc9ae867), kudos: Antonín Pospíšil

```['#C66080', '#DFBD6E', '#C8414D', '#92A441', '#5C6A4A', '#95AE8F', '#9A7583', '#181111', '#F2E9DE']```

![nas_les_kvety](palety/nas_les_kvety.png)

```['#181111', '#5C6A4A', '#C8414D', '#9A7583', '#C66080', '#92A441', '#95AE8F', '#DFBD6E', '#F2E9DE']```

![nas_les_kvety_sorted](palety/nas_les_kvety_sorted.png)

## nas_les_ptaci

originál: [Náš les](https://www.digitalniknihovna.cz/mzk/view/uuid:7a9ad190-c43a-11e2-b6da-005056827e52?page=uuid:2cbb88e0-342c-11e3-bd38-5ef3fc9ae867), kudos: Antonín Pospíšil

```['#6B8EAA', '#33444C', '#D55F50', '#9CA545', '#ECD410', '#885929', '#D29257', '#B09F67', '#121212', '#ECE2D5']```

![nas_les_ptaci](palety/nas_les_ptaci.png)

```['#121212', '#33444C', '#885929', '#D55F50', '#6B8EAA', '#9CA545', '#B09F67', '#D29257', '#ECD410', '#ECE2D5']```

![nas_les_ptaci_sorted](palety/nas_les_ptaci_sorted.png)

## narodni_soutez_velkych_dechovych_orchestru

originál: [Jan Rajlich: Užitá grafika 1965-1985](https://www.digitalniknihovna.cz/mzk/view/uuid:871d3060-4724-11e5-8851-005056827e51?page=uuid:4b2cab70-d712-11e5-9c26-5ef3fc9bb22f), kudos: Jan Rajlich

```['#810112', '#B8A218', '#021D5C', '#6F8DAC', '#010242', '#29544B', '#82998A', '#C5C88E', '#010116', '#CFD6D3']```

![narodni_soutez_velkych_dechovych_orchestru](palety/narodni_soutez_velkych_dechovych_orchestru.png)

```['#010116', '#010242', '#021D5C', '#810112', '#29544B', '#6F8DAC', '#82998A', '#B8A218', '#C5C88E', '#CFD6D3']```

![narodni_soutez_velkych_dechovych_orchestru_sorted](palety/narodni_soutez_velkych_dechovych_orchestru_sorted.png)

## mesto_prace_a_pokroku_184

originál: [Brno město práce a pokroku](https://www.digitalniknihovna.cz/mzk/view/uuid:a4d267a0-78f5-11e3-9be6-005056827e52?page=uuid:819fb410-2005-11e4-8c14-5ef3fc9bb22f), kudos: Oldřich Staněk

```['#672A23', '#547078', '#83503F', '#53573A', '#B0ABA4', '#1D1212', '#D0C8BC']```

![mesto_prace_a_pokroku_184](palety/mesto_prace_a_pokroku_184.png)

```['#1D1212', '#672A23', '#53573A', '#83503F', '#547078', '#B0ABA4', '#D0C8BC']```

![mesto_prace_a_pokroku_184_sorted](palety/mesto_prace_a_pokroku_184_sorted.png)

## josef_lada_detem_35

originál: [Josef Lada dětem](https://www.digitalniknihovna.cz/mzk/view/uuid:aca48920-54a5-11e6-ab2f-005056827e52?page=uuid:ac3f1a20-76df-11e6-8340-5ef3fc9ae867), kudos: Josef Lada

```['#677D7D', '#8E4C3A', '#D5B96C', '#6B7B55', '#A0B2A1', '#9BA86A', '#D0A581', '#2E2C26', '#D8DFD5']```

![josef_lada_detem_35](palety/josef_lada_detem_35.png)

```['#2E2C26', '#8E4C3A', '#6B7B55', '#677D7D', '#9BA86A', '#A0B2A1', '#D0A581', '#D5B96C', '#D8DFD5']```

![josef_lada_detem_35_sorted](palety/josef_lada_detem_35_sorted.png)

## lada_leto

originál: [Josef Lada dětem](https://www.digitalniknihovna.cz/mzk/view/uuid:aca48920-54a5-11e6-ab2f-005056827e52?page=uuid:c954eef0-76df-11e6-8340-5ef3fc9ae867), kudos: Josef Lada

```['#98B5A1', '#71351E', '#CF5230', '#CB7530', '#CDBB5E', '#C0C162', '#AD7B3B', '#738F43', '#372C23', '#DDDBB4']```

![lada_leto](palety/lada_leto.png)

```['#372C23', '#71351E', '#CF5230', '#738F43', '#AD7B3B', '#CB7530', '#98B5A1', '#CDBB5E', '#C0C162', '#DDDBB4']```

![lada_leto_sorted](palety/lada_leto_sorted.png)

## pejsek_a_kocicka

originál: [Povídání o pejskovi a kočičce](https://www.digitalniknihovna.cz/mzk/view/uuid:be9df790-3019-11e9-b81e-005056827e52?page=uuid:fa987a00-5124-11e9-abdc-5ef3fc9bb22f), kudos: Josef Čapek

```['#D8462F', '#E49A45', '#92B8AE', '#A9C6BA', '#232323', '#E6E1CF']```

![pejsek_a_kocicka](palety/pejsek_a_kocicka.png)

```['#232323', '#D8462F', '#E49A45', '#92B8AE', '#A9C6BA', '#E6E1CF']```

![pejsek_a_kocicka_sorted](palety/pejsek_a_kocicka_sorted.png)

## pet_olympijskych_kruhu_6

originál: [Pět olympijských kruhů](https://www.digitalniknihovna.cz/mzk/view/uuid:fd622800-21c1-11e3-a5bb-005056827e52?page=uuid:6c632270-35f6-11e3-b62e-005056825209), kudos: Jan Schmid

```['#658B88', '#363130', '#B44350', '#FAE204', '#86A82A', '#FCF7E9', '#353130', '#FEFFFA']```

![pet_olympijskych_kruhu_6](palety/pet_olympijskych_kruhu_6.png)

```['#353130', '#363130', '#B44350', '#658B88', '#86A82A', '#FAE204', '#FCF7E9', '#FEFFFA']```

![pet_olympijskych_kruhu_6_sorted](palety/pet_olympijskych_kruhu_6_sorted.png)

## pet_olympijskych_kruhu_227

originál: [Pět olympijských kruhů](https://www.digitalniknihovna.cz/mzk/view/uuid:fd622800-21c1-11e3-a5bb-005056827e52?page=uuid:89091e70-35f6-11e3-b62e-005056825209), kudos: Jan Schmid

```['#EB78BB', '#548EC1', '#FEF325', '#3C3833', '#333430', '#FFFFFB']```

![pet_olympijskych_kruhu_227](palety/pet_olympijskych_kruhu_227.png)

```['#333430', '#3C3833', '#548EC1', '#EB78BB', '#FEF325', '#FFFFFB']```

![pet_olympijskych_kruhu_227_sorted](palety/pet_olympijskych_kruhu_227_sorted.png)

## pet_olympijskych_kruhu_318

originál: [Pět olympijských kruhů](https://www.digitalniknihovna.cz/mzk/view/uuid:fd622800-21c1-11e3-a5bb-005056827e52?page=uuid:9585fce0-35f6-11e3-b62e-005056825209), kudos: Jan Schmid

```['#65A8CD', '#D66847', '#DC7C49', '#E06AA7', '#649515', '#42403D', '#FFFFF7']```

![pet_olympijskych_kruhu_318](palety/pet_olympijskych_kruhu_318.png)

```['#42403D', '#649515', '#D66847', '#DC7C49', '#E06AA7', '#65A8CD', '#FFFFF7']```

![pet_olympijskych_kruhu_318_sorted](palety/pet_olympijskych_kruhu_318_sorted.png)

## uz_vim_proc_knihy

originál: [Už vím proč](https://www.digitalniknihovna.cz/mzk/view/uuid:c1777710-793f-11e4-8ce5-005056827e52?page=uuid:0be61030-b3ca-11e4-92dd-001018b5eb5c), kudos: Vojtěch Kubašta

```['#824a42', '#608793', '#beb47d', '#828f9b', '#98807f', '#a0a465', '#405045', '#93918a', '#83563f', '#42403D', '#DCDDD6']```

![uz_vim_proc_knihy](palety/uz_vim_proc_knihy.png)

```['#42403D', '#405045', '#824a42', '#83563f', '#608793', '#98807f', '#828f9b', '#93918a', '#a0a465', '#beb47d', '#DCDDD6']```

![uz_vim_proc_knihy_sorted](palety/uz_vim_proc_knihy_sorted.png)

## zelezny_mita_2

originál: [Železný Míťa](https://www.digitalniknihovna.cz/mzk/view/uuid:c8068180-cb3b-11ea-b7a2-005056827e51?page=uuid:050a9326-a335-4af0-b742-d828a4912db3), kudos: Jindřich Hegr

```['#B95D42', '#E1AD9C', '#0B0505', '#FEFDDE']```

![zelezny_mita_2](palety/zelezny_mita_2.png)

```['#0B0505', '#B95D42', '#E1AD9C', '#FEFDDE']```

![zelezny_mita_2_sorted](palety/zelezny_mita_2_sorted.png)

## jancuv_plan

originál: [Jančův plán Velkého Brna](https://www.digitalniknihovna.cz/mzk/view/uuid:ba4934d1-0a1e-4a01-a89d-c948477ca833?page=uuid:d22baf06-7fb6-4488-bc6f-995b644fd085)

```['#b97e67', '#596C74', '#979d85', '#c1b07e', '#ab9b8e', '#403E3B', '#cdbfa6']```

![jancuv_plan](palety/jancuv_plan.png)

```['#403E3B', '#596C74', '#b97e67', '#979d85', '#ab9b8e', '#c1b07e', '#cdbfa6']```

![jancuv_plan_sorted](palety/jancuv_plan_sorted.png)

## vitej_zpet_karle

originál: [ERA 21](https://www.digitalniknihovna.cz/mzk/view/uuid:f466f0f0-871b-11e2-b6e7-001018b5eb5c?page=uuid:abf360e1-edb0-b433-d50c-95d079751f3a), kudos: Vladimir 518

```['#C92546', '#D7A0AC', '#96ADB2', '#A3BCBE', '#131410', '#E5E5E5']```

![vitej_zpet_karle](palety/vitej_zpet_karle.png)

```['#131410', '#C92546', '#96ADB2', '#D7A0AC', '#A3BCBE', '#E5E5E5']```

![vitej_zpet_karle_sorted](palety/vitej_zpet_karle_sorted.png)

## devet_rychlych_muzu

originál: [Devět rychlých mužů](https://www.digitalniknihovna.cz/mzk/view/uuid:9893c1f0-796b-11e5-99af-005056827e52?page=uuid:a1a3b2c0-b488-11e5-b770-5ef3fc9ae867)

```['#B24E36', '#54677F', '#CCAD51', '#191518', '#C2B4A9']```

![devet_rychlych_muzu](palety/devet_rychlych_muzu.png)

```['#191518', '#54677F', '#B24E36', '#CCAD51', '#C2B4A9']```

![devet_rychlych_muzu_sorted](palety/devet_rychlych_muzu_sorted.png)

## f1_benetton95

originál: [Michael Schumacher](https://www.digitalniknihovna.cz/mzk/view/uuid:ea9bfd70-122c-11e4-8e0d-005056827e51?page=uuid:ea0f96b0-21a8-11e4-90aa-005056825209)

```['#394050', '#537998', '#BBA343', '#A3742F', '#395431', '#843323']```

![f1_benetton95](palety/f1_benetton95.png)

```['#394050', '#395431', '#843323', '#537998', '#A3742F', '#BBA343']```

![f1_benetton95_sorted](palety/f1_benetton95_sorted.png)

## f1_williams94

originál: [Ayrton Senna](https://www.digitalniknihovna.cz/mzk/view/uuid:98d48a10-1737-11ee-8fa0-005056827e52?page=uuid:33f826ae-fb67-41f2-acbf-10c7054418f7)

```['#4D5A86', '#C44C4E', '#C2A177']```

![f1_williams94](palety/f1_williams94.png)

```['#4D5A86', '#C44C4E', '#C2A177']```

![f1_williams94_sorted](palety/f1_williams94_sorted.png)

## f1_senna

originál: [Ayrton Senna](https://www.digitalniknihovna.cz/mzk/view/uuid:98d48a10-1737-11ee-8fa0-005056827e52?page=uuid:1d9c8892-1120-499e-ac25-3e071b076ce5)

```['#E05F54', '#71996A', '#FAC640']```

![f1_senna](palety/f1_senna.png)

```['#E05F54', '#71996A', '#FAC640']```

![f1_senna_sorted](palety/f1_senna_sorted.png)