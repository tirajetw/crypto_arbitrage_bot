from binance.client import Client
from binance.enums import *
import time
import os
from datetime import datetime
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
import pprint
import math
from BinanceKeys import BinanceKey1
from line_notify import LineNotify

#Line
ACCESS_TOKEN = "LW5XR09lAOagmoYiazj0Se89GFR1TTLOgYOSLvJYEbx"
#ACCESS_TOKEN = "ZMBvfTnxGHmmMfbZDOZiqb0uEEQZCDUdq65dOljsqWi"

notify = LineNotify(ACCESS_TOKEN)

precision = 8
#price_str = '{:0.0{}f}'.format(price, precision)

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)

exch_rate_list = []
qtt_rate_list = []
tri_sym_list = []
fee = 0.001
start_amount = 0
amt_ratio = 1
global update_amt
update_amt = False
global start_amount_bnb
global start_amount_eth
start_amount_bnb = 0
start_amount_eth = 0

list_of_symbols2 = ['BNBBTC', 'ADABNB', 'ADABTC']
list_of_symbols3 = ['BNBBTC', 'ADXBNB', 'ADXBTC']
list_of_symbols4 = ['BNBBTC', 'AEBNB', 'AEBTC']
list_of_symbols5 = ['BNBBTC', 'AGIBNB', 'AGIBTC']
list_of_symbols6 = ['BNBBTC', 'AIONBNB', 'AIONBTC']
list_of_symbols7 = ['BNBBTC', 'AMBBNB', 'AMBBTC']
list_of_symbols8 = ['BNBBTC', 'APPCBNB', 'APPCBTC']
list_of_symbols9 = ['BNBBTC', 'ARDRBNB', 'ARDRBTC']
list_of_symbols10 = ['BNBBTC', 'BATBNB', 'BATBTC']
list_of_symbols11 = ['BNBBTC', 'BCCBNB', 'BCCBTC']
list_of_symbols12 = ['BNBBTC', 'BCPTBNB', 'BCPTBTC']
list_of_symbols13 = ['BNBBTC', 'BLZBNB', 'BLZBTC']
list_of_symbols14 = ['BNBBTC', 'BRDBNB', 'BRDBTC']
list_of_symbols15 = ['BNBBTC', 'BTSBNB', 'BTSBTC']
list_of_symbols16 = ['BNBBTC', 'CMTBNB', 'CMTBTC']
list_of_symbols17 = ['BNBBTC', 'CNDBNB', 'CNDBTC']
list_of_symbols18 = ['BNBBTC', 'CVCBNB', 'CVCBTC']
list_of_symbols19 = ['BNBBTC', 'DLTBNB', 'DLTBTC']
list_of_symbols20 = ['BNBBTC', 'ENJBNB', 'ENJBTC']
list_of_symbols21 = ['BNBBTC', 'EOSBNB', 'EOSBTC']
list_of_symbols22 = ['BNBBTC', 'ETCBNB', 'ETCBTC']
list_of_symbols23 = ['BNBBTC', 'GNTBNB', 'GNTBTC']
list_of_symbols24 = ['BNBBTC', 'GTOBNB', 'GTOBTC']
list_of_symbols25 = ['BNBBTC', 'ICXBNB', 'ICXBTC']
list_of_symbols26 = ['BNBBTC', 'IOTABNB', 'IOTABTC']
list_of_symbols27 = ['BNBBTC', 'LOOMBNB', 'LOOMBTC']
list_of_symbols28 = ['BNBBTC', 'LSKBNB', 'LSKBTC']
list_of_symbols29 = ['BNBBTC', 'LTCBNB', 'LTCBTC']
list_of_symbols30 = ['BNBBTC', 'MCOBNB', 'MCOBTC']
list_of_symbols31 = ['BNBBTC', 'MFTBNB', 'MFTBTC']
list_of_symbols32 = ['BNBBTC', 'NANOBNB', 'NANOBTC']
list_of_symbols33 = ['BNBBTC', 'NASBNB', 'NASBTC']
list_of_symbols34 = ['BNBBTC', 'NAVBNB', 'NAVBTC']
list_of_symbols35 = ['BNBBTC', 'NCASHBNB', 'NCASHBTC']
list_of_symbols36 = ['BNBBTC', 'NEBLBNB', 'NEBLBTC']
list_of_symbols37 = ['BNBBTC', 'NEOBNB', 'NEOBTC']
list_of_symbols38 = ['BNBBTC', 'NULSBNB', 'NULSBTC']
list_of_symbols39 = ['BNBBTC', 'NXSBNB', 'NXSBTC']
list_of_symbols40 = ['BNBBTC', 'ONTBNB', 'ONTBTC']
list_of_symbols41 = ['BNBBTC', 'OSTBNB', 'OSTBTC']
list_of_symbols42 = ['BNBBTC', 'PAXBNB', 'PAXBTC']
list_of_symbols43 = ['BNBBTC', 'PHXBNB', 'PHXBTC']
list_of_symbols44 = ['BNBBTC', 'PIVXBNB', 'PIVXBTC']
list_of_symbols45 = ['BNBBTC', 'POABNB', 'POABTC']
list_of_symbols46 = ['BNBBTC', 'POWRBNB', 'POWRBTC']
list_of_symbols47 = ['BNBBTC', 'QLCBNB', 'QLCBTC']
list_of_symbols48 = ['BNBBTC', 'QSPBNB', 'QSPBTC']
list_of_symbols49 = ['BNBBTC', 'QTUMBNB', 'QTUMBTC']
list_of_symbols50 = ['BNBBTC', 'RCNBNB', 'RCNBTC']
list_of_symbols51 = ['BNBBTC', 'RDNBNB', 'RDNBTC']
list_of_symbols52 = ['BNBBTC', 'REPBNB', 'REPBTC']
list_of_symbols53 = ['BNBBTC', 'RLCBNB', 'RLCBTC']
list_of_symbols54 = ['BNBBTC', 'SCBNB', 'SCBTC']
list_of_symbols55 = ['BNBBTC', 'SKYBNB', 'SKYBTC']
list_of_symbols56 = ['BNBBTC', 'STEEMBNB', 'STEEMBTC']
list_of_symbols57 = ['BNBBTC', 'STORMBNB', 'STORMBTC']
list_of_symbols58 = ['BNBBTC', 'SYSBNB', 'SYSBTC']
list_of_symbols59 = ['BNBBTC', 'THETABNB', 'THETABTC']
list_of_symbols60 = ['BNBBTC', 'TRXBNB', 'TRXBTC']
list_of_symbols61 = ['BNBBTC', 'TUSDBNB', 'TUSDBTC']
list_of_symbols62 = ['BNBBTC', 'VETBNB', 'VETBTC']
list_of_symbols63 = ['BNBBTC', 'VIABNB', 'VIABTC']
list_of_symbols64 = ['BNBBTC', 'WABIBNB', 'WABIBTC']
list_of_symbols65 = ['BNBBTC', 'WANBNB', 'WANBTC']
list_of_symbols66 = ['BNBBTC', 'WAVESBNB', 'WAVESBTC']
list_of_symbols67 = ['BNBBTC', 'WTCBNB', 'WTCBTC']
list_of_symbols68 = ['BNBBTC', 'XEMBNB', 'XEMBTC']
list_of_symbols69 = ['BNBBTC', 'XLMBNB', 'XLMBTC']
list_of_symbols70 = ['BNBBTC', 'XRPBNB', 'XRPBTC']
list_of_symbols71 = ['BNBBTC', 'XZCBNB', 'XZCBTC']
list_of_symbols72 = ['BNBBTC', 'YOYOBNB', 'YOYOBTC']
list_of_symbols73 = ['BNBBTC', 'ZENBNB', 'ZENBTC']
list_of_symbols74 = ['BNBBTC', 'ZILBNB', 'ZILBTC']
list_of_symbols75 = ['BNBETH', 'ADABNB', 'ADAETH']
list_of_symbols76 = ['BNBETH', 'ADXBNB', 'ADXETH']
list_of_symbols77 = ['BNBETH', 'AEBNB', 'AEETH']
list_of_symbols78 = ['BNBETH', 'AGIBNB', 'AGIETH']
list_of_symbols79 = ['BNBETH', 'AIONBNB', 'AIONETH']
list_of_symbols80 = ['BNBETH', 'AMBBNB', 'AMBETH']
list_of_symbols81 = ['BNBETH', 'APPCBNB', 'APPCETH']
list_of_symbols82 = ['BNBETH', 'ARDRBNB', 'ARDRETH']
list_of_symbols83 = ['BNBETH', 'BATBNB', 'BATETH']
list_of_symbols84 = ['BNBETH', 'BCCBNB', 'BCCETH']
list_of_symbols85 = ['BNBETH', 'BCPTBNB', 'BCPTETH']
list_of_symbols86 = ['BNBETH', 'BLZBNB', 'BLZETH']
list_of_symbols87 = ['BNBETH', 'BRDBNB', 'BRDETH']
list_of_symbols88 = ['BNBETH', 'BTSBNB', 'BTSETH']
list_of_symbols89 = ['BNBETH', 'CMTBNB', 'CMTETH']
list_of_symbols90 = ['BNBETH', 'CNDBNB', 'CNDETH']
list_of_symbols91 = ['BNBETH', 'CVCBNB', 'CVCETH']
list_of_symbols92 = ['BNBETH', 'DLTBNB', 'DLTETH']
list_of_symbols93 = ['BNBETH', 'ENJBNB', 'ENJETH']
list_of_symbols94 = ['BNBETH', 'EOSBNB', 'EOSETH']
list_of_symbols95 = ['BNBETH', 'ETCBNB', 'ETCETH']
list_of_symbols96 = ['BNBETH', 'GNTBNB', 'GNTETH']
list_of_symbols97 = ['BNBETH', 'GTOBNB', 'GTOETH']
list_of_symbols98 = ['BNBETH', 'ICXBNB', 'ICXETH']
list_of_symbols99 = ['BNBETH', 'IOTABNB', 'IOTAETH']
list_of_symbols100 = ['BNBETH', 'LOOMBNB', 'LOOMETH']
list_of_symbols101 = ['BNBETH', 'LSKBNB', 'LSKETH']
list_of_symbols102 = ['BNBETH', 'LTCBNB', 'LTCETH']
list_of_symbols103 = ['BNBETH', 'MCOBNB', 'MCOETH']
list_of_symbols104 = ['BNBETH', 'MFTBNB', 'MFTETH']
list_of_symbols105 = ['BNBETH', 'NANOBNB', 'NANOETH']
list_of_symbols106 = ['BNBETH', 'NASBNB', 'NASETH']
list_of_symbols107 = ['BNBETH', 'NAVBNB', 'NAVETH']
list_of_symbols108 = ['BNBETH', 'NCASHBNB', 'NCASHETH']
list_of_symbols109 = ['BNBETH', 'NEBLBNB', 'NEBLETH']
list_of_symbols110 = ['BNBETH', 'NEOBNB', 'NEOETH']
list_of_symbols111 = ['BNBETH', 'NULSBNB', 'NULSETH']
list_of_symbols112 = ['BNBETH', 'NXSBNB', 'NXSETH']
list_of_symbols113 = ['BNBETH', 'ONTBNB', 'ONTETH']
list_of_symbols114 = ['BNBETH', 'OSTBNB', 'OSTETH']
list_of_symbols115 = ['BNBETH', 'PAXBNB', 'PAXETH']
list_of_symbols116 = ['BNBETH', 'PHXBNB', 'PHXETH']
list_of_symbols117 = ['BNBETH', 'PIVXBNB', 'PIVXETH']
list_of_symbols118 = ['BNBETH', 'POABNB', 'POAETH']
list_of_symbols119 = ['BNBETH', 'POWRBNB', 'POWRETH']
list_of_symbols120 = ['BNBETH', 'QLCBNB', 'QLCETH']
list_of_symbols121 = ['BNBETH', 'QSPBNB', 'QSPETH']
list_of_symbols122 = ['BNBETH', 'QTUMBNB', 'QTUMETH']
list_of_symbols123 = ['BNBETH', 'RCNBNB', 'RCNETH']
list_of_symbols124 = ['BNBETH', 'RDNBNB', 'RDNETH']
list_of_symbols125 = ['BNBETH', 'REPBNB', 'REPETH']
list_of_symbols126 = ['BNBETH', 'RLCBNB', 'RLCETH']
list_of_symbols127 = ['BNBETH', 'SCBNB', 'SCETH']
list_of_symbols128 = ['BNBETH', 'SKYBNB', 'SKYETH']
list_of_symbols129 = ['BNBETH', 'STEEMBNB', 'STEEMETH']
list_of_symbols130 = ['BNBETH', 'STORMBNB', 'STORMETH']
list_of_symbols131 = ['BNBETH', 'SYSBNB', 'SYSETH']
list_of_symbols132 = ['BNBETH', 'THETABNB', 'THETAETH']
list_of_symbols133 = ['BNBETH', 'TRXBNB', 'TRXETH']
list_of_symbols134 = ['BNBETH', 'TUSDBNB', 'TUSDETH']
list_of_symbols135 = ['BNBETH', 'VETBNB', 'VETETH']
list_of_symbols136 = ['BNBETH', 'VIABNB', 'VIAETH']
list_of_symbols137 = ['BNBETH', 'WABIBNB', 'WABIETH']
list_of_symbols138 = ['BNBETH', 'WANBNB', 'WANETH']
list_of_symbols139 = ['BNBETH', 'WAVESBNB', 'WAVESETH']
list_of_symbols140 = ['BNBETH', 'WTCBNB', 'WTCETH']
list_of_symbols141 = ['BNBETH', 'XEMBNB', 'XEMETH']
list_of_symbols142 = ['BNBETH', 'XLMBNB', 'XLMETH']
list_of_symbols143 = ['BNBETH', 'XRPBNB', 'XRPETH']
list_of_symbols144 = ['BNBETH', 'XZCBNB', 'XZCETH']
list_of_symbols145 = ['BNBETH', 'YOYOBNB', 'YOYOETH']
list_of_symbols146 = ['BNBETH', 'ZENBNB', 'ZENETH']
list_of_symbols147 = ['BNBETH', 'ZILBNB', 'ZILETH']
list_of_symbols148 = ['ETHBTC', 'ADAETH', 'ADABTC']
list_of_symbols149 = ['ETHBTC', 'ADXETH', 'ADXBTC']
list_of_symbols150 = ['ETHBTC', 'AEETH', 'AEBTC']
list_of_symbols151 = ['ETHBTC', 'AGIETH', 'AGIBTC']
list_of_symbols152 = ['ETHBTC', 'AIONETH', 'AIONBTC']
list_of_symbols153 = ['ETHBTC', 'AMBETH', 'AMBBTC']
list_of_symbols154 = ['ETHBTC', 'APPCETH', 'APPCBTC']
list_of_symbols155 = ['ETHBTC', 'ARDRETH', 'ARDRBTC']
list_of_symbols156 = ['ETHBTC', 'ARKETH', 'ARKBTC']
list_of_symbols157 = ['ETHBTC', 'ARNETH', 'ARNBTC']
list_of_symbols158 = ['ETHBTC', 'ASTETH', 'ASTBTC']
list_of_symbols159 = ['ETHBTC', 'BATETH', 'BATBTC']
list_of_symbols160 = ['ETHBTC', 'BCCETH', 'BCCBTC']
list_of_symbols161 = ['ETHBTC', 'BCDETH', 'BCDBTC']
list_of_symbols162 = ['ETHBTC', 'BCPTETH', 'BCPTBTC']
list_of_symbols163 = ['ETHBTC', 'BLZETH', 'BLZBTC']
list_of_symbols164 = ['ETHBTC', 'BNBETH', 'BNBBTC']
list_of_symbols165 = ['ETHBTC', 'BNTETH', 'BNTBTC']
list_of_symbols166 = ['ETHBTC', 'BQXETH', 'BQXBTC']
list_of_symbols167 = ['ETHBTC', 'BRDETH', 'BRDBTC']
list_of_symbols168 = ['ETHBTC', 'BTGETH', 'BTGBTC']
list_of_symbols169 = ['ETHBTC', 'BTSETH', 'BTSBTC']
list_of_symbols170 = ['ETHBTC', 'CDTETH', 'CDTBTC']
list_of_symbols171 = ['ETHBTC', 'CLOAKETH', 'CLOAKBTC']
list_of_symbols172 = ['ETHBTC', 'CMTETH', 'CMTBTC']
list_of_symbols173 = ['ETHBTC', 'CNDETH', 'CNDBTC']
list_of_symbols174 = ['ETHBTC', 'CVCETH', 'CVCBTC']
list_of_symbols175 = ['ETHBTC', 'DASHETH', 'DASHBTC']
list_of_symbols176 = ['ETHBTC', 'DATAETH', 'DATABTC']
list_of_symbols177 = ['ETHBTC', 'DENTETH', 'DENTBTC']
list_of_symbols178 = ['ETHBTC', 'DGDETH', 'DGDBTC']
list_of_symbols179 = ['ETHBTC', 'DLTETH', 'DLTBTC']
list_of_symbols180 = ['ETHBTC', 'DNTETH', 'DNTBTC']
list_of_symbols181 = ['ETHBTC', 'DOCKETH', 'DOCKBTC']
list_of_symbols182 = ['ETHBTC', 'EDOETH', 'EDOBTC']
list_of_symbols183 = ['ETHBTC', 'ELFETH', 'ELFBTC']
list_of_symbols184 = ['ETHBTC', 'ENGETH', 'ENGBTC']
list_of_symbols185 = ['ETHBTC', 'ENJETH', 'ENJBTC']
list_of_symbols186 = ['ETHBTC', 'EOSETH', 'EOSBTC']
list_of_symbols187 = ['ETHBTC', 'ETCETH', 'ETCBTC']
list_of_symbols188 = ['ETHBTC', 'EVXETH', 'EVXBTC']
list_of_symbols189 = ['ETHBTC', 'FUELETH', 'FUELBTC']
list_of_symbols190 = ['ETHBTC', 'FUNETH', 'FUNBTC']
list_of_symbols191 = ['ETHBTC', 'GNTETH', 'GNTBTC']
list_of_symbols192 = ['ETHBTC', 'GRSETH', 'GRSBTC']
list_of_symbols193 = ['ETHBTC', 'GTOETH', 'GTOBTC']
list_of_symbols194 = ['ETHBTC', 'GVTETH', 'GVTBTC']
list_of_symbols195 = ['ETHBTC', 'GXSETH', 'GXSBTC']
list_of_symbols196 = ['ETHBTC', 'HCETH', 'HCBTC']
list_of_symbols197 = ['ETHBTC', 'HOTETH', 'HOTBTC']
list_of_symbols198 = ['ETHBTC', 'ICXETH', 'ICXBTC']
list_of_symbols199 = ['ETHBTC', 'INSETH', 'INSBTC']
list_of_symbols200 = ['ETHBTC', 'IOSTETH', 'IOSTBTC']
list_of_symbols201 = ['ETHBTC', 'IOTAETH', 'IOTABTC']
list_of_symbols202 = ['ETHBTC', 'IOTXETH', 'IOTXBTC']
list_of_symbols203 = ['ETHBTC', 'KEYETH', 'KEYBTC']
list_of_symbols204 = ['ETHBTC', 'KMDETH', 'KMDBTC']
list_of_symbols205 = ['ETHBTC', 'KNCETH', 'KNCBTC']
list_of_symbols206 = ['ETHBTC', 'LENDETH', 'LENDBTC']
list_of_symbols207 = ['ETHBTC', 'LINKETH', 'LINKBTC']
list_of_symbols208 = ['ETHBTC', 'LOOMETH', 'LOOMBTC']
list_of_symbols209 = ['ETHBTC', 'LRCETH', 'LRCBTC']
list_of_symbols210 = ['ETHBTC', 'LSKETH', 'LSKBTC']
list_of_symbols211 = ['ETHBTC', 'LTCETH', 'LTCBTC']
list_of_symbols212 = ['ETHBTC', 'LUNETH', 'LUNBTC']
list_of_symbols213 = ['ETHBTC', 'MANAETH', 'MANABTC']
list_of_symbols214 = ['ETHBTC', 'MCOETH', 'MCOBTC']
list_of_symbols215 = ['ETHBTC', 'MDAETH', 'MDABTC']
list_of_symbols216 = ['ETHBTC', 'MFTETH', 'MFTBTC']
list_of_symbols217 = ['ETHBTC', 'MODETH', 'MODBTC']
list_of_symbols218 = ['ETHBTC', 'MTHETH', 'MTHBTC']
list_of_symbols219 = ['ETHBTC', 'MTLETH', 'MTLBTC']
list_of_symbols220 = ['ETHBTC', 'NANOETH', 'NANOBTC']
list_of_symbols221 = ['ETHBTC', 'NASETH', 'NASBTC']
list_of_symbols222 = ['ETHBTC', 'NAVETH', 'NAVBTC']
list_of_symbols223 = ['ETHBTC', 'NCASHETH', 'NCASHBTC']
list_of_symbols224 = ['ETHBTC', 'NEBLETH', 'NEBLBTC']
list_of_symbols225 = ['ETHBTC', 'NEOETH', 'NEOBTC']
list_of_symbols226 = ['ETHBTC', 'NPXSETH', 'NPXSBTC']
list_of_symbols227 = ['ETHBTC', 'NULSETH', 'NULSBTC']
list_of_symbols228 = ['ETHBTC', 'NXSETH', 'NXSBTC']
list_of_symbols229 = ['ETHBTC', 'OAXETH', 'OAXBTC']
list_of_symbols230 = ['ETHBTC', 'OMGETH', 'OMGBTC']
list_of_symbols231 = ['ETHBTC', 'ONTETH', 'ONTBTC']
list_of_symbols232 = ['ETHBTC', 'OSTETH', 'OSTBTC']
list_of_symbols233 = ['ETHBTC', 'PAXETH', 'PAXBTC']
list_of_symbols234 = ['ETHBTC', 'PHXETH', 'PHXBTC']
list_of_symbols235 = ['ETHBTC', 'PIVXETH', 'PIVXBTC']
list_of_symbols236 = ['ETHBTC', 'POAETH', 'POABTC']
list_of_symbols237 = ['ETHBTC', 'POEETH', 'POEBTC']
list_of_symbols238 = ['ETHBTC', 'POWRETH', 'POWRBTC']
list_of_symbols239 = ['ETHBTC', 'PPTETH', 'PPTBTC']
list_of_symbols240 = ['ETHBTC', 'QKCETH', 'QKCBTC']
list_of_symbols241 = ['ETHBTC', 'QLCETH', 'QLCBTC']
list_of_symbols242 = ['ETHBTC', 'QSPETH', 'QSPBTC']
list_of_symbols243 = ['ETHBTC', 'QTUMETH', 'QTUMBTC']
list_of_symbols244 = ['ETHBTC', 'RCNETH', 'RCNBTC']
list_of_symbols245 = ['ETHBTC', 'RDNETH', 'RDNBTC']
list_of_symbols246 = ['ETHBTC', 'REPETH', 'REPBTC']
list_of_symbols247 = ['ETHBTC', 'REQETH', 'REQBTC']
list_of_symbols248 = ['ETHBTC', 'RLCETH', 'RLCBTC']
list_of_symbols249 = ['ETHBTC', 'SALTETH', 'SALTBTC']
list_of_symbols250 = ['ETHBTC', 'SCETH', 'SCBTC']
list_of_symbols251 = ['ETHBTC', 'SKYETH', 'SKYBTC']
list_of_symbols252 = ['ETHBTC', 'SNGLSETH', 'SNGLSBTC']
list_of_symbols253 = ['ETHBTC', 'SNMETH', 'SNMBTC']
list_of_symbols254 = ['ETHBTC', 'SNTETH', 'SNTBTC']
list_of_symbols255 = ['ETHBTC', 'STEEMETH', 'STEEMBTC']
list_of_symbols256 = ['ETHBTC', 'STORJETH', 'STORJBTC']
list_of_symbols257 = ['ETHBTC', 'STORMETH', 'STORMBTC']
list_of_symbols258 = ['ETHBTC', 'STRATETH', 'STRATBTC']
list_of_symbols259 = ['ETHBTC', 'SUBETH', 'SUBBTC']
list_of_symbols260 = ['ETHBTC', 'SYSETH', 'SYSBTC']
list_of_symbols261 = ['ETHBTC', 'THETAETH', 'THETABTC']
list_of_symbols262 = ['ETHBTC', 'TNBETH', 'TNBBTC']
list_of_symbols263 = ['ETHBTC', 'TNTETH', 'TNTBTC']
list_of_symbols264 = ['ETHBTC', 'TRXETH', 'TRXBTC']
list_of_symbols265 = ['ETHBTC', 'TUSDETH', 'TUSDBTC']
list_of_symbols266 = ['ETHBTC', 'VETETH', 'VETBTC']
list_of_symbols267 = ['ETHBTC', 'VIAETH', 'VIABTC']
list_of_symbols268 = ['ETHBTC', 'VIBEETH', 'VIBEBTC']
list_of_symbols269 = ['ETHBTC', 'VIBETH', 'VIBBTC']
list_of_symbols270 = ['ETHBTC', 'WABIETH', 'WABIBTC']
list_of_symbols271 = ['ETHBTC', 'WANETH', 'WANBTC']
list_of_symbols272 = ['ETHBTC', 'WAVESETH', 'WAVESBTC']
list_of_symbols273 = ['ETHBTC', 'WINGSETH', 'WINGSBTC']
list_of_symbols274 = ['ETHBTC', 'WPRETH', 'WPRBTC']
list_of_symbols275 = ['ETHBTC', 'WTCETH', 'WTCBTC']
list_of_symbols276 = ['ETHBTC', 'XEMETH', 'XEMBTC']
list_of_symbols277 = ['ETHBTC', 'XLMETH', 'XLMBTC']
list_of_symbols278 = ['ETHBTC', 'XMRETH', 'XMRBTC']
list_of_symbols279 = ['ETHBTC', 'XRPETH', 'XRPBTC']
list_of_symbols280 = ['ETHBTC', 'XVGETH', 'XVGBTC']
list_of_symbols281 = ['ETHBTC', 'XZCETH', 'XZCBTC']
list_of_symbols282 = ['ETHBTC', 'YOYOETH', 'YOYOBTC']
list_of_symbols283 = ['ETHBTC', 'ZECETH', 'ZECBTC']
list_of_symbols284 = ['ETHBTC', 'ZENETH', 'ZENBTC']
list_of_symbols285 = ['ETHBTC', 'ZILETH', 'ZILBTC']
list_of_symbols286 = ['ETHBTC', 'ZRXETH', 'ZRXBTC']             

list_of_arb_sym = [list_of_symbols2,list_of_symbols3,list_of_symbols4,list_of_symbols5,list_of_symbols6
    ,list_of_symbols7,list_of_symbols8,list_of_symbols9,list_of_symbols10,list_of_symbols11,list_of_symbols12
    ,list_of_symbols13,list_of_symbols14,list_of_symbols15,list_of_symbols16,list_of_symbols17,list_of_symbols18
    ,list_of_symbols19,list_of_symbols20,list_of_symbols21,list_of_symbols22,list_of_symbols23,list_of_symbols24
    ,list_of_symbols25,list_of_symbols26,list_of_symbols27,list_of_symbols28,list_of_symbols29,list_of_symbols30
    ,list_of_symbols31,list_of_symbols32,list_of_symbols33,list_of_symbols34,list_of_symbols35,list_of_symbols36
    ,list_of_symbols37,list_of_symbols38,list_of_symbols39,list_of_symbols40,list_of_symbols41,list_of_symbols42
    ,list_of_symbols43,list_of_symbols44,list_of_symbols45,list_of_symbols46,list_of_symbols47,list_of_symbols48
    ,list_of_symbols49,list_of_symbols50,list_of_symbols51,list_of_symbols52,list_of_symbols53,list_of_symbols54
    ,list_of_symbols55,list_of_symbols56,list_of_symbols57,list_of_symbols58,list_of_symbols59,list_of_symbols60
    ,list_of_symbols61,list_of_symbols62,list_of_symbols63,list_of_symbols64,list_of_symbols65,list_of_symbols66
    ,list_of_symbols67,list_of_symbols68,list_of_symbols69,list_of_symbols70,list_of_symbols71,list_of_symbols72
    ,list_of_symbols73,list_of_symbols74,list_of_symbols75,list_of_symbols76,list_of_symbols77,list_of_symbols78
    ,list_of_symbols79,list_of_symbols80,list_of_symbols81,list_of_symbols82,list_of_symbols83,list_of_symbols84
    ,list_of_symbols85,list_of_symbols86,list_of_symbols87,list_of_symbols88,list_of_symbols89,list_of_symbols90
    ,list_of_symbols91,list_of_symbols92,list_of_symbols93,list_of_symbols94,list_of_symbols95,list_of_symbols96
    ,list_of_symbols97,list_of_symbols98,list_of_symbols99,list_of_symbols100,list_of_symbols101,list_of_symbols102
    ,list_of_symbols103,list_of_symbols104,list_of_symbols105,list_of_symbols106,list_of_symbols107,list_of_symbols108
    ,list_of_symbols109,list_of_symbols110,list_of_symbols111,list_of_symbols112,list_of_symbols113,list_of_symbols114
    ,list_of_symbols115,list_of_symbols116,list_of_symbols117,list_of_symbols118,list_of_symbols119,list_of_symbols120
    ,list_of_symbols121,list_of_symbols122,list_of_symbols123,list_of_symbols124,list_of_symbols125,list_of_symbols126
    ,list_of_symbols127,list_of_symbols128,list_of_symbols129,list_of_symbols130,list_of_symbols131,list_of_symbols132
    ,list_of_symbols133,list_of_symbols134,list_of_symbols135,list_of_symbols136,list_of_symbols137,list_of_symbols138
    ,list_of_symbols139,list_of_symbols140,list_of_symbols141,list_of_symbols142,list_of_symbols143,list_of_symbols144
    ,list_of_symbols145,list_of_symbols146,list_of_symbols147,list_of_symbols148,list_of_symbols149,list_of_symbols150
    ,list_of_symbols151,list_of_symbols152,list_of_symbols153,list_of_symbols154,list_of_symbols155,list_of_symbols156
    ,list_of_symbols157,list_of_symbols158,list_of_symbols159,list_of_symbols160,list_of_symbols161,list_of_symbols162
    ,list_of_symbols163,list_of_symbols164,list_of_symbols165,list_of_symbols166,list_of_symbols167,list_of_symbols168
    ,list_of_symbols169,list_of_symbols170,list_of_symbols171,list_of_symbols172,list_of_symbols173,list_of_symbols174
    ,list_of_symbols175,list_of_symbols176,list_of_symbols177,list_of_symbols178,list_of_symbols179,list_of_symbols180
    ,list_of_symbols181,list_of_symbols182,list_of_symbols183,list_of_symbols184,list_of_symbols185,list_of_symbols186
    ,list_of_symbols187,list_of_symbols188,list_of_symbols189,list_of_symbols190,list_of_symbols191,list_of_symbols192
    ,list_of_symbols193,list_of_symbols194,list_of_symbols195,list_of_symbols196,list_of_symbols197,list_of_symbols198
    ,list_of_symbols199,list_of_symbols200,list_of_symbols201,list_of_symbols202,list_of_symbols203,list_of_symbols204
    ,list_of_symbols205,list_of_symbols206,list_of_symbols207,list_of_symbols208,list_of_symbols209,list_of_symbols210
    ,list_of_symbols211,list_of_symbols212,list_of_symbols213,list_of_symbols214,list_of_symbols215,list_of_symbols216
    ,list_of_symbols217,list_of_symbols218,list_of_symbols219,list_of_symbols220,list_of_symbols221,list_of_symbols222
    ,list_of_symbols223,list_of_symbols224,list_of_symbols225,list_of_symbols226,list_of_symbols227,list_of_symbols228
    ,list_of_symbols229,list_of_symbols230,list_of_symbols231,list_of_symbols232,list_of_symbols233,list_of_symbols234
    ,list_of_symbols235,list_of_symbols236,list_of_symbols237,list_of_symbols238,list_of_symbols239,list_of_symbols240
    ,list_of_symbols241,list_of_symbols242,list_of_symbols243,list_of_symbols244,list_of_symbols245,list_of_symbols246
    ,list_of_symbols247,list_of_symbols248,list_of_symbols249,list_of_symbols250,list_of_symbols251,list_of_symbols252
    ,list_of_symbols253,list_of_symbols254,list_of_symbols255,list_of_symbols256,list_of_symbols257,list_of_symbols258
    ,list_of_symbols259,list_of_symbols260,list_of_symbols261,list_of_symbols262,list_of_symbols263,list_of_symbols264
    ,list_of_symbols265,list_of_symbols266,list_of_symbols267,list_of_symbols268,list_of_symbols269,list_of_symbols270
    ,list_of_symbols271,list_of_symbols272,list_of_symbols273,list_of_symbols274,list_of_symbols275,list_of_symbols276
    ,list_of_symbols277,list_of_symbols278,list_of_symbols279,list_of_symbols280,list_of_symbols281,list_of_symbols282
    ,list_of_symbols283,list_of_symbols284,list_of_symbols285,list_of_symbols286]
        
print(client)

def run():
    #set_time_binance()
    #Initialize Arbitrage Binance Bot
    os.system('cls')
    bot_start_time = str(datetime.now())
    btc_begin = client.get_asset_balance(asset='BTC')["free"]
    bnb_begin = client.get_asset_balance(asset='BNB')["free"]
    eth_begin = client.get_asset_balance(asset='ETH')["free"]
    welcome_message = "\n(*) Bot Start Time: {}\n".format(bot_start_time)
    welcome_message+= '\n(*) Account Detail'
    welcome_message+= '\n\tBTC : ' + str(btc_begin)
    welcome_message+= '\n\tBNB : ' + str(bnb_begin)
    welcome_message+= '\n\tETH : ' + str(eth_begin)
    welcome_message+= '\n\tFEE : {}%\n'.format(fee*100)

    print(welcome_message)
    notify.send(welcome_message)

    while 1:
        try:
            initialize_arb()
            global update_amt
            update_amt = False
            tickers = client.get_orderbook_tickers()
            for symlistCnt in list_of_arb_sym:
                exch_rate_list.clear()
                qtt_rate_list.clear()
                #os.system('cls')
                tickers = client.get_orderbook_tickers()
                try:
                    print('(*) Arbitrage Bot Status : Running\n')
                    arbitrage_bin(symlistCnt, tickers, 1, 1)
                    if profit_cal(symlistCnt,get_amout(symlistCnt)) == True:
                        continue

                    arbitrage_bin_rv(symlistCnt, tickers, 1, 1)
                    if profit_cal_rv(symlistCnt,get_amout(symlistCnt)) == True:
                        continue

                    print("\n(*) ## Can't Arbitrage ##")
                           
                except Exception as e:
                    print(e)
                    print("\n(!) ARBITRAGE FAIL\n")
                    if str(e) == "list index out of range":
                        continue
                    elif str(e) == "float division by zero":
                        continue
                    elif str(e) == "APIError(code=-1013): Filter failure: MIN_NOTIONAL":
                        continue
                    elif str(e) == "APIError(code=-1003): Too many requests; current limit is 1200 requests per 1 MINUTE. Please use the websocket for live updates to avoid polling the API.":
                        continue
                    elif str(e) == "('Connection aborted.', OSError(\"(10054, 'WSAECONNRESET')\"))":
                        notify.send(symlistCnt[0] + ' ' + symlistCnt[1] + ' ' + symlistCnt[2])
                        notify.send("API Connection aborted.")
                        continue

                    #input("Press Enter to continue...")
                    notify.send(symlistCnt[0] + ' ' + symlistCnt[1] + ' ' + symlistCnt[2])
                    notify.send(e)
                    time.sleep(0.5)
                    pass
                    
                print('=============NEXT=============\n')
                #time.sleep(0.1)
                #input("Press Enter to continue...")

        except:
            print("(!) Fail to run\n\n")

    pass

def initialize_arb():
    welcome_message = "\n------------------------------------------------------------------\n"
    bot_start_time = str(datetime.now())
    welcome_message+= "\n(*) Bot Start Time: {}\n".format(bot_start_time)
    print(welcome_message)
    #notify.send(welcome_message)
    print('(*) Fee = ' + str(fee*100) + '%')
    #info = client.get_account()
    #print(info)
    try:
        status = client.get_system_status()
        print("\n(*) Exchange Status: {}\n".format(status))
        msg1 = "(*) LOADING BALANCES FROM BINANCE" 
        print(msg1)

    except Exception as e:
        print(e)
        print("\nFAILURE INITIALIZE\n")
        raise
    time.sleep(1)

def get_amout(symlistCnt):
    global update_amt
    global start_amount_bnb
    global start_amount_eth
    if update_amt == False:
            start_amount_bnb = float(int(float(client.get_asset_balance(asset='BNB')["free"])*100)/100)
            start_amount_eth = float(int(float(client.get_asset_balance(asset='ETH')["free"])*1000)/1000) 
            print('(*) Amout Updated.')
            #notify.send('Amout Updated.')
            update_amt = True

    if symlistCnt[0][0:3] == 'BNB':
        start_amount = start_amount_bnb
    if symlistCnt[0][0:3] == 'ETH':
        start_amount = start_amount_eth

    return start_amount

def profit_cal(list_of_sym,start_amount):
    print('(*) normal solution calculate...')
    amt_coin2 = start_amount * float(exch_rate_list[0])
    amt_coin2_no_fee = amt_coin2
    amt_coin2_fee = amt_coin2*fee
    amt_coin2_adj = amt_coin2*(1-fee)
    amt_coin3 = amt_coin2_adj / float(exch_rate_list[2])
    amt_coin3 = int(amt_coin3)
    amt_coin3_no_fee = amt_coin2_no_fee/float(exch_rate_list[2])
    amt_coin3_fee = amt_coin3 * fee
    amt_coin3_adj = amt_coin3*(1-fee)
    amt_coin3_adj = amt_coin3_adj
    final_amount = amt_coin3_adj * float(exch_rate_list[1])
    final_amount_no_fee = amt_coin3_no_fee * float(exch_rate_list[1])
    final_amount_fee = final_amount *fee
    final_amount_adj = final_amount *(1-fee)
    print('(*) normal solution profit = {}'.format(final_amount_adj-start_amount))
    if final_amount_adj > start_amount : 
        global update_amt
        update_amt = False
        #notify.send('(*) normal solution profit = {}'.format(final_amount_adj-start_amount))
        #Quantity check
        qtt_status = True
        if (amt_coin3 >= qtt_rate_list[1]):
            print("[{} > {}] Order3 is check fail. Calculate again..".format(amt_coin3,qtt_rate_list[1]))
            #notify.send("[{} > {}] Order3 is check fail. Calculate again..".format(amt_coin3,qtt_rate_list[1]))
            start_amount = start_amount * (qtt_rate_list[1]/amt_coin3) * amt_ratio
            qtt_status = False
        elif (amt_coin3 >= qtt_rate_list[2]):
            print("[{} > {}] Order2 is check fail. Calculate again..".format(amt_coin3,qtt_rate_list[2]))
            #notify.send("[{} > {}] Order2 is check fail. Calculate again..".format(amt_coin3,qtt_rate_list[2]))
            start_amount = start_amount * (qtt_rate_list[2]/amt_coin3) * amt_ratio
            qtt_status = False
        if qtt_status == False:
            start_amount = float(int(float(start_amount)*100)/100)
            print('(New) Start amount = {}'.format(start_amount))
            #notify.send('(New) Start amount = {}'.format(start_amount))
            amt_coin2 = start_amount * float(exch_rate_list[0])
            amt_coin2_no_fee = amt_coin2
            amt_coin2_fee = amt_coin2*fee
            amt_coin2_adj = amt_coin2*(1-fee)
            amt_coin3 = amt_coin2_adj / float(exch_rate_list[2])
            amt_coin3 = int(amt_coin3)
            amt_coin3_no_fee = amt_coin2_no_fee/float(exch_rate_list[2])
            amt_coin3_fee = amt_coin3 * fee
            amt_coin3_adj = amt_coin3*(1-fee)
            amt_coin3_adj = amt_coin3_adj
            final_amount = amt_coin3_adj * float(exch_rate_list[1])
            final_amount_no_fee = amt_coin3_no_fee * float(exch_rate_list[1])
            final_amount_fee = final_amount *fee
            final_amount_adj = final_amount *(1-fee)

        if final_amount_adj > start_amount : 
            notify.send('(New) Start amount = {}'.format(start_amount))
            notify.send('(*) normal solution profit = {}'.format(final_amount_adj-start_amount))
            tri_arb_paper_msg = "\n(*) Starting Amount: "+str(start_amount)+str(list_of_sym[0][0:3])+" "+'\n'
            #Buy Currency 2 with Currency 1
            tri_arb_paper_msg += "\n"+str(list_of_sym[0]) + " ,order_sell price : " + str(exch_rate_list[0])
            tri_arb_paper_msg += "\nAmount Coin 2: "+str(list_of_sym[0][3:6])+" "+str(amt_coin2)
            tri_arb_paper_msg += "\nAmount Coin 2 (no fee): "+str(list_of_sym[0][3:6])+" "+str(amt_coin2_no_fee)
            tri_arb_paper_msg += "\nAmount Coin 2 Fee: "+str(list_of_sym[0][3:6])+" "+str(amt_coin2_fee)
            tri_arb_paper_msg += "\nAmount Coin 2 Adjusted: "+str(list_of_sym[0][3:6])+" "+str(amt_coin2_adj)+'\n'
            #Buy Currency 3 with Currency 2
            tri_arb_paper_msg += "\n"+str(list_of_sym[2]) + " ,order_buy price : " + str(exch_rate_list[2])
            tri_arb_paper_msg += "\nAmount Coin 3: "+str(list_of_sym[1][0:3])+" "+str(amt_coin3) 
            tri_arb_paper_msg += "\nAmount Coin 3 (no fee): "+str(list_of_sym[1][0:3])+" "+str(amt_coin3_no_fee) 
            tri_arb_paper_msg += "\nAmount Coin 3 Fee: "+str(list_of_sym[1][0:3])+" "+str(amt_coin3_fee)
            tri_arb_paper_msg += "\nAmount Coin 3 Adjusted: "+str(list_of_sym[1][0:3])+" "+str(amt_coin3_adj)+'\n'
            #Buy Currency 1 with Currency 3
            tri_arb_paper_msg += "\n"+str(list_of_sym[1]) + " ,order_sell price : " + str(exch_rate_list[1])
            tri_arb_paper_msg += "\nFinal Amount: "+str(list_of_sym[0][0:3])+" "+str(final_amount)
            tri_arb_paper_msg += "\nFinal Amount (No Fee): "+str(list_of_sym[0][0:3])+" "+str(final_amount_no_fee)
            tri_arb_paper_msg += "\nFinal Amount Fee: "+str(list_of_sym[0][0:3])+" "+str(final_amount_fee)
            tri_arb_paper_msg += "\nFinal Amount Adjusted: "+str(list_of_sym[0][0:3])+" "+str(final_amount_adj)+'\n'
            print(tri_arb_paper_msg)
            notify.send(tri_arb_paper_msg)

            """1ST TRADE"""
            print("order1 = client.order_limit_sell(\n\tsymbol=\'"+str(list_of_sym[0])+'\',\n\t'+'quantity='+str(start_amount)+',\n\t'+'price=\''+str(float(exch_rate_list[0]))+'\')\n')
            notify.send("order1 = client.order_limit_sell(\n\tsymbol=\'"+str(list_of_sym[0])+'\',\n\t'+'quantity='+str(start_amount)+',\n\t'+'price=\''+str(float(exch_rate_list[0]))+'\')\n')

            client.order_limit_sell(
                symbol=str(list_of_sym[0]),
                quantity=start_amount,
                price='{:0.0{}f}'.format(exch_rate_list[0], precision))

            while bool(client.get_open_orders(symbol=str(list_of_sym[0]))):
                print('.', end = '')
            
            """2ND TRADE"""
            print("order2 = client.order_limit_buy(\n\tsymbol=\'"+str(list_of_sym[2])+'\',\n\t'+'quantity='+str(int(amt_coin3))+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[2], precision)+'\')\n')
            notify.send("order2 = client.order_limit_buy(\n\tsymbol=\'"+str(list_of_sym[2])+'\',\n\t'+'quantity='+str(int(amt_coin3))+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[2], precision)+'\')\n')

            client.order_limit_buy(
                symbol=str(list_of_sym[2]),
                quantity=int(amt_coin3),
                price='{:0.0{}f}'.format(exch_rate_list[2], precision))

            while bool(client.get_open_orders(symbol=str(list_of_sym[2]))):
                print('.', end = '')
            
            """3TH TRADE"""
            print("order3 = client.order_limit_sell(\n\tsymbol=\'"+str(list_of_sym[1])+'\',\n\t'+'quantity='+str(int(amt_coin3_adj))+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[1], precision)+'\')\n')
            notify.send("order3 = client.order_limit_sell(\n\tsymbol=\'"+str(list_of_sym[1])+'\',\n\t'+'quantity='+str(int(amt_coin3_adj))+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[1], precision)+'\')\n')

            client.order_limit_sell(
                symbol=str(list_of_sym[1]),
                quantity=int(amt_coin3_adj),
                price='{:0.0{}f}'.format(exch_rate_list[1], precision))

            while bool(client.get_open_orders(symbol=str(list_of_sym[1]))):
                print('.', end = '')
            
            return True
        
        else:
            print("(*) Can't Normal Arbitrage for new calculate.")
            #notify.send("Can't Normal Arbitrage for new calculate.")

    else:
        print("(*) Can't Normal Arbitrage")
        return False

def profit_cal_rv(list_of_sym,start_amount):
    print('\n(*) reverse solution calculate...')
    amt_coin2 = start_amount / float(exch_rate_list[4])
    amt_coin2 = int(amt_coin2)#
    amt_coin2_no_fee = amt_coin2
    amt_coin2_fee = amt_coin2*fee
    amt_coin2_adj = amt_coin2*(1-fee)
    amt_coin3 = amt_coin2_adj * float(exch_rate_list[5])
    amt_coin3_no_fee = amt_coin2_no_fee*float(exch_rate_list[5])
    amt_coin3_fee = amt_coin3 * fee
    amt_coin3_adj = amt_coin3*(1-fee)
    final_amount = amt_coin3_adj / float(exch_rate_list[3])
    final_amount_no_fee = amt_coin3_no_fee / float(exch_rate_list[3])
    final_amount_fee = final_amount *fee
    final_amount_adj = final_amount *(1-fee)
    print('(*) reverse solution profit = {}'.format(final_amount_adj-start_amount))

    if final_amount_adj > start_amount :
        global update_amt
        update_amt = False
        #notify.send('(*) reverse solution profit = {}'.format(final_amount_adj-start_amount))

        #Quantity check
        qtt_status = True
        if (amt_coin2 >= qtt_rate_list[4]):
            print("[{} > {}] Order1 is check fail. Calculate again..".format(amt_coin2,qtt_rate_list[4]))
            #notify.send("[{} > {}] Order3 is check fail. Calculate again..".format(amt_coin2,qtt_rate_list[4]))
            start_amount = start_amount * (qtt_rate_list[4]/amt_coin2) * amt_ratio
            qtt_status = False
        elif (amt_coin2 >= qtt_rate_list[5]):
            print("[{} > {}] Order2 is check fail. Calculate again..".format(amt_coin2,qtt_rate_list[5]))
            #notify.send("[{} > {}] Order2 is check fail. Calculate again..".format(amt_coin2,qtt_rate_list[5]))
            start_amount = start_amount * (qtt_rate_list[5]/amt_coin2) * amt_ratio
            qtt_status = False
        if qtt_status == False:
            start_amount = float(int(float(start_amount)*100)/100)
            print("Volume check is fail, Calculate again..")
            print('(New) Start amount = {}'.format(start_amount))
            #notify.send("Volume check is fail, Calculate again..")
            #notify.send('(New) Start amount = {}'.format(start_amount))
            amt_coin2 = start_amount / float(exch_rate_list[4])
            amt_coin2 = int(amt_coin2)
            amt_coin2_no_fee = amt_coin2
            amt_coin2_fee = amt_coin2*fee
            amt_coin2_adj = amt_coin2*(1-fee)
            amt_coin3 = amt_coin2_adj * float(exch_rate_list[5])
            amt_coin3_no_fee = amt_coin2_no_fee*float(exch_rate_list[5])
            amt_coin3_fee = amt_coin3 * fee
            amt_coin3_adj = amt_coin3*(1-fee)
            final_amount = amt_coin3_adj / float(exch_rate_list[3])
            final_amount_no_fee = amt_coin3_no_fee / float(exch_rate_list[3])
            final_amount_fee = final_amount *fee
            final_amount_adj = final_amount *(1-fee)

        if final_amount_adj > start_amount :
            notify.send('(New) Start amount = {}'.format(start_amount))
            notify.send('(*) reverse solution profit = {}'.format(final_amount_adj-start_amount))
            tri_arb_paper_msg = "(*) [reverse] Starting Amount: "+str(start_amount)+str(list_of_sym[0][0:3])+" "+'\n'
            #Buy Currency 2 with Currency 1
            tri_arb_paper_msg += "\n"+str(list_of_sym[1]) + " ,order_buy price : " + str(exch_rate_list[4])
            tri_arb_paper_msg += "\nAmount Coin 2: "+str(list_of_sym[0][3:6])+" "+str(amt_coin2)
            tri_arb_paper_msg += "\nAmount Coin 2 (no fee): "+str(list_of_sym[0][3:6])+" "+str(amt_coin2_no_fee)
            tri_arb_paper_msg += "\nAmount Coin 2 Fee: "+str(list_of_sym[0][3:6])+" "+str(amt_coin2_fee)
            tri_arb_paper_msg += "\nAmount Coin 2 Adjusted: "+str(list_of_sym[0][3:6])+" "+str(amt_coin2_adj)+'\n'
            #Buy Currency 3 with Currency 2
            tri_arb_paper_msg += "\n"+str(list_of_sym[2]) + " ,order_sell price : " + str(exch_rate_list[5])
            tri_arb_paper_msg += "\nAmount Coin 3: "+str(list_of_sym[1][0:3])+" "+str(amt_coin3) 
            tri_arb_paper_msg += "\nAmount Coin 3 (no fee): "+str(list_of_sym[1][0:3])+" "+str(amt_coin3_no_fee) 
            tri_arb_paper_msg += "\nAmount Coin 3 Fee: "+str(list_of_sym[1][0:3])+" "+str(amt_coin3_fee)
            tri_arb_paper_msg += "\nAmount Coin 3 Adjusted: "+str(list_of_sym[1][0:3])+" "+str(amt_coin3_adj)+'\n'
            #Buy Currency 1 with Currency 3
            tri_arb_paper_msg += "\n"+str(list_of_sym[0]) + " ,order_buy price : " + str(exch_rate_list[3])
            tri_arb_paper_msg += "\nFinal Amount: "+str(list_of_sym[0][0:3])+" "+str(final_amount)
            tri_arb_paper_msg += "\nFinal Amount (No Fee): "+str(list_of_sym[0][0:3])+" "+str(final_amount_no_fee)
            tri_arb_paper_msg += "\nFinal Amount Fee: "+str(list_of_sym[0][0:3])+" "+str(final_amount_fee)
            tri_arb_paper_msg += "\nFinal Amount Adjusted: "+str(list_of_sym[0][0:3])+" "+str(final_amount_adj)+'\n'
            print(tri_arb_paper_msg)
            notify.send(tri_arb_paper_msg)

            """1ST TRADE"""
            print("order1 = client.order_limit_buy(\n\tsymbol=\'"+str(list_of_sym[1])+'\',\n\t'+'quantity='+str(amt_coin2)+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[4], precision)+'\')\n')
            notify.send("order1 = client.order_limit_buy(\n\tsymbol=\'"+str(list_of_sym[1])+'\',\n\t'+'quantity='+str(amt_coin2)+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[4], precision)+'\')\n')

            client.order_limit_buy(
                symbol=str(list_of_sym[1]),
                quantity=amt_coin2,
                price='{:0.0{}f}'.format(exch_rate_list[4], precision))

            while bool(client.get_open_orders(symbol=str(list_of_sym[1]))):
                print('.', end = '')
            
            """2ND TRADE"""
            print("order2 = client.order_limit_sell(\n\tsymbol=\'"+str(list_of_sym[2])+'\',\n\t'+'quantity='+str(int(amt_coin2_adj))+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[5], precision)+'\')\n')
            notify.send("order2 = client.order_limit_sell(\n\tsymbol=\'"+str(list_of_sym[2])+'\',\n\t'+'quantity='+str(int(amt_coin2_adj))+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[5], precision)+'\')\n')

            client.order_limit_sell(
                symbol=str(list_of_sym[2]),
                quantity=int(amt_coin2_adj),
                price='{:0.0{}f}'.format(exch_rate_list[5], precision))

            while bool(client.get_open_orders(symbol=str(list_of_sym[2]))):
                print('.', end = '')
            
            """3TH TRADE"""
            print("order3 = client.order_limit_buy(\n\tsymbol=\'"+str(list_of_sym[0])+'\',\n\t'+'quantity='+str(start_amount)+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[3], precision)+'\')\n')
            notify.send("order3 = client.order_limit_buy(\n\tsymbol=\'"+str(list_of_sym[0])+'\',\n\t'+'quantity='+str(start_amount)+',\n\t'+'price=\''+'{:0.0{}f}'.format(exch_rate_list[3], precision)+'\')\n')
    
            client.order_limit_buy(
                symbol=str(list_of_sym[0]),
                quantity=start_amount,
                price='{:0.0{}f}'.format(exch_rate_list[3], precision))

            while bool(client.get_open_orders(symbol=str(list_of_sym[0]))):
                print('.', end = '')

            return True

        else:
            print("(*) Can't Reverse Arbitrage for new calculate")
            #notify.send("Can't Reverse Arbitrage for new calculate")

    else:
        print("(*) Can't Reverse Arbitrage")
        return False

def arbitrage_bin(list_of_sym, tickers, cycle_num=1, cycle_time=30, place_order='Yes', real_order='Yes'):
    print("(*) List of Arbitrage Symbols:", list_of_sym)
    for k in range(0,cycle_num):
                i=0
                for sym in list_of_sym:
                    currency_pair = "(~) Currency Pair: "+str(sym)+" "
                    if sym in list_of_sym:
                        if i % 2==0:
                            depth = next(item for item in tickers if item['symbol'] == sym)
                            if i ==0:
                                price1 = float(depth['askPrice'])
                                qtt1 = float(depth['askQty'])
                                exch_rate_list.append(price1)
                                qtt_rate_list.append(qtt1)
                                Exch_rate1 = currency_pair+ "Exchange Rate ['asks']: {}".format(depth['askPrice']) +' '
                            if i ==2:
                                price3 = float(depth['askPrice'])
                                exch_rate_list.append(price3)
                                qtt3 = float(depth['askQty'])
                                qtt_rate_list.append(qtt3)
                                Exch_rate1 = currency_pair+ "Exchange Rate ['asks']: {}".format(depth['askPrice']) +' '
                            print(Exch_rate1)
                        if i == 1:
                            depth = next(item for item in tickers if item['symbol'] == sym)
                            price2 = float(depth['bidPrice'])
                            exch_rate_list.append(price2)
                            qtt2 = float(depth['bidQty'])
                            qtt_rate_list.append(qtt2)
                            Exch_rate2 = currency_pair+"Exchange Rate ['bids']: {}".format(float(depth['bidPrice']))+' '
                            print(Exch_rate2)
                        i+=1
                    else:
                        exch_rate_list.append(0)
        
                print(exch_rate_list)
                print('\n')

def arbitrage_bin_rv(list_of_sym, tickers, cycle_num=1, cycle_time=30, place_order='Yes', real_order='Yes'):
    print("\n(*) [reverse] List of Arbitrage Symbols:", list_of_sym)
    for k in range(0,cycle_num):
                i=0
                for sym in list_of_sym:
                    currency_pair = "(~) Currency Pair: "+str(sym)+" "
                    if sym in list_of_sym:
                        if i % 2==0:
                            depth = next(item for item in tickers if item['symbol'] == sym)
                            if i ==0:
                                price1 = float(depth['bidPrice'])
                                qtt1 = float(depth['bidQty'])
                                exch_rate_list.append(price1)
                                qtt_rate_list.append(qtt1)
                                Exch_rate1 = currency_pair+ "Exchange Rate ['bids']: {}".format(depth['bidPrice']) +' '
                            if i ==2:
                                price3 = float(depth['bidPrice'])
                                exch_rate_list.append(price3)
                                qtt3 = float(depth['bidQty'])
                                qtt_rate_list.append(qtt3)
                                Exch_rate1 = currency_pair+ "Exchange Rate ['bids']: {}".format(depth['bidPrice']) +' '
                            print(Exch_rate1)
                        if i == 1:
                            depth = next(item for item in tickers if item['symbol'] == sym)
                            price2 = float(depth['askPrice'])
                            exch_rate_list.append(price2)
                            qtt2 = float(depth['askQty'])
                            qtt_rate_list.append(qtt2)
                            Exch_rate2 = currency_pair+"Exchange Rate ['asks']: {}".format(float(depth['askPrice']))+' '
                            print(Exch_rate2)
                        i+=1
                    else:
                        exch_rate_list.append(0)
                        
                print(exch_rate_list[3:])

run()