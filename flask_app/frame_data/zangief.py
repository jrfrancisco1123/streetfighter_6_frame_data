normals = {
        'lp': ['7', '7-9', '9', ['4', '2'], '400'],
        'lp (rapid cancel version)': ['4', '4-6', '9', ['4', '2'], '400'],
        'mp': ['9', '9-12', '17', ['2', '-2'], '700'],
        'hp': ['16', '16-18', '22', ['3', '-3'], '1000'],
        'hp (charged)': ['32', '32-34', '22', ['D', '3'], '1400'],
        'lk': ['7', '7-8', '17', ['2', '-4'], '400'],
        'mk': ['10', '10-13', '19', ['1', '-4'], '800'],
        'hk': ['13', '13-16', '21', ['3', '1'], '1000'],
        'clp': ['6', '6-7', '8', ['6', '1'], '300'],
        'clp (rapid cancel version)': ['3', '3-4', '8', ['6', '1'], '300'],
        'cmp': ['8', '8-10', '16', ['3', '-1'], '700'],
        'chp': ['12', '12-19', '35', ['D', '-19'], '1000'],
        'clk': ['4', '4-6', '12', ['0', '-3'], '250'],
        'clk (rapid cancel version)': ['3', '3-5', '12', ['0', '-3'], '250'],
        'cmk': ['9', '9-11', '18', ['2', '-2'], '700'],
        'chk': ['12', '12-14', '27', ['D', '-13'], '1000'],
        'jlp': ['5', '5-11', '3 frames after landing', ['', ''], '300'],
        'jmp': ['8', '8-12', '3 frames after landing', ['', ''], '700'],
        'jhp': ['9', '9-14', '3 frames after landing', ['', ''], '800'],
        'jlk': ['5', '5-14', '3 frames after landing', ['', ''], '300'],
        'jmk': ['8', '8-15', '3 frames after landing', ['', ''], '500'],
        'jhk': ['10', '10-16', '3 frames after landing', ['', ''], '800'],
        'jhk (charged)': ['32', '32-37', '20 frames after landing', ['', ''], '1500']
}

uniques = {
    'hell stab': ['7', '7-9', '21', ['-1', '-3'], '800'],
    'knee hammer': ['14', '14-20', '14', ['0', '-4'], '600'],
    'headbutt': ['14', '14-18', '15', ['6', '4'], '900'],
    'cyclone wheel kick': ['22', '22-28', '25', ['D', '-12'], '1300'],
    'smetana dropkick': ['16', '16-19', '40', ['D', '-18'], '1000'],
    'flying body press (airborne)': ['9', '9-17', '8 frames after landing', ['', ''], '800'],
    'flying headbutt (neutral jump)': ['8', '8-11', '3 frames after landing', ['', ''], '800'],
    'machine gun chops (2)': ['9', '9-12', '20', ['2', '-6'], '600'],
    'machine gun chops (3)': ['15', '15-17', '32', ['D', '-17'], '900'],
    'power stomps (1)': ['9', '9-11', '17', ['4', '-3'], '500'],
    'power stomps (2)': ['9', '9-11', '19', ['-3', '-4'], '500'],
    'power stomps (3)': ['10', '10-12', '24', ['-2', '-10'], '700']
}

specials = {
    'double lariat': ['15', '15-45', '27', ['D', '-12'], '1200'],
    'od double lariat': ['12', '12-36', '26', ['D', '-11'], '1500'],
    'light screw piledriver': ['5', '5-7', '54', ['D', ''], '2500'],
    'medium screw piledriver': ['5', '5-7', '54', ['D', ''], '2900'],
    'heavy screw piledriver': ['5', '5-7', '54', ['D', ''], '3300'],
    'od screw piledriver': ['5', '5-7', '54', ['D', ''], '3400'],
    'borscht dynamite': ['4', '4-6', '16 frames after landing', ['D', ''], '2900'],
    'od borscht dynamite': ['4', '4-6', '16 frames after landing', ['D', ''], '3000'],
    'russian suplex': ['10', '10-11', '50', ['D', ''], '2900'],
    'od russian suplex': ['10', '10-11', '50', ['D', ''], '3200'],
    'siberian express (close)': ['28', '28-29', '41', ['D', ''], '2700'],
    'od siberian express (close)': ['23', '23-24', '44', ['D', ''], '3000'],
    'siberian express (far)': ['55', '55-56', '40', ['D', ''], '2700'],
    'od siberian express (far)': ['54', '54-55', '40', ['D', ''], '3000'],
    'tundra storm': ['5', '5-55', '24', ['D', ''], '2400']
}

super_arts = {
    'aerial russian slam': ['11', '11-17', '60', ['D', ''], '3500'],
    'aerial russian slam (charged)': ['18', '18-122', '52', ['D', '-35'], '1100'],
    'cyclone lariat (immediately)': ['', '', '', ['D', ''], '3100'],
    'cyclone lariat (movement)': ['', '', '', ['D', ''], '3000'],
    'bolshoi storm buster': ['6+0', '6-7', '116', ['D', ''], '4800'],
    'bolshoi storm buster (under 25% vit)': ['6+0', '6-7', '116', ['D', ''], '5300']
}

throws = {
    'bodyslam': ['5', '5-7', '23', ['D', ''], '1200'],
    'capture suplex': ['5', '5-7', '23', ['D', ''], '1400'],
    'german suplex': ['5', '5-7', '23', ['D', ''], '1500'],
    'spinebuster': ['5', '5-7', '23', ['D', ''], '1200'],
    'russian drop': ['5', '5-7', '23', ['D', ''], '1500'],
    'brain buster': ['5', '5-7', '23', ['D', ''], '1500']
}

commons = {
    'forward dash': ['', '', '22 total frames', ['', ''], '0'],
    'backward dash': ['', '', '25 total frames', ['', ''], '0'],
    'drive impact': ['26', '26-27', '35', ['D', '-3'], '800'],
    'drive reversal': ['20', '20-22', '26', ['D', '-8'], '500'],
    'drive parry': ['1', '1-8', '29', ['', ''], '0'],
    'perfect parry (strike)': ['1', '', '1', ['', ''], '0'],
    'perfect parry (projectile)': ['1', '', '10', ['', ''], '0'],
    'parry drive rush': ['', '', '45 total frames', ['', ''], '0'],
    'cancel drive rush': ['', '', '46 total frames', ['', ''], '0']
}