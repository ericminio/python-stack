from sqlalchemy import create_engine

def test_db_is_prepopulated(db):
    user  = db.engine.execute('select count(1) as count from foi_user').fetchone()
    
    assert user['count'] == 2