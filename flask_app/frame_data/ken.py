normals = {
        'lp': ['4', '4-6', '7', ['4', '-1'], '300'],
        'mp': ['5', '5-8', '14', ['4', '-2'], '600'],
        'hp': ['10', '10-14', '17', ['3', '-2'], '800'],
        'lk': ['5', '5-6', '12', ['0', '-2'], '300'],
        'mk': ['8', '8-10', '20', ['3', '-5'], '600'],
        'hk': ['12', '12-13', '23', ['1', '-5'], '800'],
        'clp': ['4', '4-5', '9', ['5', '-1'], '300'],
        'cmp': ['6', '6-8', '14', ['3', '0'], '700'],
        'chp': ['8', '8-11', '24', ['3', '-10'], '800'],
        'clk': ['5', '5-7', '10', ['1', '-3'], '200'],
        'cmk': ['7', '7-9', '19', ['-2', '-6'], '500'],
        'chk': ['8', '8-10', '24', ['D', '-10'], '900'],
        'jlp': ['5', '5-11', '3 frames after landing', ['', ''], '300'],
        'jmp': ['6', '6-9', '3 frames after landing', ['', ''], '700'],
        'jhp': ['9', '9-14', '3 frames after landing', ['', ''], '800'],
        'jlk': ['6', '6-11', '3 frames after landing', ['', ''], '300'],
        'jmk': ['7', '7-12', '3 frames after landing', ['', ''], '500'],
        'jhk': ['10', '10-16', '3 frames after landing', ['', ''], '800'],
        'jhk (neutral jump)': ['6', '6-9', '3 frames after landing', ['', ''], '900']
    }

uniques = {
    'quick dash': ['', '', '45 total frames', ['', ''], '0'],
    'emergency stop': ['', '', '16 total frames', ['', ''], '0'],
    'thunder kick': ['18', '18-20', '20', ['3', '-3'], '1000'],
    'forward step kick (during quick dash)': ['10', '10-13', '20', ['3', '-4'], '800'],
    'chin buster': ['11', '11-13', '27', ['D', '-14'], '400'],
    'triple flash kicks (2)': ['11', '11-12', '27', ['D', '-12'], '400'],
    'triple flash kicks (3)': ['13', '13-15', '28', ['D', '-11'], '700']
}

specials = {
    'light hadoken': ['16', '', '49 total frames', ['-1', '-7'], '600'],
    'medium hadoken': ['14', '', '49 total frames', ['-3', '-9'], '600'],
    'heavy hadoken': ['12', '', '49 total frames', ['-5', '-11'], '600'],
    'od hadoken': ['12', '', '40 total frames', ['-2', '2'], '800'],
    'light shoryuken': ['5', '5-14', '21+12 frames after landing', ['D', '-23'], '1100'],
    'medium shoryuken': ['6', '6-15', '28+12 frames after landing', ['D', '-28'], '1300'],
    'heavy shoryuken': ['7', '7-16', '35+15 frames after landing', ['D', '-36'], '1400'],
    'od shoryuken': ['6', '6-39', '35+15 frames after landing', ['D', '-40'], '1600'],
    'shoryuken (during quick dash)': ['9', '9-18', '33+15 frames after landing', ['D', '-35'], '1700'], 
    'light tatsumaki senpu-kyaku': ['4', '4-14', '32', ['D', '-14'], '700'],
    'medium tatsumaki senpu-kyaku': ['14', '14-30', '31', ['D', '-12'], '900'],
    'heavy tatsumaki senpu-kyaku': ['16', '16-47', '31', ['D', '-12'], '1000'],
    'od tatsumaki senpu-kyaku': ['9', '9-56', '22+12 frames after landing', ['D', '-61'], '1500'],
    'tatsumaki senpu-kyaku (during quick dash)': ['13', '13-58', '20', ['3', '-9'], '1200'],
    'aerial tatsumaki senpu-kyaku': ['11', '11-27', '14 frames after landing', ['D', ''], '900'],
    'od aerial tatsumaki senpu-kyaku': ['11', '11-28', '14 frames after landing', ['D', ''], '900'],
    'light dragonlash kick': ['18', '18-23', '21', ['2', '-4'], '1000'],
    'medium dragonlash kick': ['23', '23-27', '25', ['3', '-8'], '1100'],
    'heavy dragonlash kick': ['28', '28-32', '21', ['3', '-1'], '1200'],
    'od dragonlash kick': ['9', '9-24', '24', ['1', '-9'], '1200'],
    'od dragonlash kick (during quick dash)': ['9', '9-23', '24', ['2', '-8'], '1200'],
    'light jinrai kick': ['12', '12-14', '28', ['1', '-11'], '500'],
    'medium jinrai kick': ['16', '16-18', '24', ['2', '-7'], '600'],
    'heavy jinrai kick': ['25', '25-27', '19', ['D', '-2'], '700'],
    'od jinrai kick': ['13', '13-15', '25', ['-4', '-7'], '600'],
    'kazekama shin kick (during jinrai kick)': ['6', '6-9', '19', ['3', '-5'], '500'],
    'od kazekama shin kick (during od jinrai kick)': ['6', '6-8', '20', ['3', '-5'], '500'],
    'kasai thrust kick (during od kazekama shin kick)': ['15', '15-17', '29', ['D', '-12'], '500'],
    'gorai axe kick (during jinrai kick)': ['18', '18-20', '20', ['3', '-3'], '1000'],
    'od gorai axe kick (during od jinrai kick)': ['17', '17-19', '24', ['-3', '-7'], '1000'],
    'kasai thrust kick (during od gorai axe kick)': ['11', '11-13', '29', ['D', '-12'], '500'],
    'senka snap kick (during jinrai kick)': ['10', '10-12', '25', ['D', '-3'], '800'],
    'od senka snap kick (during od jinrai kick)': ['10', '10-13', '20', ['D', '-4'], '800'],
    'kasai thrust kick (during od senka snap kick)': ['15', '15-17', '37', ['D', '-20'], '500']
}

super_arts = {
    'dragonlash flame': ['7', '7-9', '41', ['D', '-24'], '2000'],
    'shippu jinrai-kyaku': ['6', '6-60', '32', ['D', '-19'], '2700'],
    'shinryu reppa': ['7', '7-45', '45', ['D', '-30'], '4000'],
    'shinryu reppa (under 25% vit)': ['7', '7-45', '45', ['D', '-30'], '4500']
}

throws = {
    'knee strikes': ['5', '5-7', '23', ['D', ''], '1200'],
    'hell wheel': ['5', '5-7', '23', ['D', ''], '1200']
}

commons = {
    'forward dash': ['', '', '19 total frames', ['', ''], '0'],
    'backward dash': ['', '', '23 total frames', ['', ''], '0'],
    'drive impact': ['26', '26-27', '35', ['D', '-3'], '800'],
    'drive reversal': ['20', '20-22', '26', ['D', '-8'], '500'],
    'drive parry': ['1', '1-8', '29', ['', ''], '0'],
    'perfect parry (strike)': ['1', '', '1', ['', ''], '0'],
    'perfect parry (projectile)': ['1', '', '10', ['', ''], '0'],
    'parry drive rush': ['', '', '48 total frames', ['', ''], '0'],
    'cancel drive rush': ['', '', '48 total frames', ['', ''], '0']
}