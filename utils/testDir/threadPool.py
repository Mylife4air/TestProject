#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2017/12/21 0021 8:50
# @author  : zza
# @Email   : 740713651@qq.com
import json
import time

import math
import threadpool
import websocket

symbols = ['BCNBTC', 'BTCUSD', 'DASHBTC', 'DOGEBTC', 'DOGEUSD', 'DSHBTC', 'EMCBTC', 'ETHBTC', 'FCNBTC', 'LSKBTC',
           'LTCBTC',
           'LTCUSD', 'NXTBTC', 'QCNBTC', 'SBDBTC', 'SCBTC', 'STEEMBTC', 'XDNBTC', 'XEMBTC', 'XMRBTC', 'ARDRBTC',
           'ZECBTC',
           'WAVESBTC', 'MAIDBTC', 'AMPBTC', 'BUSBTC', 'DGDBTC', 'ICNBTC', 'SNGLSBTC', '1STBTC', 'XLCBTC', 'TRSTBTC',
           'TIMEBTC', 'GNOBTC', 'REPBTC', 'XMRUSD', 'DASHUSD', 'ETHUSD', 'NXTUSD', 'ZRCBTC', 'BOSBTC', 'DCTBTC',
           'ANTBTC',
           'AEONBTC', 'GUPBTC', 'PLUBTC', 'LUNBTC', 'TAASBTC', 'NXCBTC', 'EDGBTC', 'RLCBTC', 'SWTBTC', 'TKNBTC',
           'WINGSBTC',
           'XAURBTC', 'AEBTC', 'PTOYBTC', 'WTTBTC', 'ZECUSD', 'XEMUSD', 'BCNUSD', 'XDNUSD', 'MAIDUSD', 'ETCBTC',
           'ETCUSD',
           'CFIBTC', 'PLBTBTC', 'BNTBTC', 'XDNCOBTC', 'FYNETH', 'SNMETH', 'SNTETH', 'CVCUSD', 'PAYETH', 'OAXETH',
           'OMGETH',
           'BQXETH', 'XTZBTC', 'CRSUSD', 'DICEBTC', 'CFIETH', 'PTOYETH', '1STETH', 'XAURETH', 'TAASETH', 'TIMEETH',
           'DICEETH',
           'SWTETH', 'XMRETH', 'ETCETH', 'DASHETH', 'ZECETH', 'PLUETH', 'GNOETH', 'XRPBTC', 'NETETH', 'STRATUSD',
           'STRATBTC',
           'SNCETH', 'ADXETH', 'BETETH', 'EOSETH', 'DENTETH', 'SANETH', 'EOSBTC', 'EOSUSD', 'MNEBTC', 'MRVETH',
           'MSPETH',
           'DDFETH', 'XTZETH', 'XTZUSD', 'UETETH', 'MYBETH', 'SURETH', 'IXTETH', 'HRBETH', 'PLRETH', 'TIXETH', 'NDCETH',
           'PROETH', 'AVTETH', 'COSSETH', 'PBKXETH', 'PQTUSD', '8BTUSD', 'EVXUSD', 'IMLETH', 'ROOTSETH', 'DLTBTC',
           'BNTETH',
           'BNTUSD', 'QAUBTC', 'QAUETH', 'MANAUSD', 'DNTBTC', 'FYPBTC', 'OPTBTC', 'GRPHBTC', 'TNTETH', 'STXBTC',
           'STXETH',
           'STXUSD', 'TNTUSD', 'TNTBTC', 'CATBTC', 'CATETH', 'CATUSD', 'BCHBTC', 'BCHETH', 'BCHUSD', 'ECATETH',
           'XUCUSD',
           'SNCBTC', 'SNCUSD', 'OAXUSD', 'OAXBTC', 'BASETH', 'ZRXBTC', 'ZRXETH', 'ZRXUSD', 'RVTBTC', 'ICOSBTC',
           'ICOSETH',
           'ICOSUSD', 'PPCBTC', 'PPCUSD', 'QTUMETH', 'VERIBTC', 'VERIETH', 'VERIUSD', 'IGNISETH', 'PRGBTC', 'PRGETH',
           'PRGUSD', 'BMCBTC', 'BMCETH', 'BMCUSD', 'CNDBTC', 'CNDETH', 'CNDUSD', 'SKINBTC', 'EMGOBTC', 'EMGOUSD',
           'CDTETH',
           'CDTUSD', 'FUNBTC', 'FUNETH', 'FUNUSD', 'HVNBTC', 'HVNETH', 'FUELBTC', 'FUELETH', 'FUELUSD', 'POEBTC',
           'POEETH',
           'MCAPBTC', 'AIRBTC', 'AIRETH', 'AIRUSD', 'AMBUSD', 'AMBETH', 'AMBBTC', 'NTOBTC', 'ICOBTC', 'PINGBTC',
           'RKCETH',
           'GAMEBTC', 'TKRETH', 'HPCBTC', 'PPTETH', 'MTHBTC', 'MTHETH', 'WMGOBTC', 'WMGOUSD', 'LRCBTC', 'LRCETH',
           'ICXBTC',
           'ICXETH', 'NEOBTC', 'NEOETH', 'NEOUSD', 'CSNOBTC', 'ORMEBTC', 'ICXUSD', 'PIXBTC', 'PIXETH', 'INDETH',
           'KICKBTC',
           'YOYOWBTC', 'MIPSBTC', 'CDTBTC', 'XVGBTC', 'XVGETH', 'XVGUSD', 'DGBBTC', 'DGBETH', 'DGBUSD', 'DCNETH',
           'DCNUSD',
           'LATBTC', 'CCTETH', 'EBETETH', 'VIBEBTC', 'VOISEBTC', 'ENJBTC', 'ENJETH', 'ENJUSD', 'ZSCBTC', 'ZSCETH',
           'ZSCUSD',
           'ETBSBTC', 'TRXBTC', 'TRXETH', 'TRXUSD', 'VENBTC', 'VENETH', 'VENUSD', 'ARTBTC', 'EVXBTC', 'EVXETH',
           'QVTETH',
           'EBTCOLDBTC', 'EBTCOLDETH', 'EBTCOLDUSD', 'BKBBTC', 'EXNBTC', 'TGTBTC', 'ATSETH', 'UGTBTC', 'UGTETH',
           'UGTUSD',
           'CTRBTC', 'CTRETH', 'CTRUSD', 'BMTBTC', 'BMTETH', 'SUBBTC', 'SUBETH', 'SUBUSD', 'WTCBTC', 'CNXBTC', 'ATBBTC',
           'ATBETH', 'ATBUSD', 'ODNBTC', 'BTMBTC', 'BTMETH', 'BTMUSD', 'B2XBTC', 'B2XETH', 'B2XUSD', 'ATMBTC', 'ATMETH',
           'ATMUSD', 'LIFEBTC', 'VIBBTC', 'VIBETH', 'VIBUSD', 'DRTETH', 'STUUSD', 'HDGETH', 'OMGBTC', 'PAYBTC',
           'COSSBTC',
           'PPTBTC', 'SNTBTC', 'BTGBTC', 'BTGETH', 'BTGUSD', 'SMARTBTC', 'SMARTETH', 'SMARTUSD', 'XUCETH', 'XUCBTC',
           'CLBTC',
           'CLETH', 'CLUSD', 'LAETH', 'CLDBTC', 'CLDETH', 'CLDUSD', 'ELMBTC', 'EDOBTC', 'EDOETH', 'EDOUSD', 'HGTETH',
           'POLLBTC', 'IXTBTC', 'PREBTC', 'ATSBTC', 'SCLBTC', 'BCCBTC', 'BCCETH', 'BCCUSD', 'ATLBTC', 'EBTCNEWBTC',
           'EBTCNEWETH', 'EBTCNEWUSD', 'ETPBTC', 'ETPETH', 'ETPUSD', 'OTXBTC', 'CDXETH', 'DRPUBTC', 'NEBLBTC',
           'NEBLETH',
           'HACBTC', 'CTXBTC', 'CTXETH', 'ELEBTC', 'ARNBTC', 'ARNETH', 'SISABTC', 'SISAETH', 'STUBTC', 'STUETH',
           'GVTETH',
           'INDIBTC', 'BTXBTC', 'BTXUSDT', 'LTCETH', 'BCNETH', 'MAIDETH', 'NXTETH', 'STRATETH', 'XDNETH', 'XEMETH',
           'PLRBTC',
           'SURBTC', 'BQXBTC', 'DOGEETH', 'ITSBTC', 'AMMBTC', 'AMMETH', 'AMMUSD', 'DBIXBTC', 'PRSBTC', 'KBRBTC',
           'TBTBTC',
           'EROBTC', 'SMSBTC', 'SMSETH', 'SMSUSD', 'ZAPBTC', 'DOVBTC', 'DOVETH', 'FRDBTC', 'OTNBTC', 'CAPPBTC',
           'CAPPETH',
           'XRPETH', 'XRPUSDT', 'CAPPUSDT', 'HSRBTC', 'LENDBTC', 'LENDETH', 'SPFETH', 'LOCBTC', 'LOCETH', 'LOCUSD',
           'BTCABTC',
           'BTCAETH', 'BTCAUSD', 'WRCBTC', 'WRCETH', 'WRCUSD', 'SWFTCBTC', 'SWFTCETH', 'SWFTCUSD', 'SBTCBTC', 'SBTCETH',
           'STORMBTC', 'STARETH', 'SBTCUSDT']

x_space = 10
b = []
c = []
# symbols_list = [symbols[x * x_space:x * x_space + x_space] for x in range(int(math.floor(len(symbols) / x_space)))]
for i in range(0, len(symbols), x_space):
    b = symbols[i:i + x_space]
    c.append(b)

def quit():
    print('fuck you')

def sayhello(arg):
    str = arg.get("name")
    symbols = arg.get("symbols")
    try:

        print(str)
        print(symbols)

        def on_open(ws):
            for i in symbols:
                # d = {
                #     "method": "subscribeOrderbook",
                #     "params": {
                #         "symbol": i
                #     },
                #     "id": 123
                # }
                # ws.send(json.dumps(d))
                d = {
                    "method": "subscribeTrades",
                    "params": {
                        "symbol": i
                    },
                    "id": 123
                }
                ws.send(json.dumps(d))
                # d = {
                #     "method": "subscribeOrderbook",
                #     "params": {
                #         "symbol": i
                #     },
                #     "id": 123
                # }
                # ws.send(json.dumps(d))
            print(str + " finish send ")

        def on_message(ws, message):
            message = json.loads(message)
            print(str, ':', message)

        url = 'wss://api.hitbtc.com/api/2/ws'
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
        # ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=9999)
        ws.run_forever()

        print(str, 'death over' + '*' * 50)
    except Exception as e:
        print(str, e)


new_list = []
for i in range(len(c)):
    new_list.append({"name": 'thread ' + str(i), "symbols": c[i]})

# print(new_list)
pool = threadpool.ThreadPool(len(c))
requests = []
requests += threadpool.makeRequests(sayhello, new_list)
[pool.putRequest(req) for req in requests]
pool.wait()
print('over')



