import numpy as np


# 例如：distance如下，start=0,end=2
# [[0 1 2]
#  [1 0 1]
#  [2 1 0]]
# 表示起点0，终点2的TSP问题，出去起点终点有一个过程点1 。d01=1,d02=2,d12=1。
# 返回值为a.ans=[total,s]
# 元组s(1,2)表示0-1-2路径(也就是说s[-1]=end；s[0]表示从起点0出发到1这条路径)
# 数值total=2表示共花2距离
class Tsp:

    def __init__(self,distance:np.ndarray,start:int,end:int):
        self.distance=distance
        self.start=start
        self.end=end
        self.dp={}#dp={State:[int,(int,int,int)表示路径] }
        v=list(range(len(self.distance)))
        v.remove(start)
        v.remove(end)
        v=tuple(v)
        stt=self.State(start,v)
        self.ans=self.solve(stt)

    # dp求解路线
    def solve(self,state):
        #如果包含，则返回计算结果
        if self.dp.keys().__contains__(state):
            return self.dp[state]

        if list(state.v)==[]:
            v=tuple([self.end])
            self.dp[state]=[self.distance[state.i][self.end],v]
            return self.dp[state]


        #dp(i,v)=min(ditance[i][k]+dp(k,v-k))
        def dp(sup):
            #print('dpdp')
            #state.show()
            return self.solve(self.new_state(state,sup))

        sup = list(state.v)[-1]
        for k in state.v:
            if self.distance[state.i][sup]+dp(sup)[0]>self.distance[state.i][k]+dp(k)[0]:
                sup=k

        self.dp[state]=[self.distance[state.i][sup]+dp(sup)[0],tuple([sup]+list(dp(sup)[1]))]
        return self.dp[state]

    def new_state(self, state_old, spot_remove):
        #state_old.show()
        state_new=self.State(spot_remove,state_old.v)
        state_new.v=tuple( set(state_new.v) - set([spot_remove]) )
        return state_new
    class State:
        def __init__(self,i:int,v:tuple):
            self.i=i
            self.v=v
        def show(self):
            print('当前处于节点',self.i)
            print('还待遍历节点',self.v)


sup=[[0,1,1,2],
     [1,0,3,1],
     [1,3,0,1],
     [2,1,1,0]]
distance_test=np.array(sup)
#如下所示：计算从0到1的TSP问题
a=Tsp(distance_test,0,1)
print(a.ans)



