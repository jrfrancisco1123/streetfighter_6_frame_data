normals = {
        'lp': ['5', '5-6', '8', ['5', '-2'],'270'],
        'mp': ['6', '6-8', '18', ['3', '-2'],'540'],
        'hp': ['9', '9-11', '20', ['3', '-4'],'630'],
        'lk': ['5', '5-7', '11', ['1', '-3'],'270'],
        'mk': ['8', '8-10', '18', ['1', '-4'],'540'],
        'hk': ['12', '12-15', '17', ['7', '2'],'630'],
        'clp': ['4', '4-6', '7', ['4', '-2'],'270'],
        'cmp': ['6', '6-8', '13', ['7', '-1'],'450'],
        'chp': ['8', '8-13', '17', ['3', '-2'],'720'],
        'clk': ['5', '5-7', '7', ['2', '-2'],'180'],
        'cmk': ['7', '7-9', '16', ['5', '1'],'540'],
        'chk': ['8', '8-10', '24', ['D', '-10'],'810'],
        'jlp': ['4', '4-13', '3 frames after landing', ['', ''],'270'],
        'jmp': ['6', '6-9', '3 frames after landing', ['', ''],'450'],
        'jhp': ['8', '8-12', '3 frames after landing', ['', ''],'630'],
        'jlk': ['5', '5-14', '3 frames after landing', ['', ''],'270'],
        'jmk': ['7', '7-12', '3 frames after landing', ['', ''],'540'],
        'jhk': ['9', '9-14', '3 frames after landing', ['', ''],'630']
}

uniques = {
    'water slicer slide': ['11', '11-20', '16', ['-3', '-9'],'450'],
    'windmill kick': ['22', '22-23', '19', ['4', '-3'],'720'],
    'hisen kick': ['27', '27-29', '21', ['1', '-3'],'720'],
    'step up': ['', '', '3 frames after landing', ['-10', '-22'],'0'],
    'elbow drop': ['13', '13-25', '8 frames after landing', ['', ''],'540'],
    'bushin tiger fangs': ['10', '10-12', '26', ['D', '-12'],'360'],
    'bushin prism strikes (2)': ['6', '6-8', '18', ['1', '-6'],'360'],
    'bushin prism strikes (3)': ['12', '12-13', '25', ['D', '-10'],'440'],
    'bushin prism strikes (4)': ['26', '26-28', '24', ['D', '-12'],'520'],
    'bushin hellchain (3)': ['10', '10-11', '25', ['2', '-10'],'580'],
    'bushin hellchain (4)': ['15', '15-17', '24', ['D', '-12'],'720'],
    'bushin hellchain throw': ['15', '15-17', '23', ['D', '-12'],'720']
}

specials = {
    'light bushin senpukyaku': ['6', '6-36', '17 frames after landing', ['D', '-30'],'990'],
    'medium bushin senpukyaku': ['7', '7-37', '17 frames after landing', ['D', '-32'],'1080'],
    'heavy bushin senpukyaku': ['8', '8-38', '17 frames after landing', ['D', '-35'],'1170'],
    'od bushin senpukyaku': ['6', '6-35', '17 frames after landing', ['D', '-40'],'1350'],
    'aerial bushin senpukyaku': ['8', '8-37', '12 frames after landing', ['5', '1'],'900'],
    'od aerial bushin senpukyaku': ['8', '8-28', '12 frames after landing', ['5', '1'],'990'],
    'sprint': ['', '', '55 total frames', ['', ''],'0'],
    'od sprint': ['', '', '54 total frames', ['', ''],'0'],
    'emergency stop': ['', '', '14 total frames', ['', ''],'0'],
    'od emergency stop': ['', '', '13 total frames', ['', ''],'0'],
    'torso cleaver': ['21', '21-27', '16', ['D', '1'],'900'],
    'od torso cleaver': ['17', '17-23', '16', ['D', '3'],'1080'],
    'shadow slide': ['10', '10-21', '19', ['D', '-12'],'720'],
    'od shadow slide': ['8', '8-19', '19', ['D', '-10'],'900'],
    'neck hunter': ['19', '19-23', '19', ['D', '-3'],'900'],
    'od neck hunter': ['15', '15-19', '19', ['D', '-1'],'1080'],
    'arc step': ['8', '8-17', '26+4 frames after landing', ['3', '-6'],'450'],
    'od arc step': ['8', '8-17', '26+4 frames after landing', ['3', '-6'],'270'],
    'bushin izuna otoshi': ['13', '13-18', '40 frames after landing', ['D', ''],'1440'],
    'od bushin izuna otoshi': ['13', '13-18', '40 frames after landing', ['D', ''],'900'],
    'bushin hojin kick': ['13', '13-18', '20 frames after landing', ['D', '-8'],'630'],
    'od bushin hojin kick': ['13', '13-18', '20 frames after landing', ['D', '-8'],'630'],
    'light vagabond edge': ['10', '10-11', '22', ['3', '-6'],'810'],
    'medium vagabond edge': ['17', '17-43', '28', ['D', '-12'],'1080'],
    'heavy vagabond edge': ['24', '24-45', '28', ['D', '-12'],'540'],
    'od vagabond edge': ['17', '17-38', '28', ['D', '-12'],'540'],
    'hidden variable': ['', '', '43 total frames', ['', ''],'0'],
    'od hidden variable': ['', '', '3 frames after landing', ['', ''],'0'],
    'genius at play': ['', '', '44 total frames', ['', ''],'0'],
    'od genius at play': ['', '', '44 total frames', ['', ''],'0'],
    'light shuriken bomb': ['122', '122-131', '44 total frames', ['', ''],'450'], 
    'medium shuriken bomb': ['124', '124-133', '44 total frames', ['', ''],'450'], 
    'heavy shuriken bomb': ['128', '128-137', '44 total frames', ['', ''],'450'], 
    'light shuriken bomb spread': ['*', '*', '44 total frames', ['', ''],'450'], 
    'medium shuriken bomb spread': ['*', '*', '44 total frames', ['', ''],'450'], 
    'heavy shuriken bomb spread': ['*', '*', '44 total frames', ['', ''],'450'], 
    'nue twister': ['5', '5-7', '20 frames after landing', ['D', ''],'1440'], 
    'od nue twister': ['5', '5-7', '20 frames after landing', ['D', ''],'900']
}

super_arts = {
    'bushin beats': ['12', '12-36', '40', ['D', '-25'],'1800'],
    'bushin thunderous beats': ['12', '12-26', '40', ['D', '-25'],'200'],
    'bushin scramble': ['13', '13-20', '39 frames after landing', ['D', '-25'],'2600'],
    'soaring bushin scramble': ['13', '13-until landing', '39 frames after landing', ['D', ''],'2600'],
    'bushin ninjastar cypher': ['8', '8-13', '51', ['D', '-35'],'4000'],
    'bushin ninjastar cypher (under 25% vit)': ['8', '8-13', '51', ['D', '-35'],'4500']
}

throws = {
    'ripcord throw': ['5', '5-7', '23', ['D', ''],'1082'],
    'bell ringer': ['5', '5-7', '23', ['D', ''],'1082']
}

commons = {
    'forward dash': ['', '', '18 total frames', ['', ''],'0'],
    'backward dash': ['', '', '23 total frames', ['', ''],'0'],
    'drive impact': ['26', '26-27', '35', ['D', '-3'],'720'],
    'drive reversal': ['20', '20-22', '26', ['D', '-8'],'500'],
    'drive parry': ['1', '1-8', '29', ['', ''],'0'],
    'perfect parry (strike)': ['1', '', '1', ['', ''],'0'],
    'perfect parry (projectile)': ['1', '', '10', ['', ''],'0'],
    'parry drive rush': ['', '', '45 total frames', ['', ''],'0'],
    'cancel drive rush': ['', '', '46 total frames', ['', ''],'0']
}