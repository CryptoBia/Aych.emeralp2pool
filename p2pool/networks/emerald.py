from p2pool.bitcoin import networks

PARENT = networks.nets['emerald']
SHARE_PERIOD = 5
CHAIN_LENGTH = 24*60*60//10
REAL_CHAIN_LENGTH = 24*60*60//10
TARGET_LOOKBEHIND = 200
SPREAD = 12
IDENTIFIER = 'e40ef614eeebb396'.decode('hex')
PREFIX = '502f757a499bf613'.decode('hex')
P2P_PORT = 46858
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 12125
BOOTSTRAP_ADDRS = 'crypto.office-on-the.net siberia.mine.nu'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-emd'
VERSION_CHECK = lambda v: True
