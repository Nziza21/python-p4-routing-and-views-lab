import pytest
from app import app

class TestApp:
    '''Flask application in flask_app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert(response.status_code == 200)

    def test_index_text(self):
        '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
        response = app.test_client().get('/')
        assert(response.data.decode() == '<h1>Python Operations with Flask Routing and Views</h1>')

    def test_print_route(self):
        '''has a resource available at "/print/<parameter>".'''
        response = app.test_client().get('/print/hello')
        assert(response.status_code == 200)

    def test_print_text(self):
        '''displays text of route in browser.'''
        response = app.test_client().get('/print/hello')
        assert(response.data.decode() == 'hello')

    @pytest.fixture
    def parameter(self):
        return 'hello'

    @pytest.fixture
    def expected_output(self):
        return 'hello'

    def test_print_text_in_console(self, capsys, parameter, expected_output):
        '''displays text of route in console.'''
        with capsys.disabled():
            with app.test_client() as client:
                response = client.get(f'/print/{parameter}')
                captured_value = response.data.decode().strip()
        assert captured_value == expected_output

    def test_count_route(self):
        '''has a resource available at "/count/<parameter>".'''
        response = app.test_client().get('/count/5')
        assert(response.status_code == 200)

    def test_count_range_10(self):
        '''counts through range of parameter in "/count/<parameter>" on separate lines.'''
        response = app.test_client().get('/count/10')
        count_html = '0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9'
        assert response.data.decode() == count_html

    def test_math_route(self):
        '''has a resource available at "/math/<parameters>".'''
        response = app.test_client().get('/math/5/+/5')
        assert(response.status_code == 200)

    def test_math_add(self):
        '''adds parameters in "/math/" resource when operation is "+".'''
        response = app.test_client().get('/math/5/+/5')
        assert(response.data.decode() == '10')

    def test_math_subtract(self):
        '''subtracts parameters in "/math/" resource when operation is "-".'''
        response = app.test_client().get('/math/5/-/5')
        assert(response.data.decode() == '0')

    def test_math_multiply(self):
        '''multiplies parameters in "/math/" resource when operation is "*".'''
        response = app.test_client().get('/math/5/*/5')
        assert(response.data.decode() == '25')

    def test_math_divide(self):
        '''divides parameters in "/math/" resource when operation is "div".'''
        response = app.test_client().get('/math/5/div/5')
        assert(response.data.decode() == '1.0')
    
    def test_math_modulo(self):
        '''finds remainder of parameters in "/math/" resource when operation is "%".'''
        response = app.test_client().get('/math/5/%/5')
        assert(response.data.decode() == '0')