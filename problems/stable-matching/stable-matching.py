PREFERENCES_FILE_NAME = 'preferences.txt'

def get_agent_preferences():
    agents1_pref = []
    agents2_pref = []
    
    with open(PREFERENCES_FILE_NAME) as f:
        agents1 = True
        for line in f:
            if len(line) < 2:
                agents1 = False
                continue
            
            if agents1:
                agents1_pref.append(list(map(int, line.split(' '))))
            else:
                agents2_pref.append(list(map(int, line.split(' '))))
    
    assert len(agents1_pref) == len(agents2_pref)
    assert len(agents1_pref) == len(agents1_pref[0])
    assert len(agents2_pref) == len(agents2_pref[0])
    
    return agents1_pref, agents2_pref

def match(agents1_pref, agents2_pref):
    not_decided_agents1 = list(range(len(agents1_pref)))
    agents1_pref_idx = [0] * len(agents1_pref)  # counting from the hightest to lowest preference of the agents (idx 0 = hightest pref., val = agent2)
    agents2_taken_by = [-1] * len(agents2_pref)  # which agent1 has taken agent2 (idx = agent2, val = assigned agent1)

    agents2_pref_inv = [[0] * len(agents1_pref) for i in range(len(agents1_pref))] # idx = agent1, val = pref
    for i in range(len(agents1_pref)):
        for j in range(len(agents1_pref)):
            agents2_pref_inv[i][agents2_pref[i][j]] = j
    
    while len(not_decided_agents1) != 0:
        agent = not_decided_agents1[0] # get any agent
        not_decided_agents1 = not_decided_agents1[1:]

        prefered_agent2 = agents1_pref[agent][agents1_pref_idx[agent]]
        agent1_assigned_to_pref_agent2 = agents2_taken_by[prefered_agent2]

        if agent1_assigned_to_pref_agent2 == -1:  # agent2 not taken
            agents2_taken_by[prefered_agent2] = agent
        # else if prefered agent2 taken AND taken agent2 prefers current agent1 to assigned agent1
        elif agent1_assigned_to_pref_agent2 != -1 and agents2_pref_inv[prefered_agent2][agent] < agents2_pref_inv[prefered_agent2][agent1_assigned_to_pref_agent2]:
            not_decided_agents1 = [agent1_assigned_to_pref_agent2] + not_decided_agents1
            agents2_taken_by[prefered_agent2] = agent
        else: # agent2 taken and prefers already assigned agent1 to current agent1
            not_decided_agents1 = [agent] + not_decided_agents1
        
        agents1_pref_idx[agent] += 1

    return agents2_taken_by


if __name__ == '__main__':
    agents1_pref, agents2_pref = get_agent_preferences()
    
    match_list = match(agents1_pref, agents2_pref)

    for i in range(len(match_list)):
        print("Agent1 Nr. {} assigned to Agent2 Nr. {}".format(match_list[i], i))
