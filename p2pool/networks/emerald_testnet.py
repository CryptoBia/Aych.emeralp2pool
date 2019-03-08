from p2pool.bitcoin import networks

PARENT = networks.nets['emerald_testnet']
SHARE_PERIOD = 4
CHAIN_LENGTH = 24*60//3
REAL_CHAIN_LENGTH = 20*60//3
TARGET_LOOKBEHIND = 200
SPREAD = 12
IDENTIFIER = 'e40ef614eeebb396'.decode('hex')
PREFIX = '502f757a499bf613'.decode('hex')
P2P_PORT = 56858
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 22125
BOOTSTRAP_ADDRS = 'tseed1.emeraldcrypto.de'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-emd'
VERSION_CHECK = lambda v: True
