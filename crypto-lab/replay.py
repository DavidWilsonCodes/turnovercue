import argparse, csv, math
from dataclasses import dataclass

@dataclass
class Bar:
    ts: str; o: float; h: float; l: float; c: float; v: float

def load_csv(path):
    out=[]
    with open(path,newline='',encoding='utf-8') as f:
        for r in csv.DictReader(f):
            out.append(Bar(r['timestamp'],*[float(r[k]) for k in ['open','high','low','close','volume']]))
    return out

def ema(xs,n):
    a=2/(n+1); y=[]; e=None
    for x in xs:
        e=x if e is None else a*x+(1-a)*e; y.append(e)
    return y

def atr(bars,n=14):
    tr=[]
    for i,b in enumerate(bars):
        pc=bars[i-1].c if i else b.c
        tr.append(max(b.h-b.l,abs(b.h-pc),abs(b.l-pc)))
    return ema(tr,n)

def max_dd(curve):
    peak=curve[0]; m=0
    for x in curve:
        peak=max(peak,x); m=max(m,(peak-x)/peak if peak else 0)
    return m

def run(bars,strategy,cash=100,fee=.0005,slippage=.0005,leverage=1):
    closes=[b.c for b in bars]; e20,e50,e200=ema(closes,20),ema(closes,50),ema(closes,200); a=atr(bars)
    equity=cash; pos=None; trades=[]; curve=[equity]
    for i in range(205,len(bars)-1):
        b,nxt=bars[i],bars[i+1]
        if pos:
            side,entry,qty,stop,target,entry_i=pos; exit_px=None; reason=None
            if side==1:
                if nxt.l<=stop: exit_px=stop*(1-slippage); reason='stop'
                elif nxt.h>=target: exit_px=target*(1-slippage); reason='target'
                elif strategy=='swing_v1' and b.c<e50[i]: exit_px=nxt.o*(1-slippage); reason='ema_exit'
            else:
                if nxt.h>=stop: exit_px=stop*(1+slippage); reason='stop'
                elif nxt.l<=target: exit_px=target*(1+slippage); reason='target'
            if exit_px:
                gross=(exit_px-entry)*qty*side; fees=(abs(entry*qty)+abs(exit_px*qty))*fee
                equity+=gross-fees; trades.append((bars[entry_i].ts,nxt.ts,side,entry,exit_px,gross-fees,reason)); pos=None
        if not pos and equity>0:
            look=bars[i-20:i]; hi=max(x.h for x in look); lo=min(x.l for x in look)
            up=b.c>e20[i]>e50[i]>e200[i]; dn=b.c<e20[i]<e50[i]<e200[i]
            long_sig=up and b.c>hi; short_sig=strategy!='swing_v1' and dn and b.c<lo
            if long_sig or short_sig:
                side=1 if long_sig else -1; entry=nxt.o*(1+slippage*side); dist=max(1.5*a[i],entry*.005)
                stop=entry-dist*side; target=entry+2.5*dist*side
                risk={'swing_v1':.02,'aggressive_v1':.08,'extreme_v1':.20}[strategy]
                qty=min((equity*risk/dist)*leverage,(equity*leverage)/entry)
                pos=(side,entry,qty,stop,target,i+1)
        mark=equity+(0 if not pos else (b.c-pos[1])*pos[2]*pos[0]); curve.append(max(mark,0))
    wins=[t[5] for t in trades if t[5]>0]; losses=[-t[5] for t in trades if t[5]<0]
    pf=sum(wins)/sum(losses) if losses else (math.inf if wins else 0)
    return {'start_cash':cash,'final_equity':round(equity,4),'net_pnl':round(equity-cash,4),'trades':len(trades),'win_rate':round(len(wins)/len(trades),4) if trades else 0,'profit_factor':round(pf,4) if math.isfinite(pf) else 'inf','max_drawdown':round(max_dd(curve),4)}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--csv',required=True); p.add_argument('--strategy',choices=['swing_v1','aggressive_v1','extreme_v1'],default='aggressive_v1'); p.add_argument('--cash',type=float,default=100); p.add_argument('--fee',type=float,default=.0005); p.add_argument('--slippage',type=float,default=.0005); p.add_argument('--leverage',type=float,default=1)
    a=p.parse_args(); print(run(load_csv(a.csv),a.strategy,a.cash,a.fee,a.slippage,a.leverage))
