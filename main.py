# !/usr/bin/env python
# -*- coding:utf-8 -*-
#
# ==============================================
# ·
# · Author: A wang
# ·
# · Albert.mj.wang@gmail.com
# ·
# · Filename: af.py
# ·
# · COPYRIGHT 2018
# ·
# ==============================================

# - paraments ... ---------------------------------------------------------------
RunTimes=10000
AgentNumber=100
MsgNameLen=15
AgentTimeUnit=1
FieldTimeUnit=1
msgname0="---------------"
msgname1="..............."
msgname2="..............."
msgname3="..............."
msgname4="..............."
msgname5="..............."
AgentList={}
#...


# - classes ... -----------------------------------------------------------------
class Basis():
    def __init__(self, name="Basis_Process"):
        self._Name, self._Messages = name, dict()

    def put_MSG(self, name, value=None):
        self._Messages[name] = value

    def len_MSG(self):
        return len(self._Messages)

    def get_MSG(self): #FIFO
        return self._Messages.popitem(0)

    def clr_MSG():
        self._Messages.clear()


class Field(Basis):
    def __init__(self, name="Field"):
        Basis.__init__(self, name)
        self.InMessage  = []
        self.OutMessage = []

    def run(self):
        while True:    # The main loop of the 'Field'
            while self.len_MSG() > 0:
                self.InMessage = self.get_MSG()
                if self.InMessage[0][0:MsgNameLen]==msgname1:
                    #...
                elif self.InMessage[0][0:MsgNameLen]==msgname2:
                    #...
                else: print "!!Wrong Msg:", self.name, self.InMessage

            for self.i in random_range(AgentNumber):
                self.OutMessage=[...]
                AgentList[self.i].put_MSG(msgname3+"%015d"%randint(1,999999999999999),self.OutMessage)
                self.OutMessage=[...]
                AgentList[self.i].put_MSG(msgname4+"%015d"%randint(1,999999999999999),self.OutMessage)
                self.OutMessage=[...]
                AgentList[self.i].put_MSG(msgname5+"%015d"%randint(1,999999999999999),self.OutMessage)


class Agent(Basis):
    def __init__(self, name="Agent", myid=0):
        Basis.__init__(self, name)
        self.InMessage = []
        self.OutMessage = []

    def run(self):
        while True: # the main loop of each worker(Agent)...
            # the Delta function (state transition):
            # clear the accumulators here.

            if self.InMessage[0][0:MsgNameLen]==msgname3 and ...:
                #...
            elif self.InMessage[0][0:MsgNameLen]==msgname4 and ...:
                #...
            elif self.InMessage[0][0:MsgNameLen]==msgname4 and ...:
                #...
            elif self.InMessage[0][0:MsgNameLen]==msgname5:
                #...
            else: print "!!Wrong Msg:", self.id, self.InMessage

            # the Omega function (output messages):
            self.OutMessage = [...]
            if ...: AIOshoper.put_MSG(msgname1+"%015d"%randint(1,999999999999999), self.OutMessage)
            self.OutMessage = [...]
            if ...: AIOshoper.put_MSG(msgname2+"%015d"%randint(1,999999999999999), self.OutMessage)
