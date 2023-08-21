normals = {
        'lp': ['5', '5-7', '10', ['3', '-3']],
        'mp': ['10', '10-12', '15', ['3', '-4']],
        'hp': ['10', '10-16', '22', ['3', '-3']],
        'lk': ['4', '4-7', '7', ['5', '-2']],
        'mk': ['8', '8-10', '17', ['4', '-2']],
        'hk': ['7', '7-15', '18', ['6', '-4']],
        'clp': ['6', '6-8', '8', ['4', '-2']],
        'cmp': ['9', '9-13', '16', ['-1', '-5']],
        'chp': ['15', '15-19', '20', ['0', '-5']],
        'clk': ['5', '5-6', '10', ['3', '-3']],
        'cmk': ['8', '8-10', '16', ['5', '-5']],
        'chk': ['11', '11-14', '23', ['D', '-12']],
        'jlp': ['4', '4-8', '3 frames after landing', ['', '']],
        'jmp': ['7', '7-13', '3 frames after landing', ['', '']],
        'jhp': ['9', '9', '3 frames after landing', ['', '']],
        'jlk': ['5', '5-10', '3 frames after landing', ['', '']],
        'jmk': ['7', '7-12', '3 frames after landing', ['', '']],
        'jhk': ['11', '11-16', '3 frames after landing', ['', '']],
        'jhk (neutral jump)': ['7', '7-9', '3 frames after landing', ['', '']]
}

uniques = {
    'rock crusher': ['20', '20-22', '20', ['3', '-2']],
    'double knee bombs': ['9', '9-20', '18', ['6', '-2']],
    'wild edge': ['9', '9-14', '12', ['8', '2']],
    'wild nail': ['18', '18-21', '31', ['D', '-15']],
    'amazon river run': ['14', '14-23', '22', ['D', '-18']],
    'coward crouch': ['', '', '98 total frames', ['', '']],
    'wild lift (during coward crouch)': ['8', '8-14', '31', ['D', '-21']],
    'raid jump (during coward crouch)': ['', '', '43+12 frames after landing', ['', '']],
    'surprise forward hop': ['', '', '27 total frames', ['', '']],
    'surprise back hop': ['', '', '32 total frames', ['', '']]
}

specials = {
    'electric thunder': ['10', '10-21', '17', ['D', '-3']],
    'electric thunder (lightning beast)': ['10', '10-21', '17', ['D', '-3']],
    'od electric thunder': ['10', '10-18', '17', ['D', '4']],
    'od electric thunder (lightning beast)': ['10', '10-18', '17', ['D', '4']],
    'light rolling attack': ['10', '10-20', '11', ['D', '-23']],
    'light rolling attack (lightning beast)': ['10', '10-20', '11', ['D', '-21']],
    'medium rolling attack': ['12', '12-30', '11', ['D', '-23']],
    'medium rolling attack (lightning beast)': ['12', '12-30', '11', ['D', '-21']],
    'heavy rolling attack': ['22', '22-41', '26', ['D', '-15']],
    'heavy rolling attack (lightning beast)': ['22', '22-41', '26', ['D', '-21']],
    'od rolling attack': ['18', '18-39', '17', ['D', '-7']],
    'od rolling attack (lightning beast)': ['18', '18-39', '17', ['D', '-7']],
    'light vertical rolling attack': ['8', '8-27', '31+17 frames after landing', ['D', '-27']],
    'light vertical rolling attack (lightning beast)': ['8', '8-27', '31+17 frames after landing', ['D', '-27']],
    'medium vertical rolling attack': ['8', '8-27', '31+17 frames after landing', ['D', '-27']],
    'medium vertical rolling attack (lightning beast)': ['8', '8-27', '31+17 frames after landing', ['D', '-27']],
    'heavy vertical rolling attack': ['8', '8-27', '31+17 frames after landing', ['D', '-27']],
    'heavy vertical rolling attack (lightning beast)': ['8', '8-27', '31+17 frames after landing', ['D', '-27']],
    'od vertical rolling attack': ['7', '7-22', '31+17 frames after landing', ['D', '-40']],
    'od vertical rolling attack (lightning beast)': ['7', '7-22', '31+17 frames after landing', ['D', '-40']],
    'light backstep rolling attack': ['41', '41-until landing', '5 frames after landing', ['9', '3']],
    'light backstep rolling attack (lightning beast)': ['41', '41-until landing', '5 frames after landing', ['9', '3']],
    'medium backstep rolling attack': ['41', '41-until landing', '5 frames after landing', ['8', '2']],
    'medium backstep rolling attack (lightning beast)': ['41', '41-until landing', '5 frames after landing', ['8', '2']],
    'heavy backstep rolling attack': ['41', '41-until landing', '5 frames after landing', ['8', '4']],
    'heavy backstep rolling attack (lightning beast)': ['41', '41-until landing', '5 frames after landing', ['8', '4']],
    'od backstep rolling attack': ['8', '8-66', '4 frames after landing', ['10', '6']],
    'od backstep rolling attack (lightning beast)': ['8', '8-66', '4 frames after landing', ['10', '6']],
    'light aerial rolling attack': ['13', '13-until landing', '17 frames after landing', ['D', '']],
    'light aerial rolling attack (lightning beast)': ['13', '13-until landing', '17 frames after landing', ['D', '']],
    'medium aerial rolling attack': ['13', '13-until landing', '17 frames after landing', ['D', '']],
    'medium aerial rolling attack (lightning beast)': ['13', '13-until landing', '17 frames after landing', ['D', '']],
    'heavy aerial rolling attack': ['13', '13-until landing', '17 frames after landing', ['D', '']],
    'heavy aerial rolling attack (lightning beast)': ['13', '13-until landing', '17 frames after landing', ['D', '']],
    'od aerial rolling attack': ['13', '13-until landing', '10 frames after landing', ['D', '']],
    'od aerial rolling attack (lightning beast)': ['13', '13-until landing', '10 frames after landing', ['D', '']],
    'light wild hunt': ['34', '34-36', '57', ['D', '']],
    'medium wild hunt': ['39', '39-41', '57', ['D', '']],
    'heavy wild hunt': ['43', '43-45', '57', ['D', '']],
    'od wild hunt': ['32', '32-34', '57', ['D', '']],
    'blanka-chan bomb': ['', '', '50 total frames', ['', '']],
    'rolling cannon': ['3', '3-27', '9 frames of recovery upon landing', ['D', '']]
}

super_arts = {
    'shout of earth': ['8', '8-16', '78 total frames', ['D', '-29']],
    'shout of earth (lightning beast)': ['8', '8-16', '78 total frames', ['D', '-29']],
    'lightning beast': ['', '', '10 total frames', ['', '']],
    'ground shave cannonball': ['10', '10-12', '61', ['D', '-46']],
    'ground shave cannonball (under 25% vit)': ['10', '10-12', '61', ['D', '-46']]
}

throws = {
    'wild fang': ['5', '5-7', '23', ['D', '']],
    'jungle flip': ['5', '5-7', '23', ['D', '']],
    'wild bites (airborne)': ['5', '5-7', '', ['D', '']]
}

commons = {
    'forward dash': ['', '', '19 total frames', ['', '']],
    'backward dash': ['', '', '23 total frames', ['', '']],
    'drive impact': ['26', '26-27', '35', ['D', '-3']],
    'drive reversal': ['24', '24-26', '26', ['D', '-8']],
    'drive parry': ['1', '1-8', '29', ['', '']],
    'perfect parry (strike)': ['1', '', '1', ['', '']],
    'perfect parry (projectile)': ['1', '', '10', ['', '']],
    'parry drive rush': ['', '', '55 total frames', ['', '']],
    'cancel drive rush': ['', '', '55 total frames', ['', '']]
}