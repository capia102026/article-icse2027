#!/usr/bin/env python3
"""Recomputes the agreement statistics of the paper from ratings/*.csv (standard library only).
Usage: python3 scripts/analyze.py   (run from the repository root)"""
import csv, itertools, math
def rd(p): return list(csv.DictReader(open(p, encoding='utf-8')))
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n; c = p + z*z/(2*n); h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return round(100*(c-h)/d), round(100*(c+h)/d)
def cohen(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b))/n
    pe = sum((a.count(c)/n)*(b.count(c)/n) for c in set(a)|set(b))
    return float('nan') if pe == 1 else (po-pe)/(1-pe)
def fleiss(rows):
    N = len(rows); n = len(rows[0]); cats = sorted({x for r in rows for x in r})
    pj = {c: sum(r.count(c) for r in rows)/(N*n) for c in cats}
    Pi = [(sum(r.count(c)**2 for c in cats)-n)/(n*(n-1)) for r in rows]
    Pe = sum(v*v for v in pj.values()); Pb = sum(Pi)/N
    return float('nan') if Pe == 1 else (Pb-Pe)/(1-Pe)
C = ['unambiguous', 'verifiable', 'singular']

print('== PANEL (21 candidates x 3 criteria, Y/Partial/N, three categories, pooled) ==')
P = rd('ratings/panel_ratings_E1_E4.csv'); ev = sorted({r['evaluator'] for r in P}); ids = sorted({r['candidate'] for r in P})
g = {(r['evaluator'], r['candidate']): [r[c] for c in C] for r in P}
pool = {e: [x for i in ids for x in g[(e, i)]] for e in ev}
for a, b in itertools.combinations(ev, 2): print(f'Cohen {a}-{b}: {cohen(pool[a], pool[b]):+.2f}')
print('Fleiss pooled:', f"{fleiss([[pool[e][k] for e in ev] for k in range(63)]):+.3f}")
for j, c in enumerate(C): print('Fleiss', c, f"{fleiss([[g[(e, i)][j] for e in ev] for i in ids]):+.3f}")
appr = {e: sum(all(x == 'Y' for x in g[(e, i)]) for i in ids) for e in ev}; print('Approved on all three, per evaluator:', appr)
maj = [i for i in ids if sum(all(x == 'Y' for x in g[(e, i)]) for e in ev) >= 3]; print('Majority (>=3 of 4) on all three:', len(maj), maj)

print('\n== V03 (15 candidates) ==')
V = rd('ratings/v03_ratings.csv'); cands = sorted({r['candidate'] for r in V})
for r_ in ('R1', 'A', 'B'):
    k = sum(r['approved_all_three'] == 'Y' for r in V if r['rater'] == r_); print(r_, f'approved {k}/15 ({round(100*k/15)}%, CI {wilson(k,15)})')
ap = {r_: [1 if next(r for r in V if r['rater'] == r_ and r['candidate'] == c)['approved_all_three'] == 'Y' else 0 for c in cands] for r_ in ('R1', 'A', 'B')}
for a, b in itertools.combinations(ap, 2): print(f'Cohen approval {a}-{b}: {cohen(ap[a], ap[b]):+.2f}')
print('Fleiss approval (3 raters):', f"{fleiss([[ap['R1'][i], ap['A'][i], ap['B'][i]] for i in range(15)]):+.2f}")
ab = {r_: {r['candidate']: r for r in V if r['rater'] == r_} for r_ in ('A', 'B')}
for c in C: print('A x B', c, f"{cohen([ab['A'][i][c] for i in cands], [ab['B'][i][c] for i in cands]):+.2f}")
print('Fully faithful A/B:', sum(ab['A'][i]['fidelity'] == 'Faithful' for i in cands), sum(ab['B'][i]['fidelity'] == 'Faithful' for i in cands),
      '| kappa A-B:', f"{cohen([ab['A'][i]['fidelity'] for i in cands], [ab['B'][i]['fidelity'] for i in cands]):+.2f}")
at = {r_: [1 if next(r for r in V if r['rater'] == r_ and r['candidate'] == c)['actor_shift'] == 'Y' else 0 for c in cands] for r_ in ('R1', 'A', 'B')}
print('Actor shift R1/A/B:', {k: sum(v) for k, v in at.items()}, '| majority >=2 of 3:', sum(sum(at[r_][i] for r_ in at) >= 2 for i in range(15)))

print('\n== V06 baseline (20 items; rater answers Y/Partial/N; blank excluded) ==')
B = rd('ratings/v06_baseline_ratings.csv'); it = sorted({r['item'] for r in B})
a = {r['item']: r['already_in_first_3_responses'] for r in B if r['rater'] == 'A'}; b = {r['item']: r['already_in_first_3_responses'] for r in B if r['rater'] == 'B'}
both = [i for i in it if a[i] != '(blank)' and b[i] != '(blank)']
k = sum(a[i] == 'N' and b[i] == 'N' for i in both); print(f'both "N": {k}/{len(both)} ({round(100*k/len(both))}%, CI {wilson(k,len(both))}); Cohen {cohen([a[i] for i in both],[b[i] for i in both]):+.2f}')
