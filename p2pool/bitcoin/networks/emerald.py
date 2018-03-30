import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 12127
ADDRESS_VERSION = 34
RPC_PORT = 12128
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'emeraldaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 0.1*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 20
SYMBOL = 'EMD'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'emerald') 
		if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/emerald/') 
		if platform.system() == 'Darwin' else os.path.expanduser('~/.emerald'), 'emerald.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/emd/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/emd/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/emd/tx.dws?'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8
