#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


states = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 
          's18', 's19', 's20', 's21', 's22', 's23']

actions = ['a1', 'a2', 'a3', 'a4'] #up, down, right, left

transition = {
    's1': {
        'a1': {'s1': 0.95, 's2': 0.05},
        'a2': {'s6': 0.8, 's2': 0.05, 's1': 0.15},
        'a3': {'s2': 0.8, 's1': 0.15, 's6': 0.05},
        'a4': {'s1': 0.95, 's6': 0.05}
    },
    's2': {
        'a1': {'s2': 0.9, 's3': 0.05, 's1': 0.05},
        'a2': {'s7': 0.8, 's3': 0.05, 's1': 0.05, 's2': 0.1},
        'a3': {'s3': 0.8, 's2': 0.15, 's7': 0.05},
        'a4': {'s1': 0.8, 's2': 0.15, 's7': 0.05}
    },
    's3': {
        'a1': {'s3': 0.9, 's4': 0.05, 's2': 0.05},
        'a2': {'s8': 0.8, 's4': 0.05, 's2': 0.05, 's3': 0.1},
        'a3': {'s4': 0.8, 's3': 0.15, 's8': 0.05},
        'a4': {'s2': 0.8, 's3': 0.15, 's8': 0.05}
    },
    's4': {
        'a1': {'s4': 0.9, 's5': 0.05, 's3': 0.05},
        'a2': {'s9': 0.8, 's5': 0.05, 's3': 0.05, 's4': 0.1},
        'a3': {'s5': 0.8, 's4': 0.15, 's9': 0.05},
        'a4': {'s3': 0.8, 's4': 0.15, 's9': 0.05}
    },
    's5': {
        'a1': {'s5': 0.95, 's4': 0.05},
        'a2': {'s10': 0.8, 's5': 0.15, 's4': 0.05},
        'a3': {'s5': 0.95, 's10': 0.05},
        'a4': {'s4': 0.8, 's5': 0.15, 's10': 0.05}
    },
    's6': {
        'a1': {'s1': 0.8, 's7': 0.05, 's6': 0.15},
        'a2': {'s11': 0.8, 's7': 0.05, 's6': 0.15},
        'a3': {'s7': 0.8, 's1': 0.05, 's11': 0.05, 's6': 0.1},
        'a4': {'s6': 0.9, 's1': 0.05, 's11': 0.05}
    },
    's7': {
        'a1': {'s2': 0.8, 's8': 0.05, 's6': 0.05, 's7': 0.1},
        'a2': {'s12': 0.8, 's8': 0.05, 's6': 0.05, 's7': 0.1},
        'a3': {'s8': 0.8, 's2': 0.05, 's12': 0.05, 's7': 0.1},
        'a4': {'s6': 0.8, 's2': 0.05, 's12': 0.05, 's7': 0.1}
    },
    's8': {
        'a1': {'s3': 0.8, 's9': 0.05, 's7': 0.05, 's8': 0.1},
        'a2': {'s8': 0.9, 's9': 0.05, 's7': 0.05},
        'a3': {'s9': 0.8, 's3': 0.05, 's8': 0.15},
        'a4': {'s7': 0.8, 's3': 0.05, 's8': 0.15}
    },
    's9': {
        'a1': {'s4': 0.8, 's10': 0.05, 's8': 0.05, 's9': 0.1},
        'a2': {'s13': 0.8, 's10': 0.05, 's8': 0.05, 's9': 0.1},
        'a3': {'s10': 0.8, 's4': 0.05, 's13': 0.05, 's9': 0.1},
        'a4': {'s8': 0.8, 's4': 0.05, 's13': 0.05, 's9': 0.1}
    },
    's10': {
        'a1': {'s5': 0.8, 's10': 0.15, 's9': 0.05},
        'a2': {'s14': 0.8, 's10': 0.15, 's9': 0.05},
        'a3': {'s10': 0.9, 's5': 0.05, 's14': 0.05},
        'a4': {'s9': 0.8, 's5': 0.05, 's14': 0.05, 's10': 0.1}
    },
    's11': {
        'a1': {'s6': 0.8, 's12': 0.05, 's11': 0.15},
        'a2': {'s15': 0.8, 's12': 0.05, 's11': 0.15},
        'a3': {'s12': 0.8, 's6': 0.05, 's15': 0.05, 's11': 0.1},
        'a4': {'s11': 0.9, 's6': 0.05, 's15': 0.05}
    },
    's12': {
        'a1': {'s7': 0.8, 's12': 0.15, 's11': 0.05},
        'a2': {'s16': 0.8, 's12': 0.15, 's11': 0.05},
        'a3': {'s12': 0.9, 's7': 0.05, 's16': 0.05},
        'a4': {'s11': 0.8, 's7': 0.05, 's16': 0.05, 's12': 0.1}
    },
    's13': {
        'a1': {'s9': 0.8, 's14': 0.05, 's13': 0.15},
        'a2': {'s17': 0.8, 's14': 0.05, 's13': 0.15},
        'a3': {'s14': 0.8, 's9': 0.05, 's17': 0.05, 's13': 0.1},
        'a4': {'s13': 0.9, 's9': 0.05, 's17': 0.05}
    },
    's14': {
        'a1': {'s10': 0.8, 's14': 0.15, 's13': 0.05},
        'a2': {'s18': 0.8, 's14': 0.15, 's13': 0.05},
        'a3': {'s14': 0.9, 's10': 0.05, 's18': 0.05},
        'a4': {'s13': 0.8, 's10': 0.05, 's18': 0.05, 's14': 0.1}
    },
    's15': {
        'a1': {'s11': 0.8, 's16': 0.05, 's15': 0.15},
        'a2': {'s19': 0.8, 's16': 0.05, 's15': 0.15},
        'a3': {'s16': 0.8, 's11': 0.05, 's19': 0.05, 's15': 0.1},
        'a4': {'s15': 0.9, 's11': 0.05, 's19': 0.05}
    },
    's16': {
        'a1': {'s12': 0.8, 's16': 0.15, 's15': 0.05},
        'a2': {'s20': 0.8, 's16': 0.15, 's15': 0.05},
        'a3': {'s16': 0.9, 's12': 0.05, 's20': 0.05},
        'a4': {'s15': 0.8, 's12': 0.05, 's20': 0.05, 's16': 0.1}
    },
    's17': {
        'a1': {'s13': 0.8, 's18': 0.05, 's17': 0.15},
        'a2': {'s22': 0.8, 's18': 0.05, 's17': 0.15},
        'a3': {'s18': 0.8, 's13': 0.05, 's22': 0.05, 's17': 0.1},
        'a4': {'s17': 0.9, 's13': 0.05, 's22': 0.05}
    },
    's18': {
        'a1': {'s14': 0.8, 's18': 0.15, 's17': 0.05},
        'a2': {'s23': 0.8, 's18': 0.15, 's17': 0.05},
        'a3': {'s18': 0.9, 's14': 0.05, 's23': 0.05},
        'a4': {'s17': 0.8, 's14': 0.05, 's23': 0.05, 's18': 0.1}
    },
    's19': {
        'a1': {'s15': 0.8, 's20': 0.05, 's19': 0.15},
        'a2': {'s19': 0.95, 's20': 0.05},
        'a3': {'s20': 0.8, 's15': 0.05, 's19': 0.15},
        'a4': {'s19': 0.95, 's15': 0.05}
    },
    's20': {
        'a1': {'s16': 0.8, 's21': 0.05, 's19': 0.05, 's20': 0.1},
        'a2': {'s20': 0.9, 's21': 0.05, 's19': 0.05},
        'a3': {'s21': 0.8, 's16': 0.05, 's20': 0.15},
        'a4': {'s19': 0.8, 's16': 0.05, 's20': 0.15}
    },
    's21': {
        'a1': {'s21': 0.9, 's22': 0.05, 's20': 0.05},
        'a2': {'s21': 0.9, 's22': 0.05, 's20': 0.05},
        'a3': {'s22': 0.8, 's21': 0.2},
        'a4': {'s20': 0.8, 's21': 0.2}
    },
    's22': {
        'a1': {'s17': 0.8, 's23': 0.05, 's21': 0.05, 's22': 0.1},
        'a2': {'s22': 0.9, 's23': 0.05, 's21': 0.05},
        'a3': {'s23': 0.8, 's17': 0.05, 's22': 0.15},
        'a4': {'s21': 0.8, 's17': 0.05, 's22': 0.15}
    },
    's23': {
        'a1': {'s23': 0},
        'a2': {'s23': 0},
        'a3': {'s23': 0},
        'a4': {'s23': 0}
    }
}

reward = {
    's1': {
        'a1': {'s1': 0, 's2': 0},
        'a2': {'s6': 0, 's2': 0, 's1': 0},
        'a3': {'s2': 0, 's1': 0, 's6': 0},
        'a4': {'s1': 0, 's6': 0}
    },
    's2': {
        'a1': {'s2': 0, 's3': 0, 's1': 0},
        'a2': {'s7': 0, 's3': 0, 's1': 0, 's2': 0},
        'a3': {'s3': 0, 's2': 0, 's7': 0},
        'a4': {'s1': 0, 's2': 0, 's7': 0}
    },
    's3': {
        'a1': {'s3': 0, 's4': 0, 's2': 0},
        'a2': {'s8': 0, 's4': 0, 's2': 0, 's3': 0},
        'a3': {'s4': 0, 's3': 0, 's8': 0},
        'a4': {'s2': 0, 's3': 0, 's8': 0}
    },
    's4': {
        'a1': {'s4': 0, 's5': 0, 's3': 0},
        'a2': {'s9': 0, 's5': 0, 's3': 0, 's4': 0},
        'a3': {'s5': 0, 's4': 0, 's9': 0},
        'a4': {'s3': 0, 's4': 0, 's9': 0}
    },
    's5': {
        'a1': {'s5': 0, 's4': 0},
        'a2': {'s10': 0, 's5': 0, 's4': 0},
        'a3': {'s5': 0, 's10': 0},
        'a4': {'s4': 0, 's5': 0, 's10': 0}
    },
    's6': {
        'a1': {'s1': 0, 's7': 0, 's6': 0},
        'a2': {'s11': 0, 's7': 0, 's6': 0},
        'a3': {'s7': 0, 's1': 0, 's11': 0, 's6': 0},
        'a4': {'s6': 0, 's1': 0, 's11': 0}
    },
    's7': {
        'a1': {'s2': 0, 's8': 0, 's6': 0, 's7': 0},
        'a2': {'s12': 0, 's8': 0, 's6': 0, 's7': 0},
        'a3': {'s8': 0, 's2': 0, 's12': 0, 's7': 0},
        'a4': {'s6': 0, 's2': 0, 's12': 0, 's7': 0}
    },
    's8': {
        'a1': {'s3': 0, 's9': 0, 's7': 0, 's8': 0},
        'a2': {'s8': 0, 's9': 0, 's7': 0},
        'a3': {'s9': 0, 's3': 0, 's8': 0},
        'a4': {'s7': 0, 's3': 0, 's8': 0}
    },
    's9': {
        'a1': {'s4': 0, 's10': 0, 's8': 0, 's9': 0},
        'a2': {'s13': 0, 's10': 0, 's8': 0, 's9': 0},
        'a3': {'s10': 0, 's4': 0, 's13': 0, 's9': 0},
        'a4': {'s8': 0, 's4': 0, 's13': 0, 's9': 0}
    },
    's10': {
        'a1': {'s5': 0, 's10': 0, 's9': 0},
        'a2': {'s14': 0, 's10': 0, 's9': 0},
        'a3': {'s10': 0, 's5': 0, 's14': 0},
        'a4': {'s9': 0, 's5': 0, 's14': 0, 's10': 0}
    },
    's11': {
        'a1': {'s6': 0, 's12': 0, 's11': 0},
        'a2': {'s15': 0, 's12': 0, 's11': 0},
        'a3': {'s12': 0, 's6': 0, 's15': 0, 's11': 0},
        'a4': {'s11': 0, 's6': 0, 's15': 0}
    },
    's12': {
        'a1': {'s7': 0, 's12': 0, 's11': 0},
        'a2': {'s16': 0, 's12': 0, 's11': 0},
        'a3': {'s12': 0, 's7': 0, 's16': 0},
        'a4': {'s11': 0, 's7': 0, 's16': 0, 's12': 0}
    },
    's13': {
        'a1': {'s9': 0, 's14': 0, 's13': 0},
        'a2': {'s17': 0, 's14': 0, 's13': 0},
        'a3': {'s14': 0, 's9': 0, 's17': 0, 's13': 0},
        'a4': {'s13': 0, 's9': 0, 's17': 0}
    },
    's14': {
        'a1': {'s10': 0, 's14': 0, 's13': 0},
        'a2': {'s18': 0, 's14': 0, 's13': 0},
        'a3': {'s14': 0, 's10': 0, 's18': 0},
        'a4': {'s13': 0, 's10': 0, 's18': 0, 's14': 0}
    },
    's15': {
        'a1': {'s11': 0, 's16': 0, 's15': 0},
        'a2': {'s19': 0, 's16': 0, 's15': 0},
        'a3': {'s16': 0, 's11': 0, 's19': 0, 's15': 0},
        'a4': {'s15': 0, 's11': 0, 's19': 0}
    },
    's16': {
        'a1': {'s12': 0, 's16': 0, 's15': 0},
        'a2': {'s20': 0, 's16': 0, 's15': 0},
        'a3': {'s16': 0, 's12': 0, 's20': 0},
        'a4': {'s15': 0, 's12': 0, 's20': 0, 's16': 0}
    },
    's17': {
        'a1': {'s13': 0, 's18': 0, 's17': 0},
        'a2': {'s22': 0, 's18': 0, 's17': 0},
        'a3': {'s18': 0, 's13': 0, 's22': 0, 's17': 0},
        'a4': {'s17': 0, 's13': 0, 's22': 0}
    },
    's18': {
        'a1': {'s14': 0, 's18': 0, 's17': 0},
        'a2': {'s23': 10, 's18': 0, 's17': 0},
        'a3': {'s18': 0, 's14': 0, 's23': 10},
        'a4': {'s17': 0, 's14': 0, 's23': 10, 's18': 0}
    },
    's19': {
        'a1': {'s15': 0, 's20': 0, 's19': 0},
        'a2': {'s19': 0, 's20': 0},
        'a3': {'s20': 0, 's15': 0, 's19': 0},
        'a4': {'s19': 0, 's15': 0}
    },
    's20': {
        'a1': {'s16': 0, 's21': -10, 's19': 0, 's20': 0},
        'a2': {'s20': 0, 's21': -10, 's19': 0},
        'a3': {'s21': -10, 's16': 0, 's20': 0},
        'a4': {'s19': 0, 's16': 0, 's20': 0}
    },
    's21': {
        'a1': {'s21': -10, 's22': 0, 's20': 0},
        'a2': {'s21': -10, 's22': 0, 's20': 0},
        'a3': {'s22': 0, 's21': -10},
        'a4': {'s20': 0, 's21': -10}
    },
    's22': {
        'a1': {'s17': 0, 's23': 10, 's21': -10, 's22': 0},
        'a2': {'s22': 0, 's23': 10, 's21': -10},
        'a3': {'s23': 10, 's17': 0, 's22': 0},
        'a4': {'s21': -10, 's17': 0, 's22': 0}
    },
    's23': {
        'a1': {'s23': 0},
        'a2': {'s23': 0},
        'a3': {'s23': 0},
        'a4': {'s23': 0}
    }
}
value2={
    's1': 0,
    's2': 0,
    's3': 0,
    's4': 0,
    's5': 0,
    's6': 0,
    's7': 0,
    's8': 0,
    's9': 0,
    's10': 0,
    's11': 0,
    's12': 0,
    's13': 0,
    's14': 0,
    's15': 0,
    's16': 0,
    's17': 0,
    's18': 0,
    's19': 0,
    's20': 0,
    's21': 0,
    's22': 0,
    's23': 0
}
policy2={
    's1': 0,
    's2': 0,
    's3': 0,
    's4': 0,
    's5': 0,
    's6': 0,
    's7': 0,
    's8': 0,
    's9': 0,
    's10': 0,
    's11': 0,
    's12': 0,
    's13': 0,
    's14': 0,
    's15': 0,
    's16': 0,
    's17': 0,
    's18': 0,
    's19': 0,
    's20': 0,
    's21': 0,
    's22': 0,
    's23': 0
}
gamma = 0.25

def value_iteration2(gamma, value2, reward, transition, states, actions, policy2):
    for i in range(10000):
        delta = 0.0
        
        for state in states:
            if state == 's23':
                continue
            # print('state before', value1[state], 'state', state)
            initial_v = value2[state]
            max_action = None
            max_value = float('-inf')

            for action in transition[state]:
                action_value = 0.0
                for next_state in transition[state][action]:
                    action_value += transition[state][action][next_state] * (reward[state][action][next_state] + gamma * value2[next_state])

                if action_value > max_value:
                    max_value = action_value
                    max_action = action

            value2[state] = max_value
            policy2[state] = max_action
            # print('state after', value1[state], 'state', state)
            
            delta = max(delta, abs(initial_v - value2[state]))
        
        if delta < 0.0001:
            print('Iteration number:', i+1)
            print('\n')
            break
    return policy2, value2

policy2, value2 = value_iteration2(gamma, value2, reward, transition, states, actions, policy2)

rounded_value2 = {key: round(value, 4) for key, value in value2.items()}

# print(policy1)
# print(rounded_value1)

matrix_order = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10',
                's11', 's12', '0.0000', 's13', 's14', 's15', 's16', '0.0000', 's17', 's18',
                's19', 's20', 's21', 's22', 's23']

print('Value Function')

# Print the dictionary as a 5x5 matrix
for i in range(0, 25, 5):
    row = matrix_order[i:i + 5]
    for key in row:
        if key not in rounded_value2:
            print('0.0000', end='\t')
        else:
            print(f"{rounded_value2[key]:.4f}", end='\t')
    print()
print('\n')    
print('Policy')

up_arrow = '\u2191'
down_arrow = '\u2193'
right_arrow = '\u2192'
left_arrow = '\u2190'

for i in range(0, 25, 5):
    row = matrix_order[i:i + 5]
    for key in row:
        if key not in policy2:
            print(' ', end='\t')
        else:
            if policy2[key] == 'a1':
                print(f"{up_arrow}", end='\t')
            elif policy2[key] == 'a2':
                print(f"{down_arrow}", end='\t')
            elif policy2[key] == 'a3':
                print(f"{right_arrow}", end='\t')
            elif policy2[key] == 'a4':
                print(f"{left_arrow}", end='\t')
            else:
                print("G", end='\t')
    print()


# In[ ]:




