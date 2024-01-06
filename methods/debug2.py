import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of')
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
def stopligth(st):
    for key in st.keys():
        if st[key] == 'green':
            st[key] = 'yellow'
        elif st[key] == 'yellow':
            st[key]= 'red'
        elif st[key] == 'red':
            st[key] = 'green'
            
        assert 'red' in st.values(), 'neither signal is red' + str(st)
    
    
stopligth(mission_16th)