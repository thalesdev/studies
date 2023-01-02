

class HiddenMarkovModel:
    def __init__(self, model_name="Hidden Markov Model", states = (), p_trans = {}, p_start = {}, p_emit = {}):
        self.name = model_name
        self.states = states
        self.p_trans = p_trans
        self.p_emit = p_emit
        self.p_init = p_start
        self._obs = []
        print("Markov model has been created.")
    
    def __min_p(self, values):
        return False
        """
        l = []
        try:
            for k,v in values.items():
                if iter(v) != None:
                    for val in v:
                        if issubclass(val, float) or  issubclass(val, int):
                            l.append(val)
                        else:
                            return False
            return len([l_ for l_ in l if l_ > 0]) != len(l)  
        except:
            return False"""

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, value):
            self._states = value
    
    @property
    def p_trans(self):
        return self._p_trans
    
    @p_trans.setter
    def p_trans(self, value):
        if self.__min_p(value):
            raise Exception("Deve informar uma Matriz De Transação REGULAR!")
        else:
            self._p_trans = value
    
    @property
    def p_emit(self):
        return self._p_emit
    
    @p_emit.setter
    def p_emit(self, value):
        if self.__min_p(value):
            raise Exception("Deve informar uma Matriz De Emissão REGULAR!")
        else:
            self._p_emit = value
    
    @property
    def p_init(self):
        return self._p_init
    
    @p_init.setter
    def p_init(self, value):
        if self.__min_p(value):
            raise Exception("Deve informar um estado inicial VALIDO!")
        else:
            self._p_init = value

    def assign(self, obs):
        for ob in obs:
            c = 0
            for em in self.p_emit.values():
                if ob in list(em.keys()):
                    c+=1
                    break
            if c == 0:
                raise Exception("O Simbolo observado não faz parte do modelo!")
        self._obs = obs
    
    def viterbi(self):
        v = [{}]
        for state in self.states:
            v[0][state] = {"p": self.p_init[state] * self.p_emit[state][obs[0]], "prev" : None}
       # print(self.p_trans[self.states[0]]['Viciada'])
        for t in range(1, len(self._obs)):
            v.append({})
            for state in self.states:
                max_prob_trans = v[t-1][self.states[0]]["p"]*self.p_trans[self.states[0]][state]
                prev_st_selected = self.states[0]

                for prev_st in states[1:]:
                    trans_prob = v[t-1][prev_st]["p"]*self._p_trans[prev_st][state]
                    if trans_prob < max_prob_trans:
                        max_prob_trans = trans_prob
                        prev_st_selected = prev_st
                v[t][state] = {"p": max_prob_trans, "prev": prev_st_selected}
        
        print(v[len(self._obs)-1])
        return 1,1
if __name__ == "__main__":
    states = ("Viciada", "Normal")
    p_trans = {
        "Viciada": {
            "Viciada" : 0.9,
            "Normal": 0.1
        },
        "Normal": {
            "Viciada" : 0.9,
            "Normal": 0.1
        }
    }
    p_init = {
        "Viciada": 0.5,
        "Normal" : 0.5
    }
    p_emit = {
        "Normal":
        {
            "CARA": 0.5,
            "COROA": 0.5 
        },
        "Viciada":{
            "CARA": 0.75,
            "COROA": 0.25
        }
    }
    obs = [
        "CARA", "COROA","COROA","CARA","CARA","CARA","COROA"
    ]
    mkdemo = HiddenMarkovModel("Testinho Hidden Model",
        states=states,
        p_trans = p_trans,
        p_start = p_init,
        p_emit = p_emit
    )
    mkdemo.assign(obs)
    viterbi_path, probs = mkdemo.viterbi()
    #print(mkdemo.__dict__)
