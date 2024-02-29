from threading import Thread
import time

def car(velocity, driver):
    path = 0
    while path <= 100:
        path+=velocity
        time.sleep(0.5)
        print('Piloto: {} km: {}'.format(driver, path))

t_car1 = Thread(target=car, args=[1, 'Anna'])
t_car2 = Thread(target=car, args=[2, 'Gabriel'])

t_car1.start()
t_car2.start()