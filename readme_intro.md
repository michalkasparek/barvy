xxx barevných palet vytahaných z knižních ilustrací a obrazů.
 
 Rychlý import palet do kódu:
 
1. ```wget https://raw.githubusercontent.com/michalkasparek/barvy/refs/heads/master/barvy.json```

2. ```with open('barvy.json', 'r', encoding='utf-8') as palety:```  
$~~~~$```palety = json.loads(palety.read())```

3. ```palety["název_palety"]```

U naprosté většiny palet je předposlední barva v seznamu černá (či nejtmavší barva na stránce) a poslední bílá (či nejsvětlejší barva na stránce).

Vedle výchozí ručně poskládané palety se generuje ještě seznam ```název_palety_sorted``` poskládaný od nejtmavější (typicky černé) po nejsvětlejší (typicky bílou).

