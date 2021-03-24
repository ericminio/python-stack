import json

def test_users_are_sorted(db, client):
    db.engine.execute("insert into foi_user (username) values ('tic')")
    db.engine.execute("insert into foi_user (username) values ('tac')")
    db.engine.execute("insert into foi_user (username) values ('toc')")
    rv = client.get('/users')
    users = json.loads(rv.data)
    entries = users['entries']
    
    assert len(entries) == 3
    assert entries[0]['username'] == 'tac'
    assert entries[1]['username'] == 'tic'
    assert entries[2]['username'] == 'toc'
