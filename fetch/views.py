from flask import Blueprint, request, redirect
import datetime
import sqlite3 as sq3

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
    return {"ad_id": "1"}

@fetch.route('/ad/<ad_id>', methods=['POST'])
def get_content(ad_id):
    try:
        height = request.args['h']
        width = request.args['w']
        
        ad_type = 'slim' if width > height else 'tall'
        print(height, width)
        print(ad_type)
    except:
        ad_type = 'tall'
    code = open(f'designs/{ad_id}/{ad_type}.html', 'r').read()
    return {"code":code}