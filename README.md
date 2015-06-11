# Off-policy experiments evaluating WIS-based O(n) algorithms (Mahmood & Sutton 2015)

This project contains random MDP experiments evaluating the usage-based step-size adaptation idea (Mahmood & Sutton 2015) applied to true online TD (TOTD) (van Seijen & Sutton 2014) and TD with accumulating traces (TD) (Sutton & Barto 1998).

This project can be imported as an Eclipse Pydev project.

In order to run the random-walk Markov chain experiment and generate plot, execute `run-stdrw-sparse-experiments.sh`.

In order to run the experiment on the randomly generated MDP with 10 state and generate plot, execute `run-offrndmdp-experiments10.sh`.

In order to run the experiment on the randomly generated MDP with 10 state and generate plot, execute `run-offrndmdp-experiments100.sh`.

#References

Mahmood, A. R., Sutton, R. S. (2015). Off-policy learning based on weighted importance sampling with linear computational complexity. In Proceedings of the 31st Conference on Uncertainty in Artificial Intelligence, Amsterdam, Netherlands.
