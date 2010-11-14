from itertools import product

pyramidal   = 4**9
cubic       = 6**6


die4    = [1,2,3,4]
die6    = [1,2,3,4,5,6]

peter   = [die4]*9
colin   = [die6]*6


ev_peter    = {}
for each in product(*peter):
    total   = sum(each)
    ev_peter[total] = ev_peter.get(total, 0) + 1

# Frequency distribution of expected value for Peter
evfd_peter   = dict((ev, float(c) / pyramidal) for (ev, c) in ev_peter.items())


ev_colin    = {}
for each in product(*colin):
    total   = sum(each)
    ev_colin[total] = ev_colin.get(total, 0) + 1

# Frequency distribution of expected value for Colin
evfd_colin  = dict((ev, float(c) / cubic) for (ev, c) in ev_colin.items())


p   = 0
for ev_peter in evfd_peter:
    for ev_colin in range(6, ev_peter):
        p_peter = evfd_peter[ev_peter]
        p_colin = evfd_colin[ev_colin]
        p   += p_peter * p_colin

print '%.7f' % p
