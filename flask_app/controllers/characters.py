from flask_app import app
from flask import render_template, session, redirect

from flask_app.frame_data import aki, blanka, cammy, chunli, deejay, dhalsim, guile, ed, honda, jamie, jp, juri, ken, kimberly, lily, luke, manon, marisa, rashid, ryu, zangief

@app.route('/view/aki')
def view_aki():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('aki.html', normals=aki.normals, uniques=aki.uniques, specials=aki.specials, super_arts=aki.super_arts, throws=aki.throws, commons=aki.commons)

@app.route('/view/blanka')
def view_blanka():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('blanka.html', normals=blanka.normals, uniques=blanka.uniques, specials=blanka.specials, super_arts=blanka.super_arts, throws=blanka.throws, commons=blanka.commons)

@app.route('/view/cammy')
def view_cammy():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('cammy.html', normals=cammy.normals, uniques=cammy.uniques, specials=cammy.specials, super_arts=cammy.super_arts, throws=cammy.throws, commons=cammy.commons)

@app.route('/view/chunli')
def view_chunli():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('chunli.html', normals=chunli.normals, uniques=chunli.uniques, specials=chunli.specials, super_arts=chunli.super_arts, throws=chunli.throws, commons=chunli.commons)

@app.route('/view/deejay')
def view_jay():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('deejay.html', normals=deejay.normals, uniques=deejay.uniques, specials=deejay.specials, super_arts=deejay.super_arts, throws=deejay.throws, commons=deejay.commons)

@app.route('/view/dhalsim')
def view_dhalsim():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dhalsim.html', normals=dhalsim.normals, uniques=dhalsim.uniques, specials=dhalsim.specials, super_arts=dhalsim.super_arts, throws=dhalsim.throws, commons=dhalsim.commons)

@app.route('/view/ed')
def view_ed():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('ed.html', normals=ed.normals, uniques=ed.uniques, specials=ed.specials, super_arts=ed.super_arts, throws=ed.throws, commons=ed.commons)

@app.route('/view/guile')
def view_guile():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('guile.html', normals=guile.normals, uniques=guile.uniques, specials = guile.specials, super_arts=guile.super_arts, throws=guile.throws, commons=guile.commons)

@app.route('/view/honda')
def view_honda():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('honda.html', normals=honda.normals, uniques=honda.uniques, specials=honda.specials, super_arts=honda.super_arts, throws=honda.throws, commons=honda.commons)

@app.route('/view/jamie')
def view_jamie():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('jamie.html', normals=jamie.normals, uniques=jamie.uniques, specials=jamie.specials, super_arts=jamie.super_arts, throws=jamie.throws, commons=jamie.commons)

@app.route('/view/jp')
def view_jp():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('jp.html', normals=jp.normals, uniques=jp.uniques, specials=jp.specials, super_arts=jp.super_arts, throws=jp.throws, commons=jp.commons)

@app.route('/view/juri')
def view_juri():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('juri.html', normals=juri.normals, uniques=juri.uniques, specials=juri.specials, super_arts=juri.super_arts, throws=juri.throws, commons=juri.commons)

@app.route('/view/ken')
def view_ken():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('ken.html', normals=ken.normals, uniques=ken.uniques, specials=ken.specials, super_arts=ken.super_arts, throws=ken.throws, commons=ken.commons)

@app.route('/view/kimberly')
def view_kimberly():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('kimberly.html', normals=kimberly.normals, uniques=kimberly.uniques, specials=kimberly.specials, super_arts=kimberly.super_arts, throws=kimberly.throws, commons=kimberly.commons)

@app.route('/view/lily')
def view_lily():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('lily.html', normals=lily.normals, uniques=lily.uniques, specials=lily.specials, super_arts=lily.super_arts, throws=lily.throws, commons=lily.commons)

@app.route('/view/luke')
def view_luke():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('luke.html', normals=luke.normals, uniques=luke.uniques, specials=luke.specials, super_arts=luke.super_arts, throws=luke.throws, commons=luke.commons)

@app.route('/view/manon')
def view_manon():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('manon.html', normals = manon.normals, uniques=manon.uniques ,specials=manon.specials, super_arts=manon.super_arts, throws=manon.throws, commons=manon.commons)

@app.route('/view/marisa')
def view_marisa():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('marisa.html', normals=marisa.normals, uniques=marisa.uniques, specials=marisa.specials, super_arts=marisa.super_arts, throws=marisa.throws, commons=marisa.commons)

@app.route('/view/ryu')
def view_ryu():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('ryu.html', normals=ryu.normals, uniques=ryu.uniques, specials=ryu.specials, super_arts=ryu.super_arts, throws=ryu.throws, commons=ryu.commons)

@app.route('/view/rashid')
def view_rashid():
    return render_template('rashid.html', normals=rashid.normals, uniques=rashid.uniques, specials=rashid.specials, super_arts=rashid.super_arts, throws=rashid.throws, commons=rashid.commons)

@app.route('/view/zangief')
def view_zangief():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('zangief.html', normals = zangief.normals ,uniques=zangief.uniques ,specials=zangief.specials ,super_arts=zangief.super_arts ,throws=zangief.throws, commons=zangief.commons)