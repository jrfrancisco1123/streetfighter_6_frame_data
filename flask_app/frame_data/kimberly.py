normals = {
        'lp': ['5', '5-6', '8', ['5', '-2']],
        'mp': ['6', '6-8', '18', ['3', '-2']],
        'hp': ['9', '9-11', '20', ['3', '-4']],
        'lk': ['5', '5-7', '11', ['1', '-3']],
        'mk': ['8', '8-10', '18', ['1', '-4']],
        'hk': ['12', '12-15', '17', ['7', '2']],
        'clp': ['4', '4-6', '7', ['4', '-2']],
        'cmp': ['6', '6-8', '13', ['7', '-1']],
        'chp': ['8', '8-13', '17', ['3', '-2']],
        'clk': ['5', '5-7', '7', ['2', '-2']],
        'cmk': ['7', '7-9', '16', ['5', '1']],
        'chk': ['8', '8-10', '24', ['D', '-10']],
        'jlp': ['4', '4-13', '3 frames after landing', ['', '']],
        'jmp': ['6', '6-9', '3 frames after landing', ['', '']],
        'jhp': ['8', '8-12', '3 frames after landing', ['', '']],
        'jlk': ['5', '5-14', '3 frames after landing', ['', '']],
        'jmk': ['7', '7-12', '3 frames after landing', ['', '']],
        'jhk': ['9', '9-14', '3 frames after landing', ['', '']]
}

uniques = {
    'water slicer slide': ['11', '11-20', '16', ['-3', '-9']],
    'windmill kick': ['22', '22-23', '19', ['4', '-3']],
    'hisen kick': ['27', '27-29', '21', ['1', '-3']],
    'step up': ['', '', '3 frames after landing', ['-10', '-22']],
    'elbow drop': ['13', '13-25', '8 frames after landing', ['', '']],
    'bushin tiger fangs': ['10', '10-12', '26', ['D', '-12']],
    'bushin prism strikes (2)': ['6', '6-8', '18', ['1', '-6']],
    'bushin prism strikes (3)': ['12', '12-13', '25', ['D', '-10']],
    'bushin prism strikes (4)': ['26', '26-28', '24', ['D', '-12']],
    'bushin hellchain (3)': ['10', '10-11', '25', ['2', '-10']],
    'bushin hellchain (4)': ['15', '15-17', '24', ['D', '-12']],
    'bushin hellchain throw': ['15', '15-17', '23', ['D', '-12']]
}

specials = {
    'light bushin senpukyaku': ['6', '6-36', '17 frames after landing', ['D', '-30']],
    'medium bushin senpukyaku': ['7', '7-37', '17 frames after landing', ['D', '-32']],
    'heavy bushin senpukyaku': ['8', '8-38', '17 frames after landing', ['D', '-35']],
    'od bushin senpukyaku': ['6', '6-35', '17 frames after landing', ['D', '-40']],
    'aerial bushin senpukyaku': ['8', '8-37', '12 frames after landing', ['5', '1']],
    'od aerial bushin senpukyaku': ['8', '8-28', '12 frames after landing', ['5', '1']],
    'sprint': ['', '', '55 total frames', ['', '']],
    'od sprint': ['', '', '54 total frames', ['', '']],
    'emergency stop': ['', '', '14 total frames', ['', '']],
    'od emergency stop': ['', '', '13 total frames', ['', '']],
    'torso cleaver': ['21', '21-27', '16', ['D', '1']],
    'od torso cleaver': ['17', '17-23', '16', ['D', '3']],
    'shadow slide': ['10', '10-21', '19', ['D', '-12']],
    'od shadow slide': ['8', '8-19', '19', ['D', '-10']],
    'neck hunter': ['19', '19-23', '19', ['D', '-3']],
    'od neck hunter': ['15', '15-19', '19', ['D', '-1']],
    'arc step': ['8', '8-17', '26+4 frames after landing', ['3', '-6']],
    'od arc step': ['8', '8-17', '26+4 frames after landing', ['3', '-6']],
    'bushin izuna otoshi': ['13', '13-18', '40 frames after landing', ['D', '']],
    'od bushin izuna otoshi': ['13', '13-18', '40 frames after landing', ['D', '']],
    'bushin hojin kick': ['13', '13-18', '20 frames after landing', ['D', '-8']],
    'od bushin hojin kick': ['13', '13-18', '20 frames after landing', ['D', '-8']],
    'light vagabond edge': ['10', '10-11', '22', ['3', '-6']],
    'medium vagabond edge': ['17', '17-43', '28', ['D', '-12']],
    'heavy vagabond edge': ['24', '24-45', '28', ['D', '-12']],
    'od vagabond edge': ['17', '17-38', '28', ['D', '-12']],
    'hidden variable': ['', '', '43 total frames', ['', '']],
    'od hidden variable': ['', '', '3 frames after landing', ['', '']],
    'genius at play': ['', '', '44 total frames', ['', '']],
    'od genius at play': ['', '', '44 total frames', ['', '']],
    'light shuriken bomb': ['122', '122-131', '44 total frames', ['', '']], 
    'medium shuriken bomb': ['124', '124-133', '44 total frames', ['', '']], 
    'heavy shuriken bomb': ['128', '128-137', '44 total frames', ['', '']], 
    'light shuriken bomb spread': ['*', '*', '44 total frames', ['', '']], 
    'medium shuriken bomb spread': ['*', '*', '44 total frames', ['', '']], 
    'heavy shuriken bomb spread': ['*', '*', '44 total frames', ['', '']], 
    'nue twister': ['5', '5-7', '20 frames after landing', ['D', '']], 
    'od nue twister': ['5', '5-7', '20 frames after landing', ['D', '']]
}

super_arts = {
    'bushin beats': ['12', '12-36', '40', ['D', '-25']],
    'bushin thunderous beats': ['12', '12-26', '40', ['D', '-25']],
    'bushin scramble': ['13', '13-20', '39 frames after landing', ['D', '-25']],
    'soaring bushin scramble': ['13', '13-until landing', '39 frames after landing', ['D', '']],
    'bushin ninjastar cypher': ['8', '8-13', '51', ['D', '-35']],
    'bushin ninjastar cypher (under 25% vit)': ['8', '8-13', '51', ['D', '-35']]
}

throws = {
    'ripcord throw': ['5', '5-7', '23', ['D', '']],
    'bell ringer': ['5', '5-7', '23', ['D', '']]
}

commons = {
    'forward dash': ['', '', '18 total frames', ['', '']],
    'backward dash': ['', '', '23 total frames', ['', '']],
    'drive impact': ['26', '26-27', '35', ['D', '-3']],
    'drive reversal': ['20', '20-22', '26', ['D', '-8']],
    'drive parry': ['1', '1-8', '29', ['', '']],
    'perfect parry (strike)': ['1', '', '1', ['', '']],
    'perfect parry (projectile)': ['1', '', '10', ['', '']],
    'parry drive rush': ['', '', '45 total frames', ['', '']],
    'cancel drive rush': ['', '', '46 total frames', ['', '']]
}