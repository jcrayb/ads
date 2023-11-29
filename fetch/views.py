from flask import Blueprint, request, redirect, send_file
import datetime
import sqlite3 as sq3

import random
import os


fetch = Blueprint('fetch', __name__, url_prefix='/fetch')

con = sq3.connect('./db/ad.db', check_same_thread=False)
cur = con.cursor()

@fetch.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

@fetch.route('/redirect/<ad_id>', methods=['GET'])
def redir(ad_id):
    try:
        site = request.args['website']
    except KeyError:
        return {"ERR": "Origin website or ad ID are missing"}
    
    redirect_url = cur.execute(f'''
        SELECT url FROM ads
        WHERE id = "{ad_id}"
    ''').fetchone()[0]
    
    if not redirect_url:
        return {"ERR":"No ad corresponds to this ad ID"}

    cur.execute(f'''
        INSERT INTO visits
        VALUES ("{ad_id}", "{datetime.datetime.now()}", "{site}")
    ''')

    con.commit()
    print(redirect_url)
    return redirect(redirect_url)

@fetch.route('/generate', methods=['GET'])
def get_ad():
    all_ads = cur.execute("SELECT id FROM ads;").fetchall()
    print(all_ads)
    
    index = random.randint(0, len(all_ads)-1)
    
    return {"ad_id": all_ads[index][0]}
   # return {"ad_id": "6d2818f3"}

@fetch.route('/images/<ad_id>', methods=['GET'])
def ad_images(ad_id):
    images = os.listdir(f'images/{ad_id}')
    index = random.randint(0, len(images)-1)
    return send_file(os.path.join(f'images/{ad_id}', images[index]), mimetype='image/png')

@fetch.route('/ad/<ad_id>', methods=['POST'])
def get_content(ad_id):
    ads = os.listdir(f'designs/{ad_id}')
    print(ads)
    if len(ads) == 1:
        with open(f'designs/{ad_id}/{ads[0]}', 'r') as f:
            code = f.read()
        return {"code": code}

    try:
        height = int(request.args['h'])
        width = int(request.args['w'])

        ad_type = 'slim' if width > height else 'tall'
        
        print(ad_type)
        print(height, width)
    except Exception as e:
        print(e)
        ad_type = 'tall'
    
    with open(f'designs/{ad_id}/{ad_type}.html', 'r') as f:
        code = f.read()
    return {"code":code}