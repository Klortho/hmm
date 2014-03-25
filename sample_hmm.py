import hmm

s1 = hmm.state(
    'S1',            # name of the state
    0.5,             # probability of being the initial state
    { '1': 0.5,      # probability of emitting a '1' at each visit
      '2': 0.5 },    # probability of emitting a '2' at each visit
    { 'S1': 0.9,     # probability of transitioning to itself
      'S2': 0.1 }    # probability of transitioning to state 'S2'
)
s2 = hmm.state(
    'S2', 0.5,
    { '1': 0.25, '2': 0.75 },
    { 'S1': 0.8, 'S2': 0.2 }
)
model = hmm.hmm(['1', '2'],  # all symbols that can be emitted
                [s1, s2])    # all of the states in this HMM

model.enumerate('222')


path, prob = model.viterbi_path('222')
print path
print prob
