from CBAutoHelper import CheckNode, LDPlayer
import time
import threading
ld_path = r'E:\LDPlayer\LDPlayer3.0'
img_path = r'.\img\screenshot_0.png'
game_package = 'com.moonactive.coinmaster'


ld = LDPlayer()
ld.pathLD = ld_path
devices = ld.GetAllLDPlayerRunning()



def run_vip(device):
    ld = LDPlayer()
    ld.pathLD = ld_path
    print(device)
    i = device['index']
    print(i)
    ld.Info('index', i)
    ld.Connect()
    while True:
        # init clear data and start app
        ld.DeleteCache(game_package)
        ld.OpenApp(game_package)
        time.sleep(3)
        start_time = time.time()
        while time.time() - start_time < 30:
            img = ld.FindImg(img_path)
            # print(img)
            if img[0] == 450:
                time.sleep(3)
                break
        ld.StopApp(game_package)
        time.sleep(1)
        ld.DeleteCache(game_package)
        time.sleep(1)
        # (177, 147)


thread_count = len(devices)
print(f'count: {thread_count}')
def main(device):
    # device = devices[m]
    # for i in range(1, thread_count):
    run_vip(device,)

for device in devices:
    thread = threading.Thread(target=main, args=(device,)).start()
