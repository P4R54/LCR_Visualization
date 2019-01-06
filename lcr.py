import datk
import pdb
from collections import OrderedDict
import json
rounds = []
nodes = []
nr = []
steps = dict()
def new_output(self, process, key, value):
	global nr
	global MAX_NODES
	#print (process)
	if len(rounds) == 0:
		rounds.append(self.r)
	if rounds[-1] != self.r:
		nodes.append(nr)
		nr = []
		rounds.append(self.r)
		if self.r == 10:
			nodes.append(nr)
	nr.append(str(process).replace("P" , ""))
	#pdb.set_trace()
	#print(process, key, value)

def trans_ii(self, p, msgs):
	if len(msgs) == 0:
            self.set(p,"send", None)
        else:
            msg = msgs.pop()
            if msg.content == p.UID:
                self.output(p,"status", "leader")
                #print (p.UID , msg.content)
                steps[p.UID] = msg.content
            elif msg.content > p.UID:
                self.set(p,"send", msg)
                if not self.has(p, "decided"):
                    self.set(p, "decided", None)
                    self.output(p,"status", "non-leader")
		    #print (p.UID , msg.content)
		    steps[p.UID] = msg.content
            else:
                self.set(p, "send",  None)
        if self.r == p.state['n']: p.terminate(self)

datk.core.distalgs.Algorithm.output = new_output
datk.core.algs.LCR.trans_i = trans_ii

def run_lcr():
	global nodes , nr , rounds
	nodes = []
	rounds = []
	nr = []
	x = datk.Unidirectional_Ring(10)
	lcr = datk.LCR(x)
	kk = {}
	for i in range(len(rounds)):
		#print rounds[i] , nodes[i]
		kk[rounds[i]] = nodes[i]
	return kk , str(x) , steps
