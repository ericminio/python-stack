def test_data(client):
    rv = client.get('/data')
    assert b'hello world' in rv.data
