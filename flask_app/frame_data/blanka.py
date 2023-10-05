normals = {
        'lp': ['5', '5-7', '10', ['3', '-3'], '300'],
        'mp': ['10', '10-12', '15', ['3', '-4'], '700'],
        'hp': ['10', '10-16', '22', ['3', '-3'], '800'],
        'lk': ['4', '4-7', '7', ['5', '-2'], '300'],
        'mk': ['8', '8-10', '17', ['4', '-2'], '600'],
        'hk': ['7', '7-15', '18', ['6', '-4'], '800'],
        'clp': ['6', '6-8', '8', ['4', '-2'], '300'],
        'cmp': ['9', '9-13', '16', ['-1', '-5'], '600'],
        'chp': ['15', '15-19', '20', ['0', '-5'], '800'],
        'clk': ['5', '5-6', '10', ['3', '-3'], '200'],
        'cmk': ['8', '8-10', '16', ['5', '-5'], '500'],
        'chk': ['11', '11-14', '23', ['D', '-12'], '900'],
        'jlp': ['4', '4-8', '3 frames after landing', ['', ''], '300'],
        'jmp': ['7', '7-13', '3 frames after landing', ['', ''], '700'],
        'jhp': ['9', '9', '3 frames after landing', ['', ''], '800'],
        'jlk': ['5', '5-10', '3 frames after landing', ['', ''], '300'],
        'jmk': ['7', '7-12', '3 frames after landing', ['', ''], '500'],
        'jhk': ['11', '11-16', '3 frames after landing', ['', ''], '800'],
        'jhk (neutral jump)': ['7', '7-9', '3 frames after landing', ['', ''], '800']
}

uniques = {
    'rock crusher': ['20', '20-22', '20', ['3', '-2'], '600'],
    'double knee bombs': ['9', '9-20', '18', ['6', '-2'], '600'],
    'wild edge': ['9', '9-14', '12', ['8', '2'], '600'],
    'wild nail': ['18', '18-21', '31', ['D', '-15'], '1100'],
    'amazon river run': ['14', '14-23', '22', ['D', '-18'], '100'],
    'coward crouch': ['', '', '98 total frames', ['', ''], '0'],
    'wild lift (during coward crouch)': ['8', '8-14', '31', ['D', '-21'], '600'],
    'raid jump (during coward crouch)': ['', '', '43+12 frames after landing', ['', ''], '0'],
    'surprise forward hop': ['', '', '27 total frames', ['', ''], '0'],
    'surprise back hop': ['', '', '32 total frames', ['', ''], '0']
}

specials = {
    'electric thunder': ['10', '10-21', '17', ['D', '-3'], '800'],
    'electric thunder (lightning beast)': ['10', '10-21', '17', ['D', '-3'], '900'],
    'od electric thunder': ['10', '10-18', '17', ['D', '4'], '100'],
    'od electric thunder (lightning beast)': ['10', '10-18', '17', ['D', '4'], '1100'],
    'light rolling attack': ['10', '10-20', '11', ['D', '-23'], '100'],
    'light rolling attack (lightning beast)': ['10', '10-20', '11', ['D', '-21'], '1100'],
    'medium rolling attack': ['12', '12-30', '11', ['D', '-23'], '1200'],
    'medium rolling attack (lightning beast)': ['12', '12-30', '11', ['D', '-21'], '1300'],
    'heavy rolling attack': ['22', '22-41', '26', ['D', '-15'], '1300'],
    'heavy rolling attack (lightning beast)': ['22', '22-41', '26', ['D', '-21'], '1400'],
    'od rolling attack': ['18', '18-39', '17', ['D', '-7'], '800'],
    'od rolling attack (lightning beast)': ['18', '18-39', '17', ['D', '-7'], '900'],
    'light vertical rolling attack': ['8', '8-27', '31+17 frames after landing', ['D', '-27'], '1200'],
    'light vertical rolling attack (lightning beast)': ['8', '8-27', '31+17 frames after landing', ['D', '-27'], '1300'],
    'medium vertical rolling attack': ['8', '8-27', '31+17 frames after landing', ['D', '-27'], '1300'],
    'medium vertical rolling attack (lightning beast)': ['8', '8-27', '31+17 frames after landing', ['D', '-27'], '1400'],
    'heavy vertical rolling attack': ['8', '8-27', '31+17 frames after landing', ['D', '-27'], '1400'],
    'heavy vertical rolling attack (lightning beast)': ['8', '8-27', '31+17 frames after landing', ['D', '-27'], '1500'],
    'od vertical rolling attack': ['7', '7-22', '31+17 frames after landing', ['D', '-40'], '1600'],
    'od vertical rolling attack (lightning beast)': ['7', '7-22', '31+17 frames after landing', ['D', '-40'], '1750'],
    'light backstep rolling attack': ['41', '41-until landing', '5 frames after landing', ['9', '3'], '1000'],
    'light backstep rolling attack (lightning beast)': ['41', '41-until landing', '5 frames after landing', ['9', '3'], '1100'],
    'medium backstep rolling attack': ['41', '41-until landing', '5 frames after landing', ['8', '2'], '1000'],
    'medium backstep rolling attack (lightning beast)': ['41', '41-until landing', '5 frames after landing', ['8', '2'], '1100'],
    'heavy backstep rolling attack': ['41', '41-until landing', '5 frames after landing', ['8', '4'], '1000'],
    'heavy backstep rolling attack (lightning beast)': ['41', '41-until landing', '5 frames after landing', ['8', '4'], '1100'],
    'od backstep rolling attack': ['8', '8-66', '4 frames after landing', ['10', '6'], '1000'],
    'od backstep rolling attack (lightning beast)': ['8', '8-66', '4 frames after landing', ['10', '6'], '1200'],
    'light aerial rolling attack': ['13', '13-until landing', '17 frames after landing', ['D', ''], '1000'],
    'light aerial rolling attack (lightning beast)': ['13', '13-until landing', '17 frames after landing', ['D', ''], '1100'],
    'medium aerial rolling attack': ['13', '13-until landing', '17 frames after landing', ['D', ''], '1000'],
    'medium aerial rolling attack (lightning beast)': ['13', '13-until landing', '17 frames after landing', ['D', ''], '1100'],
    'heavy aerial rolling attack': ['13', '13-until landing', '17 frames after landing', ['D', ''], '1000'],
    'heavy aerial rolling attack (lightning beast)': ['13', '13-until landing', '17 frames after landing', ['D', ''], '1100'],
    'od aerial rolling attack': ['13', '13-until landing', '10 frames after landing', ['D', ''], '1200'],
    'od aerial rolling attack (lightning beast)': ['13', '13-until landing', '10 frames after landing', ['D', ''], '1400'],
    'light wild hunt': ['34', '34-36', '57', ['D', ''], '1600'],
    'medium wild hunt': ['39', '39-41', '57', ['D', ''], '1700'],
    'heavy wild hunt': ['43', '43-45', '57', ['D', ''], '1800'],
    'od wild hunt': ['32', '32-34', '57', ['D', ''], '2000'],
    'blanka-chan bomb': ['', '', '50 total frames', ['', ''], '0'],
    'rolling cannon': ['3', '3-27', '9 frames of recovery upon landing', ['D', ''], '400']
}

super_arts = {
    'shout of earth': ['8', '8-16', '78 total frames', ['D', '-29'], '200'],
    'shout of earth (lightning beast)': ['8', '8-16', '78 total frames', ['D', '-29'], '2200'],
    'lightning beast': ['', '', '10 total frames', ['', ''], '0'],
    'ground shave cannonball': ['10', '10-12', '61', ['D', '-46'], '4000'],
    'ground shave cannonball (under 25% vit)': ['10', '10-12', '61', ['D', '-46'], '4500']
}

throws = {
    'wild fang': ['5', '5-7', '23', ['D', ''], '1200'],
    'jungle flip': ['5', '5-7', '23', ['D', ''], '1200'],
    'wild bites (airborne)': ['5', '5-7', '', ['D', ''], '1200']
}

commons = {
    'forward dash': ['', '', '19 total frames', ['', ''], '0'],
    'backward dash': ['', '', '23 total frames', ['', ''], '0'],
    'drive impact': ['26', '26-27', '35', ['D', '-3'], '800'],
    'drive reversal': ['24', '24-26', '26', ['D', '-8'], '500'],
    'drive parry': ['1', '1-8', '29', ['', ''], '0'],
    'perfect parry (strike)': ['1', '', '1', ['', ''], '0'],
    'perfect parry (projectile)': ['1', '', '10', ['', ''], '0'],
    'parry drive rush': ['', '', '55 total frames', ['', ''], '0'],
    'cancel drive rush': ['', '', '55 total frames', ['', ''], '0']
}