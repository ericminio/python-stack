import json

def test_users(db, client):
    db.engine.execute("insert into foi_user (username) values ('tic')")
    db.engine.execute("insert into foi_user (username) values ('tac')")
    db.engine.execute("insert into foi_user (username) values ('toc')")
    rv = client.get('/users')
    users = json.loads(rv.data)
    
    assert len(users['data']) == 3
