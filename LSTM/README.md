### Time Series Forecasting : Extrapolation
Having known the level of association between the dependent and dependent variables from analysis about the passt, making predictions about the future, also known as `Extrapolation`, but lately refered to as `time series forecasting`. is possible.
This is truest especially in the classical statistical modelling of time series data.

This statistical Modelling involves taking models fit on historical data and using them to predict future observations(Of course based on previous Records)

Descriptive models can borrow for the future (i.e. to smooth or remove noise), they only seek to best describe the data.

### Long Short-Term Memory Network(LSTM-NN)
<hr>

Long Short-Term Memory (LSTM) networks are a type of [Recurrent Neural Network(RNN)](link_here) that are trained using [Back Propagation](link) using data over a long period of time and are capable of learning order dependence in sequence prediction problems.
- Their main advantage is to overcome the problem of `vanishing gradient problem` that was initially seen in old traditional ML models.

Having that in mind, LSTM can be `applicable` in complex problem domains e.g 
  * Machine translation
  * Speech recognition
  * High accuracy Weather Forecasting
  * More to achieve `state-of-the-art` results.



Instead of neurons, LSTM networks have memory blocks that are connected through layers as shown in the arch

A block has components that make it smarter than a classical neuron and a memory for recent sequences. A block contains gates that manage the block’s state and output. A block operates upon an input sequence and each gate within a block uses the sigmoid activation units to control whether they are triggered or not, making the change of state and addition of information flowing through the block conditional.